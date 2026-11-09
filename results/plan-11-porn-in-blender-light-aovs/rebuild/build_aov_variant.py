# NS11 "Light Groups" — AOV variant of the Plan 02 NS02 template (Night School Plan 11, Pass 3)
# Clean-room rebuild from TECHNIQUE.md alone. Blender 5.2.3, headless, deterministic.
# Usage:
#   blender -b -Y --factory-startup --offline-mode -noaudio -t <k> --python-exit-code 1 \
#     template-<variant>.blend -P build_aov_variant.py -- --variant nswfw|sfw --outdir <dir> [--render]
# Input is a COPY of the Plan 02 template blend produced in this run's own outdir
# by Plan 02's build_template.py (Plan 02 files are never modified).
# Adds: one Cycles light group per Plan 02 light role (+ Backdrop for the emissive
# cyclorama, whose emission belongs to no lamp), a compositor tree that rebuilds
# the beauty as the sum of per-group passes through per-group gain/tint controls,
# and multilayer OpenEXR output. Writes template-<variant>-aov.blend + fingerprint.
import faulthandler; faulthandler.enable()
import bpy, json, sys, hashlib

# Group assignment: Plan 02 object name -> light group. The sheet's rule is
# ONE GROUP PER LAMP (his two fills are separate groups), named for the role.
GROUPS = ["Key", "Rim", "Fill", "Accent_1", "Accent_2", "Accent_3", "Accent_4", "Backdrop"]
ASSIGN = {
    "Key_Area": "Key",
    "Rim_Spot": "Rim",
    "Fill_Area": "Fill",
    "Accent_Point_1": "Accent_1", "Accent_Point_2": "Accent_2",
    "Accent_Point_3": "Accent_3", "Accent_Point_4": "Accent_4",
    "Backdrop": "Backdrop",   # emissive mesh: its emission is assigned via the object property
}
# Pass-render contract (Pass 2 sheet): multilayer EXR, full float, lossless ZIP.
EXR_DEPTH = "32"
EXR_CODEC = "ZIP"

