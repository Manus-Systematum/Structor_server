#!/usr/bin/env python3
"""Generate the page's mark and favicons from the Structor app icon.

The icon is two-tone — a pale gold helmet on its own navy — and the page's navy
is not the icon's. So rather than crop the artwork, each pixel is projected onto
the navy->gold axis to recover its coverage, and the gold is re-composited onto
nothing. The mark then sits on whatever dark ground the page gives it.

Usage: python3 tools/make-assets.py [path-to-icon-source.png]
"""
import sys
from PIL import Image

SRC = sys.argv[1] if len(sys.argv) > 1 else (
    "../Wh40k_Companion/packages/wh40k_app/design/icon-source.png")

NAVY_IN = (8, 36, 71)      # the icon's ground
GOLD = (248, 216, 163)     # the icon's line work
NAVY_PAGE = (11, 28, 54)   # --navy, for the favicons' own ground

src = Image.open(SRC).convert("RGB")
axis = tuple(g - n for g, n in zip(GOLD, NAVY_IN))
denom = sum(c * c for c in axis)

out = Image.new("RGBA", src.size)
sp, op = src.load(), out.load()
for y in range(src.size[1]):
    for x in range(src.size[0]):
        r, g, b = sp[x, y]
        t = ((r - NAVY_IN[0]) * axis[0] + (g - NAVY_IN[1]) * axis[1]
             + (b - NAVY_IN[2]) * axis[2]) / denom
        op[x, y] = GOLD + (max(0, min(255, round(t * 255))),)

# Trim to the artwork, then give it back a 6% margin, so the mark fills the
# tile it is placed in instead of floating inside the icon's own padding.
mark = out.crop(out.getbbox())
mw, mh = mark.size
side = max(mw, mh)
pad = int(side * 0.06)
canvas = Image.new("RGBA", (side + 2 * pad, side + 2 * pad), (0, 0, 0, 0))
canvas.paste(mark, (pad + (side - mw) // 2, pad + (side - mh) // 2), mark)

canvas.resize((512, 512), Image.LANCZOS).save("assets/logo.png")
canvas.resize((128, 128), Image.LANCZOS).save("assets/logo-mark.png")


def tile(size):
    """Favicons need their own ground: gold line art on a light tab strip
    would disappear."""
    t = Image.new("RGBA", (size, size), NAVY_PAGE + (255,))
    m = canvas.resize((size, size), Image.LANCZOS)
    t.paste(m, (0, 0), m)
    return t.convert("RGB")


tile(180).save("assets/apple-touch-icon.png")
tile(64).save("assets/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
print("wrote assets/logo.png, logo-mark.png, apple-touch-icon.png, favicon.ico")
