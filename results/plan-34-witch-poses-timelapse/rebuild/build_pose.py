# Plan 34 Pass 3 — controlled posing-order comparison.
# One shared pose-target table; two strict phase orders (T = video's
# distilled order, E = estate order operationalised in INTAKE.md).
# Usage: blender -b -Y --factory-startup --offline-mode -noaudio -t 4
#   --python-exit-code 1 <in.blend> -P build_pose.py --
#   --run T|E --pose 1..4 --stage 1|2 --outdir DIR [--corr corrections.json]
# Stage 1 poses per the run's order up to its read/verify point and
# renders preview(s) (T) or finals (E). Stage 2 finishes the order,
# applies agent-read corrections (JSON deltas), renders finals.
import bpy, json, sys, time, math, os

argv = sys.argv[sys.argv.index("--") + 1:]
def arg(k, d=None):
    return argv[argv.index(k) + 1] if k in argv else d
RUN = arg("--run"); POSE = int(arg("--pose")); STAGE = int(arg("--stage"))
OUTDIR = arg("--outdir"); CORR = arg("--corr")
os.makedirs(OUTDIR, exist_ok=True)

D = math.radians
def E3(x, y, z): return (D(x), D(y), D(z))
FING_L = [f"mixamorig:LeftHand{n}{i}" for n in ("Thumb","Index","Middle","Ring","Pinky") for i in (1,2,3)]
FING_R = [f"mixamorig:RightHand{n}{i}" for n in ("Thumb","Index","Middle","Ring","Pinky") for i in (1,2,3)]

