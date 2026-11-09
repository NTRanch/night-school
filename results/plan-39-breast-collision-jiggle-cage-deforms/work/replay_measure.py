#!/usr/bin/env python3
"""Plan 39 (A) — toggle-free sequential replay measurement.
Opens a blend, steps frames 1..48 IN ORDER (the only sanctioned way
to replay a baked point cache), records evaluated positions of
Prima_Body's chest band and both cages per frame, plus a NaN/huge
scan. Never touches a modifier. Usage:
  blender -b -Y --python replay_measure.py -- <blend> <out.json>
"""
import bpy, json, math, sys
argv = sys.argv[sys.argv.index("--") + 1:]
BLEND, OUT = argv[0], argv[1]
bpy.ops.wm.open_mainfile(filepath=BLEND)
scene = bpy.context.scene
body = scene.objects["Prima_Body"]
cages = {s: scene.objects["PrimaCage.%s" % s] for s in ("L", "R")}

def evpos(ob):
    deps = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(deps)
    me = ev.to_mesh()
    pos = [ev.matrix_world @ v.co for v in me.vertices]
    ev.to_mesh_clear()
    return pos

scene.frame_set(1)
bpy.context.view_layer.update()
ref = evpos(body)
zs = [p.z for p in ref]
lo = min(zs) + 0.66 * (max(zs) - min(zs))
hi = min(zs) + 0.84 * (max(zs) - min(zs))
band_idx = [i for i, p in enumerate(ref) if lo <= p.z <= hi]

frames = {}
for fr in range(1, 49):
    scene.frame_set(fr)
    bpy.context.view_layer.update()
    bp = evpos(body)
    rec = {"band": [[round(c, 6) for c in bp[i]] for i in band_idx]}
    bad = 0
    mx = 0.0
    for p in bp:
        for c in p:
            if not math.isfinite(c):
                bad += 1
            else:
                mx = max(mx, abs(c))
    rec["body_nonfinite"] = bad
    rec["body_max_abs_coord"] = round(mx, 4)
    for s, cage in cages.items():
        cp = evpos(cage)
        rec["cage_" + s] = [[round(c, 6) for c in p] for p in cp]
        cb = sum(1 for p in cp for c in p if not math.isfinite(c))
        rec["cage_%s_nonfinite" % s] = cb
    frames[fr] = rec
with open(OUT, "w") as f:
    json.dump({"band_idx": band_idx, "frames": {str(k): v for k, v in frames.items()}}, f)
print("REPLAY_MEASURE_DONE", OUT)
