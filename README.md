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
- Town list in the service area, FAQ and schema (draft guesses, confirm with Tim)

## Preview locally

```bash
python3 -m http.server 8000
```
