# BrazLatch.com

Marketing site for **BrazLatch** — a patent-protected (US10934749B2) self-resetting triple-action sliding bolt latch. Built with Astro + Tailwind, deployed on Cloudflare Pages.

The full product spec is in [`website-brief-v2.md`](./website-brief-v2.md).

---

## Quick start

Requires Node 18 or newer.

```bash
npm install        # one time
npm run dev        # http://localhost:4321
```

## Build and preview

```bash
npm run build      # runs astro check then astro build → outputs to dist/
npm run preview    # serves dist/ locally to verify the production bundle
```

## Deploy to Cloudflare Pages

Two paths — pick one:

### A. Direct (Wrangler CLI)

```bash
npx wrangler login                  # one-time browser auth
npm run build
npm run deploy                      # = wrangler pages deploy dist --project-name=brazlatch
```

The first `deploy` will prompt to create the Cloudflare Pages project called `brazlatch`. Confirm and the site goes live at `https://brazlatch.pages.dev`.

### B. Git-connected (recommended)

1. Push this repo to GitHub.
2. In Cloudflare dashboard → Workers and Pages → Create → connect the repo.
3. Build command: `npm run build` · Output directory: `dist` · Node version: `18` (or newer).
4. Every push to `main` auto-deploys. Pull-request branches get preview URLs.

### Custom domain

Once the Cloudflare Pages project exists, add `brazlatch.com` under **Custom domains**. Cloudflare provisions HTTPS automatically when DNS resolves to its nameservers.

---

## How to update content

Every editable piece of copy lives in a Markdown file. **You do not need to touch any `.astro` or `.ts` file to edit text.**

### The 7 pages

```
src/content/pages/
├── home.md
├── how-it-works.md
├── applications.md
├── partner.md
├── about.md
├── contact.md
└── buy.md
```

Edit the body Markdown or the YAML frontmatter (title, description, headline, subhead). Save. Run `npm run dev` to preview locally, or commit + push for the live site (auto-deploy).

### The 6 application use-cases

```
src/content/applications/
├── equestrian.md
├── livestock.md
├── trailers.md
├── backyards.md
├── logistic.md
└── farms.md
```

Each has frontmatter (`title`, `headline`, `icon`, `order`, `description`). Reorder with the `order` field. Replace an icon by dropping the new PNG into `src/assets/icons/` using the existing filename (`farms.png`, `trailers.png`, etc.).

### Brand colors and fonts

`tailwind.config.mjs` — all brand colors, fonts, and tokens live here. The green is `#7ED957` (from the logo SVG). To rebrand, change the value and rebuild.

### Open `[CONFIRM]` items

Search the codebase for `[CONFIRM` to see every placeholder that still needs Alik's input. Each one is intentionally visible so you spot them at preview time:

```bash
grep -r "\[CONFIRM" src/ astro.config.mjs .env.example
```

Currently outstanding:

- `[CONFIRM: launch year]` — the year National Hardware shipped the first BrazLatch units in the US. Appears on `/`, `/partner`.
- `[CONFIRM: replace with hi-res 3D render]` — `/how-it-works` hero image is a low-res still from the marketing video.
- `[CONFIRM: provide horse+rider photograph]` — `/about` hero. Currently shows the same video still as the renders.
- `[CONFIRM: provide patent PDF for download link]` — `/how-it-works` patent section.
- `[CONFIRM: FORMSPREE_FORM_ID]` — `.env`. Sign up at https://formspree.io, create a form, paste its ID into `.env` as `PUBLIC_FORMSPREE_ID`.
- `[CONFIRM: TURNSTILE_SITE_KEY]` — `.env`. Optional anti-spam widget on the contact form. Create at https://dash.cloudflare.com → Turnstile.

### Forms

The `<ContactForm>` posts to `https://formspree.io/f/<PUBLIC_FORMSPREE_ID>` with a hidden `intent` field (`license` / `distribute` / `buy`). Configure Formspree to route the three intents to the right inbox.

To migrate off Formspree (e.g. to Cloudflare Pages Functions): replace the `<form action>` in `src/components/ContactForm.astro` and add a `functions/api/contact.ts` handler.

### Email routing (Cloudflare)

Set up free addresses (`licensing@`, `distribution@`, `hello@brazlatch.com`) via Cloudflare Email Routing once the domain is on Cloudflare DNS. Point Formspree to these addresses.

---

## Project structure

```
.
├── CLAUDE.md                 # master project memory (used by Claude Code)
├── README.md                 # this file
├── website-brief-v2.md       # master spec
├── astro.config.mjs          # Astro + Tailwind + Sitemap
├── tailwind.config.mjs       # brand tokens
├── wrangler.toml             # Cloudflare Pages
├── public/                   # static files served as-is
│   ├── favicon.svg
│   ├── robots.txt
│   └── videos/
├── src/
│   ├── assets/               # images optimized by Astro at build time
│   │   ├── logo/             # logo.svg, logo-light.svg, favicon.svg
│   │   ├── icons/            # 6 application PNGs
│   │   ├── photos/           # horse-rider-placeholder.jpg
│   │   └── renders/          # hero-poster.jpg, about-poster.jpg
│   ├── content/
│   │   ├── config.ts         # Zod schema for collections
│   │   ├── pages/            # 7 page markdown files
│   │   └── applications/     # 6 use-case markdown files
│   ├── components/           # 11 Astro components
│   ├── layouts/
│   │   └── BaseLayout.astro  # <head>, JSON-LD, Nav, Footer
│   ├── pages/                # 7 route files
│   └── styles/
│       └── global.css        # Tailwind + utility classes
└── webflow/                  # untouched archive of old assets and Webflow exports
```

## Stack

- **Astro 4.16** — static-site generator
- **Tailwind CSS 3.4** — utility-first styling
- **TypeScript strict** — type-checked content schema + components
- **`@astrojs/sitemap` 3.1.6** — pinned for Astro 4.16 compatibility (3.2+ requires Astro 4.17+ hook)
- **Cloudflare Pages** — hosting
- **Formspree** — forms
- **Cloudflare Turnstile** — anti-spam (optional)

## License

Site code: proprietary, Braz Innovation Ltd.
Latch mechanism: US Patent 10,934,749 B2 and international counterparts.
