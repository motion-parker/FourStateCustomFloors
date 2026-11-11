"""Generate the five service pages for fourstatecustomfloors from one template.
Usage (from the repo root): python3 tools/build_services.py .
Edit the SERVICES data here and re-run; it overwrites each <slug>/index.html.

Copy rules (StoryBrand): the homeowner is the hero, we are the guide.
Say "we" in body copy. Name Tim only in the answer block (so search and AI
tools can tie the owner to the business). Keep the business name written out
in full: "Four State Custom Floors". Anything Tim has not confirmed stays in
[brackets] or is listed in docs/for-tim-to-confirm.md.
"""
import html, json, os, sys

REPO = sys.argv[1]
SITE = "https://www.fourstatecustomfloors.com"
UPDATED = "November 2026"
STATES = ["Missouri", "Kansas", "Oklahoma", "Arkansas"]

SERVICES = [
  {
    "slug": "custom-tile-showers", "nav": "Custom Tile Showers", "short": "Custom tile showers",
    "projects_sub": "Real showers we've built around the Four State area.",
    "title": "Custom Tile Showers | Four State Custom Floors",
    "desc": "Walk-in showers and tub-to-shower conversions, fully waterproofed. 25+ years of tile work, a written quote up front and dust-controlled demo. Call 417-825-8240.",
    "eyebrow": "Our specialty",
    "h1": "Custom tile showers in the Four State area.",
    "sub": "Get the shower you've been picturing, built by a tile setter with 25+ years in the trade and waterproofed to stay dry for decades. No leaks, no surprises, no dust through the house.",
    "hero_ph": "Hero: finished custom shower, straight on",
    "answer": "Four State Custom Floors builds custom tile showers for homeowners across Missouri, Kansas, Oklahoma and Arkansas. The company is owned by Tim Schmit, who has set tile for 25+ years and is on every job. Most showers run [$X,XXX to $XX,XXX] and take [X to X] working days from demo to grout.",
    "included_h": "What's included.",
    "included": [
      ("Dust-controlled demo", "Your old shower or tub comes out with the room sealed off from the rest of the house."),
      ("Waterproofing", "[Waterproofing system] goes on the walls and floor before any tile goes up."),
      ("Sloped pan and drain", "Water runs to the drain instead of sitting in the corners."),
      ("Tile install", "We plan the layout with you before the first cut."),
      ("Niches and benches", "Built in and waterproofed along with the rest of the shower."),
      ("Grout and cleanup", "You get your bathroom back clean and ready to use."),
    ],
    "options_h": "What your shower could look like.",
    "options_sub": "A few of the styles homeowners ask us for most.",
    "options": [
      ("Walk-in showers", "Easy to step into, with no tub to climb over."),
      ("Curbless showers", "Level with the bathroom floor, so there's nothing to trip on."),
      ("Tub-to-shower conversions", "Trade the tub you never use for a shower you'll use every day."),
      ("Niches and benches", "A place for your shampoo and a place to sit."),
      ("Tile patterns", "Stacked, offset, herringbone or vertical layouts."),
      ("Drain styles", "Linear or square drains to match your tile."),
    ],
    "steps_h": "How your shower gets built.",
    "steps": [
      ("Send us a photo.", "Text or call with a picture of your current shower. We'll get back to you [same day]."),
      ("Get a design and written quote.", "We measure, help you choose the layout and tile, and put the price in writing."),
      ("Demo and waterproofing.", "The old shower comes out, the room stays sealed off, and the waterproofing goes in."),
      ("Tile, grout and cleanup.", "The tile goes up, the grout goes in, and we clean up before we leave."),
    ],
    "steps_ph": "Tall: waterproofing going on before tile",
    "projects": ["Walk-in shower with niche and bench", "Curbless shower with linear drain", "Tub-to-shower conversion"],
    "faqs": [
      ("How much does a custom tile shower cost?", "Most custom tile showers we build across the Four State area run [$X,XXX to $XX,XXX]. Size, tile choice, niches, benches and glass drive the price. You get a written quote before any work starts."),
      ("How long does a tile shower take?", "Most showers take [X to X] working days from demo to grout. You get the schedule in writing with your quote."),
      ("What waterproofing system do you use?", "Every shower gets [waterproofing system] behind the tile, so water stays away from the studs and subfloor."),
      ("Can you turn my tub into a walk-in shower?", "Yes. The tub comes out and a tile shower is built in its place. [Confirm with Tim: who handles moving the drain and plumbing.]"),
      ("Can I use my bathroom during the job?", "Not the shower being rebuilt. If you have another bathroom, plan to use it while the job is underway."),
      ("Do you install the glass?", "[Answer to confirm with Tim: whether we install glass or work with a glass company we trust.]"),
      ("Do I have to pick out and buy the tile?", "[Answer to confirm with Tim: whether we supply tile or send you to a supplier we trust.]"),
    ],
    "related": ["tile-flooring", "backsplashes", "dust-free-tile-removal"],
    "cta_h": "Ready for a shower you love walking into?",
    "cta_sub": "Send us a photo of the one you have now and we'll tell you what it takes.",
  },
  {
    "slug": "tile-flooring", "nav": "Tile Floors", "short": "Tile floors",
    "projects_sub": "Real tile floors we've laid around the Four State area.",
    "title": "Tile Floor Installation | Four State Custom Floors",
    "desc": "Porcelain, ceramic and large format tile floors, set flat on a properly prepped subfloor across the Four State area. Call 417-825-8240.",
    "eyebrow": "Tile floors",
    "h1": "Tile floors in the Four State area.",
    "sub": "A tile floor that looks great on day one and still looks great in year twenty. 25+ years of setting tile taught us it all starts under the tile.",
    "hero_ph": "Hero: large format tile floor, wide shot",
    "answer": "Four State Custom Floors installs tile floors in kitchens, bathrooms, entries and whole homes across Missouri, Kansas, Oklahoma and Arkansas. The company is owned by Tim Schmit, who has set tile for 25+ years. Most tile floors run [$X to $X per square foot] installed and take [X to X] days. We check and prep the subfloor first, because that's what keeps tile from cracking.",
    "included_h": "What's included.",
    "included": [
      ("Old floor removal", "Your old tile, vinyl or carpet comes out with dust control."),
      ("Subfloor prep", "We level and repair the floor so your tile sits flat."),
      ("Underlayment", "[Underlayment we use] goes down under every tile floor."),
      ("Layout first", "We plan the layout so cuts land where you won't notice them."),
      ("Install and grout", "Even grout lines, sealed when the tile calls for it."),
      ("Transitions and cleanup", "Clean edges into the next room and a clean house when we leave."),
    ],
    "options_h": "Floors homeowners ask for.",
    "options_sub": "Every one starts with a flat, solid base. That's the part 25+ years taught us never to rush.",
    "options": [
      ("Large format porcelain", "Bigger tiles and fewer grout lines for a clean look."),
      ("Wood-look tile", "The look of hardwood in rooms that get wet."),
      ("Patterned layouts", "Herringbone, chevron and offset patterns."),
      ("Bathroom floors", "Often done along with a new tile shower."),
      ("Kitchens and entries", "Hard-wearing floors for your busiest rooms."),
      ("Heated floors", "[Confirm with Tim: whether we install in-floor heat.]"),
    ],
    "steps_h": "How your new floor goes in.",
    "steps": [
      ("Send us a photo.", "Text or call with a picture of the room and rough measurements if you have them."),
      ("Get a written quote.", "We check the subfloor, talk through tile and layout, and put the price in writing."),
      ("Tear-out and prep.", "Your old floor comes out with dust control and the subfloor gets prepped."),
      ("Tile, grout and cleanup.", "The tile goes down, the grout goes in, and we clean up before we leave."),
    ],
    "steps_ph": "Tall: large format tile being set",
    "projects": ["Large format porcelain kitchen floor", "Wood-look tile living room", "Herringbone bathroom floor"],
    "faqs": [
      ("How much does tile flooring cost?", "Most tile floors we install run [$X to $X per square foot], including prep. Tile choice, layout and subfloor repairs change the price. You get a written quote first."),
      ("How long does a tile floor take?", "A bathroom floor usually takes [X to X] days. A kitchen or larger area takes [X to X] days, plus time for the grout to cure."),
      ("Can you tile over my existing floor?", "Usually not. We check what's there first, because tiling over a bad floor is one of the main reasons tile cracks later."),
      ("Will large tiles be uneven?", "Not on a flat floor with the tile set right. We prep the subfloor so the edges line up."),
      ("Do you move appliances and toilets?", "[Answer to confirm with Tim: whether we pull and reset toilets and appliances.]"),
      ("Do I have to pick out and buy the tile?", "[Answer to confirm with Tim: whether we supply tile or send you to a supplier we trust.]"),
    ],
    "related": ["custom-tile-showers", "vinyl-plank-and-hardwood", "dust-free-tile-removal"],
    "cta_h": "Ready for a floor you never have to think about?",
    "cta_sub": "Send us a photo of the room and we'll tell you what it takes.",
  },
  {
    "slug": "backsplashes", "nav": "Backsplashes", "short": "Backsplashes",
    "projects_sub": "Real backsplashes we've installed around the Four State area.",
    "title": "Kitchen Backsplash Installation | Four State Custom Floors",
    "desc": "Kitchen tile backsplashes with clean cuts and finished edges across the Four State area. Written quote up front. Call 417-825-8240.",
    "eyebrow": "Backsplashes across the Four State area",
    "h1": "Kitchen backsplashes.",
    "sub": "Finish your kitchen with a backsplash that looks like it was always meant to be there: straight lines, clean cuts and edges that look finished, set by hands with 25+ years of practice.",
    "hero_ph": "Hero: kitchen backsplash, straight on",
    "answer": "Four State Custom Floors installs kitchen tile backsplashes across Missouri, Kansas, Oklahoma and Arkansas. The company is owned by Tim Schmit, who has set tile for 25+ years. Most backsplashes run [$X to $X] and take [X to X] days. We protect your counters, cut clean around outlets and windows, and finish every edge.",
    "included_h": "What's included.",
    "included": [
      ("Counter and cabinet protection", "Everything gets covered before we start."),
      ("Old backsplash removal", "If you have one, it comes out with dust control."),
      ("Wall prep", "We patch and flatten the wall so your tile sits straight."),
      ("Clean cuts", "Around outlets, switches and windows."),
      ("Finished edges", "Clean trim or finished edges where the tile stops."),
      ("Grout, caulk and cleanup", "Your kitchen is cleaned up before we leave."),
    ],
    "options_h": "Backsplash styles.",
    "options_sub": "A few of the looks homeowners ask for most.",
    "options": [
      ("Subway tile", "Classic, clean and easy to live with."),
      ("Handmade-look tile", "Glossy, slightly uneven tile with a lot of character."),
      ("Mosaics", "Small tiles on sheets for a detailed look."),
      ("Full-height backsplash", "Tile from the counter to the ceiling or up to the hood."),
      ("Herringbone and patterns", "A little more work for a lot more interest."),
      ("Range feature wall", "A standout section behind your stove."),
    ],
    "steps_h": "How your backsplash goes in.",
    "steps": [
      ("Send us a photo.", "Text or call with a picture of the wall and your counters."),
      ("Get a written quote.", "We measure, talk through tile and layout, and put the price in writing."),
      ("Install day.", "Your counters get covered, the tile goes up, and every outlet gets a clean cut."),
      ("Grout and cleanup.", "We grout, caulk and leave your kitchen clean."),
    ],
    "steps_ph": "Tall: backsplash detail around an outlet",
    "projects": ["Subway tile backsplash", "Full-height backsplash to the hood", "Herringbone backsplash"],
    "faqs": [
      ("How much does a backsplash cost?", "Most kitchen backsplashes we install run [$X to $X]. The size of the wall, the tile and the number of outlets and windows change the price."),
      ("How long does a backsplash take?", "Most take [X to X] days. Bigger or patterned jobs can take longer."),
      ("Do I need to clear off my counters?", "Yes, clear the counters along the wall being tiled. We cover them and your cabinets before we start."),
      ("What happens with the outlets?", "We cut around them so the covers sit flush with the new tile. [Confirm with Tim: whether we add outlet extenders.]"),
      ("Can you remove my old backsplash?", "Yes. The old tile comes out with dust control and the wall gets patched before the new tile goes up."),
      ("Do I have to pick out and buy the tile?", "[Answer to confirm with Tim: whether we supply tile or send you to a supplier we trust.]"),
    ],
    "related": ["custom-tile-showers", "tile-flooring", "vinyl-plank-and-hardwood"],
    "cta_h": "Ready to finish your kitchen?",
    "cta_sub": "Send us a photo of the wall and we'll get back to you with next steps.",
  },
  {
    "slug": "vinyl-plank-and-hardwood", "nav": "LVP and Hardwood", "short": "LVP and hardwood",
    "projects_sub": "Real LVP and hardwood jobs from around the Four State area.",
    "title": "LVP and Hardwood Installation | Four State Custom Floors",
    "desc": "Luxury vinyl plank and hardwood floors installed on a flat, prepped subfloor with clean trim across the Four State area. Call 417-825-8240.",
    "eyebrow": "Flooring across the Four State area",
    "h1": "LVP and hardwood floors.",
    "sub": "New floors that lie flat, lock tight and don't bounce, gap or squeak. Same 25+ years of care we put into every tile job.",
    "hero_ph": "Hero: LVP living room, wide shot",
    "answer": "Four State Custom Floors installs luxury vinyl plank (LVP) and hardwood floors across Missouri, Kansas, Oklahoma and Arkansas. The company is owned by Tim Schmit, who has 25+ years in the trade. Most installs run [$X to $X per square foot] and take [X to X] days for a typical home. We flatten the subfloor first so your new floor lies flat and stays tight.",
    "included_h": "What's included.",
    "included": [
      ("Old floor removal", "Carpet, vinyl or tile comes out with dust control."),
      ("Subfloor prep", "We fix high and low spots so the floor lies flat."),
      ("Underlayment", "The right underlayment for your floor and subfloor."),
      ("Install", "Seams staggered so the room looks right."),
      ("Trim and transitions", "Clean edges at doorways and where your new floor meets tile. [Confirm with Tim: baseboards and quarter round.]"),
      ("Cleanup", "Scraps hauled off and your floor cleaned."),
    ],
    "options_h": "Floors homeowners ask for.",
    "options_sub": "Pick the look you want and how much water it needs to handle.",
    "options": [
      ("Whole-house LVP", "One floor through your main living areas."),
      ("LVP in kitchens and baths", "Water-resistant floors where you need them most."),
      ("Engineered hardwood", "Real wood on top with a stable core underneath."),
      ("Solid hardwood", "[Confirm with Tim: prefinished only, or site-finished too.]"),
      ("Stairs", "[Confirm with Tim: whether we do stairs in LVP or hardwood.]"),
      ("Transitions to tile", "Clean lines where your new floor meets tile."),
    ],
    "steps_h": "How your new floor goes in.",
    "steps": [
      ("Send us a photo.", "Text or call with pictures of the rooms and a rough square footage if you know it."),
      ("Get a written quote.", "We measure, check the subfloor and put the price in writing."),
      ("Tear-out and prep.", "Your old floor comes out and the subfloor gets flattened."),
      ("Install, trim and cleanup.", "The new floor goes down, the trim goes on, and we clean up before we leave."),
    ],
    "steps_ph": "Tall: LVP being installed",
    "projects": ["Whole-house LVP", "Engineered hardwood living room", "LVP kitchen and dining room"],
    "faqs": [
      ("Should I pick LVP or hardwood?", "LVP handles water, pets and kids better and usually costs less. Hardwood is real wood and can be refinished. We'll help you decide what fits each room."),
      ("Is LVP waterproof?", "Most LVP is water-resistant on the surface, but water can still get under it at the edges. That's why the install and transitions matter in kitchens and baths."),
      ("How long does it take?", "Most homes take [X to X] days, depending on square footage and how much subfloor prep is needed."),
      ("How much does it cost?", "Most installs run [$X to $X per square foot] for labor and prep. Flooring, subfloor repairs and stairs change the price. You get a written quote first."),
      ("Do you move furniture?", "[Answer to confirm with Tim: whether we move furniture or you clear the rooms.]"),
      ("Do I buy the flooring?", "[Answer to confirm with Tim: whether we supply flooring or send you to a supplier we trust.]"),
    ],
    "related": ["tile-flooring", "dust-free-tile-removal", "custom-tile-showers"],
    "cta_h": "Ready for floors that feel solid underfoot?",
    "cta_sub": "Send us photos of the rooms and we'll get back to you with next steps.",
  },
  {
    "slug": "dust-free-tile-removal", "nav": "Dust-Controlled Removal", "short": "Dust-controlled removal",
    "projects_sub": "Real removal jobs from around the Four State area.",
    "title": "Dust-Controlled Tile Removal | Four State Custom Floors",
    "desc": "Old tile removed with the work area sealed off and dust control running, so the rest of your house stays clean. Call 417-825-8240.",
    "eyebrow": "Dust-controlled removal across the Four State area",
    "h1": "Tile removal without the dust.",
    "sub": "We seal off the room so the dust stays where the work is, not on your furniture, vents and floors. Your house stays livable while the old tile comes out.",
    "hero_ph": "Hero: sealed-off room during tile removal",
    "answer": "Four State Custom Floors removes old tile floors, shower walls and backsplashes with dust control across Missouri, Kansas, Oklahoma and Arkansas. The company is owned by Tim Schmit, who has 25+ years in the trade. We seal off the work area and run [dust control equipment], so the dust that normally covers a whole house stays in one room. Most removals take [X to X] days.",
    "included_h": "What's included.",
    "included": [
      ("Sealed work area", "The room gets closed off from the rest of your house."),
      ("Protected path", "We cover the floor from your door to the work area."),
      ("Dust control equipment", "[Dust control equipment] runs the whole time."),
      ("Tile and adhesive removal", "Your old tile and what's holding it down come up."),
      ("Floor left ready", "The slab or subfloor is cleaned up and ready for what's next."),
      ("Haul-off and cleanup", "Debris is hauled away and the room is cleaned."),
    ],
    "options_h": "What we remove.",
    "options_sub": "Dust control on every one.",
    "options": [
      ("Tile floors", "Kitchens, bathrooms, entries and whole homes."),
      ("Shower walls and pans", "The first step toward a new tile shower."),
      ("Backsplashes", "Old tile off the wall without damaging your counters."),
      ("Mortar beds", "Thick mortar floors broken up and hauled out."),
      ("Tile on slab", "Removed and cleaned up, ready for new flooring."),
      ("Tile on wood subfloor", "Removed and checked for damage underneath."),
    ],
    "steps_h": "How dust-controlled removal works.",
    "steps": [
      ("Send us a photo.", "Text or call with a picture of the tile that needs to come out."),
      ("Get a written quote.", "We look at the floor or wall and put the price in writing."),
      ("Seal and remove.", "The room gets sealed off, dust control runs, and your old tile comes out."),
      ("Clean up.", "Debris is hauled away and the space is ready for your new floor or shower."),
    ],
    "steps_ph": "Tall: sealed-off room during removal",
    "projects": ["Kitchen tile floor removal", "Shower tear-out before rebuild", "Whole-house tile removal on slab"],
    "faqs": [
      ("Is it really dust-free?", "No removal is completely dust-free, which is why we call it dust-controlled. With the room sealed and [dust control equipment] running, the dust stays in the work area instead of spreading through your house."),
      ("Can I stay home during removal?", "Yes. The work area is sealed off, so most homeowners stay home. It is loud while the tile is coming up."),
      ("How long does tile removal take?", "Most rooms take [X to X] days. Whole-house removal and thick mortar beds take longer."),
      ("Do you haul the old tile away?", "Yes. Debris is hauled off and the work area is cleaned before we leave."),
      ("Can you remove tile without installing new flooring?", "[Answer to confirm with Tim: whether we take removal-only jobs.]"),
      ("What does removal cost?", "Most removals run [$X to $X per square foot]. Thick mortar beds and glued-down tile cost more. You get a written quote first."),
    ],
    "related": ["tile-flooring", "custom-tile-showers", "vinyl-plank-and-hardwood"],
    "cta_h": "Ready to get the old tile out?",
    "cta_sub": "Send us a photo and we'll tell you what it takes.",
  },
]
BY_SLUG = {s["slug"]: s for s in SERVICES}
CARD_PH = {
  "custom-tile-showers": "Custom tile shower", "tile-flooring": "Tile floor",
  "backsplashes": "Backsplash", "vinyl-plank-and-hardwood": "LVP / hardwood",
  "dust-free-tile-removal": "Dust-controlled demo",
}
CARD_LINE = {
  "custom-tile-showers": "A walk-in shower or a tub-to-shower conversion, waterproofed so it lasts.",
  "tile-flooring": "Porcelain and large format tile, set flat and tight.",
  "backsplashes": "Kitchen backsplashes with clean cuts around every outlet and edge.",
  "vinyl-plank-and-hardwood": "Vinyl plank and hardwood for the rest of your home, from the first row to the last cut.",
  "dust-free-tile-removal": "Your old tile comes out. The dust stays in that room.",
}

