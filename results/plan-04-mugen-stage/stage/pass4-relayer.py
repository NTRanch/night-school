#!/usr/bin/env python3
"""Plan 04 Pass 4 (NSFW application): re-layer an existing flat
Torogao scene plate to the Plan 04 grammar, in the compositor.
Source plate (read-only): torogao-plates-20261028/plates/
pl04-scenes-prima-v2.png (1280x900 theatre scene).
Cuts are horizontal/vertical bands by depth story; one ambient
anim (spotlight shimmer, Action-1 timing); one foreground
addalpha ghost (side curtains, 100,120). Markers embedded for
displacement measurement. Outputs to stage/pass4/."""
import hashlib, json, os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "/home/hatch/workspace/torogao-plates-20261028/plates/pl04-scenes-prima-v2.png"
OUT = os.path.join(HERE, "pass4")
os.makedirs(OUT, exist_ok=True)
W, H = 1280, 900
MARKER = (255, 0, 128, 255)

src = Image.open(SRC).convert("RGB")
arr = np.asarray(src).copy()

def band(rows=None, cols=None, marker_at=None):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    r = rows if rows else (0, H)
    c = cols if cols else (0, W)
    crop = Image.fromarray(arr[r[0]:r[1], c[0]:c[1]]).convert("RGBA")
    img.alpha_composite(crop, (c[0], r[0]))
    if marker_at:
        a = np.asarray(img).copy()
        x, y = marker_at
        a[y:y + 6, x:x + 6] = MARKER
        img = Image.fromarray(a)
    return img

# Depth-story cuts (rows/cols of the 1280x900 plate)
back = band(rows=(0, 640), marker_at=(640, 100))            # truss + rear curtain
sides = band(cols=(0, 150), marker_at=(60, 400))            # left curtain wall
sides_r = band(cols=(1130, 1280))                           # right curtain wall
floor = band(rows=(640, 900), marker_at=(640, 800))         # tiled floor + rose
# ambient: spotlight beam glints - bright pixels of the back band, 8 frames
backa = np.asarray(back).astype(int)
bright = (backa[:, :, :3].sum(axis=2) > 560) & (backa[:, :, 3] > 0)
frames = []
for f in range(8):
    fa = np.zeros((H, W, 4), dtype=np.uint8)
    ys, xs = np.nonzero(bright)
    keep = (xs * 7 + ys * 13 + f * 29) % (3 if f == 6 else 5) == 0
    fa[ys[keep], xs[keep]] = (255, 240, 220, 255 if f == 6 else 150)
    frames.append(Image.fromarray(fa, "RGBA"))
# foreground ghost: darkened side strips, addalpha
ghost_a = np.asarray(sides).astype(float)
ghost_r = np.asarray(sides_r).astype(float)
ghost = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ga = np.asarray(ghost).astype(float)
for g in (ghost_a, ghost_r):
    m = g[:, :, 3:4] > 0
    ga = np.where(m, g * 0.35, ga)
ga[:, :, 3] = np.maximum(ghost_a[:, :, 3], ghost_r[:, :, 3])
ghost = Image.fromarray(np.clip(ga, 0, 255).astype(np.uint8), "RGBA")

LAYERS = [  # name, image(s), delta, layerno, blend
    ("back curtain", [back], 0.5, 0, None),
    ("spotlight shimmer", frames, 0.5, 0, None),
    ("side curtains", [sides, sides_r], 0.75, 0, None),
    ("floor", [floor], 1.0, 0, None),
    ("curtain ghost", [ghost], 1.0, 1, (100, 120)),
]
TICKS = [10, 10, 10, 10, 10, 10, 50, 10]

def anim_idx(tick):
    t = tick % sum(TICKS)
    for i, d in enumerate(TICKS):
        if t < d:
            return i
        t -= d
    return 0

def render(c, tick=0, only=None):
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    for name, imgs, delta, layerno, blend in LAYERS:
        if only and name != only:
            continue
        img = imgs[anim_idx(tick)] if len(imgs) > 1 else imgs[0]
        ox = round(-c * delta)
        if blend:
            tmp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            tmp.paste(img, (ox, 0))
            s = np.asarray(tmp).astype(int)
            d = np.asarray(canvas).astype(int)
            m = s[:, :, 3:4] > 0
            a_, b_ = blend
            out = np.where(m, np.clip(s * a_ // 255 + d * b_ // 255, 0, 255), d)
            out[:, :, 3] = 255
            canvas = Image.fromarray(out.astype(np.uint8), "RGBA")
        else:
            canvas.alpha_composite(img, (ox, 0))
            if len(imgs) == 1 and name == "side curtains":
                canvas.alpha_composite(imgs[1], (ox, 0))
    return canvas

def centroid(img):
    a = np.asarray(img.convert("RGB")).astype(int)
    m = np.abs(a - np.array([255, 0, 128])).sum(axis=2) < 30
    ys, xs = np.nonzero(m)
    return float(xs.mean()) if len(xs) else None

meas = {"layers": {}}
for c in (0, 60, 120):
    render(c).save(os.path.join(OUT, f"relayered-c{c:03d}.png"))
src.resize((W, H)).save(os.path.join(OUT, "before-flat.png"))
for name, imgs, delta, layerno, blend in LAYERS:
    if name in ("spotlight shimmer", "curtain ghost", "side curtains"):
        continue
    d0, d1 = centroid(render(0, only=name)), centroid(render(120, only=name))
    meas["layers"][name] = {"delta": delta,
                            "disp_measured": None if d0 is None or d1 is None else d1 - d0,
                            "disp_expected": -120 * delta}
meas["frame_hash_c060"] = hashlib.sha256(
    np.asarray(render(60).convert("RGB")).tobytes()).hexdigest()
json.dump(meas, open(os.path.join(OUT, "relayer-measurements.json"), "w"), indent=1)
print(json.dumps(meas, indent=1))
