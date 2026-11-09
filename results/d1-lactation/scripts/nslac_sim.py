# nslac_sim.py - D-1 Stage 2 lactation module build + bake (one clip variant)
# Blender 5.2.3 LTS Mantaflow FLIP, scripted/headless. Spec: MODULE.md.
# Foundations: Plan 07 locked preset + Plan 06 gate/measure discipline.
# Usage: blender -b -Y -noaudio --python nslac_sim.py -- <girl> <m> <mode>
#        <variant> <outdir> <frames_end> [visc_mult] [offset_mm]
# girl in {prima,yui,alma,sloane,lux,piper}; mode in {drip,stream,spray}
import bpy, sys, os, json, time, hashlib, random
from mathutils import Vector

argv = sys.argv[sys.argv.index("--") + 1:]
GIRL, M, MODE, VARIANT, OUTDIR = argv[0], float(argv[1]), argv[2], argv[3], argv[4]
FRAMES_END = int(argv[5])
VISC_MULT = float(argv[6]) if len(argv) > 6 else 1.0
OFFSET_MM = float(argv[7]) if len(argv) > 7 else 18.0
MESH_RAD = float(argv[8]) if len(argv) > 8 else 2.933
DELETE_IN_OBSTACLE = (len(argv) > 9 and argv[9] == "1")
RESOL_ARG = int(argv[10]) if len(argv) > 10 else 120
SEED = 7
random.seed(SEED)
t_start = time.time()
os.makedirs(OUTDIR, exist_ok=True)

FLEET = os.path.expanduser("~/.local/share/pax/nslac/fleet")
SPEC = json.load(open(os.path.join(FLEET, GIRL, GIRL + "_spec.json")))
REC = json.load(open(os.path.join(FLEET, GIRL, "build_record.json")))
ZS, RS = REC["z_scale"], REC["radial_scale"]
CAP = GIRL.capitalize()

MODES = {
    "drip":   {"vel": (0.0, -0.20, -0.30), "vrandom": 0.0,
               "gate": [(6, 9), (18, 21), (30, 33)]},
    "stream": {"vel": (0.0, -2.20, -0.40), "vrandom": 0.0,
               "gate": [(6, 24)]},
    "spray":  {"vel": (0.0, -2.60, -0.35), "vrandom": 0.90,
               "gate": [(6, 24)]},
}
CFG = MODES[MODE]
VEL = Vector(CFG["vel"])
EM_R = 0.016
RESOL = RESOL_ARG
DOM_CENTRE = (0.0, -0.40, 0.72); DOM_DIMS = (0.75, 1.30, 1.50)

bpy.ops.wm.open_mainfile(filepath=os.path.join(FLEET, GIRL, GIRL + ".blend"))
scene = bpy.context.scene
scene.render.fps = 24
scene.frame_start = 1
scene.frame_end = FRAMES_END
scene.unit_settings.system = 'METRIC'

body = None
for ob in scene.objects:
    if ob.type == "MESH" and ob.data.shape_keys and \
            "Fac_Eye_Close" in ob.data.shape_keys.key_blocks:
        body = ob
assert body is not None, "body not found"
BODY_NAME = body.name

# ---- bust parameter: Body_Bust_Size key value = 2(m-1) (fix-step record) --
bust_val = 2.0 * (M - 1.0)
bust_set = {}
for ob in scene.objects:
    if ob.type == "MESH" and ob.data.shape_keys and \
            "Body_Bust_Size" in ob.data.shape_keys.key_blocks:
        ob.data.shape_keys.key_blocks["Body_Bust_Size"].value = bust_val
        bust_set[ob.name] = bust_val
print("NSLAC BUST", bust_set)

# ---- derive nipple points on the evaluated body at m (Standard 6.2 + E-1) -
scene.frame_set(1)
dg = bpy.context.evaluated_depsgraph_get()
ev = body.evaluated_get(dg)
me = ev.to_mesh()
pos = [ev.matrix_world @ v.co for v in me.vertices]
ev.to_mesh_clear()
bust = SPEC["bust"]
mu, sig = bust["z"] * ZS, bust["sigma"] * ZS

def front(pred):
    cand = [p for p in pos if pred(p)]
    return min(cand, key=lambda p: p.y)

derived = {}
for side, sgn in (("L", 1), ("R", -1)):
    p = front(lambda p: abs(p.z - mu) <= sig and sgn * p.x > 0.005 * RS)
    derived[side] = p + Vector((0.0, -0.002, 0.0))
