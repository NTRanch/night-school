#!/usr/bin/env python3
# NS40 Pass 3 — measurement lane (Plan 11 method, system python3 on primo:
# OpenEXR 3.5.3 + numpy). File processing only; no renderer involved.
# 1) Per-group energy shares from each multilayer probe EXR + the
#    sum-of-groups vs renderer Combined check (beauty-match).
# 2) Decoded-pixel SHA-256 of the twin variant EXRs' Combined pass
#    (determinism — pixel hash, never file hash).
# 3) PNG plate statistics (decoded via ffmpeg to raw RGB): mean luminance,
#    per-channel means, RMS + mean|diff| between plates — the numbers behind
#    the named differences in PASS3-REBUILD.md.
import hashlib, json, subprocess, sys
import numpy as np
import OpenEXR

def lum(rgb):
    return rgb[..., 0] * 0.2126 + rgb[..., 1] * 0.7152 + rgb[..., 2] * 0.0722

def read_exr(path):
    # Plan 11's proven reader for Blender 5.2 File-Output multilayer EXRs
    # on this OpenEXR binding: OpenEXR.File, one part per pass, channels
    # keyed by pass-group name with .pixels an (H, W, 4) float32 array.
    f = OpenEXR.File(path)
    layers = {}
    for part in f.parts:
        for cname, ch in part.channels.items():
            px = np.asarray(ch.pixels, dtype=np.float32)
            layers[cname] = px[:, :, :3].astype(np.float64)
    return layers

def exr_report(path, groups):
    parts = read_exr(path)
    rep = {"file": path, "parts": sorted(parts.keys())}
    comb = parts.get("Combined")
    gsum = None
    shares = {}
    for g in groups:
        p = parts.get(f"Combined_{g}")
        if p is None:
            shares[g] = None
            continue
        gsum = p.copy() if gsum is None else gsum + p
        shares[g] = float(np.mean(lum(p)))
    tot = sum(v for v in shares.values() if v is not None)
    rep["group_mean_lum"] = shares
    rep["group_shares"] = {g: (None if v is None else v / tot) for g, v in shares.items()}
    if comb is not None and gsum is not None:
        d = gsum - comb
        rep["sum_vs_combined"] = {
            "mean_abs_diff": float(np.mean(np.abs(d))),
            "pct_px_gt_1e-3": float(100.0 * np.mean(np.max(np.abs(d), axis=2) > 1e-3)),
            "combined_mean_lum": float(np.mean(lum(comb))),
            "sum_mean_lum": float(np.mean(lum(gsum))),
        }
    if comb is not None:
        rep["combined_pixel_sha256"] = hashlib.sha256(
            comb.astype(np.float32).tobytes()).hexdigest()
        rep["combined_nonzero_px"] = int(np.count_nonzero(np.max(np.abs(comb), axis=2) > 0))
    return rep

def png_stats(path):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
        capture_output=True, check=True).stdout
    # dimensions via ffprobe
    dims = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height", "-of", "csv=p=0", path],
        capture_output=True, check=True, text=True).stdout.strip().split(",")
    w, h = int(dims[0]), int(dims[1])
    a = np.frombuffer(raw, dtype=np.uint8).reshape(h, w, 3).astype(np.float64) / 255.0
    return a

def plate_report(name, arr):
    return {"name": name, "mean_lum": float(np.mean(lum(arr))),
            "channel_means": [float(np.mean(arr[..., i])) for i in range(3)],
            "pct_px_lum_gt_0.5": float(100.0 * np.mean(lum(arr) > 0.5)),
            "pct_px_lum_lt_0.02": float(100.0 * np.mean(lum(arr) < 0.02)),
            "pixel_sha256": hashlib.sha256(
                (arr * 255.0).round().astype(np.uint8).tobytes()).hexdigest()}

def pair_diff(a, b):
    d = a - b
    return {"mean_abs_diff": float(np.mean(np.abs(d))),
            "rmse": float(np.sqrt(np.mean(d * d))),
            "mean_lum_a": float(np.mean(lum(a))), "mean_lum_b": float(np.mean(lum(b)))}

def main():
    cfg = json.load(open(sys.argv[1]))
    out = {}
    out["control_exr"] = exr_report(cfg["control_exr"],
                                    ["Key", "Rim", "Fill", "Accent_1", "Accent_2",
                                     "Accent_3", "Accent_4", "Backdrop"])
    out["variant_exr"] = exr_report(cfg["variant_exr"],
                                    ["NS40Key", "NS40Fill", "NS40Strip", "NS40SpotKey",
                                     "NS40SpotRim", "NS40Points", "Backdrop"])
    if cfg.get("variant_exr_twin"):
        out["variant_exr_twin"] = exr_report(cfg["variant_exr_twin"],
                                             ["NS40Key", "NS40Fill", "NS40Strip",
                                              "NS40SpotKey", "NS40SpotRim", "NS40Points",
                                              "Backdrop"])
        out["determinism_combined_pixel_equal"] = (
            out["variant_exr"]["combined_pixel_sha256"]
            == out["variant_exr_twin"]["combined_pixel_sha256"])
    plates = {}
    for key in ("beauty_control", "beauty_variant_graded", "beauty_variant_raw"):
        if cfg.get(key):
            arr = png_stats(cfg[key])
            plates[key] = arr
            out[key] = plate_report(key, arr)
    if "beauty_variant_raw" in plates and "beauty_variant_graded" in plates:
        out["diff_raw_vs_graded"] = pair_diff(plates["beauty_variant_raw"],
                                              plates["beauty_variant_graded"])
    if "beauty_control" in plates and "beauty_variant_graded" in plates:
        out["diff_control_vs_variant_graded"] = pair_diff(plates["beauty_control"],
                                                          plates["beauty_variant_graded"])
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
