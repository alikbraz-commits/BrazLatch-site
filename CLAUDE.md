# ðŸ§  CLAUDE.md â€” BrazLatch Project Memory System

> **×”×•×¨××•×ª ×œ×ž×•×“×œ:** ×§×¨× ×§×•×‘×¥ ×–×” ×œ×¤× ×™ ×›×œ ×¤×¢×•×œ×” ×‘×¤×¨×•×™×§×˜.

---

## ðŸ“ CONTEXT SNAPSHOT

```yaml
project: BrazLatch (a Braz Innovation product)
domain: brazlatch.com
owner: Alik Alexander Braz (inventor)
patent: US10934749B2 â€” "Sliding Bolt Latch and Use Thereof"
mission: Find licensees and distributors in 6 open markets
language_default: ×¢×‘×¨×™×ª for chat / English for product
session_goal: [×ª×¢×“×›×Ÿ ×™×“× ×™×ª ×œ×¤× ×™ ×›×œ ×¡×©×Ÿ]
```

---

## ðŸ·ï¸ PRODUCT ESSENTIALS

**BrazLatch** is a self-resetting spring bolt latch. Trapped-pin sequential release system. Animal-proof, vibration-proof, one-handed human operation. Auto-resets to locked when partial attempts are made.

**Origin story:** Invented by a stable owner after horses kept opening conventional latches.

**Applications:** Equestrian, livestock, trailers, backyards, logistic/warehouse, farms.

---

## ðŸŒ MARKET STATUS

| Market | Status |
|---|---|
| ðŸ‡ºðŸ‡¸ USA | âœ… Licensed to **National Hardware** (exclusive) â€” manufactures in China; sells through National Hardware, Amazon, Lowe's. All US packaging carries Alik's logo. |
| ðŸ‡¨ðŸ‡¦ Canada | ðŸŸ¢ OPEN â€” Priority 1 |
| ðŸ‡¦ðŸ‡º Australia | ðŸŸ¢ OPEN â€” Priority 1 |
| ðŸ‡¬ðŸ‡§ UK | ðŸŸ¢ OPEN â€” Priority 2 |
| ðŸ‡ªðŸ‡º Europe | ðŸŸ¢ OPEN â€” Priority 2 |
| ðŸ‡®ðŸ‡³ India | ðŸŸ¢ OPEN â€” Long-term |
| ðŸ‡¨ðŸ‡³ China | ðŸŸ¢ OPEN â€” âš ï¸ IP-cautious |

**Ajustco:** past partner (tried European distribution, ended), still useful for industry connections only.

### ðŸ”‘ The Manufacturing Advantage
National Hardware manufactures in China. Alik can purchase finished product from their production line. **This means new licensees don't need to build manufacturing from day one** â€” they can buy ready inventory, build distribution, scale, then transition to local manufacturing later. **This is the killer sales angle.**

---

## ðŸŽ¨ BRAND IDENTITY

```yaml
parent_brand: Braz Innovation
product: BrazLatch (first product â€” more inventions planned)
logo: "brAz" wordmark with green 'A' + "INNOVATION" subtitle
colors:
  black: "#0a0a0a"      # primary background
  white: "#ffffff"       # primary text on dark
  green: "#6cb04a"       # accent (from logo â€” refine from actual SVG)
  cream: "#f5f1ea"       # alternative section bg
mood: industrial confidence + warm authenticity (horses + engineering)
```

---

## ðŸ”Œ INSTALLED PLUGINS

```
superpowers@claude-plugins-official    â†’ enhanced capabilities
get-shit-done-cc (npx)                 â†’ action-first mode
context-mode@context-mode              â†’ smart context switching
claude-mem@thedotmack                  â†’ persistent memory
skill-creator@claude-plugins-official  â†’ skill authoring
frontend-design@claude-plugins-official â†’ UI design
```

**Recommended marketing skills (install in Claude Code):**
```bash
/plugin marketplace add thatrebeccarae/claude-marketing
/plugin install seo-content-writer@claude-marketing
/plugin install content-workflow@claude-marketing
/plugin install email-composer@claude-marketing
```

