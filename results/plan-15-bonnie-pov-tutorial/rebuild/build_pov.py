#!/usr/bin/env python3
"""Plan 15 Pass 3 clean-room rebuild — POV viewpoint rig on the Plan 01 loop.

Opens a COPY of the Plan 01 scene (Prima = Follower/partner,
Yui = Leader/viewpoint character; 78 samples @ 60 Hz, Contact 38,
follower peak 45) and builds the distilled viewpoint rig from
runs/plan-15/TECHNIQUE.md alone:

  Armature_Yui:mixamorig:Head
    --(Child Of, Influence 1.000, manual Set Inverse)--> POVAnchor (empty)
    --(plain parent)--> POVBob (empty, keyed authored head-motion layer)
    --(plain parent)--> POVCam (camera)

Body presence: the viewpoint character's own hands/forearms are
already in the scene (Yui's hands solved onto Prima's thighs in
the Plan 01 build); the POV framing is solved at frame 0 so those
hands sit inside the lower frame, and their registration is
measured, not assumed.

Measurements (records/pov_measurements.json):
  - contact anchor (Prima mixamorig:Hips head) and Yui hand
    screen positions under POVCam and under the fixed NSCam for
    every sample 0..78 (world_to_camera_view), with per-axis
    standard deviation in px at 960x540.
  - hand-presence registration error: 3D distance (mm) and
    screen distance (px, POVCam) between each Yui Hand bone head
    and its nominal grip point on Prima's UpLeg (frac 0.10 +
    world offset (0, 0.05, 0.055), the Plan 01 solve target).
  - anchor world drift (the Plan 01 lock, re-measured here):
    ContactEmpty vs Prima Hips head, mm.

Evidence renders: POVCam at samples 0, 19, 38, 45, 58, 78
(960x540, same engine route as Plan 01) + fixed-cam sample 38
re-render for the comparison record. Determinism is proven by
the caller running this script twice and comparing decoded-pixel
hashes (pixelhash.py from Plan 01).

Usage: blender -b -Y --factory-startup --python build_pov.py -- \
       <src_blend> <out_dir>
"""
import bpy
import json
import math
import os
import sys

from mathutils import Matrix, Vector

argv = sys.argv[sys.argv.index("--") + 1:]
SRC, OUT = argv[0], argv[1]
os.makedirs(os.path.join(OUT, "frames"), exist_ok=True)
os.makedirs(os.path.join(OUT, "records"), exist_ok=True)
os.makedirs(os.path.join(OUT, "scene"), exist_ok=True)

M = "mixamorig:"
FPS = 60
CYCLE = 78
CONTACT = 38
FOLLOWER_PEAK = 45
RES_X, RES_Y = 960, 540

REC = {"blender": bpy.app.version_string, "src_blend": SRC}


def B(n):
    return M + n


def log(*a):
    print("[ns15r]", *a, flush=True)


bpy.ops.wm.open_mainfile(filepath=SRC)
scene = bpy.context.scene
arm_p = bpy.data.objects["Armature_Prima"]
arm_y = bpy.data.objects["Armature_Yui"]
fixed_cam = bpy.data.objects["NSCam"]
contact_empty = bpy.data.objects["ContactEmpty"]

# ------------------------------------------------------------ rig build
scene.frame_set(0)
bpy.context.view_layer.update()


def bone_head_world(arm, bn):
    bpy.context.view_layer.update()
    pb = arm.pose.bones[bn]
    return (arm.matrix_world @ pb.matrix).translation.copy()


def bone_world_matrix(arm, bn):
    bpy.context.view_layer.update()
    pb = arm.pose.bones[bn]
    return (arm.matrix_world @ pb.matrix).copy()


