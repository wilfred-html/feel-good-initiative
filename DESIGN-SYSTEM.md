# Design System — The Feel Good Initiative

The canonical reference is `brand-book.html` (rendered) and the inline `<style>` block at the top of `index.html` (implemented). This document consolidates both so designers and developers don't have to read either to extend the system. When in doubt, **the live CSS wins** — the brand book describes intent, `index.html` ships pixels.

Scope: applies to `index.html` and `brand-book.html`. `pitch-deck.html` uses a separate (older) palette and Crimson Pro serif — do not back-port these tokens into it.

---

## 1. Colour

The palette is **60-30-10**: 60% neutrals, 30% deep teals, 10% sunset orange. Orange is an accent only — never a section background, never body text.

### Primary

| Name | Hex | RGB | CMYK | Variable |
|---|---|---|---|---|
| Deep Forest | `#1A3C3C` | 26, 60, 60 | 57, 0, 0, 76 | `--dark`, `--text` |
| Ocean Teal | `#2A8B8B` | 42, 139, 139 | 70, 0, 0, 45 | `--teal` |
| Coastal Light | `#5CBDAE` | 92, 189, 174 | 51, 0, 8, 26 | `--teal-light` |

### Accent & neutral

| Name | Hex | Variable | Use |
|---|---|---|---|
| Sunset Orange | `#D95A10` | `--orange` | CTAs, the *one* accent |
| Sunset Hover | `#B84A0D` | `--orange-hover` | Hover state for orange |
| Deep Dark | `#122E2E` | `--dark-deep` | Darkest backgrounds, value-prop section |
| Teal Pale | `#D1F0EA` | `--teal-pale` | Highlight cards on light bg |
| Teal Wash | `#EDF8F6` | `--teal-wash` | Hero, label pills |
| Off-white body | `#F7F9F8` | `--bg` | Page background |
| Bg alt | `#EEF3F2` | `--bg-alt` | Alternating section bg |
| Bg card | `#FAFCFB` | `--bg-card`, `--white` | Card surfaces |
| Border | `#D0DFDC` | `--border` | Default border |
| Border light | `#E2EDEB` | `--border-light` | Hairlines, dividers |

Text scale: `--text` (`#1A3C3C`, body) → `--text-light` (`#3D6363`, descriptions, max 560px width) → `--text-muted` (`#5E8585`, captions).

Pantone equivalents (print only): Ocean Teal ≈ Pantone 7473 C, Sunset Orange ≈ Pantone 1665 C.

### Pairing rules

- **Light surfaces** (`--bg`, `--bg-card`): use `--text` for body, `--teal` for accents/links, `--orange` for CTAs only.
- **Dark surfaces** (`--dark`, `--dark-deep`): use `#fff` for body, `--teal-light` for accents (Ocean Teal fails AA on dark), `--orange` for CTAs.
- **Never** put `--teal-light` (`#5CBDAE`) on white — fails contrast.
- **Never** use `--orange` for body text or section backgrounds. It's reserved for the primary CTA, the pulse animation, and a single hover/focus accent per view (Von Restorff).

### Section background alternation

Sections alternate to create rhythm: `--bg` → `--bg-alt` → `--bg-card` → `--dark-deep` (one "value prop" per page). Adjacent sections must not share the same background.

---

## 2. Typography

Two families, loaded from Google Fonts. Both pages preconnect to fonts.gstatic.com.

### Display — Josefin Sans
- All `h1`–`h4`, `.sec-title`, the tagline, hero card numbers, nav logo wordmark.
- Used uppercase + wide tracking (`letter-spacing: .12em–.15em`) for labels and the wordmark.
- Weights in use: 300, 400, 500, 600, 700.
- Headline letter-spacing: `-.02em` (h1), `-.03em` (cover h1).

