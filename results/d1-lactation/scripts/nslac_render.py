# nslac_render.py - evidence renders from a baked lactation blend
# Full camera (NSCam) + bust camera (NSBustCam) at the requested frames.
# Usage: blender -b -Y -noaudio --python nslac_render.py -- <blend> <outdir>
#        <frames_csv>
import bpy, sys, os, json, time
argv = sys.argv[sys.argv.index("--") + 1:]
blend_path, outdir, frames_csv = argv[0], argv[1], argv[2]
frames = [int(x) for x in frames_csv.split(",") if x]
os.makedirs(outdir, exist_ok=True)
bpy.ops.wm.open_mainfile(filepath=blend_path)
scene = bpy.context.scene
dom = bpy.data.objects["NSLAC_Domain"]
stats = []
for cam_name, tag in (("NSCam", "full"), ("NSBustCam", "bust")):
    scene.camera = bpy.data.objects[cam_name]
    for f in frames:
        t0 = time.time()
        scene.frame_set(f)
        scene.render.filepath = os.path.join(
            outdir, "%s_frame_%04d.png" % (tag, f))
        bpy.ops.render.render(write_still=True)
        dg = bpy.context.evaluated_depsgraph_get()
        ev = dom.evaluated_get(dg); me = ev.to_mesh()
        st = {"camera": tag, "frame": f, "mesh_verts": len(me.vertices),
              "render_seconds": round(time.time() - t0, 2)}
        ev.to_mesh_clear()
        stats.append(st); print("NSLAC RENDER", st)
with open(os.path.join(outdir, "render_stats.json"), "w") as fh:
    json.dump(stats, fh, indent=2)
print("NSLAC RENDER DONE")