e = html.escape

# ---------- Real photos (see tools/photos.py) ----------
# Each entry: photo name, alt text, object-position. Anything not listed keeps its labeled placeholder.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from photos import img
CARD_IMG = {
  "custom-tile-showers": ("gray-subway-tile-walk-in-shower-penny-floor", "Walk-in shower with gray subway tile, a penny tile floor and a fold-down teak seat", "50% 55%"),
  "tile-flooring": ("hex-mosaic-bathroom-floor-walk-in-shower", "Bathroom floor in white and gray hex mosaic with brass accent tiles", "50% 75%"),
  "backsplashes": ("stone-subway-tile-kitchen-backsplash", "Stone subway tile backsplash behind a range", "50% 55%"),
  "dust-free-tile-removal": ("dust-control-containment-tile-removal", "Bathroom sealed off with plastic sheeting during tile removal", "50% 45%"),  "vinyl-plank-and-hardwood": ("gray-wood-look-lvp-floor-bedroom", "Gray wood-look vinyl plank floor with staggered seams across a bedroom", "50% 50%"),
}
PAGE_IMG = {
  "custom-tile-showers": {
    "hero": ("curbless-walk-in-shower-marble-subway-tile", "Curbless walk-in shower with marble subway tile walls and a hex mosaic floor", "50% 62%"),
    "steps": ("schluter-kerdi-waterproofing-before-tile", "Shower walls and floor covered in Schluter-KERDI waterproofing before tile", "60% 45%"),
    "Walk-in showers": ("tiled-shower-bench-niche-detail", "Dark marble-look walk-in shower with a tiled bench and niche", "50% 60%"),
    "Curbless showers": ("hex-mosaic-bathroom-floor-walk-in-shower", "Curbless shower with a glass panel and a hex mosaic floor that runs through the bathroom", "60% 55%"),
    "Niches and benches": ("shower-niche-hex-mosaic-metal-trim", "Built-in shower niche with a hex mosaic back and metal trim", "50% 40%"),
    "Tile patterns": ("hex-mosaic-brass-accent-grout-detail", "Hex mosaic tile with brass accent tiles", "50% 50%"),
    "Drain styles": ("schluter-shower-drain-pebble-floor-detail", "Square stainless steel shower drain set flush in a river pebble floor", "50% 50%"),
    "projects": [
      ("Subway tile shower with teak seat and grab bar", "subway-tile-shower-teak-seat-grab-bar", "Subway tile shower with a fold-down teak seat, grab bar and handheld shower", "50% 45%"),
      ("Gray tile shower with niche and teak seat", "gray-tile-shower-niche-teak-seat", "Gray tile shower with a hex mosaic niche, hex floor and fold-down teak seat", "50% 50%"),
      ("Hex mosaic tub surround with brass accents", "hex-mosaic-tub-surround-brass-accents", "Hex mosaic tub surround with brass accent tiles", "50% 50%"),
    ],
  },
  "tile-flooring": {
    "hero": ("hex-mosaic-bathroom-floor-walk-in-shower", "Bathroom floor in white and gray hex mosaic with brass accents", "50% 70%"),
    "steps": ("uncoupling-membrane-bathroom-floor-prep", "Uncoupling membrane down on a bathroom floor before tile, with the vanity covered in plastic", "50% 55%"),
    "Patterned layouts": ("black-hex-mosaic-shower-floor-detail", "Black hex mosaic floor with tight, even grout", "50% 60%"),
    "Bathroom floors": ("curbless-walk-in-shower-marble-subway-tile", "Hex mosaic bathroom floor running into a curbless shower", "50% 80%"),
    "projects": [
      ("River pebble stone floor", "river-pebble-stone-floor", "River pebble stone floor", "50% 50%"),
      ("Black hex mosaic shower floor", "black-hex-mosaic-shower-floor-detail", "Black hex mosaic shower floor meeting the bathroom floor tile in a clean edge", "50% 60%"),
      ("Large format porcelain kitchen floor", None, None, None),
    ],
  },
  "backsplashes": {
    "hero": ("stone-subway-tile-kitchen-backsplash", "Stone subway tile backsplash behind a range, between two windows", "50% 50%"),
  },
  "vinyl-plank-and-hardwood": {
    "hero": ("gray-wood-look-lvp-floor-bedroom", "Gray wood-look vinyl plank floor with staggered seams across a bedroom", "50% 55%"),
    "Whole-house LVP": ("wood-look-plank-floor-bedroom", "Wood-look plank floor with long, staggered planks", "50% 75%"),
  },
  "dust-free-tile-removal": {
    "hero": ("dust-control-containment-tile-removal", "Bathroom sealed off with plastic sheeting and an air scrubber running during tile removal", "50% 45%"),
    "steps": ("uncoupling-membrane-bathroom-floor-prep", "Vanity and mirror covered in plastic to keep dust off during floor work", "50% 30%"),
  },
}

