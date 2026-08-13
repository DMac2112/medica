# ARSMEDICA — website concept (11 styles × 10 colorways)

A fast, responsive, **light-mode-only** medical-practice site for *ARSMEDICA* (Kalisz).
One page, all real content from **e-arsmedica.pl**, with a live **flicker** to switch the
whole **design language** and **colour palette** — the way `dmac2112.github.io` does.

No build step. No framework. No external requests (fonts are self-hosted). Just open it.

---

## How to check it

**Fastest:** double-click `index.html`.

**Or serve it** (nicer, avoids any `file://` quirks):
```bash
node serve.mjs
```
then open `http://localhost:5177`.

### The flicker control (bottom centre)
- **STYL ‹ ›** — cycle the 11 design languages
- **KOLOR ‹ ›** — cycle the 10 palettes
- **LOSUJ** — shuffle a random combination
- **Keyboard:** `←/→` style · `↑/↓` colour · `R` random
- Your last choice is **remembered** (localStorage). First-ever load opens on *Informacyjny · Czerwień* — the calm, plain-spoken default.

That's **11 × 10 = 110** distinct looks, every one all-light-mode and legible.

---

## The direction (read this first)

The brief is a POZ przychodnia in a small-to-medium Polish town, and a lot of the people
reading it will be **older**. So the baseline is **calm and unmistakably informational**, not
a showpiece. Two rules drive everything:

1. **White is the page.** Every colourway sits on a **pure-white** background
   (`--bg #ffffff`). Colour never washes over the page — it lives only in the *accent*:
   buttons, links, small labels, the left-borders on cards, the icon chips, a short rule
   under each section heading. This is lifted straight from the practice's real site
   (white + red + muted green + grey, red left-border lists).
2. **Contrast is not optional.** Near-black text (`#1a1d21`, 16.9:1) on white; every accent
   clears **AA** on white (≥ 4.5:1) *and* carries white text at ≥ 4.5:1. Verified across all
   ten palettes — see below.

**Informacyjny** is the style built for that baseline: big Public Sans type, generous line
height, phone/address/hours in a left-bordered utility bar right under the hero, a short
accent rule under each heading, and the practice's signature accent left-border on every
card. It is the default because it is the one to show the client first.

---

## The 11 styles (each a real design language, not a reskin)

