# nslac_measure.py - post-bake measurement for the lactation module
# Per frame: particle count, mesh verts/islands/bbox, interior count vs the
# girl's real Body mesh (two-axis ray parity, Plan 06 route), particle
# kinematics (centroid, mean velocity), cone angle about the carrier axis,
# landing count (particles below z=0.03), emitter-clearance stats.
# Usage: blender -b -Y -noaudio --python nslac_measure.py -- <baked_blend>
#        <body_name> <out_json> <frames_csv> <emitter_json>
# emitter_json: {"L":[x,y,z],"R":[x,y,z],"vel":[x,y,z]}
import bpy, sys, os, json, math
from mathutils import Vector
from mathutils.bvhtree import BVHTree

argv = sys.argv[sys.argv.index("--") + 1:]
blend_path, body_name, out_json, frames_csv, emitter_json = argv[:5]
frames = [int(x) for x in frames_csv.split(",") if x]
EM = json.loads(emitter_json)
origins = [Vector(EM["L"]), Vector(EM["R"])]
axis = Vector(EM["vel"]).normalized()

bpy.ops.wm.open_mainfile(filepath=blend_path)
scene = bpy.context.scene
dom = bpy.data.objects["NSLAC_Domain"]
body = bpy.data.objects[body_name]

def crossings(tree, origin, direction, max_hits=10):
    n = 0; o = Vector(origin)
    for _ in range(max_hits):
        loc, nrm, idx, dist = tree.ray_cast(o, direction)
        if loc is None: break
        n += 1; o = loc + direction * 1e-5
    return n

def inside(tree, p):
    return (crossings(tree, p, Vector((1, 0, 0))) % 2 == 1 and
            crossings(tree, p, Vector((0, 0, -1))) % 2 == 1)

out = {"frames": {}}
for f in frames:
    scene.frame_set(f)
    dg = bpy.context.evaluated_depsgraph_get()
    ev = dom.evaluated_get(dg)
    me = ev.to_mesh()
    mw = ev.matrix_world
    verts = [mw @ v.co for v in me.vertices]
    bbox = None
    if verts:
        bbox = [[round(min(v[i] for v in verts), 4),
                 round(max(v[i] for v in verts), 4)] for i in range(3)]
    islands = None
    if 0 < len(verts) <= 400000:
        parent = list(range(len(verts)))
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]; a = parent[a]
            return a
        for e in me.edges:
            ra, rb = find(e.vertices[0]), find(e.vertices[1])
            if ra != rb: parent[ra] = rb
        islands = len({find(i) for i in range(len(verts))})
    ev.to_mesh_clear()
    pts, vels = [], []
    for ps in ev.particle_systems:
        for p in ps.particles:
            if p.is_exist:
                # Mantaflow FLIP particle locations are WORLD-space in this
                # route (verified vs emitter landmark, probe round 1:
                # mw @ location double-counts the domain translation).
                pts.append(Vector(p.location))
                vels.append(Vector(p.velocity))
    rec = {"mesh_verts": len(verts), "mesh_islands": islands,
           "mesh_bbox": bbox, "particles": len(pts)}
    if pts:
        cen = sum(pts, Vector()) / len(pts)
        mv = sum(vels, Vector()) / len(vels)
        rec["centroid"] = [round(v, 4) for v in cen]
        rec["mean_vel"] = [round(v, 4) for v in mv]
        rec["mean_speed"] = round(mv.length, 4)
        angs = []
        young = []
        for p, v in zip(pts, vels):
            o = min(origins, key=lambda q: (p - q).length)
            d = p - o
            if d.length > 0.03:
                angs.append(math.degrees(d.angle(axis)))
            if d.length < 0.15 and v.length > 0.05:
                young.append((d, v))
        angs.sort()
        if angs:
            rec["cone_p90_deg"] = round(angs[int(0.9 * (len(angs) - 1))], 2)
            rec["cone_max_deg"] = round(angs[-1], 2)
            rec["cone_n"] = len(angs)
        if young:
            yv = sum((v for _, v in young), Vector()) / len(young)
            rec["young_mean_vel"] = [round(v, 4) for v in yv]
            rec["young_n"] = len(young)
            vangs = sorted(math.degrees(v.angle(axis)) for _, v in young
                           if v.length > 0.05)
            if vangs:
                rec["vcone_p90_deg"] = round(
                    vangs[int(0.9 * (len(vangs) - 1))], 2)
                rec["vcone_n"] = len(vangs)
        rec["landed_z_lt_0.03"] = sum(1 for p in pts if p.z < 0.03)
        rec["fwd_y_lt_-0.30"] = sum(1 for p in pts if p.y < -0.30)
    # interior vs the real body mesh at this frame
    bev = body.evaluated_get(dg)
    bme = bev.to_mesh()
    bverts = [bev.matrix_world @ v.co for v in bme.vertices]
    bpolys = [tuple(p.vertices) for p in bme.polygons]
    tree = BVHTree.FromPolygons([tuple(v) for v in bverts], bpolys)
    lo = [min(v[i] for v in bverts) - 0.005 for i in range(3)]
    hi = [max(v[i] for v in bverts) + 0.005 for i in range(3)]
    cand = [p for p in pts if all(lo[i] <= p[i] <= hi[i] for i in range(3))]
    rec["interior"] = sum(1 for p in cand if inside(tree, p))
    rec["interior_candidates"] = len(cand)
    bev.to_mesh_clear()
    out["frames"][str(f)] = rec
    print("NSLAC MEASURE", f, json.dumps(rec))
with open(out_json, "w") as fh:
    json.dump(out, fh, indent=2)
print("NSLAC MEASURE DONE")
