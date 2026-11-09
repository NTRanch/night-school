# Branch-energy analysis: load runA's saved blend, strip its File Output nodes,
# write each recipe branch (Diff/Gloss/Trans/Rest + boosted variant branches) to
# its own EXR, re-render (deterministic, same seed/settings), and report each
# branch's mean RGB + share of the recreated sum's mean energy.
import bpy, os, sys
argv = sys.argv[sys.argv.index("--") + 1:]
args = dict(zip(argv[::2], argv[1::2]))
outdir = os.path.abspath(args["--outdir"])
os.makedirs(outdir, exist_ok=True)
scene = bpy.context.scene
nt = scene.compositing_node_group
for n in list(nt.nodes):
    if n.bl_idname == "CompositorNodeOutputFile":
        nt.nodes.remove(n)

def fileout(fname, sock, x, y):
    fo = nt.nodes.new("CompositorNodeOutputFile")
    fo.location = (x, y)
    fo.directory = outdir
    fo.file_name = ""
    fo.format.media_type = 'IMAGE'
    fo.format.file_format = 'OPEN_EXR'
    fo.format.exr_codec = 'ZIP'
    fo.format.color_depth = '32'
    fo.file_output_items.new("RGBA", fname)
    nt.links.new(sock, fo.inputs[0])

targets = [("branch_diff", "Diff_Mul"), ("branch_gloss", "Gloss_Mul"),
           ("branch_trans", "Trans_Mul"), ("branch_rest", "Rest_Add2"),
           ("branch_gloss_v", "GlossV_Boost"), ("branch_rest_v", "RestV_Add2")]
for i, (fname, node_name) in enumerate(targets):
    n = nt.nodes.get(node_name)
    assert n is not None, node_name
    fileout(fname, n.outputs[2], 600, 900 - i * 140)
scene.render.filepath = os.path.join(outdir, "main.exr")
bpy.ops.render.render(write_still=True)
print("OK branch energy render")
print("FILES:", sorted(os.listdir(outdir)))
