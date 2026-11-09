# Plan 36 Pass 3 rebuild: Mala-class articulated worn prop on a COPY of
# Prima's conformed rig. Registration = the video's method as translated:
#   (i) internal: child nodes parented under a prop root (hierarchy);
#   (ii) body-side: prop root registered to the chest bone, measured in
#        Form A (Child Of constraint, manual inverse) and
#        Form B (keyed at the clip's own 15-frame density, LINEAR).
# Animation: a 120-frame max-motion window of the estate prima-arc clip.
# Usage: blender -b prima-fleet-copy.blend -Y --python build_prop.py -- <workdir> <runname>
import bpy, json, math, os, sys
from mathutils import Vector, Quaternion, Matrix

argv = sys.argv[sys.argv.index("--") + 1:]
WORK, RUN = argv[0], argv[1]
os.makedirs(os.path.join(WORK, RUN), exist_ok=True)
rec = {"run": RUN, "blender": bpy.app.version_string}

# ---------- clip ----------
clip = json.load(open(os.path.join(WORK, "prima.clip.json")))
rec["clip"] = {"id": clip["id"], "frames": clip["frames"],
               "skeleton": clip["skeleton"]}
body = [g for g in clip["groups"] if g["kind"] == "body"][0]

def track_keys(track, chan):
    ks = sorted(track[chan], key=lambda k: k["frame"])
    return [(k["frame"], k["value"]) for k in ks]

def sample(keys, f, is_quat):
    if f <= keys[0][0]:
        v = keys[0][1]
        return Quaternion((v[3], v[0], v[1], v[2])) if is_quat else Vector(v)
    if f >= keys[-1][0]:
        v = keys[-1][1]
        return Quaternion((v[3], v[0], v[1], v[2])) if is_quat else Vector(v)
    for i in range(len(keys) - 1):
        f0, v0 = keys[i]; f1, v1 = keys[i + 1]
        if f0 <= f <= f1:
            t = 0.0 if f1 == f0 else (f - f0) / (f1 - f0)
            if is_quat:
                q0 = Quaternion((v0[3], v0[0], v0[1], v0[2]))
                q1 = Quaternion((v1[3], v1[0], v1[1], v1[2]))
                return q0.slerp(q1, t)
            return Vector(v0).lerp(Vector(v1), t)
    raise RuntimeError("sample fallthrough")

tracks = {}
for t in body["tracks"]:
    e = {}
    if "rotation" in t: e["rotation"] = track_keys(t, "rotation")
    if "translation" in t: e["translation"] = track_keys(t, "translation")
    tracks[t["bone"]] = e

# max-motion 120-frame window by Spine1 angular travel (ties -> earliest)
spine = tracks["mixamorig_Spine1"]["rotation"]
best, best_travel = 0, -1.0
for start in range(0, clip["frames"] - 120 + 1, 15):
    travel, prev = 0.0, None
    for f in range(start, start + 121):
        q = sample(spine, f, True)
        if prev is not None:
            travel += 2.0 * math.acos(min(1.0, abs(prev.dot(q))))
        prev = q
    if travel > best_travel + 1e-9:
        best, best_travel = start, travel
W0, W1 = best, best + 120
rec["window"] = {"start": W0, "end": W1,
                 "spine1_travel_rad": round(best_travel, 6)}

# ---------- rig ----------
arm = next(o for o in bpy.data.objects if o.type == "ARMATURE")
rec["armature"] = arm.name
bone_names = [b.name for b in arm.data.bones]
rec["bone_count"] = len(bone_names)
def rig_name(clip_name):
    if clip_name in bone_names: return clip_name
    alt = clip_name.replace("mixamorig_", "mixamorig:")
    if alt in bone_names: return alt
    return None
name_map = {cn: rig_name(cn) for cn in tracks}
missing = [cn for cn, rn in name_map.items() if rn is None]
rec["bones_missing"] = missing
CHEST = rig_name("mixamorig_Spine2") or rig_name("mixamorig_Spine1")
rec["chest_bone"] = CHEST

def apply_clip(f):
    for cn, e in tracks.items():
        rn = name_map[cn]
        if rn is None: continue
        pb = arm.pose.bones[rn]
        pb.rotation_mode = "QUATERNION"
        if "rotation" in e:
            pb.rotation_quaternion = sample(e["rotation"], f, True)
        if "translation" in e:
            pb.location = sample(e["translation"], f, False)
    bpy.context.view_layer.update()