---

## ðŸ§  MEMORY ARCHITECTURE

### Layer 1 â€” this file (always loaded)
### Layer 2 â€” claude-mem (persistent across sessions)
```
"×–×›×•×¨: [fact]"             â†’ save
"recall [topic]"            â†’ retrieve
"mem: save session"         â†’ close session
```

**Categories:**
- `mem:markets`  â€” market research per country
- `mem:contacts` â€” companies / leads
- `mem:content`  â€” approved marketing copy
- `mem:deals`    â€” active negotiations
- `mem:website`  â€” site-related decisions

### Layer 3 â€” context-mode
```
"context: website"     â†’ website project
"context: canada"      â†’ Canada market work
"context: australia"   â†’ Australia market work
"context: outreach"    â†’ B2B outreach
"context: deck"        â†’ license pitch deck
```

---

## âš¡ WORKING RULES

1. **Action first** (GSD mode) â€” execute, don't over-ask
2. **Save everything to mem** â€” research, decisions, contacts
3. **Target-market language** â€” content for Canada/AU/UK in English; Europe per country
4. **B2B focused** â€” the customer is a company, not a consumer (except US end-buyers â†’ existing retailers)
5. **Patent + proof always present** â€” every outreach mentions US10934749B2 + National Hardware success

---

## ðŸ“ PROJECT STRUCTURE

```
brazlatch/
â”œâ”€â”€ CLAUDE.md                  â† this file
â”œâ”€â”€ .claude/
â”‚   â”œâ”€â”€ memory/                â† claude-mem
â”‚   â””â”€â”€ contexts/              â† context-mode
â”œâ”€â”€ product/
â”‚   â””â”€â”€ patent-summary.md
â”œâ”€â”€ website/                   â† the website project
â”‚   â”œâ”€â”€ website-brief-v2.md
â”‚   â””â”€â”€ (Astro project once built)
â”œâ”€â”€ marketing/
â”‚   â”œâ”€â”€ pitch-deck/
â”‚   â”œâ”€â”€ outreach-emails/
â”‚   â””â”€â”€ brand-voice.md
â”œâ”€â”€ market-research/
â”‚   â”œâ”€â”€ canada/
â”‚   â”œâ”€â”€ australia/
â”‚   â”œâ”€â”€ uk/
â”‚   â”œâ”€â”€ europe/
â”‚   â”œâ”€â”€ india/
â”‚   â””â”€â”€ china/
â””â”€â”€ assets/
    â”œâ”€â”€ 3d-renders/
    â”œâ”€â”€ icons/
    â”œâ”€â”€ photos/
    â””â”€â”€ videos/
```

---

## ðŸ’¬ QUICK COMMANDS

```
"build the website from website-brief-v2.md"  â†’ Claude Code starts building
"market research [country]"                    â†’ deep market analysis
"draft cold email for [industry] in [country]" â†’ B2B outreach
"license pitch deck for [market]"              â†’ presentation
"summary of what you know about BrazLatch"     â†’ context dump
```

---

## ðŸš€ SESSION CHECKLIST

**Opening:**
- [ ] Read CLAUDE.md
- [ ] `recall last-session`
- [ ] Set `context: [topic]`

**Closing:**
- [ ] `mem: save [summary]`
- [ ] Update Market Status if changed

---

*Updated: May 2025 | Version 3.0 | brazlatch.com | Patent US10934749B2*


---

## 🌐 WEBSITE PROJECT (built 2026-05-14)

The website at `brazlatch.com` is an **Astro 4 + Tailwind** static site at the **root of this directory**. Built per `website-brief-v2.md`. Deploys to **Cloudflare Pages**.

### File map

```
src/content/pages/        ← 7 page markdown files (edit copy here)
src/content/applications/ ← 6 use-case markdown files
src/components/           ← 11 Astro components (Nav, Hero, PatentBadge, etc.)
src/layouts/BaseLayout    ← <head>, JSON-LD, Nav, Footer
src/pages/                ← 7 route files
src/assets/               ← optimized images (logo, icons, renders, photos)
public/videos/            ← marketing videos (served as-is)
```

