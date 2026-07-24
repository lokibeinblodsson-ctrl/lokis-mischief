#!/usr/bin/env python3
"""Premium 8-legged Sleipnir splash (1080x1350).

The body base is a GREYSCALE horse render on a darker grey vignette. There is no
alpha channel and no hue separation, so the background is keyed out by LUMINANCE:
horse pixels are brighter than the background. We feather the luminance mask into a
soft alpha, build a transparent RGBA horse, then clone each real leg ONCE to the
right with a cool shadow tint -> 4 originals + 4 clones = 8 legs (four pairs), which
is how Sleipnir is actually depicted. No numpy required.
"""
import os
from PIL import Image, ImageFilter, ImageDraw

BASE = "/data/data/com.termux/files/home/storage/downloads/hermes-output"
SRC = os.path.join(BASE, "lokis-assets/sleipnir/sleipnir-body-base.png")
OUT = os.path.join(BASE, "lokis-assets/sleipnir/sleipnir-8leg-splash.png")

# ---------------------------------------------------------------- load + key
im = Image.open(SRC).convert("RGB")
W, H = im.size                      # 1200 x 1200
lum = im.convert("L")

THR = 100                           # luminance above this = horse (brighter than bg)
mask = lum.point(lambda v: 255 if v > THR else 0)
mask = mask.filter(ImageFilter.GaussianBlur(2))   # tighter feather -> less halo
horse = Image.merge("RGBA", (im.split()[0], im.split()[1], im.split()[2], mask))

# ---------------------------------------------------------------- leg positions
# The two front legs sit very close and merge in auto-detection, so we use the
# four validated leg-center fractions (all verified to land on real leg coverage).
leg_centers = [0.42, 0.48, 0.65, 0.76]

# ---------------------------------------------------------------- canvas
CW, CH = 1080, 1350
# vertical-gradient background + faint central glow
bg = Image.new("RGB", (CW, CH))
for y in range(CH):
    t = y / CH
    r = int(20 + (8 - 20) * t)
    g = int(18 + (6 - 18) * t)
    b = int(30 + (16 - 30) * t)
    for x in range(0, CW, 8):
        bg.paste((r, g, b), (x, y, x + 8, y + 1))
glow = Image.new("RGB", (CW, CH), (0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([CW*0.18, CH*0.30, CW*0.82, CH*0.80], fill=(60, 54, 84))
glow = glow.filter(ImageFilter.GaussianBlur(120))
bg = Image.blend(bg, glow, 0.18)

# ---------------------------------------------------------------- place horse
scale = CW / W                       # 0.9 -> horse is 1080x1080
horse_s = horse.resize((CW, int(H * scale)), Image.LANCZOS)
by = (CH - horse_s.height) // 2     # center vertically
canvas = bg.copy()
canvas.paste(horse_s, (0, by), horse_s)

# ---------------------------------------------------------------- clone legs
half_w_f = 0.05                      # leg half-width as fraction of source W
top_f, bot_f = 0.63, 0.93
SX = CW / W                       # source->canvas x scale (== scale)


def shadow_tint(rgba):
    r, g, b, a = rgba.split()
    r = r.point(lambda v: int(v * 0.50))      # red cut most -> cool
    g = g.point(lambda v: int(v * 0.58))
    b = g.point(lambda v: int(v * 0.70))      # blue cut least -> cool shadow
    a = a.point(lambda v: int(v * 0.92))
    return Image.merge("RGBA", (r, g, b, a))


# tiny per-leg rotation (deg) + offset so each pair looks organic, not stamped
rot = [2.0, -1.5, 1.2, -2.3]
jit = [int(0.012 * CW), int(0.018 * CW), int(0.010 * CW), int(0.015 * CW)]

for i, c in enumerate(leg_centers):
    cx = c * SX                                   # leg center, canvas x
    cy_top = by + int(top_f * horse_s.height)
    cy_bot = by + int(bot_f * horse_s.height)
    # crop the leg (with real alpha) from the scaled horse
    leg = horse_s.crop((int(cx - half_w_f * CW), cy_top,
                        int(cx + half_w_f * CW), cy_bot))
    clone = shadow_tint(leg)
    # slight rotation around the leg's top-center so it stays anchored to the body
    clone = clone.rotate(rot[i], resample=Image.BICUBIC, center=(clone.width // 2, 0),
                         expand=True)
    # paste clone to the right = paired leg; original leg already present in body.
    # offset kept small so the pair reads as a near-double, not a stray third leg.
    base_x = int(cx - half_w_f * CW) + int(0.032 * CW) + jit[i]
    canvas.paste(clone, (base_x, cy_top - clone.height // 12), clone)

canvas = canvas.filter(ImageFilter.GaussianBlur(0.5))
canvas.save(OUT)
print("saved", OUT, os.path.getsize(OUT) // 1024, "KB")
