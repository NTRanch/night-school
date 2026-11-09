#!/usr/bin/env python3
"""Plan 39 (B) — jiggle layer over the Plan 01 two-body loop.

Opens the Plan 01 Pass 3 scene (Prima = Follower, Yui = Leader) and
keys the SIX-GIRL-STANDARD S5.2 Bounce beat on both girls' conformed
cages (standard L/R convention: +X = .L; peak L 1.0 / R 0.85, settle
0.30 x amp), phased per the Plan 01 sheet's T-16 translation as
recorded in PASS3-REBUILD S5 and the coordinator's follower-phasing:

  * Yui (Leader) beats off her own motion: peak at Contact, sample 38;
    settle at 53; rest at 83 == sample 5 of the next cycle.
  * Prima (Follower) beats off her reaction phase: peak at her
    reaction peak, sample 45; settle at 60; rest at 90 == sample 12.

Each beat is written as a period-78 key set spanning samples 0..78
with equal endpoint values (the wrapped tail value), LINEAR
interpolation and a CYCLES fcurve modifier — the fleet's loop form,
so the beat repeats over the scene's 0..234 range with the loop.

Gates measured in-script: per-girl band displacement at her own peak
(layered vs Bounce=0 reference at the same sample, same pose; band =
S5.1.3 z-band of the rest body), contact-set penetration at the
Plan 01 record's worst samples 61..67 (build_loop.py's own test:
pelvis-box verts, two-axis ray parity, nearest-surface depth
<= 15 mm), evidence renders at 0/38/45/60 with decoded-pixel hashes.

Usage: blender -b -Y --python layer_loop.py -- <base_scene> <out_dir>
"""
import bpy
import hashlib
import json
import math
import os
import sys

import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

argv = sys.argv[sys.argv.index("--") + 1:]
BASE, OUT = argv[0], argv[1]
for sub in ("frames", "records", "scene"):
    os.makedirs(os.path.join(OUT, sub), exist_ok=True)

CYCLE = 78
# (frame, normalised value) key sets, period 78, endpoints equal.
WAVE = {
    "yui": [(0, 0.05), (5, 0.0), (23, 0.0), (38, 1.0), (53, 0.30),
            (78, 0.05)],
    "prima": [(0, 0.12), (12, 0.0), (30, 0.0), (45, 1.0), (60, 0.30),
              (78, 0.12)],
}
PEAK = {"prima": 45, "yui": 38}
AMP = {"L": 1.0, "R": 0.85}

with open(BASE, "rb") as f:
    base_sha = hashlib.sha256(f.read()).hexdigest()
bpy.ops.wm.open_mainfile(filepath=BASE)
scene = bpy.context.scene
O = {o.name: o for o in scene.objects}
GIRLS = {
    "prima": {"body": O["Prima_Body"], "arm": O["Armature_Prima"],
              "cages": {"L": O["PrimaCage.L"], "R": O["PrimaCage.R"]}},
    "yui": {"body": O["Yui_Body"], "arm": O["Armature_Yui"],
            "cages": {"L": O["YuiCage.L"], "R": O["YuiCage.R"]}},
}
REC = {"base_scene_sha256": base_sha, "blender": bpy.app.version_string,
       "wave": WAVE, "amps": AMP, "peaks": PEAK}

# ---- bind readback (conformed cages must be bound on Body + outfits)
binds = {}
for g, gd in GIRLS.items():
    for ob in scene.objects:
        if ob.name.startswith(g.capitalize() + "_") and ob.type == "MESH":
            for m in ob.modifiers:
                if m.type == "MESH_DEFORM":
                    binds["%s/%s" % (ob.name, m.name)] = bool(m.is_bound)
REC["mesh_deform_binds"] = binds
assert all(binds.values()) and len(binds) == 12, binds


def action_fcurves(action):
    if hasattr(action, "fcurves"):
        return list(action.fcurves)
    out = []
    for layer in action.layers:
        for strip in layer.strips:
            for slot in action.slots:
                try:
                    cb = strip.channelbag(slot)
                except Exception:
                    continue
                if cb is not None and hasattr(cb, "fcurves"):
                    out.extend(list(cb.fcurves))
    return out


