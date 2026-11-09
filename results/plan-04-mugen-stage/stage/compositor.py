#!/usr/bin/env python3
"""Plan 04 rebuild compositor: renders harbor-steps.def under two models.

--model mugen : screen = start - c*delta, declaration order, PIL paste.
--model depth : estate depth-plane renderer. Each layer is a textured
                fronto-parallel plane at depth z = f*(1/delta - 1),
                f = 640, rendered by per-pixel ray->plane projection
                (numpy). Independent implementation of the same record.

Common: viewport 640x480; camera path c = 0..480 step 60 (9 frames);
anim tick selectable; layerno=1 drawn after the (empty) actor plane;
addalpha blends out = src*a/255 + dst*b/255 (MUGEN semantics).

Outputs: sweep frames + layer-only renders + measurements.json
Usage: python3 compositor.py --model mugen|depth --out DIR [--tick N]
"""
import argparse, hashlib, json, os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FOCAL = 640, 480, 640.0
CAMS = list(range(0, 481, 60))
FRAME_TICKS = [10, 10, 10, 10, 10, 10, 50, 10]  # Action 1 durations

def anim_frame(tick):
    t = tick % sum(FRAME_TICKS)
    for i, d in enumerate(FRAME_TICKS):
        if t < d:
            return i
        t -= d
    return 0

def load(name):
    return Image.open(os.path.join(HERE, name + ".png")).convert("RGBA")

# Layer table parsed by hand from harbor-steps.def (the spec of record).
def layers(tick):
    star = f"stars{anim_frame(tick)}"
    return [
        # name, image, start, delta, tile_x, scale, layerno, blend
        ("sky",     load("sky"),     (0, 0),    (0.25, 0.25), False, (1, 1),     0, None),
        ("stars",   load(star),      (40, 10),  (0.25, 0.25), False, (1, 1),     0, None),
        ("skyline", load("skyline"), (-40, 90), (0.5, 0.5),   False, (1, 1),     0, None),
        ("plate",   load("plate"),   (0, 0),    (1.0, 1.0),   True,  (1, 1),     0, None),
        ("beacon",  load("beacon"),  (430, 190), (1.0, 1.0),  False, (1.5, 1.5), 0, None),
        ("beacon solid", load("beacon"), (470, 130), (1.0, 1.0), False, (2, 2), 0, None),
        ("beacon trans", load("beacon"), (455, 90), (1.0, 1.0), False, (2.5, 2.5), 1, (100, 120)),
    ]

def scaled(img, sc):
    if sc == (1, 1):
        return img
    return img.resize((round(img.width * sc[0]), round(img.height * sc[1])),
                      Image.BICUBIC)

