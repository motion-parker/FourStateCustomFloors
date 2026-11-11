"""Shared helper for real project photos.

Photos live in assets/photos as <name>-<width>.webp (640/1000/1600 wide).
tools/photos.json lists each photo's widths and size. Use img() to get a
responsive <img> that fills a .ph box (the box keeps its layout size).
"""
import html, json, os

_META = json.load(open(os.path.join(os.path.dirname(__file__), "photos.json")))
PHOTOS = {v["name"]: v for v in _META.values()}


def img(name, alt, prefix="", sizes="(min-width: 900px) 40vw, 100vw", pos=None, eager=False):
    m = PHOTOS[name]
    ws = m["widths"]
    srcset = ", ".join(f"{prefix}assets/photos/{name}-{w}.webp {w}w" for w in ws)
    style = f' style="object-position: {pos}"' if pos else ""
    load = ' fetchpriority="high"' if eager else ' loading="lazy"'
    return (f'<img src="{prefix}assets/photos/{name}-{ws[-1]}.webp" srcset="{srcset}" sizes="{sizes}" '
            f'width="{m["w"]}" height="{m["h"]}" alt="{html.escape(alt)}"{style}{load} decoding="async">')
