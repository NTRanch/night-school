# Plan 28 Pass 3 -- bend test v2: corridor-ladder measures + seam measures.
import bpy, json, math, os, sys
from mathutils import Vector
from collections import defaultdict

OUT = sys.argv[sys.argv.index("--") + 1]
REC = json.load(open(os.path.join(OUT, "build_record.json")))
CUT = REC["cut_prima"]
bpy.ops.wm.open_mainfile(filepath=os.path.join(OUT, "headhack_both.blend"))
arm = bpy.data.objects["Armature"]
mA = bpy.data.objects["MethodA_Theirs"]
mB = bpy.data.objects["MethodB_Estate"]
offA = REC["body_part_verts"]
dg = bpy.context.evaluated_depsgraph_get()

POSES = {
    "rest":      {"mixamorig:Neck": (0,0,0),   "mixamorig:Head": (0,0,0)},
    "flexion":   {"mixamorig:Neck": (25,0,0),  "mixamorig:Head": (20,0,0)},
    "extension": {"mixamorig:Neck": (-18,0,0), "mixamorig:Head": (-12,0,0)},
    "yaw":       {"mixamorig:Neck": (0,30,0),  "mixamorig:Head": (0,20,0)},
    "lateral":   {"mixamorig:Neck": (0,0,15),  "mixamorig:Head": (0,0,12)},
}
def set_pose(p):
    for pb in arm.pose.bones:
        pb.rotation_mode = 'XYZ'; pb.rotation_euler = (0,0,0)
    for bn, (x,y,z) in p.items():
        arm.pose.bones[bn].rotation_euler = (math.radians(x), math.radians(y), math.radians(z))
    bpy.context.view_layer.update()

def evaluated(ob):
    return bpy.data.meshes.new_from_object(ob.evaluated_get(dg), depsgraph=dg)

