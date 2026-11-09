"""Generate the five service pages for fourstatecustomfloors from one template.
Usage (from the repo root): python3 tools/build_services.py .
Edit the SERVICES data here and re-run; it overwrites each <slug>/index.html.
"""
import html, json, os, sys

REPO = sys.argv[1]
SITE = "https://www.fourstatecustomfloors.com"
UPDATED = "November 2026"
STATES = ["Missouri", "Kansas", "Oklahoma", "Arkansas"]

SERVICES = [
  {
    "slug": "custom-tile-showers", "projects_sub": "Real showers Tim has built around the Four State area.", "nav": "Custom Tile Showers", "short": "Custom tile showers",
    "title": "Custom Tile Showers | Four State Custom Floors",
    "desc": "Walk-in, curbless and tub-to-shower conversions built by Tim Schmit. Fully waterproofed, dust-controlled demo, written quote. Call 417-825-8240.",
    "eyebrow": "Our specialty",
    "h1": "Custom tile showers in the Four State area.",
    "sub": "Walk-in, curbless and tub-to-shower conversions. Fully waterproofed and built by Tim, start to finish.",
    "hero_ph": "Hero: finished custom shower, straight on",
    "answer": "Four State Custom Floors builds custom tile showers for homeowners across Missouri, Kansas, Oklahoma and Arkansas. Most showers run [$X,XXX to $XX,XXX] and take [X to X] working days from demo to grout. Tim does the work himself, from tear-out and waterproofing to the last grout line.",
    "included_h": "What's included.",
    "included": [
      ("Dust-controlled demo", "The old shower or tub comes out with the room sealed off."),
      ("Full waterproofing", "[Waterproofing system] on every wall and the floor before any tile goes up."),
      ("Sloped pan and drain", "Built so water runs to the drain, not into the corners."),
      ("Tile install", "Walls, floor and ceiling if you want it, laid out before the first cut."),
      ("Niches and benches", "Built in and waterproofed with the rest of the shower."),
      ("Grout, sealing and cleanup", "You get the room back clean and ready to use."),
    ],
    "options_h": "Your shower, your way.",
    "options_sub": "A few of the styles Tim builds most.",
    "options": [
      ("Walk-in showers", "Open, easy to step into, no tub to climb over."),
      ("Curbless showers", "Flush with the bathroom floor. Great for aging in place."),
      ("Tub-to-shower conversions", "Swap the tub you never use for a real shower."),
      ("Niches and benches", "Storage and a place to sit, tiled in."),
      ("Tile patterns", "Stacked, offset, herringbone or vertical layouts."),
      ("Linear and square drains", "Clean lines that match the tile."),
    ],
    "steps_h": "How a shower gets built.",
    "steps": [
      ("Call or text Tim a photo.", "Send a picture of your current shower. Tim gets back to you [same day]."),
      ("Design and written quote.", "Tim measures, helps you pick the layout and tile, and puts the price in writing."),
      ("Demo and waterproofing.", "Old shower out, room sealed off, waterproofing in. About [X] days."),
      ("Tile, grout and cleanup.", "Tile goes up, grout gets sealed, and the room is cleaned. About [X] days."),
    ],
    "steps_ph": "Tall: Tim waterproofing a shower",
    "projects": ["Walk-in shower with niche and bench", "Curbless shower with linear drain", "Tub-to-shower conversion"],
    "faqs": [
      ("How much does a custom tile shower cost?", "Most custom tile showers Tim builds across the Four State area run [$X,XXX to $XX,XXX]. Size, tile choice, niches, benches and glass drive the price. You get a written quote before any work starts."),
      ("How long does a tile shower take?", "Most showers take [X to X] working days from demo to grout. Tim gives you the schedule in writing with your quote."),
      ("What waterproofing system do you use?", "Every shower gets [waterproofing system] behind the tile. It is a full membrane system, so water never reaches the studs or subfloor."),
      ("Can you turn my tub into a walk-in shower?", "Yes. Tub-to-shower conversions are one of the most common jobs Tim does. The tub comes out, the plumbing gets moved for the new drain [confirm who handles plumbing], and the shower is built in its place."),
      ("Can I use my bathroom during the job?", "Not the shower being rebuilt. If you have another bathroom, plan to use it for the [X to X] days the job takes."),
      ("Do you install the glass?", "[Answer to confirm with Tim: whether he installs glass or works with a glass company he trusts.]"),
      ("Do I have to pick out and buy the tile?", "[Answer to confirm with Tim: whether he supplies tile or sends you to a supplier he trusts.]"),
    ],
    "related": ["tile-flooring", "backsplashes", "dust-free-tile-removal"],
    "cta_h": "Ready for a new shower?",
    "cta_sub": "Text Tim a photo of the one you have now. He will tell you what it takes.",
  },
  {
    "slug": "tile-flooring", "projects_sub": "Real tile floors Tim has laid around the Four State area.", "nav": "Tile Floors", "short": "Tile floors",
    "title": "Tile Floor Installation | Four State Custom Floors",
    "desc": "Porcelain, ceramic and large format tile floors installed flat and tight by Tim Schmit across the Four State area. Call 417-825-8240.",
    "eyebrow": "Tile floors",
    "h1": "Tile floors in the Four State area.",
    "sub": "Porcelain, ceramic and large format tile. Flat, tight and built on a floor that is ready for it.",
    "hero_ph": "Hero: large format tile floor, wide shot",
    "answer": "Four State Custom Floors installs tile floors in kitchens, bathrooms, entries and whole homes across Missouri, Kansas, Oklahoma and Arkansas. Most tile floors run [$X to $X per square foot] installed and take [X to X] days, depending on size and prep. Tim checks and preps the subfloor first, because that is what keeps tile from cracking.",
    "included_h": "What's included.",
    "included": [
      ("Old floor removal", "Dust-controlled tear-out of tile, vinyl or carpet."),
      ("Subfloor check and prep", "Leveling and repairs so the tile sits flat."),
      ("Underlayment", "[Backer board or uncoupling membrane] under every tile floor."),
      ("Layout first", "Planned from the center of the room so cuts land where you will not see them."),
      ("Install and grout", "Tight grout lines, sealed when the job calls for it."),
      ("Transitions and cleanup", "Clean edges into the next room and a clean house when Tim leaves."),
    ],
    "options_h": "Floors Tim lays most.",
    "options_sub": "Every one starts with a flat, solid base.",
    "options": [
      ("Large format porcelain", "Big tiles, fewer grout lines, a clean modern look."),
      ("Wood-look tile", "The look of hardwood that does not mind water."),
      ("Patterned layouts", "Herringbone, chevron and offset patterns."),
      ("Bathroom floors", "Often paired with a new tile shower."),
      ("Kitchens and entries", "Hard-wearing floors for the busiest rooms."),
      ("Heated floors", "[Confirm with Tim: whether he installs in-floor heat.]"),
    ],
    "steps_h": "How a tile floor goes in.",
    "steps": [
      ("Call or text Tim a photo.", "Send a picture of the room and rough measurements if you have them."),
      ("Measure and written quote.", "Tim checks the subfloor, talks through tile and layout, and puts the price in writing."),
      ("Tear-out and prep.", "Old floor out with dust control, subfloor leveled and underlayment down."),
      ("Tile, grout and cleanup.", "Tile goes down, grout goes in, and the room is cleaned."),
    ],
    "steps_ph": "Tall: Tim setting large format tile",
    "projects": ["Large format porcelain kitchen floor", "Wood-look tile living room", "Herringbone bathroom floor"],
    "faqs": [
      ("How much does tile flooring cost?", "Most tile floors Tim installs run [$X to $X per square foot], including prep. Tile choice, layout pattern and subfloor repairs change the price. You get a written quote first."),
      ("How long does a tile floor take?", "A bathroom floor usually takes [X to X] days. A kitchen or larger area takes [X to X] days, plus time for the grout to cure before heavy use."),
      ("Can you tile over my existing floor?", "Sometimes, but usually not. Tim checks what is there first. Tiling over a bad floor is one of the main reasons tile cracks later."),
      ("Will large tiles be uneven?", "Not if the floor is flat and the tile is set right. Tim flattens the subfloor and uses [leveling system] so edges line up."),
      ("Do you move appliances and toilets?", "[Answer to confirm with Tim: whether he pulls and resets toilets and appliances.]"),
      ("Do I have to pick out and buy the tile?", "[Answer to confirm with Tim: whether he supplies tile or sends you to a supplier he trusts.]"),
    ],
    "related": ["custom-tile-showers", "vinyl-plank-and-hardwood", "dust-free-tile-removal"],
    "cta_h": "Ready for a new floor?",
    "cta_sub": "Send Tim a photo of the room and he will tell you what it takes.",
  },
  {
    "slug": "backsplashes", "projects_sub": "Real backsplashes Tim has installed around the Four State area.", "nav": "Backsplashes", "short": "Backsplashes",
    "title": "Kitchen Backsplash Installation | Four State Custom Floors",
    "desc": "Kitchen backsplashes installed clean and straight in a day or two by Tim Schmit across the Four State area. Call 417-825-8240.",
    "eyebrow": "Kitchen backsplashes",
    "h1": "Kitchen backsplashes in the Four State area.",
    "sub": "Subway, mosaic, handmade-look and full-height tile. Usually done in a day or two.",
    "hero_ph": "Hero: kitchen backsplash, straight on",
    "answer": "Four State Custom Floors installs kitchen backsplashes across Missouri, Kansas, Oklahoma and Arkansas. Most backsplashes run [$X to $X] and are done in [1 to 2] days. Tim protects your counters, cuts clean around outlets and windows, and finishes every edge.",
    "included_h": "What's included.",
    "included": [
      ("Counter and cabinet protection", "Everything covered before work starts."),
      ("Old backsplash removal", "If there is one, it comes out with dust control."),
      ("Wall prep", "Patched and flat so the tile sits straight."),
      ("Clean cuts", "Around outlets, switches and windows, with outlet extenders where needed."),
      ("Edge finish", "Trim or finished edges where the tile stops."),
      ("Grout, caulk and cleanup", "Sealed where needed and cleaned up the same day."),
    ],
    "options_h": "Backsplash styles.",
    "options_sub": "A few of the looks Tim installs most.",
    "options": [
      ("Subway tile", "Classic, clean and easy to live with."),
      ("Handmade-look tile", "Glossy, uneven tile with a lot of character."),
      ("Mosaics", "Small tile on sheets for a detailed look."),
      ("Full-height backsplash", "Tile from counter to ceiling or up to the hood."),
      ("Herringbone and patterns", "A little more work, a lot more interest."),
      ("Range feature wall", "A standout section behind the stove."),
    ],
    "steps_h": "How a backsplash goes in.",
    "steps": [
      ("Call or text Tim a photo.", "Send a picture of the wall and the counters."),
      ("Measure and written quote.", "Tim measures, talks through tile and layout, and puts the price in writing."),
      ("Install day.", "Counters protected, tile set, cuts made around every outlet."),
      ("Grout and cleanup.", "Grout, caulk and a clean kitchen, usually by day [two]."),
    ],
    "steps_ph": "Tall: backsplash detail around outlet",
    "projects": ["Subway tile backsplash", "Full-height backsplash to the hood", "Herringbone backsplash"],
    "faqs": [
      ("How much does a backsplash cost?", "Most kitchen backsplashes Tim installs run [$X to $X]. The size of the wall, the tile and the number of outlets and windows change the price."),
      ("How long does a backsplash take?", "Most are done in [1 to 2] days. Bigger or patterned jobs can take a day longer."),
      ("Do I need to clear off my counters?", "Yes, clear the counters along the wall being tiled. Tim covers them and the cabinets before he starts."),
      ("What happens with the outlets?", "Tim cuts around them and adds outlet extenders so the covers sit flush with the new tile."),
      ("Can you remove my old backsplash?", "Yes. Old tile comes out with dust control and the wall gets patched before the new tile goes up."),
      ("Do I have to pick out and buy the tile?", "[Answer to confirm with Tim: whether he supplies tile or sends you to a supplier he trusts.]"),
    ],
    "related": ["custom-tile-showers", "tile-flooring", "vinyl-plank-and-hardwood"],
    "cta_h": "Ready for a new backsplash?",
    "cta_sub": "Send Tim a photo of the wall and he will get back to you with next steps.",
  },
  {
    "slug": "vinyl-plank-and-hardwood", "projects_sub": "Real LVP and hardwood jobs from around the Four State area.", "nav": "LVP and Hardwood", "short": "LVP and hardwood",
    "title": "LVP and Hardwood Installation | Four State Custom Floors",
    "desc": "Luxury vinyl plank and hardwood floors installed right by Tim Schmit across the Four State area. Flat subfloor, clean trim. Call 417-825-8240.",
    "eyebrow": "LVP and hardwood",
    "h1": "LVP and hardwood floors in the Four State area.",
    "sub": "Luxury vinyl plank and hardwood, installed on a flat floor with clean trim and transitions.",
    "hero_ph": "Hero: LVP living room, wide shot",
    "answer": "Four State Custom Floors installs luxury vinyl plank (LVP) and hardwood floors across Missouri, Kansas, Oklahoma and Arkansas. Most installs run [$X to $X per square foot] and take [X to X] days for a typical home. Tim flattens the subfloor first so planks lock tight and do not bounce or gap.",
    "included_h": "What's included.",
    "included": [
      ("Old floor removal", "Carpet, vinyl or tile out, with dust control."),
      ("Subfloor flattening", "High spots ground down, low spots filled."),
      ("Underlayment and moisture barrier", "The right one for your floor and your subfloor."),
      ("Install", "Planks laid out so seams are staggered and the room looks right."),
      ("Trim and transitions", "Clean edges at doorways, tile and stairs. [Confirm baseboards and quarter round.]"),
      ("Cleanup", "Scraps hauled off and the floor cleaned."),
    ],
    "options_h": "Floors Tim installs.",
    "options_sub": "Pick the look and how much water it needs to handle.",
    "options": [
      ("Whole-house LVP", "One floor through the main living areas."),
      ("LVP in kitchens and baths", "Water-resistant floors where you need them most."),
      ("Engineered hardwood", "Real wood on top, stable in Four State humidity."),
      ("Solid hardwood", "[Confirm with Tim: prefinished only, or site-finished too.]"),
      ("Stairs", "[Confirm with Tim: whether he wraps stairs in LVP or hardwood.]"),
      ("Transitions to tile", "Clean lines where wood or LVP meets a tile floor."),
    ],
    "steps_h": "How a new floor goes in.",
    "steps": [
      ("Call or text Tim a photo.", "Send pictures of the rooms and a rough square footage if you know it."),
      ("Measure and written quote.", "Tim measures, checks the subfloor and puts the price in writing."),
      ("Tear-out and prep.", "Old floor out, subfloor flattened and underlayment down."),
      ("Install, trim and cleanup.", "Planks go down, trim goes on, and the house is cleaned."),
    ],
    "steps_ph": "Tall: LVP being installed",
    "projects": ["Whole-house LVP", "Engineered hardwood living room", "LVP kitchen and dining room"],
    "faqs": [
      ("Should I pick LVP or hardwood?", "LVP handles water, pets and kids better and usually costs less. Hardwood is real wood and can be refinished. Tim can walk you through which fits each room."),
      ("Is LVP waterproof?", "Most LVP is water-resistant to waterproof on the surface. Water can still get under it at the edges, so the install and transitions matter in kitchens and baths."),
      ("How long does it take?", "Most homes take [X to X] days depending on square footage and how much prep the subfloor needs."),
      ("How much does it cost?", "Most installs run [$X to $X per square foot] for labor and prep. Flooring, subfloor repairs and stairs change the price. You get a written quote first."),
      ("Do you move furniture?", "[Answer to confirm with Tim: whether he moves furniture or the homeowner clears the rooms.]"),
      ("Do I buy the flooring?", "[Answer to confirm with Tim: whether he supplies flooring or sends you to a supplier he trusts.]"),
    ],
    "related": ["tile-flooring", "dust-free-tile-removal", "custom-tile-showers"],
    "cta_h": "Ready for new floors?",
    "cta_sub": "Send Tim photos of the rooms and he will get back to you with next steps.",
  },
  {
    "slug": "dust-free-tile-removal", "projects_sub": "Real removal jobs from around the Four State area.", "nav": "Dust-Controlled Removal", "short": "Dust-controlled removal",
    "title": "Dust-Controlled Tile Removal | Four State Custom Floors",
    "desc": "Old tile out without dust through the whole house. Sealed work area, dust control equipment and full cleanup by Tim Schmit. Call 417-825-8240.",
    "eyebrow": "Dust-controlled removal",
    "h1": "Old tile out. Dust stays in the room.",
    "sub": "Tile removal with the work area sealed off, so the rest of your house stays clean.",
    "hero_ph": "Hero: sealed-off room during tile removal",
    "answer": "Four State Custom Floors removes old tile floors, shower walls and backsplashes with dust control across Missouri, Kansas, Oklahoma and Arkansas. Tim seals the work area with plastic walls and runs [dust control equipment] while he works, so the dust that normally covers a whole house stays in one room. Most removals take [X to X] days.",
    "included_h": "What's included.",
    "included": [
      ("Sealed work area", "Plastic walls and zip doors around the room."),
      ("Protected path", "Floor protection from the door to the work area."),
      ("Dust control equipment", "[Dust control equipment] running the whole time."),
      ("Tile and thinset removal", "Tile and the old adhesive or mortar bed come up."),
      ("Floor left ready", "Slab or subfloor cleaned up and ready for what is next."),
      ("Haul-off and cleanup", "Debris gone and the room vacuumed."),
    ],
    "options_h": "What Tim removes.",
    "options_sub": "Dust control on every one.",
    "options": [
      ("Tile floors", "Kitchens, bathrooms, entries and whole homes."),
      ("Shower walls and pans", "The first step of a new tile shower."),
      ("Backsplashes", "Old tile off the wall without wrecking the counters."),
      ("Mortar beds", "Old-school thick mortar floors, broken up and hauled out."),
      ("Tile on slab", "Ground down clean and ready for new flooring."),
      ("Tile on wood subfloor", "Removed and checked for damage underneath."),
    ],
    "steps_h": "How dust-controlled removal works.",
    "steps": [
      ("Call or text Tim a photo.", "Send a picture of the tile that needs to come out."),
      ("Walkthrough and written quote.", "Tim checks the floor or wall and puts the price in writing."),
      ("Seal and remove.", "Room sealed off, dust control running, old tile out."),
      ("Clean up and next steps.", "Debris hauled away and the space left ready for the new install."),
    ],
    "steps_ph": "Tall: containment wall with zip door",
    "projects": ["Kitchen tile floor removal", "Shower tear-out before rebuild", "Whole-house tile removal on slab"],
    "faqs": [
      ("Is it really dust-free?", "No removal is completely dust-free, so we call it dust-controlled. With the room sealed and [dust control equipment] running, the dust stays in the work area instead of spreading through the house."),
      ("Can I stay home during removal?", "Yes. The work area is sealed off, so most homeowners stay home. It is loud while tile is coming up."),
      ("How long does tile removal take?", "Most rooms take [X to X] days. Whole-house removal or thick mortar beds take longer."),
      ("Do you haul the old tile away?", "Yes. Debris is hauled off and the work area is cleaned before Tim leaves."),
      ("Can you just remove tile without installing new flooring?", "[Answer to confirm with Tim: whether he takes removal-only jobs.]"),
      ("What does removal cost?", "Most removals run [$X to $X per square foot]. Thick mortar beds and glued-down tile cost more. You get a written quote first."),
    ],
    "related": ["tile-flooring", "custom-tile-showers", "vinyl-plank-and-hardwood"],
    "cta_h": "Ready to get the old tile out?",
    "cta_sub": "Send Tim a photo and he will tell you what it takes.",
  },
]
BY_SLUG = {s["slug"]: s for s in SERVICES}
CARD_PH = {
  "custom-tile-showers": "Custom tile shower", "tile-flooring": "Tile floor",
  "backsplashes": "Backsplash", "vinyl-plank-and-hardwood": "LVP / hardwood",
  "dust-free-tile-removal": "Dust-controlled demo",
}
CARD_LINE = {
  "custom-tile-showers": "Walk-in, curbless and tub-to-shower, fully waterproofed.",
  "tile-flooring": "Porcelain and large format tile, flat and tight.",
  "backsplashes": "Kitchen backsplashes done in a day or two.",
  "vinyl-plank-and-hardwood": "Vinyl plank and hardwood, installed right.",
  "dust-free-tile-removal": "Old tile out. Dust stays in the room.",
}