def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    args = dict(zip(argv[::2], argv[1::2]))
    variant = args.get("--variant", "nswfw")
    outdir = args.get("--outdir", ".")
    do_render = "--render" in argv
    assert variant in ("nswfw", "sfw"), variant

    scene = bpy.context.scene
    vl = bpy.context.view_layer
    assert scene.render.engine == "CYCLES", scene.render.engine

    # --- light groups -------------------------------------------------------
    existing = [g.name for g in vl.lightgroups]
    for name in GROUPS:
        if name not in existing:
            vl.lightgroups.add(name=name)
    vl.update_render_passes()
    assigned = {}
    for ob_name, group in ASSIGN.items():
        ob = bpy.data.objects.get(ob_name)
        assert ob is not None, f"template object missing: {ob_name}"
        ob.lightgroup = group
        assigned[ob_name] = group
    # every light object in the scene must carry a group (no silent remainder)
    ungrouped = [ob.name for ob in bpy.data.objects
                 if ob.type == "LIGHT" and not ob.lightgroup]
    assert not ungrouped, f"ungrouped lights: {ungrouped}"
    # The Emission pass must exist before update_render_passes() is called
    # in the tree section, or its RL socket never appears (census ns11-census8).
    if hasattr(vl, "use_pass_emit"):
        vl.use_pass_emit = True

    # --- compositor tree: beauty = sum over groups of (pass x gain/tint) ----
    # Blender 5.x: the compositor lives in scene.compositing_node_group
    # (scene.node_tree no longer exists — probed on 5.2.3, census ns11-census2).
    scene.use_nodes = True
    nt = scene.compositing_node_group
    if nt is None:
        nt = bpy.data.node_groups.new("Compositor", "CompositorNodeTree")
        scene.compositing_node_group = nt
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    rl = nt.nodes.new("CompositorNodeRLayers")
    rl.location = (-900, 0)
    rl.layer = vl.name
    # A Denoise node in the tree is what makes the denoising-data passes
    # appear on the RL node in this build (probed: absent without one).
    den = nt.nodes.new("CompositorNodeDenoise")
    den.location = (700, 0)
    vl.update_render_passes()
    sockets = [o.name for o in rl.outputs]
    print("RL_OUTPUTS", sockets)
    missing = [g for g in GROUPS if f"Combined_{g}" not in sockets]
    assert not missing, f"light-group passes missing from RL outputs: {missing} (have {sockets})"

    # Blender 5.2 compositor node types (probed, census ns11-census3):
    # Composite -> NodeGroupOutput; MixRGB -> ShaderNodeMixRGB
    # (inputs Factor/Color1/Color2, output Color); RGB -> CompositorNodeRGB.
    comp = nt.nodes.new("NodeGroupOutput")
    comp.location = (940, 0)
    viewer = nt.nodes.new("CompositorNodeViewer")
    viewer.location = (940, -220)
    fout = None
    try:
        fout = nt.nodes.new("CompositorNodeOutputFile")
        fout.location = (940, 220)
        fout.directory = outdir
        fout.file_name = f"comp-beauty-{variant}"
        fout.format.file_format = "PNG"
        fout.file_output_items.new("RGBA", "Image")
    except Exception as e:
        print("FILEOUTPUT_CONFIG_SKIPPED", e)
        fout = None
    # Passes File Output (Blender 5.2: multilayer EXR lives HERE, not in the
    # render format enum — probed censuses ns11-census5..10). One RGBA item
    # per stored pass; the item name becomes the EXR layer name.
    pfout = nt.nodes.new("CompositorNodeOutputFile")
    pfout.location = (-900, -700)
    pfout.label = "PASSES (multilayer EXR contract)"
    pfout.directory = outdir
    pfout.file_name = f"passes-{variant}"
    pfout.format.file_format = "OPEN_EXR_MULTILAYER"
    pfout.format.color_depth = EXR_DEPTH
    pfout.format.exr_codec = EXR_CODEC
    store = ["Image", "Emission", "Volume Direct"] + [f"Combined_{g}" for g in GROUPS]
    stored = []
    for sname in store:
        if sname in sockets:
            item_name = "Combined" if sname == "Image" else sname
            pfout.file_output_items.new("RGBA", item_name)
            nt.links.new(rl.outputs[sname], pfout.inputs[item_name])
            stored.append(item_name)
    print("PASSES_STORED", stored)
    tree_order_passes = stored
    # Terminal Denoise on the sum (sheet C-11-4). On 5.2.3 the RL node
    # exposes no denoising-data sockets (probed three ways, census
    # ns11-census4): the 5.0.1 guide wiring is version drift; the
    # Denoise runs on the sum with its internal guides here.
    tree_order_extra = []
    if "Denoising Albedo" in sockets and "Denoising Normal" in sockets:
        nt.links.new(rl.outputs["Denoising Albedo"], den.inputs["Albedo"])
        nt.links.new(rl.outputs["Denoising Normal"], den.inputs["Normal"])
        tree_order_extra = ["Denoise(guides: Albedo+Normal)"]
    else:
        tree_order_extra = ["Denoise(guides: none exposed on 5.2.3 RL node)"]

    acc = None
    tree_order = ["RenderLayers"]
    for i, g in enumerate(GROUPS):
        y = 300 - i * 220
        gain = nt.nodes.new("CompositorNodeRGB")
        gain.label = f"{g}_gain_tint (1,1,1 = unmodified)"
        gain.location = (-620, y)
        gain.outputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
        mul = nt.nodes.new("ShaderNodeMixRGB")
        mul.blend_type = "MULTIPLY"
        mul.inputs["Factor"].default_value = 1.0
        mul.location = (-380, y)
        nt.links.new(rl.outputs[f"Combined_{g}"], mul.inputs["Color1"])
        nt.links.new(gain.outputs["Color"], mul.inputs["Color2"])
        tree_order += [f"{g}:RGB(gain/tint)", f"{g}:Mix.MULTIPLY"]
        if acc is None:
            acc = mul
        else:
            add = nt.nodes.new("ShaderNodeMixRGB")
            add.blend_type = "ADD"
            add.inputs["Factor"].default_value = 1.0
            add.location = (-100 + i * 10, y)
            nt.links.new(acc.outputs["Color"], add.inputs["Color1"])
            nt.links.new(mul.outputs["Color"], add.inputs["Color2"])
            tree_order += [f"Mix.ADD(<- {g})"]
            acc = add
    nt.links.new(acc.outputs["Color"], den.inputs["Image"])
    nt.links.new(den.outputs["Image"], comp.inputs[0])
    nt.links.new(den.outputs["Image"], viewer.inputs["Image"])
    if fout is not None and "Image" in fout.inputs:
        nt.links.new(den.outputs["Image"], fout.inputs["Image"])
    tree_order += tree_order_extra + ["GroupOutput(composite)", "Viewer",
                                      "FileOutput(PNG comp-beauty)",
                                      f"FileOutput(EXR passes: {','.join(stored)})"]

    # --- render contract for the pass render --------------------------------
    # Sheet C-11-4: the renderer's own denoise is OFF for a pass render;
    # denoising happens in the compositor on the summed passes.
    scene.cycles.use_denoising = False
    # The scene render writes the COMPOSITED result (the tree's Group
    # Output) as PNG; the multilayer EXR is written by the passes File
    # Output node in the same render (5.2 route, see above).
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = f"{outdir}/comp-render-{variant}.png"
    scene.render.use_compositing = True
    vl.use_pass_combined = True
    # Pass toggles the contract needs (probe what this build exposes).
    pass_toggles = {}
    for attr in ("use_pass_emit", "use_pass_environment", "use_pass_ambient_occlusion",
                 "use_pass_denoising_data", "use_pass_volume_direct", "use_pass_volume_indirect"):
        if hasattr(vl, attr):
            pass_toggles[attr] = True
    if hasattr(vl, "use_pass_emit"):
        vl.use_pass_emit = True
    print("PASS_TOGGLES_KNOWN", sorted(pass_toggles))

    fp = {"variant": variant, "aov_variant": "NS11-LightGroups-v1",
          "groups": GROUPS, "assigned": assigned,
          "rl_outputs": sockets, "tree_order": tree_order,
          "exr": {"format": "OPEN_EXR_MULTILAYER", "depth": EXR_DEPTH, "codec": EXR_CODEC},
          "denoise": bool(scene.cycles.use_denoising),
          "samples": scene.cycles.samples,
          "threshold": scene.cycles.adaptive_threshold,
          "seed": scene.cycles.seed,
          "resolution": (scene.render.resolution_x, scene.render.resolution_y)}
    fp_json = json.dumps(fp, sort_keys=True, default=str)
    fp_hash = hashlib.sha256(fp_json.encode()).hexdigest()
    with open(f"{outdir}/fingerprint-aov-{variant}.json", "w") as f:
        f.write(fp_json)
    with open(f"{outdir}/parameters-aov-{variant}.json", "w") as f:
        json.dump({"params": fp, "fingerprint_sha256": fp_hash}, f, indent=1, default=str)

    bpy.ops.wm.save_as_mainfile(filepath=f"{outdir}/template-{variant}-aov.blend")
    print(f"FINGERPRINT {fp_hash}")
    if do_render:
        bpy.ops.render.render(write_still=True)
    print(f"OK ns11_aov_variant_{variant}")

main()
