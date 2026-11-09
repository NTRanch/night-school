# nslac_closeup3.py - origin-framing close camera (third pass; passes 1-2
# framed mid-fall and upper chest respectively - see GATE-RECORD).
# Camera (0.05, -0.62, bz+0.06), target (0, -0.13, bz-0.02), lens 50:
# at the target depth (~0.49 m) the vertical half-extent is ~0.118 m, so
# the frame spans roughly bz-0.14 .. bz+0.10 - bust apex and the strand
# fall below it are both in frame.
# Usage: blender -b -Y -noaudio --python nslac_closeup3.py --
#        <baked_blend> <outdir> <frames_csv> <bust_z>
import bpy, sys, os, json, time
from mathutils import Vector
argv = sys.argv[sys.argv.index("--") + 1:]
blend_path, outdir, frames_csv, bz = argv[0], argv[1], argv[2], float(argv[3])
frames = [int(x) for x in frames_csv.split(",") if x]
os.makedirs(outdir, exist_ok=True)
bpy.ops.wm.open_mainfile(filepath=blend_path)
scene = bpy.context.scene
campos = Vector((0.05, -0.62, bz + 0.06))
target = Vector((0.0, -0.13, bz - 0.02))
bpy.ops.object.camera_add(location=campos)
cam = bpy.context.active_object; cam.name = "NSCloseCam3"
cam.rotation_euler = (target - campos).to_track_quat('-Z', 'Y').to_euler()
cam.data.lens = 50
scene.camera = cam
stats = []
for f in frames:
    t0 = time.time()
    scene.frame_set(f)
    scene.render.filepath = os.path.join(outdir, "close_frame_%04d.png" % f)
    bpy.ops.render.render(write_still=True)
    stats.append({"frame": f, "render_seconds": round(time.time() - t0, 2)})
    print("NSLAC CLOSE3", stats[-1])
with open(os.path.join(outdir, "close_stats.json"), "w") as fh:
    json.dump(stats, fh, indent=2)
print("NSLAC CLOSE3 DONE")
