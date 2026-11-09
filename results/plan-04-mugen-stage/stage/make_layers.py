#!/usr/bin/env python3
"""Plan 04 rebuild: procedurally author the Harbor Steps layers.
Seeded, deterministic. No source art. Run: python3 make_layers.py
Outputs PNG layers beside this script."""
import math, os, random
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 4404
MARKER = (255, 0, 128, 255)  # measurement-only colour, unique in palette

def marker(draw, x, y):
    draw.rectangle([x, y, x + 5, y + 5], fill=MARKER)

# 1. sky: 800x480 vertical gradient, opaque
def make_sky():
    img = Image.new("RGBA", (800, 480))
    px = img.load()
    top, mid, bot = (10, 8, 38), (74, 42, 112), (16, 14, 34)
    for y in range(480):
        if y < 330:
            t = y / 330
            c = tuple(int(top[i] + (mid[i] - top[i]) * t) for i in range(3))
        else:
            t = (y - 330) / 150
            c = tuple(int(mid[i] + (bot[i] - mid[i]) * t) for i in range(3))
        for x in range(800):
            px[x, y] = c + (255,)
    d = ImageDraw.Draw(img)
    marker(d, 400, 60)
    img.save(os.path.join(HERE, "sky.png"))

# 2. stars: 8 frames 800x300, frame index 6 is the bright hold frame
def make_stars():
    rng = random.Random(SEED + 1)
    base = [(rng.randrange(4, 796), rng.randrange(4, 290),
             rng.choice([1, 1, 2])) for _ in range(110)]
    for f in range(8):
        img = Image.new("RGBA", (800, 300), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        frng = random.Random(SEED + 100 + f)
        for (x, y, s) in base:
            if f == 6:
                a = 255  # hold frame: full twinkle peak
            else:
                a = frng.choice([70, 110, 160, 210])
            d.rectangle([x, y, x + s, y + s], fill=(235, 238, 255, a))
        if f == 0:
            marker(d, 300, 40)
        img.save(os.path.join(HERE, f"stars{f}.png"))

# 3. skyline: 1200x300 silhouettes + lit windows, transparent sky
def make_skyline():
    rng = random.Random(SEED + 2)
    img = Image.new("RGBA", (1200, 300), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x = 0
    while x < 1200:
        w = rng.randrange(46, 110)
        h = rng.randrange(90, 250)
        tone = rng.randrange(18, 34)
        d.rectangle([x, 300 - h, x + w, 300], fill=(tone, tone + 4, tone + 16, 255))
        for _ in range(w * h // 260):
            wx = rng.randrange(x + 4, x + w - 4)
            wy = rng.randrange(300 - h + 6, 292)
            d.rectangle([wx, wy, wx + 2, wy + 3], fill=(255, 176, 92, 235))
        x += w + rng.randrange(2, 14)
    marker(d, 600, 30)
    img.save(os.path.join(HERE, "skyline.png"))

# 4. plate: 700x480, transparent above the water; tiles horizontally
def make_plate():
    rng = random.Random(SEED + 3)
    img = Image.new("RGBA", (700, 480), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # water band 250..330
    for y in range(250, 330):
        t = (y - 250) / 80
        c = (int(14 + 16 * t), int(22 + 22 * t), int(48 + 40 * t), 255)
        d.line([(0, y), (700, y)], fill=c)
    for _ in range(260):  # water sparkle
        x, y = rng.randrange(700), rng.randrange(256, 326)
        d.line([(x, y), (x + rng.randrange(3, 12), y)], fill=(255, 190, 110, 150))
    # railing 330..390: top rail, mid rail, posts every 100 px (tile-clean)
    d.rectangle([0, 330, 700, 336], fill=(8, 8, 14, 255))
    d.rectangle([0, 362, 700, 366], fill=(8, 8, 14, 255))
    for x in range(0, 700, 100):
        d.rectangle([x, 330, x + 7, 390], fill=(8, 8, 14, 255))
    # floor 390..479 (zoffset = 390: the contact line is the floor top)
    for y in range(390, 480):
        t = (y - 390) / 90
        c = (int(30 - 12 * t), int(28 - 10 * t), int(40 - 12 * t), 255)
        d.line([(0, y), (700, y)], fill=c)
    for x in range(0, 700, 100):  # floor seams aligned to tile period
        d.line([(x, 390), (x, 479)], fill=(12, 12, 18, 255))
    marker(d, 100, 430)
    img.save(os.path.join(HERE, "plate.png"))

# 5. beacon: 160x220 statue-lamp silhouette, authored once, scaled by the def
def make_beacon():
    img = Image.new("RGBA", (160, 220), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([62, 120, 98, 210], fill=(20, 20, 30, 255))       # post
    d.rectangle([44, 206, 116, 220], fill=(14, 14, 22, 255))      # base
    d.ellipse([48, 30, 112, 94], fill=(24, 24, 38, 255))          # housing
    d.ellipse([60, 42, 100, 82], fill=(255, 196, 96, 255))        # lamp orb
    d.polygon([(80, 6), (104, 30), (56, 30)], fill=(16, 16, 26, 255))  # cap
    marker(d, 76, 54)
    img.save(os.path.join(HERE, "beacon.png"))

if __name__ == "__main__":
    make_sky(); make_stars(); make_skyline(); make_plate(); make_beacon()
    print("layers written:", sorted(f for f in os.listdir(HERE) if f.endswith(".png")))
