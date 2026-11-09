#!/usr/bin/env python3
# NS11 relight + measurement lane (Night School Plan 11, Pass 3/4).
# System python3 on primo (OpenEXR 3.5.3 + numpy 2.5.4). File processing only.
# Reads the multilayer EXR written by the AOV variant, then:
#   1. lists channels; identifies Combined + per-light-group RGB passes;
#   2. measures the unmodified comp (plain sum of group passes) against the
#      renderer's Combined pass in the same EXR (linear-space pixel stats);
#   3. measures each group's base contribution (mean-luminance share);
#   4. writes three relights (per-group gain x tint recipes below) as
#      single-layer linear EXRs + a measurements JSON.
# No renderer is involved after the EXR exists: relights are pass algebra.
import json, sys
import numpy as np
import OpenEXR

GROUPS = ["Key", "Rim", "Fill", "Accent_1", "Accent_2", "Accent_3", "Accent_4", "Backdrop"]
ACCENTS = ["Accent_1", "Accent_2", "Accent_3", "Accent_4"]

def _accents(gain, tint=(1.0, 1.0, 1.0)):
    return {a: (gain, tint) for a in ACCENTS}

# Relight recipes: group -> (gain, (tint_r, tint_g, tint_b)) in linear space.
# MEASURED on the probe EXR (540x960): the eight group passes sum to the
# Combined at mean|diff| 1.5e-7, and the Emission layer OVERLAPS the grouped
# Backdrop pass (adding it double-counts: mean 0.750 vs Combined 0.704).
# Base comp is therefore the group sum ONLY; the Emission layer is reported
# as a diagnostic. A "rim-dominant" recipe was attempted first and is NOT
# in this set: Combined_Rim is identically zero in the Plan 02 template
# (the Rim_Spot at (1.6, 1.5, 2.1) sits behind the backdrop wall at
# y = +1.3 and is fully occluded) — see PASS3-REBUILD.md. The third
# relight is driven by the passes that carry the scene's edge/ground
# energy instead: the Backdrop group and the Accents.
RELIGHTS = {
    "neon-backdrop": {
        "Key": (0.55, (1.0, 1.0, 1.0)),
        "Rim": (1.00, (1.0, 1.0, 1.0)),
        "Fill": (0.60, (1.0, 1.0, 1.0)),
        **_accents(1.60),
        "Backdrop": (2.00, (1.05, 0.95, 1.10)),
    },
    "key-warm": {
        "Key": (1.45, (1.25, 1.02, 0.72)),
        "Rim": (0.70, (1.0, 1.0, 1.0)),
        "Fill": (0.90, (1.05, 1.0, 0.95)),
        **_accents(1.00),
        "Backdrop": (0.75, (1.0, 1.0, 1.0)),
    },
    "low-key": {
        "Key": (0.80, (1.0, 1.0, 1.0)),
        "Rim": (1.15, (1.0, 1.0, 1.0)),
        "Fill": (0.12, (1.0, 1.0, 1.0)),
        **_accents(1.80),
        "Backdrop": (0.35, (1.0, 1.0, 1.0)),
    },
}

def read_exr(path):
    """Read a Blender 5.2 File-Output multilayer EXR: a MULTI-PART file,
    one part per pass, part name = pass name, each part holding one
    RGBA channel group whose .pixels is an (H, W, 4) float32 array.
    Returns (layers, (w, h)) with layers: pass name -> (H, W, 3) float32."""
    f = OpenEXR.File(path)
    layers = {}
    size = None
    for part in f.parts:
        for cname, ch in part.channels.items():
            px = np.asarray(ch.pixels, dtype=np.float32)
            layers[cname] = px[:, :, :3].copy()
            size = (px.shape[1], px.shape[0])
    return layers, size

def lum(rgb):
    return 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]

def write_exr(path, rgb):
    import Imath
    h, w, _ = rgb.shape
    hdr = OpenEXR.Header(w, h)
    hdr["channels"] = {c: Imath.Channel(Imath.PixelType(Imath.PixelType.FLOAT))
                       for c in ("R", "G", "B", "A")}
    out = OpenEXR.OutputFile(path, hdr)
    alpha = np.ones((h, w), dtype=np.float32)
    out.writePixels({"R": rgb[..., 0].astype(np.float32).tobytes(),
                     "G": rgb[..., 1].astype(np.float32).tobytes(),
                     "B": rgb[..., 2].astype(np.float32).tobytes(),
                     "A": alpha.tobytes()})
    out.close()

