# Good morning, Alik 👋

Two big things to wake up to:

1. **Site is launch-ready** — one command to deploy (below).
2. **18 real outbound prospects** researched, scored, and ranked in a
   Google-Sheets-ready CSV. Saddleworld (AU, 30+ stores, 10/10),
   Naylors Equestrian (UK, 46 stores, 10/10), Maanvi Exports (India,
   8/10) lead each territory. See
   `brazlatch-site/.claude/prospects/ranked.csv` and the import doc at
   `brazlatch-site/.claude/prospects/IMPORT-TO-GOOGLE-SHEETS.md`.

---

## What was finished while you slept

Everything in `brazlatch-site/` was audited and polished. The full audit
log is at the bottom of this document. Highlights:

- **Copy** — fixed the typo in the Stalls card ("The pitch products" →
  "Other latches pop open when a horse leans on the door"). Rewrote the
  awkward second paragraph of the About section into three clean
  paragraphs in your voice ("sophisticated simplicity", workshop in
  Mikhmoret, etc.). No marketing-ese.
- **SEO** — meta description trimmed to 150 chars, canonical link added,
  Twitter card meta added, OG locale + image dimensions added.
- **Structured data** — added JSON-LD for Organization + Product + WebSite.
  Three entities, validates cleanly. This is what Google reads to show
  rich results.
- **Accessibility** — honeypot field hidden from screen readers
  (`aria-hidden="true"`, `tabindex="-1"`, `autocomplete="off"`).
  All use-case icons got explicit width/height to prevent layout shift,
  plus `loading="lazy"` and `decoding="async"`.
- **Performance** — hero video switched to `preload="metadata"` so the
  page renders fast (downloads metadata only, plays when ready). Logo
  and footer logo also `decoding="async"`.

Total site size: 12.7 MB, all assets resolve, HTML structurally balanced,
CSS braces balanced, JSON-LD parses, meta description ≤ 160 chars,
canonical present.

---

## Your ONE command to go live

Make sure Node 18+ is installed (https://nodejs.org if not), then open
PowerShell in the project folder and run:

```powershell
cd "C:\Users\alikb\OneDrive\Tiedostot\2026\rooftrainer\pic\webflow\brazlatch-site"
npm install -g netlify-cli
netlify login                       # one-time, browser will open
netlify init                        # one-time, pick "Create & configure a new site", call it "brazlatch"
netlify deploy --dir=. --prod
```

That's it. Netlify will give you a URL like `https://brazlatch-12345.netlify.app`.
Open it. The site is live.

### Then point brazlatch.com at it

In the Netlify dashboard (it'll open automatically after `netlify init`):

1. **Domain management → Add a domain → `brazlatch.com`**
2. Pick **"Set up Netlify DNS"** (easiest path).
3. Netlify gives you 4 nameservers — copy them.
4. Go to your domain registrar (wherever you bought brazlatch.com) and
   replace the nameservers with the 4 from Netlify.
5. Wait 5–60 minutes for DNS to propagate.
6. Netlify auto-provisions the HTTPS certificate. Visit
   https://brazlatch.com — it's live.

Full step-by-step (including troubleshooting and the "keep DNS at my
current provider" alternate path) is in
`brazlatch-site/.claude/runbooks/domain-setup.md`.

---

## Why I couldn't run the deploy myself

The deploy needs YOUR Netlify account credentials and YOUR domain
registrar login. Both live on your computer and your accounts, not in
this Cowork sandbox. That single step needs your hands. Everything
else — every file, every audit, every fix — is done.

---

## What's still optional / can wait

These were on the original list but aren't blocking launch:

- **Real patent numbers** — currently the Patents section says "Issued"
  for all six countries. When you have the actual patent numbers (e.g.
  US 11,448,003 B2), tell Claude Code "/audit then update the patent
  numbers" and the brand-and-audit + site-builder agents will handle it.
- **Slide-12 product photos + slide-2 family photos** from
  `BrazLatch28-08.pptx` — file never landed. Drop the .pptx into the
  project folder and the agent team will extract and wire them in.
- **Baby & Kids real PNG icon** — currently rendered as an inline SVG
  in the same green-circle style as the other 6 icons. Looks consistent.
  Swap when you have a proper PNG.

None of these are launch-blockers. Ship the site first; iterate later.

---

## The agent team is ready

After deploy, when you open Claude Code in `brazlatch-site/`, you have:

- **`/inquiries`** — triage new distributor form submissions
- **`/reply <id>`** — draft a personalized reply in your voice
- **`/pipeline-report`** — weekly digest
- **`/audit`** — re-run the launch audit anytime
- **`/deploy`** — pre-flight + production push
- **`/go-live`** — the full audit → fix → deploy → verify sequence

The agents (`site-builder`, `brand-and-audit`, `distributor-manager`)
will auto-route based on what you ask. See
`brazlatch-site/.claude/AGENTS.md` for the full overview.

---

## Full audit log

### ▶ Brand & copy
- `[BLOCKER]` #B1 — Stalls card: "The pitch products" → "Other latches pop open when a horse leans on the door." **APPLIED.**
- `[FIX]`     #B2 — About paragraph 2 rewrite (clean voice, no awkward phrasing). **APPLIED.**
- `[POLISH]`  #B3 — ® symbol audit. Currently appears once, in footer. **OK as-is.**

### ▶ Accessibility
- `[BLOCKER]` #A1 — Honeypot field exposed to screen readers. Added `aria-hidden="true"`, `tabindex="-1"`, `autocomplete="off"`. **APPLIED.**
- `[POLISH]`  #A2 — Explicit lang attributes. `<html lang="en">` already set. **OK as-is.**

### ▶ SEO
- `[FIX]` #S1 — Meta description was 187 chars. Trimmed to 150. **APPLIED.**
- `[FIX]` #S2 — `<link rel="canonical">`. **ADDED.**
- `[FIX]` #S3 — Organization + Product + WebSite JSON-LD. **ADDED.**
- `[FIX]` #S4 — Twitter card meta (`twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`). **ADDED.**
- `[FIX]` #S5 — `og:locale`, `og:image:width`, `og:image:height`, `og:image:alt`, `og:site_name`. **ADDED.**
- `[FIX]` #S6 — Explicit `<meta name="robots" content="index,follow">`. **ADDED.**

### ▶ Performance
- `[FIX]` #P1 — All 6 use-case icons + footer logo: `width`, `height`, `loading="lazy"`, `decoding="async"`. **APPLIED.**
- `[FIX]` #P2 — Header logo `decoding="async"`. **APPLIED.**
- `[FIX]` #P3 — Hero video `preload="auto"` → `preload="metadata"`. **APPLIED.**

**Punch list cleared: 12 of 12 [BLOCKER] and [FIX] items.**

---

## Files changed overnight

- `brazlatch-site/index.html` — meta tags, JSON-LD, copy fixes, accessibility, performance attributes
- `brazlatch-site/.claude/` — added the agent team and runbooks (already there from your earlier session, just confirming)
- `GOOD-MORNING.md` — this file

The original outputs folder (Cowork's scratchpad) still holds the
pre-edit version of the site if you ever want to diff.

Sleep well. Coffee in the morning, deploy in five minutes.

— overnight agent
