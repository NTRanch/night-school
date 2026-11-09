# ns09_gn.py - Night School Plan 09 Pass 3 clean-room rebuild
# Blender 5.2.3 LTS. Scripted, seeded, headless, re-runnable.
# Route under test (from OBSERVATION.md, sheet alone):
#   BezierCurve -> GN group (Curve to Points -> Points to Volume ->
#   Volume to Mesh -> Set Shade Smooth -> Set Material) -> Smooth modifier.
# Variants:
#   v1_firstform : Count 10, Voxel Amount 64, Radius 0.5   (sheet 660 s state)
#   v2_lumps     : Count 100, Voxel Amount 64, Radius 0.25 (sheet 720 s region;
#                  count interpolated from the 1380 s Count-100 state - the
#                  720 s tree itself is not pane-read; see PASS3-REBUILD.md)
#   v3_final     : Length 0.001 m, Voxel Size = Radius/Resolution,
#                  Radius 0.100, Resolution 2.000, shade smooth + material +
#                  Smooth modifier 1.5 x20                  (sheet final form)
#   v4_bodyradius: v3 with Radius 0.025                     (sheet 2030 s state)
# Usage: blender -b -Y --factory-startup --python ns09_gn.py -- <outdir>
import bpy, sys, os, json, time, hashlib, math

argv = sys.argv[sys.argv.index("--") + 1:]
outdir = argv[0]
os.makedirs(outdir, exist_ok=True)
os.makedirs(os.path.join(outdir, "renders"), exist_ok=True)

t_start = time.time()

# ---------------------------------------------------------------- scene ----
def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.render.fps = 24
    scene.frame_start = 1
    scene.frame_end = 24
    scene.unit_settings.system = 'METRIC'
    scene.unit_settings.length_unit = 'METERS'
    return scene

def add_sphere(name, loc):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16,
                                         radius=1.0, location=loc)
    ob = bpy.context.active_object
    ob.name = name
    mat = bpy.data.materials.new(name + "Mat")
    mat.diffuse_color = (0.8, 0.15, 0.15, 1.0)   # sheet: red debug proxy
    ob.data.materials.append(mat)
    return ob

def strand_points(growth=1.0):
    """Deterministic path draped over the unit sphere at origin.
    Returns list of (x, y, z) on/near the sphere surface (y = front)."""
    pts = []
    # Arc over the crown: parametrize by angle a from -70deg..+80deg in the
    # x/z plane at y = +0.55 (front band), radius slightly above surface.
    import math as m
    for i in range(9):
        a = m.radians(-70 + i * (150.0 / 8.0))
        r = 1.02
        pts.append((r * m.sin(a), 0.55, r * m.cos(a)))
    # Drip: from the last arc point, descend the front face; length scales
    # with `growth` (the animation parameter).
    base = pts[-1]
    drip_len = 0.9 * growth
    steps = 4
    for i in range(1, steps + 1):
        f = i / steps
        z = base[2] - drip_len * f
        # stay near the surface while |z| allows, then fall straight
        y = 0.55 - 0.18 * f
        pts.append((base[0], y, z))
    return pts

def bridge_points():
    """Second path: from sphere A crown across the gap to sphere B
    (sphere B centre x=+2.6). Sheet C-11: one curve spanning both."""
    import math as m
    pts = []
    for i in range(7):
        f = i / 6.0
        x = 0.4 + f * 2.2
        z = 1.0 + 0.25 * m.sin(f * m.pi) - 0.55 * f
        pts.append((x, 0.35, z))
    return pts

def make_curve(name, pts):
    cu = bpy.data.curves.new(name, 'CURVE')
    cu.dimensions = '3D'
    cu.fill_mode = 'FULL'
    cu.resolution_u = 12
    sp = cu.splines.new('BEZIER')
    sp.bezier_points.add(len(pts) - 1)
    for bp, co in zip(sp.bezier_points, pts):
        bp.co = (co[0], co[1], co[2])
        bp.handle_left_type = 'AUTO'
        bp.handle_right_type = 'AUTO'
    ob = bpy.data.objects.new(name, cu)
    bpy.context.collection.objects.link(ob)
    return ob

