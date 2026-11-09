# Plan 36 census: inventory a .blend's animator-facing control surface.
# Usage: blender -b <file.blend> -Y --python census.py -- <out.json>
import bpy, json, sys
argv = sys.argv[sys.argv.index("--") + 1:]
out_path = argv[0]
rec = {"file": bpy.data.filepath, "objects": [], "armatures": {}, "totals": {}}
n_shape_keys = 0
n_constraints = 0
for ob in bpy.data.objects:
    entry = {"name": ob.name, "type": ob.type,
             "parent": ob.parent.name if ob.parent else None,
             "constraints": [c.type for c in ob.constraints],
             "custom_props": sorted(ob.keys())}
    n_constraints += len(ob.constraints)
    if ob.type == "MESH":
        kb = ob.data.shape_keys
        keys = [k.name for k in kb.key_blocks] if kb else []
        entry["shape_keys"] = keys
        entry["verts"] = len(ob.data.vertices)
        n_shape_keys += len(keys)
    rec["objects"].append(entry)
    if ob.type == "ARMATURE":
        bones = [b.name for b in ob.data.bones]
        rec["armatures"][ob.name] = {
            "bones": bones, "bone_count": len(bones),
            "pose_constraints": {pb.name: [c.type for c in pb.constraints]
                                 for pb in ob.pose.bones if pb.constraints},
            "custom_props": sorted(ob.keys())}
rec["totals"] = {"objects": len(bpy.data.objects),
                 "shape_keys": n_shape_keys,
                 "object_constraints": n_constraints}
with open(out_path, "w") as f:
    json.dump(rec, f, indent=1, sort_keys=True)
print("CENSUS WROTE", out_path, rec["totals"])
