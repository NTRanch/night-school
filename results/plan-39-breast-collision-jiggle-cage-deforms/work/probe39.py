import bpy, json, sys
argv = sys.argv[sys.argv.index("--")+1:]
bpy.ops.wm.open_mainfile(filepath=argv[0])
out = {"objects": [], "cloth_props": None, "surfdef_props": None, "datatransfer_props": None}
for o in bpy.context.scene.objects:
    e = {"name": o.name, "type": o.type, "parent": o.parent.name if o.parent else None,
         "mods": [(m.name, m.type) for m in o.modifiers]}
    if o.type == "MESH":
        e["verts"] = len(o.data.vertices)
        e["vgroups"] = [g.name for g in o.vertex_groups]
        e["shape_keys"] = [kb.name for kb in o.data.shape_keys.key_blocks] if o.data.shape_keys else []
    out["objects"].append(e)
# cloth settings props via a temp object
bpy.ops.mesh.primitive_cube_add()
tmp = bpy.context.active_object
cm = tmp.modifiers.new("c", "CLOTH")
cs = cm.settings
out["cloth_props"] = sorted(p.identifier for p in cs.bl_rna.properties)
out["cloth_modifier_props"] = sorted(p.identifier for p in cm.bl_rna.properties)
try:
    out["cloth_collision_props"] = sorted(p.identifier for p in cm.collision_settings.bl_rna.properties)
except Exception as ex:
    out["cloth_collision_props_err"] = repr(ex)
out["cloth_cache_props"] = sorted(p.identifier for p in cm.point_cache.bl_rna.properties)
out["cloth_defaults"] = {k: getattr(cs, k) for k in ("quality","mass","use_pressure","pin_stiffness") if hasattr(cs,k)}
try:
    out["cloth_defaults"]["uniform_pressure_force"] = cs.uniform_pressure_force
except Exception as ex:
    out["cloth_defaults"]["uniform_pressure_force_err"] = repr(ex)
try:
    out["cloth_defaults"]["pressure_factor"] = cs.pressure_factor
except Exception as ex:
    out["cloth_defaults"]["pressure_factor_err"] = repr(ex)
try:
    out["cloth_defaults"]["gravity"] = cs.effector_weights.gravity
except Exception as ex:
    out["cloth_defaults"]["gravity_err"] = repr(ex)
sd = tmp.modifiers.new("s", "SURFACE_DEFORM")
out["surfdef_props"] = sorted(p.identifier for p in sd.bl_rna.properties)
dt = tmp.modifiers.new("d", "DATA_TRANSFER")
out["datatransfer_props"] = sorted(p.identifier for p in dt.bl_rna.properties)
out["scene"] = {"fps": bpy.context.scene.render.fps, "frame_start": bpy.context.scene.frame_start, "frame_end": bpy.context.scene.frame_end}
print("PROBE39_JSON_BEGIN")
print(json.dumps(out, indent=1))
print("PROBE39_JSON_END")