head0 = bone_head_world(arm_y, B("Head"))
target0 = bone_head_world(arm_p, B("Hips")) + Vector((0, 0, 0.05))
# Eye offset in HEAD-BONE space (probe_gaze.py, frame 0): the head
# bone head sits at the neck joint; the eyes sit up the bone (+Y)
# and out of the face (+Z in bone space). A world-axis offset put
# the camera inside Yui's hair mesh (run A failure, recorded in
# PASS3-REBUILD.md): hair bbox at frame 0 spans world y
# -0.082..0.089 / z 1.115..1.319; the bone-space offset below
# lands the eye at world y approx -0.107, in front of the hair.
head_mat0 = bone_world_matrix(arm_y, B("Head"))
eye0 = head_mat0 @ Vector((0.0, 0.10, 0.09))

anchor = bpy.data.objects.new("POVAnchor", None)
scene.collection.objects.link(anchor)
look = (target0 - eye0).to_track_quat('-Z', 'Y')
anchor.matrix_world = Matrix.Translation(eye0) @ look.to_matrix().to_4x4()

con = anchor.constraints.new('CHILD_OF')
con.name = "POVHeadLock"
con.target = arm_y
con.subtarget = B("Head")
con.use_location_x = con.use_location_y = con.use_location_z = True
con.use_rotation_x = con.use_rotation_y = con.use_rotation_z = True
con.use_scale_x = con.use_scale_y = con.use_scale_z = True
con.influence = 1.0
pre_world = anchor.matrix_world.copy()
con.inverse_matrix = bone_world_matrix(arm_y, B("Head")).inverted()
bpy.context.view_layer.update()
delta_mm = (anchor.matrix_world.translation - pre_world.translation).length * 1000.0
REC["setinverse_delta_mm"] = round(delta_mm, 6)
REC["anchor_frame0_eye_m"] = [round(v, 5) for v in eye0]
REC["anchor_frame0_target_m"] = [round(v, 5) for v in target0]
log("set-inverse delta mm:", REC["setinverse_delta_mm"])

# Bob layer: authored keys driven by the Leader phase table of the
# Plan 01 loop (p: 0->0, 15->0.12, 38->1.0, 53->0.38, 78->0), plus a
# 2-cycles-per-loop micro sway. Local axes of POVBob = anchor axes
# (camera looks down local -Z): forward bob = -Z, dip = -Y... in
# Blender object space the anchor's local Y is camera-up, Z is
# back. Bob: translation (0, -0.006*p, -0.012*p) metres and pitch
# rotation_x = +1.1 deg * p (look further down as the thrust
# lands), roll rotation_z = 0.35 deg * sin(2 * 2pi * s/78).
bob = bpy.data.objects.new("POVBob", None)
scene.collection.objects.link(bob)
# Plain parent, identity parent-inverse: POVBob's local transform
# (the keyed bob) is expressed directly in anchor space, so at
# local identity the bob frame IS the anchor frame.
bob.parent = anchor
bob.matrix_parent_inverse = Matrix.Identity(4)

PHASE = {0: 0.0, 15: 0.12, 26: 0.55, 38: 1.0, 45: 0.92, 53: 0.38,
         65: 0.15, 78: 0.0}
bob.animation_data_create()
act = bpy.data.actions.new("POVBobAction")
bob.animation_data.action = act


def key_bob():
    frames = sorted(PHASE)
    for s in frames:
        p = PHASE[s]
        sway = math.sin(2 * 2 * math.pi * s / CYCLE)
        bob.location = (0.0, -0.006 * p, -0.012 * p)
        bob.rotation_euler = (math.radians(1.1 * p), 0.0,
                              math.radians(0.35 * sway))
        bob.keyframe_insert(data_path="location", frame=s)
        bob.keyframe_insert(data_path="rotation_euler", frame=s)
    # Seam law: frame 78 keys are copies of frame 0 values (they are:
    # PHASE[78] = PHASE[0] = 0 and sway(78) = sway(0) = 0).


key_bob()
REC["bob_phase_table"] = {str(k): v for k, v in PHASE.items()}
REC["bob_amplitudes"] = {"forward_m_at_p1": 0.012, "dip_m_at_p1": 0.006,
                         "pitch_deg_at_p1": 1.1, "roll_deg_micro": 0.35,
                         "roll_cycles_per_loop": 2}

