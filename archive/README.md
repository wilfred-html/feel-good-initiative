# Image archive

Files not referenced by any rendered page (`index.html`, `brand-book.html`,
`pitch-deck.html`). Kept in the repo but moved out of the served directories to
keep `images/`, `logos/`, and the project root lean. Nothing here is loaded by
the live site.

| Folder | What's in it |
|--------|--------------|
| `originals/site/` | Full-res `.png`/`.jpg` sources for the root-level webps (team profiles, hero, backgrounds, icon, submark). Re-export the matching `.webp` from these when an image changes. |
| `originals/sections/` | Full-res sources for the `images/` section webps (cleanup, coastal-build, community-bins, entrance, gorilla-gardeners, vision, shoreline, imizamo-yethu, marine-survey, rock-pool). |
| `originals/logos/` | Full-res `.png` sources for the partner-logo webps in `logos/`. |
| `pitch-slides/` | Gemini-generated pitch-deck renders (`slide-01..13`). The rendered `pitch-deck.html` is pure CSS and does not use these. Output target of `generate-images.py`. |
| `design-refs/` | Design comps used as reference only. |
| `retired/` | Replaced or obsolete assets: old `logo`/`logo-2`/`ref-test`, the unused `INANDA` logo, the superseded `houtbay-entrance` / `community-gardens` / `tidalpool-vision` photos, and leftover `beach-ranger`/`hangberg` variants. |

## Re-exporting a webp from an original

```sh
cwebp -q 82 archive/originals/sections/rock-pool.jpg -o images/rock-pool.webp
# large originals: add -resize 1600 0 to cap width
```

Note: `images/beach-ranger.png` and `images/hangberg.png` are still served as
PNGs on the live site (not yet converted to webp) — their sources therefore stay
in `images/`, not here.