def addalpha_over(dst, src, pos, ab):
    """MUGEN addalpha: out = src*a/255 + dst*b/255 where src alpha>0."""
    a, b = ab
    x0, y0 = pos
    region = dst.crop((x0, y0, x0 + src.width, y0 + src.height))
    s = np.asarray(src).astype(np.int32)
    d = np.asarray(region).astype(np.int32)
    m = (s[:, :, 3:4] > 0)
    out = np.where(m, np.clip(s * a // 255 + d * b // 255, 0, 255), d)
    out[:, :, 3] = 255
    dst.paste(Image.fromarray(out.astype(np.uint8), "RGBA"), (x0, y0))

def render_mugen(c, tick, only=None):
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    for name, img, start, delta, tile, sc, layerno, blend in layers(tick):
        if only and name != only:
            continue
        im = scaled(img, sc)
        ox = round(start[0] - c * delta[0])
        oy = round(start[1])
        xs = [ox]
        if tile:
            xs = [ox + k * im.width for k in range(-1, W // im.width + 2)]
        for x in xs:
            if blend:
                tmp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                tmp.paste(im, (x, oy))
                addalpha_over(canvas, tmp, (0, 0), blend)
            else:
                canvas.alpha_composite(im, (x, oy))
    return canvas

def render_depth(c, tick, only=None):
    """Per-pixel projection. For screen pixel (u,v) and plane depth z:
    world X = C + (u - W/2)*(f+z)/f ; texture x = X - world_x0, where
    world_x0 = (start_x - W/2)*(f+z)/f so that C=0 matches Run A,
    and the texture is pre-scaled by scalestart (world sprite size)."""
    acc = np.zeros((H, W, 4), dtype=np.float64)
    acc[:, :, 3] = 255.0
    us = np.arange(W)[None, :].repeat(H, 0)
    vs = np.arange(H)[:, None].repeat(W, 1)
    for name, img, start, delta, tile, sc, layerno, blend in layers(tick):
        if only and name != only:
            continue
        z = FOCAL * (1.0 / delta[0] - 1.0)
        k = (FOCAL + z) / FOCAL  # = 1/delta
        im = scaled(img, sc)
        # The plane's texture lives in world units: a sprite that is
        # S screen px wide at C=0 is S*k world units wide on its plane.
        im = im.resize((round(im.width * k), round(im.height * k)),
                       Image.BICUBIC)
        tex = np.asarray(im).astype(np.float64)
        th, tw = tex.shape[:2]
        wx0 = (start[0] - W / 2) * k
        wy0 = (start[1] - H / 2) * k
        X = c + (us - W / 2) * k - wx0
        Y = (vs - H / 2) * k - wy0
        if tile:
            X = np.mod(X, tw)
        xi = np.floor(X).astype(int)
        yi = np.floor(Y).astype(int)
        valid = (xi >= 0) & (xi < tw) & (yi >= 0) & (yi < th)
        samp = np.zeros((H, W, 4))
        samp[valid] = tex[yi[valid], xi[valid]]
        if blend:
            a, b = blend
            m = (samp[:, :, 3] > 0)[:, :, None]
            acc = np.where(m, np.clip(samp * a / 255 + acc * b / 255, 0, 255), acc)
            acc[:, :, 3] = 255.0
        else:
            sa = (samp[:, :, 3:4] / 255.0)
            acc[:, :, :3] = samp[:, :, :3] * sa + acc[:, :, :3] * (1 - sa)
            acc[:, :, 3] = 255.0
    return Image.fromarray(np.clip(acc, 0, 255).astype(np.uint8), "RGBA")

RENDER = {"mugen": render_mugen, "depth": render_depth}
MARKER_RGB = np.array([255, 0, 128])

def marker_centroid(img):
    a = np.asarray(img.convert("RGB")).astype(int)
    m = (np.abs(a - MARKER_RGB).sum(axis=2) < 30)
    ys, xs = np.nonzero(m)
    if len(xs) == 0:
        return None
    return float(xs.mean()), float(ys.mean()), int(len(xs))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=["mugen", "depth"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--tick", type=int, default=0)
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    render = RENDER[args.model]
    meas = {"model": args.model, "frames": {}, "layers": {}}
    for c in CAMS:
        fr = render(c, args.tick)
        fr.save(os.path.join(args.out, f"sweep-c{c:03d}.png"))
        meas["frames"][str(c)] = hashlib.sha256(
            np.asarray(fr.convert("RGB")).tobytes()).hexdigest()
    for name in ["sky", "stars", "skyline", "plate", "beacon solid"]:
        d = {}
        for c in (0, 480):
            lo = render(c, args.tick, only=name)
            lo.save(os.path.join(args.out, f"layer-{name.replace(' ', '_')}-c{c}.png"))
            d[str(c)] = marker_centroid(lo)
        if d["0"] and d["480"]:
            d["disp_x"] = d["480"][0] - d["0"][0]
        meas["layers"][name] = d
    with open(os.path.join(args.out, "measurements.json"), "w") as fh:
        json.dump(meas, fh, indent=1)
    print(json.dumps({k: v.get("disp_x") for k, v in meas["layers"].items()}))

if __name__ == "__main__":
    main()
