# Plan 28 Pass 3 -- headhack rebuild v2: their method (A) vs estate method (B)
# Blender 5.2.3 headless, deterministic, vanilla bpy. Body meshes only.
# Donor pair: Alma head -> Prima body (copies; fleet untouched).
# A (theirs, distilled): delete body head band; donor head positioned by
#   translation only (no scale reconciliation), neck stump overlapping the
#   body by 6 mm; objects joined (Ctrl+J analogue, NO vertex merge);
#   boundary loops bridged with hand-fill triangles (F analogue); weights
#   repainted with the BODY rig's profile over the donor head (their
#   weight-paint step) + ONE Smooth Vertex Weights iteration (Factor 0.5,
#   the observed operator settings) on Neck/Head groups of head verts.
# B (estate): donor head scaled ring-exact (XY by ring ratio, Z by head-
#   height ratio), boundary ring snapped onto the body ring (max snap
#   recorded), welded (merge by distance 0.1 mm), seam weight field
#   re-derived from the body profile over the corridor, smooth normals
#   across the weld (shared verts).
import bpy, bmesh, json, math, os, sys
from mathutils import Vector

SRC = os.path.expanduser("~/.local/share/pax/night-school/plan-28/src")
OUT = sys.argv[sys.argv.index("--") + 1]
os.makedirs(os.path.join(OUT, "renders"), exist_ok=True)
CUT_P = 1.426
CUT_A = 1.573
OVERLAP = 0.006

bpy.ops.wm.read_factory_settings(use_empty=True)
with bpy.data.libraries.load(os.path.join(SRC, "prima.blend")) as (df, dt):
    dt.objects = [n for n in df.objects if n in ("Prima_Body", "Armature")]
with bpy.data.libraries.load(os.path.join(SRC, "alma.blend")) as (df, dt):
    dt.objects = [n for n in df.objects if n == "Alma_Body"]
for ob in list(bpy.data.objects):
    if ob.name in ("Prima_Body", "Armature", "Alma_Body"):
        bpy.context.scene.collection.objects.link(ob)
prima_body = bpy.data.objects["Prima_Body"]
alma_body = bpy.data.objects["Alma_Body"]
armature = bpy.data.objects["Armature"]
for ob in (prima_body, alma_body):
    for m in list(ob.modifiers):
        ob.modifiers.remove(m)

# Prima weight profile by z
prof = {}
for v in prima_body.data.vertices:
    z = round(v.co.z, 3)
    d = prof.setdefault(z, {})
    for g in v.groups:
        n = prima_body.vertex_groups[g.group].name
        a = d.setdefault(n, [0.0, 0]); a[0] += g.weight; a[1] += 1
profile = {z: {n: a[0]/a[1] for n, a in d.items()} for z, d in prof.items()}
zs_sorted = sorted(profile)
def profile_at(z):
    if z <= zs_sorted[0]: return profile[zs_sorted[0]]
    if z >= zs_sorted[-1]: return profile[zs_sorted[-1]]
    for i in range(len(zs_sorted) - 1):
        a, b = zs_sorted[i], zs_sorted[i+1]
        if a <= z <= b:
            t = 0 if b == a else (z - a) / (b - a)
            return {n: profile[a].get(n, 0) * (1 - t) + profile[b].get(n, 0) * t
                    for n in set(profile[a]) | set(profile[b])}
    return {}

def split_by_face_z(me, cut, keep_above):
    keep = []
    for p in me.polygons:
        zs = [me.vertices[i].co.z for i in p.vertices]
        if keep_above:
            if min(zs) >= cut - 0.002: keep.append(p.index)
        else:
            if max(zs) <= cut + 0.002: keep.append(p.index)
    bm = bmesh.new(); bm.from_mesh(me)
    bm.faces.ensure_lookup_table()
    drop = [f for f in bm.faces if f.index not in set(keep)]
    bmesh.ops.delete(bm, geom=drop, context='FACES')
    loose = [v for v in bm.verts if not v.link_faces]
    bmesh.ops.delete(bm, geom=loose, context='VERTS')
    out = bpy.data.meshes.new("part")
    bm.to_mesh(out); bm.free()
    return out

def boundary_loop(me, cut):
    bm = bmesh.new(); bm.from_mesh(me)
    verts = {}
    for e in bm.edges:
        if len(e.link_faces) == 1:
            for v in e.verts:
                if abs(v.co.z - cut) <= 0.02:
                    verts[v.index] = Vector(v.co)
    bm.free()
    cx = sum(v.x for v in verts.values()) / max(len(verts), 1)
    cy = sum(v.y for v in verts.values()) / max(len(verts), 1)
    loop = sorted(verts.items(), key=lambda kv: math.atan2(kv[1].y - cy, kv[1].x - cx))
    return loop, Vector((cx, cy, 0))

