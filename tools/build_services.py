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
# Bump when styles.css or main.js changes (also in index.html) so phones fetch the new files
ASSET_VERSION = "20261116h"
STATES = ["Missouri", "Kansas", "Oklahoma", "Arkansas"]

SERVICES = [
  {
    "slug": "custom-tile-showers", "h1_accent": "showers", "nav": "Custom Tile Showers", "short": "Custom tile showers",
    "projects_sub": "Real showers we've built around the Four State area.",
    "title": "Custom Tile Showers | Four State Custom Floors",
    "desc": "Walk-in showers and tub-to-shower conversions, fully waterproofed. 28 years of tile work, a written quote up front and dust-controlled demo. Call 417-825-8240.",
    "eyebrow": "Our specialty",
    "h1": "Custom tile showers in the Four State area.",
    "sub": "Get the shower you've been picturing, built by a tile setter with 28 years in the trade and waterproofed to stay dry for decades. No leaks, no surprises, no dust through the house.",
    "hero_ph": "Hero: finished custom shower, straight on",
    "answer": "Four State Custom Floors builds custom tile showers across Missouri, Kansas, Oklahoma and Arkansas. Most showers run $4,000 to $12,000 and take 7 to 14 working days, depending on the size and details.",
    "included_h": "What's included.",
    "included": [
      ("Dust-controlled demo", "Your old shower or tub comes out with the room sealed off from the rest of the house."),
      ("Waterproofing", "The Schluter waterproofing system goes on the walls and floor before any tile goes up."),
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
      ("Tile patterns", "Mosaics, herringbone, stacked or offset layouts."),
      ("Drain styles", "Linear or square drains to match your tile."),
    ],
    "steps_h": "How your shower gets built.",
    "steps": [
      ("Send us a photo.", "Text or call with a picture of your current shower. We'll get back to you the same day."),
      ("Get a design and written quote.", "We measure, help you choose the layout and tile, and put the price in writing."),
      ("Demo and waterproofing.", "The old shower comes out, the room stays sealed off, and the waterproofing goes in."),
      ("Tile, grout and cleanup.", "The tile goes up, the grout goes in, and we clean up before we leave."),
    ],
    "steps_ph": "Tall: waterproofing going on before tile",
    "projects": ["Walk-in shower with niche and bench", "Curbless shower with linear drain", "Tub-to-shower conversion"],
    "faqs": [
      ("How much does a custom tile shower cost?", "Most custom tile showers we build across the Four State area run $4,000 to $12,000, with larger custom showers costing more. That includes the setting and Schluter waterproofing materials. Size, tile choice, niches, benches and glass drive the price. You get a written quote before any work starts."),
      ("How long does a tile shower take?", "Most showers take 7 to 14 working days, depending on the size and details of the shower. You get the schedule in writing with your quote."),
      ("What waterproofing system do you use?", "Every shower gets the Schluter waterproofing system behind the tile, so water stays away from the studs and subfloor."),
      ("Can you turn my tub into a walk-in shower?", "Yes. The tub comes out and a tile shower is built in its place. We can make minor adjustments to the drain, and a plumber moves any water lines."),
      ("Can I use my bathroom during the job?", "Not the shower being rebuilt. If you have another bathroom, plan to use it while the job is underway."),
      ("Do you install the glass?", "We can install over-the-counter shower doors. For custom glass, most homeowners hire a glass company once the tile is done."),
      ("Do I have to pick out and buy the tile?", "You pick out and buy the tile, so you get exactly the look you want. Our price covers the setting and Schluter waterproofing materials, and we're happy to help you choose."),
    ],
    "related": ["tile-flooring", "backsplashes", "dust-free-tile-removal"],
    "cta_h": "Ready for a shower you love walking into?",
    "cta_sub": "Send us a photo of the one you have now and we'll tell you what it takes.",
  },
  {
    "slug": "tile-flooring", "h1_accent": "floors", "nav": "Tile Floors", "short": "Tile floors",
    "projects_sub": "Real tile floors we've laid around the Four State area.",
    "title": "Tile Floor Installation | Four State Custom Floors",
    "desc": "Porcelain, ceramic and large format tile floors, set flat on a properly prepped subfloor across the Four State area. Call 417-825-8240.",
    "eyebrow": "Tile floors",
    "h1": "Tile floors in the Four State area.",
    "sub": "A tile floor that looks great on day one and still looks great in year twenty. 28 years of setting tile taught us it all starts under the tile.",
    "hero_ph": "Hero: large format tile floor, wide shot",
    "answer": "Four State Custom Floors installs tile floors in kitchens, bathrooms and whole homes across Missouri, Kansas, Oklahoma and Arkansas. Most tile floors run $10 to $25 per square foot installed, with large format tile at the high end.",
    "included_h": "What's included.",
    "included": [
      ("Old floor removal", "Your old tile, vinyl or carpet comes out with dust control."),
      ("Subfloor prep", "We level and repair the floor so your tile sits flat."),
      ("Underlayment", "Schluter DITRA goes down under every tile floor to protect it from cracking."),
      ("Layout first", "We plan the layout so cuts land where you won't notice them."),
      ("Install and grout", "Even grout lines, sealed when the tile calls for it."),
      ("Transitions and cleanup", "Clean edges into the next room and a clean house when we leave."),
    ],
    "options_h": "Floors homeowners ask for.",
    "options_sub": "Every one starts with a flat, solid base. That's the part 28 years taught us never to rush.",
    "options": [
      ("Large format porcelain", "Bigger tiles and fewer grout lines for a clean look."),
      ("Wood-look tile", "The look of hardwood in rooms that get wet."),
      ("Patterned layouts", "Herringbone, chevron and offset patterns."),
      ("Bathroom floors", "Often done along with a new tile shower."),
      ("Kitchens and entries", "Hard-wearing floors for your busiest rooms."),
      ("Polished porcelain", "Glossy marble-look tile that makes a bathroom feel bigger and brighter."),
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
      ("How much does tile flooring cost?", "Most tile floors we install run $10 to $25 per square foot, with large format tile at the high end. That includes setting materials like thinset and Schluter DITRA. Tile choice, layout and subfloor repairs change the price. You get a written quote first."),
      ("How long does a tile floor take?", "It depends on the square footage, so there's no one-size answer. You get the schedule in writing with your quote, plus time for the grout to cure before heavy use."),
      ("Can you tile over my existing floor?", "Usually not. We check what's there first, because tiling over a bad floor is one of the main reasons tile cracks later."),
      ("Do you install heated floors?", "Yes. The heating goes in under the tile, so the floor is warm underfoot in bathrooms and showers."),
      ("Will large tiles be uneven?", "Not on a flat floor with the tile set right. We prep the subfloor first, then use a tile leveling system when the tile calls for it. Leveling clips help, but they can't fix a floor that wasn't prepped right."),
      ("Do you move appliances and toilets?", "Yes. We pull and reset toilets and move appliances as part of the job, so you don't have to line up anyone else."),
      ("Do I have to pick out and buy the tile?", "You pick out and buy the tile, so you get exactly the look you want. Our price covers the setting and Schluter waterproofing materials, and we're happy to help you choose."),
    ],
    "related": ["custom-tile-showers", "vinyl-plank-and-hardwood", "dust-free-tile-removal"],
    "cta_h": "Ready for a floor you never have to think about?",
    "cta_sub": "Send us a photo of the room and we'll tell you what it takes.",
  },
  {
    "slug": "backsplashes", "h1_accent": "backsplashes", "nav": "Backsplashes", "short": "Backsplashes",
    "projects_sub": "Real backsplashes we've installed around the Four State area.",
    "title": "Kitchen Backsplash Installation | Four State Custom Floors",
    "desc": "Kitchen tile backsplashes with clean cuts and finished edges across the Four State area. Written quote up front. Call 417-825-8240.",
    "eyebrow": "Kitchen backsplashes",
    "h1": "Kitchen backsplashes in the Four State area.",
    "sub": "Finish your kitchen with a backsplash that looks like it was always meant to be there: straight lines, clean cuts and edges that look finished, set by hands with 28 years of experience.",
    "hero_ph": "Hero: kitchen backsplash, straight on",
    "answer": "Four State Custom Floors installs kitchen tile backsplashes across Missouri, Kansas, Oklahoma and Arkansas. Most backsplashes run $800 to $2,000 and usually take about 2 days.",
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
      ("Subway tile", "Classic, clean and easy to live with, from glossy to stone-look."),
      ("Handmade-look tile", "Glossy tile with natural color variation and a hand-crafted look."),
      ("Mosaics", "Small tiles on sheets for a detailed look."),
      ("Full-height backsplash", "Tile from the counter to the ceiling or up to the hood."),
      ("Patterns and shapes", "Arabesque, diamond and other shaped tile that makes the wall stand out."),
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
      ("How much does a backsplash cost?", "Most kitchen backsplashes we install run $800 to $2,000. The size of the wall, the tile and the number of outlets and windows change the price."),
      ("How long does a backsplash take?", "Usually about 2 days. Bigger or patterned jobs can take a little longer."),
      ("Do I need to clear off my counters?", "Yes, clear the counters along the wall being tiled. We cover them and your cabinets before we start."),
      ("What happens with the outlets?", "We cut clean around every outlet and switch so the covers sit right on the new tile."),
      ("Can you remove my old backsplash?", "Yes. The old tile comes out with dust control and the wall gets patched before the new tile goes up."),
      ("Do I have to pick out and buy the tile?", "You pick out and buy the tile, so you get exactly the look you want. Our price covers the setting and Schluter waterproofing materials, and we're happy to help you choose."),
    ],
    "related": ["custom-tile-showers", "tile-flooring", "vinyl-plank-and-hardwood"],
    "cta_h": "Ready to finish your kitchen?",
    "cta_sub": "Send us a photo of the wall and we'll get back to you with next steps.",
  },
  {
    "slug": "vinyl-plank-and-hardwood", "h1_accent": "floors", "nav": "LVP and Hardwood", "short": "LVP and hardwood",
    "projects_sub": "Real LVP and hardwood jobs from around the Four State area.",
    "title": "LVP and Hardwood Installation | Four State Custom Floors",
    "desc": "Luxury vinyl plank and hardwood floors installed on a flat, prepped subfloor with clean trim across the Four State area. Call 417-825-8240.",
    "eyebrow": "LVP and hardwood",
    "h1": "LVP and hardwood floors in the Four State area.",
    "sub": "New floors that lie flat, lock tight and don't bounce, gap or squeak. Same 28 years of care we put into every tile job.",
    "hero_ph": "Hero: LVP living room, wide shot",
    "answer": "Four State Custom Floors installs luxury vinyl plank (LVP) and hardwood floors across Missouri, Kansas, Oklahoma and Arkansas. LVP runs about $3 per square foot and prefinished hardwood $4 to $6 per square foot installed.",
    "included_h": "What's included.",
    "included": [
      ("Old floor removal", "Carpet, vinyl or tile comes out with dust control."),
      ("Subfloor prep", "We fix high and low spots so the floor lies flat."),
      ("Underlayment", "The right underlayment for your floor and subfloor."),
      ("Install", "Seams staggered so the room looks right."),
      ("Trim and transitions", "Baseboards and quarter round installed, plus clean edges at doorways and where your new floor meets tile."),
      ("Cleanup", "Scraps hauled off and your floor cleaned."),
    ],
    "options_h": "Floors homeowners ask for.",
    "options_sub": "Pick the look you want and how much water it needs to handle.",
    "options": [
      ("Whole-house LVP", "One floor through your main living areas."),
      ("LVP in kitchens and baths", "Water-resistant floors where you need them most."),
      ("Engineered hardwood", "Real wood on top with a stable core underneath."),
      ("Prefinished hardwood", "Real hardwood that arrives finished, so it's ready to walk on as soon as it's down."),
      ("Stairs", "Treads and risers covered in LVP to match the floors around them."),
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
      ("How long does it take?", "It depends on the square footage and how much subfloor prep is needed. You get the schedule in writing with your quote."),
      ("How much does it cost?", "LVP runs about $3 per square foot and prefinished hardwood $4 to $6 per square foot installed. Flooring, subfloor repairs and stairs change the price. You get a written quote first."),
      ("Do you move furniture?", "You move the small stuff, and we can move the furniture."),
      ("Do I buy the flooring?", "You buy the flooring, so you get exactly the look you want. Our price covers the install."),
    ],
    "related": ["tile-flooring", "dust-free-tile-removal", "custom-tile-showers"],
    "cta_h": "Ready for floors that feel solid underfoot?",
    "cta_sub": "Send us photos of the rooms and we'll get back to you with next steps.",
  },
  {
    "slug": "dust-free-tile-removal", "h1_accent": "without dust", "nav": "Dust-Controlled Removal", "short": "Dust-controlled removal",
    "projects_sub": "Real removal jobs from around the Four State area.",
    "title": "Dust-Controlled Tile Removal | Four State Custom Floors",
    "desc": "Old tile removed with the work area sealed off and dust control running, so the rest of your house stays clean. Call 417-825-8240.",
    "eyebrow": "Dust-controlled removal",
    "h1": "Your old tile out, without dust through the house.",
    "sub": "We seal off the room so the dust stays where the work is, not on your furniture, vents and floors. Your house stays livable while the old tile comes out.",
    "hero_ph": "Hero: sealed-off room during tile removal",
    "answer": "Four State Custom Floors removes old tile floors, shower walls and backsplashes across Missouri, Kansas, Oklahoma and Arkansas. Most removals run about $4 per square foot. We seal off the work area, so the dust that normally covers a whole house stays in one room.",
    "included_h": "What's included.",
    "included": [
      ("Sealed work area", "The room gets closed off from the rest of your house."),
      ("Protected path", "We cover the floor from your door to the work area."),
      ("Dust control equipment", "HEPA-filtered vacuums and an air scrubber vented outside run the whole time."),
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
      ("Is it really dust-free?", "No removal is completely dust-free, which is why we call it dust-controlled. With the room sealed and HEPA vacuums and an air scrubber running, the dust stays in the work area instead of spreading through your house."),
      ("Can I stay home during removal?", "Yes. The work area is sealed off, so most homeowners stay home. It is loud while the tile is coming up."),
      ("How long does tile removal take?", "Most rooms take 1 to 2 days, depending on the floor and what's under it. Whole-house removal and thick mortar beds take longer."),
      ("Do you haul the old tile away?", "Yes. Debris is hauled off and the work area is cleaned before we leave."),
      ("Can you remove tile without installing new flooring?", "Yes. We'll take out the old tile even if you have someone else installing the new floor, or you're doing it yourself."),
      ("What does removal cost?", "Most removals run about $4 per square foot. Thick mortar beds and glued-down tile can cost more. You get a written quote first."),
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
  "tile-flooring": "Mosaic, porcelain, natural stone and large format tile, set flat and level.",
  "backsplashes": "Kitchen backsplashes with clean cuts around every outlet and edge.",
  "vinyl-plank-and-hardwood": "Vinyl plank and hardwood for the rest of your home, from the first row to the last cut.",
  "dust-free-tile-removal": "Your old tile comes out. The dust stays in that room.",
}

e = html.escape

# ---------- Real photos (see tools/photos.py) ----------
# Each entry: photo name, alt text, object-position. Anything not listed keeps its labeled placeholder.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from photos import img
import nav
PROJECT_TOWNS = {
  "Slate-look tile living room floor": "Neosho, MO",
  "LVP stairs and upstairs hallway": "Noel, MO",
  "Wood-look plank bedroom floor": "Grove, OK",
  "LVP kitchen floor": "Joplin, MO",
  "Subway tile shower with penny mosaic niche": "Noel, MO",
  "Marble-look shower with corner bench and niche": "Grove, OK",
  "Black hex mosaic shower floor": "Pineville, MO",
  "Travertine backsplash with butcher block counters": "Noel, MO",
  "Linear stone mosaic backsplash": "Grove, OK",
  "Marble-look subway backsplash": "Grove, OK",
  "River pebble stone floor": "Joplin, MO",
  "Hand-set floral mosaic medallion": "Grove, OK",
  "Subway tile shower with teak seat and grab bar": "Noel, MO",
  "Gray tile shower with niche and teak seat": "Noel, MO",
  "Hex mosaic tub surround with brass accents": "Rogers, AR",
}
CARD_IMG = {
  "custom-tile-showers": ("penny-tile-shower-floor-marble-look-walls", "Custom walk-in shower with a penny tile floor sloped to a square drain, marble-look wall tile and a tiled curb", "50% 22%"),
  "tile-flooring": ("hex-mosaic-bathroom-floor-walk-in-shower", "Bathroom floor in white and gray hex mosaic with brass accent tiles", "50% 75%"),
  "backsplashes": ("stone-subway-tile-kitchen-backsplash", "Stone subway tile backsplash behind a range", "50% 55%"),
  "dust-free-tile-removal": ("dust-control-containment-tile-removal", "Bathroom sealed off with plastic sheeting during tile removal", "50% 45%"),  "vinyl-plank-and-hardwood": ("gray-wood-look-lvp-floor-bedroom", "Gray wood-look vinyl plank floor with staggered seams across a bedroom", "50% 50%"),
}
PAGE_IMG = {
  "custom-tile-showers": {
    "hero": ("curbless-walk-in-shower-marble-subway-tile", "Curbless walk-in shower with marble subway tile walls and a hex mosaic floor", "50% 62%"),
    "steps": ("schluter-kerdi-waterproofing-before-tile", "Shower walls and floor covered in Schluter-KERDI waterproofing before tile", "60% 45%"),
    "Walk-in showers": ("stone-look-walk-in-shower-pebble-floor", "Walk-in shower with stone-look wall tile, a ledge, a niche and a river pebble floor", "50% 55%"),
    "Curbless showers": ("curbless-shower-skylight-penny-floor", "Curbless shower under a skylight with marble-look walls, a decorative band and a penny tile floor", "50% 60%"),
    "Tub-to-shower conversions": ("gray-tile-shower-niche-teak-seat", "Gray tile shower with a hex mosaic floor, niche and fold-down teak seat, built where a tub used to be", "50% 50%"),
    "Niches and benches": ("wood-look-tile-shower-bench-niche-stone-floor", "Dark wood-look tile shower with a built-in bench, a two-shelf niche and a stone mosaic floor", "50% 45%"),
    "Tile patterns": ("flower-mosaic-shower-floor", "Marble flower mosaic shower floor around a square drain", "50% 45%"),
    "Drain styles": ("shower-drain-penny-tile-floor", "Square shower drain set flush in a penny tile floor", "50% 45%"),
    "projects": [
      ("Subway tile shower with penny mosaic niche", "penny-mosaic-niche-glass-subway-shower", "Built-in niche with a penny mosaic back, a shelf and gold trim in a gray subway tile shower", "50% 45%"),
      ("Marble-look shower with corner bench and niche", "marble-look-shower-corner-bench-niche", "Marble-look shower with a tiled corner bench and a two-shelf niche", "50% 40%"),
      ("Hex mosaic tub surround with brass accents", "hex-mosaic-tub-surround-brass-accents", "Hex mosaic tub surround with brass accent tiles", "50% 50%"),
    ],
  },
  "tile-flooring": {
    "hero": ("hex-mosaic-bathroom-floor-walk-in-shower", "Bathroom floor in white and gray hex mosaic with brass accents", "50% 70%"),
    "steps": ("uncoupling-membrane-bathroom-floor-prep", "Uncoupling membrane down on a bathroom floor before tile, with the vanity covered in plastic", "50% 55%"),
    "Polished porcelain": ("polished-marble-look-porcelain-bathroom-floor", "Polished marble-look porcelain tile floor in a bathroom", "50% 60%"),
    "Wood-look tile": ("wood-look-tile-floor-master-bath-tub-shower", "Dark wood-look plank tile through a master bath with a freestanding tub and glass shower", "50% 75%"),
    "Patterned layouts": ("black-white-geometric-tile-bathroom-floor", "Black and white geometric pattern tile floor in a bathroom", "50% 50%"),
    "Bathroom floors": ("curbless-walk-in-shower-marble-subway-tile", "Hex mosaic bathroom floor running into a curbless shower", "50% 80%"),
    "Large format porcelain": ("marble-look-large-format-tile-hallway", "Large format marble-look porcelain tile in a bathroom hallway", "50% 55%"),
    "Kitchens and entries": ("gray-tile-entry-floor", "Gray stone-look tile in an offset pattern through an entry", "50% 60%"),
    "projects": [
      ("River pebble stone floor", "river-pebble-stone-floor", "River pebble stone floor", "50% 50%"),
      ("Black hex mosaic shower floor", "black-hex-mosaic-shower-floor-detail", "Black hex mosaic shower floor meeting the bathroom floor tile in a clean edge", "50% 60%"),
      ("Slate-look tile living room floor", "slate-look-tile-living-room-floor", "Rust and blue slate-look tile floor in a living room with a stacked stone fireplace", "50% 55%"),
    ],
  },
  "backsplashes": {
    "hero": ("stone-subway-tile-kitchen-backsplash", "Stone subway tile backsplash behind a range, between two windows", "50% 50%"),
    "steps": ("marble-basketweave-mosaic-backsplash-outlet", "Marble basketweave mosaic backsplash cut cleanly around an outlet", "50% 40%"),
    "Subway tile": ("stone-look-subway-backsplash-white-cabinets", "Stone-look subway tile backsplash under white cabinets", "50% 55%"),
    "Handmade-look tile": ("handmade-gray-subway-tile-cooktop-backsplash", "Glossy handmade-look gray subway tile behind a cooktop", "50% 40%"),
    "Mosaics": ("marble-basketweave-backsplash-pot-filler", "Marble basketweave mosaic backsplash behind a range with a pot filler", "50% 45%"),
    "Full-height backsplash": ("diamond-tile-full-height-backsplash-range-hood", "Diamond pattern tile running full height around a white range hood", "50% 35%"),
    "Patterns and shapes": ("black-arabesque-tile-backsplash", "Black arabesque tile backsplash with light grout lines", "50% 50%"),
    "Range feature wall": ("travertine-range-wall-mosaic-medallion", "Travertine backsplash with a mosaic medallion behind a range", "50% 55%"),
    "projects": [
      ("Travertine backsplash with butcher block counters", "travertine-versailles-backsplash-butcher-block", "Travertine tile backsplash in a mixed pattern above butcher block counters", "50% 55%"),
      ("Linear stone mosaic backsplash", "linear-stone-mosaic-backsplash-kitchen", "Linear stone mosaic backsplash wrapping a kitchen with alder cabinets", "50% 40%"),
      ("Marble-look subway backsplash", "navy-kitchen-marble-look-subway-backsplash", "Marble-look subway tile backsplash behind a range in a navy kitchen with LVP floors", "50% 45%"),
    ],
  },
  "vinyl-plank-and-hardwood": {
    "hero": ("gray-wood-look-lvp-floor-bedroom", "Gray wood-look vinyl plank floor with staggered seams across a bedroom", "50% 55%"),
    "steps": ("wood-look-lvp-kitchen-floor-closeup", "Wood-look LVP floor running between navy base cabinets in a kitchen", "58% 60%"),
    "Transitions to tile": ("wood-look-tile-tub-deck-lvp-floor", "Wood-look tile tub surround meeting a wood-look LVP floor in a clean line", "50% 60%"),
    "Whole-house LVP": ("wood-look-plank-floor-bedroom", "Wood-look plank floor with long, staggered planks", "50% 75%"),
    "LVP in kitchens and baths": ("gray-lvp-kitchen-floor", "Gray wood-look LVP installed through a galley kitchen between oak cabinets", "50% 45%"),
    "Stairs": ("lvp-stairs-and-landing-top-view", "Staircase and landing covered in wood-look LVP, seen from above", "50% 45%"),
    "projects": [
      ("LVP stairs and upstairs hallway", "lvp-stairs-and-upstairs-hallway", "Staircase and upstairs hallway finished in matching wood-look LVP", "50% 60%"),
      ("Wood-look plank bedroom floor", "wood-look-plank-floor-bedroom", "Wood-look plank floor with long, staggered planks in a bedroom", "50% 60%"),
      ("LVP kitchen floor", "gray-lvp-kitchen-floor", "Gray wood-look LVP installed through a galley kitchen between oak cabinets", "50% 40%"),
    ],
  },
  "dust-free-tile-removal": {
    "hero": ("dust-control-containment-tile-removal", "Bathroom sealed off with plastic sheeting and an air scrubber running during tile removal", "50% 45%"),
    "steps": ("air-scrubber-vented-outside-during-demo", "Air scrubber with its exhaust duct vented out a sealed window during tile removal", "50% 55%"),
    "Tile floors": ("tile-removal-hepa-vacuums-living-room", "Living room tile floor coming up with HEPA vacuums running", "50% 60%"),
    "Mortar beds": ("old-flagstone-mortar-bed-under-tile", "Old flagstone and mortar bed uncovered under a tile floor during removal", "50% 50%"),
    "Tile on wood subfloor": ("floor-grinder-vacuum-wood-subfloor", "Floor grinder hooked to a dust vacuum, cleaning old adhesive off a wood subfloor", "50% 55%"),
    "Tile on slab": ("tile-removal-down-to-slab", "Old tile removed down to the slab, with a HEPA vacuum and plastic sealing the doorway", "50% 55%"),
  },
}

def box(cls, label, ph_text, photo=None, p="../", sizes="(min-width: 900px) 30vw, 100vw", eager=False):
  """A .ph box: real photo if given, otherwise the labeled grid placeholder."""
  classes = " ".join(c for c in [cls, "ph"] if c)
  if photo and photo[0]:
    name, alt, pos = photo
    return f'<div class="{classes} has-img">{img(name, alt, p, sizes, pos, eager)}</div>'
  return f'<div class="{classes}" role="img" aria-label="{e(label)}"><span>{e(ph_text)}</span></div>'


def header(p, current=None):
  return f'''  <a class="skip-link" href="#main">Skip to content</a>

  <!-- ===== Header ===== -->
  <header class="site-header">
    <div class="container header-inner">
      <a class="logo" href="{p}">
        <img src="{p}assets/four-state-logo.webp" alt="Four State Custom Floors" width="139" height="60">
      </a>

      <nav class="nav" aria-label="Main">
        <ul>
{nav.desktop_item(p, current)}
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
{nav.mobile_item(p, current)}
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
            <img src="{p}assets/four-state-logo.webp" alt="Four State Custom Floors" width="148" height="64" loading="lazy">
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
            <li><a href="https://maps.app.goo.gl/QmneSirVp7D9XJJp6" target="_blank" rel="noopener">Google</a></li>
            <li><a href="https://www.facebook.com/fourstatecustomfloors" target="_blank" rel="noopener">Facebook</a></li>
            <li><a href="https://www.instagram.com/four_state_custom_floors" target="_blank" rel="noopener">Instagram</a></li>
          </ul>
        </nav>
      </div>
      <div class="footer-bottom fine">
        <span>© 2026 Four State Custom Floors. All rights reserved.</span>
        <span><a href="{p}privacy/">Privacy</a> · <a href="{p}terms/">Terms</a></span>
      </div>
    </div>
  </footer>

  <!-- ===== Mobile sticky bar ===== -->
  <div class="mobile-bar">
    <a class="btn btn--outline" href="tel:+14178258240">Call now</a>
    <a class="btn" href="{p}#estimate">Free Estimate</a>
  </div>

  <script src="{p}assets/main.js?v={ASSET_VERSION}" defer></script>
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
  opt_list = [(t, d) for t, d in s["options"] if pi.get(t)]
  grid_cls = "grid grid--two" if len(opt_list) == 4 else "grid"
  opts = "\n".join(f'''          <article class="bento-card bento-third reveal">
            {box("", t, t, pi.get(t))}
            <div class="bento-text"><h3 class="h3">{e(t)}.</h3><p>{e(d)}</p></div>
          </article>''' for t, d in opt_list)
  steps = "\n".join(f'''            <li class="step">
              <span class="step-num" aria-hidden="true">{i}</span>
              <div>
                <h3>{e(t)}</h3>
                <p>{e(d)}</p>
              </div>
            </li>''' for i, (t, d) in enumerate(s["steps"], 1))
  proj_list = [x for x in (pi.get("projects") or []) if x[1]]
  projs = "\n".join(f'''          <article class="project reveal">
            {box("", t, "Project photo", (n, a, pos) if n else None)}
            <h3>{e(t)}</h3>
            <p class="caption">{e(PROJECT_TOWNS.get(t, "[Town, ST]"))}</p>
          </article>''' for t, n, a, pos in proj_list)
  projects_section = (f'''    <!-- ===== Projects ===== -->
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

''' if proj_list else "")
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
  <link rel="icon" href="{p}favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="{p}assets/favicon-32.png">
  <link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
  <meta name="theme-color" content="#FFFFFF">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{e(s["title"])}">
  <meta property="og:description" content="{e(s["desc"])}">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="Four State Custom Floors">
  <!-- Share image: switch to https://www.fourstatecustomfloors.com/assets/share-image.jpg at launch -->
  <meta property="og:image" content="https://motion-parker.github.io/FourStateCustomFloors/assets/share-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Four State Custom Floors logo">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://motion-parker.github.io/FourStateCustomFloors/assets/share-image.jpg">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}assets/styles.css?v={ASSET_VERSION}">

  <script type="application/ld+json">
{schema(s)}
  </script>
</head>
<body>
{header(p, s["slug"])}
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
        <h1 class="h1">{e(s["h1"]).replace(e(s["h1_accent"]), '<span class="accent">' + e(s["h1_accent"]) + '</span>', 1)}</h1>
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
      </div>
    </section>

    <!-- ===== What's included ===== -->
    <section class="section band-soft" aria-labelledby="inc-h">
      <div class="container split split--top">
        <div class="faq-head reveal">
          <h2 class="h2 h2--split" id="inc-h">{e(s["included_h"])}</h2>
          <p class="subhead">The way we\'ve done it for 28 years: the owner on every job, a written quote and a full cleanup.</p>
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
        <div class="{grid_cls}">
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

{projects_section}    <!-- ===== FAQ ===== -->
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

# One word or phrase per section heading in brand green (headings as written; matched after HTML escaping)
H2_ACCENT_ALL = {
  "What's included.": "included",
  "Recent work.": "Recent",
  "Questions, answered.": "Questions",
  "More for your home.": "home",
}
H2_ACCENT = {
  "custom-tile-showers": {"What your shower could look like.": "shower", "How your shower gets built.": "built", "Ready for a shower you love walking into?": "love"},
  "tile-flooring": {"Floors homeowners ask for.": "ask for", "How your new floor goes in.": "floor", "Ready for a floor you never have to think about?": "never"},
  "backsplashes": {"Backsplash styles.": "Backsplash", "How your backsplash goes in.": "backsplash", "Ready to finish your kitchen?": "finish"},
  "vinyl-plank-and-hardwood": {"Floors homeowners ask for.": "ask for", "How your new floor goes in.": "floor", "Ready for floors that feel solid underfoot?": "solid"},
  "dust-free-tile-removal": {"What we remove.": "remove", "How dust-controlled removal works.": "dust-controlled", "Ready to get the old tile out?": "out"},
}

def accent_h2s(html_text, slug):
  import re
  rules = {**H2_ACCENT_ALL, **H2_ACCENT.get(slug, {})}
  def rep(m):
    heading = m.group(2)
    for text, word in rules.items():
      if heading == e(text):
        w = e(word)
        # whole-word match so "out" doesn't hit inside another word
        return m.group(1) + re.sub(r'(?<![\w-])' + re.escape(w) + r'(?![\w-])', '<span class="accent">' + w + '</span>', heading, count=1) + m.group(3)
    return m.group(0)
  return re.sub(r'(<h2 class="h2[^"]*"[^>]*>)([^<]*)(</h2>)', rep, html_text)

for s in SERVICES:
  d = os.path.join(REPO, s["slug"])
  os.makedirs(d, exist_ok=True)
  with open(os.path.join(d, "index.html"), "w") as f:
    f.write(accent_h2s(page(s), s["slug"]))
  print("wrote", s["slug"])

# ---------- 404 page (served by GitHub Pages for any missing URL, at any depth) ----------
def page_404():
  # A <base> tag pins relative links to the site root, both on the github.io preview and the real domain
  base = ('<script>document.write(\'<base href="\' + (location.pathname.indexOf("/FourStateCustomFloors/") === 0 ? "/FourStateCustomFloors/" : "/") + \'">\')</script>')
  links = "\n".join(f'          <li><a class="link-cta" href="{s["slug"]}/">{e(s["nav"])}&nbsp;›</a></li>' for s in SERVICES)
  return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {base}
  <title>Page Not Found | Four State Custom Floors</title>
  <meta name="robots" content="noindex">
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/styles.css?v={ASSET_VERSION}">
</head>
<body>
{header("")}
  <main id="main">
    <section class="hero">
      <div class="container">
        <p class="eyebrow">Page not found</p>
        <h1 class="h1">This page <span class="accent">moved</span>.</h1>
        <p class="subhead">The page you were looking for isn't here anymore. Here's where to find what you need.</p>
        <div class="cta-row">
          <a class="btn" href="#estimate">Get a Free Estimate</a>
          <a class="link-cta" href="./">Go to the homepage&nbsp;›</a>
        </div>
        <ul class="notfound-links">
{links}
        </ul>
      </div>
    </section>
  </main>

{footer("")}'''

with open(os.path.join(REPO, "404.html"), "w") as f:
  f.write(page_404())
print("wrote 404.html")

# ---------- Privacy and Terms (plain language; covers SMS/A2P requirements) ----------
LEGAL_UPDATED = "November 16, 2026"
LEGAL = {
  "privacy": {
    "title": "Privacy Policy | Four State Custom Floors",
    "desc": "How Four State Custom Floors collects, uses and protects your information, including text messages.",
    "h1": "Privacy Policy",
    "body": """
<p>Four State Custom Floors ("we," "us") respects your privacy. This page explains, in plain terms, what information we collect and what we do with it.</p>

<h2>What we collect</h2>
<p>When you fill out our estimate form, call or text us, we may collect:</p>
<ul>
  <li>Your name, phone number and town</li>
  <li>Details about your project and any photos you send</li>
  <li>Basic website data, like which page you came from, to help us understand how people find us</li>
</ul>

<h2>How we use it</h2>
<ul>
  <li>To contact you about your project and give you an estimate</li>
  <li>To schedule and do the work</li>
  <li>To send project updates, and after the job, a request for a review</li>
</ul>

<h2>Text messages</h2>
<p>If you give us your phone number, you agree that we can text you about your project. Message frequency varies. Message and data rates may apply. Reply <b>STOP</b> at any time to stop texts, or <b>HELP</b> for help.</p>
<p><b>We do not sell, rent or share your mobile number or text message consent with anyone for their marketing.</b> Mobile opt-in data and consent are never shared with third parties.</p>

<h2>Who we share it with</h2>
<p>We don't sell your information. We only share it with the tools that help us run the business (like our scheduling, texting and email software), and only so they can do that job for us. We may also share information if the law requires it.</p>

<h2>Keeping it safe</h2>
<p>We take reasonable steps to protect your information. No system is perfect, but we only keep what we need to serve you.</p>

<h2>Your choices</h2>
<p>You can ask us to update or delete your information, or stop contacting you, at any time. Just call or text <a href="tel:+14178258240">417-825-8240</a>.</p>

<h2>Changes</h2>
<p>If we update this policy, we'll post the new version here with a new date.</p>
""",
  },
  "terms": {
    "title": "Terms of Service | Four State Custom Floors",
    "desc": "Terms for using the Four State Custom Floors website, estimates and text messages.",
    "h1": "Terms of Service",
    "body": """
<p>By using this website, submitting our estimate form or texting us, you agree to these terms. We've kept them short and simple.</p>

<h2>Estimates and quotes</h2>
<p>Prices on this website are typical ranges, not quotes. Your actual price comes in a written quote after we see the space. The work and price in that written quote are what we agree to.</p>

<h2>Text messages</h2>
<ul>
  <li><b>What you'll get:</b> texts from Four State Custom Floors about your estimate, scheduling, your project, and a review request after the job.</li>
  <li><b>How often:</b> message frequency varies, depending on your project.</li>
  <li><b>Cost:</b> message and data rates may apply.</li>
  <li><b>To stop:</b> reply <b>STOP</b> at any time. You'll get one message confirming you're unsubscribed.</li>
  <li><b>For help:</b> reply <b>HELP</b>, or call <a href="tel:+14178258240">417-825-8240</a>.</li>
  <li>Carriers are not responsible for delayed or undelivered messages.</li>
</ul>
<p>See our <a href="../privacy/">Privacy Policy</a> for how we handle your information.</p>

<h2>Photos and content</h2>
<p>The photos on this website are our own work. Please don't copy them without asking. If you send us photos of your space, we only use them to plan and quote your project.</p>

<h2>Website information</h2>
<p>We do our best to keep this website accurate, but things like prices and timelines can change. Nothing on this site is a guarantee until it's in your written quote.</p>

<h2>Changes</h2>
<p>We may update these terms from time to time. The latest version will always be posted here.</p>

<h2>Questions</h2>
<p>Call or text <a href="tel:+14178258240">417-825-8240</a>.</p>
""",
  },
}

def page_legal(slug, L):
  p = "../"
  url = f"{SITE}/{slug}/"
  return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(L["title"])}</title>
  <meta name="description" content="{e(L["desc"])}">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="{p}favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="{p}assets/favicon-32.png">
  <link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
  <meta name="theme-color" content="#FFFFFF">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{p}assets/styles.css?v={ASSET_VERSION}">
</head>
<body>
{header(p)}
  <main id="main">
    <section class="section legal">
      <div class="container">
        <nav class="crumbs" aria-label="Breadcrumb">
          <ol>
            <li><a href="{p}">Home</a></li>
            <li aria-current="page">{e(L["h1"])}</li>
          </ol>
        </nav>
        <h1 class="h2">{e(L["h1"])}.</h1>
        <p class="caption">Last updated {LEGAL_UPDATED}</p>
        <div class="legal-body">
{L["body"]}
        </div>
      </div>
    </section>
  </main>

{footer(p)}'''

for slug, L in LEGAL.items():
  d = os.path.join(REPO, slug)
  os.makedirs(d, exist_ok=True)
  with open(os.path.join(d, "index.html"), "w") as f:
    f.write(page_legal(slug, L))
  print("wrote", slug)