### Body — Plus Jakarta Sans
- All paragraphs, buttons, labels, form fields, navigation links, UI.
- `line-height: 1.6` body, `1.7` for descriptions, `1.2` for headings.
- Weights in use: 300, 400, 500, 600, 700, 800.

### Type scale (Major Third — 1.25)

| Token | Value | Where |
|---|---|---|
| `--t-3xl` | 3.052rem (≈48px) | h1, hero headline |
| `--t-2xl` | 2.441rem (≈39px) | h2, section headlines |
| `--t-xl` | 1.953rem (≈31px) | Card titles |
| `--t-lg` | 1.563rem (≈25px) | h3, feature headings |
| `--t-md` | 1.25rem (≈20px) | Lead text, hcard amounts |
| `--t-base` | 1rem (16px) | Body |
| `--t-sm` | .875rem (14px) | Buttons, nav links, descriptions |
| `--t-xs` | .8rem (≈13px) | Labels, badges, small caps |

Headings use `clamp()` for fluid sizing: `h1 { font-size: clamp(2.2rem, 4.5vw, var(--t-3xl)) }`, `h2 { clamp(1.6rem, 3vw, var(--t-2xl)) }`. Keep this pattern for any new headline.

### Label / pill style

Repeating motif: uppercase, `.12em–.15em` tracking, `--t-xs`, weight 700, teal text on `--teal-wash` pill background, `border-radius: 100px`. Used as the section-intro `.label`, hero badge, and brand-book `.sec-label`.

---

## 3. Spacing & layout

### 8px grid — `--s*` scale

| Token | rem | px |
|---|---|---|
| `--s1` | .5 | 8 |
| `--s2` | 1 | 16 |
| `--s3` | 1.5 | 24 |
| `--s4` | 2 | 32 |
| `--s5` | 2.5 | 40 |
| `--s6` | 3 | 48 |
| `--s8` | 4 | 64 |
| `--s10` | 5 | 80 |
| `--s12` | 6 | 96 |
| `--s16` | 8 | 128 |

Always pick from this scale. Don't introduce arbitrary values like `1.25rem` — round to `--s2` or `--s3`.

### Container & sections

- `.container { max-width: var(--max-w) /* 1140px */; padding: 0 var(--s3) }`
- `.section { padding: var(--s12) 0 }` (96px top/bottom). Mobile reduces to `--s8`.
- Brand book pages cap content at 1200–1320px via `padding: var(--s8) max(var(--s6), calc((100% - 1200px) / 2))`.

### Grid systems

- **Golden ratio** (primary): `display: grid; grid-template-columns: 61.8% 38.2%; gap: var(--s6)`. Used in hero, origin, sponsor sections.
- **Even split**: `.two-col.even { 1fr 1fr }`.
- **Three-column**: `.three-col { repeat(3, 1fr); gap: var(--s3) }` for projects, leadership, environment, treatment rules.
- Below 1024px, all golden-ratio grids collapse to a single column.

### Radii

- `--r: 8px` — buttons, inputs, small cards.
- `--rlg: 16px` — hero card, large cards, primary CTA.
- `100px` — pills, labels, progress bars (full round).
- `50%` — avatars, the nav logo, status dots.

### Nav

- `--nav-h: 64px`, sticky, `rgba(247,249,248,.92)` with `backdrop-filter: blur(12px)`. Bottom border `--border-light`.

---

## 4. Components

All component CSS lives inline in `index.html` — class names below map to that file. The brand book has its own visually-equivalent re-implementations (`.swatch`, `.value-card`, `.rule-box`, etc.) tuned for A4 print.

### Buttons (`index.html` ~line 39)

| Class | Use |
|---|---|
| `.btn` | Base — `var(--s1) var(--s3)` padding, `--t-sm`, weight 600, `--r` radius |
| `.btn-teal` | Default action. Hover → `--dark` + `translateY(-1px)` |
| `.btn-orange` | Primary CTA — sponsor, partner, donate-equivalents. Hover → `--orange-hover` |
| `.btn-outline` | Secondary — transparent with `--border`, hover gains teal border |
| `.btn-white` | On dark backgrounds |
| `.btn-lg` | `var(--s2) var(--s4)` padding + `--t-base` |
| `.btn-cta-main` | The hero/final CTA — `--rlg` radius and a 3s `pulse` keyframe (Von Restorff). Use **once per page maximum** |