# corridor bins: 3 mm bins from CUT-30mm to CUT+48mm, defined at REST per method
BIN0, BINW, NBIN = CUT - 0.030, 0.003, 26
def bin_of(z): return int((z - BIN0) // BINW)
def build_bins(me, head_pred):
    bins = defaultdict(list)
    for v in me.vertices:
        if BIN0 <= v.co.z < BIN0 + BINW * NBIN and head_pred(v.index):
            bins[bin_of(v.co.z)].append(v.index)
    return {k: v for k, v in bins.items() if len(v) >= 4}
def bin_stats(me, bins):
    out = {}
    for k, idxs in bins.items():
        cs = [me.vertices[i].co for i in idxs]
        cen = sum(cs, Vector((0,0,0))) / len(cs)
        r = sum(math.hypot(c.x - cen.x, c.y - cen.y) for c in cs) / len(cs)
        ns = [me.vertices[i].normal for i in idxs]
        nmean = sum(ns, Vector((0,0,0)))
        out[k] = (cen, r, nmean.normalized() if nmean.length > 0 else Vector((0,0,1)))
    return out
def ladder(stats_rest, stats_pose):
    ks = sorted(set(stats_rest) & set(stats_pose))
    kink, kink_z, rstep = 0.0, None, 0.0
    nstep, nstep_z = 0.0, None
    for a, b in zip(ks, ks[1:]):
        dr = (stats_rest[b][0] - stats_rest[a][0]); dp = (stats_pose[b][0] - stats_pose[a][0])
        d = (dp - dr).length * 1000
        if d > kink: kink, kink_z = d, round(BIN0 + b * BINW, 3)
        rr = abs((stats_pose[b][1] - stats_pose[a][1]) - (stats_rest[b][1] - stats_rest[a][1])) * 1000
        rstep = max(rstep, rr)
        na, nb = stats_rest[a][2], stats_rest[b][2]
        pa, pb = stats_pose[a][2], stats_pose[b][2]
        ang_r = math.degrees(math.acos(max(-1, min(1, na.dot(nb)))))
        ang_p = math.degrees(math.acos(max(-1, min(1, pa.dot(pb)))))
        if abs(ang_p - ang_r) > nstep: nstep, nstep_z = abs(ang_p - ang_r), round(BIN0 + b * BINW, 3)
    return {"kink_max_mm": round(kink, 3), "kink_at_z": kink_z,
            "radius_step_max_mm": round(rstep, 3),
            "normal_step_change_max_deg": round(nstep, 2), "normal_step_at_z": nstep_z}

set_pose(POSES["rest"])
meA0 = evaluated(mA); meB0 = evaluated(mB)
binsA_body = build_bins(meA0, lambda i: i < offA)
binsA_head = build_bins(meA0, lambda i: i >= offA)
binsB_all  = build_bins(meB0, lambda i: True)
rest_stats = {"A_body": bin_stats(meA0, binsA_body), "A_head": bin_stats(meA0, binsA_head),
              "B": bin_stats(meB0, binsB_all)}
pairsA = REC["pairsA"]
rest_pairsA = [(meA0.vertices[a].co - meA0.vertices[b].co).length * 1000 for a, b in pairsA]
# B weld edges: edges incident to weld verts (by recorded positions)
weld_idx = []
for wp in REC["weld_positions"]:
    w = Vector(wp); best, bd = None, 1e9
    for v in meB0.vertices:
        d = (v.co - w).length
        if d < bd: bd, best = d, v.index
    if bd < 0.001: weld_idx.append(best)
weld_edges = set()
for e in meB0.edges:
    if e.vertices[0] in weld_idx or e.vertices[1] in weld_idx:
        weld_edges.add((e.vertices[0], e.vertices[1]))
weld_edges = sorted(weld_edges)
rest_weld = [(meB0.vertices[a].co - meB0.vertices[b].co).length * 1000 for a, b in weld_edges]
# Method A weld verts/edges (same ring positions after snap+weld)
weld_idx_A = []
for wp in REC["weld_positions"]:
    w = Vector(wp); best, bd = None, 1e9
    for v in meA0.vertices:
        d = (v.co - w).length
        if d < bd: bd, best = d, v.index
    if bd < 0.001: weld_idx_A.append(best)
adjA0 = defaultdict(set)
for e in meA0.edges:
    adjA0[e.vertices[0]].add(e.vertices[1]); adjA0[e.vertices[1]].add(e.vertices[0])
weld_edges_A = set()
for wi in weld_idx_A:
    for nb in adjA0[wi]:
        weld_edges_A.add((min(wi, nb), max(wi, nb)))
weld_edges_A = sorted(weld_edges_A)
rest_weld_A = [(meA0.vertices[a].co - meA0.vertices[b].co).length * 1000 for a, b in weld_edges_A]
bpy.data.meshes.remove(meA0); bpy.data.meshes.remove(meB0)

def axis_tilt():
    m = arm.pose.bones["mixamorig:Head"].matrix
    origin = m @ Vector((0,0,0))
    ay = (m @ Vector((0,1,0)) - origin).normalized()
    ax = (m @ Vector((1,0,0)) - origin).normalized()
    return ay, ax
results = {"bins": {"A_body": len(binsA_body), "A_head": len(binsA_head), "B": len(binsB_all)},
           "pairsA": len(pairsA), "weld_edges": len(weld_edges), "weld_edges_A": len(weld_edges_A), "poses": {}}
set_pose(POSES["rest"]); ref_y, ref_x = axis_tilt()
for name, pose in POSES.items():
    set_pose(pose)
    ay, ax = axis_tilt()
    tilt_y = math.degrees(math.acos(max(-1, min(1, ref_y.dot(ay)))))
    tilt_x = math.degrees(math.acos(max(-1, min(1, ref_x.dot(ax)))))
    meA = evaluated(mA); meB = evaluated(mB)
    sA_b = bin_stats(meA, binsA_body); sA_h = bin_stats(meA, binsA_head); sB = bin_stats(meB, binsB_all)
    dA = [(meA.vertices[a].co - meA.vertices[b].co).length * 1000 for a, b in pairsA]
    wB = [(meB.vertices[a].co - meB.vertices[b].co).length * 1000 for a, b in weld_edges]
    strainB = [abs(x - r) for x, r in zip(wB, rest_weld)]
    wA = [(meA.vertices[a].co - meA.vertices[b].co).length * 1000 for a, b in weld_edges_A]
    strainA = [abs(x - r) for x, r in zip(wA, rest_weld_A)]
    entry = {"head_tilt_deg": round(max(tilt_y, tilt_x), 2),
             "A_body": ladder(rest_stats["A_body"], sA_b),
             "A_head": ladder(rest_stats["A_head"], sA_h),
             "B": ladder(rest_stats["B"], sB),
             "A_seam_pair_dist_max_mm": round(max(dA), 3),
             "A_seam_pair_dist_mean_mm": round(sum(dA)/len(dA), 3),
             "A_seam_pair_change_max_mm": round(max(abs(x - r) for x, r in zip(dA, rest_pairsA)), 3),
             "B_weld_strain_max_mm": round(max(strainB), 3),
             "B_weld_strain_mean_mm": round(sum(strainB)/len(strainB), 3),
             "A_weld_strain_max_mm": round(max(strainA), 3),
             "A_weld_strain_mean_mm": round(sum(strainA)/len(strainA), 3)}
    results["poses"][name] = entry
    print("POSE", name, json.dumps(entry))
    bpy.data.meshes.remove(meA); bpy.data.meshes.remove(meB)

# renders
sc = bpy.context.scene
sc.render.engine = 'BLENDER_WORKBENCH'
sc.display.shading.light = 'STUDIO'
sc.display.shading.color_type = 'SINGLE'
sc.display.shading.single_color = (0.75, 0.72, 0.70)
sc.render.resolution_x = 640; sc.render.resolution_y = 640
cam_data = bpy.data.cameras.new("cam"); cam = bpy.data.objects.new("cam", cam_data)
sc.collection.objects.link(cam); sc.camera = cam
neck_c = Vector((0, -0.01, CUT + 0.055))
def render(hide, view, path):
    for o in (mA, mB): o.hide_render = (o.name == hide)
    if view == "front": cam.location = neck_c + Vector((0.34, -0.52, 0.10))
    else: cam.location = neck_c + Vector((0.58, -0.06, 0.07))
    d = (neck_c - cam.location).normalized()
    cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    cam.data.lens = 50
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)
for name, pose in POSES.items():
    set_pose(pose)
    render("MethodB_Estate", "front", os.path.join(OUT, "renders", f"A_{name}_front.png"))
    render("MethodB_Estate", "side",  os.path.join(OUT, "renders", f"A_{name}_side.png"))
    render("MethodA_Theirs", "front", os.path.join(OUT, "renders", f"B_{name}_front.png"))
    render("MethodA_Theirs", "side",  os.path.join(OUT, "renders", f"B_{name}_side.png"))
set_pose(POSES["rest"])
with open(os.path.join(OUT, "measures.json"), "w") as f:
    json.dump(results, f, indent=1)
print("OK plan28-bend")
