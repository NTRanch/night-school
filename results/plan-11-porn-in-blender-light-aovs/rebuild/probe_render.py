# NS11 probe render: shrink the AOV variant scene and render once, so the
# EXR channel layout + relight lane can be validated before the full render.
import bpy, sys

def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    args = dict(zip(argv[::2], argv[1::2]))
    outdir = args.get("--outdir", ".")
    scene = bpy.context.scene
    scene.cycles.samples = 128
    scene.render.resolution_x = 540
    scene.render.resolution_y = 960
    scene.render.filepath = f"{outdir}/comp-render-probe.png"
    nt = scene.compositing_node_group
    for n in nt.nodes:
        if n.bl_idname == "CompositorNodeOutputFile":
            if n.format.file_format == "OPEN_EXR_MULTILAYER":
                n.file_name = "passes-probe"
            else:
                n.file_name = "comp-beauty-probe"
    bpy.ops.render.render(write_still=True)
    print("OK ns11_probe_render")

main()
