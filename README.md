# Four State Custom Floors

Static, server-rendered site for fourstatecustomfloors.com. No build step: plain HTML, one stylesheet, one small progressive-enhancement script.

- `docs/design-system.md` is the source of truth for every page. Match it.
- `assets/styles.css` holds the design tokens (`:root`) and all components.
- `assets/main.js` only adds scroll reveal, the before/after slider and small niceties. All content reads without it.

## Status: homepage mock draft

Photos are grid placeholders labeled with the shot that goes there. Anything in `[brackets]` needs a real answer from Tim before launch:

- Google rating and review count, real review text and reviewer
- Price range and timelines
- Waterproofing system, dust control equipment, insurance
- Tile supply and full-remodel scope answers
- Project towns, service-area lines, hours, response time
- GBP / Facebook / Houzz links (also add to schema `sameAs`)
- See docs/for-tim-to-confirm.md for every fact Tim needs to fill in or sign off on

## Preview locally

```bash
python3 -m http.server 8000
```

## Service pages

The five service pages (`custom-tile-showers/`, `tile-flooring/`, `backsplashes/`, `vinyl-plank-and-hardwood/`, `dust-free-tile-removal/`) are generated from `tools/build_services.py`. Edit the copy in that file and run `python3 tools/build_services.py .` from the repo root to rebuild them. Bracketed text marks facts to confirm with Tim.

## Cache busting

When you change `assets/styles.css` or `assets/main.js`, bump the `?v=` number in `index.html` and `ASSET_VERSION` in `tools/build_services.py`, then rebuild the service pages. Otherwise phones keep the old file for a while.

## Launch checklist

- Switch the og:image and twitter:image URLs (index.html and tools/build_services.py) from the github.io preview address to https://www.fourstatecustomfloors.com/assets/share-image.jpg, then rebuild the service pages.
- Replace the Google Maps search links (Read all 13 reviews, footer Google) with Tim's real Google Business Profile share link: index.html and tools/build_services.py.