### Brand tokens (defined in `tailwind.config.mjs`)

| Token | Value | Use |
|---|---|---|
| `brand.black` | `#0a0a0a` | Primary background |
| `brand.white` | `#ffffff` | Text on dark |
| `brand.green` | `#7ED957` | Accent (sampled from logo SVG) |
| `brand.green-deep` | `#5BB237` | Hover, kickers on light bg |
| `brand.cream` | `#f5f1ea` | Alternate section bg |
| `brand.ink` | `#1a1a1a` | Text on light |
| Font sans | Manrope | All text |
| Font mono | JetBrains Mono | Patent numbers |

### Commands

```bash
npm run dev      # localhost:4321
npm run build    # astro check + astro build → dist/
npm run preview  # serve dist/ locally
npm run deploy   # wrangler pages deploy dist --project-name=brazlatch
```

### How to update content

Every editable string lives in a Markdown file under `src/content/`. Do not touch `.astro` files to change copy. Edit, save, `git push` → Cloudflare auto-deploys.

- Headlines, subheads, body copy → `src/content/pages/*.md`
- The 6 application use-cases → `src/content/applications/*.md`
- Brand color or font → `tailwind.config.mjs`
- Logo or icon swap → drop the new file in `src/assets/logo/` or `src/assets/icons/` using the existing filename

### Architectural decisions made during build

1. **Content collections at `src/content/pages/` and `src/content/applications/`** (not `src/content/en/...` as the brief suggested). Astro's content-collection API expects the first directory level to be the collection name. The original i18n folder shape was incompatible with the collection schema. Future locales will be added as separate collections (`pages_es`, etc.) or via filename-based locale suffix.
2. **No Astro i18n routing yet.** Removed from `astro.config.mjs` because `@astrojs/sitemap` 3.x trips on it without a matching `sitemap({ i18n: ... })` config. Re-introduce both when a second locale ships.
3. **`@astrojs/sitemap` pinned to `3.1.6`.** Versions 3.2+ require the `astro:routes:resolved` hook (Astro 4.17+); we are on 4.16.
4. **Forms via Formspree.** Single endpoint with hidden `intent` field. Routing logic lives in the Formspree dashboard, not in code.
5. **`#7ED957` is the brand green.** Sampled from the actual `logo.svg` (which had this hex). The brief's `#6cb04a` was an explicit placeholder.
6. **The existing `webflow/brazlatch-site/` static HTML site is preserved** as historical reference. It was a previous interim build (single-page anchored, Netlify-targeted) and is not maintained.

### Open `[CONFIRM]` items (need Aliks input)

1. **Launch year** — "Selling in the US since [CONFIRM: launch year]" on `/` and `/partner`.
2. **Hi-res 3D render** — `/how-it-works` hero currently uses a 10 KB still from the marketing video.
3. **Horse + rider photograph** — `/about` hero placeholder is the same video still.
4. **Patent PDF** — drop the file into `public/patent/` and link from `/how-it-works`.
5. **Formspree form ID** — set `PUBLIC_FORMSPREE_ID` in `.env` (copy `.env.example`).
6. **Turnstile site key** — optional; set `PUBLIC_TURNSTILE_SITE_KEY` in `.env` to enable.
7. **Email routing** — set up `licensing@`, `distribution@`, `hello@brazlatch.com` via Cloudflare Email Routing once the domain is on Cloudflare DNS, then point Formspree to them.
8. **Real-world photography** — installed BrazLatches on stables, gates, trailers would dramatically lift the applications page.

Grep the source tree for `[CONFIRM` to find every remaining marker.

### Build status (last verified 2026-05-14)

```
✓ astro check         0 errors, 0 warnings, 3 hints
✓ astro build         7 pages, 17 optimized images, sitemap generated
✓ dist/sitemap-0.xml  all 7 routes listed
```

