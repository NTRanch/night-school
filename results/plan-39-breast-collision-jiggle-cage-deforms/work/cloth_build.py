#!/usr/bin/env python3
"""Plan 39 (A) — build the video's TRUE stack on Prima's conformed rig.

Stack per runs/plan-39/TECHNIQUE.md (corrected stack) and
SIX-GIRL-STANDARD S5.3: per-breast cage carries Cloth physics and
drives the body via Surface Deform (mask Cage.L/R); the cage follows
the armature via vertex groups copied from the body by a Data
Transfer modifier (applied), on top of an Armature modifier; the
flat (chest-wall, +Y) cage face is the Pin group.

The estate keyed route's Mesh Deform modifiers are REMOVED in this
scene copy only (the fleet file is never touched). The drive is a
skeletal beat on Spine/Spine1 keyed on the pilot's timing grid
(24 fps: rest f1, wind f4, peak f7, release f10, settle f13, rest
f19, hold to f48) so the cloth response is comparable to the pilot's
keyed beat (peak f7 of a 19-frame window).

Usage: blender -b -Y --python cloth_build.py -- <in.blend> <out.blend> <record.json>
Blender 5.2.3 LTS, headless, no audio.
"""
import bpy
import json
import math
import os
import sys

argv = sys.argv[sys.argv.index("--") + 1:]
IN_BLEND, OUT_BLEND, REC_PATH = argv[0], argv[1], argv[2]
EXTRA = argv[3:]
NOCLOTH = "nocloth" in EXTRA
PRESSURE_FACTOR = 10000.0
for _t in EXTRA:
    if _t.startswith("pressure="):
        PRESSURE_FACTOR = float(_t.split("=", 1)[1])

REC = {"blender": bpy.app.version_string, "input": IN_BLEND, "nocloth": NOCLOTH, "pressure_factor": PRESSURE_FACTOR}
bpy.ops.wm.open_mainfile(filepath=IN_BLEND)
scene = bpy.context.scene
objs = {o.name: o for o in scene.objects}
body = objs["Prima_Body"]
outfit = objs["Prima_Outfit"]
outfit_end = objs["Prima_OutfitEnd"]
arm = objs["Armature"]

scene.render.fps = 24
scene.frame_start = 1
scene.frame_end = 48
scene.frame_set(1)

# Canon bust (m = 1.0): the conformed file stores Body_Bust_Size at 0.
for tgt in (body, outfit, outfit_end):
    kb = tgt.data.shape_keys.key_blocks.get("Body_Bust_Size")
    assert kb is not None and abs(kb.value) < 1e-9, "bust not at canon"

# --- remove the keyed route's Mesh Deform (this scene copy only)
removed = {}
for tgt in (body, outfit, outfit_end):
    names = [m.name for m in tgt.modifiers if m.type == "MESH_DEFORM"]
    for n in names:
        tgt.modifiers.remove(tgt.modifiers[n])
    removed[tgt.name] = names
REC["mesh_deform_removed"] = removed

BONES = [b.name for b in arm.data.bones]
REC["bone_count"] = len(BONES)


def band_of(positions):
    zs = [p.z for p in positions]
    zmin, zmax = min(zs), max(zs)
    lo = zmin + 0.66 * (zmax - zmin)
    hi = zmin + 0.84 * (zmax - zmin)
    idx = [i for i, p in enumerate(positions) if lo <= p.z <= hi]
    return lo, hi, idx


world = [body.matrix_world @ v.co for v in body.data.vertices]
lo, hi, band_idx = band_of(world)
REC["band"] = {"lo": round(lo, 5), "hi": round(hi, 5), "verts": len(band_idx)}

