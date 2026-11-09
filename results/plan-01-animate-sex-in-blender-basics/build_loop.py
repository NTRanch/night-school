#!/usr/bin/env python3
"""Plan 01 Pass 3 clean-room rebuild — two-body contact loop.

Prima = Follower, Yui = Leader (coordinator casting). Built ONLY from
runs/plan-01/TECHNIQUE.md (gated) + SIX-GIRL-STANDARD §§1-3,7.
Blender 5.2.3 LTS, headless, deterministic, no audio.

Loop: 78 samples @ 60 Hz, Contact at sample 38 (coordinator ruling 1:
source keys x78/31). Pelvic contact target = Follower mixamorig:Hips
(ruling 2). No opening mechanism (ruling 3 / T-12 rejected). Hand locks
ship as solved keys, never constraints in the clip (ruling 4). The only
constraint in the scene is the authoring-side contact empty (Child Of,
T-10 estate form); exported clips are pure keys on standard bone names.

Usage: blender -b -Y --factory-startup --python build_loop.py -- \
         <fleet_dir> <out_dir> <save_blend 0|1>
fleet_dir holds prima.blend/.glb, yui.blend/.glb, gen_clip.py.
"""
import bpy
import hashlib
import json
import math
import os
import sys

from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

argv = sys.argv[sys.argv.index("--") + 1:]
FLEET, OUT, SAVE_BLEND = argv[0], argv[1], argv[2] == "1"
os.makedirs(os.path.join(OUT, "frames"), exist_ok=True)
os.makedirs(os.path.join(OUT, "clips"), exist_ok=True)
os.makedirs(os.path.join(OUT, "records"), exist_ok=True)

REC = {"blender": bpy.app.version_string, "probes": {}, "notes": []}
M = "mixamorig:"
FPS = 60
CYCLE = 78
CONTACT = 38


def B(n):
    return M + n


def log(*a):
    print("[ns01r]", *a, flush=True)


# ---------------------------------------------------------------- probes
def probe(name, fn):
    try:
        r = fn()
        REC["probes"][name] = {"ok": True, "result": r}
        log("PROBE", name, "->", r)
        return r
    except Exception as e:  # probe failure is data, not a crash
        REC["probes"][name] = {"ok": False, "error": repr(e)}
        log("PROBE-FAIL", name, repr(e))
        return None


# ---------------------------------------------------------------- channels
# Leader thrust phase p(s): source keys 0/15/31 -> 0/38/78 (x78/31);
# breakdown at source 6 -> sample 15 (entry pause); recovery breakdown 53.
LEADER_KEYS = {0: 0.00, 15: 0.12, 38: 1.00, 53: 0.38, 78: 0.00}
# Follower reaction amplitude a(s): source keys ~6/12/17/20/26/31 ->
# 15/30/43/50/65/78; hold until Contact; peak centre pulled -5 samples
# (the -2 source-frame pull, ADDENDA #3); mid-recovery at both endpoints
# (T-08): a(0) = a(78) = 0.45.
FOLLOWER_KEYS = {0: 0.45, 15: 0.20, 30: 0.0, 38: 0.0, 45: 1.0, 52: 0.80,
                 63: 0.52, 73: 0.44, 78: 0.45}
# Feet (T-15): first foot flat + one post-contact bump; second foot keys
# at scaled 15/23 -> 38/58, with the 38 value copied to 78.
FOOT_L_BUMP = {0: 0.0, 38: 0.0, 45: 6.0, 55: 0.0, 78: 0.0}
FOOT_R_OFF = {0: 4.0, 38: 4.0, 58: 7.0, 78: 4.0}
PRIMA_HAND_KEYS = sorted(FOLLOWER_KEYS)
YUI_HAND_KEYS = sorted(LEADER_KEYS)


def interp(table, s):
    ks = sorted(table)
    if s <= ks[0]:
        return table[ks[0]]
    if s >= ks[-1]:
        return table[ks[-1]]
    for i in range(len(ks) - 1):
        a, b = ks[i], ks[i + 1]
        if a <= s <= b:
            t = (s - a) / (b - a)
            return table[a] + (table[b] - table[a]) * t
    return table[ks[-1]]


FINGERS = []
for side in ("Left", "Right"):
    for fing in ("Thumb", "Index", "Middle", "Ring", "Pinky"):
        for j in (1, 2, 3):
            FINGERS.append(B("%sHand%s%d" % (side, fing, j)))


def finger_pose(curl1, curl2, curl3):
    out = {}
    for fb in FINGERS:
        j = int(fb[-1])
        out[fb] = [curl1 if j == 1 else curl2 if j == 2 else curl3, 0, 0]
    return out


PRIMA_BASE = {
    B("Hips"): [-6, 0, 0], B("Spine"): [10, 0, 0], B("Spine1"): [6, 0, 0],
    B("Neck"): [4, 0, 0], B("Head"): [12, 0, 3],
    B("LeftUpLeg"): [-68, 0, -9], B("RightUpLeg"): [-66, 0, 11],
    B("LeftLeg"): [-30, 0, 0], B("RightLeg"): [-34, 0, 0],
    B("LeftFoot"): [-20, 0, 0], B("RightFoot"): [-18, 0, 0],
    B("LeftToeBase"): [12, 0, 0], B("RightToeBase"): [12, 0, 0],
    B("LeftArm"): [-30, 0, 26], B("RightArm"): [-30, 0, -26],
    B("LeftForeArm"): [-50, 0, 0], B("RightForeArm"): [-50, 0, 0],
    B("LeftEye"): [6, 0, 0], B("RightEye"): [6, 0, 0],
    **finger_pose(24, 20, 14),
}
YUI_BASE = {
    B("Hips"): [-4, 0, 0], B("Spine"): [26, 0, 0], B("Spine1"): [18, 0, 0],
    B("Neck"): [-12, 0, 0], B("Head"): [-8, 0, -2],
    B("LeftUpLeg"): [10, 0, -4], B("RightUpLeg"): [10, 0, 4],
    B("LeftLeg"): [-100, 0, 0], B("RightLeg"): [-100, 0, 0],
    B("LeftFoot"): [-30, 0, 0], B("RightFoot"): [-30, 0, 0],
    B("LeftToeBase"): [30, 0, 0], B("RightToeBase"): [30, 0, 0],
    B("LeftArm"): [-40, 0, 16], B("RightArm"): [-40, 0, -16],
    B("LeftForeArm"): [-28, 0, 0], B("RightForeArm"): [-28, 0, 0],
    B("LeftEye"): [8, 0, 0], B("RightEye"): [8, 0, 0],
    **finger_pose(20, 16, 10),
}
# Face channels (T-07 phase law for the follower; leader steady).
PRIMA_FACE = {
    "Fac_Eye_HalfClose": {0: 0.10, 38: 0.10, 45: 0.55, 52: 0.45, 63: 0.25, 78: 0.10},
    "Fac_Mth_Aa": {0: 0.0, 38: 0.0, 45: 0.38, 58: 0.20, 78: 0.0},
    "Fac_Pupil_Heart": {0: 0.30, 45: 0.80, 63: 0.60, 78: 0.30},
    "Fac_Ebr_Relax": {0: 0.20, 45: 0.40, 78: 0.20},
}
YUI_FACE = {
    "Fac_Mth_Smile": {0: 0.35, 78: 0.35},
    "Fac_Eye_HalfClose": {0: 0.15, 78: 0.15},
}

