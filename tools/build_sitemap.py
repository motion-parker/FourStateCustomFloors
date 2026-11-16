"""Build sitemap.xml with real last-modified dates (from git) and every photo on each page.
Usage (from the repo root, after build_services.py): python3 tools/build_sitemap.py
"""
import html, re, subprocess
from xml.sax.saxutils import escape

SITE = "https://www.fourstatecustomfloors.com"
PAGES = [
  ("", "index.html"),
  ("custom-tile-showers/", "custom-tile-showers/index.html"),
  ("tile-flooring/", "tile-flooring/index.html"),
  ("backsplashes/", "backsplashes/index.html"),
  ("vinyl-plank-and-hardwood/", "vinyl-plank-and-hardwood/index.html"),
  ("dust-free-tile-removal/", "dust-free-tile-removal/index.html"),
  ("privacy/", "privacy/index.html"),
  ("terms/", "terms/index.html"),
]

def lastmod(path):
  out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path], capture_output=True, text=True).stdout.strip()
  return out or subprocess.run(["date", "+%F"], capture_output=True, text=True).stdout.strip()

def images(path):
  src = open(path).read()
  seen, out = set(), []
  for tag in re.findall(r"<img [^>]*>", src):
    m = re.search(r'src="(?:\.\./)?(assets/photos/[^"]+)"', tag)
    if not m or m.group(1) in seen:
      continue
    seen.add(m.group(1))
    alt = re.search(r'alt="([^"]*)"', tag)
    out.append((f"{SITE}/{m.group(1)}", html.unescape(alt.group(1)) if alt else ""))
  return out

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
total = 0
for loc, path in PAGES:
  lines.append(f"  <url>\n    <loc>{SITE}/{loc}</loc>\n    <lastmod>{lastmod(path)}</lastmod>")
  for url, alt in images(path):
    lines.append(f"    <image:image><image:loc>{escape(url)}</image:loc><image:title>{escape(alt)}</image:title></image:image>")
    total += 1
  lines.append("  </url>")
lines.append("</urlset>")
open("sitemap.xml", "w").write("\n".join(lines) + "\n")
print(f"sitemap.xml: {len(PAGES)} pages, {total} images")
