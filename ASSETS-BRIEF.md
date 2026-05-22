# BrazLatch — asset brief

Shot list and render brief for the v2 asset swap. The site ships today on specimen-quality SVG placeholders; every slot below has a one-line code change to drop in the real asset when it arrives.

---

## 1. SolidWorks renders — mechanism sequence

**Used in:** [src/components/MechanismSequence.astro](src/components/MechanismSequence.astro) (`/how-it-works` page), 5 steps + 1 finale.

**Format:** PNG with transparent background, OR rendered on the ground color `#0E0D0B` (brand-black). Either works.

**Resolution:** 1920×1080 minimum per render. 2400×1350 preferred for retina.

**Camera angle:** identical across all 5 renders. The eye should not move between steps. Three-quarter front view (slightly elevated, looking down at the mechanism by ~10°) is the safest single angle.

**Lighting:** soft top-key. No specular hot-spots. No dramatic rim light. The mechanism is a part, not a hero shot.

**Annotation:** none on the render itself. The green callout overlays (force arrows, rotation arcs, RESET label) are drawn by the site in code. The render is the clean mechanical subject; the site adds the annotation layer.

**The 6 renders:**

| Slot | State | Pin position | Spring | Bolt position |
|---|---|---|---|---|
| Step 01 — Spring bias | Locked, at rest | Trapped at far end of channel | Relaxed | Fully extended into strike |
| Step 02 — Trapped pin | Same as Step 01 with optional close-up insert on the trap | Same | Same | Same |
| Step 03 — Load | Partway through push | Mid-channel | Compressed ~4 mm | Partially retracted |
| Step 04 — Release zone | Fully advanced | At release zone (channel exit) | Fully compressed | Fully retracted, awaiting rotation |
| Step 05 — Open (finale) | Past the release zone, exiting upward | Compressed | Fully retracted, clear of strike |
| Step 05 — Reset (finale alt) | Returning from mid-channel back to trap | Decompressing | Returning to extended |

The Step 5 finale slot displays both states as labelled overlays today. A single composited "open vs reset" render works, or two separate renders that the site can swap between. Either is fine.

**Swap-in code path:** in [src/components/MechanismSequence.astro](src/components/MechanismSequence.astro), each step's `<aside>` has an `<svg>` block. Replace with:
```astro
<Image src={renderStep01} alt="Step 01 — spring bias" width={1920} height={1080} class="relative z-10 w-full h-auto" />
```
Add the import at the top of the file. The `<SchematicFrame />` corner ticks and the green annotation `<g>` blocks stay — they overlay the render.

---

## 2. SolidWorks cutaway hero

**Used in:** [src/pages/how-it-works.astro](src/pages/how-it-works.astro) — "The problem" section, currently the `heroPoster` placeholder.

**Format:** PNG or JPG.

**Resolution:** 1280×720 minimum.

**Subject:** exploded view OR cutaway showing all three internal components (bolt, spring, pin in channel) in one frame. Strong axis lines preferred.

**Background:** neutral. Brand-black or a soft warm gray. Not white.

**Swap-in code path:** the file already imports `heroPoster` from `src/assets/renders/hero-poster.jpg`. Replace the file at that path; no code change needed.

---

## 3. Auto-reset micro-loop (optional)

**Used in:** [src/components/MechanismSequence.astro](src/components/MechanismSequence.astro) Step 5 finale. Currently a CSS animation on the SVG reset arrow.

**Format:** MP4 (h264) + WebM (vp9), silent, 30 fps, looped.

**Duration:** 1.5–3 seconds.

**Subject:** the reset gesture only. Pin released from mid-channel, spring snaps back, pin returns to its trap. The whole loop. No music, no fade, no UI motion.

**Resolution:** 1280×720 minimum.

**Swap-in:** convert the Step 5 finale `<aside>` from `<svg>` to a `<video>` tag. The CSS animation block at the bottom of the file becomes unused and can be deleted at that point.

---

## 4. Real installation photography — 6 environments