# Camera
cam_data = bpy.data.cameras.new("POVCamData")
cam_data.lens = 21.0
cam_data.clip_start = 0.02
cam_data.clip_end = 20.0
pov_cam = bpy.data.objects.new("POVCam", cam_data)
scene.collection.objects.link(pov_cam)
# Plain parent, identity parent-inverse + identity local: the
# camera frame IS the bob frame.
pov_cam.parent = bob
pov_cam.matrix_parent_inverse = Matrix.Identity(4)
REC["camera"] = {"lens_mm": 21.0, "parent_chain":
                 "POVCam -> POVBob -> POVAnchor -(Child Of 1.000)-> "
                 "Armature_Yui:mixamorig:Head"}

# F-curve discipline: LINEAR + CYCLES on the bob action (5.2 layered
# actions: fcurves live on strip.channelbag(slot) — a method that
# requires the action slot; Plan 01's probed route).
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


fcurves = action_fcurves(act)
for fc in fcurves:
    for kp in fc.keyframe_points:
        kp.interpolation = 'LINEAR'
    mod = fc.modifiers.new('CYCLES')
    mod.mode_before = 'REPEAT'
    mod.mode_after = 'REPEAT'
REC["bob_fcurves"] = len(fcurves)

# Render setup matches Plan 01 evidence (EEVEE probe order, 960x540).
for cand in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE", "BLENDER_WORKBENCH"):
    try:
        scene.render.engine = cand
        if scene.render.engine == cand:
            break
    except Exception:
        continue
REC["render_engine"] = scene.render.engine
scene.render.resolution_x = RES_X
scene.render.resolution_y = RES_Y
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.film_transparent = False

# ------------------------------------------------------------ measures
from bpy_extras.object_utils import world_to_camera_view

GRIP_OFF = Vector((0, 0.05, 0.055))
GRIP_FRAC = 0.10


def grip_point(side):
    head = bone_head_world(arm_p, B(side + "UpLeg"))
    knee = bone_head_world(arm_p, B(side + "Leg"))
    return head + (knee - head) * GRIP_FRAC + GRIP_OFF


# Frozen registration offset (the Plan 01 definition): each Yui
# hand's frame-0 position expressed in the target UpLeg bone's
# frame; per-frame error is measured against upmat @ offset.
scene.frame_set(0)
bpy.context.view_layer.update()
HAND_OFF = {}
for side in ("Left", "Right"):
    upmat = bone_world_matrix(arm_p, B(side + "UpLeg"))
    HAND_OFF[side] = upmat.inverted() @ bone_head_world(
        arm_y, B(side + "Hand"))
yui_pelvis_anchor = bpy.data.objects["Anchor_Fluid_Pelvis.001"]


def screen(cam_ob, world):
    v = world_to_camera_view(scene, cam_ob, world)
    return [v.x * RES_X, (1.0 - v.y) * RES_Y, v.z]


meas = {"contact_pov_px": [], "contact_fixed_px": [],
        "handL_pov_px": [], "handR_pov_px": [],
        "handL_err_mm": [], "handR_err_mm": [],
        "handL_err_px": [], "handR_err_px": [],
        "anchor_drift_mm": [], "head_world": [],
        "pelvis_pov_px": [], "pelvis_fixed_px": [],
        "spine2_pov_px": [], "spine2_fixed_px": [],
        "phead_pov_px": [], "phead_fixed_px": [],
        "handLf_err_mm": [], "handRf_err_mm": [],
        "handLf_err_px": [], "handRf_err_px": [],
        "cam_world": [], "bob_world": []}