Icons come from Bootstrap Icons (`bootstrap-icons@1.11.3`, CDN-loaded). Always pair the CTA button with a directional `bi-arrow-up-right` or action `bi-send` glyph for clarity.

### Forms

- Light forms (`.contact-form`): white-ish bg (`--bg`), `1.5px solid var(--border)`, focus border → `--teal`.
- Dark forms (`.sponsor-form` inside the dark sponsor section): transparent bg, `1.5px` borders at `rgba(255,255,255,.16)`, focus → `--teal-light` + `rgba(255,255,255,.03)` background.
- All inputs use the body font, `--t-base`, `--s2` padding, `--r` radius, and `-webkit-appearance: none` to neutralise iOS chrome.
- See `CLAUDE.md` for the Netlify Forms wiring rules — only the sponsorship form is live.

### Cards

- Default card: `padding: var(--s3); background: var(--bg-card); border: 1px solid var(--border-light); border-radius: var(--rlg); transition: all .25s var(--ease)`.
- Hover: `translateY(-2px) + box-shadow: 0 var(--s1) var(--s4) rgba(26,60,60,.05)`.
- Dark variant: `background: rgba(255,255,255,.04); border-color: rgba(255,255,255,.08)`.

### Hero card (`.hcard`)

The recurring "donation/progress" card pattern: dark `--dark` header with stacked label/amount/sub, body with `.pbar` progress bar (animates from 0% to a JS-set width via `IntersectionObserver`), and a 3-column stat row beneath a top border.

### Reveal animations

- `.reveal` starts hidden, gains `.v` when intersecting (`threshold: .1, rootMargin: '0px 0px -30px 0px'`).
- Stagger with `.rd1`, `.rd2`, `.rd3` (delay classes — check the live CSS for the exact delay values; usually 100–300ms steps).
- Easing: `--ease: cubic-bezier(.16, 1, .3, 1)`. Use this for *every* transition longer than 200ms — never default `ease`.
- Doherty: keep all interaction transitions ≤ 400ms (`.15s–.25s` is the working range in the file).

### Other transitions

- Hover micro-lift on cards & teal buttons: `translateY(-1px to -2px)`, `transition: all .2s` or `.25s var(--ease)`.
- Pulse keyframe on `.btn-cta-main`: 3s ease-in-out, expanding `box-shadow: 0 0 0 8px rgba(217,90,16,.15)` at 50%.
- Blink keyframe on the hero badge dot: 2s, `opacity: 1 → .4 → 1`.

---

## 5. Iconography & imagery

- **Icons**: Bootstrap Icons via CDN. Standardise on `bi-` glyphs already in use (`bi-arrow-up-right`, `bi-send`, `bi-envelope`, `bi-people`, `bi-tree`, `bi-chevron-down`, etc.). No custom SVGs introduced ad hoc.
- **Photography**: real, never stock. Action shots, community, drone landscapes of Hout Bay. Warm natural grading — slight boost to greens/teals, never over-saturated. When using as a section background, overlay a teal-wash or dark gradient at 85–95% opacity for text readability (see `.hero-bg::after`).
- **Sponsor logos**: real raster/SVG marks live in `logos/`. White-logo-on-dark is preferred in the sponsor carousel. For sponsors without a usable logo, render a styled wordmark in Josefin Sans instead (precedent: Beach Bar, Hout Bay Gallery, Handiman in commit `4c5b0a3`).
- **Children**: photos require parental consent. Never show poverty, suffering, or anything that could read as exploitative — show pride, action, transformation.