def stats(a, b):
    d = a - b
    return {"mean_abs_diff": float(np.mean(np.abs(d))),
            "rmse": float(np.sqrt(np.mean(d * d))),
            "max_abs_diff": float(np.max(np.abs(d))),
            "pct_pixels_gt_1e-3": float(100.0 * np.mean(np.max(np.abs(d), axis=2) > 1e-3)),
            "pct_pixels_gt_1e-2": float(100.0 * np.mean(np.max(np.abs(d), axis=2) > 1e-2)),
            "mean_a": float(np.mean(a)), "mean_b": float(np.mean(b))}

def main():
    exr_path, out_prefix = sys.argv[1], sys.argv[2]
    layers, (w, h) = read_exr(exr_path)
    print("LAYERS", json.dumps(sorted(layers.keys())))
    assert "Combined" in layers, "no Combined layer"
    combined = layers["Combined"]
    passes = {}
    for g in GROUPS:
        key = f"Combined_{g}"
        assert key in layers, f"no pass for group {g}"
        passes[g] = layers[key]
    # Ungrouped-energy layers (sheet C-11-2): in HIS scene these carry the
    # backdrop/fog because nothing emissive is grouped. In THIS variant the
    # backdrop IS grouped, so the layers are diagnostics, not sum terms —
    # the probe measured adding them as double-counting (see header note).
    remainder = np.zeros_like(combined)
    rem_names = []
    for needle in ("Emission", "Volume Direct", "VolumeDir", "VolumeInd"):
        if needle in layers:
            remainder += layers[needle]
            rem_names.append(needle)
    base = sum(passes[g] for g in GROUPS)
    result = {"exr": exr_path, "size": [w, h], "layers": sorted(layers.keys()),
              "diagnostic_layers_not_summed": rem_names,
              "beauty_match_sum_vs_combined": stats(base, combined),
              "doublecount_check_sum_plus_diagnostic_vs_combined":
                  stats(base + remainder, combined),
              "per_group_stats": {
                  g: {"mean": float(np.mean(passes[g])),
                      "max": float(np.max(passes[g])),
                      "nonzero_px": int((np.abs(passes[g]).max(axis=2) > 0).sum())}
                  for g in GROUPS}}
    base_lum_total = float(np.mean(lum(base)))
    result["base_group_shares"] = {
        g: float(np.mean(lum(passes[g]))) / base_lum_total for g in GROUPS}
    result["base_group_shares"]["Accents_total"] = sum(
        result["base_group_shares"][a] for a in ACCENTS)
    result["relights"] = {}
    write_exr(f"{out_prefix}-basecomp.exr", base)
    for name, recipe in RELIGHTS.items():
        out = np.zeros_like(base)
        shares = {}
        for g in GROUPS:
            gain, tint = recipe[g]
            contrib = passes[g] * (gain * np.array(tint, dtype=np.float32))
            shares[g] = float(np.mean(lum(contrib)))
            out += contrib
        shares["Accents_total"] = sum(shares[a] for a in ACCENTS)
        tot = float(np.mean(lum(out)))
        result["relights"][name] = {
            "recipe": {g: {"gain": recipe[g][0], "tint": list(recipe[g][1])} for g in GROUPS},
            "group_shares": {g: shares[g] / tot for g in shares},
            "share_change_vs_base": {g: shares[g] / tot - result["base_group_shares"][g]
                                     for g in shares},
            "vs_basecomp": stats(out, base),
            "mean_luminance": tot,
            "mean_luminance_vs_base_ratio": tot / base_lum_total}
        write_exr(f"{out_prefix}-{name}.exr", out)
        print("WROTE", name)
    with open(f"{out_prefix}-measurements.json", "w") as fh:
        json.dump(result, fh, indent=1)
    print("BEAUTY_MATCH", json.dumps(result["beauty_match_sum_vs_combined"]))
    print("DOUBLECOUNT_CHECK", json.dumps(result["doublecount_check_sum_plus_diagnostic_vs_combined"]))
    print("BASE_SHARES", json.dumps(result["base_group_shares"]))
    print("OK ns11_relight")

main()
