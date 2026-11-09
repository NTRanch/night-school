#!/usr/bin/env python3
"""Plan 39 (A) — bake ONE copy of the cloth scene, measure, render, hash.

Opens the given .blend (a byte-identical copy of the build output),
bakes all point caches to disk, then:
  * sha256 of every cache file in the blendcache dir beside the blend
    (the cache files ARE the object of the determinism question);
  * per-frame chest-band displacement of Prima_Body vs frame 1
    (pilot measurement convention: band = z in [zmin+0.66 dz,
    zmin+0.84 dz] of the rest body, max/mean over the band);
  * decoded-pixel sha256 of renders at the drive peak (f7), the
    measured cloth-response peak, and the settle frame (f48).

Usage: blender -b -Y --python cloth_bake.py -- <blend> <out_dir>
"""
import bpy
import hashlib
import json
import os
import sys

import numpy as np

argv = sys.argv[sys.argv.index("--") + 1:]
BLEND, OUT = argv[0], argv[1]
os.makedirs(os.path.join(OUT, "frames"), exist_ok=True)
os.makedirs(os.path.join(OUT, "records"), exist_ok=True)

bpy.ops.wm.open_mainfile(filepath=BLEND)
scene = bpy.context.scene
body = bpy.context.scene.objects["Prima_Body"]

with open(BLEND, "rb") as f:
    blend_sha = hashlib.sha256(f.read()).hexdigest()

# ---- bake
bpy.ops.ptcache.bake_all(bake=True)
print("BAKE_ALL_DONE", flush=True)

# ---- cache file hashes (cache dir sits beside the .blend)
blend_dir = os.path.dirname(os.path.abspath(BLEND))
base = os.path.splitext(os.path.basename(BLEND))[0]
cache_dir = os.path.join(blend_dir, "blendcache_%s" % base)
cache_hashes = {}
if os.path.isdir(cache_dir):
    for fn in sorted(os.listdir(cache_dir)):
        p = os.path.join(cache_dir, fn)
        if os.path.isfile(p):
            with open(p, "rb") as f:
                cache_hashes[fn] = hashlib.sha256(f.read()).hexdigest()
combined = hashlib.sha256(
    "\n".join("%s %s" % (k, cache_hashes[k])
              for k in sorted(cache_hashes)).encode()).hexdigest()


def evaluated_positions():
    deps = bpy.context.evaluated_depsgraph_get()
    ev = body.evaluated_get(deps)
    me = ev.to_mesh()
    pos = [ev.matrix_world @ v.co for v in me.vertices]
    ev.to_mesh_clear()
    return pos


# band from frame-1 (rest) evaluated positions, pilot rule
scene.frame_set(1)
bpy.context.view_layer.update()
ref = evaluated_positions()
zs = [p.z for p in ref]
zmin, zmax = min(zs), max(zs)
lo = zmin + 0.66 * (zmax - zmin)
hi = zmin + 0.84 * (zmax - zmin)
band_idx = [i for i, p in enumerate(ref) if lo <= p.z <= hi]

per_frame = {}
band_pos = {}
for fr in range(1, 49):
    scene.frame_set(fr)
    bpy.context.view_layer.update()
    pos = evaluated_positions()
    band_pos[fr] = [pos[i] for i in band_idx]
    disps = [(pos[i] - ref[i]).length for i in band_idx]
    per_frame[fr] = {
        "max_mm": round(max(disps) * 1000.0, 3),
        "mean_mm": round((sum(disps) / len(disps)) * 1000.0, 3),
        "verts_over_5mm": sum(1 for d in disps if d > 0.005),
    }
peak_frame = max(per_frame, key=lambda f: per_frame[f]["max_mm"])

# ---- secondary isolation: same scene, cloth modifiers bypassed, so
# the cage follows the armature only and Surface Deform carries pure
# skeletal follow. secondary(fr) = |baked(fr) - skeletal(fr)| over the
# band — the quantity comparable to the pilot's keyed-route numbers
# (the pilot had no skeletal motion; its 15.6 mm is pure secondary).
cloth_mods = []
for ob in scene.objects:
    for m in ob.modifiers:
        if m.type == "CLOTH":
            cloth_mods.append(m)
            m.show_viewport = False
            m.show_render = False
bpy.context.view_layer.update()
secondary = {}
for fr in range(1, 49):
    scene.frame_set(fr)
    bpy.context.view_layer.update()
    pos = evaluated_positions()
    disps = [(pos[i] - band_pos[fr][k]).length
             for k, i in enumerate(band_idx)]
    secondary[fr] = {
        "max_mm": round(max(disps) * 1000.0, 3),
        "mean_mm": round((sum(disps) / len(disps)) * 1000.0, 3),
        "verts_over_5mm": sum(1 for d in disps if d > 0.005),
    }
sec_peak_frame = max(secondary, key=lambda f: secondary[f]["max_mm"])
for m in cloth_mods:
    m.show_viewport = True
    m.show_render = True
bpy.context.view_layer.update()


def pixel_hash(path):
    img = bpy.data.images.load(path)
    w, h = img.size
    px = np.empty(w * h * 4, dtype=np.float32)
    img.pixels.foreach_get(px)
    q = np.rint(px * 255.0).astype(np.uint8)
    digest = hashlib.sha256(q.tobytes()).hexdigest()
    bpy.data.images.remove(img)
    return digest


pixel = {}
for fr in sorted({1, 7, peak_frame, sec_peak_frame, 19, 48}):
    scene.frame_set(fr)
    scene.render.filepath = os.path.join(OUT, "frames", "f_%02d.png" % fr)
    bpy.ops.render.render(write_still=True)
    pixel["f%02d" % fr] = pixel_hash(scene.render.filepath)

rec = {
    "blend_sha256": blend_sha,
    "cache_dir": os.path.basename(cache_dir),
    "cache_files": len(cache_hashes),
    "cache_hashes": cache_hashes,
    "cache_combined_sha256": combined,
    "band_verts": len(band_idx),
    "band": [round(lo, 5), round(hi, 5)],
    "per_frame": {str(k): v for k, v in per_frame.items()},
    "peak_frame": peak_frame,
    "peak": per_frame[peak_frame],
    "secondary_per_frame": {str(k): v for k, v in secondary.items()},
    "secondary_peak_frame": sec_peak_frame,
    "secondary_peak": secondary[sec_peak_frame],
    "secondary_at_f7": secondary[7],
    "secondary_at_f19": secondary[19],
    "secondary_at_f48": secondary[48],
    "at_drive_peak_f7": per_frame[7],
    "at_settle_f48": per_frame[48],
    "pixel_hashes": pixel,
}
with open(os.path.join(OUT, "records", "bake_record.json"), "w") as f:
    json.dump(rec, f, indent=1, sort_keys=True)
print("CLOTH_BAKE_DONE peak_frame", peak_frame, "peak", per_frame[peak_frame],
      "cache_files", len(cache_hashes), "combined", combined[:16])
