# NS40 Pass 3 — groupify (Plan 11 method): add light groups + the multilayer
# EXR pass contract to an EXISTING template copy, without touching its rig.
# Usage: blender -b -Y <in.blend> -P p3_groupify.py -- --outdir <dir> --tag <tag>
# Control-side groups follow Plan 11's names so shares compare 1:1.
import faulthandler; faulthandler.enable()
import bpy, json, sys

ASSIGN = {
    "Key_Area": "Key", "Fill_Area": "Fill", "Rim_Spot": "Rim",
    "Accent_Point_1": "Accent_1", "Accent_Point_2": "Accent_2",
    "Accent_Point_3": "Accent_3", "Accent_Point_4": "Accent_4",
    "Backdrop": "Backdrop",
}
GROUPS = ["Key", "Rim", "Fill", "Accent_1", "Accent_2", "Accent_3", "Accent_4", "Backdrop"]

def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    args = dict(zip(argv[::2], argv[1::2]))
    outdir = args["--outdir"]; tag = args["--tag"]
    scene = bpy.context.scene
    vl = bpy.context.view_layer
    assert scene.render.engine == "CYCLES", scene.render.engine

    existing = [g.name for g in vl.lightgroups]
    for name in GROUPS:
        if name not in existing:
            vl.lightgroups.add(name=name)
    vl.update_render_passes()
    for ob_name, group in ASSIGN.items():
        ob = bpy.data.objects.get(ob_name)
        assert ob is not None, f"template object missing: {ob_name}"
        ob.lightgroup = group
    ungrouped = [ob.name for ob in bpy.data.objects
                 if ob.type == "LIGHT" and not ob.lightgroup]
    assert not ungrouped, f"ungrouped lights: {ungrouped}"
    if hasattr(vl, "use_pass_emit"):
        vl.use_pass_emit = True

    # Compositor: direct beauty + multilayer EXR pass contract (Plan 11).
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
    if not any(s.name == "Image" and s.in_out == 'OUTPUT' for s in nt.interface.items_tree
               if hasattr(s, "in_out")):
        try:
            nt.interface.new_socket(name="Image", in_out='OUTPUT',
                                    socket_type='NodeSocketColor')
        except Exception as e:
            print("INTERFACE_SOCKET_NOTE", e)
    comp = nt.nodes.new("NodeGroupOutput")
    nt.links.new(rl.outputs["Image"], comp.inputs[0])

    pfout = nt.nodes.new("CompositorNodeOutputFile")
    pfout.label = "PASSES (multilayer EXR contract)"
    pfout.directory = outdir
    pfout.file_name = f"passes-{tag}"
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
    print("PASSES_STORED", stored)
    with open(f"{outdir}/groups-{tag}.json", "w") as f:
        json.dump({"tag": tag, "assign": ASSIGN, "stored_passes": stored}, f, indent=1)
    bpy.ops.wm.save_as_mainfile(filepath=f"{outdir}/{tag}-groups.blend")
    print(f"OK groupify {tag}")

main()