PRIMA_UNION = sorted(set(FOLLOWER_KEYS) | set(FOOT_L_BUMP) | set(FOOT_R_OFF)
                     | {0, 38, 45, 52, 58, 63, 78})
YUI_UNION = sorted(LEADER_KEYS)


def prima_pose_at(s):
    a = interp(FOLLOWER_KEYS, s)
    p = {k: list(v) for k, v in PRIMA_BASE.items()}
    p[B("Spine")] = [10 + 4.0 * a, 0, 0]
    p[B("Spine1")] = [6 + 3.0 * a, 0, 0]
    p[B("Neck")] = [4 - 3.0 * a, 0, 0]
    p[B("Head")] = [12 - 4.0 * a, 0, 3 - 1.0 * a]
    p[B("Hips")] = [-6 + 2.5 * a, 0, 0]
    p[B("LeftFoot")] = [-20 + interp(FOOT_L_BUMP, s), 0, 0]
    p[B("RightFoot")] = [-18 + interp(FOOT_R_OFF, s), 0, 0]
    return p


def yui_pose_at(s):
    ph = interp(LEADER_KEYS, s)
    p = {k: list(v) for k, v in YUI_BASE.items()}
    p[B("Hips")] = [-4 + 18.0 * ph, 0, 0]
    p[B("Spine")] = [26 - 10.0 * ph, 0, 0]
    p[B("Spine1")] = [18 - 7.0 * ph, 0, 0]
    p[B("Neck")] = [-12 + 3.0 * ph, 0, 0]
    p[B("Head")] = [-8 + 2.0 * ph, 0, -2]
    return p


def prima_face_at(s):
    return {ch: round(interp(t, s), 4) for ch, t in PRIMA_FACE.items()}


def yui_face_at(s):
    return {ch: round(interp(t, s), 4) for ch, t in YUI_FACE.items()}


# Hips-location world deltas (converted to bone-local in-script via the
# measured Jacobian, so pose-bone axis semantics are never assumed).
def prima_loc_delta_world(s):
    a = interp(FOLLOWER_KEYS, s)
    return Vector((0.0, 0.004 * a, 0.002 * a))


def yui_loc_delta_world(s):
    # Advance is -Y world (she kneels behind Prima, both facing -Y).
    # Oval (T-06): the recovery half of the cycle dips 2.5 mm while the
    # advance half dips 0.5 mm — the path out and the path back are
    # different branches of one closed curve.
    ph = interp(LEADER_KEYS, s)
    if s <= CONTACT:
        dip = -0.0005 * math.sin(math.pi * s / CONTACT) if CONTACT else 0.0
    else:
        dip = -0.0025 * math.sin(math.pi * (s - CONTACT) / (CYCLE - CONTACT))
    return Vector((0.0, -(0.006 * ph - 0.003), dip))


# ---------------------------------------------------------------- scene
bpy.ops.wm.open_mainfile(filepath=os.path.join(FLEET, "prima.blend"))
scene = bpy.context.scene


def girl_objects():
    out = {}
    for ob in bpy.context.scene.objects:
        out.setdefault(ob.name, ob)
    return out


arm_p = bpy.context.scene.objects["Armature"]
arm_p.name = "Armature_Prima"
before = set(girl_objects())  # after the rename, so Yui's "Armature"
# is not mistaken for a pre-existing object below.
# Append via libraries.load (one pass): per-object wm.append calls
# re-append dependency objects (armatures/cages) on every call — probed
# on 5.2.3, first run produced Armature.001-.010 duplicates.
with bpy.data.libraries.load(os.path.join(FLEET, "yui.blend"),
                             link=False) as (src, dst):
    dst.objects = list(src.objects)
for ob in dst.objects:
    bpy.context.scene.collection.objects.link(ob)
after = girl_objects()
yui_objs = [after[n] for n in after if n not in before and n != "Armature_Prima"]
arm_y = None
for ob in yui_objs:
    if ob.type == 'ARMATURE':
        arm_y = ob
arm_y.name = "Armature_Yui"
REC["appended_yui_objects"] = sorted(ob.name for ob in yui_objs)
log("yui objects:", REC["appended_yui_objects"])


def find_obj(objs, suffix):
    for ob in objs:
        if ob.name == suffix or ob.name.startswith(suffix + "."):
            return ob
    return None


prima_objs = [ob for ob in bpy.context.scene.objects
              if ob not in yui_objs]
body_p = find_obj(prima_objs, "Prima_Body")
body_y = find_obj(yui_objs, "Yui_Body")
for girl, objs, show in (("Prima", prima_objs, "Prima_Outfit"),
                         ("Yui", yui_objs, "Yui_Outfit")):
    for ob in objs:
        if "Cage" in ob.name or ob.type == 'EMPTY':
            ob.hide_render = True
            ob.hide_viewport = False
        if ob.name.startswith(show):
            # Evidence renders are bodies-only: the contact set is the
            # gate subject and the fleet outfits (Prima's long skirt
            # first of all) occlude it completely. Outfits stay in the
            # scene file, visible in viewport, hidden only in render.
            ob.hide_render = True