| # | Nazwa | Character | Type pairing |
|---|-------|-----------|--------------|
| 01 | **Informacyjny** | Calm, plain-spoken, older-reader-first — big type, phone-forward utility bar, accent left-borders & heading rules (the practice's own signature) | Public Sans |
| 02 | **Apteka Klasyczna** | Pharmacopeia / editorial, hairline double-frames, Roman-numeral index | Fraunces + Newsreader |
| 03 | **Klinika Szwajcarska** | Swiss International — strict grid, margin section-numbers, zero radius | Archivo |
| 04 | **Ciepły Humanizm** | Reassuring — big radii, soft shadows, rounded hero panel, pill CTAs | Bricolage + Public Sans |
| 05 | **Redakcja Zdrowia** | Health magazine — masthead dateline, giant headline, italic standfirst, dotted leaders | Fraunces + Newsreader |
| 06 | **Modernizm** | Polish constructivist / Bauhaus — primary shapes, colour-blocked cards | Space Grotesk |
| 07 | **Instytut** | Neoclassical institution — centred axis, AM monogram crest, thin rules | Instrument Serif + Public Sans |
| 08 | **Koordynacja** | Coordinated-care dashboard — graph-paper field, mono data, panel headers | Space Grotesk + IBM Plex Mono |
| 09 | **Zielnik** | Herbarium — botanical sprig motif, italic serif, leaf bullets | Fraunces italic + Newsreader |
| 10 | **Formularz** | Official medical form / *skierowanie* — field framing, `SEKCJA 01`, checkboxes | Archivo + IBM Plex Mono |
| 11 | **Współczesny Premium** | Private-clinic flagship — grotesque married to italic serif, gradient wash | Bricolage + Instrument Serif |

## The 10 colourways (pure-white page, colour only in the accent)

Every palette keeps the same white page and near-black text; only the **accent** changes.
All clear AA on white in both directions (accent-on-white *and* white-on-accent).

| # | Nazwa | Accent | Rationale | Accent-on-white |
|---|-------|--------|-----------|-----------------|
| 01 | **Czerwień** | `#c01527` | The practice's own brand red (default) | 6.22:1 |
| 02 | **Zieleń** | `#277049` | Their secondary medical green | 6.00:1 |
| 03 | **Błękit** | `#1668a8` | Clinical blue | 5.87:1 |
| 04 | **Granat** | `#23386b` | Trustworthy navy | 11.35:1 |
| 05 | **Morski** | `#0e7370` | Teal | 5.67:1 |
| 06 | **Szmaragd** | `#12784a` | Emerald | 5.51:1 |
| 07 | **Bordo** | `#8c2033` | Deep burgundy | 8.86:1 |
| 08 | **Grafit** | `#34383f` | Near-mono charcoal | 11.77:1 |
| 09 | **Stal** | `#3f5670` | Steel blue | 7.56:1 |
| 10 | **Bursztyn** | `#8a5e10` | Warm amber | 5.69:1 |

---

## Content
**Only their existing Polish copy is used — nothing invented.** Sourced from the current
site: hero line, NFZ/POZ hours, prevention programmes (CHUK, *Moje Zdrowie*), vaccinations
(Euvax/Prevenar/Rotarix/Infanrix), the 6 family doctors + schedules, the 8 specialists,
the exact price list, laboratory hours, the *Zamów receptę* flow, and full contact details.

## Tech
- **Fonts self-hosted** as `woff2` (latin + **latin-ext** for ł ż ś ć ń ą ę ó ź) → fast + works offline.
- Palette = CSS custom properties (`colorways.css`, one white scaffold + per-palette accent);
  style = token + component overrides (`styles.css`); the two axes are **orthogonal**, so
  every one of the 110 combinations stays on white and readable.
- Responsive to 375px, keyboard focus visible, `prefers-reduced-motion` respected, **0px horizontal overflow**.

---

## Scroll-driven video animation — feasibility (your second question)

**TL;DR: very doable, and it fits this site. The right technique is a scroll-scrubbed
*frame sequence on `<canvas>`* (the "Apple AirPods" effect), driven by GSAP ScrollTrigger.
No React needed. Budget ~1 focused day once footage exists.**

### The options, ranked for this project
1. **Frame-sequence on canvas (recommended).** Record a short, *locked-off/steady* clip →
   extract 150–300 frames → preload → draw the frame that matches scroll position onto a
   pinned `<canvas>`. Buttery and pixel-precise on **all** browsers incl. mobile Safari.
   This is the industry-standard approach *because* it sidesteps the mobile-Safari problem below.
2. **Native CSS scroll animations** (`animation-timeline: scroll()/view()`). Baseline in
   Chromium + Firefox now, Safari catching up. Perfect for **parallax, reveals, pinned
   sections, progress bars** with *zero JS* — but not for frame-accurate video scrubbing yet.
3. **Scrub a real `<video>` via `currentTime`.** Simplest to write, but mobile Safari
   won't decode-seek smoothly → judder. Avoid for the hero effect; fine for autoplay ambience.
4. **Framer Motion** (`useScroll`+`useTransform`). Elegant, but **React/Next only** → adds a
   build step + framework weight this zero-build site doesn't currently need. GSAP ScrollTrigger
   is the vanilla-JS equivalent and keeps the current architecture.

### What to record
Tripod or gimbal, slow and steady, 4–10s each: a push-in on the entrance, a corridor walk,
a reception/care detail, hands. High fps, good light. We convert to frames afterwards.

### What needs installing
- **For the recommended route:** essentially nothing mandatory. `ffmpeg` to extract frames
  (⚠️ **not currently installed** — one command to add), and **GSAP + ScrollTrigger** vendored
  as a local file (no CDN, keeps it self-contained). Optional **Lenis** for smooth scroll.
- **Only** if you choose the Framer Motion route: Next.js/React + `framer-motion` (bigger change).

### Recommendation
Ship the flicker site as-is (it's done). Add the scroll-video as **one pinned section** using
GSAP + canvas frames. I can scaffold the tooling and a working demo with placeholder frames now,
so it's plug-and-play the moment you send the footage — just say the word.