**Used in:** [src/components/ApplicationDetail.astro](src/components/ApplicationDetail.astro). The `photoSrc` prop on each `<ApplicationDetail>` in [src/pages/applications.astro](src/pages/applications.astro). When `photoSrc` is provided, the specimen card is replaced by the photograph; when absent, the specimen card stays.

**Format:** JPG.

**Resolution:** 2400×3200 (3:4 portrait crop). Site downscales to 1200×1600 at build time.

**Aspect ratio:** 3:4 portrait. Critical — the layout depends on this consistency across all 6.

**Tone:** warm, real, unstylized. Editorial documentary register. Not commercial product photography. The latch should be visible but not necessarily centered or hero-lit. Real installation context is more important than the hardware being the obvious subject.

**Anti-references:** stock photography, AI imagery, "lifestyle" warmth, golden-hour filters, soft focus.

**The 6 shots:**

| Slot | Subject | Framing | Critical details |
|---|---|---|---|
| ENV-01 Equestrian | A horse near a stable door, the latch visible in the door's hardware band | Portrait, horse upper-body in frame, door at horse's shoulder height | Real working stable, not a show barn |
| ENV-02 Livestock | Cattle (or sheep / goats) behind a gate, latch in foreground | Portrait, gate post on the right, animal beyond | Heavy-gauge gate, weathered finish, dirt |
| ENV-03 Trailers | A horse or utility trailer ramp or door, latch in working position | Portrait, latch occupies the lower third, trailer body fills the rest | Mud, hay, real road wear |
| ENV-04 Backyards | A residential garden or pool gate, the latch in a wood or metal fence | Portrait, eye-level, fence and gate visible | Premium home aesthetic, well-kept |
| ENV-05 Logistic | A warehouse roller door or storage gate, the latch on industrial steel | Portrait, slightly low angle, industrial floor | Real working warehouse, not staged |
| ENV-06 Farms | An outbuilding door — grain shed, equipment barn, greenhouse | Portrait, weathered wood or metal door | Working farm, not a showpiece |

**Swap-in code path:** in [src/pages/applications.astro](src/pages/applications.astro), for each environment, add `photoSrc={import_for_that_env}` and `photoAlt="..."` to the `<ApplicationDetail>` call. Import the asset at the top of the frontmatter.

---

## 5. Horse + inventor photograph

**Used in:** [src/pages/index.astro](src/pages/index.astro) — "It started with a horse" section, currently the `horsePhoto` placeholder.

**Format:** JPG.

**Resolution:** 1920×1280.

**Subject:** Alik at the family ranch in Mikhmoret. Working stable context preferred over portrait studio. A horse should be in frame.

**Swap-in:** replace `src/assets/photos/horse-rider-placeholder.jpg` with the real file at the same path. No code change.

---

## 6. Line-art environment icons — refinement (optional)

**Used in:** [src/components/LineArtIcon.astro](src/components/LineArtIcon.astro).

The 6 icons are currently hand-coded SVGs. They work, but a vector illustrator could refine proportions and stroke detail. If you do this:

- Same 24×24 viewBox.
- `stroke="currentColor"`, `fill="none"`, `stroke-width="1.25"` so the existing tints inherit.
- Drop the refined SVG paths in place of the existing ones, keep the file's prop structure.

---

## Priority order for asset sourcing

If budget or time forces a sequence, the order with most credibility return per dollar is:

1. **5 mechanism renders** (Step 01–04 + Step 05 finale). Replaces the most visible placeholders.
2. **Cutaway hero render** for the `/how-it-works` "The problem" section.
3. **Real installation photos** for the 2 highest-volume markets (Equestrian + Livestock). The remaining 4 can ship later without losing page integrity.
4. **Horse + inventor photo** for the about-story beat.
5. **Auto-reset micro-loop video**. The CSS animation is already credible; this is a refinement, not a fix.
6. Icon refinement. Last priority — current icons are on-brand.

Every slot above has a fallback that ships today. Nothing is blocked on assets.