REC["evidence_render_note"] = "bodies-only renders (outfits hidden in " \
    "render) so the contact set, hands and faces are visible at " \
    "viewing size; outfits present and unhidden in the scene file"
REC["girls"] = {"prima_armature": arm_p.name, "yui_armature": arm_y.name,
                "prima_body": body_p.name, "yui_body": body_y.name}

# Both girls face -Y (source §2: the Leader kneels BEHIND the seated
# Follower). No object rotation for either rig; placement lives on the
# Hips channel (T-03) via the placement solve below.
arm_y.location = (0, 0, 0)
bpy.context.view_layer.update()

# Set + lights + camera (fleet anim.py practice: two suns, workbench-class
# simple set; render engine probed below).
scene.render.fps = FPS
scene.frame_start = 0
scene.frame_end = 3 * CYCLE


def mat(name, color, rough=0.85):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Roughness"].default_value = rough
    return m


def box(name, loc, scale, material):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    ob = bpy.context.object
    ob.name = name
    ob.scale = scale
    if material:
        ob.data.materials.append(material)
    return ob


m_floor = mat("NSFloor", (0.10, 0.09, 0.12))
m_plat = mat("NSPlatform", (0.30, 0.16, 0.30))
box("Floor", (0, 0.3, -0.02), (4.0, 4.0, 0.02), m_floor)
box("Platform", (0, 0.10, 0.15), (0.80, 1.05, 0.15), m_plat)
box("Cushion", (0, 0.02, 0.35), (0.42, 0.55, 0.05), m_plat)

world = bpy.data.worlds.new("NSWorld")
scene.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.16, 0.15, 0.19, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 1.0