e = html.escape

def header(p):
  return f'''  <a class="skip-link" href="#main">Skip to content</a>

  <!-- ===== Header ===== -->
  <header class="site-header">
    <div class="container header-inner">
      <a class="logo" href="{p}">
        <img src="{p}assets/four-state-logo.png" alt="Four State Custom Floors" width="139" height="60">
      </a>

      <nav class="nav" aria-label="Main">
        <ul>
          <li><a href="{p}#services">Services</a></li>
          <li><a href="{p}#projects">Projects</a></li>
          <li><a href="{p}#about">About</a></li>
          <li><a href="{p}#reviews">Reviews</a></li>
          <li><a href="{p}#faq">FAQ</a></li>
        </ul>
      </nav>

      <div class="header-actions">
        <a class="header-phone desk-only" href="tel:+14178258240">417-825-8240</a>
        <a class="btn btn--sm desk-only" href="{p}#estimate">Free Estimate</a>
        <details class="menu">
          <summary aria-label="Open menu"><i></i></summary>
          <div class="menu-panel">
            <nav aria-label="Mobile">
              <a href="{p}#services">Services</a>
              <a href="{p}#projects">Projects</a>
              <a href="{p}#about">About</a>
              <a href="{p}#reviews">Reviews</a>
              <a href="{p}#faq">FAQ</a>
            </nav>
            <div class="menu-ctas">
              <a class="btn btn--block" href="{p}#estimate">Get a Free Estimate</a>
              <a class="btn btn--outline btn--block" href="tel:+14178258240">Call Tim at 417-825-8240</a>
            </div>
          </div>
        </details>
      </div>
    </div>
  </header>
'''

