# NS11 EXR -> PNG: display-referred conversion of a single-layer linear EXR
# through Blender's own colour management (AgX view transform + the Plan 02
# template's exposure -1.8), so relight PNGs are judged in the same pipeline
# as the template's beauty PNG. Usage:
#   blender -b -Y --factory-startup --offline-mode -noaudio --python-exit-code 1 \
#     -P exr_to_png.py -- --in <file.exr> --out <file.png>
import bpy, sys

def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    args = dict(zip(argv[::2], argv[1::2]))
    src, dst = args["--in"], args["--out"]
    scene = bpy.context.scene
    img = bpy.data.images.load(src)
    w, h = img.size
    scene.render.resolution_x = w
    scene.render.resolution_y = h
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.filepath = dst
    scene.render.film_transparent = False
    scene.view_settings.view_transform = "AgX"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = -1.8
    scene.view_settings.gamma = 1.0
    scene.use_nodes = True
    nt = scene.compositing_node_group
    if nt is None:
        nt = bpy.data.node_groups.new("Compositor", "CompositorNodeTree")
        scene.compositing_node_group = nt
    # A hand-made group has no interface sockets: the Group Output then has
    # nothing to emit and the render comes out black (probed). Ensure one.
    outs = [s.name for s in nt.interface.items_tree
            if getattr(s, "in_out", None) == "OUTPUT"]
    if not outs:
        nt.interface.new_socket(name="Image", in_out="OUTPUT",
                                socket_type="NodeSocketColor")
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    inode = nt.nodes.new("CompositorNodeImage")
    inode.image = img
    out = nt.nodes.new("NodeGroupOutput")
    tgt = out.inputs.get("Image") or out.inputs[0]
    nt.links.new(inode.outputs["Image"], tgt)
    # A render is required to execute the compositor; the scene is empty,
    # the Group Output comes solely from the Image node.
    bpy.ops.render.render(write_still=True)
    print("OK ns11_exr_to_png")

main()