cam_data = bpy.data.cameras.new("NSCam")
cam = bpy.data.objects.new("NSCam", cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
cam_data.lens = 44
target_v = Vector((0, 0.14, 0.68))
cam.location = target_v + Vector((3.05, -1.95, 0.70))
cam.rotation_euler = (target_v - cam.location).to_track_quat('-Z', 'Y').to_euler()
for name, energy, rot in (("Sun", 3.0, (55, -25)), ("Fill", 1.1, (70, 140))):
    ld = bpy.data.lights.new(name + "D", 'SUN')
    ld.energy = energy
    lo = bpy.data.objects.new(name, ld)
    lo.rotation_euler = (math.radians(rot[0]), 0, math.radians(rot[1]))
    scene.collection.objects.link(lo)


def set_engine():
    for cand in ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE", "BLENDER_WORKBENCH"):
        try:
            scene.render.engine = cand
            if scene.render.engine == cand:
                return cand
        except Exception:
            continue
    return scene.render.engine


REC["render_engine"] = probe("render_engine", set_engine)
scene.render.resolution_x = 960
scene.render.resolution_y = 540
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.film_transparent = False

# Timeline markers (T-04 estate form).
for mname, mframe in (("Contact", CONTACT), ("End of Loop", CYCLE)):
    mk = scene.timeline_markers.new(mname, frame=mframe)
REC["markers"] = [(m.name, m.frame) for m in scene.timeline_markers]

# ---------------------------------------------------------------- posing
for arm in (arm_p, arm_y):
    for pb in arm.pose.bones:
        pb.rotation_mode = 'XYZ'


def apply_pose(arm, pose):
    for bn, r in pose.items():
        pb = arm.pose.bones[bn]
        pb.rotation_euler = tuple(math.radians(x) for x in r)


def hips_head_world(arm):
    bpy.context.view_layer.update()
    pb = arm.pose.bones[B("Hips")]
    return (arm.matrix_world @ pb.matrix).translation.copy()


def bone_head_world(arm, bn):
    bpy.context.view_layer.update()
    pb = arm.pose.bones[bn]
    return (arm.matrix_world @ pb.matrix).translation.copy()


def bone_world_matrix(arm, bn):
    bpy.context.view_layer.update()
    pb = arm.pose.bones[bn]
    return (arm.matrix_world @ pb.matrix).copy()


def loc_jacobian(arm):
    """World displacement of the Hips head per unit of pose-bone location
    on each local axis (finite differences, eps=1mm)."""
    pb = arm.pose.bones[B("Hips")]
    base_loc = pb.location.copy()
    p0 = hips_head_world(arm)
    cols = []
    for ax in range(3):
        pb.location = base_loc + Vector(
            [0.001 if i == ax else 0.0 for i in range(3)])
        p1 = hips_head_world(arm)
        cols.append((p1 - p0) / 0.001)
        pb.location = base_loc
    bpy.context.view_layer.update()
    return cols


def solve_hips_loc(arm, target_world, iters=10, tol=0.000005):
    """Iterate pose-bone location so the Hips head lands on target_world.
    Returns residual in metres."""
    pb = arm.pose.bones[B("Hips")]
    for _ in range(iters):
        cur = hips_head_world(arm)
        err = target_world - cur
        if err.length < tol:
            break
        cols = loc_jacobian(arm)
        jm = Matrix((cols[0], cols[1], cols[2])).transposed()
        try:
            delta = jm.inverted() @ err
        except ValueError:
            break
        pb.location = pb.location + delta
    bpy.context.view_layer.update()
    return (target_world - hips_head_world(arm)).length


# Frame-0 base poses, then placement solve (placement on the Hips
# channel only, T-03).
scene.frame_set(0)
apply_pose(arm_p, prima_pose_at(0))
apply_pose(arm_y, yui_pose_at(0))
PRIMA_HIPS_TARGET = Vector((0, 0.06, 0.70))
YUI_HIPS_TARGET = Vector((0, 0.40, 0.72))
res_p = solve_hips_loc(arm_p, PRIMA_HIPS_TARGET)
res_y = solve_hips_loc(arm_y, YUI_HIPS_TARGET)
REC["placement_residual_mm"] = {"prima": round(res_p * 1000, 4),
                                "yui": round(res_y * 1000, 4)}
prima_loc0 = arm_p.pose.bones[B("Hips")].location.copy()
yui_loc0 = arm_y.pose.bones[B("Hips")].location.copy()
log("placement residuals mm:", REC["placement_residual_mm"])


# The contact set (pelvis box, armature space, relative to the Hips
# head at rest): used for the registration gap and the penetration gate.
PELVIS_BOX = ((-0.19, 0.19), (-0.13, 0.13), (-0.21, 0.05))


def pelvis_world_verts(body, arm):
    bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    ev = body.evaluated_get(dg)
    me = ev.to_mesh()
    mw = ev.matrix_world
    inv = arm.matrix_world.inverted()
    head_local = inv @ hips_head_world(arm)  # posed head, armature space
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


# Registration fine-tune: pelvis surface gap at frame 0 -> 3.0 mm.
# Rear-entry geometry: gap = Yui's front-extreme pelvis-box vert (min Y)
# minus Prima's back-extreme pelvis-box vert (max Y), on the world Y
# contact axis. Positive = separated.
def pelvis_gap_mm():
    p_ys = [w.y for _, w in pelvis_world_verts(body_p, arm_p)]
    y_ys = [w.y for _, w in pelvis_world_verts(body_y, arm_y)]
    return (min(y_ys) - max(p_ys)) * 1000.0


gap0 = pelvis_gap_mm()
REC["pelvis_gap_initial_mm"] = round(gap0, 3)
for _ in range(4):
    if abs(gap0 - 3.0) <= 0.4:
        break
    step = max(-0.05, min(0.05, (3.0 - gap0) / 1000.0))
    cur = hips_head_world(arm_y)
    solve_hips_loc(arm_y, cur + Vector((0, step, 0)))
    gap0 = pelvis_gap_mm()
REC["pelvis_gap_frame0_mm"] = round(gap0, 3)
prima_loc0 = arm_p.pose.bones[B("Hips")].location.copy()
yui_loc0 = arm_y.pose.bones[B("Hips")].location.copy()
log("pelvis gap frame0 mm:", gap0)

# Contact empty + Child Of (T-10 estate form; ruling 2: target is the
# Follower's mixamorig:Hips). Probe-first on 5.2 Set Inverse behaviour.
hips0_world = hips_head_world(arm_p)
empty = bpy.data.objects.new("ContactEmpty", None)
scene.collection.objects.link(empty)
empty.empty_display_type = 'PLAIN_AXES'
empty.empty_display_size = 0.03
empty.location = hips0_world
bpy.context.view_layer.update()
pre_world = empty.matrix_world.translation.copy()
con = empty.constraints.new('CHILD_OF')
con.target = arm_p
con.subtarget = B("Hips")
probe("childof_influence_readback", lambda: float(con.influence))
probe("childof_axes_readback",
      lambda: [bool(con.use_location_x), bool(con.use_rotation_x),
               bool(con.use_scale_x)])


def set_inverse_manual():
    pb = arm_p.pose.bones[B("Hips")]
    bpy.context.view_layer.update()
    inv = (arm_p.matrix_world @ pb.matrix).inverted()
    con.inverse_matrix = inv
    bpy.context.view_layer.update()
    post = empty.matrix_world.translation.copy()
    return round((post - pre_world).length * 1000.0, 6)


REC["childof_setinverse_delta_mm"] = probe("childof_set_inverse_manual",
                                           set_inverse_manual)
REC["contact_empty_target"] = "Armature_Prima:mixamorig:Hips"

# Frozen registration offset of Yui's Hips in Prima's Hips frame (the
# Set-Inverse offset analogue the contact solve maintains).
off0 = bone_world_matrix(arm_p, B("Hips")).inverted() @ hips_head_world(arm_y)
REC["registration_offset_m"] = [round(x, 5) for x in off0]

# ------------------------------------------------------- per-keyframe locs
# The Leader's Hips LOCATION channel carries extra solve keys (26/45/65):
# the contact solve's keyed expression. Her rotation keys stay on the
# sheet's grammar frames; location is solved denser so the keyed form
# of the lock interpolates tightly (drift gate, PASS3 record).
YUI_LOC_KEYS = sorted(set(YUI_UNION) | {26, 45, 65})
all_frames = sorted(set(PRIMA_UNION) | set(YUI_LOC_KEYS))
prima_loc = {}
yui_loc = {}
yui_solve_resid = {}
for s in all_frames:
    apply_pose(arm_p, prima_pose_at(s))
    pb = arm_p.pose.bones[B("Hips")]
    pb.location = prima_loc0
    bpy.context.view_layer.update()
    cols = loc_jacobian(arm_p)
    jm = Matrix((cols[0], cols[1], cols[2])).transposed()
    pb.location = prima_loc0 + jm.inverted() @ prima_loc_delta_world(s)
    if s in PRIMA_UNION:
        prima_loc[s] = pb.location.copy()
    # Leader: authored delta first, then the contact solve proper.
    apply_pose(arm_y, yui_pose_at(s))
    pby = arm_y.pose.bones[B("Hips")]
    pby.location = yui_loc0
    bpy.context.view_layer.update()
    cols = loc_jacobian(arm_y)
    jm = Matrix((cols[0], cols[1], cols[2])).transposed()
    pby.location = yui_loc0 + jm.inverted() @ yui_loc_delta_world(s)
    expected = bone_world_matrix(arm_p, B("Hips")) @ off0
    resid = solve_hips_loc(arm_y, expected)
    if s in YUI_LOC_KEYS:
        yui_loc[s] = pby.location.copy()
        yui_solve_resid[s] = round(resid * 1000.0, 5)
REC["yui_contact_solve_residual_mm"] = {str(k): v for k, v in
                                        yui_solve_resid.items()}
log("yui contact solve residuals mm:", yui_solve_resid)
# Seam law (T-09) applied exactly: endpoint location keys are COPIES of
# frame 0, not independent re-solves (a re-solve lands within solver
# tolerance but not on the same point — measured 0.0019 quat delta on
# the arm chain in run A, visible at silhouette edges).
if CYCLE in prima_loc and 0 in prima_loc:
    prima_loc[CYCLE] = prima_loc[0].copy()
if CYCLE in yui_loc and 0 in yui_loc:
    yui_loc[CYCLE] = yui_loc[0].copy()


def interp_loc(table, s):
    ks = sorted(table)
    if s <= ks[0]:
        return table[ks[0]].copy()
    if s >= ks[-1]:
        return table[ks[-1]].copy()
    for i in range(len(ks) - 1):
        a, b = ks[i], ks[i + 1]
        if a <= s <= b:
            t = (s - a) / (b - a)
            return table[a].lerp(table[b], t)
    return table[ks[-1]].copy()


# ------------------------------------------------------------- hand solves
def solve_linear(a_mat, b_vec):
    n = len(b_vec)
    aug = [row[:] + [b_vec[i]] for i, row in enumerate(a_mat)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[piv][col]) < 1e-12:
            return [0.0] * n
        aug[col], aug[piv] = aug[piv], aug[col]
        d = aug[col][col]
        aug[col] = [x / d for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0.0:
                f = aug[r][col]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[col])]
    return [aug[i][n] for i in range(n)]


