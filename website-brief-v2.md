# 🌐 BrazLatch Website Brief — v2 (Final Handoff)

> **Master spec for Claude Code.** This is the complete blueprint.
> Use this together with the materials folder (old site screenshots, 3D renders, icons, video, photos).

---

## 1. Project Overview

**Site:** brazlatch.com
**Brand:** Braz Innovation (parent) / BrazLatch (product #1, more to come)
**Patent:** US10934749B2 — *Sliding Bolt Latch and Use Thereof*
**Inventor:** Alik Alexander Braz

### Site Purpose
A simple, professional marketing website that clearly conveys BrazLatch's value to **three audiences** and routes each to the right action:

1. 🏢 **License buyers** — companies looking to acquire patent rights in their market *(highest commercial value)*
2. 🚚 **Distributors** — companies wanting to sell BrazLatch in their region
3. 🛒 **End consumers (US only currently)** — route to National Hardware / Amazon / Lowe's

**Not a goal:** E-commerce, accounts, complex apps. Pure marketing.

---

## 2. Current Market Reality (Critical for Copy)

| Market | Status | Action on Site |
|---|---|---|
| 🇺🇸 USA | ✅ **National Hardware** — exclusive licensee | Show retailers: Amazon, Lowe's, National Hardware. All US packaging carries Braz Innovation logo. |
| 🇨🇦 Canada | 🟢 OPEN | Recruit licensee + distributors |
| 🇦🇺 Australia | 🟢 OPEN | Recruit licensee + distributors |
| 🇬🇧 UK | 🟢 OPEN | Recruit licensee + distributors |
| 🇪🇺 Europe | 🟢 OPEN | Recruit licensee + distributors |
| 🇮🇳 India | 🟢 OPEN | Long-term — keep low profile for now |
| 🇨🇳 China | 🟢 OPEN | ⚠️ Approach with caution (IP risk) |

### 💡 The Killer Sales Angle (USE THIS THROUGHOUT)
> **"Don't build manufacturing from day one."**
> National Hardware manufactures BrazLatch in China. New licensees can purchase finished product directly from this production line to test their market, build distribution, then scale to local manufacturing when it makes business sense.

This dramatically lowers the barrier to entry. Hit this hard on the Partner page.

---

## 3. Tech Stack (Confirmed)

```yaml
framework: Astro 4.x
styling: Tailwind CSS
hosting: Cloudflare Pages (free tier)
domain: brazlatch.com (~$12/year via Cloudflare Registrar)
forms: Cloudflare Pages Functions or Formspree (free tier)
analytics: Cloudflare Web Analytics (free, privacy-friendly)
i18n: astro-i18n (English first, future-ready for additional languages)
content: Markdown files for easy non-developer editing
deployment: Git push → auto deploy

annual_cost: ~$12-15 (domain only)
```

---

## 4. Brand Identity (From Existing Materials)

### Logo
- Wordmark: `brAz` (lowercase except 'A')
- The **'A' is GREEN** — this is the brand accent color
- Subtitle: `INNOVATION` (small caps, letter-spaced)
- Position: "Braz Innovation" is the company, BrazLatch is the first product

### Color Palette
```css
--color-black:       #0a0a0a   /* Primary background */
--color-white:       #ffffff   /* Text on dark */
--color-green:       #6cb04a   /* Brand accent — from logo 'A' (approximate; refine from actual asset) */
--color-cream:       #f5f1ea   /* Alternative section backgrounds */
--color-text-dark:   #1a1a1a   /* Text on light backgrounds */
--color-text-muted:  #6b7280   /* Secondary text */
```

### Typography (suggested — refine from old site fonts)
- **Headlines:** Wide-letterspaced sans-serif in CAPS (matches existing site mood)
  - Candidates: `Manrope`, `Sora`, `DM Sans` in 600-700 weight
- **Body:** Clean readable sans-serif
  - Candidates: `Inter`, `Geist` regular
- **Mono (patent #, technical):** `JetBrains Mono`

### Mood
**Industrial confidence + warm authenticity.** Black backgrounds suggest premium engineering. The horse-and-ranch story softens it into human. The green accent ties it back to natural / agricultural context.

---

## 5. Reusable Assets Inventory

✅ **KEEP AND REUSE** (already excellent):
- The **3D render of the latch mechanism** (hero shot — multiple angles if available)
- The **6 circular hand-drawn application icons** (Fences & Gates, Trailers, Stalls, Backyards, Logistic Warehouse, Farms)
- The **horse-and-rider photograph** (the "About" section anchor)
- The **personal origin story** copy ("since I was 2 years old…") — keep almost verbatim, light polish only
- **Marketing video** (`Alik_ajustco_final__1_.mov`) — embed on homepage as "Watch the story"
- The **brAz logo** (request high-res vector from Alik)

⚠️ **FIX BEFORE REUSING** (typos and weak copy):
- "INSTOLATION" → **"INSTALLATION"**
- "tripel action" → **"triple action"**
- The 6 application descriptions need tightening (current copy is too long and bumpy)

🔄 **REPLACE/UPDATE:**
- The "Where to Buy" section — Ajustco label was incorrect (they're not a current licensee). New section should show **only**: National Hardware (US), Amazon (US), Lowe's (US), with clear "Coming to your market — become a partner →" for everywhere else.

➕ **ADD NEW:**
- Patent number badge: **US10934749B2** — show prominently on Home and How It Works
- World map showing patent coverage by status (sold vs. open)
- "Partner with Us" page with licensing + distribution paths
- Comparison table (BrazLatch vs. standard vs. other "animal-proof" latches)
- The manufacturing-from-China sales angle on the Partner page

---

## 6. Site Map

```
brazlatch.com/
├── /                          → Home
├── /how-it-works              → Mechanism, patent, comparison
├── /applications              → 6 use cases in detail
├── /partner                   → Licensing + Distribution opportunities
├── /about                     → The inventor's story
├── /contact                   → Multi-path contact form
└── /buy                       → US retailers (Amazon, Lowe's, National Hardware)

[Future, when ready]
├── /[locale]/...              → Localized versions (es, fr, de, zh)
└── /innovations               → Parent brand portfolio (when product #2 arrives)
```

**6 main pages + 1 lightweight `/buy` page.** Simple, focused.

---

## 7. Page-by-Page Brief

### 🏠 Home

**Hero (above the fold)**
- Background: Black, with the 3D latch render as the visual anchor (right side or full-bleed with overlay)
- **Headline:** *"The latch animals can't beat. Built for one-handed humans."*
- **Subhead:** *"US-patented self-resetting bolt latch. Licensed and selling across America through National Hardware. Now seeking partners in 6 more markets."*
- **Patent badge** (small, near subhead): `US Patent 10,934,749 · Protected in 7 markets`
- **CTAs:** "See How It Works" (scroll) | "Partner with Us"

**Section 2 — The Story (warmth)**
- Headline: *"It started with a horse."*
- 2-3 sentences: stable owner → horses outsmarting every latch → a mechanical solution → patent → America.
- Visual: a still from the horse video OR the existing horse photo
- CTA: "Read the full story →" (links to /about)

**Section 3 — How It Works (preview)**
- Black background, 3 icon boxes (reuse existing style, fix typos):
  - **Installation** — simple mount, fits standard openings
  - **Triple Action** — push, rotate, release in sequence
  - **Side Changing** — left or right hand mount
- CTA: "See the mechanism →" (to /how-it-works)

**Section 4 — Applications Grid**
- 6 circular icons (reuse existing icons)
- Cream or light section background to contrast the dark hero
- Each card: icon + 1-line value statement
- CTA: "Explore all applications →"

**Section 5 — Proof & Patent**
- Headline: *"Patent-protected in 7 markets. Selling in the US since [year]."*
- Visual: SVG world map highlighting the 7 patent countries
- Logos row: National Hardware, Amazon, Lowe's
- Quote/stat if available

**Section 6 — Three Paths**
- Three cards side by side:
  - **License BrazLatch** → "Acquire exclusive rights in your market" → /partner
  - **Become a Distributor** → "Sell BrazLatch in your region" → /partner#distributors
  - **Find BrazLatch** → "Available in the US through our retailers" → /buy

**Footer**
- Logo + tagline
- Quick links
- "BrazLatch is a Braz Innovation product."
- Patent number
- Contact email, copyright

---

### 🔧 How It Works

**Hero**
- Headline: *"A latch that thinks one step ahead."*
- Subhead: Technical-focused — what makes this mechanism different.
- Background: dark, with mechanism render

**Section 1 — The Problem**
- Conventional latches: animals open them, vibrations loosen them, accidents happen.
- "Animal-proof" latches require two hands and frustrate humans.

**Section 2 — The Mechanism (animated or video)**
- Embed the marketing video here OR build a CSS/SVG animation showing the 5-step sequence:
  1. Spring biases the mechanism to reset
  2. Pin trapped in channel (locked)
  3. Push the bolt against spring force
  4. Pin reaches release zone → rotate
  5. Slide open
- Highlight: **"Interrupted mid-sequence? It auto-resets to locked."**

**Section 3 — Why It's Different**

| Feature | Standard Latch | "Animal-Proof" Latches | BrazLatch |
|---|---|---|---|
| Animal-resistant | ❌ | ✅ | ✅ |
| One-handed operation | ✅ | ❌ | ✅ |
| Vibration-resistant | ❌ | varies | ✅ |
| Self-resetting | ❌ | ❌ | ✅ |
| Patent-protected mechanism | — | varies | ✅ US10934749B2 |

**Section 4 — Patent Details**
- US Patent **US10934749B2** — "Sliding Bolt Latch and Use Thereof"
- Inventor: Alik Alexander Braz
- Coverage map: 7 countries
- Optional: link to USPTO record

**CTA at bottom:** "See where it's used →" or "Partner with us →"

---

### 🎯 Applications

**Hero**
- Headline: *"One mechanism. Many problems solved."*

**Six sections — each application gets its own block:**

For each, structure:
- Existing circular icon (large)
- Headline (concise, problem-focused)
- 2-3 sentences of value statement
- Real-use photo if available

Suggested headlines and copy (refine):

**🐴 Equestrian — Stalls & Stables**
- Headline: *"Your horse won't outsmart this one."*
- Body: The original use case. Stable doors, paddock gates, tack rooms. Animal-resistant, easy for the rider.

**🐄 Livestock — Fences & Gates**
- Headline: *"Zero escapes. Zero compromises."*
- Body: Cattle, sheep, pigs, goats. Heavy-duty for daily agricultural use.

**🚛 Trailers**
- Headline: *"Stays locked at 70 mph."*
- Body: Road vibration won't shake it loose. Storage compartments, ramps, gates.

**🏡 Backyards**
- Headline: *"Pet-proof. Kid-friendly."*
- Body: Residential gates, pool enclosures, garden access. Premium home hardware.

**📦 Logistic & Warehouse**
- Headline: *"Built for industrial reliability."*
- Body: Warehouse gates, container security, equipment enclosures. Vibration and tamper resistant.

**🚜 Farms**
- Headline: *"From greenhouse to grain shed."*
- Body: Agricultural buildings, equipment storage, livestock housing. One latch, every gate on the property.

**Bottom CTA:** "Have a different application in mind? Talk to us →"

---

### 🤝 Partner With Us *(the commercial heart of the site)*

**Hero**
- Headline: *"BrazLatch is open for business in 6 markets."*
- Subhead: *"Already proven in the United States. Looking for licensees and distributors in Canada, Australia, UK, Europe, India, and China."*

**Section 1 — Patent Status Map**
- World map SVG
- US shaded differently (sold/established) vs the 6 open markets
- Hover/tap: "Canada — open for licensing" etc.

**Section 2 — The US Case Study (Proof)**
- Headline: *"What's already working in America."*
- Body: National Hardware licensed BrazLatch and built distribution across the United States. Today BrazLatch is sold through major retailers including Amazon and Lowe's. Manufacturing runs out of China at scale. Every package in the US market carries the Braz Innovation logo — a partnership model that protects the inventor's brand while empowering the licensee.
- Stat highlights (if available): years on market, retailers, units sold

**Section 3 — Two Partnership Paths**

**Path A — License BrazLatch (Exclusive Market Rights)**
For: manufacturers, hardware brands, agricultural suppliers
- Exclusive manufacturing + marketing rights for your country
- Patent protection in your market
- Co-branding rights (your label + Braz Innovation)
- Direct access to inventor for product development
- CTA: "Apply for a license →"

**Path B — Become a Distributor**
For: distributors, retailers, agricultural cooperatives
- Distribution rights for your region (exclusivity negotiable)
- Marketing support and product training
- CTA: "Apply to distribute →"

**Section 4 — 🔑 The Manufacturing Advantage (the killer angle)**
- Headline: *"You don't need to build manufacturing from day one."*
- Body:
  > BrazLatch is already in production at scale through National Hardware's facility in China. New partners can begin by purchasing finished product directly from this production line — test your market, build your distribution network, scale your operation. When the business justifies it, you can transition to local manufacturing. No multi-million-dollar tooling investment to start.
- Visual: simple diagram showing the path: *Purchase from existing line → Build market → (Optional) Local manufacturing*

**Section 5 — Why Now**
Four reasons:
- ✅ Proven product (US market traction)
- ✅ Patent-protected in your country
- ✅ Multiple application categories = multiple revenue streams
- ✅ Direct relationship with the inventor

**Bottom: Contact Form**
- Headline: *"Tell us about your market."*
- Form fields: Name, Company, Country, Role (Licensee / Distributor / Both), Industry, Message
- Submit → routes to licensing inbox

---

### 👤 About

**Hero**
- Headline: *"The inventor."*
- Visual: the existing horse photograph (the man + rearing horse)

**The Story** (use existing copy, lightly polished):
> *Since I was 2 years old I remember myself on our ranch, running between the horses' legs, jumping from horses to the tractor, climbing up to my tree house. Growing up on the ranch made my love for horses inevitable, along with many other passions — building, mechanics, problem-solving. It turned me into a mature young adult fast, doing big mature jobs. While still relatively young, I became the person everyone came to when there was a sophisticated task that needed a creative, simple solution.*
>
> *As the years went by, it became clear: I had a real appreciation for sophisticated simplicity. What I want to share with the world is exactly that — simple solutions to everyday problems that make life easier in a sophisticated, smart way.*
>
> *BrazLatch is the first.*

**Section — Braz Innovation**
- Brief paragraph: "BrazLatch is the first product from Braz Innovation. More inventions are in development — all focused on the same principle: mechanical simplicity solving real-world problems."

**CTAs:** "See how BrazLatch works →" | "Partner with us →"

---

### 📬 Contact

**Hero**
- Headline: *"Let's talk."*

**Three Paths (cards or radio buttons):**

1. **License BrazLatch in my market**
   - Fields: Name, Company, Country, Industry, Message
   - Submit → routes to licensing inbox

2. **Distribute BrazLatch**
   - Fields: Name, Company, Country, Distribution channels, Message
   - Submit → routes to distribution inbox

3. **Buy a BrazLatch**
   - If user selects US → "BrazLatch is available through National Hardware, Amazon, and Lowe's. Visit /buy"
   - If outside US → "BrazLatch is not yet available in your market. Leave your details and we'll notify you when a distributor is appointed. Or — are you interested in becoming one?"
   - Fields: Name, Country, Email, Intended use

---

### 🛒 Buy (US Retail Landing)

Lightweight page. Logos + links:
- **National Hardware** → their product page link
- **Amazon** → Amazon US listing
- **Lowe's** → Lowe's listing

Headline: *"BrazLatch is available across the United States."*
Subhead: *"Not in the US? Become a distributor in your country →"*

---

## 8. Technical Requirements

```yaml
SEO:
  - Semantic HTML, proper heading hierarchy (one H1 per page)
  - Meta tags per page (title, description, OG image)
  - Sitemap.xml + robots.txt
  - JSON-LD schema: Product, Organization, BreadcrumbList
  - Open Graph + Twitter card meta for social sharing

Performance:
  - Lighthouse target: 95+ on all metrics
  - Astro built-in image optimization (.avif/.webp with fallback)
  - Lazy-load below-the-fold images and video
  - Video poster image; load video on click or in-view

Accessibility:
  - WCAG AA compliance
  - Alt text on all images (meaningful, not decorative-only)
  - Keyboard navigation throughout
  - Form labels and aria attributes
  - Focus states visible

Forms:
  - Spam protection: Cloudflare Turnstile (free)
  - Email routing by intent: licensing@brazlatch.com / distribution@brazlatch.com / hello@brazlatch.com
  - Confirmation page + auto-reply email
  - Honeypot field as secondary defense

i18n readiness:
  - Astro project structured with /src/content/[locale]/ folders
  - English-only at launch; future-proofed for /es, /fr, /de, /zh
  - Language switcher in nav (hidden until 2nd language exists)

Privacy:
  - No third-party trackers
  - Cloudflare Web Analytics (cookieless)
  - Privacy policy + cookie banner (minimal, GDPR-aware for EU traffic)
```

---

## 9. Component Library Needed (for Claude Code)

Astro components to build:
- `<Nav>` — sticky transparent over hero, solid on scroll
- `<Hero>` — black bg, headline + subhead + CTAs, supports image or video right-side
- `<PatentBadge>` — compact display: "US Patent 10,934,749 · Protected in 7 markets"
- `<ApplicationCard>` — circular icon + headline + body
- `<HowItWorksStep>` — icon + title + description block
- `<ComparisonTable>` — responsive (cards on mobile, table on desktop)
- `<PatentMap>` — SVG world map with country status colors
- `<AudienceRouter>` — 3-card section with audience-specific CTAs
- `<RetailerLogos>` — logo row with links
- `<ContactForm>` — multi-path with conditional fields
- `<Footer>` — brand mark + links + contact + patent + copyright

---

## 10. Instructions for Claude Code

When you receive this brief plus the materials folder:

1. **Inspect materials first.** Inventory the 3D renders, icons, video, photos, and any other assets. Build a `/src/assets/` structure that mirrors usage on the site.

2. **Set up Astro project:**
   ```bash
   npm create astro@latest brazlatch -- --template minimal --typescript strict
   cd brazlatch
   npx astro add tailwind
   npx astro add sitemap
   ```

3. **Configure i18n structure** (even with English only):
   ```
   /src/content/en/
     home.md
     how-it-works.md
     applications/
       equestrian.md
       livestock.md
       trailers.md
       backyards.md
       logistic.md
       farms.md
     partner.md
     about.md
   ```

4. **Build component library** (see section 9).

5. **Build the 7 pages** following the briefs in section 7. Use Markdown for all editable copy so Alik can update without touching code.

6. **Deploy preview** to Cloudflare Pages on first push. Configure custom domain `brazlatch.com` once site looks ready.

7. **Update the project CLAUDE.md** with: live URL, repo URL, deployment notes, any architectural decisions made during build.

---

## 11. Open Items / Final Decisions

Before Claude Code starts, confirm with Alik:

- [ ] **Logo file** — need high-res vector (SVG or AI). Old site has it; Alik to export from Webflow if needed.
- [ ] **Exact green hex** — sample from logo SVG once available (current placeholder `#6cb04a`).
- [ ] **National Hardware launch year** — for "Selling in the US since [year]" line.
- [ ] **Patent PDF** — provide for /how-it-works download link.
- [ ] **Marketing video** — preferred treatment: hero auto-play (muted) or click-to-watch?
- [ ] **3D render variations** — does Alik have multiple angles? Useful for different page heros.
- [ ] **Photography** — any real-world photos of BrazLatch in use (on actual stables, gates, trailers)?
- [ ] **Email addresses** — set up `licensing@`, `distribution@`, `hello@brazlatch.com` (free with Cloudflare Email Routing).
- [ ] **Copy review** — Alik to read through and approve final copy or request changes.

---

*Brief v2.0 — Final | May 2025 | brazlatch.com | Patent US10934749B2*