# ---------- prop build (Mala-class, minimal, deterministic) ----------
scene = bpy.context.scene
scene.render.fps = 60
# anchor offset in chest-bone space: computed in the Form A section from a
# WORLD-space sternum target (fleet convention: front = -Y world), because
# mixamorig bone-space axes do not align with world axes. Attempt-3 fix:
# the constant bone-space offset (0,-0.055,0.10) landed behind the torso.
OFFSET_LOCAL = None  # set below, before first use

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.select_all(action="DESELECT")

root = bpy.data.objects.new("MalaPropRoot", None)
scene.collection.objects.link(root)
root.empty_display_type = "PLAIN_AXES"
root.empty_display_size = 0.05

# prop armature: root + 3 segment bones hanging -Z, slight forward curl
pdata = bpy.data.armatures.new("MalaPropArmature")
prop = bpy.data.objects.new("MalaProp", pdata)
scene.collection.objects.link(prop)
bpy.context.view_layer.objects.active = prop
bpy.ops.object.mode_set(mode="EDIT")
seg_len = 0.045
heads = [(0, 0, 0), (0, 0, -seg_len), (0, 0, -2 * seg_len), (0, 0, -3 * seg_len)]
tails = [(0, 0, -seg_len), (0, 0, -2 * seg_len), (0, 0, -3 * seg_len),
         (0, -0.012, -4 * seg_len)]
names = ["root", "seg1", "seg2", "seg3"]
ebs = []
for i, nm in enumerate(names):
    eb = pdata.edit_bones.new(nm)
    eb.head = heads[i]; eb.tail = tails[i]
    if i: eb.parent = ebs[i - 1]; eb.use_connect = True
    ebs.append(eb)
bpy.ops.object.mode_set(mode="OBJECT")
prop.parent = root  # hierarchy parenting: the video's internal mechanism

# pose the chain (static curl) in pose mode
curls = {"root": 0.0, "seg1": -6.0, "seg2": -9.0, "seg3": -12.0}  # attempt-4: bow FORWARD (-Y, away from the leaning torso); +X curls drove the strand into the garment (probe_pos.py evidence)
for nm, deg in curls.items():
    pb = prop.pose.bones[nm]
    pb.rotation_mode = "XYZ"
    pb.rotation_euler = (math.radians(deg), 0, 0)

# beads: 3 per segment bone, bone-parented; pendant at seg3 tip
bead_mat = bpy.data.materials.new("MalaBead")
bead_mat.diffuse_color = (0.3, 0.19, 0.1, 1.0)
bead_mat.use_nodes = True
bead_mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.3, 0.19, 0.1, 1.0)
beads = []
for bi, nm in enumerate(names):
    bone = pdata.bones[nm]
    for j in range(3):
        bpy.ops.mesh.primitive_uv_sphere_add(
            segments=12, ring_count=8, radius=0.011,
            location=(0, 0, 0))
        b = bpy.context.active_object
        b.name = "Bead_%s_%d" % (nm, j)
        b.data.materials.append(bead_mat)
        b.parent = prop
        b.parent_type = "BONE"
        b.parent_bone = nm
        b.matrix_parent_inverse = bone.matrix_local.inverted()
        frac = (j + 0.5) / 3.0
        b.location = bone.head_local.lerp(bone.tail_local, frac)
        beads.append(b.name)
# NOTE: for BONE parenting Blender places the child at the bone origin with
# matrix_parent_inverse identity by default in scripted assignment; bead
# local locations above are in armature space along the bone.

bpy.ops.mesh.primitive_cone_add(vertices=12, radius1=0.013, radius2=0.0,
                                depth=0.03, location=(0, 0, 0))
pend = bpy.context.active_object
pend.name = "Pendant"
pend.data.materials.append(bead_mat)
pend.parent = prop; pend.parent_type = "BONE"; pend.parent_bone = "seg3"
seg3 = pdata.bones["seg3"]
pend.matrix_parent_inverse = seg3.matrix_local.inverted()
pend.location = seg3.tail_local + Vector((0, 0, -0.015))
pend.rotation_euler = (math.radians(180), 0, 0)