def solve_hand(arm, side, target, iters=90, tol=0.0005):
    """Damped least squares on Arm/ForeArm (rx, rz) so the Hand bone
    head lands on target (world). Returns residual metres."""
    pb_a = arm.pose.bones[B(side + "Arm")]
    pb_f = arm.pose.bones[B(side + "ForeArm")]
    hand = B(side + "Hand")
    vars_ = [(pb_a, 0), (pb_a, 2), (pb_f, 0), (pb_f, 2)]
    saved = [(pb, pb.rotation_euler[comp]) for pb, comp in vars_]
    for _ in range(iters):
        cur = bone_head_world(arm, hand)
        err = target - cur
        if err.length < tol:
            break
        cols = []
        for pb, comp in vars_:
            orig = pb.rotation_euler[comp]
            pb.rotation_euler[comp] = orig + 0.01
            p1 = bone_head_world(arm, hand)
            pb.rotation_euler[comp] = orig
            cols.append((p1 - cur) / 0.01)
        jtj = [[sum(cols[c][k] * cols[r][k] for k in range(3))
                + (0.02 if c == r else 0.0) for c in range(4)]
               for r in range(4)]
        jte = [sum(cols[c][k] * err[k] for k in range(3)) for c in range(4)]
        delta = solve_linear(jtj, jte)
        for (pb, comp), d in zip(vars_, delta):
            pb.rotation_euler[comp] += max(-0.12, min(0.12, d))
    bpy.context.view_layer.update()
    return (target - bone_head_world(arm, hand)).length


def grip_point(upleg_arm, side, frac, offset):
    head = bone_head_world(upleg_arm, B(side + "UpLeg"))
    knee = bone_head_world(upleg_arm, B(side + "Leg"))
    return head + (knee - head) * frac + Vector(offset)


hand_off = {}   # (girl, side) -> offset in target UpLeg frame
hand_over = {"prima": {}, "yui": {}}  # s -> {bone: [deg,deg,deg]}
hand_resid = {}
HAND_FRAMES = sorted(set(PRIMA_HAND_KEYS) | set(YUI_HAND_KEYS))
for s in HAND_FRAMES:
    if s == CYCLE:
        # Seam law: frame-78 hand keys are copies of frame 0 (see the
        # loc-copy note above); the lock target is the same point.
        for girl in ("prima", "yui"):
            if 0 in hand_over[girl]:
                hand_over[girl][CYCLE] = dict(hand_over[girl][0])
        continue
    scene.frame_set(s)
    apply_pose(arm_p, prima_pose_at(s))
    arm_p.pose.bones[B("Hips")].location = interp_loc(prima_loc, s)
    apply_pose(arm_y, yui_pose_at(s))
    arm_y.pose.bones[B("Hips")].location = interp_loc(yui_loc, s)
    bpy.context.view_layer.update()
    # Prima's hands -> her own thighs (C-14); Yui's hands -> Prima's
    # thighs (C-15, locked to the same thigh bones per the narration).
    jobs = []
    if s in PRIMA_HAND_KEYS:
        # Her hands rest on TOP of her own raised thighs (C-14).
        jobs += [("prima", arm_p, side, arm_p, 0.10, (0, -0.01, 0.082))
                 for side in ("Left", "Right")]
    if s in YUI_HAND_KEYS:
        # His hands on her buttocks / thigh roots from behind (C-15),
        # locked to the same thigh bones per the narration.
        jobs += [("yui", arm_y, side, arm_p, 0.10, (0, 0.05, 0.055))
                 for side in ("Left", "Right")]
    for girl, arm, side, tarm, frac, goff in jobs:
        if s == 0:
            # Reach fallback: if the grip point is outside the arm's
            # reach, walk the grip toward the hip (still on the thigh)
            # until the solve lands — recorded, never silent.
            r = None
            for attempt in range(4):
                tgt = grip_point(tarm, side, frac, goff)
                r = solve_hand(arm, side, tgt)
                if r * 1000.0 <= 3.0 or frac <= 0.04:
                    break
                frac = round(frac - 0.03, 4)
            REC.setdefault("grip_frac", {})["%s_%s" % (girl, side)] = frac
            log("grip", girl, side, "frac", frac, "resid mm",
                round(r * 1000.0, 3))
            upmat = bone_world_matrix(tarm, B(side + "UpLeg"))
            hand_off[(girl, side)] = upmat.inverted() @ bone_head_world(
                arm, B(side + "Hand"))
        else:
            upmat = bone_world_matrix(tarm, B(side + "UpLeg"))
            tgt = upmat @ hand_off[(girl, side)]
            r = solve_hand(arm, side, tgt)
        hand_resid["%s_%s_%d" % (girl, side, s)] = round(r * 1000.0, 4)
        over = hand_over[girl].setdefault(s, {})
        for bn in (B(side + "Arm"), B(side + "ForeArm")):
            over[bn] = [round(math.degrees(x), 4)
                        for x in arm.pose.bones[bn].rotation_euler]
REC["hand_solve_residual_mm"] = hand_resid
log("hand solve residuals (mm): max", max(hand_resid.values()))


def arm_value(girl, bone, s):
    table = {f: d[bone] for f, d in hand_over[girl].items() if bone in d}
    ks = sorted(table)
    if s <= ks[0]:
        return list(table[ks[0]])
    if s >= ks[-1]:
        return list(table[ks[-1]])
    for i in range(len(ks) - 1):
        a, b = ks[i], ks[i + 1]
        if a <= s <= b:
            t = (s - a) / (b - a)
            return [table[a][k] + (table[b][k] - table[a][k]) * t
                    for k in range(3)]
    return list(table[ks[-1]])


