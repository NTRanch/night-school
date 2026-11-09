import bpy, sys
from mathutils import Vector
argv = sys.argv[sys.argv.index("--")+1:]
bpy.ops.wm.open_mainfile(filepath=argv[0])
scene = bpy.context.scene
def evpos(ob):
    deps = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(deps)
    me = ev.to_mesh()
    pos = [ev.matrix_world @ v.co for v in me.vertices]
    ev.to_mesh_clear()
    return pos
cage = scene.objects["PrimaCage.L"]
body = scene.objects["Prima_Body"]
print("cage mods:", [(m.name, m.type) for m in cage.modifiers])
for fr in (1,2,3,4,5,7,9,12):
    scene.frame_set(fr)
    bpy.context.view_layer.update()
    cp = evpos(cage)
    cen = sum(cp, Vector((0,0,0)))/len(cp)
    bp = evpos(body)
    zs = [p.z for p in bp]
    print("f", fr, "cageL centroid", [round(x,4) for x in cen], "cageL vert0", [round(x,4) for x in cp[0]])
