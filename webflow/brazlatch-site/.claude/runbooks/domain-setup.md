# Runbook — point brazlatch.com at the Netlify site

One-time setup. After this, every `/deploy` ships to brazlatch.com automatically.

## 0. Prerequisites

- You own `brazlatch.com` at a registrar (GoDaddy, Namecheap, Cloudflare,
  Google Domains, etc.).
- A Netlify site exists for this project. If not, run `netlify init` from
  inside `brazlatch-site/` first and pick "Create & configure a new site".
- The Netlify CLI is logged in: `netlify login`.

## 1. Add the custom domain in Netlify

```
netlify open
```

In the Netlify dashboard for this site:
**Site configuration → Domain management → Add a domain →** type
`brazlatch.com`.

Netlify will offer two options:

### Option A — let Netlify manage DNS (simplest)

1. Click "Set up Netlify DNS for brazlatch.com".
2. Netlify shows 4 nameservers (e.g. `dns1.p01.nsone.net`, …).
3. At your domain registrar, replace the existing nameservers with these
   4 Netlify nameservers.
4. Propagation: 1 minute to 24 hours. Usually under an hour.
5. Netlify auto-provisions a Let's Encrypt cert once DNS resolves.

### Option B — keep DNS at your current provider

1. At your registrar's DNS panel, add:
   - **A record** for `@` (apex) → `75.2.60.5` (Netlify load balancer IP)
   - **CNAME** for `www` → `your-site-name.netlify.app`
2. Or the modern, recommended way: an **ALIAS / ANAME** record for the
   apex pointing to `apex-loadbalancer.netlify.com` (use this if your
   registrar supports it — Cloudflare, DNSimple, Namecheap "ALIAS").
3. In Netlify dashboard, click "Verify DNS configuration" once propagated.
4. Click "Provision SSL certificate" (Let's Encrypt) once DNS verifies.

Recommend Option A unless you have other services on `brazlatch.com` (like
a separate email host's MX records) that you don't want to migrate.

## 2. Configure the www → apex redirect

Already handled — see `netlify.toml`:

```toml
[[redirects]]
  from = "https://www.brazlatch.com/*"
  to   = "https://brazlatch.com/:splat"
  status = 301
  force  = true
```

If you prefer `www` as the primary (most modern sites use apex; some old
SEO advice still says www) flip the from/to.

In the Netlify dashboard: **Domain management → Domains** — set
`brazlatch.com` as the **primary domain** (or `www.brazlatch.com` if you
went the other way).

## 3. Force HTTPS

**Site configuration → Domain management → HTTPS →** toggle on
"Force HTTPS redirects". Netlify will 301 all http://… → https://… traffic.

## 4. Verify

```
curl -sI https://brazlatch.com | head -5
curl -sI http://brazlatch.com  | head -5
curl -sI https://www.brazlatch.com | head -5
```

Expected:
- `https://brazlatch.com` → `HTTP/2 200`
- `http://brazlatch.com`  → `HTTP/1.1 301` with `Location: https://brazlatch.com/`
- `https://www.brazlatch.com` → `HTTP/2 301` with `Location: https://brazlatch.com/`

## 5. Hook up form notifications

In Netlify dashboard: **Forms → distributor-inquiry → Settings & usage →
Form notifications**. Add:

- **Email notification** to `alik@brazlatch.com` for every submission.
- *(Optional)* **Slack webhook** if you want pings in Slack.
- *(Optional)* **Outgoing webhook** if you want them auto-piped to a CRM.

Test by submitting the form from `https://brazlatch.com/#distributors`.

## 6. Tell the distributor-manager agent where to find new inquiries

The agent expects `.claude/inquiries/submissions.csv`. Two options:

**Manual export (simplest):** every week, in Netlify, Forms →
distributor-inquiry → Export CSV → save into `.claude/inquiries/submissions.csv`.

**Automated (better):** install the Netlify CLI and `jq`, then add this
to `.claude/inquiries/refresh.sh`:

```bash
#!/usr/bin/env bash
set -e
FORM_ID=$(netlify api listForms --data='{}' | jq -r '.[] | select(.name=="distributor-inquiry") | .id')
netlify api listFormSubmissions --data="{\"form_id\":\"$FORM_ID\"}" > .claude/inquiries/submissions.json
echo "Refreshed at $(date)"
```

Then in Claude Code: `bash .claude/inquiries/refresh.sh` before `/inquiries`.
(Or let me bake that into the `/inquiries` command if you want — say the word.)

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `DNS_PROBE_FINISHED_NXDOMAIN` after switching nameservers | DNS hasn't propagated yet | Wait 1–24 h. Check with `dig brazlatch.com NS @1.1.1.1` |
| "No HTTPS cert provisioned" after 30 min | DNS not pointing at Netlify yet | Re-verify DNS in dashboard; ensure A or ALIAS record is correct |
| Form submissions don't appear in Netlify dashboard | Form name mismatch or `data-netlify` missing | Confirm `<form name="distributor-inquiry" data-netlify="true">` in `index.html` |
| Mixed-content warning | Asset linked over `http://` | Should never happen — all our assets are relative. If it does, run `grep -r 'http://' index.html` |