def split_part(src_ob, cut, keep_above, name):
    me = split_by_face_z(src_ob.data, cut, keep_above)
    ob = bpy.data.objects.new(name, me)
    bpy.context.scene.collection.objects.link(ob)
    for g in src_ob.vertex_groups:
        ob.vertex_groups.new(name=g.name)
    src_verts = src_ob.data.vertices
    for v in me.vertices:
        best, bd = None, 1e9
        for sv in src_verts:
            d = (sv.co - v.co).length
            if d < bd: bd, best = d, sv
        if bd < 0.0002:
            for g in best.groups:
                ob.vertex_groups[g.group].add([v.index], g.weight, 'REPLACE')
    return ob

body_part = split_part(prima_body, CUT_P, False, "BodyPart")
headA = split_part(alma_body, CUT_A, True, "HeadPartA")
headB = split_part(alma_body, CUT_A, True, "HeadPartB")
loopB, cenB = boundary_loop(body_part.data, CUT_P)
loopA, cenA = boundary_loop(headA.data, CUT_A)
ring_r_B = sum(math.hypot(v.x - cenB.x, v.y - cenB.y) for _, v in loopB) / len(loopB)
ring_r_A = sum(math.hypot(v.x - cenA.x, v.y - cenA.y) for _, v in loopA) / len(loopA)
head_top_A = max(v.co.z for v in headA.data.vertices)
head_top_P = max(v.co.z for v in prima_body.data.vertices if v.co.z > CUT_P)
rec = {"cut_prima": CUT_P, "cut_alma": CUT_A, "body_loop_verts": len(loopB),
       "head_loop_verts": len(loopA), "ring_r_body_mm": round(ring_r_B * 1000, 2),
       "ring_r_head_mm": round(ring_r_A * 1000, 2),
       "head_height_alma_mm": round((head_top_A - CUT_A) * 1000, 2),
       "head_height_prima_mm": round((head_top_P - CUT_P) * 1000, 2),
       "body_part_verts": len(body_part.data.vertices),
       "head_part_verts": len(headA.data.vertices)}

def join_meshes(dst_ob, src_ob):
    """Ctrl+J analogue: concatenated geometry + union of groups + weights."""
    W = {}
    for v in dst_ob.data.vertices:
        W[v.index] = {dst_ob.vertex_groups[g.group].name: g.weight for g in v.groups}
    off = len(dst_ob.data.vertices)
    for v in src_ob.data.vertices:
        W[off + v.index] = {src_ob.vertex_groups[g.group].name: g.weight for g in v.groups}
    dm, sm = dst_ob.data, src_ob.data
    verts = [tuple(v.co) for v in dm.vertices] + [tuple(v.co) for v in sm.vertices]
    faces = [tuple(p.vertices) for p in dm.polygons] + \
            [tuple(i + off for i in p.vertices) for p in sm.polygons]
    new = bpy.data.meshes.new(dst_ob.name + "_joined")
    new.from_pydata(verts, [], faces); new.update()
    names = [g.name for g in dst_ob.vertex_groups]
    for g in src_ob.vertex_groups:
        if g.name not in names: names.append(g.name)
    dst_ob.data = new
    for n in names: dst_ob.vertex_groups.new(name=n)
    for vi, wd in W.items():
        for n, w in wd.items():
            dst_ob.vertex_groups[n].add([vi], w, 'REPLACE')
    return W

def nearest_idx(mesh, co, maxd=0.012):
    best, bd = None, 1e9
    for v in mesh.vertices:
        d = (v.co - co).length
        if d < bd: bd, best = d, v.index
    return best if bd <= maxd else None

DEFORM = ["mixamorig:Spine2", "mixamorig:Neck", "mixamorig:Head",
          "mixamorig:LeftShoulder", "mixamorig:RightShoulder"]

# ---------------- METHOD A ----------------
# Their sequence (transcript-verified): ring planes made coincident, head
# ring verts snapped one-by-one onto the body ring (Snap Selection to
# Active analogue = exact per-vert snap), Ctrl+J, then Merge by Distance
# weld. NO global scale: donor proportions above the ring are kept; ring
# verts are dragged (radial mismatch 52.51 -> 48.02 mm absorbed AT the ring).
dzA = CUT_P - CUT_A
for v in headA.data.vertices: v.co.z += dzA
headA.data.update()
loopA_shift = [(i, Vector((v.x, v.y, v.z + dzA))) for i, v in loopA]
snapA_max = 0.0
for hi, hv in loopA_shift:
    ang = math.atan2(hv.y - cenB.y, hv.x - cenB.x)
    bi, bv = min(loopB, key=lambda kv: abs(math.atan2(kv[1].y - cenB.y, kv[1].x - cenB.x) - ang))
    snapA_max = max(snapA_max, (hv - bv).length)
    headA.data.vertices[hi].co = Vector(bv)
