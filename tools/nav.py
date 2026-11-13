"""Services menu markup shared by the homepage and the service pages.

desktop_item(p, current) -> the <li> for the main nav (hover / focus dropdown)
mobile_item(p, current)  -> the expandable Services row for the hamburger menu
p is the path prefix to the site root ("" on the homepage, "../" on service pages).
"""
SERVICES = [
  ("custom-tile-showers", "Custom Tile Showers", "Our specialty"),
  ("tile-flooring", "Tile Floors", ""),
  ("backsplashes", "Backsplashes", ""),
  ("vinyl-plank-and-hardwood", "LVP and Hardwood", ""),
  ("dust-free-tile-removal", "Dust-Controlled Removal", ""),
]

def _cur(slug, current):
  return ' aria-current="page"' if slug == current else ''

def desktop_item(p="", current=None):
  links = "\n".join(
    f'                <li><a href="{p}{slug}/"{_cur(slug, current)}>{name}'
    + (f'<small>{tag}</small>' if tag else '') + '</a></li>'
    for slug, name, tag in SERVICES)
  return f'''          <li class="has-drop">
            <a href="{p}#services" class="drop-toggle" aria-haspopup="true">Services<span class="caret" aria-hidden="true"></span></a>
            <div class="drop">
              <ul>
{links}
              </ul>
              <a class="drop-all" href="{p}#services">See all services &rsaquo;</a>
            </div>
          </li>'''

def mobile_item(p="", current=None):
  links = "\n".join(
    f'                <a href="{p}{slug}/"{_cur(slug, current)}>{name}</a>' for slug, name, _ in SERVICES)
  return f'''              <details class="m-sub">
                <summary>Services<span class="caret" aria-hidden="true"></span></summary>
                <div class="m-sub-links">
{links}
                <a class="m-sub-all" href="{p}#services">See all services &rsaquo;</a>
                </div>
              </details>'''
