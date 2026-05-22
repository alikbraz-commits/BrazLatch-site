---
description: Full pre-launch sequence — audit, apply BLOCKER/FIX items, sanity-check, deploy to Netlify, verify production. Stops between phases for Alik's confirmation.
---

You are about to take the BrazLatch site live. This command coordinates
the agent team. Move through phases in order. **Stop after each phase and
get Alik's explicit "continue" before the next.**

## Phase 1 — Audit

Invoke the `brand-and-audit` subagent:

> Run the full pre-launch audit and produce the punch list. We're heading
> to production after this, so be strict about [BLOCKER] severity.

Present the punch list to Alik. Ask:

> Pre-launch audit results above. Continue to Phase 2 (apply BLOCKER + FIX
> items)? Or do you want to address anything manually first?

**Wait for "continue" / "go" / "yes".**

## Phase 2 — Apply fixes

For each [BLOCKER] and [FIX] in the punch list:

- If marked "self-applied" by brand-and-audit: ask brand-and-audit to apply it.
- If marked "handed to site-builder": delegate to the `site-builder` subagent
  with the exact file paths, line numbers, and before/after content.
- If marked "needs Alik's input": ask Alik directly and apply what he says.

Skip [POLISH] items in this phase — they're for later iterations.

After fixes land, ask brand-and-audit:

> Re-audit only the items we touched. Confirm BLOCKER and FIX items are
> resolved.

Show the confirmation. Ask:

> All fixes verified. Continue to Phase 3 (pre-deploy sanity check)?

**Wait for confirmation.**

## Phase 3 — Pre-deploy sanity check

Invoke the `site-builder` subagent:

> Run the pre-deploy sanity check. Report file count, total size, last
> commit, missing assets, and any uncommitted changes.

Show the report. Ask:

> Sanity check above. Continue to Phase 4 (Netlify deploy)?

**Wait for confirmation.**

## Phase 4 — Deploy

Confirm `netlify` CLI is available:
```
which netlify || echo "missing"
```
If missing, tell Alik to run `npm install -g netlify-cli` and `netlify login`, then resume.

If the site isn't linked yet:
```
netlify status
```
If no linked site, prompt Alik to `netlify init` first (creates the site
or links an existing one). Recommend linking to the existing `brazlatch.com`
Netlify site if one exists, rather than creating a new one.

Deploy:
```
netlify deploy --dir=. --prod
```

Capture the production URL Netlify returns.

## Phase 5 — Verify production

Run these checks against the deployed URL (use the URL Netlify returned,
or `https://brazlatch.com` if the custom domain is already attached):

1. **Reachability** — `curl -sI {url}` returns 200.
2. **HTTPS valid** — `curl -sI {url}` returns 200 and no SSL warnings.
3. **Homepage size** — `curl -s {url} | wc -c` returns ≥ 15 KB.
4. **Critical assets** — fetch `/css/styles.css`, `/js/main.js`,
   `/assets/img/logo.svg`, `/assets/video/brazlatch-triple-action.mp4` and
   confirm 200 + non-zero size.
5. **Form** — load the homepage and grep for
   `name="distributor-inquiry"` and `data-netlify="true"`. Confirm both
   present.
6. **Security headers** — `curl -sI {url}` includes
   `Strict-Transport-Security`, `X-Frame-Options`, `Referrer-Policy`.
7. **www redirect** — if domain is brazlatch.com, `curl -sI https://www.brazlatch.com`
   should return 301 to the apex.

Append to `.claude/deploy-log.md`:
```
## {ISO date}
- URL: {production url}
- Commit: {short sha}  {commit message}
- Files: {n} files, {size} total
- Audit blockers cleared: {count}
- All verification checks: {PASS|FAIL}
```

## Phase 6 — Domain setup (only if first launch on brazlatch.com)

If `netlify status` showed no custom domain yet:

1. Show Alik the DNS records he needs to add at his domain registrar
   (Netlify provides these in **Domain settings → Add custom domain**).
2. After he adds them, run `netlify domains:list` and confirm
   `brazlatch.com` is attached.
3. Trigger Netlify's automatic Let's Encrypt cert provisioning if it didn't
   fire automatically.
4. Verify `https://brazlatch.com` resolves with a valid certificate.

See `.claude/runbooks/domain-setup.md` for the full walkthrough.

## Final report

```
═══ BRAZLATCH IS LIVE ═══
URL:           {production url}
Verified at:   {timestamp}
Blockers:      0 remaining
Fixes:         0 remaining
Polish items:  {n} deferred — see audit log
Next:          {anything Alik should do manually, e.g. configure form
                notifications, set up Slack alert, etc.}
```