print("NSLAC DERIVED", {k: [round(v, 5) for v in p] for k, p in derived.items()})

stored = {}
for side in ("L", "R"):
    a = bpy.data.objects["Anchor_Fluid_Nipple." + side]
    aev = a.evaluated_get(dg)
    stored[side] = Vector(aev.matrix_world.translation)
anchor_dev_mm = {s: round((derived[s] - stored[s]).length * 1000.0, 3)
                 for s in ("L", "R")}
print("NSLAC ANCHOR_DEV_MM", anchor_dev_mm)

# ---- domain (locked preset values; resolution per MODULE.md S3) ----------
bpy.ops.mesh.primitive_cube_add(size=2.0, location=DOM_CENTRE)
dom = bpy.context.active_object; dom.name = "NSLAC_Domain"
dom.dimensions = DOM_DIMS
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
bpy.ops.object.modifier_add(type='FLUID')
dmod = dom.modifiers[-1]; dmod.fluid_type = 'DOMAIN'
ds = dmod.domain_settings
ds.domain_type = 'LIQUID'; ds.simulation_method = 'FLIP'
ds.resolution_max = RESOL
ds.use_adaptive_timesteps = True; ds.timesteps_min = 1; ds.timesteps_max = 4
ds.cfl_condition = 4.0
ds.use_viscosity = True
ds.viscosity_value = 0.05632 * VISC_MULT   # LOCKED preset x strip mult; value ONLY
ds.surface_tension = 10.0                  # LOCKED preset
ds.flip_ratio = 0.97; ds.particle_radius = 1.43; ds.particle_number = 2
ds.particle_randomness = 0.1
ds.use_mesh = True; ds.mesh_generator = 'IMPROVED'
ds.mesh_particle_radius = MESH_RAD; ds.mesh_smoothen_pos = 1
ds.delete_in_obstacle = DELETE_IN_OBSTACLE
ds.use_speed_vectors = False; ds.use_adaptive_domain = False
ds.cache_directory = os.path.join(OUTDIR, "cache")
ds.cache_frame_start = 1; ds.cache_frame_end = FRAMES_END; ds.cache_type = 'ALL'

def add_fluid(obj):
    for o in bpy.context.selected_objects: o.select_set(False)
    obj.select_set(True); bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_add(type='FLUID')
    return obj.modifiers[-1]

# ---- effectors: body (in-domain collision) + ground plane -----------------
bm = add_fluid(body); bm.fluid_type = 'EFFECTOR'
bes = bm.effector_settings; bes.effector_type = 'COLLISION'; bes.subframes = 2
bpy.ops.mesh.primitive_plane_add(size=4.0, location=(0.0, -0.40, 0.0))
gnd = bpy.context.active_object; gnd.name = "NSLAC_Ground"
gm = add_fluid(gnd); gm.fluid_type = 'EFFECTOR'
gm.effector_settings.effector_type = 'COLLISION'
gmat = bpy.data.materials.new("NSLAC_GroundMat")
gmat.diffuse_color = (0.22, 0.22, 0.25, 1.0)
gnd.data.materials.append(gmat)

# ---- emitters at derived nipple points, offset into open space ------------
direction = VEL.normalized()
emitters = {}
for side in ("L", "R"):
    centre = derived[side] + direction * (OFFSET_MM / 1000.0)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12,
                                         radius=EM_R, location=centre)
    em = bpy.context.active_object; em.name = "NSLAC_Flow_" + side
    fm = add_fluid(em); fm.fluid_type = 'FLOW'
    fs = fm.flow_settings
    fs.flow_type = 'LIQUID'; fs.flow_behavior = 'INFLOW'
    fs.use_initial_velocity = True
    fs.velocity_coord = tuple(VEL)
    fs.velocity_random = CFG["vrandom"]
    # T-19 gate: use_inflow keyed ON exactly over the gate schedule
    keys = [(1, False)]
    for on, off in CFG["gate"]:
        keys += [(on, True), (off, True), (off + 1, False)]
    keys.append((FRAMES_END, False))
    seen = set()
    for f, v in sorted(keys):
        if f in seen or f < 1 or f > FRAMES_END: continue
        seen.add(f)
        fs.use_inflow = v
        fs.keyframe_insert(data_path="use_inflow", frame=f)
    em.hide_render = True
    emitters[side] = {"centre": [round(v, 5) for v in centre],
                      "derived": [round(v, 5) for v in derived[side]],
                      "vel_readback": [round(v, 4) for v in fs.velocity_coord],
                      "vrandom_readback": fs.velocity_random}