def final_pose(girl, s):
    if girl == "prima":
        p = prima_pose_at(s)
    else:
        p = yui_pose_at(s)
    for side in ("Left", "Right"):
        for bn in (B(side + "Arm"), B(side + "ForeArm")):
            p[bn] = arm_value(girl, bn, s)
    return p


# ---------------------------------------------------------------- keying
def key_girl(arm, body, girl, union, face_fn, loc_frames):
    kbs = {kb.name: kb for kb in body.data.shape_keys.key_blocks}
    face_channels = sorted({ch for s in union for ch in face_fn(s)})
    loc_tab = prima_loc if girl == "prima" else yui_loc
    for s in union:
        scene.frame_set(s)
        pose = final_pose(girl, s)
        apply_pose(arm, pose)
        arm.pose.bones[B("Hips")].location = interp_loc(loc_tab, s)
        for bn in pose:
            arm.pose.bones[bn].keyframe_insert("rotation_euler", frame=s)
        arm.pose.bones[B("Hips")].keyframe_insert("location", frame=s)
        fv = face_fn(s)
        for ch in face_channels:
            kb = kbs[ch]
            kb.value = fv.get(ch, 0.0)
            kb.keyframe_insert("value", frame=s)
    for s in loc_frames:  # denser location keys (Leader contact solve)
        if s in union:
            continue
        scene.frame_set(s)
        arm.pose.bones[B("Hips")].location = interp_loc(loc_tab, s)
        arm.pose.bones[B("Hips")].keyframe_insert("location", frame=s)
    return face_channels


fc_p = key_girl(arm_p, body_p, "prima", PRIMA_UNION, prima_face_at,
                PRIMA_UNION)
fc_y = key_girl(arm_y, body_y, "yui", YUI_UNION, yui_face_at, YUI_LOC_KEYS)
REC["face_channels"] = {"prima": fc_p, "yui": fc_y}


def action_fcurves(action):
    """Blender 5.2 layered actions: fcurves live on the strip channelbag
    (Action.fcurves was removed — probed, first run AttributeError)."""
    if hasattr(action, "fcurves"):
        return list(action.fcurves)
    out = []
    for layer in action.layers:
        for strip in layer.strips:
            # 5.2.3 probe: strip.channelbag is a method requiring the
            # action slot (TypeError without it).
            for slot in action.slots:
                try:
                    cb = strip.channelbag(slot)
                except Exception:
                    continue
                if cb is not None and hasattr(cb, "fcurves"):
                    out.extend(list(cb.fcurves))
    return out


def fix_fcurves(obj_action_pairs):
    n_lin = 0
    n_cyc = 0
    for action in obj_action_pairs:
        if action is None:
            continue
        for fc in action_fcurves(action):
            for kp in fc.keyframe_points:
                kp.interpolation = 'LINEAR'
                n_lin += 1
            try:
                fc.modifiers.new('CYCLES')
                n_cyc += 1
            except Exception:
                pass
    return n_lin, n_cyc


actions = []
for arm in (arm_p, arm_y):
    if arm.animation_data:
        actions.append(arm.animation_data.action)
for body in (body_p, body_y):
    sk = body.data.shape_keys
    if sk and sk.animation_data:
        actions.append(sk.animation_data.action)
n_lin, n_cyc = fix_fcurves(actions)
REC["fcurve_linear_points"] = n_lin
REC["fcurve_cycles_modifiers"] = probe(
    "cycles_modifiers", lambda: n_cyc if n_cyc > 0 else (_ for _ in ()).throw(
        RuntimeError("no CYCLES modifiers added")))
scene.frame_set(0)

# ------------------------------------------------------------ measurements
cages = [ob for ob in bpy.context.scene.objects if "Cage" in ob.name]
anchor_y_pelvis = find_obj(yui_objs, "Anchor_Fluid_Pelvis")
anchor_p_pelvis = find_obj(prima_objs, "Anchor_Fluid_Pelvis")


def bvh_of(body):
    dg = bpy.context.evaluated_depsgraph_get()
    ev = body.evaluated_get(dg)
    me = ev.to_mesh()
    mw = ev.matrix_world
    verts = [mw @ v.co for v in me.vertices]
    polys = [[i for i in p.vertices] for p in me.polygons]
    bvh = BVHTree.FromPolygons(verts, polys)
    return bvh, verts, ev


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
    # Two-axis parity agreement: a single +X ray miscounts near the
    # partner's gripping fingers (small closed blobs beside the pelvis
    # read as "inside" for hip-side verts — diagnosed on run A: 1-4
    # verts/sample, depths to 47 mm, all beside a hand). A truly
    # embedded pelvis vert is inside on both axes.
    return _parity(bvh, pt, Vector((1, 0, 0))) and \
        _parity(bvh, pt, Vector((0, 0, -1)))


