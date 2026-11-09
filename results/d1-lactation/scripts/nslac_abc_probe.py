# nslac_abc_probe.py - Tier 2 round-trip probe: re-import the Alembic and
# report verts + bbox at probed frames (metre identity check, Plan 06 S3).
# Usage: blender -b -Y -noaudio --python nslac_abc_probe.py -- <abc> <frames_csv>
import bpy, sys, json
argv = sys.argv[sys.argv.index("--") + 1:]
abc_path, frames_csv = argv[0], argv[1]
frames = [int(x) for x in frames_csv.split(",") if x]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.wm.alembic_import(filepath=abc_path)
scene = bpy.context.scene
objs = [o for o in scene.objects if o.type == "MESH"]
print("NSLAC ABC objects:", [o.name for o in objs])
out = {}
for f in frames:
    scene.frame_set(f)
    dg = bpy.context.evaluated_depsgraph_get()
    for o in objs:
        ev = o.evaluated_get(dg); me = ev.to_mesh()
        vs = [ev.matrix_world @ v.co for v in me.vertices]
        bb = [[round(min(v[i] for v in vs), 4), round(max(v[i] for v in vs), 4)]
              for i in range(3)] if vs else None
        out[str(f)] = {"verts": len(vs), "bbox": bb}
        ev.to_mesh_clear()
    print("NSLAC ABC", f, json.dumps(out[str(f)]))
print("NSLAC ABC_PROBE_JSON " + json.dumps(out))
