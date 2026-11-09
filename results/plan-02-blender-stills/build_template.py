# NS02 "Neon Backdrop" — scripted Blender scene template (Night School Plan 02, Pass 3)
# Clean-room rebuild from TECHNIQUE.md alone. Blender 5.2.3, headless, deterministic.
# Usage:
#   blender -b -Y --factory-startup --offline-mode -noaudio -t <k> --python-exit-code 1 \
#     prima.blend -P build_template.py -- --variant nswfw|sfw --outdir <dir> [--no-render]
# Builds named collections LIGHTING_RIG / CAMERA / BACKDROP / CHARACTER on top of the
# loaded character file (a COPY of Prima's conformed rig; fleet files are never modified),
# writes template-<variant>.blend, a parameters/fingerprint record, and (by default) the
# still render-<variant>.png.
import faulthandler; faulthandler.enable()
import bpy, json, math, sys, colorsys, hashlib
from mathutils import Vector

# ---------------------------------------------------------------- parameters
# Every value traces to TECHNIQUE.md (Pass 2). ESTATE-CHOICE marks fill a
# Pass 1 UNREADABLE and are recorded as choices, not video evidence.
P = {
    # C-02-1 camera-first standing defaults (video evidence)
    "res_x": 1080, "res_y": 1920, "lens_mm": 35.0,
    "camera_loc": (0.8, -2.1, 1.42), "camera_target": (0.0, 0.0, 1.02),
    # Backdrop (C-02-5): procedural neon gradient standing in for the photo
    "backdrop_hue": 0.90,          # dominant neon (pink/magenta) — drives rim
    "backdrop_emission_strength": 0.7,   # ESTATE-CHOICE (UNREADABLE 1)
    "exposure": -1.8,   # ESTATE-CHOICE: video exposure UNREADABLE (its scene
                        # scale differs); set so the evidenced rig reads
    # Pose v3 (degrees, rig convention X=bend / Z=yaw, signs measured by a
    # numeric pose probe on this armature — see PASS3-REBUILD.md). The
    # three-quarter turn is done by the CAMERA (C-02-2), not the model.
    "pose": {
        "mixamorig:Hips": (2, 0, -6), "mixamorig:Spine": (2, 0, 4),
        "mixamorig:Spine1": (1, 0, 3), "mixamorig:Spine2": (1, 0, 2),
        "mixamorig:Neck": (-2, 0, -8), "mixamorig:Head": (-5, 0, -12),
        "mixamorig:LeftArm": (-55, 0, -8), "mixamorig:LeftForeArm": (-78, 0, 0),
        "mixamorig:LeftHand": (15, 0, 0),
        "mixamorig:RightArm": (8, 0, 8), "mixamorig:RightForeArm": (-14, 0, 0),
        "mixamorig:RightHand": (8, 0, 0),
        "mixamorig:LeftUpLeg": (-5, 0, 1), "mixamorig:LeftLeg": (4, 0, 0),
        "mixamorig:LeftFoot": (-2, 0, 0),
        "mixamorig:RightUpLeg": (6, 0, -1), "mixamorig:RightLeg": (3, 0, 0),
        "mixamorig:RightFoot": (2, 0, 0),
    },
    "hips_offset": (0.015, 0.0, -0.008),
    "world_strength": 0.0,               # video evidence
    # Key (C-02-6): Area Rectangle 0.6 x 1 m, ~1000 W, pale blue-white
    "key_energy": 1000.0, "key_size_x": 0.6, "key_size_y": 1.0,
    "key_color": (0.85, 0.92, 1.0), "key_loc": (-2.6, -3.2, 3.0),
    # Rim (C-02-6): Spot 55 deg, blend 0.150, ~1000 W, colour from backdrop hue
    "rim_energy": 1000.0, "rim_spot_deg": 55.0, "rim_blend": 0.150,
    "rim_saturation": 0.932, "rim_loc": (1.6, 1.5, 2.1),
    # Fill (C-02-6): oversized soft Area. Size/power ESTATE-CHOICE (UNREADABLE 2):
    # 4 x 3 m at 200 W — large area, low irradiance, no second shadow direction.
    "fill_energy": 150.0, "fill_size": 4.0, "fill_size_y": 3.0,
    "fill_color": (1.0, 1.0, 1.0), "fill_loc": (0.2, -3.6, 1.7),
    # Accents (C-02-6): Points, white, 5 W, radius 0
    "accent_energy": 5.0,
    "accent_locs": [(-1.1, -1.3, 1.55), (1.15, -1.2, 1.25),
                    (-0.9, 1.1, 1.8), (0.95, 1.05, 0.9)],
    # Skin (C-02-7, Adapt mapping): DAZ dials -> Principled inputs
    "skin_roughness": 0.50,        # Skin Bumps Roughness 0.50 / wet-skin read
    "skin_sss_weight": 0.20,       # SSS intent (dial read 0.01 on its own scale)
    "skin_sss_radius": (1.0, 0.35, 0.20),
    # Render (C-02-8): Cycles adaptive pair; denoise ESTATE-CHOICE (UNREADABLE 3)
    "render_max_samples": 4096, "render_noise_threshold": 0.0100,
    "render_denoise": True, "render_seed": 0,
    "simplify_must_be_off": True,  # C-02-3 pre-render gate
}