Generated stock-style imagery for `pitch-deck.html` is produced by `generate-images.py` (Gemini 2.5 Flash Image via OpenRouter); the `STYLE` constant in that script encodes this palette in prose. If the palette changes, update that string too.

---

## 6. Voice & copy

Persona: energetic, approachable friend in their mid-30s. Casual but purposeful. Confident without arrogance.

Spectrum (from the brand questionnaire, encoded in `brand-book.html`):

| Axis | Position |
|---|---|
| Formal ↔ Casual | 75% Casual |
| Serious ↔ Playful | 65% Slightly Playful |
| Exclusive ↔ Inclusive | 85% Inclusive |
| Traditional ↔ Modern | 70% Modern |
| Corporate ↔ Grassroots | 80% Grassroots |

Should feel: **Empowering, Joyful, Bold, Connected, Vibrant**. Never feel: **Dull, Closed-off, Helpless, Overbearing, Cynical**.

### Word lists

✅ **Use**: *"We show up. Every single day."*, *invest in positive change*, *partner with us*, *support our impact*, *real impact, real change*, *built by the community, for the community*, *join the movement*.

❌ **Avoid**: *aid*, *relief*, *hand-me-downs*, *we aim to* (we DO), *small initiative*, *budget-friendly*, *donate* (use *invest*/*partner*), guilt or pity framing, political content.

### Money language

Replace *donate* with *invest*, *partner*, or *support*. Tier names are fixed: **Supporter (R50K) → Champion (R250K) → Builder (R1M) → Visionary (R5M+)**. The chatbot KB and the sponsor section both depend on these names — change them in lockstep.

### Compliance hard rules

- TFGI is **not yet a registered NPO**. Do not write "registered NPO", "NPO-status", or imply tax-deductibility as fact (the chatbot KB still says "tax-deductible under NPO status" — flag for review before quoting in new copy).
- No political messaging, no commentary on community tensions, no exploitation framing.

---

## 7. Sponsor tier visual treatment

| Tier | Amount | Accent | Treatment |
|---|---|---|---|
| Supporter | R50K | `--text-muted` heading | Standard card, brand on website + materials |
| Champion | R250K | Default `--dark` | Standard card, on-site branding mention |
| Builder | R1M | `--teal` heading | Highlighted card, naming-rights language |
| Visionary | R5M+ | `--orange` heading | Most prominent card, advisory-seat language |

Co-branding logo rules (apply on shared collateral):
- Clear space = height of the "F" in "Feel" on all sides.
- Print min: 30mm width. Digital min: 120px width. Smaller → use icon mark only.
- Layout: TFGI left/top, sponsor right/bottom, separated by a thin Ocean Teal vertical divider.
- On photography: white logo + sufficient gradient overlay.

---

## 8. Where it lives in code

| Concern | File / location |
|---|---|
| Live design tokens | `:root` in `index.html` (~line 14) and `brand-book.html` (~line 13) — duplicated; keep in sync |
| Component CSS | Inline `<style>` at the top of each HTML page |
| Reveal observer & scroll smoothing | Inline `<script>` near the bottom of `index.html` (~line 994) |
| Brand book canonical descriptions | `brand-book.html` pages 02–08 (colour, type, voice, photography, sponsor co-branding, merch) |
| Tone-of-voice source of truth | `brand-questionnaire-summary.md` |
| Pitch-deck image style prompt | `STYLE` constant in `generate-images.py` |
| Sponsor logos | `logos/` |
| Slide renders | `slides/slide-NN-*.png` |

When changing a token (e.g. shifting orange or adding a `--s7`):

1. Update `:root` in **both** `index.html` and `brand-book.html`.
2. Update the `STYLE` string in `generate-images.py` if a brand colour has shifted.
3. Update the swatch grid on page 04 of `brand-book.html` (HEX/RGB/CMYK strings are hard-coded, not driven by the variable).
4. Update this file.
