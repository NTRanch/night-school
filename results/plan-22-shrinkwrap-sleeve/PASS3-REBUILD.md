# Plan 22 — Pass 3 Clean-Room Rebuild

Rebuilt from `TECHNIQUE.md` alone (video not reopened).
Toolchain: Blender **5.2.3 LTS** on primo (connector census),
scripted, headless except the bind phase (see Friction 2).
Target rig: **Prima** (conformed fleet rig) — sandbox copy
`~/workspace/torogao-models-20261104/prima/prima.blend`
(476 KB) transferred to primo
`~/.local/share/pax/night-school/plan-22/rebuild/prima-source.blend`;
originals untouched (the primo file is a copy; the sandbox
original was only read).

## Branch decision (task's Branch A vs B)

**Branch B — procedural sleeve tube test article** (not
wardrobe), on evidence: Prima's outfit nominally has long
sleeves (spec garment1 "sleeves: long"), but the outfit mesh
carries only **18 verts** in the upper-arm sleeve region on
either side, in incomplete rings of 1–6 verts
(`rebuild/probe2.json`, ns22_probe2.py) — there is no
extractable sleeve tube to fit. The plan's Branch B condition
("sleeveless in the relevant area") is met geometrically, so
a sleeve tube was authored procedurally around Prima's right
arm, spanning the elbow.

## Build (script: `rebuild/ns22_rebuild2.py`, phases prep/bind/measure)

- **Path**: cross-sections of the evaluated Prima_Body by
  raycast from the RightArm/RightForeArm bone axis (20 rays
  per station). Stations at upper-arm t = 0.35–0.65 found no
  free arm (bone axis buried in the shoulder mass / off-mesh;
  3–7 of 20 rays hit) and were dropped; the sleeve covers
  upper t = 0.75/0.85/0.95 + forearm t = 0.05–0.55 (9 rings ×
  20 segments = 180 verts per tube). Section radii:
  upper 30.5/35.2/35.7 mm (eccentric near the elbow: min
  3.3 mm / max 88.1 mm at t = 0.75 — the bone point runs near
  the surface there), forearm 30.0–35.1 mm (tight).
- **SleeveCollider**: the same sections at +3 mm clearance,
  triangulated faces, vertex groups RightArm/RightForeArm
  (hard split at the elbow ring), stack **Armature →
  Shrinkwrap** with the preset: Project, On Surface
  (5.2 RNA `wrap_mode`), Limit 0, Subdivision Levels 2
  (`subsurf_levels`), Negative+Positive, Face Cull Off,
  Target Prima_Body, Offset 0, no vertex group.
