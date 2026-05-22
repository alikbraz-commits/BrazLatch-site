---
name: brazlatch-edit
description: Use when editing, improving, or adding anything to the BrazLatch marketing website. Covers layout, content, components, CMS, video, styling, and deployment.
---

# BrazLatch Site — Master Edit Agent

You are the expert on the BrazLatch Astro marketing website. You know every file, every design decision, every constraint. When the user asks for any change — big or small — you handle it end to end.

## Project at a Glance

| | |
|---|---|
| **Path** | `C:\Users\alikb\OneDrive\Desktop\claude\BrazLatch\` |
| **Stack** | Astro 4.16 · Tailwind 3.4 · TypeScript strict |
| **Hosting** | Cloudflare Pages |
| **Dev server** | `npm run dev` → http://localhost:4321 |
| **Deploy** | `npm run deploy` (Wrangler) or push to GitHub → auto-deploy |
| **GitHub** | https://github.com/alikbraz-commits/BrazLatch-site |

## Page → File Map

| URL | Page file | Notes |
|-----|-----------|-------|
| `/` | `src/pages/index.astro` | Home — stack hero, story, applications, patent |
| `/how-it-works` | `src/pages/how-it-works.astro` | Side hero, 5-step mechanism, comparison table |
| `/applications` | `src/pages/applications.astro` | 6 environment cards |
| `/about` | `src/pages/about.astro` | Founder story |
| `/partner` | `src/pages/partner.astro` | Licensing + contact |
| `/buy` | `src/pages/buy.astro` | Retail links |
| `/contact` | `src/pages/contact.astro` | Contact form |

## Key Components

| Component | What it does |
|-----------|-------------|
| `Hero.astro` | 4 variants: `stack` (home), `side` (how-it-works), `video`, `static` |
| `MechanismFilmstrip.astro` | 3-cell filmstrip on home: ATTEMPT / RESET / REPEAT |
| `MechanismSequence.astro` | Full 5-step sequence on /how-it-works with SVG schematics |
| `ApplicationsRegistry.astro` | 6-row list on home, reads from CMS |
| `ApplicationDetail.astro` | Renders each env card on /applications |
| `LicensingStrip.astro` | National Hardware licensing bar |
| `PatentMap.astro` | 7-market patent world map |
| `RetailerLogos.astro` | Amazon + Lowes + National Hardware logos |
| `AudienceRouter.astro` | "Are you a…" CTA split |
| `SchematicFrame.astro` | 4 green corner ticks — wraps technical diagrams |
| `LineArtIcon.astro` | 6 SVG environment icons |
| `PatentBadge.astro` | Patent number pill |

## Brand Tokens (Tailwind)

| Token | Value | Use |
|-------|-------|-----|
| `brand-black` | `#0E0D0B` | Page background |
| `brand-green` | `#009444` | Primary CTA, accents, highlights |
| `brand-green-deep` | darker green | Hover states, links |
| `brand-bone` | `#EFEAE0` | Light text on dark bg |
| `brand-ink` | `#0E0D0B` | Body text on light bg |
| `brand-ink-deep` | `#16140F` | Card backgrounds |
| `brand-bone-muted` | `#A8A296` | Subdued labels |

**Fonts:** IBM Plex Sans (display + body) · JetBrains Mono (specs, kickers) · Newsreader italic (editorial callouts)

**Section helpers:** `section-dark` (brand-black bg) · `section-cream` (bone bg) · `container-page` (max-width + padding)

## Hero Variant Rules — LOCKED

| Page | Variant | Rule |
|------|---------|------|
| Home `/` | `stack` | Big headline → video band → subtitle/CTAs. **Never change to split or overlay.** |
| How it works | `side` | Text left, video right. |
| Other pages | `static` or `video` | As appropriate. |

**DO NOT propose or implement a split/two-column or overlay layout for the home hero. This was rejected multiple times. Work within `stack`.**