# ---- shared target table: chain -> {bone: (x,y,z) degrees} + hips_loc ----
POSES = {
 1: {"name": "standing-alert",
  "pelvis": {"mixamorig:Hips": E3(2,0,-3)}, "hips_loc": (0.01,0,0),
  "legs": {"mixamorig:LeftUpLeg": E3(-4,0,2), "mixamorig:RightUpLeg": E3(-8,0,-3),
           "mixamorig:LeftLeg": E3(4,0,0), "mixamorig:RightLeg": E3(6,0,0)},
  "feet": {"mixamorig:LeftFoot": E3(2,0,0), "mixamorig:RightFoot": E3(4,0,0)},
  "spine": {"mixamorig:Spine": E3(3,0,3), "mixamorig:Spine1": E3(2,0,2), "mixamorig:Spine2": E3(0,0,4)},
  "head": {"mixamorig:Neck": E3(0,0,-8), "mixamorig:Head": E3(-4,0,-14)},
  "arms": {"mixamorig:LeftShoulder": E3(0,0,6), "mixamorig:LeftArm": E3(-12,0,10), "mixamorig:LeftForeArm": E3(-18,0,0),
           "mixamorig:RightShoulder": E3(0,0,-6), "mixamorig:RightArm": E3(-38,0,-12), "mixamorig:RightForeArm": E3(-30,0,0)},
  "hands_L": 12, "hands_R": 6, "contact_delta": {}},
 2: {"name": "seated-bench",
  "pelvis": {"mixamorig:Hips": E3(6,0,0)}, "hips_loc": (0, 0.02, -0.52),
  "legs": {"mixamorig:LeftUpLeg": E3(-88,0,6), "mixamorig:RightUpLeg": E3(-84,0,-8),
           "mixamorig:LeftLeg": E3(82,0,0), "mixamorig:RightLeg": E3(78,0,0)},
  "feet": {"mixamorig:LeftFoot": E3(-6,0,0), "mixamorig:RightFoot": E3(-2,0,4)},
  "spine": {"mixamorig:Spine": E3(4,0,0), "mixamorig:Spine1": E3(3,0,2), "mixamorig:Spine2": E3(2,0,2)},
  "head": {"mixamorig:Neck": E3(2,0,6), "mixamorig:Head": E3(0,0,10)},
  "arms": {"mixamorig:LeftShoulder": E3(0,0,4), "mixamorig:LeftArm": E3(-30,0,14), "mixamorig:LeftForeArm": E3(-12,0,0),
           "mixamorig:RightShoulder": E3(0,0,-4), "mixamorig:RightArm": E3(-24,0,-16), "mixamorig:RightForeArm": E3(-8,0,0)},
  "hands_L": 18, "hands_R": 18,
  "contact_delta": {"mixamorig:LeftForeArm": E3(-6,0,0), "mixamorig:LeftHand": E3(-4,0,0)}},
 3: {"name": "reaching",
  "pelvis": {"mixamorig:Hips": E3(0,0,4)}, "hips_loc": (-0.01,0,0),
  "legs": {"mixamorig:LeftUpLeg": E3(-10,0,4), "mixamorig:RightUpLeg": E3(6,0,-4),
           "mixamorig:LeftLeg": E3(8,0,0), "mixamorig:RightLeg": E3(4,0,0)},
  "feet": {"mixamorig:LeftFoot": E3(6,0,0), "mixamorig:RightFoot": E3(-8,0,0)},
  "spine": {"mixamorig:Spine": E3(6,0,-4), "mixamorig:Spine1": E3(6,0,-4), "mixamorig:Spine2": E3(4,0,-2)},
  "head": {"mixamorig:Neck": E3(-6,0,-10), "mixamorig:Head": E3(-8,0,-12)},
  "arms": {"mixamorig:LeftShoulder": E3(0,0,6), "mixamorig:LeftArm": E3(-16,0,18), "mixamorig:LeftForeArm": E3(-24,0,0),
           "mixamorig:RightShoulder": E3(0,0,-6), "mixamorig:RightArm": E3(-150,0,-10), "mixamorig:RightForeArm": E3(-12,0,0)},
  "hands_L": 10, "hands_R": 2,
  "contact_delta": {"mixamorig:LeftForeArm": E3(-6,0,0)}},
 4: {"name": "contrapposto-rest",
  "pelvis": {"mixamorig:Hips": E3(0,0,7)}, "hips_loc": (0.03,0,-0.01),
  "legs": {"mixamorig:LeftUpLeg": E3(-2,0,3), "mixamorig:RightUpLeg": E3(-16,0,-6),
           "mixamorig:LeftLeg": E3(2,0,0), "mixamorig:RightLeg": E3(22,0,0)},
  "feet": {"mixamorig:LeftFoot": E3(0,0,-3), "mixamorig:RightFoot": E3(10,0,0)},
  "spine": {"mixamorig:Spine": E3(2,0,-5), "mixamorig:Spine1": E3(2,0,-3), "mixamorig:Spine2": E3(0,0,-2)},
  "head": {"mixamorig:Neck": E3(0,0,4), "mixamorig:Head": E3(-2,0,6)},
  "arms": {"mixamorig:LeftShoulder": E3(0,0,6), "mixamorig:LeftArm": E3(-14,0,8), "mixamorig:LeftForeArm": E3(-52,0,0),
           "mixamorig:RightShoulder": E3(0,0,-4), "mixamorig:RightArm": E3(-8,0,-10), "mixamorig:RightForeArm": E3(-10,0,0)},
  "hands_L": 26, "hands_R": 14,
  "contact_delta": {"mixamorig:LeftArm": E3(0,0,4), "mixamorig:LeftForeArm": E3(-8,0,0)}},
}
SETTLE = {"mixamorig:Spine2": E3(1,0,0), "mixamorig:Head": E3(1,0,0)}  # secondary micro-settle, both runs

arm_obj = next(o for o in bpy.data.objects if o.type == "ARMATURE")
bpy.context.view_layer.objects.active = arm_obj
bpy.ops.object.mode_set(mode="POSE")
PB = arm_obj.pose.bones
log = {"run": RUN, "pose": POSE, "pose_name": POSES[POSE]["name"], "stage": STAGE, "steps": []}
seen = {}
def note_retouch(bone):
    seen[bone] = seen.get(bone, 0) + 1
def apply_chain(phase, table):
    t0 = time.perf_counter(); bones = []
    for b, rot in table.items():
        PB[b].rotation_mode = "XYZ"; PB[b].rotation_euler = rot; bones.append(b); note_retouch(b)
    log["steps"].append({"phase": phase, "bones": bones, "wall_s": round(time.perf_counter() - t0, 4)})
