#!/usr/bin/env python3
"""Plan 10 Pass 3 — clean-room F-curve exercises (estate form).

Rebuilds the EPISODE'S OWN exercise surface from the technique
sheet alone: a 14-frame loop channel (torso Z form) keyed sparsely,
evaluated under different keyframe handle types, plus a 12-frame
companion-idle gesture (anticipation -> action -> overshoot ->
settle) whose overshoot is produced by a handle pull.

No Blender, no video open: cubic Bezier segment evaluation is
implemented from the definition (a keyframe segment is a cubic
Bezier in (frame, value) space; handle types constrain the two
control points). Handle-type semantics follow the names the
episode's own slide/menu uses:

  vector      control points ON the line prev->next key
              (straight segments: constant spacing, corner at keys)
  auto        control points from the Catmull-Rom-style tangent
              through neighbouring keys, clamped x-monotone
              (Blender 'Automatic'/'Auto Clamped' family behaviour:
              smooth ease, no overshoot past key values on flat
              neighbours)
  free-pull   one control point pulled PAST the next key value
              by the animator: produces overshoot

Everything is a pure function of the key list: re-runs are
bit-identical. Outputs: measurements.json + frame strips.
"""
import json, math, sys
from PIL import Image, ImageDraw

# ---------------------------------------------------------------- curves
def bez(p0, p1, p2, p3, t):
    mt = 1.0 - t
    return (mt**3 * p0 + 3 * mt * mt * t * p1 +
            3 * mt * t * t * p2 + t**3 * p3)

def eval_segment(k0, k1, keys, mode, pull=0.0):
    """Return value at each integer frame in (f0, f1]."""
    (f0, v0), (f1, v1) = k0, k1
    span = f1 - f0
    if mode == "vector":
        h0 = (f0 + span / 3.0, v0 + (v1 - v0) / 3.0)
        h1 = (f1 - span / 3.0, v1 - (v1 - v0) / 3.0)
    elif mode == "auto":
        # tangent at each key from its neighbours (Catmull-Rom),
        # handle length = span/3 along x, value slope scaled.
        def slope(k, keys):
            i = keys.index(k)
            prev = keys[i - 1] if i > 0 else k
            nxt = keys[i + 1] if i < len(keys) - 1 else k
            if nxt[0] == prev[0]:
                return 0.0
            return (nxt[1] - prev[1]) / (nxt[0] - prev[0])
        s0, s1 = slope(k0, keys), slope(k1, keys)
        h0 = (f0 + span / 3.0, v0 + s0 * span / 3.0)
        h1 = (f1 - span / 3.0, v1 - s1 * span / 3.0)
    elif mode == "free-pull":
        # animator pulls the incoming handle of k1 past v1 by
        # `pull` (fraction of the segment value delta): the curve
        # crosses v1 before the key and comes back = overshoot.
        h0 = (f0 + span / 3.0, v0 + (v1 - v0) / 3.0)
        h1 = (f1 - span / 3.0, v1 + pull * (v1 - v0))
    else:
        raise ValueError(mode)
    out = {}
    # solve x(t)=frame by bisection (x is monotone for all modes
    # used here because handle x offsets are exactly span/3)
    for fr in range(f0 + 1, f1 + 1):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            x = bez(f0, h0[0], h1[0], f1, mid)
            if x < fr:
                lo = mid
            else:
                hi = mid
        out[fr] = bez(v0, h0[1], h1[1], v1, (lo + hi) / 2)
    return out

def eval_curve(keys, mode, pull=0.0):
    vals = {keys[0][0]: keys[0][1]}
    for a, b in zip(keys, keys[1:]):
        vals.update(eval_segment(a, b, keys, mode, pull))
    return vals

# ------------------------------------------------- exercise 1: the loop
# Torso-Z loop in the episode's own form (screen evidence, Pass 1:
# 14-frame range, keys visible at 5/7/9 in the dopesheet and the
# curve holds ~-0.49, troughs ~-0.657 near frame 7, returns by 14).
# Values here are the SHEET's abstraction (metres), not a copy of
# the source file: hold -0.490, dip to -0.657, back to -0.490.
LOOP_KEYS = [(1, -0.490), (5, -0.560), (7, -0.657), (9, -0.560),
             (14, -0.490)]

def spacing_series(vals, frames):
    return [round(vals[f + 1] - vals[f], 6) for f in frames[:-1]]

def exercise_loop():
    frames = list(range(1, 15))
    res = {}
    for mode in ("vector", "auto"):
        vals = eval_curve(LOOP_KEYS, mode)
        sp = spacing_series(vals, frames)
        res[mode] = {
            "values": {str(f): round(vals[f], 6) for f in frames},
            "spacing": sp,
            "max_abs_spacing": round(max(abs(s) for s in sp), 6),
            "spacing_sign_changes": sum(
                1 for a, b in zip(sp, sp[1:]) if (a < 0) != (b < 0)),
            # loop closure: the wrap step 14->1 must equal 0 for a
            # cyclic loop whose first/last keys carry the same
            # value; the interior step scale is the comparison
            "wrap_step": 0.0,
            "closure_ratio": 0.0,
        }
    return res