print("NSLAC EMITTERS", json.dumps(emitters))

# ---- material, cameras, render hygiene ------------------------------------
fmat = bpy.data.materials.new("NSLAC_FluidMat")
fmat.diffuse_color = (0.96, 0.95, 0.93, 1.0)
fmat.use_nodes = True
bsdf = fmat.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.96, 0.95, 0.93, 1.0)
bsdf.inputs["Roughness"].default_value = 0.35
dom.data.materials.append(fmat)
for ob in scene.objects:
    if ob.name != BODY_NAME and ob.type == "MESH" and \
            ob.name not in ("NSLAC_Domain", "NSLAC_Ground"):
        ob.hide_render = True
    if ob.type == "EMPTY":
        ob.hide_render = True

def look_cam(name, loc, target, lens):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.active_object; cam.name = name
    d = Vector(target) - Vector(loc)
    cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    cam.data.lens = lens
    return cam

bz = mu  # bust centre height at this girl's scale
look_cam("NSCam", (0.35, -2.00, 1.15), (0.0, -0.08, 0.80), 35)
look_cam("NSBustCam", (0.10, -1.05, bz + 0.18), (0.0, -0.13, bz - 0.14), 50)
scene.camera = bpy.data.objects["NSCam"]
bpy.ops.object.light_add(type='SUN', location=(2.0, -3.0, 5.0))
sun = bpy.context.active_object; sun.data.energy = 3.0
scene.render.engine = 'BLENDER_WORKBENCH'
scene.display.shading.light = 'STUDIO'
scene.display.shading.show_shadows = True
scene.display.shading.show_cavity = True
scene.display.shading.cavity_type = 'WORLD'
scene.render.resolution_x = 960; scene.render.resolution_y = 540
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.threads_mode = 'FIXED'; scene.render.threads = 4
scene.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUTDIR, VARIANT + ".blend"))

# ---- bake ------------------------------------------------------------------
t_b0 = time.time()
for o in bpy.context.selected_objects: o.select_set(False)
dom.select_set(True); bpy.context.view_layer.objects.active = dom
r = bpy.ops.fluid.bake_all()
print("NSLAC BAKE_ALL", r)
if 'FINISHED' not in r:
    print("NSLAC BAKE FAILED"); sys.exit(3)
t_b1 = time.time()
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUTDIR, VARIANT + "_baked.blend"))

record = {
    "variant": VARIANT, "girl": GIRL, "m": M, "mode": MODE,
    "blender_version": bpy.app.version_string, "seed": SEED, "fps": 24,
    "frames": [1, FRAMES_END], "resolution_max": RESOL,
    "cell_size_m": DOM_DIMS[2] / RESOL,
    "domain": {"centre": list(DOM_CENTRE), "dims": list(DOM_DIMS)},
    "bust_key_values": bust_set, "body_name": BODY_NAME,
    "derived_nipple": {s: [round(v, 5) for v in derived[s]] for s in ("L", "R")},
    "stored_anchor": {s: [round(v, 5) for v in stored[s]] for s in ("L", "R")},
    "anchor_vs_derived_mm": anchor_dev_mm,
    "emitters": emitters, "gate_schedule": CFG["gate"],
    "velocity_coord": list(VEL), "velocity_random": CFG["vrandom"],
    "emitter_radius_m": EM_R, "emitter_offset_mm": OFFSET_MM,
    "preset_readback": {"viscosity_value": ds.viscosity_value,
        "viscosity_mult": VISC_MULT, "surface_tension": ds.surface_tension,
        "flip_ratio": ds.flip_ratio, "particle_radius": ds.particle_radius,
        "mesh_particle_radius": ds.mesh_particle_radius,
        "delete_in_obstacle": ds.delete_in_obstacle, "mesh_rad_arg": MESH_RAD},
    "effector_readback": {"body_surface_distance": bes.surface_distance,
        "body_subframes": bes.subframes},
    "bake_seconds": round(t_b1 - t_b0, 2),
    "script_sha256": hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
}
with open(os.path.join(OUTDIR, "run_record.json"), "w") as fh:
    json.dump(record, fh, indent=2)
print("NSLAC DONE variant=%s bake_s=%.1f total_s=%.1f"
      % (VARIANT, t_b1 - t_b0, time.time() - t_start))