for s in range(0, CYCLE + 1):
    scene.frame_set(s)
    bpy.context.view_layer.update()
    contact = bone_head_world(arm_p, B("Hips"))
    hl = bone_head_world(arm_y, B("LeftHand"))
    hr = bone_head_world(arm_y, B("RightHand"))
    gl, gr = grip_point("Left"), grip_point("Right")
    meas["contact_pov_px"].append(screen(pov_cam, contact))
    meas["contact_fixed_px"].append(screen(fixed_cam, contact))
    pelvis = yui_pelvis_anchor.matrix_world.translation.copy()
    spine2 = bone_head_world(arm_p, B("Spine2"))
    phead = bone_head_world(arm_p, B("Head"))
    meas["pelvis_pov_px"].append(screen(pov_cam, pelvis))
    meas["pelvis_fixed_px"].append(screen(fixed_cam, pelvis))
    meas["spine2_pov_px"].append(screen(pov_cam, spine2))
    meas["spine2_fixed_px"].append(screen(fixed_cam, spine2))
    meas["phead_pov_px"].append(screen(pov_cam, phead))
    meas["phead_fixed_px"].append(screen(fixed_cam, phead))
    meas["cam_world"].append([round(v, 5) for v in
                              pov_cam.matrix_world.translation])
    meas["bob_world"].append([round(v, 5) for v in
                              bob.matrix_world.translation])
    for side, hand, key in (("Left", hl, "L"), ("Right", hr, "R")):
        upmat = bone_world_matrix(arm_p, B(side + "UpLeg"))
        tgt = upmat @ HAND_OFF[side]
        meas[f"hand{key}f_err_mm"].append(
            round((hand - tgt).length * 1000.0, 4))
        st = screen(pov_cam, tgt)
        sh = screen(pov_cam, hand)
        meas[f"hand{key}f_err_px"].append(
            round(math.hypot(sh[0] - st[0], sh[1] - st[1]), 3))
    meas["handL_pov_px"].append(screen(pov_cam, hl))
    meas["handR_pov_px"].append(screen(pov_cam, hr))
    meas["handL_err_mm"].append(round((hl - gl).length * 1000.0, 4))
    meas["handR_err_mm"].append(round((hr - gr).length * 1000.0, 4))
    sgl, sgr = screen(pov_cam, gl), screen(pov_cam, gr)
    shl, shr = meas["handL_pov_px"][-1], meas["handR_pov_px"][-1]
    meas["handL_err_px"].append(round(math.hypot(shl[0] - sgl[0],
                                                 shl[1] - sgl[1]), 3))
    meas["handR_err_px"].append(round(math.hypot(shr[0] - sgr[0],
                                                 shr[1] - sgr[1]), 3))
    ce = contact_empty.matrix_world.translation.copy()
    meas["anchor_drift_mm"].append(round((ce - contact).length * 1000.0, 4))
    meas["head_world"].append([round(v, 5) for v in
                               bone_head_world(arm_y, B("Head"))])


def std(vals):
    n = len(vals)
    mu = sum(vals) / n
    return math.sqrt(sum((v - mu) ** 2 for v in vals) / n)


def screen_stats(rows):
    xs = [r[0] for r in rows]
    ys = [r[1] for r in rows]
    return {"std_x_px": round(std(xs), 3), "std_y_px": round(std(ys), 3),
            "range_x_px": round(max(xs) - min(xs), 3),
            "range_y_px": round(max(ys) - min(ys), 3),
            "mean_x_px": round(sum(xs) / len(xs), 2),
            "mean_y_px": round(sum(ys) / len(ys), 2)}


