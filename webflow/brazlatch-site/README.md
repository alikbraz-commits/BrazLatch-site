# BrazLatch — brazlatch.com

Static, deploy-ready website for BrazLatch.

## Deploy to Netlify

**Drag-and-drop**
1. Zip the entire `brazlatch-site` folder.
2. Go to https://app.netlify.com/drop and drop the zip.
3. Set the production domain to `brazlatch.com` in **Domain management**.

**CLI**
```
npm i -g netlify-cli
netlify deploy --dir=./brazlatch-site --prod
```

**Git-based**
1. Push this folder to a GitHub/GitLab repo.
2. In Netlify "New site from Git" → pick the repo.
3. Build command: *(leave blank)*  ·  Publish directory: `/`.

## What's wired up

- **Distributor inquiry form** — Netlify Forms (no backend needed). Submissions appear under
  Netlify → *Forms* → `distributor-inquiry`. Spam-protected with a honeypot field.
  Successful submits redirect to `/thanks.html`.
- **Security & cache headers** — see `netlify.toml`.
- **www → apex redirect** — toggle the direction in `netlify.toml` if you prefer `www`.
- **Sitemap & robots.txt** — pointing at `https://brazlatch.com/`.

## File map

```
brazlatch-site/
├── index.html              # 8-section homepage
├── thanks.html             # post-submit page
├── css/styles.css          # all styles
├── js/main.js              # nav, sticky header, video helpers
├── assets/
│   ├── img/
│   │   ├── logo.svg            # primary mark
│   │   ├── logo-light.svg      # white version (footer)
│   │   ├── favicon.svg
│   │   ├── hero-poster.jpg     # auto-generated from triple-action video
│   │   ├── about-poster.jpg    # auto-generated from Alik/Ajustco video
│   │   └── icons/              # 6 use-case PNGs + inline SVG for Baby & Kids
│   └── video/
│       ├── brazlatch-triple-action.mp4
│       └── alik-ajustco.mp4
├── netlify.toml
├── robots.txt
└── sitemap.xml
```

## Editing copy

All copy lives in `index.html`. Sections are clearly commented (`<!-- ============== HERO ============== -->` etc.). No build step.

## Updating videos

Replace files in `assets/video/`. If you swap to a different filename, update the
`<source>` tag in `index.html` and (optionally) regenerate the poster frames:

```bash
ffmpeg -i assets/video/brazlatch-triple-action.mp4 -ss 3 -vframes 1 -q:v 3 assets/img/hero-poster.jpg
ffmpeg -i assets/video/alik-ajustco.mp4         -ss 30 -vframes 1 -q:v 3 assets/img/about-poster.jpg
```

## Brand tokens

Defined as CSS custom properties at the top of `css/styles.css`. Quick reference:

| Token       | Value     | Use                          |
|-------------|-----------|------------------------------|
| `--green`   | `#7ED957` | Primary brand accent         |
| `--green-deep` | `#5BB237` | Hover / kicker text         |
| `--ink`     | `#1a1a1a` | Default text                 |
| `--soft`    | `#f6f8f6` | Alternate section background |
| `--dark`    | `#0f1411` | Distributor form section     |