tip = bpy.data.objects.new("RegisterTip", None)
scene.collection.objects.link(tip)
tip.parent = prop; tip.parent_type = "BONE"; tip.parent_bone = "seg3"
tip.matrix_parent_inverse = seg3.matrix_local.inverted()
tip.location = seg3.tail_local + Vector((0, 0, -0.03))

rec["prop_controls"] = {
    "root_transform_channels": 9,
    "prop_bones": names,
    "prop_bone_rotation_channels": 12,
    "bead_objects": len(beads),
    "bead_animator_channels": 0,
    "pendant_animator_channels": 0,
    "total_animator_channels": 21}

# ---------- registration, Form A: Child Of with manual inverse ----------
apply_clip(W0)
bpy.context.view_layer.update()
arm.update_tag()
dg = bpy.context.evaluated_depsgraph_get()
arm_ev = arm.evaluated_get(dg)
bone_mat0 = arm_ev.matrix_world @ arm_ev.pose.bones[CHEST].matrix
sternum_world = bone_mat0.translation + Vector((0.0, -0.16, 0.03))  # attempt-5: worn OVER the garment — at -0.095 the strand hung inside the loose Outfit mesh in the arc pose (prop-only vs full render pair, probe_render*.py)
OFFSET_LOCAL = bone_mat0.inverted() @ sternum_world
rec["offset_local"] = [round(x, 5) for x in OFFSET_LOCAL]
rec["sternum_world"] = [round(x, 5) for x in sternum_world]
anchor0 = bone_mat0 @ OFFSET_LOCAL
root.matrix_world = Matrix.Translation(anchor0)
bpy.context.view_layer.update()
pre = root.matrix_world.copy()
con = root.constraints.new("CHILD_OF")
con.target = arm; con.subtarget = CHEST
con.inverse_matrix = bone_mat0.inverted()
bpy.context.view_layer.update()
dg = bpy.context.evaluated_depsgraph_get()
post = root.evaluated_get(dg).matrix_world
delta_mm = (post.translation - pre.translation).length * 1000.0
rec["set_inverse_delta_mm"] = round(delta_mm, 6)
rec["childof_influence"] = con.influence

# frozen registration: tip offset in anchor-bone frame at W0
def tip_world():
    dg = bpy.context.evaluated_depsgraph_get()
    return tip.evaluated_get(dg).matrix_world.translation.copy()
def bone_frame():
    dg = bpy.context.evaluated_depsgraph_get()
    ae = arm.evaluated_get(dg)
    return ae.matrix_world @ ae.pose.bones[CHEST].matrix
def root_world():
    dg = bpy.context.evaluated_depsgraph_get()
    return root.evaluated_get(dg).matrix_world.translation.copy()

frozen_tip = bone_frame().inverted() @ tip_world()
frozen_tip_in_root = None
tip0 = tip_world()
root_inv0 = root.evaluated_get(bpy.context.evaluated_depsgraph_get()).matrix_world.inverted()
frozen_tip_in_root = root_inv0 @ tip0

def measure(form):
    errs, internal = [], []
    for f in range(W0, W1 + 1):
        apply_clip(f)
        bpy.context.view_layer.update()
        expected = bone_frame() @ frozen_tip
        actual = tip_world()
        errs.append((actual - expected).length * 1000.0)
        dg = bpy.context.evaluated_depsgraph_get()
        rw = root.evaluated_get(dg).matrix_world
        internal.append(((rw @ frozen_tip_in_root) - actual).length * 1000.0)
    def stats(v):
        return {"max_mm": round(max(v), 4), "mean_mm": round(sum(v) / len(v), 4),
                "n": len(v)}
    return {"tip_error": stats(errs), "internal_error": stats(internal),
            "per_frame_mm": [round(x, 4) for x in errs]}

formA = measure("A")
rec["formA_childof"] = formA
print("FORM A", formA["tip_error"], formA["internal_error"])

