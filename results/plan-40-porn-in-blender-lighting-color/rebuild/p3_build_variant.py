# NS40 "Resolve-First" variant — Pass 3 rebuild (Night School Plan 40).
# Loads a COPY of the Plan 02 NS02 template (built fresh from Plan 02's own
# builder; the template of record is never opened for writing), removes its
# lighting rig, and installs Anime Nyan's Plan-40 recipe translated onto the
# same stage: same Prima, pose, camera, backdrop, world (0.000) — only the
# light rig + grade chain change (the variables under test).
#
# Rig mapping (OBSERVATION.md §3.3 panel reads -> variant lamps):
#   Area.003 pink 8.8 W ellipse 1x1 m      -> NS40_Key_Area   (pink, 8.8 W)
#   white Area 10 W (several)             -> NS40_Fill_Area  (white, 10 W)
#   Area.005 strip 16x45 cm 10 W          -> NS40_Strip_Area (white, 10 W)
#   Spot white 25.7 W 14.2deg blend .732  -> NS40_Key_Spot + NS40_Rim_Spot
#   Point 10 W r=1cm / Point 1 W r=.1cm   -> NS40_Fill_Point / NS40_Accent_Point
# Grade (OBSERVATION.md §5.3, compositor translation of his Resolve chain):
#   FilmicBlend (RGB Curves) -> TealOrange (Color Balance) -> Contrast
#   (RGB Curves) -> Glow (Glare Bloom) -> Vignette (ellipse mask multiply)
#   -> Sharpen (Filter). His delivery tree's Denoising stage maps to the
#   render-side OIDN denoise (already the template's estate choice); his
#   Base Encoding stage maps to exposure 0.0 + linear EXR discipline (the
#   grade works on the scene-referred Combined, as his Resolve does).
# Exposure: variant view exposure 0.0 (the template's -1.8 is an estate
# fill for Plan 02's own UNREADABLE; the variant's lift lives in the grade).
# Usage: blender -b -Y <template-copy.blend> -P p3_build_variant.py -- --outdir <dir>
import faulthandler; faulthandler.enable()
import bpy, json, math, sys, hashlib
from mathutils import Vector

VARIANT_NAME = "NS40-ResolveFirst"

RIG = [
    # name, type, energy, color, loc, aim, kwargs, group
    ("NS40_Key_Area", 'AREA', 8.8, (1.0, 0.55, 0.85), (-0.85, -1.15, 1.75), (0, 0, 1.0),
     dict(shape='ELLIPSE', size=1.0, size_y=1.0), "NS40Key"),
    ("NS40_Fill_Area", 'AREA', 10.0, (1.0, 1.0, 1.0), (0.95, -1.05, 0.95), (0, 0, 0.95),
     dict(shape='ELLIPSE', size=1.0, size_y=1.0), "NS40Fill"),
    ("NS40_Strip_Area", 'AREA', 10.0, (1.0, 1.0, 1.0), (1.05, 0.15, 1.35), (0, 0, 1.05),
     dict(shape='ELLIPSE', size=0.16, size_y=0.45), "NS40Strip"),
    ("NS40_Key_Spot", 'SPOT', 25.7, (1.0, 1.0, 1.0), (0.45, -1.25, 2.05), (0, 0, 1.15),
     dict(spot_size=math.radians(14.2), spot_blend=0.732, shadow_soft_size=0.0), "NS40SpotKey"),
    ("NS40_Rim_Spot", 'SPOT', 25.7, (1.0, 1.0, 1.0), (0.65, 1.0, 2.15), (0, 0, 1.25),
     dict(spot_size=math.radians(14.2), spot_blend=0.732, shadow_soft_size=0.0), "NS40SpotRim"),
    ("NS40_Fill_Point", 'POINT', 10.0, (1.0, 1.0, 1.0), (0.3, -0.9, 0.55), None,
     dict(shadow_soft_size=0.01), "NS40Points"),
    ("NS40_Accent_Point", 'POINT', 1.0, (1.0, 1.0, 1.0), (-0.7, -0.6, 0.35), None,
     dict(shadow_soft_size=0.001), "NS40Points"),
]
GROUPS = ["NS40Key", "NS40Fill", "NS40Strip", "NS40SpotKey", "NS40SpotRim",
          "NS40Points", "Backdrop"]
