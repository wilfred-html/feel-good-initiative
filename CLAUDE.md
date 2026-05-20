# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Marketing site + brand collateral for **The Feel Good Initiative** (TFGI), a Hout Bay (Cape Town) NPO running daily beach cleanups and a R50M tidal-pool capital project. The repository is **pure static HTML/CSS/JS** — no framework, no build step, no package manager. Deployed to Netlify (`feel-good-initiative.netlify.app`).

## Running locally

There is no build, lint, or test command. Open the HTML files directly, or serve the directory:

- VSCode Live Server is preconfigured on port **5501** (`.vscode/settings.json`).
- Any static server works (`python3 -m http.server`, `npx serve`, etc.).

Forms only work end-to-end on the deployed Netlify site — local submits will fail. See "Forms" below.

## Top-level pages

The three HTML files below are independent and self-contained. Each has its **own inline `<style>` and `<script>`**; there are no shared CSS/JS files. Design tokens (colors, spacing, type scale) are **duplicated** across the files — when adjusting the palette or scale, update each file you touch.

| File | Purpose |
|------|---------|
| `index.html` | Main marketing site (~1.9k lines, all inline). Section order: hero → ongoing-projects ticker → value-prop (with `.vp-partners` logo carousel inside it as proof band) → core values (5-icon band) → origin story → vision → 6-phase roadmap → environment → projects → community → leadership → voices → sponsor tiers + Netlify form → final-cta → footer → chatbot. There is **no separate contact section/form** — enquiries route through the sponsor form (`#sponsorForm`). |
| `brand-book.html` | Print-ready A4 brand book (`@page { size: A4 }`). Same tokens as `index.html`, page-based layout. |
| `pitch-deck.html` | Scroll-snap pitch deck. **Different type system** (Crimson Pro serif, simpler `--teal/--orange` vars). Don't import its styles into the others. |
| `pitch-deck-v2.txt` | Plain-text source for a v2 pitch deck — narrative only, not rendered anywhere. |
| `DESIGN-SYSTEM.md` | Consolidated colour/type/spacing/motion reference. Read this before extending the design system; the live CSS in `index.html` is still authoritative when the two disagree. |

## Image assets

- `images/` — section photography (hero, environment, projects, community, vision). `logos/` — partner/sponsor logos for the `.vp-partners` carousel. `slides/` — pitch-deck renders. `design-refs/` — design comps (reference only).
- The live HTML references **`.webp`** everywhere (via a plain `src`, no `<picture>` fallback). Each `.webp` has a same-named `.png`/`.jpg`/`.svg` original kept on disk as the source — when swapping an image, regenerate the `.webp` from the original (the originals are large and not all served).

## Design system (index.html + brand-book.html)

These two files share a deliberate system — keep changes consistent across both:

- **60-30-10 palette**: warm dark teal `#1A3C3C` (60), off-white `#F7F9F8` (30), burnt orange `#D95A10` (10 — accent only, never a section background).
- **Type**: `Josefin Sans` for all headings (h1–h4) and labels in uppercase wide-tracked style; `Plus Jakarta Sans` for body. Major Third scale (`--t-xs` … `--t-3xl`).
- **Spacing**: 8px grid (`--s1` = .5rem … `--s16` = 8rem).
- **Layout**: golden-ratio two-column grids (`61.8% 38.2%`) recur in hero, origin, sponsor sections.
- **Reveal animations** use `.reveal` + `.rd1/.rd2/.rd3` delay classes, driven by an `IntersectionObserver` at the bottom of `index.html`. Add `.reveal` to anything new that should fade in.

CSS is hand-minified-ish (multi-rule lines, no whitespace). Match the surrounding density; don't reformat the whole file when adding rules.

## Forms (Netlify-specific)

The file is long and edited often, so search by attribute rather than chasing line numbers.

- The **only form** is `<form name="sponsorship-interest" data-netlify="true">` (id `#sponsorForm`) inside the sponsor section — it doubles as the site's general enquiry form. Netlify discovers forms by parsing static HTML at deploy time, so:
  - The form must stay rendered in HTML at page load (do not inject it via JS).
  - The hidden `<input name="form-name" value="sponsorship-interest">` and the `bot-field` honeypot must remain.
  - Its `select[name="interest-type"]` options are the targets the chatbot pre-selects (see Chatbot below) — keep option `text` in sync with the `action:'form'` `target` strings in `KB`.
- The standalone contact-form placeholder that used to live in a contact section has been **removed** — don't reintroduce one without giving it a unique `name=`, `data-netlify="true"`, and a `form-name` hidden input.

## Chatbot (index.html)

The "assistant" floating button is a static keyword-matched FAQ, not an LLM. The knowledge base lives in the `KB` object inside the `/* ═══ CHATBOT ENGINE ═══ */` IIFE near the bottom of `index.html`. Topics currently covered: `project`, `sponsor`, `donate`, `team`, `environment`, `community`, plus volunteering / contact / timeline / cost entries. Add topics by extending `KB` with `keywords`, `answer`, and optional `actions`. Two action kinds (`handleAction()`): `action:'navigate'` scrolls to a section anchor; `action:'form'` scrolls to `#sponsorForm` and pre-selects the matching `select[name="interest-type"]` option by matching the action's `target` string against the option `text` (so the `target` must equal an existing option, e.g. `Volunteering`, `Sponsorship prospectus`). `matchTopic()` scores by keyword length, so multi-word keywords beat single words.

## Roadmap section (index.html)

The `<section class="roadmap">` block is a six-phase tabbed stepper (Foundation → Authorisation → Design → Funding → Build → Open) with one `.phase-panel` per phase and a single `.active` panel at a time. Markup, styling, and the click-to-switch script must stay in lockstep — `data-phase="N"` on the `.step-node` button matches the `.phase-panel[data-phase="N"]` it controls, and the per-phase border/accent colours are keyed off that same attribute.

## Pitch-deck slide images

`generate-images.py` is a one-shot OpenRouter (Gemini 2.5 Flash Image) generator that wrote `slides/slide-01..13-*.png`. Notes before re-running:

- The script has a **hard-coded API key and a Linux output path** (`/home/node/.openclaw/...`). Treat the key as compromised (it's in git history); rotate before reuse, and update `OUT_DIR` for this machine.
- Existing slides are committed; the script `SKIP`s files that already exist, so you must delete the target PNG to regenerate it.
- The shared `STYLE` string at the top encodes the brand palette into every prompt — keep it in sync with the design tokens above if the palette shifts.

## Brand voice (from `brand-questionnaire-summary.md`)

When writing copy for the site, brand book, or pitch deck, follow the questionnaire decisions:

- **Avoid** the words *aid*, *relief*, *hand-me-downs*, *we aim to*, *small initiative*, *budget-friendly*, and any guilt-driven framing.
- Prefer *invest in positive change* / *partner* / *support our impact* over *donate*.
- Tone is energetic, grassroots, confident — never dull, helpless, overbearing, or cynical.
- TFGI is **not yet a registered NPO** — do not add "registered NPO" claims (this has been removed twice; see git history). Tax-deductibility language in the chatbot KB is aspirational and should be reviewed before being repeated in copy.

## Git / deploy

- Remote: `github.com/wilfred-html/feel-good-initiative`. Pushing to `main` deploys via Netlify.
- Commit style observed in history: imperative subject + short scope, e.g. `Brand book: fix invisible card h4 on dark pages`.