cage_rec = {}
for side in ("L", "R"):
    cage = objs["PrimaCage.%s" % side]
    # --- Pin group: the flat chest-wall face. Front is -Y, so the
    # chest-wall plane is the cage-local maximum-Y vertex plane.
    ys = [v.co.y for v in cage.data.vertices]
    ymax = max(ys)
    pin_idx = [i for i, v in enumerate(cage.data.vertices)
               if v.co.y > ymax - 1e-5]
    pin = cage.vertex_groups.new(name="Pin")
    pin.add(pin_idx, 1.0, "REPLACE")
    # --- empty bone groups (Ctrl+P Armature Deform With Empty Groups,
    # API form), then parent to the armature keeping world transform.
    for bn in BONES:
        cage.vertex_groups.new(name=bn)
    mw = cage.matrix_world.copy()
    cage.parent = arm
    cage.matrix_parent_inverse = arm.matrix_world.inverted()
    cage.matrix_world = mw
    bpy.context.view_layer.update()
    drift = (cage.matrix_world.translation - mw.translation).length
    assert drift < 1e-6, "cage moved on parenting: %s" % drift
    # --- Data Transfer of the body's vertex-group weights, applied
    # from the top of the stack (video 05:22). Bounce key is removed
    # for the apply (weight transfer does not need it; the cloth
    # route never keys Bounce) and re-added empty afterwards.
    sk = cage.data.shape_keys
    bounce_present = sk is not None and "Bounce" in sk.key_blocks
    if bounce_present:
        cage.shape_key_remove(sk.key_blocks["Bounce"])
    dt = cage.modifiers.new(name="XferVG", type="DATA_TRANSFER")
    dt.object = body
    dt.use_vert_data = True
    dt.data_types_verts = {"VGROUP_WEIGHTS"}
    bpy.context.view_layer.objects.active = cage
    for o in scene.objects:
        o.select_set(o == cage)
    bpy.ops.object.modifier_apply(modifier=dt.name)
    if bounce_present:
        cage.shape_key_add(name="Bounce")
    # weight sanity: transferred weights should sum to ~1 per vertex
    sums = []
    for v in cage.data.vertices:
        s = sum(g.weight for g in v.groups)
        sums.append(s)
    # --- Armature modifier (cage follows the rig), then Cloth.
    am = cage.modifiers.new(name="Armature", type="ARMATURE")
    am.object = arm
    if NOCLOTH:
        cage_rec[side] = {
            "pin_verts": len(pin_idx),
            "weight_sum_min": round(min(sums), 4),
            "weight_sum_mean": round(sum(sums) / len(sums), 4),
            "weight_sum_max": round(max(sums), 4),
            "mods_after": [(m.name, m.type) for m in cage.modifiers],
            "parent": cage.parent.name,
        }
        continue
    cl = cage.modifiers.new(name="Cloth", type="CLOTH")
    s = cl.settings
    s.quality = 5            # OPEN in the source; 5 = Blender default, stated
    s.mass = 3.0             # video: keep between 2 and 4
    s.vertex_group_mass = "Pin"
    s.pin_stiffness = 0.0    # video: pin stiffness 0
    s.use_pressure = True
    s.pressure_factor = PRESSURE_FACTOR   # video: Pressure Scale 10,000 (kPa); variant overrides
    s.uniform_pressure_force = 0.0  # volume-preserving balloon; no
    # constant inflation value is given by the source (OPEN).
    s.effector_weights.gravity = 0.5  # video: gravity multiplier 0.5
    cl.collision_settings.use_collision = True
    cl.collision_settings.collision_quality = 2
    pc = cl.point_cache
    pc.use_disk_cache = True
    pc.name = "ns39cloth_%s" % side
    pc.frame_start = 1
    pc.frame_end = 48
    col = cage.modifiers.new(name="Collision", type="COLLISION")
    cage_rec[side] = {
        "pin_verts": len(pin_idx),
        "weight_sum_min": round(min(sums), 4),
        "weight_sum_mean": round(sum(sums) / len(sums), 4),
        "weight_sum_max": round(max(sums), 4),
        "mods_after": [(m.name, m.type) for m in cage.modifiers],
        "parent": cage.parent.name,
    }
REC["cages"] = cage_rec

# --- collision on the body (estate form of the video's collision
# shell: the full body carries Collision; the shell in the video is
# the same surface reduced to colliding regions — recorded as an
# adaptation in BAKE-DETERMINISM.md).
body.modifiers.new(name="Collision", type="COLLISION")