OLD_RIG = ["Key_Area", "Fill_Area", "Rim_Spot"] + [f"Accent_Point_{i}" for i in range(1, 5)]

def aim(obj, target):
    d = Vector(target) - obj.location
    obj.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

def set_curve(node, pts, channel=3):
    try:
        curve = node.mapping.curves[channel]
        while len(curve.points) > 2:
            curve.points.remove(curve.points[1])
        curve.points[0].location = pts[0]
        curve.points[-1].location = pts[-1]
        for p in pts[1:-1]:
            curve.points.new(*p)
        node.mapping.update()
        return [tuple(pp.location) for pp in curve.points]
    except Exception as e:
        print("CURVE_SET_NOTE", node.name, e)
        return None

def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    args = dict(zip(argv[::2], argv[1::2]))
    outdir = args["--outdir"]
    scene = bpy.context.scene
    vl = bpy.context.view_layer
    readback = {"variant": VARIANT_NAME, "notes": []}

    # --- remove the template rig (the copy only; template of record safe) --
    for name in OLD_RIG:
        ob = bpy.data.objects.get(name)
        assert ob is not None, f"template lamp missing: {name}"
        bpy.data.objects.remove(ob, do_unlink=True)
    rig_coll = bpy.data.collections.get("LIGHTING_RIG")
    assert rig_coll is not None

    # --- install the NS40 rig ----------------------------------------------
    for name, ltype, energy, color, loc, target, kw, group in RIG:
        data = bpy.data.lights.new(name, ltype)
        data.energy = energy
        data.color = color
        for k, v in kw.items():
            setattr(data, k, v)
        ob = bpy.data.objects.new(name, data)
        ob.location = loc
        rig_coll.objects.link(ob)
        if target is not None:
            aim(ob, target)
        ob.lightgroup = group
    backdrop = bpy.data.objects.get("Backdrop")
    assert backdrop is not None
    backdrop.lightgroup = "Backdrop"

    # --- light groups + pass enables (Plan 11 method) -----------------------
    existing = [g.name for g in vl.lightgroups]
    for name in GROUPS:
        if name not in existing:
            vl.lightgroups.add(name=name)
    vl.update_render_passes()
    ungrouped = [ob.name for ob in bpy.data.objects
                 if ob.type == "LIGHT" and not ob.lightgroup]
    assert not ungrouped, f"ungrouped lights: {ungrouped}"
    if hasattr(vl, "use_pass_emit"):
        vl.use_pass_emit = True

    # --- grade-side render state --------------------------------------------
    scene.view_settings.exposure = 0.0
    readback["exposure"] = scene.view_settings.exposure

    # --- compositor: EXR pass contract + the grade chain --------------------
    scene.use_nodes = True
    nt = scene.compositing_node_group
    if nt is None:
        nt = bpy.data.node_groups.new("Compositor", "CompositorNodeTree")
        scene.compositing_node_group = nt
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    rl = nt.nodes.new("CompositorNodeRLayers")
    rl.layer = vl.name
    den = nt.nodes.new("CompositorNodeDenoise")  # materialises denoise sockets
    vl.update_render_passes()
    sockets = [o.name for o in rl.outputs]
    missing = [g for g in GROUPS if f"Combined_{g}" not in sockets]
    assert not missing, f"group passes missing: {missing} (have {sockets})"
    try:
        nt.interface.new_socket(name="Image", in_out='OUTPUT',
                                socket_type='NodeSocketColor')
    except Exception as e:
        readback["notes"].append(f"interface socket: {e}")

    pfout = nt.nodes.new("CompositorNodeOutputFile")
    pfout.label = "PASSES (multilayer EXR contract)"
    pfout.directory = outdir
    pfout.file_name = "passes-variant"
    pfout.format.file_format = "OPEN_EXR_MULTILAYER"
    pfout.format.color_depth = "32"
    pfout.format.exr_codec = "ZIP"
    store = ["Image", "Emission", "Volume Direct"] + [f"Combined_{g}" for g in GROUPS]
    stored = []
    for sname in store:
        if sname in sockets:
            item_name = "Combined" if sname == "Image" else sname
            pfout.file_output_items.new("RGBA", item_name)
            nt.links.new(rl.outputs[sname], pfout.inputs[item_name])
            stored.append(item_name)
    readback["stored_passes"] = stored

    # grade chain (each stage in try/except; readback records what exists)
    chain_src = rl.outputs["Image"]
    def link(a, b, bidx=0):
        nt.links.new(a, b.inputs[bidx] if not hasattr(b.inputs, "get") or True else b.inputs[0])

    stages = []
    # 1. FilmicBlend — filmic-like S with a lifted toe (his EXR is dark; the
    #    Resolve grade lifts hard, cf. OBSERVATION §5.1).
    try:
        c1 = nt.nodes.new("CompositorNodeCurveRGB"); c1.name = "NS40_FilmicBlend"
        got = set_curve(c1, [(0.0, 0.10), (0.25, 0.30), (0.5, 0.55), (0.75, 0.80), (1.0, 0.97)])
        nt.links.new(chain_src, c1.inputs["Image"]); chain_src = c1.outputs["Image"]
        stages.append(("FilmicBlend", got))
    except Exception as e:
        readback["notes"].append(f"FilmicBlend: {e}")
    # 2. TealOrange — lift toward teal, gain toward warm (Qazi split).
    # Blender 5.2 new compositor is SOCKET-driven (probed on primo):
    # ColorBalance inputs carry Lift/Gamma/Gain as (factor, colour) pairs.
    def set_nth_color(node, name, nth, rgba):
        def is_colour(sock):
            v = sock.default_value
            return hasattr(v, "__len__") and len(v) >= 3
        hits = [s for s in node.inputs if s.name == name and is_colour(s)]
        hits[nth].default_value = rgba
    try:
        cb = nt.nodes.new("CompositorNodeColorBalance"); cb.name = "NS40_TealOrange"
        set_nth_color(cb, 'Lift', 0, (0.94, 1.03, 1.05, 1.0))
        set_nth_color(cb, 'Gamma', 0, (1.0, 1.0, 1.0, 1.0))
        set_nth_color(cb, 'Gain', 0, (1.07, 1.0, 0.93, 1.0))
        nt.links.new(chain_src, cb.inputs["Image"]); chain_src = cb.outputs["Image"]
        stages.append(("TealOrange", "lift(0.94,1.03,1.05) gain(1.07,1.0,0.93) via colour sockets"))
    except Exception as e:
        readback["notes"].append(f"TealOrange: {e}")
    # 3. Contrast — gentle S.
    try:
        c2 = nt.nodes.new("CompositorNodeCurveRGB"); c2.name = "NS40_Contrast"
        got = set_curve(c2, [(0.0, 0.03), (0.3, 0.26), (0.7, 0.75), (1.0, 0.99)])
        nt.links.new(chain_src, c2.inputs["Image"]); chain_src = c2.outputs["Image"]
        stages.append(("Contrast", got))
    except Exception as e:
        readback["notes"].append(f"Contrast: {e}")
    # 4. Glow — bloom on highlights (his glow node; Resolve glow ~ thresholded).
    try:
        gl = nt.nodes.new("CompositorNodeGlare"); gl.name = "NS40_Glow"
        for sock, val in (("Type", 'Bloom'), ("Threshold", 1.0), ("Strength", 0.6)):
            if sock in gl.inputs:
                gl.inputs[sock].default_value = val
        nt.links.new(chain_src, gl.inputs[0]); chain_src = gl.outputs[0]
        stages.append(("Glow", {s.name: getattr(s, "default_value", None)
                                for s in gl.inputs}))
    except Exception as e:
        readback["notes"].append(f"Glow: {e}")
    # 5. Vignette — soft ellipse mask driving a ColorBalance gain darken:
    #    mask 1 at centre (Factor 0 -> identity), mask 0 at corners
    #    (Factor 1 -> gain 0.42). Socket-probed route (no Mix node needed).
    try:
        em = nt.nodes.new("CompositorNodeEllipseMask"); em.name = "NS40_VignetteMask"
        for sock, val in (("Operation", 'Add'), ("Value", 1.0),
                          ("Position", (0.5, 0.5)), ("Size", (0.85, 0.85))):
            if sock in em.inputs:
                em.inputs[sock].default_value = val
        bl = nt.nodes.new("CompositorNodeBlur"); bl.name = "NS40_VignetteBlur"
        if "Type" in bl.inputs:
            bl.inputs["Type"].default_value = 'Gaussian'
        if "Size" in bl.inputs:
            bl.inputs["Size"].default_value = (240.0, 240.0)
        nt.links.new(em.outputs[0], bl.inputs["Image"])
        inv = nt.nodes.new("CompositorNodeInvert"); inv.name = "NS40_VignetteInvert"
        nt.links.new(bl.outputs[0], inv.inputs["Color"])
        vg = nt.nodes.new("CompositorNodeColorBalance"); vg.name = "NS40_Vignette"
        set_nth_color(vg, 'Gain', 0, (0.72, 0.72, 0.72, 1.0))
        nt.links.new(chain_src, vg.inputs["Image"])
        nt.links.new(inv.outputs[0], vg.inputs["Factor"])
        chain_src = vg.outputs["Image"]
        stages.append(("Vignette", "ellipse(0.85) blur(240) invert -> CB gain 0.72 by factor"))
    except Exception as e:
        readback["notes"].append(f"Vignette: {e}")
    # 6. Sharpen — his sharpening sits in the vignette node pair; a light
    #    terminal sharpen closes the translation. Filter type is a socket
    #    in the new compositor.
    try:
        sh = nt.nodes.new("CompositorNodeFilter"); sh.name = "NS40_Sharpen"
        if "Type" in sh.inputs:
            sh.inputs["Type"].default_value = 'Box Sharpen'
        if "Factor" in sh.inputs:
            sh.inputs["Factor"].default_value = 0.5
        nt.links.new(chain_src, sh.inputs["Image"]); chain_src = sh.outputs["Image"]
        stages.append(("Sharpen", "Filter Type socket = Box Sharpen"))
    except Exception as e:
        readback["notes"].append(f"Sharpen: {e}")

    comp = nt.nodes.new("NodeGroupOutput")
    nt.links.new(chain_src, comp.inputs[0])
    readback["grade_stages"] = [(n, str(v)[:120]) for n, v in stages]
    readback["grade_chain_nodes"] = [n.name for n in nt.nodes]

    # --- fingerprint ----------------------------------------------------------
    fp = {"variant": VARIANT_NAME,
          "lamps": sorted((ob.name, ob.data.type, round(ob.data.energy, 3),
                           tuple(round(c, 4) for c in ob.data.color),
                           tuple(round(v, 3) for v in ob.location), ob.lightgroup)
                          for ob in bpy.data.objects if ob.type == 'LIGHT'),
          "exposure": scene.view_settings.exposure,
          "render": (scene.cycles.samples, scene.cycles.adaptive_threshold,
                     scene.cycles.use_denoising, scene.cycles.seed),
          "readback": readback}
    fp_json = json.dumps(fp, sort_keys=True, default=str)
    fp_hash = hashlib.sha256(fp_json.encode()).hexdigest()
    with open(f"{outdir}/fingerprint-variant.json", "w") as f:
        f.write(fp_json)
    print(f"VARIANT_FINGERPRINT {fp_hash}")
    bpy.ops.wm.save_as_mainfile(filepath=f"{outdir}/ns40-variant.blend")
    print(f"OK build_variant {VARIANT_NAME}")

main()