def box(cls, label, ph_text, photo=None, p="../", sizes="(min-width: 900px) 30vw, 100vw", eager=False):
  """A .ph box: real photo if given, otherwise the labeled grid placeholder."""
  classes = " ".join(c for c in [cls, "ph"] if c)
  if photo and photo[0]:
    name, alt, pos = photo
    return f'<div class="{classes} has-img">{img(name, alt, p, sizes, pos, eager)}</div>'
  return f'<div class="{classes}" role="img" aria-label="{e(label)}"><span>{e(ph_text)}</span></div>'


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
              <a class="btn btn--outline btn--block" href="tel:+14178258240">Call 417-825-8240</a>
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
    <a class="btn btn--outline" href="tel:+14178258240">Call now</a>
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
  pi = PAGE_IMG.get(s["slug"], {})
  opts = "\n".join(f'''          <article class="bento-card bento-third reveal">
            {box("", t, t, pi.get(t))}
            <div class="bento-text"><h3 class="h3">{e(t)}.</h3><p>{e(d)}</p></div>
          </article>''' for t, d in s["options"])
  steps = "\n".join(f'''            <li class="step">
              <span class="step-num" aria-hidden="true">{i}</span>
              <div>
                <h3>{e(t)}</h3>
                <p>{e(d)}</p>
              </div>
            </li>''' for i, (t, d) in enumerate(s["steps"], 1))
  proj_list = pi.get("projects") or [(t, None, None, None) for t in s["projects"]]
  projs = "\n".join(f'''          <article class="project reveal">
            {box("", t, "Project photo", (n, a, pos) if n else None)}
            <h3>{e(t)}</h3>
            <p class="caption">[Town, ST]</p>
          </article>''' for t, n, a, pos in proj_list)
  faqs = "\n".join(f'''          <div class="faq-item">
            <h3>{e(q)}</h3>
            <p>{e(a)}</p>
          </div>''' for q, a in s["faqs"])
  rel = "\n".join(f'''          <a class="card-link svc reveal" href="{p}{r}/">
            {box("", BY_SLUG[r]['nav'], CARD_PH[r], CARD_IMG.get(r), sizes="(min-width: 900px) 30vw, 100vw")}
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
          <a class="link-cta" href="sms:+14178258240">Text us a photo&nbsp;›</a>
        </div>
        {box("hero-photo", s["nav"] + " by Four State Custom Floors", s["hero_ph"], pi.get("hero"), sizes="(min-width: 1240px) 1192px, 100vw", eager=True)}
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
          <p class="subhead">The way we\'ve done it for 25+ years: the owner on every job, a written quote and a full cleanup.</p>
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
          <p class="promise">Owner on every job · Written quote, no surprises · Dust control · Full cleanup</p>
        </div>
        <div class="split-media reveal">
          {box("steps-photo", s["steps_ph"], s["steps_ph"], pi.get("steps"), sizes="(min-width: 900px) 45vw, 100vw")}
        </div>
      </div>
    </section>

    <!-- ===== Projects ===== -->
    <section class="section" aria-labelledby="proj-h">
      <div class="container">
        <div class="section-head reveal">
          <h2 class="h2" id="proj-h">Recent work.</h2>
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
          <p class="subhead">Have a question that isn\'t here? Call <a class="link-cta" style="display:inline;font-size:inherit;white-space:nowrap" href="tel:+14178258240">417-825-8240</a> and talk it over.</p>
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
          <h2 class="h2" id="rel-h">More for your home.</h2>
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
          <a class="link-cta" href="tel:+14178258240">Call 417-825-8240&nbsp;›</a>
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