def footer(p):
  links = "\n".join(f'            <li><a href="{p}{s["slug"]}/">{s["nav"]}</a></li>' for s in SERVICES)
  return f'''  <!-- ===== Footer ===== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-top">
        <div class="footer-brand">
          <a class="logo" href="{p}">
            <img src="{p}assets/four-state-logo.png" alt="Four State Custom Floors" width="148" height="64" loading="lazy">
          </a>
          <address class="nap">
            Four State Custom Floors<br>
            Noel, MO<br>
            <a href="tel:+14178258240">417-825-8240</a>
          </address>
        </div>
        <nav class="footer-col" aria-label="Services">
          <h2>Services</h2>
          <ul>
{links}
          </ul>
        </nav>
        <nav class="footer-col" aria-label="Find us">
          <h2>Find us</h2>
          <ul>
            <li><a href="#" rel="noopener">Google</a></li>
            <li><a href="#" rel="noopener">Facebook</a></li>
            <li><a href="#" rel="noopener">Houzz</a></li>
          </ul>
        </nav>
      </div>
      <div class="footer-bottom fine">
        <span>© 2026 Four State Custom Floors. All rights reserved.</span>
        <span><a href="{p}privacy">Privacy</a> · <a href="{p}terms">Terms</a></span>
      </div>
    </div>
  </footer>

  <!-- ===== Mobile sticky bar ===== -->
  <div class="mobile-bar">
    <a class="btn btn--outline" href="tel:+14178258240">Call Tim</a>
    <a class="btn" href="{p}#estimate">Free Estimate</a>
  </div>

  <script src="{p}assets/main.js" defer></script>
</body>
</html>
'''

