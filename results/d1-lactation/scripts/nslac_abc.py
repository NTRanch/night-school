# nslac_abc.py - Tier 2 Alembic handoff (Plan 07 CACHE-CONTRACT): mesh only.
# Usage: blender -b -Y -noaudio --python nslac_abc.py -- <baked_blend>
#        <abc_out> <end_frame>
import bpy, sys, os
argv = sys.argv[sys.argv.index("--") + 1:]
blend_path, abc_out, endf = argv[0], argv[1], int(argv[2])
bpy.ops.wm.open_mainfile(filepath=blend_path)
for o in bpy.context.selected_objects: o.select_set(False)
dom = bpy.data.objects["NSLAC_Domain"]
dom.select_set(True); bpy.context.view_layer.objects.active = dom
bpy.ops.wm.alembic_export(filepath=abc_out, selected=True, start=1, end=endf,
                          evaluation_mode='RENDER', flatten=False)
print("NSLAC ABC EXPORTED", abc_out, os.path.getsize(abc_out))