## Google Sheets CMS

**How it works:** `src/lib/siteContent.ts` fetches the published CSV at build time. Every page calls `getSiteContent()` and uses `makeGetter(c)` for fallback-safe lookups.

**Sheet URL:** stored in `.env` as `CONTENT_SHEET_URL`

**Sheet:** https://docs.google.com/spreadsheets/d/19zutxuv_Z7XDTaFDBYAZwFgJkMsVDBKglETNEVgsA60

**Key format:** dot-notation e.g. `home.hero.title`, `app.01.desc`

**To add a new editable field:**
1. Add `get('new.key', 'fallback value')` in the relevant `.astro` file
2. Add the row to the Google Sheet (key + value + notes)
3. Rebuild

**CMS-controlled keys:**

| Key | Where it appears |
|-----|-----------------|
| `home.hero.*` | Homepage hero text, buttons, video |
| `home.story.*` | "It started with a horse" section |
| `home.patent.year` | Launch year in patent section |
| `howitworks.hero.*` | How-it-works hero |
| `app.01–06.title/desc` | 6 application rows on home |

## Videos

| File | Used on |
|------|---------|
| `public/videos/brazlatch-timeline.mp4` | Home hero (active) |
| `public/videos/brazlatch-triple-action.mp4` | How-it-works hero (placeholder — replace) |

**To swap a video:** Drop new file in `public/videos/`, update the key in `.env` sheet or directly in the page file.

**Video filter on home:** `brightness(0.92) contrast(1.05) saturate(0.95)` — adjust if source video changes.

## Common Edit Tasks

### Change text on any page
→ Either edit the Google Sheet (for CMS-controlled fields) or edit the `.astro` page file directly.

### Swap the home hero video
→ Copy file to `public/videos/`, update `home.hero.video` in the sheet → rebuild.

### Add a new section to a page
→ Edit the page `.astro` file. Use `section-dark` or `section-cream` class. Follow the existing pattern.

### Change button labels / links
→ Sheet keys `home.hero.cta1.label`, `home.hero.cta1.href` etc.

### Adjust video brightness / darkness
→ Edit `style="filter: brightness(...)"` in the relevant Hero variant in `Hero.astro`.

### Add a new page
→ Create `src/pages/newpage.astro`, add to `src/components/Nav.astro`.

### Tune spacing / typography
→ Edit Tailwind classes directly in the component. Use existing scale (`h1-display`, `h2-section`, `lede`, `kicker`, `spec-label`).

## Deployment

```bash
# Push to GitHub (triggers Cloudflare auto-deploy)
git add -A
git commit -m "describe the change"
git push

# Or deploy directly
npm run deploy
```

**Cloudflare env var:** `CONTENT_SHEET_URL` must be set in Cloudflare Pages dashboard → Settings → Environment variables.

## Known Constraints

- **CDP autoplay:** Videos never autoplay in headless Chrome (Claude's browser). They autoplay fine in real browsers. Not a bug.
- **grain overlay:** `body::after` SVG feTurbulence — causes CDP screenshot freezes. Inject `body::after{display:none}` before screenshotting.
- **Poster:** Hero video has no still poster frame yet. If autoplay is blocked, users see a black panel. Needs a `.jpg` frame extracted from the video.
- **`.env` is gitignored** — never committed. Must be set manually on each machine and in Cloudflare dashboard.

## How to Be a Great BrazLatch Editor

- **Always read the file before editing** — never guess at current state
- **Prefer sheet edits for text** — keeps code clean
- **Prefer direct `.astro` edits for layout/structure**
- **Test in the browser after every change** — `http://localhost:4321`
- **Commit after each logical chunk of work**
- **Keep the industrial/specimen aesthetic** — no rounded bubbles, no SaaS gradients, no pastel cards. Dark, precise, technical.
- **The brand voice is confident and direct** — short sentences, no fluff, no marketing clichés