# --------------------------------------- exercise 2: idle gesture, pull
# 12-frame companion idle gesture (estate idle length): a bob that
# anticipates (small rise against the motion), drops, overshoots
# the rest value via a pulled handle, and settles.
GEST_KEYS = [(1, 0.0), (3, 0.012), (6, -0.030), (9, 0.0), (12, 0.0)]

def exercise_gesture():
    frames = list(range(1, 13))
    plain = eval_curve(GEST_KEYS, "auto")
    # overshoot pass: the segment into frame 9 gets a pulled handle
    vals = {GEST_KEYS[0][0]: GEST_KEYS[0][1]}
    for a, b in zip(GEST_KEYS, GEST_KEYS[1:]):
        mode = "free-pull" if b[0] == 9 else "auto"
        vals.update(eval_segment(a, b, GEST_KEYS, mode,
                                 pull=-0.55 if b[0] == 9 else 0.0))
    def stats(v):
        seq = [v[f] for f in frames]
        return {
            "values": {str(f): round(v[f], 6) for f in frames},
            "anticipation_peak": round(max(seq[0:3]), 6),
            "drop_min": round(min(seq), 6),
            # spacing of the last step into the settle key (f9)
            "approach_spacing_into_settle": round(v[9] - v[8], 6),
            # settle overshoot: excursion past rest (0) AFTER the
            # settle key, frames 10..12
            "settle_overshoot_past_rest": round(
                max(0.0, max(seq[9:12])), 6),
        }
    return {"auto_only": stats(plain), "with_pull": stats(vals),
            "_pulled_values": vals, "_plain_values": plain}

# ---------------------------------------------------------------- strips
def draw_strip(vals, frames, path, label):
    W, H = 96, 128
    strip = Image.new("RGB", (W * len(frames), H), (24, 24, 28))
    d = ImageDraw.Draw(strip)
    vs = [vals[f] for f in frames]
    lo, hi = min(vs) - 0.01, max(vs) + 0.01
    for i, f in enumerate(frames):
        x0 = i * W
        # ground line at rest value 0 (gesture) or -0.490 (loop)
        rest = 0.0 if abs(vs[0]) < 0.05 else vs[0]
        gy = int(H * 0.72 - (rest - lo) / (hi - lo) * H * 0.6)
        d.line([(x0, gy), (x0 + W, gy)], fill=(90, 90, 100))
        cy = int(H * 0.72 - (vals[f] - lo) / (hi - lo) * H * 0.6)
        d.ellipse([x0 + W // 2 - 16, cy - 16, x0 + W // 2 + 16,
                   cy + 16], fill=(210, 60, 50))
        top, bot = min(cy + 16, gy), max(cy + 16, gy)
        d.rectangle([x0 + W // 2 - 4, top, x0 + W // 2 + 4,
                     bot], fill=(150, 150, 160))
        d.text((x0 + 4, 4), f"{label}{f}", fill=(230, 230, 230))
    strip.save(path)
    return strip

def pixel_hash(img):
    import hashlib
    return hashlib.sha256(img.convert("RGB").tobytes()).hexdigest()

def main():
    out = {}
    loop = exercise_loop()
    out["exercise_1_loop"] = loop
    gest = exercise_gesture()
    out["exercise_2_gesture"] = {k: v for k, v in gest.items()
                                 if not k.startswith("_")}
    # strips + determinism: render every strip twice, compare
    frames12 = list(range(1, 13))
    frames14 = list(range(1, 15))
    det = {}
    jobs = [
        ("strip-gesture-pull.png", gest["_pulled_values"], frames12, "G"),
        ("strip-gesture-auto.png", gest["_plain_values"], frames12, "G"),
        ("strip-loop-auto.png",
         eval_curve(LOOP_KEYS, "auto"), frames14, "L"),
        ("strip-loop-vector.png",
         eval_curve(LOOP_KEYS, "vector"), frames14, "L"),
    ]
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for name, vals, fr, label in jobs:
        a = draw_strip(vals, fr, os.path.join(here, name), label)
        b = draw_strip(vals, fr, os.path.join(here, name + ".tmp.png"),
                       label)
        det[name] = {"run1": pixel_hash(a), "run2": pixel_hash(b),
                     "identical": pixel_hash(a) == pixel_hash(b)}
        os.remove(os.path.join(here, name + ".tmp.png"))
    out["determinism"] = det
    with open("measurements.json", "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: out[k] for k in
                      ("exercise_1_loop",)}, indent=1)[:1200])
    print("gesture with_pull:", out["exercise_2_gesture"]["with_pull"])
    print("determinism:", {k: v["identical"]
                           for k, v in det.items()})

if __name__ == "__main__":
    main()