- **Project axis (the sheet's one UNREADABLE)**: resolved by
  the pre-registered rest-pose conformance test (hug =
  fraction of collider verts landing ≤1.5 mm from the body
  with station preserved ±0.2). On the first (bone-centred)
  tube: **X 1.000**, Y 0.423, Z 0.141, XYZ 0.495 → X. On the
  final raycast tube X/Y/XYZ all hug 1.000 and Z 0.967
  (the tube already sits on the body, so the test saturates);
  **X was kept** as the earlier discriminating winner.
  Recorded as the preset's least-certain field.
- **SleeveTest**: sections at +8 mm clearance; stack
  **SurfaceDeform → SleeveCollider** (falloff 4.000,
  strength 1.00, bound at rest — bind verified `is_bound
  True`) → **Solidify** Simple, thickness −35.8 mm
  (−0.87 × mean sleeve radius 41.2 mm, the demo ratio),
  offset −1.0000, Even Thickness off, Rim Fill on.
  No Armature modifier on the shell (the stricter reading of
  UNREADABLE 3): the shell follows only via Surface Deform.
- **Poses**: RightForeArm rotated about the elbow in
  armature space; achieved flexion measured from evaluated
  bones: set 0/70/120° → **achieved 0.0/70.0/120.0°** from
  rest (rest inter-axis angle 21.8°; posed 21.8°/91.8°/
  141.8°). No hand repair, no per-angle setting change: the
  preset ran as-is at all three angles.
- **Measurement**: Solidify-free clone of the bound shell
  (clone's SurfaceDeform verified bound), signed distances
  to the evaluated body via BVH (traceability:
  `rebuild/measurements.json`, `rebuild/measure.log`,
  `rebuild/prep.log`; per-angle scenes
  `rebuild/scene_{rest,flex70,flex120}.blend`; renders
  `rebuild/angle_*.png`).

## Per-angle fit table (180 sleeve verts, mm)

| Angle (achieved flexion) | Gap min | Gap mean | Gap max | Inside ≤ −0.5 mm | Pinch ratio (inner-elbow edge length vs rest) | Slide (mm) |
|---|---|---|---|---|---|---|
| rest (0.0°) | +1.87 | +3.75 | +3.99 | **0** | 1.000 (base 16.92 mm) | 0.0 |
| flex70 (70.0°) | **−7.96** | +3.00 | +5.62 | **15** | 0.886 | +2.17 |
| flex120 (120.0°) | **−4.54** | +2.34 | +6.56 | **39** | 1.167 | −0.07 |

Penetration localization (post-analysis of the saved
scenes, diag6): at 70° the 15 inside verts sit in rings
1–4, **30–42 mm from the elbow** (worst −8.0 mm, ring 2);
at 120° the 39 inside verts sit in rings 0–4, 32–112 mm
from the elbow (worst −4.5 mm). The failure is the
inner-elbow band, exactly where a sleeve must compress.

Pinch note: the edge-length ratio does NOT show compression
(0.886 at 70°, 1.167 at 120°) — the inner-elbow shell does
not shrink its edges; it **dives through the body instead**
(zone membership also grows, 41 → 74 verts at 120°, as the
shell folds). The pinch failure signature in this preset is
interpenetration, not edge collapse; both metrics are
reported as measured, per the benchmark.

## Gate read (against `rebuild/BENCHMARK-PREWRITTEN.md`)

| Condition | rest | 70° | 120° |
|---|---|---|---|
| Gap band (mean ∈ [1, 8] mm, max ≤ 15 mm) | PASS | PASS | PASS |
| Interpenetration = 0 below −0.5 mm | PASS | **FAIL (15, worst −7.96)** | **FAIL (39, worst −4.54)** |
| Pinch ratio ≥ 0.55 | PASS | PASS (0.886) | PASS (1.167) |
| Slide ≤ 10 mm | PASS | PASS (+2.17) | PASS (−0.07) |

**Gate: FAIL** — clean at rest and on gap/pinch/slide at
every angle, but the preset interpenetrates the inner elbow
at both bent angles with no hand repair permitted. The
failing angles are 70° and 120°, named with their numbers
above, per the plan gate.

## Claims verification (OBSERVATION.md §6)

- C1 (collider glues to target): **REPRODUCED** — collider
  evaluated verts sit at 0.0 mm mean |distance| at rest.
- C2 (shell follows proxy responsively): **REPRODUCED** —
  the unarmatured shell tracks the elbow through 120° of
  flexion (distal ring stays on the forearm; slide ≤ 2.2 mm).
- C3 (solidify wall inward, outer surface unmoved):
  **REPRODUCED by construction** (offset −1; fit measured
  on the pre-solidify shell; render scenes show the wall).
- C4 (survives gross slides without repair): **NOT TESTED**
  in this rebuild (the plan's rebuild spec is the bent
  joint, C5); the demo's own slides are screen evidence only.
- C5 (survives a bent joint): **REFUTED for the preset
  as-is** — interpenetration at 70° and 120° (table above).
  The mechanism that makes the sleeve responsive (offset-0
  projection + surface-deform carry) has no inner-elbow
  relief: where the joint compresses, the carried shell has
  nowhere to go but through the body. A production version
  needs an inner-elbow ease (e.g. vertex-group falloff on
  the collider at the crease, or a positive offset ramp) —
  recorded as a follow-on, NOT applied here (no hand repair).

## Attempt history (honest record)

Attempts 1–4 produced no valid gate numbers and are not
averaged in: (1) Blender 5.2 RNA rename broke the script
(`snap_mode` → `wrap_mode`; `subdivision_levels` →
`subsurf_levels`); (2) SurfaceDeform bind is a WM job that
never completes in `blender -b`, and bind rejects
concave/n-gon targets — fixed by an Xvfb GUI bind phase +
triangulated collider; (3) bone-line tube path — Prima's
bone line is buried in the shoulder and off-centre, tube
built inside the torso; (4–6) mesh-ring section derivations
missed Prima's ~62–70 mm ring spacing / axis tilt. The
raycast-section build (attempt 7, `out7` on primo) is the
run of record. Attempt logs: primo
`~/.local/share/pax/detach/ns22-*.log`; failed-run outputs
were cleaned from the run dir at task end (see
BLOCH-CANDIDATE friction log).