def apply_hands(phase, pose, include_contact):
    t0 = time.perf_counter(); bones = []
    for b in FING_L:
        PB[b].rotation_mode = "XYZ"; PB[b].rotation_euler = E3(pose["hands_L"], 0, 0); bones.append(b); note_retouch(b)
    for b in FING_R:
        PB[b].rotation_mode = "XYZ"; PB[b].rotation_euler = E3(pose["hands_R"], 0, 0); bones.append(b); note_retouch(b)
    for b in ("mixamorig:LeftHand", "mixamorig:RightHand"):
        PB[b].rotation_mode = "XYZ"; bones.append(b); note_retouch(b)
    log["steps"].append({"phase": phase, "bones": bones, "wall_s": round(time.perf_counter() - t0, 4)})
    if include_contact and pose["contact_delta"]:
        apply_delta("contact", pose["contact_delta"])
def apply_delta(phase, table):
    t0 = time.perf_counter(); bones = []
    for b, d in table.items():
        cur = PB[b].rotation_euler
        PB[b].rotation_euler = (cur[0] + d[0], cur[1] + d[1], cur[2] + d[2]); bones.append(b); note_retouch(b)
    log["steps"].append({"phase": phase, "bones": bones, "wall_s": round(time.perf_counter() - t0, 4)})
def apply_pelvis(pose):
    apply_chain("pelvis", pose["pelvis"])
    PB["mixamorig:Hips"].location = pose["hips_loc"]

def setup_scene():
    # bench for seated pose (both runs, scene setup)
    if POSE == 2 and "NS34_Bench" not in bpy.data.objects:
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.10, 0.225))
        b = bpy.context.active_object; b.name = "NS34_Bench"; b.dimensions = (0.95, 0.50, 0.45)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    # floor
    if "NS34_Floor" not in bpy.data.objects:
        bpy.ops.mesh.primitive_plane_add(size=8, location=(0, 0, 0))
        bpy.context.active_object.name = "NS34_Floor"
    # camera (Plan 02 template position, probe scale)
    cam_data = bpy.data.cameras.new("NS34_Cam"); cam_data.lens = 35.0
    cam = bpy.data.objects.new("NS34_Cam", cam_data)
    bpy.context.collection.objects.link(cam)
    cam.location = (0.8, -2.1, 1.42)
    import mathutils
    tgt = mathutils.Vector((0, 0, 1.02)); d = tgt - mathutils.Vector(cam.location)
    cam.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    bpy.context.scene.camera = cam
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_WORKBENCH"
    sc.display.shading.light = "STUDIO"
    sc.display.shading.color_type = "MATERIAL"
    sc.render.resolution_x = 540; sc.render.resolution_y = 960
    sc.render.filepath = os.path.join(OUTDIR, f"run{RUN}-pose{POSE}.png")

def render(path, res=None):
    sc = bpy.context.scene
    if res: sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.filepath = path
    t0 = time.perf_counter(); bpy.ops.render.render(write_still=True)
    return round(time.perf_counter() - t0, 2)

def hand_probe():
    # numeric hand registration: world distance L hand -> L hip area target
    bpy.context.view_layer.update()
    hw = arm_obj.matrix_world @ PB["mixamorig:LeftHand"].matrix.translation if False else None
    import mathutils
    def wpos(bone):
        return arm_obj.matrix_world @ PB[bone].head
    d = (wpos("mixamorig:LeftHand") - wpos("mixamorig:Hips")).length
    return round(float(d), 4)

