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

Three independent self-contained HTML files. Each has its **own inline `<style>` and `<script>`**; there are no shared CSS/JS files. Design tokens (colors, spacing, type scale) are **duplicated** across the files — when adjusting the palette or scale, update each file you touch.

| File | Purpose |
|------|---------|
| `index.html` | Main marketing site — sponsor-focused, all content sections + chatbot + sponsorship form. |
| `brand-book.html` | Print-ready A4 brand book (`@page { size: A4 }`). Same tokens as `index.html`, page-based layout. |
| `pitch-deck.html` | Scroll-snap pitch deck. **Different type system** (Crimson Pro serif, simpler `--teal/--orange` vars). Don't import its styles into the others. |
| `pitch-deck-v2.txt` | Plain-text source for a v2 pitch deck — narrative only, not rendered anywhere. |

## Design system (index.html + brand-book.html)

These two files share a deliberate system — keep changes consistent across both:

- **60-30-10 palette**: warm dark teal `#1A3C3C` (60), off-white `#F7F9F8` (30), burnt orange `#D95A10` (10 — accent only, never a section background).
- **Type**: `Josefin Sans` for all headings (h1–h4) and labels in uppercase wide-tracked style; `Plus Jakarta Sans` for body. Major Third scale (`--t-xs` … `--t-3xl`).
- **Spacing**: 8px grid (`--s1` = .5rem … `--s16` = 8rem).
- **Layout**: golden-ratio two-column grids (`61.8% 38.2%`) recur in hero, origin, sponsor sections.
- **Reveal animations** use `.reveal` + `.rd1/.rd2/.rd3` delay classes, driven by an `IntersectionObserver` at the bottom of `index.html`. Add `.reveal` to anything new that should fade in.

CSS is hand-minified-ish (multi-rule lines, no whitespace). Match the surrounding density; don't reformat the whole file when adding rules.

## Forms (Netlify-specific)

- `index.html:795` — `<form data-netlify="true" name="sponsorship-interest">` is the **only live form**. Netlify discovers forms by parsing static HTML at deploy time, so:
  - The form must stay rendered in HTML at page load (do not inject it via JS).
  - The hidden `<input name="form-name" value="sponsorship-interest">` and the `bot-field` honeypot must remain.
- `index.html:861` — `<form class="contact-form" onsubmit="event.preventDefault();">` is a **non-functional placeholder**. If wiring it up, give it a unique `name=`, add `data-netlify="true"` + the `form-name` hidden input, and remove the preventDefault.

## Chatbot (index.html)

The "assistant" floating button is a static keyword-matched FAQ, not an LLM. The knowledge base lives in the `KB` object near `index.html:1009`. Add topics by extending `KB` with `keywords`, `answer`, and optional `actions` (`navigate` to a section anchor or `form` to pre-select a contact-form option). `matchTopic()` scores by keyword length, so multi-word keywords beat single words.

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