# ------------------------------------------------------------- GN group ----
def build_group():
    ng = bpy.data.node_groups.new("NS09_Strand", 'GeometryNodeTree')
    ng.interface.new_socket("Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    ng.interface.new_socket("Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    rad = ng.interface.new_socket("Radius", in_out='INPUT', socket_type='NodeSocketFloat')
    rad.default_value = 0.1
    res = ng.interface.new_socket("Resolution", in_out='INPUT', socket_type='NodeSocketFloat')
    res.default_value = 2.0
    nodes, links = ng.nodes, ng.links
    gin = nodes.new('NodeGroupInput'); gin.location = (-900, 0)
    gout = nodes.new('NodeGroupOutput'); gout.location = (700, 0)
    c2p = nodes.new('GeometryNodeCurveToPoints'); c2p.location = (-650, 0)
    p2v = nodes.new('GeometryNodePointsToVolume'); p2v.location = (-350, 0)
    p2v.inputs['Density'].default_value = 1.0
    div = nodes.new('ShaderNodeMath'); div.location = (-650, -300)
    div.operation = 'DIVIDE'
    links.new(gin.outputs['Radius'], div.inputs[0])
    links.new(gin.outputs['Resolution'], div.inputs[1])
    links.new(div.outputs['Value'], p2v.inputs['Voxel Size'])
    links.new(gin.outputs['Radius'], p2v.inputs['Radius'])
    v2m = nodes.new('GeometryNodeVolumeToMesh'); v2m.location = (-50, 0)
    v2m.inputs['Threshold'].default_value = 0.1
    v2m.inputs['Adaptivity'].default_value = 0.0
    sss = nodes.new('GeometryNodeSetShadeSmooth'); sss.location = (200, 0)
    sss.domain = 'FACE'
    smat = nodes.new('GeometryNodeSetMaterial'); smat.location = (450, 0)
    mat = bpy.data.materials.get("M_ShowerGel")
    smat.inputs['Material'].default_value = mat
    links.new(gin.outputs['Geometry'], c2p.inputs['Curve'])
    links.new(c2p.outputs['Points'], p2v.inputs['Points'])
    links.new(p2v.outputs['Volume'], v2m.inputs['Volume'])
    links.new(v2m.outputs['Mesh'], sss.inputs['Mesh'])
    links.new(sss.outputs['Mesh'], smat.inputs['Geometry'])
    links.new(smat.outputs['Geometry'], gout.inputs['Geometry'])
    return ng, c2p, p2v

def shower_gel():
    mat = bpy.data.materials.new("M_ShowerGel")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.0, 1.0, 0.0, 1.0)  # debug green
    bsdf.inputs['Roughness'].default_value = 0.5
    bsdf.inputs['IOR'].default_value = 1.5
    bsdf.inputs['Alpha'].default_value = 1.0
    mat.diffuse_color = (0.0, 1.0, 0.0, 1.0)
    return mat

# ------------------------------------------------------------ rendering ----
def setup_render(scene):
    scene.render.engine = 'BLENDER_WORKBENCH'
    scene.display.shading.light = 'STUDIO'
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.display.shading.cavity_type = 'WORLD'
    scene.render.resolution_x = 960
    scene.render.resolution_y = 540
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.image_settings.compression = 15
    scene.render.use_file_extension = True
    scene.render.threads_mode = 'FIXED'
    scene.render.threads = 4
    bpy.ops.object.camera_add(location=(3.4, -4.6, 2.2))
    cam = bpy.context.active_object
    import mathutils
    direction = mathutils.Vector((0.5, 0.0, 0.2)) - cam.location
    cam.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()
    cam.data.lens = 40
    scene.camera = cam
    bpy.ops.object.light_add(type='SUN', location=(4, -3, 9))
    bpy.context.active_object.data.energy = 3.0

def evaluated_counts(ob):
    dg = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(dg)
    me = ev.to_mesh()
    n = len(me.vertices)
    ev.to_mesh_clear()
    return n

def set_group_inputs(mod, ng, radius, resolution):
    """Set Radius/Resolution on a NODES modifier.
    Blender 5.2 API (probed on primo, see PASS3-REBUILD.md): IDProperties are
    unsupported on NodesModifier; inputs live at
    mod.properties.inputs.<identifier>.value, identifiers from the interface."""
    vals = {"Radius": radius, "Resolution": resolution}
    for item in ng.interface.items_tree:
        if getattr(item, 'in_out', None) == 'INPUT' and item.name in vals:
            holder = getattr(mod.properties.inputs, item.identifier)
            holder.value = vals[item.name]