# --- Surface Deform binding on the body, per side (S5.3 names).
bind_rec = {}
for side in ("L", "R"):
    cage = objs["PrimaCage.%s" % side]
    sd = body.modifiers.new(name="CageSurface.%s" % side,
                            type="SURFACE_DEFORM")
    sd.target = cage
    sd.vertex_group = "Cage.%s" % side
    bpy.context.view_layer.objects.active = body
    for o in scene.objects:
        o.select_set(o == body)
    bpy.ops.object.surfacedeform_bind(modifier=sd.name)
    bind_rec[side] = {"is_bound": bool(sd.is_bound),
                      "strength": sd.strength, "falloff": sd.falloff}
    assert sd.is_bound, "Surface Deform bind failed %s" % side
REC["surface_deform"] = bind_rec
REC["body_mods_after"] = [(m.name, m.type) for m in body.modifiers]

# --- skeletal drive beat (pilot timing grid, 24 fps).
DRIVE = [(1, 0.0, 0.0), (4, -5.0, -3.0), (7, 7.0, 4.0), (10, 0.0, 0.0),
         (13, 2.5, 1.5), (19, 0.0, 0.0), (48, 0.0, 0.0)]
for bn in ("mixamorig:Spine", "mixamorig:Spine1"):
    arm.pose.bones[bn].rotation_mode = "XYZ"
for fr, spine_deg, spine1_deg in DRIVE:
    scene.frame_set(fr)
    arm.pose.bones["mixamorig:Spine"].rotation_euler = (
        math.radians(spine_deg), 0.0, 0.0)
    arm.pose.bones["mixamorig:Spine1"].rotation_euler = (
        math.radians(spine1_deg), 0.0, 0.0)
    arm.pose.bones["mixamorig:Spine"].keyframe_insert(
        "rotation_euler", frame=fr)
    arm.pose.bones["mixamorig:Spine1"].keyframe_insert(
        "rotation_euler", frame=fr)


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


n_lin = 0
if arm.animation_data and arm.animation_data.action:
    for fc in action_fcurves(arm.animation_data.action):
        for kp in fc.keyframe_points:
            kp.interpolation = "LINEAR"
            n_lin += 1
REC["drive"] = {"keys": DRIVE, "linear_points": n_lin}

# --- evidence camera (render_probe form: WORKBENCH matcap bust view)
scene.render.engine = "BLENDER_WORKBENCH"
scene.display.shading.light = "MATCAP"
scene.display.shading.color_type = "SINGLE"
scene.display.shading.single_color = (0.62, 0.58, 0.55)
scene.render.resolution_x = 512
scene.render.resolution_y = 640
scene.render.use_stamp = False
cen = sum((world[i] for i in band_idx), body.matrix_world.translation * 0)
cen = cen / len(band_idx)
from mathutils import Vector
cen = Vector((0.0, 0.0, 0.0))
for i in band_idx:
    cen += world[i]
cen /= len(band_idx)
cam_data = bpy.data.cameras.new("NS39Cam")
cam = bpy.data.objects.new("NS39Cam", cam_data)
scene.collection.objects.link(cam)
cam.location = cen + Vector((0.0, -1.05, 0.03))
cam.rotation_euler = (Vector((cen.x, cen.y, cen.z + 0.03))
                      - cam.location).to_track_quat("-Z", "Y").to_euler()
cam_data.lens = 55
scene.camera = cam
for nm in ("Prima_Outfit", "Prima_OutfitEnd", "Prima_Hair"):
    objs[nm].hide_render = True
REC["camera"] = {"centroid": [round(x, 4) for x in cen],
                 "note": "bodies-only evidence renders (outfits/hair "
                         "hidden in render); displacement measured on "
                         "Prima_Body"}

scene.frame_set(1)
os.makedirs(os.path.dirname(OUT_BLEND), exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=OUT_BLEND)
with open(REC_PATH, "w") as f:
    json.dump(REC, f, indent=1, sort_keys=True)
print("CLOTH_BUILD_DONE", json.dumps(bind_rec))
