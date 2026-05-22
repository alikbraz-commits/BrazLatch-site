# BrazLatch — project context for Claude Code

## What this is

Static marketing + lead-gen website for **BrazLatch**, a patent-protected
triple-action latch sold worldwide. Audience: international B2B
distributors. Deployed on Netlify at `brazlatch.com`.

## The business in one paragraph

BrazLatch is a self-locking latch with a sequential triple-action release
mechanism. Patented in US, Canada, EU, UK, Australia, Israel. Already sold
through Ajustco (EU/Canada), National Hardware (US), Lowe's, and Amazon.
Founder: **Alik Braz**, 4th-generation horse breeder from Mikhmoret,
Israel. He's actively looking for exclusive distributors in **Australia &
NZ**, **UK & EU** (territories outside the Ajustco footprint), and **India**.

## Repo layout

```
brazlatch-site/
├── CLAUDE.md            ← you are here
├── README.md            ← deploy instructions, brand tokens
├── index.html           ← 8-section homepage
├── thanks.html          ← post-submit page
├── css/styles.css
├── js/main.js
├── assets/
│   ├── img/             ← logo SVGs, posters, 7 use-case icons
│   └── video/           ← brazlatch-triple-action.mp4, alik-ajustco.mp4
├── netlify.toml
├── robots.txt
├── sitemap.xml
└── .claude/
    ├── agents/distributor-manager.md   ← project subagent
    ├── commands/                       ← /inquiries, /reply, /deploy
    ├── templates/replies/              ← territory-specific reply templates
    └── inquiries/                      ← inquiry log (CSV/JSON)
```

## Brand tokens (single source of truth: `css/styles.css`)

| Token              | Value     | Use                              |
|--------------------|-----------|----------------------------------|
| `--green`          | `#7ED957` | Primary brand accent             |
| `--green-deep`     | `#5BB237` | Hover, kickers                   |
| `--ink`            | `#1a1a1a` | Default text                     |
| `--soft`           | `#f6f8f6` | Alternate section background     |
| `--dark`           | `#0f1411` | Distributor form section         |
| Font               | Poppins   | All weights from Google Fonts    |

## Section anchors in `index.html`

`#what` · `#uses` · `#how` · `#patents` · `#markets` · `#about` · `#distributors`

## The distributor inquiry form

- Lives in `index.html` under `<section id="distributors">`
- Netlify-managed: `name="distributor-inquiry"`, honeypot field `bot-field`
- Fields: name, company, email, phone, country, territory, channels, message
- On submit → redirects to `/thanks.html`
- New submissions appear in Netlify dashboard → Forms → `distributor-inquiry`
- **Where Claude should pull them from**: either the Netlify API
  (`netlify api listFormSubmissions`) or the Netlify dashboard CSV export
  saved into `.claude/inquiries/submissions.csv`

## Deployment

- Static, no build step.
- Deploy: `netlify deploy --dir=. --prod` from inside `brazlatch-site/`
  (or drag-drop to https://app.netlify.com/drop).
- See `netlify.toml` for security headers and the www → apex redirect.

## What needs to come from Alik (not yet in repo)

- `BrazLatch28-08.pptx` — source PowerPoint (referenced by Cowork session,
  never uploaded). May contain slide-2 family photos and slide-12 product
  photography we'd want in About / What-is sections.
- A real "Baby & Kids" use-case PNG (currently rendered as an inline SVG
  placeholder matching the green-circle icon style).
- The actual 6 patent numbers + filing dates for the Patents section
  (currently labelled "Issued" without numbers).

## The agent team

Three specialist subagents own different slices of the project. See
`.claude/AGENTS.md` for the full guide. Quick summary:

- **`site-builder`** — code and assets (HTML/CSS/JS, photos, videos)
- **`brand-and-audit`** — words, claims, accessibility, SEO; produces
  punch lists, hands fixes to site-builder
- **`distributor-manager`** — Netlify form inquiry pipeline (triage,
  reply drafts in Alik's voice, status tracking)

You usually don't invoke them by name — Claude routes work automatically.
You can call them explicitly via the slash commands below.

## Common Alik-asks Claude Code should handle smoothly

1. **"Take the site live"** → `/go-live` (the full audit → fix → deploy
   → verify sequence; stops between phases for your confirmation).
2. **"Audit the site before launch"** → `/audit` (just the audit pass —
   no fixes applied without your go-ahead).
3. **"Any new distributor enquiries?"** → `/inquiries` (the
   distributor-manager triages and ranks them).
4. **"Draft a reply to the Australian guy"** → `/reply <id>` (composes a
   personalized response using `.claude/templates/replies/au-nz.md`).
5. **"Push the site live"** → `/deploy` (the lower-level deploy command;
   used by `/go-live` internally).
6. **"Add a new product photo"** → drop the image in `assets/img/`,
   tell Claude where it should slot in — site-builder + frontend-design
   handle the integration.
7. **"Update the patents list"** → site-builder updates the
   `country-grid` `<ul>`; brand-and-audit verifies the wording is clean.

## Tone for outbound communication to distributors

Match Alik's voice: **direct, practical, founder-led**. He's a 4th-gen
horse breeder and a mechanical inventor — not a marketing exec. Keep
emails short, mention the product detail he cares about (triple-action,
self-locking, sequence-only release), include one specific question that
lets the prospect prove they're serious. Sign as "Alik" (not "the team").

## Plugins expected to be active

- `superpowers` — agentic dev methodology
- `gsd` — get-stuff-done framework
- `claude-mem` — persistent memory across sessions
- `context-mode` — context-window optimization
- `frontend-design` — design quality for HTML/CSS edits

If any are missing, run the install block from `../install-claude-code-skills.md`.

## Cowork → Claude Code handoff history

Initial build done in Cowork mode. All assets, code, and deploy config
came over as-is. This file (`CLAUDE.md`) and `.claude/` were added at
the handoff. The Cowork transcript covered:
- HTML/CSS/JS build of 8 sections
- Logo SVG recreation (`assets/img/logo.svg` + `logo-light.svg` + `favicon.svg`)
- Video conversion (`Alik ajustco final.mov` 103 MB → `alik-ajustco.mp4` 11.8 MB)
- Netlify form wiring + `/thanks.html`
- Netlify.toml security headers + www → apex redirect