def build_variant(name, mode, radius, resolution, curve_pts_list,
                  smooth_mod=False):
    scene = reset_scene()
    shower_gel()
    add_sphere("Sphere", (0.0, 0.0, 0.0))
    add_sphere("Sphere.001", (2.6, 0.0, 0.0))
    ng, c2p, p2v = build_group()
    results = {}
    for ci, pts in enumerate(curve_pts_list):
        cu_ob = make_curve("%s_Curve%d" % (name, ci), pts)
        mod = cu_ob.modifiers.new("GeometryNodes", 'NODES')
        mod.node_group = ng
        set_group_inputs(mod, ng, radius, resolution)
        if mode == 'count10':
            c2p.mode = 'COUNT'
            c2p.inputs['Count'].default_value = 10
            p2v.inputs['Resolution Mode'].default_value = 'Amount'
            p2v.inputs['Voxel Amount'].default_value = 64.0
            p2v.inputs['Radius'].default_value = radius
        elif mode == 'count100':
            c2p.mode = 'COUNT'
            c2p.inputs['Count'].default_value = 100
            p2v.inputs['Resolution Mode'].default_value = 'Amount'
            p2v.inputs['Voxel Amount'].default_value = 64.0
            p2v.inputs['Radius'].default_value = radius
        elif mode == 'final':
            c2p.mode = 'LENGTH'
            c2p.inputs['Length'].default_value = 0.001
            p2v.inputs['Resolution Mode'].default_value = 'Size'
            # voxel size = radius / resolution (sheet C-05, Divide node)
            p2v.inputs['Voxel Size'].default_value = radius / resolution
            p2v.inputs['Radius'].default_value = radius
        if smooth_mod:
            sm = cu_ob.modifiers.new("Smooth", 'SMOOTH')
            sm.factor = 1.5
            sm.iterations = 20
        bpy.context.view_layer.objects.active = cu_ob
        results[cu_ob.name] = evaluated_counts(cu_ob)
    setup_render(scene)
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(outdir, name + ".blend"))
    scene.render.filepath = os.path.join(outdir, "renders", name + ".png")
    bpy.ops.render.render(write_still=True)
    return results

record = {"blender_version": bpy.app.version_string, "variants": {}}

# Two draped curves on sphere A + one bridge curve (sheet two-sphere stage).
all_pts = [strand_points(1.0), bridge_points()]
record["variants"]["v1_firstform"] = build_variant(
    "v1_firstform", 'count10', 0.5, 2.0, [strand_points(1.0)])
record["variants"]["v2_lumps"] = build_variant(
    "v2_lumps", 'count100', 0.25, 2.0, [strand_points(1.0)])
record["variants"]["v3_final"] = build_variant(
    "v3_final", 'final', 0.100, 2.0, all_pts, smooth_mod=True)
record["variants"]["v4_bodyradius"] = build_variant(
    "v4_bodyradius", 'final', 0.025, 2.0, all_pts, smooth_mod=True)

# --------------------------------------------------- animation probe (v3) --
# Estate-side motion mechanism: same curve, drip grown by re-authoring the
# path (curve shape states). Renders f01 (growth 0.15), f12 (0.55), f24 (1.0)
# of the v3 configuration to prove per-frame re-evaluation with no bake.
scene = reset_scene()
shower_gel()
add_sphere("Sphere", (0.0, 0.0, 0.0))
add_sphere("Sphere.001", (2.6, 0.0, 0.0))
ng, c2p, p2v = build_group()
c2p.mode = 'LENGTH'
c2p.inputs['Length'].default_value = 0.001
p2v.inputs['Resolution Mode'].default_value = 'Size'
p2v.inputs['Voxel Size'].default_value = 0.100 / 2.0
p2v.inputs['Radius'].default_value = 0.100
setup_render(scene)
anim_counts = {}
for label, growth in (("f01", 0.15), ("f12", 0.55), ("f24", 1.0)):
    cu_ob = make_curve("AnimCurve_" + label, strand_points(growth))
    mod = cu_ob.modifiers.new("GeometryNodes", 'NODES')
    mod.node_group = ng
    set_group_inputs(mod, ng, 0.100, 2.0)
    sm = cu_ob.modifiers.new("Smooth", 'SMOOTH')
    sm.factor = 1.5
    sm.iterations = 20
    anim_counts[label] = evaluated_counts(cu_ob)
    scene.render.filepath = os.path.join(outdir, "renders", "anim_" + label + ".png")
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(cu_ob, do_unlink=True)
record["anim_probe_counts"] = anim_counts

with open(os.path.abspath(__file__), 'rb') as fh:
    record["script_sha256"] = hashlib.sha256(fh.read()).hexdigest()
record["wall_seconds"] = round(time.time() - t_start, 2)
with open(os.path.join(outdir, "run_record.json"), "w") as fh:
    json.dump(record, fh, indent=2)
print("NS09 BUILD DONE", json.dumps(record["variants"]), "anim", anim_counts,
      "wall", record["wall_seconds"])
