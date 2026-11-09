"""Plan 23 core: PillowSquish group build + test scene + measures.

Faithful to TECHNIQUE.md (the sheet): Object Info (Relative) ->
Geometry Proximity (Faces) -> Map Range (Float/Linear/Clamp) ->
Color Ramp -> Combine XYZ (Z only) -> Set Position.
Estate adaptation (per sheet): Collider + Map Range window are
group inputs; ramp stays internal (stops are not socket-drivable)
and is set from the parameter vector.
"""
import bpy
import bmesh
import hashlib
import math
from mathutils import Vector

DEMO = dict(from_min=-2.100, from_max=1.000, to_min=0.500, to_max=0.900,
            ramp_start=0.714, ramp_end=0.982,
            press=0.06, seg=16, thick=0.25, width=1.20, depth=0.80,
            collider_r=0.30, collider_zs=0.62)


def clean_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def make_cushion(p):
    """Closed box, `seg` segments per edge, bottom at z=0, centred x/y."""
    mesh = bpy.data.meshes.new("CushionMesh")
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector((v.co.x * p['width'], v.co.y * p['depth'],
                       v.co.z * p['thick'] + p['thick'] / 2.0))
    bm.edges.ensure_lookup_table()
    bmesh.ops.subdivide_edges(bm, edges=list(bm.edges),
                              cuts=p['seg'] - 1, use_grid_fill=True)
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new("Cushion", mesh)
    bpy.context.collection.objects.link(obj)
    return obj


def make_collider(p):
    """Squashed sphere 'sitter' proxy; lowest point pressed `press`
    metres below the cushion top plane."""
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=48, ring_count=32, radius=p['collider_r'],
        location=(0.0, 0.0, 0.0))
    obj = bpy.context.active_object
    obj.name = "Collider"
    obj.scale = (1.0, 1.0, p['collider_zs'])
    cz = p['thick'] - p['press'] + p['collider_r'] * p['collider_zs']
    obj.location = (0.0, 0.0, cz)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.location = (0.0, 0.0, cz)
    return obj


def build_group(p, name="PillowSquish", collider_default=None):
    ng = bpy.data.node_groups.new(name, 'GeometryNodeTree')
    ng.interface.new_socket('Geometry', in_out='INPUT',
                            socket_type='NodeSocketGeometry')
    csock = ng.interface.new_socket('Collider', in_out='INPUT',
                                    socket_type='NodeSocketObject')
    if collider_default is not None:
        # Blender 5.2: NodesModifier rejects ID-property writes
        # ("id properties not supported for this type"); the
        # supported route is the interface socket's default.
        csock.default_value = collider_default
    for nm, key in (('From Min', 'from_min'), ('From Max', 'from_max'),
                    ('To Min', 'to_min'), ('To Max', 'to_max')):
        s = ng.interface.new_socket(nm, in_out='INPUT',
                                    socket_type='NodeSocketFloat')
        s.default_value = float(p[key])
    ng.interface.new_socket('Geometry', in_out='OUTPUT',
                            socket_type='NodeSocketGeometry')
    n = ng.nodes
    gin = n.new('NodeGroupInput')
    gout = n.new('NodeGroupOutput')
    setpos = n.new('GeometryNodeSetPosition')
    oi = n.new('GeometryNodeObjectInfo')
    oi.transform_space = 'RELATIVE'
    prox = n.new('GeometryNodeProximity')
    prox.target_element = 'FACES'
    mr = n.new('ShaderNodeMapRange')
    mr.data_type = 'FLOAT'
    mr.interpolation_type = 'LINEAR'
    mr.clamp = True
    ramp = n.new('ShaderNodeValToRGB')
    ramp.color_ramp.interpolation = 'LINEAR'
    el = ramp.color_ramp.elements
    el[0].position = float(p['ramp_start'])
    el[0].color = (0.0, 0.0, 0.0, 1.0)
    el[1].position = float(p['ramp_end'])
    el[1].color = (1.0, 1.0, 1.0, 1.0)
    comb = n.new('ShaderNodeCombineXYZ')
    comb.inputs['X'].default_value = 0.0
    comb.inputs['Y'].default_value = 0.0
    L = ng.links
    L.new(gin.outputs['Geometry'], setpos.inputs['Geometry'])
    L.new(setpos.outputs['Geometry'], gout.inputs['Geometry'])
    L.new(gin.outputs['Collider'], oi.inputs['Object'])
    L.new(oi.outputs['Geometry'], prox.inputs['Geometry'])
    L.new(prox.outputs['Distance'], mr.inputs['Value'])
    for nm in ('From Min', 'From Max', 'To Min', 'To Max'):
        L.new(gin.outputs[nm], mr.inputs[nm])
    L.new(mr.outputs['Result'], ramp.inputs['Fac'])
    L.new(ramp.outputs['Color'], comb.inputs['Z'])
    L.new(comb.outputs['Vector'], setpos.inputs['Offset'])
    return ng


