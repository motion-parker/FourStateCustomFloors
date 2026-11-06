# Four State Custom Floors: Design System

Use this file as the single source of truth for every page on fourstatecustomfloors.com. Match it exactly. When something isn't covered here, follow the spirit: white space, big confident type, photos as the hero, green only where people click.

## The look in one sentence

Apple-style restraint applied to tile work: one idea per section, huge tight headlines, lots of white, edge-to-edge photos of finished showers, and close-up detail shots treated like product photography.

## Brand

- Business name: Four State Custom Floors (always written exactly this way)
- Owner: Tim Schmit
- Phone: 417-825-8240 (always a `tel:` link)
- Logo file: `/assets/four-state-logo.png` (green script "Four State" over black "CUSTOM FLOORS" on a four-state map outline). Use on white only. Header height 48px, footer height 56px. Never recolor, stretch or place on a photo.

## Design tokens

Drop this into the global stylesheet and use the variables everywhere. No hard-coded colors outside this block.

```css
:root {
  /* Color */
  --color-bg: #FFFFFF;          /* page background, always white */
  --color-bg-soft: #F6F7F5;     /* alternating section band */
  --color-surface: #F7F7F6;     /* detail-grid cards */
  --color-text: #121212;        /* headlines and body */
  --color-text-body: #3A3A3A;   /* long paragraphs */
  --color-text-muted: #4A4A4A;  /* subheads, card copy */
  --color-text-quiet: #5A5E58;  /* captions, town names, fine print */
  --color-green: #5BB648;       /* Tim's logo green: button fills ONLY */
  --color-green-text: #2C7A21;  /* green for text and links (passes contrast on white) */
  --color-green-hover: #1F5A17;
  --color-on-green: #0E0E0E;    /* text on green buttons */
  --color-border: #E6E6E6;      /* cards, form shell */
  --color-border-strong: #D5D6D3; /* inputs */
  --color-divider: #E3E3E3;     /* FAQ rules */
  --color-header-border: #ECECEC;

  /* Type */
  --font-sans: "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;

  /* Radius */
  --radius-hero: 32px;
  --radius-card: 28px;
  --radius-stat: 20px;
  --radius-input: 12px;
  --radius-pill: 999px;

  /* Layout */
  --container: 1240px;
  --gutter: 24px;
  --section-y: 120px;
  --gap-cards: 20px;
}
```

Load Inter from Google Fonts, weights 400, 500, 600, 700:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

Set `-webkit-font-smoothing: antialiased` on the body.

### Color rules

