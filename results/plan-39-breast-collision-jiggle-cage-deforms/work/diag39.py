import bpy, json, sys
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
out = {}
for side in ("L","R"):
    cage = scene.objects["PrimaCage.%s" % side]
    cl = [m for m in cage.modifiers if m.type=="CLOTH"][0]
    print("solver_result", side, cl.solver_result.status if hasattr(cl.solver_result,'status') else cl.solver_result)
    baked = {}
    for fr in (1,4,7,8,9,10,13,19):
        scene.frame_set(fr); bpy.context.view_layer.update()
        baked[fr] = evpos(cage)
    cl.show_viewport = False; cl.show_render = False
    bpy.context.view_layer.update()
    diffs = {}
    for fr in (1,4,7,8,9,10,13,19):
        scene.frame_set(fr); bpy.context.view_layer.update()
        ref = evpos(cage)
        ds = [(baked[fr][i]-ref[i]).length*1000.0 for i in range(len(ref))]
        diffs[fr] = {"max_mm": round(max(ds),4), "mean_mm": round(sum(ds)/len(ds),4)}
    cl.show_viewport = True; cl.show_render = True
    out[side] = diffs
    print("CAGE_SECONDARY", side, json.dumps(diffs))