pose = POSES[POSE]
setup_scene()
if RUN == "T":
    if STAGE == 1:
        log["steps"].append({"phase": "context", "bones": [], "wall_s": 0.0,
                             "note": "reference pinned; bench/prop placed (setup verified)"})
        apply_chain("legs", pose["legs"]); apply_pelvis(pose)
        apply_chain("spine", pose["spine"]); apply_chain("head", pose["head"])
        apply_chain("feet", pose["feet"]); apply_chain("arms", pose["arms"])
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUTDIR, f"runT-pose{POSE}-s1.blend"))
        log["preview_front_s"] = render(os.path.join(OUTDIR, f"runT-pose{POSE}-preview.png"), res=(360, 640))
        cam = bpy.context.scene.camera; old = tuple(cam.location)
        cam.location = (2.3, -0.6, 1.30)
        import mathutils
        d = mathutils.Vector((0, 0, 0.95)) - mathutils.Vector(cam.location)
        cam.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
        log["preview_side_s"] = render(os.path.join(OUTDIR, f"runT-pose{POSE}-preview-side.png"), res=(360, 640))
        cam.location = old
    else:
        apply_hands("hands", pose, include_contact=False)
        if pose["contact_delta"]: apply_delta("contact", pose["contact_delta"])
        apply_delta("secondary-settle", SETTLE)
        if CORR and os.path.exists(CORR):
            corr = json.load(open(CORR))
            for ph, tbl in corr.get("deltas", {}).items():
                apply_delta("correction:" + ph, {b: E3(*v) for b, v in tbl.items()})
            log["corrections_applied"] = corr.get("deltas", {})
            if corr.get("hips_loc_delta"):
                hl = PB["mixamorig:Hips"].location
                PB["mixamorig:Hips"].location = (hl[0] + corr["hips_loc_delta"][0], hl[1] + corr["hips_loc_delta"][1], hl[2] + corr["hips_loc_delta"][2])
                log["corrections_applied"]["hips_loc_delta"] = corr["hips_loc_delta"]
        log["hand_hip_dist_m"] = hand_probe()
        log["final_render_s"] = render(os.path.join(OUTDIR, f"runT-pose{POSE}.png"), res=(540, 960))
else:  # E
    if STAGE == 1:
        apply_pelvis(pose)
        legs_all = dict(pose["legs"]); legs_all.update(pose["feet"])
        apply_chain("legs+feet", legs_all)
        apply_chain("spine", pose["spine"]); apply_chain("head", pose["head"])
        apply_chain("arms", pose["arms"])
        apply_hands("hands", pose, include_contact=True)
        apply_delta("secondary-settle", SETTLE)
        # ambient/expression: first blink/smile-like shape key if present
        amb = "none-found"
        for ob in bpy.data.objects:
            if ob.type == "MESH" and ob.data.shape_keys:
                for kb in ob.data.shape_keys.key_blocks:
                    if any(w in kb.name.lower() for w in ("blink", "smile", "happy")):
                        kb.value = 0.35; amb = f"{ob.name}:{kb.name}=0.35"; break
            if amb != "none-found": break
        log["steps"].append({"phase": "ambient-expression", "bones": [], "wall_s": 0.0, "note": amb})
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUTDIR, f"runE-pose{POSE}-s1.blend"))
        log["hand_hip_dist_m"] = hand_probe()
        log["final_render_s"] = render(os.path.join(OUTDIR, f"runE-pose{POSE}.png"), res=(540, 960))
    else:
        if CORR and os.path.exists(CORR):
            corr = json.load(open(CORR))
            for ph, tbl in corr.get("deltas", {}).items():
                apply_delta("correction:" + ph, {b: E3(*v) for b, v in tbl.items()})
            log["corrections_applied"] = corr.get("deltas", {})
            if corr.get("hips_loc_delta"):
                hl = PB["mixamorig:Hips"].location
                PB["mixamorig:Hips"].location = (hl[0] + corr["hips_loc_delta"][0], hl[1] + corr["hips_loc_delta"][1], hl[2] + corr["hips_loc_delta"][2])
                log["corrections_applied"]["hips_loc_delta"] = corr["hips_loc_delta"]
        log["hand_hip_dist_m"] = hand_probe()
        log["final_render_s"] = render(os.path.join(OUTDIR, f"runE-pose{POSE}.png"), res=(540, 960))
log["retouch_bone_instances"] = sum(v - 1 for v in seen.values() if v > 1)
log["bones_touched"] = len(seen)
log["posing_wall_s"] = round(sum(s["wall_s"] for s in log["steps"]), 4)
json.dump(log, open(os.path.join(OUTDIR, f"run{RUN}-pose{POSE}-s{STAGE}-log.json"), "w"), indent=1)
print(f"OK ns34_run{RUN}_pose{POSE}_s{STAGE}")