# ---- key the beats
for g, gd in GIRLS.items():
    for side, cage in gd["cages"].items():
        kb = cage.data.shape_keys.key_blocks["Bounce"]
        for fr, nv in WAVE[g]:
            kb.value = nv * AMP[side]
            kb.keyframe_insert(data_path="value", frame=fr)
        act = cage.data.shape_keys.animation_data.action
        for fc in action_fcurves(act):
            for kp in fc.keyframe_points:
                kp.interpolation = "LINEAR"
            fc.modifiers.new("CYCLES")
        kb.value = 0.0
scene.frame_set(0)
bpy.context.view_layer.update()


def band_idx_of(body):
    zs = [v.co.z for v in body.data.vertices]
    zmin, zmax = min(zs), max(zs)
    lo = zmin + 0.66 * (zmax - zmin)
    hi = zmin + 0.84 * (zmax - zmin)
    return [i for i, v in enumerate(body.data.vertices)
            if lo <= v.co.z <= hi], (lo, hi)


BAND = {}
for g, gd in GIRLS.items():
    idx, rng = band_idx_of(gd["body"])
    BAND[g] = idx
    REC.setdefault("band", {})[g] = {"verts": len(idx),
                                     "lo": round(rng[0], 5),
                                     "hi": round(rng[1], 5)}


def evaluated_positions(body):
    deps = bpy.context.evaluated_depsgraph_get()
    ev = body.evaluated_get(deps)
    me = ev.to_mesh()
    pos = [ev.matrix_world @ v.co for v in me.vertices]
    ev.to_mesh_clear()
    return pos


# ---- penetration machinery (build_loop.py's test, verbatim form)
PELVIS_BOX = ((-0.19, 0.19), (-0.13, 0.13), (-0.21, 0.05))
B = "mixamorig:"


def hips_head_world(arm):
    bpy.context.view_layer.update()
    pb = arm.pose.bones[B + "Hips"]
    return (arm.matrix_world @ pb.matrix).translation.copy()


def pelvis_world_verts(body, arm):
    bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    ev = body.evaluated_get(dg)
    me = ev.to_mesh()
    mw = ev.matrix_world
    inv = arm.matrix_world.inverted()
    head_local = inv @ hips_head_world(arm)
    out = []
    for idx, v in enumerate(me.vertices):
        w = mw @ v.co
        rel = (inv @ w) - head_local
        if (PELVIS_BOX[0][0] <= rel.x <= PELVIS_BOX[0][1]
                and PELVIS_BOX[1][0] <= rel.y <= PELVIS_BOX[1][1]
                and PELVIS_BOX[2][0] <= rel.z <= PELVIS_BOX[2][1]):
            out.append((idx, w))
    ev.to_mesh_clear()
    return out


def bvh_of(body):
    dg = bpy.context.evaluated_depsgraph_get()
    ev = body.evaluated_get(dg)
    me = ev.to_mesh()
    mw = ev.matrix_world
    verts = [mw @ v.co for v in me.vertices]
    polys = [[i for i in p.vertices] for p in me.polygons]
    return BVHTree.FromPolygons(verts, polys), ev


def _parity(bvh, pt, d):
    hits = 0
    origin = pt.copy()
    for _ in range(16):
        loc, *_ = bvh.ray_cast(origin, d, 5.0)
        if loc is None:
            break
        hits += 1
        origin = loc + d * 0.0006
    return hits % 2 == 1


def point_inside(bvh, pt):
    return _parity(bvh, pt, Vector((1, 0, 0))) and \
        _parity(bvh, pt, Vector((0, 0, -1)))


def penetration_at(s):
    scene.frame_set(s)
    bpy.context.view_layer.update()
    bp, ep = bvh_of(GIRLS["prima"]["body"])
    by, ey = bvh_of(GIRLS["yui"]["body"])
    worst = 0.0
    rejected = 0
    for body_g, other in (("prima", by), ("yui", bp)):
        gd = GIRLS[body_g]
        for idx, w in pelvis_world_verts(gd["body"], gd["arm"]):
            if point_inside(other, w):
                near = other.find_nearest(w)
                if near is not None:
                    depth = near[3] * 1000.0
                    if depth > 15.0:
                        rejected += 1
                        continue
                    worst = max(worst, depth)
    ep.to_mesh_clear()
    ey.to_mesh_clear()
    return round(worst, 4), rejected