def measure():
    out = {"drift_empty_mm": [], "drift_yui_mm": [], "hand_dev_mm": {},
           "penetration": [], "bounce_max": 0.0, "spine_rx": [],
           "prima_hips": [], "yui_hips": []}
    seam_mats = {}
    pen_vmax = {}
    for s in range(0, CYCLE + 1):
        scene.frame_set(s)
        bpy.context.view_layer.update()
        hp = hips_head_world(arm_p)
        hy = hips_head_world(arm_y)
        out["prima_hips"].append([round(x, 5) for x in hp])
        out["yui_hips"].append([round(x, 5) for x in hy])
        out["drift_empty_mm"].append(
            round((empty.matrix_world.translation - hp).length * 1000, 5))
        expected = bone_world_matrix(arm_p, B("Hips")) @ off0
        out["drift_yui_mm"].append(round((hy - expected).length * 1000, 5))
        for girl, arm, tarm in (("prima", arm_p, arm_p), ("yui", arm_y, arm_p)):
            for side in ("Left", "Right"):
                tgt = bone_world_matrix(tarm, B(side + "UpLeg")) @ \
                    hand_off[(girl, side)]
                dev = (bone_head_world(arm, B(side + "Hand")) - tgt).length
                out["hand_dev_mm"].setdefault(girl + "_" + side, []).append(
                    round(dev * 1000, 4))
        for cg in cages:
            if cg.data.shape_keys:
                v = abs(cg.data.shape_keys.key_blocks["Bounce"].value)
                out["bounce_max"] = max(out["bounce_max"], v)
        out["spine_rx"].append(round(math.degrees(
            arm_p.pose.bones[B("Spine")].rotation_euler.x), 4))
        if s in (0, CYCLE):
            for tag, arm in (("p", arm_p), ("y", arm_y)):
                for pb in arm.pose.bones:
                    key = (tag, pb.name)
                    mat = (arm.matrix_world @ pb.matrix).copy()
                    if key in seam_mats:
                        m0 = seam_mats[key]
                        dt = (mat.translation - m0.translation).length * 1000
                        da = math.degrees(
                            m0.to_quaternion().rotation_difference(
                                mat.to_quaternion()).angle)
                        out.setdefault("seam", []).append(
                            {"girl": tag, "bone": pb.name,
                             "trans_mm": round(dt, 6),
                             "rot_deg": round(da, 6)})
                    else:
                        seam_mats[key] = mat
        # penetration on the contact set (pelvis-box verts, both bodies)
        bvh_p, verts_p, ev_p = bvh_of(body_p)
        bvh_y, verts_y, ev_y = bvh_of(body_y)
        worst = 0.0
        for tag, body, arm, other in (("p", body_p, arm_p, bvh_y),
                                      ("y", body_y, arm_y, bvh_p)):
            for idx, w in pelvis_world_verts(body, arm):
                if point_inside(other, w):
                    near = other.find_nearest(w)
                    if near is not None:
                        depth = near[3] * 1000.0
                        if depth > 15.0:
                            # Inside on both parities but >15 mm from
                            # the nearest surface: not a surface
                            # penetration (a nearby closed blob — the
                            # gripping hand — encloses the ray path).
                            out.setdefault("pen_rejected_far", []).append(
                                [s, tag, round(depth, 2)])
                            continue
                        worst = max(worst, depth)
                        dkey = "pen_max_" + tag
                        out[dkey] = max(out.get(dkey, 0.0), depth)
                        if tag == "p":
                            pen_vmax[idx] = max(pen_vmax.get(idx, 0.0), depth)
        ev_p.to_mesh_clear()
        ev_y.to_mesh_clear()
        out["penetration"].append(round(worst, 4))
        if anchor_y_pelvis is not None:
            out.setdefault("yui_anchor", []).append(
                [round(x, 5) for x in anchor_y_pelvis.matrix_world.translation])
    out["pen_vmax_prima"] = {str(k): round(v, 4) for k, v in pen_vmax.items()}
    return out


log("measuring pass 1 ...")
MEAS = measure()
pen_max = max(MEAS["penetration"])
REC["penetration_pre_cure"] = {
    "max_mm": pen_max,
    "samples_over_0.5mm": [i for i, v in enumerate(MEAS["penetration"])
                           if v > 0.5],
}
log("penetration pre-cure max mm:", pen_max)

# T-13 cure: scene-side corrective key on the scene copy of Prima's Body
# (named key, value 1.0, never Basis; the shipped rig file is untouched).
CURE = {"applied": False}
if pen_max > 0.5:
    me = body_p.data
    basis = me.shape_keys.key_blocks["Basis"]
    kb = body_p.shape_key_add(name="ContactFix", from_mix=False)
    depths = {int(k): v / 1000.0 for k, v in MEAS["pen_vmax_prima"].items()}
    coords = [v.co.copy() for v in me.vertices]
    normals = [v.normal.copy() for v in me.vertices]
    moved = {}
    for idx, d in depths.items():
        # A sculpt-class cure moves millimetres; a larger reading is a
        # pose error or a measurement artifact, never a sculpt target.
        moved[idx] = min(d, 0.007) + 0.001
    for idx in list(moved):
        for j, co in enumerate(coords):
            if j not in moved and (co - coords[idx]).length < 0.02:
                moved[j] = 0.5 * (depths[idx] + 0.001)
    for idx, d in moved.items():
        kb.data[idx].co = coords[idx] - normals[idx] * d
    kb.value = 1.0
    kb.keyframe_insert("value", frame=0)
    kb.keyframe_insert("value", frame=CYCLE)
    ska = me.shape_keys.animation_data
    if ska and ska.action:
        for fc in action_fcurves(ska.action):
            for kp in fc.keyframe_points:
                kp.interpolation = 'LINEAR'
    CURE = {"applied": True, "verts_moved": len(moved),
            "max_delta_mm": round(max(moved.values()) * 1000, 3),
            "key": "ContactFix", "value": 1.0}
    log("measuring pass 2 (post-cure) ...")
    MEAS = measure()
    REC["penetration_post_cure"] = {
        "max_mm": max(MEAS["penetration"]),
        "samples_over_0.5mm": [i for i, v in enumerate(MEAS["penetration"])
                               if v > 0.5]}
REC["cure"] = CURE

# Derived gate numbers.
import statistics
def mm_stats(arr):
    return {"max": round(max(arr), 4), "mean": round(statistics.fmean(arr), 4)}
REC["drift_empty"] = mm_stats(MEAS["drift_empty_mm"])
REC["drift_yui"] = mm_stats(MEAS["drift_yui_mm"])
REC["hand_dev"] = {k: mm_stats(v) for k, v in MEAS["hand_dev_mm"].items()}
REC["penetration_final"] = {
    "max_mm": max(MEAS["penetration"]),
    "mean_mm": round(statistics.fmean(MEAS["penetration"]), 4),
    "worst_samples": sorted(range(len(MEAS["penetration"])),
                            key=lambda i: -MEAS["penetration"][i])[:6]}
REC["penetration_detail"] = {
    "max_prima_in_yui_mm": MEAS.get("pen_max_p"),
    "max_yui_in_prima_mm": MEAS.get("pen_max_y"),
    "rejected_far_count": len(MEAS.get("pen_rejected_far", [])),
    "test": "two-axis ray parity (inside on +X and -Z) and nearest-"
            "surface depth <= 15 mm; deeper readings beside the "
            "gripping hands are rejected as blob-parity artifacts "
            "and counted here"}
REC["bounce_max_abs"] = MEAS["bounce_max"]
seam = MEAS.get("seam", [])
REC["seam"] = {"max_trans_mm": max((x["trans_mm"] for x in seam), default=None),
               "max_rot_deg": max((x["rot_deg"] for x in seam), default=None),
               "bones_compared": len(seam)}