def apply_group(cushion, ng):
    mod = cushion.modifiers.new('PillowSquish', 'NODES')
    mod.node_group = ng
    return mod


def build_scene(p):
    clean_scene()
    cushion = make_cushion(p)
    collider = make_collider(p)
    ng = build_group(p, collider_default=collider)
    apply_group(cushion, ng)
    return cushion, collider, ng


def measure(cushion, collider, p):
    """Evaluate and measure. Returns dict of plain floats/ints."""
    dg = bpy.context.evaluated_depsgraph_get()
    ev = cushion.evaluated_get(dg)
    me = ev.to_mesh()
    rest = [v.co.copy() for v in cushion.data.vertices]
    verts = [v.co.copy() for v in me.vertices]
    assert len(verts) == len(rest), "vertex count changed by GN"
    nan_count = sum(1 for v in verts
                    if any(math.isnan(c) or math.isinf(c) for c in v))
    xs = [v.x for v in verts]; ys = [v.y for v in verts]; zs = [v.z for v in verts]
    bbox = (max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs)) \
        if not nan_count else (float('nan'),) * 3
    H = p['thick']
    top_idx = [i for i, r in enumerate(rest) if r.z > H - 1e-6]
    bot_idx = [i for i, r in enumerate(rest) if r.z < 1e-6]
    cz = p['thick'] - p['press'] + p['collider_r'] * p['collider_zs']

    def hdist(i):
        return math.hypot(rest[i].x, rest[i].y)

    contact = [verts[i].z for i in top_idx if hdist(i) <= 0.30]
    far = [verts[i].z for i in top_idx if hdist(i) >= 0.50]
    contact_min = min(contact) if contact else float('nan')
    contact_mean = sum(contact) / len(contact) if contact else float('nan')
    apex = max(far) if far else float('nan')
    dent = apex - contact_min
    bottom_max = max((verts[i].z for i in bot_idx), default=float('nan'))
    # Inversion is a PER-COLUMN test: a bottom vert crossing the top
    # vert of its own (x, y) column. (A global bottom-vs-top test
    # false-fires at demo settings: far bottom corners legitimately
    # lift above the pressed contact patch — measured on run A.)
    col_top = {}
    col_bot = {}
    for i in top_idx:
        col_top[(round(rest[i].x, 5), round(rest[i].y, 5))] = verts[i].z
    for i in bot_idx:
        col_bot[(round(rest[i].x, 5), round(rest[i].y, 5))] = verts[i].z
    inverted_cols = sum(1 for k, bz in col_bot.items()
                        if k in col_top and bz >= col_top[k] - 1e-4)
    inversion = inverted_cols > 0 or nan_count > 0
    col_thick = [col_top[k] - bz for k, bz in col_bot.items() if k in col_top]
    min_thickness = min(col_thick) if col_thick else float('nan')
    # Poke: how far the collider's lowest point sinks below the
    # lifted contact surface (visible interpenetration). Negative
    # or zero = the surface rose to meet / clear the collider.
    contact_lift = contact_mean - H
    poke = max(0.0, p['press'] - contact_lift) if contact else 0.0
    # penetration: cushion verts inside collider ellipsoid
    R = p['collider_r']; zs_ = p['collider_zs']
    pen = 0
    for v in verts:
        q = (v.x / R) ** 2 + (v.y / R) ** 2 + ((v.z - cz) / (R * zs_)) ** 2
        if q < 1.0:
            pen += 1
    # topology on evaluated mesh
    bm = bmesh.new()
    bm.from_mesh(me)
    nonmanifold = sum(1 for e in bm.edges if len(e.link_faces) != 2)
    degen = sum(1 for f in bm.faces if f.calc_area() < 1e-10)
    # flipped: face normal vs rest face normal (same indexing)
    rest_normals = [tuple(f.normal) for f in cushion.data.polygons]
    flipped = 0
    for i, f in enumerate(bm.faces):
        rn = rest_normals[i]
        if f.normal.dot(Vector(rn)) < 0:
            flipped += 1
    nfaces = len(bm.faces)
    bm.free()
    ev.to_mesh_clear()
    # deterministic hash of evaluated verts at 1e-6
    h = hashlib.sha256()
    for v in verts:
        h.update(("%.6f,%.6f,%.6f;" % (v.x, v.y, v.z)).encode())
    return dict(verts=len(verts), faces=nfaces, nan=nan_count,
                bbox=[round(float(b), 6) for b in bbox],
                contact_min_z=round(float(contact_min), 6),
                contact_mean_z=round(float(contact_mean), 6),
                apex_z=round(float(apex), 6),
                dent_depth=round(float(dent), 6),
                bottom_max_z=round(float(bottom_max), 6),
                inversion=bool(inversion),
                inverted_columns=int(inverted_cols),
                min_thickness=round(float(min_thickness), 6),
                thick_ratio=round(float(min_thickness) / H, 6) if H else 0.0,
                contact_lift=round(float(contact_lift), 6),
                poke_depth=round(float(poke), 6),
                penetration_verts=int(pen),
                nonmanifold=int(nonmanifold), degenerate=int(degen),
                flipped=int(flipped), vert_hash=h.hexdigest())