headA.data.update()
rec["theirs_snap_max_mm"] = round(snapA_max * 1000, 3)
join_meshes(body_part, headA)
methodA = body_part; methodA.name = "MethodA_Theirs"
bpy.data.objects.remove(headA, do_unlink=True)
rec["methodA_fill_faces"] = 0  # counts match (24=24): their delete/F-fill patch branch never triggers
rec["methodA_verts_pre_weld"] = len(methodA.data.vertices)
bpy.context.view_layer.objects.active = methodA
methodA.select_set(True)
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.remove_doubles(threshold=0.001)
bpy.ops.object.mode_set(mode='OBJECT')
methodA.select_set(False)
rec["methodA_verts"] = len(methodA.data.vertices)
# Their weight step: donor groups renamed onto body bones (fleet names
# already match -> weights KEPT), then repeated Smooth on the neck groups
# (x3, Factor 0.5, corridor verts of head origin) + hand touch-ups
# (unscriptable, omitted and recorded).
offA = rec["body_part_verts"]
adjA = {}
for e in methodA.data.edges:
    adjA.setdefault(e.vertices[0], set()).add(e.vertices[1])
    adjA.setdefault(e.vertices[1], set()).add(e.vertices[0])
def getw(ob, gi, vi):
    for g in ob.data.vertices[vi].groups:
        if g.group == gi: return g.weight
    return 0.0
for grp_name in ("mixamorig:Neck", "mixamorig:Head"):
    gobj = methodA.vertex_groups[grp_name]
    for _ in range(3):
        neww = {}
        for vi, v in enumerate(methodA.data.vertices):
            if CUT_P - 0.01 <= v.co.z <= CUT_P + 0.05:
                nb = adjA.get(vi, set())
                if nb:
                    m = sum(getw(methodA, gobj.index, j) for j in nb) / len(nb)
                    neww[vi] = 0.5 * getw(methodA, gobj.index, vi) + 0.5 * m
        for vi, w in neww.items(): gobj.add([vi], w, 'REPLACE')
pairsA = []
for (bi, bv), (hi, hv) in zip(loopB, loopA_shift):
    ia = nearest_idx(methodA.data, bv); ib = nearest_idx(methodA.data, hv)
    if ia is not None and ib is not None: pairsA.append([ia, ib])
rec["pairsA"] = pairsA; rec["methodA_pairs"] = len(pairsA)

# ---------------- METHOD B ----------------
sxy = ring_r_B / ring_r_A
sz = (head_top_P - CUT_P) / (head_top_A - CUT_A)
for v in headB.data.vertices:
    v.co.x = cenA.x + (v.co.x - cenA.x) * sxy
    v.co.y = cenA.y + (v.co.y - cenA.y) * sxy
    v.co.z = CUT_A + (v.co.z - CUT_A) * sz + (CUT_P - CUT_A)
headB.data.update()
loopBnd, cenBnd = boundary_loop(headB.data, CUT_P)
snap_max = 0.0
for hi, hv in loopBnd:
    ang = math.atan2(hv.y - cenBnd.y, hv.x - cenBnd.x)
    bi, bv = min(loopB, key=lambda kv: abs(math.atan2(kv[1].y - cenB.y, kv[1].x - cenB.x) - ang))
    snap_max = max(snap_max, (hv - bv).length)
    headB.data.vertices[hi].co = Vector(bv)
headB.data.update()
rec["estate_snap_max_mm"] = round(snap_max * 1000, 3)
rec["estate_scale_xy"] = round(sxy, 4); rec["estate_scale_z"] = round(sz, 4)
bodyB = split_part(prima_body, CUT_P, False, "BodyPartB")
join_meshes(bodyB, headB)
methodB = bodyB; methodB.name = "MethodB_Estate"
bpy.data.objects.remove(headB, do_unlink=True)
pre_weld = len(methodB.data.vertices)
bpy.context.view_layer.objects.active = methodB
methodB.select_set(True)
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.remove_doubles(threshold=0.0001)
bpy.ops.object.mode_set(mode='OBJECT')
methodB.select_set(False)
rec["methodB_verts_pre_weld"] = pre_weld
rec["methodB_verts_after_weld"] = len(methodB.data.vertices)
for v in methodB.data.vertices:
    if v.co.z > CUT_P - 0.05:
        p = profile_at(v.co.z)
        for n in DEFORM:
            methodB.vertex_groups[n].add([v.index], p.get(n, 0.0), 'REPLACE')
rec["weld_positions"] = [[round(c, 5) for c in v] for _, v in loopB]
for m in (methodA, methodB):
    for p in m.data.polygons: p.use_smooth = True
    mod = m.modifiers.new("Armature", 'ARMATURE'); mod.object = armature
    m.parent = armature
# remove build-time sources so renders/gates see only the two joins + rig
for nm in ("Prima_Body", "Alma_Body", "BodyPart"):
    if nm in bpy.data.objects and bpy.data.objects[nm] not in (methodA, methodB):
        bpy.data.objects.remove(bpy.data.objects[nm], do_unlink=True)
if "BodyPart" in bpy.data.objects:
    bpy.data.objects.remove(bpy.data.objects["BodyPart"], do_unlink=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "headhack_both.blend"))
with open(os.path.join(OUT, "build_record.json"), "w") as f:
    json.dump(rec, f, indent=1)
print("BUILD_RECORD", json.dumps({k: v for k, v in rec.items() if k not in ("pairsA", "weld_positions")}))
print("OK plan28-build")