def schema(s):
  url = f"{SITE}/{s['slug']}/"
  g = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Service",
        "name": s["nav"],
        "serviceType": s["nav"],
        "url": url,
        "description": s["answer"],
        "provider": {"@type": "HomeAndConstructionBusiness", "@id": f"{SITE}/#business", "name": "Four State Custom Floors", "telephone": "+1-417-825-8240"},
        "areaServed": [{"@type": "State", "name": st} for st in STATES],
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
          {"@type": "ListItem", "position": 2, "name": s["nav"], "item": url},
        ],
      },
      {
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faqs"]],
      },
    ],
  }
  return json.dumps(g, indent=2, ensure_ascii=False)

def page(s):
  p = "../"
  inc = "\n".join(f'          <li><span class="check" aria-hidden="true">✓</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>' for t, d in s["included"])
  opts = "\n".join(f'''          <article class="bento-card bento-third reveal">
            <div class="ph" role="img" aria-label="{e(t)}"><span>{e(t)}</span></div>
            <div class="bento-text"><h3 class="h3">{e(t)}.</h3><p>{e(d)}</p></div>
          </article>''' for t, d in s["options"])
  steps = "\n".join(f'''            <li class="step">
              <span class="step-num" aria-hidden="true">{i}</span>
              <div>
                <h3>{e(t)}</h3>
                <p>{e(d)}</p>
              </div>
            </li>''' for i, (t, d) in enumerate(s["steps"], 1))
  projs = "\n".join(f'''          <article class="project reveal">
            <div class="ph" role="img" aria-label="{e(t)}"><span>Project photo</span></div>
            <h3>{e(t)}</h3>
            <p class="caption">[Town, ST]</p>
          </article>''' for t in s["projects"])
  faqs = "\n".join(f'''          <div class="faq-item">
            <h3>{e(q)}</h3>
            <p>{e(a)}</p>
          </div>''' for q, a in s["faqs"])
  rel = "\n".join(f'''          <a class="card-link svc reveal" href="{p}{r}/">
            <div class="ph" role="img" aria-label="{e(BY_SLUG[r]['nav'])}"><span>{e(CARD_PH[r])}</span></div>
            <div class="card-body">
              <h3 class="h3">{e(BY_SLUG[r]['short'])}.</h3>
              <p>{e(CARD_LINE[r])}</p>
              <span class="more">Learn more ›</span>
            </div>
          </a>''' for r in s["related"])
  url = f"{SITE}/{s['slug']}/"
  return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(s["title"])}</title>
  <meta name="description" content="{e(s["desc"])}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#FFFFFF">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(s["title"])}">
  <meta property="og:description" content="{e(s["desc"])}">
  <meta property="og:url" content="{url}">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}assets/styles.css">

  <script type="application/ld+json">
{schema(s)}
  </script>
