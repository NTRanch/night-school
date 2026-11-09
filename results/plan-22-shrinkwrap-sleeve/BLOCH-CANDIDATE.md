# Bloch candidate — Plan 22 run

- origin_lane: ntranch
- content_label: nsfw
- origin: Night School Plan 22 study run (Blender Tutorial:
  Shrinkwrap Sleeve, rule34video 3881849), 2026-11-06.

## Candidate 1 — Surface Deform bind is a WM job, and its target has a polygon law

**Lesson:** In Blender (5.2.3), `bpy.ops.object.
surfacedeform_bind` starts a window-manager **job**: in
`blender -b` it returns FINISHED and never binds
(`is_bound` stays False, silently). It completes only
under a running event loop (Xvfb GUI mode + a timer polling
`is_bound` works). Separately, the bind **rejects targets
with concave or n-gon polygons** ("Target contains concave
polygons" / "invalid polygons" in the log — even a stock
cylinder's cap n-gons fail). A shrinkwrap-projected proxy
easily goes concave; **triangulating the collider** makes
the bind succeed on the first poll. Any estate script that
binds Surface/Mesh Deform headlessly needs the split:
prep in -b, bind under Xvfb, measure in -b, and an explicit
`is_bound` assertion — FINISHED is not bound.
**Evidence:** runs/plan-22/PASS3-REBUILD.md (attempt
history), runs/plan-22/rebuild/ns22_rebuild2.py (three-phase
structure), primo detach logs ns22-bind.log (concave
warning, BOUND_FAILED) and ns22-bind3.log (BOUND_OK tries 1
after triangulation).

## Candidate 2 — A conformance A/B needs a station test, or the torso wins

**Lesson:** When a shrinkwrap Project axis was unreadable
in the source and had to be resolved by measurement, the
naive criterion (mean |signed distance| of the wrapped
proxy to the body) scored a perfect 0.0 for the WRONG axis:
rays along X from a tube near the shoulder glue to the
**torso**, which is also "on the body". The discriminating
criterion pairs the distance with **station preservation**
(the closest surface point must belong to the same limb
station ±0.2). Any future "which setting reproduces the
demo" test on a full character must include a locality
term, or large nearby masses will absorb the fit.
**Evidence:** runs/plan-22/PASS3-REBUILD.md (axis A/B
table), runs/plan-22/rebuild/ns22_rebuild2.py `axis_score`.

## Candidate 3 — Fit the tube path to the mesh, not the skeleton

**Lesson:** Prima's bone line is buried in the shoulder
mass for the proximal upper arm and runs 15–20 mm off the
mesh arm's central axis; a sleeve tube built on bone
centres started inside the torso (ring-centre depth up to
73 mm, sleeve verts −42…+120 mm off the body). The build
that worked derives cross-sections from the **evaluated
body mesh itself** (radial raycasts from the axis; stations
with <16/20 hits are dropped as "no free limb there").
Skeleton for posing, mesh for fitting — in that order.
**Evidence:** runs/plan-22/PASS3-REBUILD.md, primo diag
scripts /tmp/diag3.py–diag5.py outputs quoted there,
runs/plan-22/rebuild/prep.log (section table).

## D-1064 friction log (this run)

- **Cost time:** ~35 min — primo transcription saturation
  (12 concurrent whisper jobs from sibling plans; load
  32–35 on 16 threads). The ns22 whisper (nice 19, 2
  threads) landed only 3:47 of 12:27 during the run; the
  screen class carried the study and the job was left
  running for the canonical transcript. Next agent: on a
  saturated box, check `ps | grep whisper` BEFORE promising
  a transcript timeline.
- **Cost time:** ~50 min — the rebuild took 7 attempts
  (RNA renames in Blender 5.2, the bind job law, the
  bone-line path defect, two failed mesh-section
  derivations). Each failure was diagnosed from its own
  numbers before the next attempt; the attempt history is
  in PASS3-REBUILD.md.
- **Forced a guess:** the source's Project **Axis** field
  is unreadable in every frame (counted as UNREADABLE 1);
  resolved by a pre-registered conformance test instead of
  a guess (Candidate 2). On the final tube the test
  saturates (X/Y/XYZ all hug 1.000); X stands as the
  earlier discriminating winner and is flagged as the
  preset's least-certain field wherever it is recorded.
- **Silent workaround caught:** in attempt 1 the
  measurement pipeline reported precise-looking fit numbers
  for a sleeve whose SurfaceDeform was **never bound** —
  the numbers were construction artefacts, not fit. The
  `is_bound` assertion is now a hard gate in the script;
  a plausible table is not evidence the mechanism ran.
- **Silent workaround caught:** the sandbox `scp` without
  `-F /home/hatch/.ssh/config` fails "Connection closed"
  (root's config lacks the primo route) — the working form
  is the one primo-ssh wraps. Recorded in MANIFEST.md.

## Per-edit attribution (rebuild script, ns22_rebuild2.py)

| Component / change | Observed difference | Verdict |
|---|---|---|
| Shrinkwrap RNA: `snap_mode`→`wrap_mode`, `subdivision_levels`→`subsurf_levels` (Blender 5.2) | Script crash at modifier setup → full run proceeds | fix (necessary) |
| Bind split into Xvfb GUI phase + `is_bound` poll | `is_bound` False (-b) → bind job executes | fix (necessary) |
| Collider faces triangulated at build | Bind log "concave polygons" + BOUND_FAILED → BOUND_OK first poll | fix (necessary) |
| Pose via armature-space point rotation (`pb.matrix`) + sign probe at 10° | Achieved flexion error ~44° → exactly 70.0°/120.0° | fix (necessary) |
| Tube path: bone centres → mesh-ring bins → gap clusters → radial raycast sections | Sleeve rest fit mean +30 mm/19 inside → +3.75 mm/0 inside | fix (necessary); intermediate derivations confounded by Prima's ~62–70 mm ring spacing and bone/mesh axis tilt |
| Axis A/B criterion + station-preservation term | X chosen on hug 1.000 vs XYZ 0.495 (coarse tube); saturates on final tube | adopted with caveat (least-certain field) |
| Sleeve spans upper t 0.75–0.95 + forearm 0.05–0.55 only | Proximal stations dropped: no free arm there (3–7/20 ray hits) | confounded — a longer sleeve toward the shoulder is untested, not disproven |

## Artefact pointers

- Technique sheet + preset: `runs/plan-22/TECHNIQUE.md`
  (this run, 2026-11-06) — preset `NS22-RESPONSIVE-SLEEVE-FIT`.
- Rebuild script: `runs/plan-22/rebuild/ns22_rebuild2.py`;
  run of record = primo out7 (`measurements.json` copied to
  `runs/plan-22/rebuild/measurements.json`).
- Gate record: `runs/plan-22/PASS3-REBUILD.md` +
  `PASS4-APPLICATION.md`; benchmark pre-written at
  `runs/plan-22/rebuild/BENCHMARK-PREWRITTEN.md`.