def rim_color():
    r, g, b = colorsys.hsv_to_rgb(P["backdrop_hue"], P["rim_saturation"], 1.0)
    return (r, g, b)

def look_at(obj, target):
    d = Vector(target) - obj.location
    obj.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

def aim_light(obj, target=(0.0, 0.0, 1.05)):
    d = Vector(target) - obj.location
    obj.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

def get_collection(name, parent=None):
    c = bpy.data.collections.get(name)
    if c is None:
        c = bpy.data.collections.new(name)
        (parent or bpy.context.scene.collection).children.link(c)
    return c

def move_to(obj, coll):
    for c in obj.users_collection:
        c.objects.unlink(obj)
    coll.objects.link(obj)

def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    args = dict(zip(argv[::2], argv[1::2]))
    variant = args.get("--variant", "nswfw")
    outdir = args.get("--outdir", ".")
    do_render = "--no-render" not in argv
    assert variant in ("nswfw", "sfw"), variant

    scene = bpy.context.scene

    # --- collections -------------------------------------------------------
    root = get_collection("NS02_TEMPLATE")
    col_light = get_collection("LIGHTING_RIG", root)
    col_cam = get_collection("CAMERA", root)
    col_back = get_collection("BACKDROP", root)
    col_char = get_collection("CHARACTER", root)
    for ob in list(bpy.data.objects):
        if ob.name.startswith(("Prima", "Armature")) or ob.type == "EMPTY":
            move_to(ob, col_char)

    # --- backdrop: curved cyclorama with procedural neon emission ---------
    mesh = bpy.data.meshes.new("BackdropMesh")
    W, H, SEGX, SEGZ = 12.0, 5.0, 24, 24
    verts, faces = [], []
    for iz in range(SEGZ + 1):
        v = iz / SEGZ
        # wall rises at y=+1.3; below z=0.55 the surface curves toward camera
        # and the floor reach extends to y=-2.6 at z=0 (v2: no black wedge)
        z = v * H
        y = 1.3 - 3.9 * (max(0.0, (0.55 - z) / 0.55) ** 2) if z < 0.55 else 1.3
        for ix in range(SEGX + 1):
            u = ix / SEGX
            verts.append(((u - 0.5) * W, y, z))
    for iz in range(SEGZ):
        for ix in range(SEGX):
            a = iz * (SEGX + 1) + ix
            faces.append((a, a + 1, a + SEGX + 2, a + SEGX + 1))
    mesh.from_pydata(verts, [], faces); mesh.update()
    backdrop = bpy.data.objects.new("Backdrop", mesh)
    col_back.objects.link(backdrop)

    mat = bpy.data.materials.new("BackdropNeon")
    mat.use_nodes = True
    nt = mat.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    princ = nt.nodes.new("ShaderNodeBsdfPrincipled")
    tex = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.0
    ramp.color_ramp.elements[0].color = (0.004, 0.035, 0.05, 1.0)  # deep teal
    mid = ramp.color_ramp.elements.new(0.55)
    mid.color = (0.008, 0.06, 0.20, 1.0)                           # neon blue
    ramp.color_ramp.elements[1].position = 1.0
    r, g, b = rim_color()
    ramp.color_ramp.elements[1].color = (r * 0.45, g * 0.45, b * 0.45, 1.0)  # pink top
    princ.inputs["Roughness"].default_value = 0.5                  # video: 0.500
    princ.inputs["Emission Strength"].default_value = P["backdrop_emission_strength"]
    nt.links.new(tex.outputs["Generated"], sep.inputs["Vector"])
    nt.links.new(sep.outputs["Z"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], princ.inputs["Base Color"])
    nt.links.new(ramp.outputs["Color"], princ.inputs["Emission Color"])
    nt.links.new(princ.outputs["BSDF"], out.inputs["Surface"])
    backdrop.data.materials.append(mat)

    # --- world: strength 0 (C-02-5) ---------------------------------------
    world = bpy.data.worlds.new("NS02World") if not scene.world else scene.world
    scene.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes.get("Background")
    bg.inputs["Strength"].default_value = P["world_strength"]

    # --- lighting rig (C-02-6) --------------------------------------------
    def add_light(name, ltype, energy, color, loc, **kw):
        data = bpy.data.lights.new(name, ltype)
        data.energy = energy
        data.color = color
        for k, v in kw.items():
            setattr(data, k, v)
        ob = bpy.data.objects.new(name, data)
        ob.location = loc
        col_light.objects.link(ob)
        aim_light(ob)
        return ob

    add_light("Key_Area", 'AREA', P["key_energy"], P["key_color"], P["key_loc"],
              shape='RECTANGLE', size=P["key_size_x"], size_y=P["key_size_y"])
    add_light("Fill_Area", 'AREA', P["fill_energy"], P["fill_color"], P["fill_loc"],
              shape='RECTANGLE', size=P["fill_size"], size_y=P["fill_size_y"])
    add_light("Rim_Spot", 'SPOT', P["rim_energy"], rim_color(), P["rim_loc"],
              spot_size=math.radians(P["rim_spot_deg"]), spot_blend=P["rim_blend"])
    for i, loc in enumerate(P["accent_locs"]):
        add_light(f"Accent_Point_{i+1}", 'POINT', P["accent_energy"],
                  (1.0, 1.0, 1.0), loc, shadow_soft_size=0.0)

    # --- camera (C-02-1) ----------------------------------------------------
    cam_data = bpy.data.cameras.new("Template_Camera")
    cam_data.lens = P["lens_mm"]
    cam_data.clip_end = 100.0
    cam = bpy.data.objects.new("Template_Camera", cam_data)
    cam.location = P["camera_loc"]
    col_cam.objects.link(cam)
    look_at(cam, P["camera_target"])
    scene.camera = cam

    # --- skin pass on the character copy (C-02-7 Adapt) ---------------------
    skin = bpy.data.materials.get("Skin")
    assert skin is not None, "Skin material missing"
    for n in skin.node_tree.nodes:
        if n.bl_idname == "ShaderNodeBsdfPrincipled":
            n.inputs["Roughness"].default_value = P["skin_roughness"]
            n.inputs["Subsurface Weight"].default_value = P["skin_sss_weight"]
            n.inputs["Subsurface Radius"].default_value = (*P["skin_sss_radius"],)

    # --- outfit variant (Target 2 item 5, estate form) ----------------------
    outfit = bpy.data.objects.get("Prima_Outfit")
    outfit_end = bpy.data.objects.get("Prima_OutfitEnd")
    if variant == "nswfw":
        if outfit: outfit.hide_render = True
        if outfit_end: outfit_end.hide_render = True
    else:
        if outfit: outfit.hide_render = False
        if outfit_end: outfit_end.hide_render = True

    # --- pose: standing three-quarter promo (Target 2 order: gross -> fine)
    arm = bpy.data.objects.get("Armature")
    assert arm is not None and arm.type == "ARMATURE"
    assert tuple(arm.location) == (0.0, 0.0, 0.0), "C-02-2: model must not be moved"
    pb = arm.pose.bones
    for bone, (x, y, z) in P["pose"].items():
        b = pb.get(bone)
        assert b is not None, bone
        b.rotation_mode = 'XYZ'
        b.rotation_euler = (math.radians(x), math.radians(y), math.radians(z))
    pb["mixamorig:Hips"].location = P["hips_offset"]
    bpy.context.view_layer.update()

    # --- render preset (C-02-8) + simplify gate (C-02-3) --------------------
    scene.render.engine = 'CYCLES'
    scene.cycles.samples = P["render_max_samples"]
    scene.cycles.use_adaptive_sampling = True
    scene.cycles.adaptive_threshold = P["render_noise_threshold"]
    scene.cycles.use_denoising = P["render_denoise"]
    scene.cycles.denoiser = 'OPENIMAGEDENOISE'
    scene.cycles.device = 'CPU'          # deterministic route (Pass 2 Adapt)
    scene.cycles.seed = P["render_seed"]
    scene.cycles.use_animated_seed = False
    scene.render.resolution_x = P["res_x"]
    scene.render.resolution_y = P["res_y"]
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    scene.render.film_transparent = False
    scene.view_settings.exposure = P["exposure"]
    if P["simplify_must_be_off"]:
        scene.render.use_simplify = False
    assert scene.render.use_simplify is False, "C-02-3: simplify must be OFF"

    # --- fingerprint ----------------------------------------------------------
    fp = {"variant": variant, "params": {k: v for k, v in P.items()},
          "rim_color_computed": rim_color(),
          "objects": sorted((ob.name, ob.type) for ob in bpy.data.objects),
          "lights": sorted((ob.name, ob.data.type, round(ob.data.energy, 3),
                            tuple(round(c, 4) for c in ob.data.color))
                           for ob in bpy.data.objects if ob.type == 'LIGHT'),
          "camera": (cam_data.lens, tuple(round(v, 4) for v in cam.location),
                     tuple(round(v, 4) for v in cam.rotation_euler)),
          "render": (scene.cycles.samples, scene.cycles.adaptive_threshold,
                     scene.cycles.use_denoising, scene.cycles.seed,
                     scene.render.resolution_x, scene.render.resolution_y,
                     scene.render.use_simplify)}
    fp_json = json.dumps(fp, sort_keys=True, default=str)
    fp_hash = hashlib.sha256(fp_json.encode()).hexdigest()
    with open(f"{outdir}/fingerprint-{variant}.json", "w") as f:
        f.write(fp_json)
    with open(f"{outdir}/parameters-{variant}.json", "w") as f:
        json.dump({"params": P, "rim_color_computed": rim_color(),
                   "fingerprint_sha256": fp_hash}, f, indent=1, default=str)

    bpy.ops.wm.save_as_mainfile(filepath=f"{outdir}/template-{variant}.blend")
    print(f"FINGERPRINT {fp_hash}")

    if "--probe" in argv:
        scene.cycles.samples = 128
        scene.render.resolution_x = 540
        scene.render.resolution_y = 960
    if do_render:
        name = f"render-probe-{variant}.png" if "--probe" in argv else f"render-{variant}.png"
        scene.render.filepath = f"{outdir}/{name}"
        bpy.ops.render.render(write_still=True)
    print(f"OK ns02_template_{variant}")

main()