</head>
<body>
{header(p)}
  <main id="main">

    <!-- ===== Hero ===== -->
    <section class="hero page-hero">
      <div class="container">
        <nav class="crumbs" aria-label="Breadcrumb">
          <ol>
            <li><a href="{p}">Home</a></li>
            <li aria-current="page">{e(s["nav"])}</li>
          </ol>
        </nav>
        <p class="eyebrow">{e(s["eyebrow"])}</p>
        <h1 class="h1">{e(s["h1"])}</h1>
        <p class="subhead">{e(s["sub"])}</p>
        <div class="cta-row">
          <a class="btn" href="{p}#estimate">Get a Free Estimate</a>
          <a class="link-cta" href="sms:+14178258240">Text Tim a photo&nbsp;›</a>
        </div>
        <div class="hero-photo ph" role="img" aria-label="{e(s["nav"])} by Four State Custom Floors">
          <span>{e(s["hero_ph"])}</span>
        </div>
      </div>
    </section>

    <!-- ===== Answer block ===== -->
    <section class="answer" aria-label="About this service">
      <div class="container">
        <p class="lead reveal">{e(s["answer"])}</p>
        <p class="caption updated">Last updated {UPDATED}</p>
      </div>
    </section>

    <!-- ===== What's included ===== -->
    <section class="section band-soft" aria-labelledby="inc-h">
      <div class="container split split--top">
        <div class="faq-head reveal">
          <h2 class="h2 h2--split" id="inc-h">{e(s["included_h"])}</h2>
          <p class="subhead">Tim on every job, a written quote and a full cleanup, every time.</p>
        </div>
        <ul class="check-list reveal">
{inc}
        </ul>
      </div>
    </section>

    <!-- ===== Options ===== -->
    <section class="section" aria-labelledby="opt-h">
      <div class="container">
        <div class="section-head reveal">
          <h2 class="h2" id="opt-h">{e(s["options_h"])}</h2>
          <p class="subhead">{e(s["options_sub"])}</p>
        </div>
        <div class="grid">
{opts}
        </div>
      </div>
    </section>

    <!-- ===== Process ===== -->
    <section class="section band-soft" aria-labelledby="proc-h">
      <div class="container split">
        <div class="split-text reveal">
          <h2 class="h2 h2--split" id="proc-h">{e(s["steps_h"])}</h2>
          <ol class="steps">
{steps}
          </ol>
          <p class="promise">Tim on every job · Written quote, no surprises · Dust control · Full cleanup</p>
        </div>
        <div class="split-media reveal">
          <div class="steps-photo ph" role="img" aria-label="{e(s["steps_ph"])}"><span>{e(s["steps_ph"])}</span></div>
        </div>
      </div>
    </section>

    <!-- ===== Projects ===== -->
    <section class="section" aria-labelledby="proj-h">
      <div class="container">
        <div class="section-head reveal">
          <h2 class="h2" id="proj-h">Recent jobs.</h2>
          <p class="subhead">{e(s["projects_sub"])}</p>
        </div>
        <div class="grid">
{projs}
        </div>
      </div>
    </section>

    <!-- ===== FAQ ===== -->
    <section class="section band-soft" id="faq">
      <div class="container split split--top">
        <div class="faq-head reveal">
          <h2 class="h2 h2--split">Questions, answered.</h2>
          <p class="subhead">Still wondering? Call Tim at <a class="link-cta" style="display:inline;font-size:inherit;white-space:nowrap" href="tel:+14178258240">417-825-8240</a>.</p>
        </div>
        <div class="faq-list reveal">
{faqs}
        </div>
      </div>
    </section>

    <!-- ===== Related services ===== -->
    <section class="section" aria-labelledby="rel-h">
      <div class="container">
        <div class="section-head reveal">
          <h2 class="h2" id="rel-h">More from Tim.</h2>
        </div>
        <div class="grid">
{rel}
        </div>
      </div>
    </section>

    <!-- ===== Final CTA ===== -->
    <section class="section band-soft final-cta">
      <div class="container">
        <div class="section-head reveal">
          <h2 class="h2">{e(s["cta_h"])}</h2>
          <p class="subhead">{e(s["cta_sub"])}</p>
        </div>
        <div class="cta-row reveal">
          <a class="btn" href="{p}#estimate">Get a Free Estimate</a>
          <a class="link-cta" href="tel:+14178258240">Call Tim at 417-825-8240&nbsp;›</a>
        </div>
      </div>
    </section>
  </main>

{footer(p)}'''

for s in SERVICES:
  d = os.path.join(REPO, s["slug"])
  os.makedirs(d, exist_ok=True)
  with open(os.path.join(d, "index.html"), "w") as f:
    f.write(page(s))
  print("wrote", s["slug"])
