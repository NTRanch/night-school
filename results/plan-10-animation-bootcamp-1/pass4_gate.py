#!/usr/bin/env python3
"""Plan 10 Pass 4 gate — NS10 Three-Layer Loop applied.
Renders the application strip (NSFW-lane form) and the SFW
translation strip (same curves, lane-neutral mannequin), then
scores the five benchmark items from PASS4-APPLICATION.md.
Decoded-pixel comparisons only (PF-2)."""
import hashlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fcurve_exercises import GEST_KEYS, eval_curve, eval_segment
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
FRAMES = list(range(1, 13))

def gesture_values():
    vals = {GEST_KEYS[0][0]: GEST_KEYS[0][1]}
    for a, b in zip(GEST_KEYS, GEST_KEYS[1:]):
        mode = "free-pull" if b[0] == 9 else "auto"
        vals.update(eval_segment(a, b, GEST_KEYS, mode,
                                 pull=-0.55 if b[0] == 9 else 0.0))
    return vals

def render_frames(vals, body_rgb, label):
    W, H = 96, 128
    vs = [vals[f] for f in FRAMES]
    lo, hi = min(vs) - 0.01, max(vs) + 0.01
    frames = []
    for i, f in enumerate(FRAMES):
        im = Image.new("RGB", (W, H), (24, 24, 28))
        d = ImageDraw.Draw(im)
        rest = 0.0
        gy = int(H * 0.72 - (rest - lo) / (hi - lo) * H * 0.6)
        d.line([(0, gy), (W, gy)], fill=(90, 90, 100))
        cy = int(H * 0.72 - (vals[f] - lo) / (hi - lo) * H * 0.6)
        top, bot = min(cy + 16, gy), max(cy + 16, gy)
        d.rectangle([W // 2 - 4, top, W // 2 + 4, bot],
                    fill=(150, 150, 160))
        d.ellipse([W // 2 - 16, cy - 16, W // 2 + 16, cy + 16],
                  fill=body_rgb)
        d.text((4, 4), f"{label}{f}", fill=(230, 230, 230))
        frames.append(im)
    return frames

def frame_hash(im):
    return hashlib.sha256(im.convert("RGB").tobytes()).hexdigest()

def main():
    vals = gesture_values()
    jobs = {"nsfw": render_frames(vals, (210, 60, 50), "A"),
            "sfw": render_frames(vals, (40, 160, 170), "S")}
    out = {}
    for name, frames in jobs.items():
        strip = Image.new("RGB", (96 * 12, 128))
        for i, im in enumerate(frames):
            strip.paste(im, (i * 96, 0))
        path = os.path.join(HERE, f"pass4-strip-{name}.png")
        strip.save(path)
        hashes = [frame_hash(im) for im in frames]
        dead = sum(1 for a, b in zip(hashes, hashes[1:]) if a == b)
        out[name] = {"strip": os.path.basename(path),
                     "strip_pixel_hash": frame_hash(strip),
                     "dead_consecutive_pairs": dead,
                     "first_last_identical": hashes[0] == hashes[-1]}
    sp = [round(vals[f + 1] - vals[f], 6) for f in FRAMES[:-1]]
    # piecewise-constant run detection (Vector signature)
    runs = 1
    maxrun = 1
    for a, b in zip(sp, sp[1:]):
        if a == b:
            runs += 1
            maxrun = max(maxrun, runs)
        else:
            runs = 1
    out["measurements"] = {
        "wrap_step": round(vals[1] - vals[12], 6),
        "spacing": sp,
        "max_constant_spacing_run": maxrun,
        "settle_overshoot_past_rest": round(
            max(0.0, max(vals[f] for f in (10, 11, 12))), 6),
        "approach_spacing_into_settle": round(vals[9] - vals[8], 6),
    }
    with open(os.path.join(HERE, "pass4-measurements.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