- Background is white. The only other band color is `--color-bg-soft`, used on every other section to create rhythm.
- `--color-green` (#5BB648) is for button backgrounds only, with black text on it. Never put green text on white with this shade; it fails contrast.
- Any green words (eyebrows, links, "Learn more", step numbers, stars) use `--color-green-text`.
- No gradients, no shadows, no dark sections. Contrast comes from type size and photos, not color.

## Typography

| Role | Size | Weight | Line height | Letter spacing |
| --- | --- | --- | --- | --- |
| H1 (hero) | `clamp(46px, 6.4vw, 92px)` | 700 | 1.02 | -0.035em |
| H2 (section) | `clamp(40px, 5vw, 72px)` (64px max in split sections) | 700 | 1.05 | -0.03em |
| H3 (large card) | 32px | 600 to 700 | 1.2 | -0.02em |
| H3 (card) | 22 to 26px | 600 to 700 | 1.2 | -0.02em |
| Answer block / lead | 28px | 500 | 1.4 | -0.01em |
| Subhead | 21px | 400 | 1.45 | 0 |
| Body | 17 to 19px | 400 | 1.55 | 0 |
| Eyebrow | 17px | 600, green text | 1.3 | 0 |
| Label / tag | 13px | 700, uppercase | 1.3 | 0.08em |
| Caption | 14 to 15px | 400, quiet color | 1.5 | 0 |
| Fine print | 12px | 400, quiet color | 1.5 | 0 |

Rules: headlines are short (3 to 9 words) and end with a period. Two or three weights per screen, max. Never center more than 3 lines of body text.

## Layout

- Content container: `max-width: var(--container); margin: 0 auto; padding-inline: var(--gutter)`.
- Vertical rhythm: `padding-block: var(--section-y)` per section. The hero is 96px top, 40px bottom.
- One idea per section. Each section = headline, at most one supporting sentence, then the visual.
- Alternate white and `--color-bg-soft` sections.
- Use flexbox with `flex-wrap: wrap` and `gap`, and give children flex-basis values (`flex: 2 1 560px`, `flex: 1 1 300px`, etc.) so layouts collapse naturally on phones. No breakpoint-heavy grids needed.
- Mobile first. Everything must work at 375px wide.

## Components

### Header
Sticky, white at 92% opacity, 1px bottom border `--color-header-border`. Logo left, nav center (14px / 500, gap 28px, black text, no underline), phone number (15px / 600) and green "Free Estimate" button right. On mobile, the nav collapses into a menu button and the phone plus Free Estimate stay visible.

### Buttons
- **Primary:** `background: var(--color-green); color: var(--color-on-green); font-weight: 600; border-radius: var(--radius-pill);` Large is 17px text with 16px x 30px padding. Small (header) is 14px with 11px x 20px padding and a 44px minimum height.
- **Text link CTA:** green text, 17px / 600, no underline, ends with " ›" (e.g. "Text Tim a photo of your shower ›").
- Never more than two CTAs side by side: one primary, one text link.

### Hero
Centered. Eyebrow, H1, subhead (max-width 640px), primary button plus text link, then a full-width photo below at 660px tall with `--radius-hero`.

### Answer block
Centered 28px / 500 paragraph, max-width 860px. It's the plain who/what/where summary written for AI search. It sits right under the hero photo.

### Stat tiles
1px border, `--radius-stat`, padding 22px x 28px, min-width 200px. Value at 30px / 700, label at 14px muted. Use 4 in a centered wrapping row.

### Detail ("Look closer") bento grid
Cards with `--color-surface` background, `--radius-card`, overflow hidden. Photo on top, then 20 to 30px padding with a short H3 like "Built-in niches." One large card (`flex: 2 1 560px`) plus a column of two small cards, then a row of three. Photos are macro close-ups of craftsmanship.

### Service cards
Whole card is a link. 1px border, `--radius-card`, photo on top (380px featured, 220px standard), then padding 24 to 30px with an optional uppercase green tag ("Our specialty"), H3, one line of copy and a green "Learn more ›". The custom tile shower card is always first and biggest.

### Steps (3-step plan)
On a `--color-bg-soft` band, text left and a tall photo right (600px). The numbers 1, 2, 3 are 44px / 700 green text, the step title is 22px / 600, the step detail is 17px muted. A thin divider plus the promise line goes underneath: "Tim on every job · Written quote, no surprises · Dust control · Full cleanup".

### Before and after
Two equal photos with `--radius-card`. On the live site, combine them into one drag-to-compare slider.

### Project cards
Photo 420px tall with `--radius-card`, then the title at 19px / 600 and the town at 15px in the quiet color. Always include a town name.

### Meet Tim
Soft band. Portrait left, text right: green eyebrow "Meet Tim Schmit", H2, body paragraph at 19px, small caption line.

### Review
Centered, max-width 1040px. Green stars, then a big pull quote at `clamp(28px, 3.4vw, 44px)` / 600, then the name and town, then "Read all reviews on Google ›". Show real reviews only, quoted word for word.

### FAQ
H2 left (1 part), questions right (2 parts). Each item has a top border `--color-divider` with 26px vertical padding, the question as an H3 at 21px / 600 and the answer at 17px muted. Answers are 1 to 3 sentences and lead with the direct answer. Write FAQs in real HTML, not hidden behind JavaScript, and add FAQPage schema.

### Town pills
White background, 1px border `#E0E1DE`, pill radius, 10px x 18px padding, 15px / 500.

### Estimate form
Lives on the homepage at `#estimate`. The form shell has a 1px border, `--radius-card` and 36px padding. Labels are 14px / 600 above the inputs. Inputs are 16px with 14px x 16px padding, a `--color-border-strong` border and `--radius-input`. Fields: Name, Phone, Town, Project (select), Photo upload (dashed border), Message. Full-width primary submit button. SMS consent fine print underneath with Privacy and Terms links (required for A2P texting).

### Footer
Top border, logo plus NAP (name, city, phone, matching the Google Business Profile character for character), a Services column and a "Find us" column (Google, Facebook, Houzz), then a copyright line with Privacy and Terms.

### Image placeholders (dev only)
Until real photos arrive, use a light grid placeholder with a centered white pill label saying what shot goes there:

```css
.ph{background-color:#F2F3F1;background-image:linear-gradient(#E3E6E1 1px,transparent 1px),linear-gradient(90deg,#E3E6E1 1px,transparent 1px);background-size:56px 56px;display:flex;align-items:center;justify-content:center}
.ph span{font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#5A5E58;background:#fff;padding:8px 14px;border-radius:999px}
```

## Photography rules

- Real jobs only. No stock photos, ever.
- Hero and service images: straight-on, symmetrical, natural light, glass wiped, toiletries removed.
- Detail shots: macro close-ups of corners, niches, grout lines, benches and drains.
- Export as AVIF or WebP, sized per breakpoint, `loading="lazy"` below the fold, and preload the hero.
- Use descriptive file names and alt text with the town, e.g. `walk-in-tile-shower-bench-carthage-mo.avif`.

## Motion

Subtle only: fade and rise 16px on scroll into view, one sticky photo section, and the before/after slider. Use CSS or IntersectionObserver with no heavy libraries. Disable all of it under `prefers-reduced-motion: reduce`.

## Voice (StoryBrand)

The homeowner is the hero and Tim is the guide. Write short, plain sentences with no fluff ("elevate your space" is banned). Be specific: towns, materials, days, price ranges. Headlines are confident and end with a period. Write for owners aged 35 to 65.

## Technical non-negotiables

- Static, server-rendered HTML. All content is readable without JavaScript.
- Core Web Vitals green on mobile (LCP < 2.5s, INP < 200ms, CLS < 0.1).
- One H1 per page, logical H2/H3 order, a unique title and meta description per page.
- JSON-LD schema: HomeAndConstructionBusiness, Person (Tim), Service, FAQPage and BreadcrumbList.
- robots.txt allows Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot and Claude-SearchBot.
- Accessibility: text contrast 4.5:1 minimum, touch targets 44px or larger, real `<button>`, `<a>`, `<label>` and `<input>` elements, alt text on every image.
- Mobile: a sticky bottom bar with "Call Tim" and "Free Estimate" on every page.

## Don'ts

- No em dashes in any copy.
- No gradients, drop shadows, dark sections, icon-in-circle grids or badge walls.
- No green text using #5BB648.
- No Apple fonts, logos, product names or copied layouts. We borrow the restraint, not the assets.
- No keyword stuffing in headlines or the business name.
