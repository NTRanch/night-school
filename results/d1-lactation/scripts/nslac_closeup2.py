# nslac_closeup.py - close bust-camera renders from a baked lactation blend
# Adds a dedicated close camera framing the bust + emission origin (the
# in-scene NSBustCam reads as a torso crop at 1 m; this camera sits at
# 0.55 m). Usage: blender -b -Y -noaudio --python nslac_closeup.py --
#        <baked_blend> <outdir> <frames_csv> <bust_z>
import bpy, sys, os, json, time
from mathutils import Vector
argv = sys.argv[sys.argv.index("--") + 1:]
blend_path, outdir, frames_csv, bz = argv[0], argv[1], argv[2], float(argv[3])
frames = [int(x) for x in frames_csv.split(",") if x]
os.makedirs(outdir, exist_ok=True)
bpy.ops.wm.open_mainfile(filepath=blend_path)
scene = bpy.context.scene
bpy.ops.object.camera_add(location=(0.06, -0.52, bz + 0.17))
cam = bpy.context.active_object; cam.name = "NSCloseCam"
d = Vector((0.0, -0.14, bz + 0.04)) - Vector((0.06, -0.58, bz + 0.10))
cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
cam.data.lens = 55
scene.camera = cam
stats = []
for f in frames:
    t0 = time.time()
    scene.frame_set(f)
    scene.render.filepath = os.path.join(outdir, "close_frame_%04d.png" % f)
    bpy.ops.render.render(write_still=True)
    stats.append({"frame": f, "render_seconds": round(time.time() - t0, 2)})
    print("NSLAC CLOSE", stats[-1])
with open(os.path.join(outdir, "close_stats.json"), "w") as fh:
    json.dump(stats, fh, indent=2)
print("NSLAC CLOSE DONE")