# evidence camera (for renders after both forms; uses Form B state last)
cam_data = bpy.data.cameras.new("EvidenceCam")
cam = bpy.data.objects.new("EvidenceCam", cam_data)
scene.collection.objects.link(cam)
scene.camera = cam
cam_data.lens = 35
sun_data = bpy.data.lights.new("Sun", "SUN"); sun_data.energy = 3.0
sun = bpy.data.objects.new("Sun", sun_data); scene.collection.objects.link(sun)
sun.rotation_euler = (math.radians(50), 0, math.radians(30))
world = bpy.data.worlds.new("W") if not scene.world else scene.world
scene.world = world; world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.4, 0.4, 0.42, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 0.6
scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x = 960; scene.render.resolution_y = 540
scene.render.image_settings.file_format = "PNG"
rec["render_engine_readback"] = scene.render.engine

def place_cam(f):
    apply_clip(f)
    bpy.context.view_layer.update()
    bf = bone_frame()
    target = bf @ OFFSET_LOCAL
    eye = target + Vector((0.34, -0.72, 0.18))
    cam.matrix_world = Matrix.Translation(eye)
    d = (target - eye).normalized()
    cam.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()

frames_out = []
for label, f in (("start", W0), ("mid", (W0 + W1) // 2), ("end", W1)):
    place_cam(f)
    out = os.path.join(WORK, RUN, "formA_%s.png" % label)
    scene.render.filepath = out
    bpy.ops.render.render(write_still=True)
    frames_out.append(out)

# ---------- Form B: keyed bake at 15-frame density, LINEAR ----------
# capture evaluated root world transforms under the constraint first
worlds = {}
for f in range(W0, W1 + 1):
    apply_clip(f)
    bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    worlds[f] = root.evaluated_get(dg).matrix_world.copy()
root.constraints.remove(con)
if root.animation_data and root.animation_data.action:
    root.animation_data_clear()
key_frames = list(range(W0, W1 + 1, 15))
if key_frames[-1] != W1: key_frames.append(W1)
for f in key_frames:
    root.matrix_world = worlds[f]
    root.keyframe_insert("location", frame=f - W0)
    root.keyframe_insert("rotation_euler", frame=f - W0)
# force LINEAR on the new action
act = root.animation_data.action
slot = root.animation_data.action_slot
chans = act.layers[0].strips[0].channelbag(slot).fcurves
for fc in chans:
    for kp in fc.keyframe_points:
        kp.interpolation = "LINEAR"
rec["formB_key_frames"] = key_frames
# scene frame mapping: clip frame f -> scene frame f - W0
def apply_clip_scene(sf):
    apply_clip(sf + W0)
orig_measure = measure
def measure_B():
    errs, internal = [], []
    for sf in range(0, W1 - W0 + 1):
        apply_clip(W0 + sf)
        scene.frame_set(sf)
        bpy.context.view_layer.update()
        expected = bone_frame() @ frozen_tip
        actual = tip_world()
        errs.append((actual - expected).length * 1000.0)
        dg = bpy.context.evaluated_depsgraph_get()
        rw = root.evaluated_get(dg).matrix_world
        internal.append(((rw @ frozen_tip_in_root) - actual).length * 1000.0)
    def stats(v):
        return {"max_mm": round(max(v), 4), "mean_mm": round(sum(v) / len(v), 4),
                "n": len(v)}
    return {"tip_error": stats(errs), "internal_error": stats(internal),
            "per_frame_mm": [round(x, 4) for x in errs]}
formB = measure_B()
rec["formB_keyed"] = formB
print("FORM B", formB["tip_error"], formB["internal_error"])

for label, sf in (("start", 0), ("mid", (W1 - W0) // 2), ("end", W1 - W0)):
    apply_clip(W0 + sf)
    scene.frame_set(sf)
    place_cam(W0 + sf)
    scene.frame_set(sf)
    out = os.path.join(WORK, RUN, "formB_%s.png" % label)
    scene.render.filepath = out
    bpy.ops.render.render(write_still=True)
    frames_out.append(out)

bpy.ops.wm.save_as_mainfile(filepath=os.path.join(WORK, RUN, "scene.blend"))
rec["frames"] = frames_out
with open(os.path.join(WORK, RUN, "build_record.json"), "w") as fh:
    json.dump(rec, fh, indent=1, sort_keys=True)
print("BUILD DONE", RUN, json.dumps(rec["formA_childof"]["tip_error"]),
      json.dumps(rec["formB_keyed"]["tip_error"]))