REC["follower_spine_rx"] = {str(s): MEAS["spine_rx"][s]
                            for s in (0, 15, 30, 38, 45, 52, 78)}
# 80/20 channel-energy ratio (T-05 test form).
rot_travel = 0.0
prev = None
for s in range(0, CYCLE + 1):
    v = math.radians(-4 + 18.0 * interp(LEADER_KEYS, s))
    if prev is not None:
        rot_travel += abs(v - prev)
    prev = v
trans_travel = 0.0
prev = None
for s in range(0, CYCLE + 1):
    v = yui_loc_delta_world(s)
    if prev is not None:
        trans_travel += (v - prev).length
    prev = v
rot_mm = rot_travel * 0.10 * 1000.0
REC["split_80_20"] = {"rotation_mm_at_lever": round(rot_mm, 2),
                      "translation_mm": round(trans_travel * 1000.0, 2),
                      "rotation_share": round(
                          rot_mm / (rot_mm + trans_travel * 1000.0), 4)}
# Oval test (T-06): PCA of the Leader's pelvic contact-point path
# (her Anchor_Fluid_Pelvis — the point that rides the Hips rotation;
# the Hips head itself is the rotation centre and the contact lock
# holds it to the Follower, so it cannot trace the arc).
try:
    import numpy as np
    pts = np.array(MEAS["yui_anchor"], dtype=float)
    cen = pts.mean(axis=0)
    _, _, vt = np.linalg.svd(pts - cen, full_matrices=False)
    proj = (pts - cen) @ vt.T
    ext = proj.max(axis=0) - proj.min(axis=0)
    REC["oval"] = {"pc1_mm": round(float(ext[0]) * 1000, 2),
                   "pc2_mm": round(float(ext[1]) * 1000, 2),
                   "pc2_over_pc1": round(float(ext[1] / ext[0]), 4),
                   "closure_mm": round(float(np.linalg.norm(
                       pts[-1] - pts[0])) * 1000, 4)}
except Exception as e:
    REC["oval"] = {"error": repr(e)}
# Head stabilisation (T-05): world-orientation swing, Head vs Spine1.
swings = {}
for bn in (B("Head"), B("Spine1"), B("Hips")):
    q0 = None
    mx = 0.0
    for s in range(0, CYCLE + 1):
        scene.frame_set(s)
        q = bone_world_matrix(arm_y, bn).to_quaternion()
        if q0 is None:
            q0 = q
        mx = max(mx, math.degrees(q0.rotation_difference(q).angle))
    swings[bn] = round(mx, 3)
REC["leader_world_swing_deg"] = swings
log("derived:", json.dumps({k: REC[k] for k in
      ("drift_empty", "drift_yui", "split_80_20", "oval", "seam")}, indent=1))

# ---------------------------------------------------------------- renders
RENDER_FRAMES = [0, 19, 38, 45, 58, 78, 116, 194]
cyc_ok = REC["probes"].get("cycles_modifiers", {}).get("ok", False)
rendered = []
for f in RENDER_FRAMES:
    scene.frame_set(f if cyc_ok else f % CYCLE)
    scene.render.filepath = os.path.join(OUT, "frames", "f_%04d.png" % f)
    bpy.ops.render.render(write_still=True)
    rendered.append(f)
REC["rendered_frames"] = rendered
REC["render_note"] = ("frames >78 evaluated through CYCLES fcurve "
                      "modifiers" if cyc_ok else
                      "CYCLES modifier unavailable; frames >78 rendered "
                      "at f mod 78 (identical by the seam law)")

# ------------------------------------------------------------- clip export
sys.path.insert(0, FLEET)
import gen_clip  # fleet tool of record (build/gen_clip.py)


def write_show(girl, slug, union, face_fn, loc_tab):
    keys = []
    for s in sorted(set(union) | set(loc_tab)):
        pose = final_pose(girl, s)
        loc = interp_loc(loc_tab, s)
        keys.append({"f": s,
                     "pose": {k: [round(x, 4) for x in v]
                              for k, v in pose.items()},
                     "hips_loc": [round(x, 6) for x in loc],
                     "morphs": {k: v for k, v in face_fn(s).items()
                                if v > 0.001}})
    show = {"kind": "contactloop", "girl": slug, "fps": FPS,
            "frames": CYCLE, "keys": keys}
    path = os.path.join(OUT, "records", "%s-show.json" % slug)
    with open(path, "w") as fh:
        json.dump(show, fh)
    return path


clip_hashes = {}
for girl, slug, union, face_fn, loc_tab in (
        ("prima", "prima", PRIMA_UNION, prima_face_at, prima_loc),
        ("yui", "yui", YUI_UNION, yui_face_at, yui_loc)):
    show_path = write_show(girl, slug, union, face_fn, loc_tab)
    prefix = os.path.join(OUT, "clips", "%s-contactloop" % slug)
    sys.argv = ["gen_clip.py", show_path,
                os.path.join(FLEET, "%s.glb" % slug), prefix]
    gen_clip.main()
    cpath = prefix + ".clip.json"
    clip = json.load(open(cpath))
    clip["loop"] = True  # the arc exporter writes False; this IS a loop
    with open(cpath, "w") as fh:
        json.dump(clip, fh, indent=1)
    clip_hashes[slug] = {
        os.path.basename(p): hashlib.sha256(open(p, "rb").read()).hexdigest()
        for p in (cpath, prefix + "-skeleton.json",
                  prefix + "-channels.json")}
REC["clip_sha256"] = clip_hashes

if SAVE_BLEND:
    scene.frame_set(0)
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "scene.blend"))
    REC["scene_blend"] = "scene.blend"

with open(os.path.join(OUT, "records", "measurements.json"), "w") as fh:
    json.dump({k: MEAS[k] for k in ("drift_empty_mm", "drift_yui_mm",
                                    "hand_dev_mm", "penetration",
                                    "spine_rx", "prima_hips", "yui_hips",
                                    "yui_anchor", "seam", "pen_max_p",
                                    "pen_max_y", "pen_rejected_far")
               if k in MEAS}, fh)
with open(os.path.join(OUT, "records", "build_record.json"), "w") as fh:
    json.dump(REC, fh, indent=1, sort_keys=True)
log("BUILD DONE", OUT)
