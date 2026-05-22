---
name: brazlatch-edit
description: Use when editing, improving, or adding anything to the BrazLatch marketing website. Covers layout, content, components, CMS, video, styling, and deployment.
---

# BrazLatch Site — Master Edit Agent

You are the expert on the BrazLatch Astro marketing website. Every time this skill is invoked, you follow the intake workflow below before touching any file.

---

## Step 1 — Intake (ALWAYS run this first)

Before doing anything, ask the user these questions using the AskUserQuestion tool:

**Question 1 — What type of change?** (single select)
- Text / wording — headline, paragraph, button label
- Image or video — swap a photo or video file
- Layout or design — move things, resize, add a section
- New feature or page — something that doesn't exist yet
- Bug fix — something broken or looking wrong
- Deploy — push changes live

**Question 2 — Which page(s)?** (multi-select)
- Home (`/`)
- How it works (`/how-it-works`)
- Applications (`/applications`)
- About (`/about`)
- Partner (`/partner`)
- Buy (`/buy`)
- Contact (`/contact`)
- All pages / shared component

**Question 3 — How urgent / how big?** (single select)
- Quick fix — one thing, do it now
- Medium — a few related changes
- Big improvement — rethink a whole section

Then based on answers, follow the matching workflow below.

---

## Step 2 — Route to the Right Workflow

### TEXT CHANGE → Use the CMS first
1. Check if the field already exists in the sheet key list below
2. If YES → tell the user to update the Google Sheet cell. Done. No code needed.
3. If NO → add `get('new.key', 'fallback')` to the relevant `.astro` file, tell user to add the row to the sheet

### IMAGE / VIDEO SWAP
1. Ask: "Do you have the new file ready? What's the filename or URL?"
2. If local file → confirm it's in `public/videos/` or `public/images/`
3. If external URL → update the sheet key directly
4. Edit the relevant `get(...)` call or hardcoded `src` attribute
5. Adjust `object-position` / `filter` / `brightness` if needed
6. Ask user to check in browser, iterate on position/brightness

### LAYOUT / DESIGN CHANGE
1. Read the current file before any edit
2. Describe the plan in 2–3 sentences — what you'll change and why
3. Make the change
4. Tell user what URL to check and what to look for

### NEW FEATURE / PAGE
1. Ask: "What should this do? Who is it for?"
2. Check if a similar component already exists to reuse
3. Follow the existing aesthetic (dark sections, hairline borders, mono specs — no SaaS gradients)
4. Scaffold the page/component, then ask for feedback before detailing

### BUG FIX
1. Read the broken file first
2. Check if it's a known constraint (video autoplay in CDP, grain overlay screenshot freeze — see Known Issues below)
3. Fix, verify with `curl http://localhost:4321/page` returns 200
4. Report what was wrong and what was changed

### DEPLOY
1. Run `git status` to confirm what's uncommitted
2. Show the user a summary of changes
3. Run `git add -A && git commit -m "..."` with a sensible message
4. Run `git push`
5. Confirm push succeeded

---

## Project Reference

### Page → File Map

| URL | File |
|-----|------|
| `/` | `src/pages/index.astro` |
| `/how-it-works` | `src/pages/how-it-works.astro` |
| `/applications` | `src/pages/applications.astro` |
| `/about` | `src/pages/about.astro` |
| `/partner` | `src/pages/partner.astro` |
| `/buy` | `src/pages/buy.astro` |
| `/contact` | `src/pages/contact.astro` |

### Key Components

| Component | Role |
|-----------|------|
| `Hero.astro` | 4 variants: `stack` (home), `side` (how-it-works), `video`, `static` |
| `MechanismFilmstrip.astro` | 3-cell filmstrip: ATTEMPT / RESET / REPEAT |
| `MechanismSequence.astro` | 5-step mechanism sequence with SVG schematics |
| `ApplicationsRegistry.astro` | 6-row list, CMS-driven |
| `LicensingStrip.astro` | National Hardware licensing bar |
| `PatentMap.astro` | 7-market world map |
| `SchematicFrame.astro` | Green corner ticks for technical diagrams |

### Brand Tokens

| Token | Value |
|-------|-------|
| `brand-black` | `#0E0D0B` — page background |
| `brand-green` | `#009444` — primary CTA, accents |
| `brand-bone` | `#EFEAE0` — light text on dark |
| `brand-ink-deep` | `#16140F` — card backgrounds |
| `brand-bone-muted` | `#A8A296` — subdued labels |

Fonts: IBM Plex Sans · JetBrains Mono (specs/kickers) · Newsreader italic (callouts)

### Hero Variant Rules — LOCKED

| Page | Variant | Constraint |
|------|---------|-----------|
| `/` | `stack` | headline → video → subtitle. **Never split or overlay. Non-negotiable.** |
| `/how-it-works` | `side` | text left, video right |
| Other | `static` / `video` | as appropriate |

### Google Sheets CMS Keys

Sheet: https://docs.google.com/spreadsheets/d/19zutxuv_Z7XDTaFDBYAZwFgJkMsVDBKglETNEVgsA60

| Key | Controls |
|-----|---------|
| `home.hero.eyebrow` | Small label above headline |
| `home.hero.title` | Main homepage headline |
| `home.hero.subtitle` | Paragraph under buttons |
| `home.hero.cta1.label` / `.href` | Green button |
| `home.hero.cta2.label` / `.href` | Ghost button |
| `home.hero.video` | Home hero video path |
| `home.story.heading` | "It started with a horse." |
| `home.story.body` | Story paragraph |
| `home.story.image` | Story photo (URL or blank = local) |
| `home.patent.year` | Launch year |
| `howitworks.hero.title` | How-it-works headline |
| `howitworks.hero.subtitle` | How-it-works subtitle |
| `howitworks.hero.video` | How-it-works video |
| `app.01–06.title` | 6 application row labels |
| `app.01–06.desc` | 6 application row descriptions |

### Videos

| File | Used on |
|------|---------|
| `public/videos/brazlatch-timeline.mp4` | Home hero ✅ active |
| `public/videos/brazlatch-triple-action.mp4` | How-it-works (placeholder — replace) |

### Known Issues / Constraints

- **Video autoplay in CDP:** Never autoplays in Claude's headless Chrome. Works fine in real browser. Not a bug.
- **Grain overlay screenshot freeze:** `body::after` SVG feTurbulence causes CDP timeouts. Inject `body::after{display:none}` before screenshotting.
- **No video poster:** Hero shows black panel when autoplay blocked. Needs a `.jpg` still frame extracted from the video.
- **`.env` is gitignored:** `CONTENT_SHEET_URL` must be set manually and in Cloudflare dashboard.

### Deploy Commands

```bash
# Push to GitHub (Cloudflare auto-deploys)
git add -A && git commit -m "message" && git push

# Direct deploy
npm run deploy
```

---

## Quality Rules — Always Enforce

- **Read before editing** — never guess the current state of a file
- **Verify after editing** — `curl http://localhost:4321/page` → must return 200
- **Commit after each logical chunk**
- **Aesthetic:** industrial, precise, technical. No rounded bubbles, no pastel cards, no SaaS gradients.
- **Voice:** short sentences, no fluff, no marketing clichés
- **Sheet over code** — if the change is content, push it to the sheet first
- **Ask before doing** for anything larger than a single-line edit