summary = {
    "contact_anchor_screen": {
        "pov": screen_stats(meas["contact_pov_px"]),
        "fixed": screen_stats(meas["contact_fixed_px"])},
    "yui_pelvis_anchor_screen": {
        "pov": screen_stats(meas["pelvis_pov_px"]),
        "fixed": screen_stats(meas["pelvis_fixed_px"])},
    "prima_spine2_screen": {
        "pov": screen_stats(meas["spine2_pov_px"]),
        "fixed": screen_stats(meas["spine2_fixed_px"])},
    "prima_head_screen": {
        "pov": screen_stats(meas["phead_pov_px"]),
        "fixed": screen_stats(meas["phead_fixed_px"])},
    "handLf_err_mm": {"max": max(meas["handLf_err_mm"]),
                      "mean": round(sum(meas["handLf_err_mm"]) / 79, 4)},
    "handRf_err_mm": {"max": max(meas["handRf_err_mm"]),
                      "mean": round(sum(meas["handRf_err_mm"]) / 79, 4)},
    "handLf_err_px_max": max(meas["handLf_err_px"]),
    "handRf_err_px_max": max(meas["handRf_err_px"]),
    "handL_err_mm": {"max": max(meas["handL_err_mm"]),
                     "mean": round(sum(meas["handL_err_mm"]) / 79, 4)},
    "handR_err_mm": {"max": max(meas["handR_err_mm"]),
                     "mean": round(sum(meas["handR_err_mm"]) / 79, 4)},
    "handL_err_px_at_peaks": {str(s): meas["handL_err_px"][s]
                              for s in (19, 38, 45)},
    "handR_err_px_at_peaks": {str(s): meas["handR_err_px"][s]
                              for s in (19, 38, 45)},
    "handL_err_px_max": max(meas["handL_err_px"]),
    "handR_err_px_max": max(meas["handR_err_px"]),
    "anchor_drift_mm": {"max": max(meas["anchor_drift_mm"]),
                        "mean": round(sum(meas["anchor_drift_mm"]) / 79, 5)},
    "contact_px_at_peaks": {
        str(s): {"pov": meas["contact_pov_px"][s],
                 "fixed": meas["contact_fixed_px"][s]}
        for s in (0, 19, 38, 45, 58, 78)},
    "hands_in_frame_pov": {
        str(s): {"L": meas["handL_pov_px"][s], "R": meas["handR_pov_px"][s]}
        for s in (0, 19, 38, 45, 58, 78)},
}
REC["summary"] = summary
log("summary:", json.dumps(summary, indent=1))

with open(os.path.join(OUT, "records", "pov_measurements.json"), "w") as f:
    json.dump(meas, f)
with open(os.path.join(OUT, "records", "pov_build_record.json"), "w") as f:
    json.dump(REC, f, indent=1)

# --- occlusion record: first render-visible surface on eye->contact ray ---
def first_visible_hit(dg, origin, target):
    d = target - origin
    dist = d.length
    if dist < 1e-9:
        return None
    direction = d / dist
    loc = origin.copy()
    for _ in range(24):
        hit, hloc, _n, _i, obj, _m = scene.ray_cast(
            dg, loc + direction * 1e-4, direction, distance=dist + 0.6)
        if not hit:
            return None
        travelled = (hloc - origin).length
        if obj.hide_render:
            loc = hloc
            continue
        return {"object": obj.name, "distance_m": round(travelled, 4)}
    return None


REC["occlusion"] = {}
for s in (0, 19, 38, 45, 58, 78):
    scene.frame_set(s)
    dg = bpy.context.evaluated_depsgraph_get()
    eye = pov_cam.matrix_world.translation.copy()
    tgt = bone_head_world(arm_p, B("Hips")) + Vector((0, 0, 0.05))
    REC["occlusion"][str(s)] = {
        "to_contact": first_visible_hit(dg, eye, tgt),
        "contact_distance_m": round((tgt - eye).length, 4)}
with open(os.path.join(OUT, "records", "pov_build_record.json"), "w") as f:
    json.dump(REC, f, indent=1)

# ------------------------------------------------------------ renders
scene.camera = pov_cam
for s in (0, 19, 38, 45, 58, 78):
    scene.frame_set(s)
    scene.render.filepath = os.path.join(OUT, "frames", "pov_%04d.png" % s)
    bpy.ops.render.render(write_still=True)
    log("rendered pov", s)
scene.camera = fixed_cam
scene.frame_set(38)
scene.render.filepath = os.path.join(OUT, "frames", "fixed_0038.png")
bpy.ops.render.render(write_still=True)
log("rendered fixed 38")

scene.camera = pov_cam
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "scene",
                                                  "pov_scene.blend"))
log("POV_BUILD_OK")