def setup_render(scene, out_path, res=640):
    scene.render.engine = 'BLENDER_WORKBENCH'
    scene.display.shading.light = 'STUDIO'
    scene.display.shading.color_type = 'OBJECT'
    scene.display.shading.show_cavity = True
    scene.render.resolution_x = res
    scene.render.resolution_y = int(res * 0.75)
    scene.render.filepath = out_path
    cam_data = bpy.data.cameras.new("Cam")
    cam = bpy.data.objects.new("Cam", cam_data)
    scene.collection.objects.link(cam)
    cam.location = (1.7, -2.0, 1.45)
    cam.rotation_euler = (Vector((0.0, 0.0, 0.12)) - cam.location).to_track_quat('-Z', 'Y').to_euler()
    cam_data.lens = 50
    scene.camera = cam
    return cam


def classify(m, base_faces):
    """Classification rules, Revision 1 (PASS3-REBUILD.md records
    the pre-registered rules and why two changed):
    - The penetration-count rule was REMOVED: it counts verts in
      the contact patch, i.e. it measures the mechanism working;
      the video's own demo settings "failed" it (126 > 2% of
      1538), which falsifies the rule, not the demo.
    - Added poke (collider sinks below the lifted surface) and
      over-inflation (contact lift > 0.60 m) as strain signals.
    CLIFF = breaks, DEGRADED = strained/absent, SAFE = holds."""
    if m['nan'] > 0 or m['inversion'] or m['nonmanifold'] > 0:
        return 'CLIFF'
    if m['degenerate'] > 0.005 * base_faces:
        return 'CLIFF'
    if m['dent_depth'] < 0.02 or m['dent_depth'] > 0.75:
        return 'DEGRADED'
    if m.get('thick_ratio', 1.0) < 0.30:
        return 'DEGRADED'
    if m.get('poke_depth', 0.0) > 0.02:
        return 'DEGRADED'
    if m.get('contact_lift', 0.0) > 0.60:
        return 'DEGRADED'
    if m['flipped'] > 0:
        return 'DEGRADED'
    return 'SAFE'