# ---- layered pass: bounce sampling + peak positions + penetration
bounce = {g: {"L": [], "R": []} for g in GIRLS}
layered_pos = {}
for s in range(0, CYCLE + 1):
    scene.frame_set(s)
    bpy.context.view_layer.update()
    for g, gd in GIRLS.items():
        for side, cage in gd["cages"].items():
            v = cage.data.shape_keys.key_blocks["Bounce"].value
            bounce[g][side].append(round(v, 4))
    if s in (38, 45):
        layered_pos[s] = {g: evaluated_positions(GIRLS[g]["body"])
                          for g in GIRLS}
REC["bounce_sampled"] = bounce
REC["bounce_max"] = {g: {side: max(abs(v) for v in bounce[g][side])
                         for side in ("L", "R")} for g in GIRLS}

pen = {}
for s in list(range(61, 68)) + [38, 45]:
    w, rej = penetration_at(s)
    pen[s] = {"max_mm": w, "rejected_far": rej}
REC["penetration_layered"] = {str(k): v for k, v in pen.items()}
REC["penetration_layered_worst_61_67"] = max(
    pen[s]["max_mm"] for s in range(61, 68))


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
for fr in (0, 38, 45, 60):
    scene.frame_set(fr)
    scene.render.filepath = os.path.join(OUT, "frames", "f_%04d.png" % fr)
    bpy.ops.render.render(write_still=True)
    pixel["f%04d" % fr] = pixel_hash(scene.render.filepath)
REC["pixel_hashes"] = pixel

# ---- save the layered scene BEFORE the reference pass mutates state
scene.frame_set(0)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "scene",
                                                  "scene.blend"))

# ---- reference pass: Bounce forced to 0 (actions detached in-memory)
saved_actions = {}
for g, gd in GIRLS.items():
    for side, cage in gd["cages"].items():
        ad = cage.data.shape_keys.animation_data
        saved_actions[cage.name] = ad.action if ad else None
        if ad:
            ad.action = None
        cage.data.shape_keys.key_blocks["Bounce"].value = 0.0
bpy.context.view_layer.update()
ref_pos = {}
for s in (38, 45):
    scene.frame_set(s)
    bpy.context.view_layer.update()
    ref_pos[s] = {g: evaluated_positions(GIRLS[g]["body"]) for g in GIRLS}

disp = {}
for g in GIRLS:
    for s in (38, 45):
        ds = [(layered_pos[s][g][i] - ref_pos[s][g][i]).length
              for i in BAND[g]]
        disp["%s@%d" % (g, s)] = {
            "max_mm": round(max(ds) * 1000.0, 3),
            "mean_mm": round((sum(ds) / len(ds)) * 1000.0, 3),
            "verts_over_5mm": sum(1 for d in ds if d > 0.005),
            "band_verts": len(ds),
        }
REC["displacement"] = disp
REC["displacement_own_peak"] = {
    "prima": disp["prima@45"], "yui": disp["yui@38"]}

# canonical scene-data fingerprint (determinism object for the layer)
fp_src = {
    "wave": WAVE, "amps": AMP,
    "bounce_max": REC["bounce_max"],
    "displacement": disp,
    "penetration_layered": REC["penetration_layered"],
    "pixel_hashes": pixel,
}
REC["scene_data_sha256"] = hashlib.sha256(
    json.dumps(fp_src, sort_keys=True).encode()).hexdigest()

with open(os.path.join(OUT, "records", "layer_record.json"), "w") as f:
    json.dump(REC, f, indent=1, sort_keys=True)
with open(os.path.join(OUT, "records", "measurements.json"), "w") as f:
    json.dump({"displacement": disp,
               "penetration_layered": REC["penetration_layered"],
               "bounce_max": REC["bounce_max"]}, f, indent=1)
print("LAYER_DONE scene_data", REC["scene_data_sha256"][:16],
      "disp", json.dumps(REC["displacement_own_peak"]),
      "pen61_67", REC["penetration_layered_worst_61_67"])
