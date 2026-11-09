# Plan 38 — Pass 3 Rebuild Record

## 0. Wrap3D availability probe (required first step)

- Primo: no Wrap3D binary anywhere (`find` over ~, /opt,
  /usr for `*wrap3d*`: nothing). Wine EXISTS
  (`/usr/bin/wine`) but holds no Wrap3D install and there is
  no licence. Sandbox: nothing, and no Blender either.
- Blender on primo: **5.2.3 LTS** (`/usr/bin/blender`,
  build e13b728c6880) — the estate pin.
- **Verdict: Wrap3D genuinely absent.** The rebuild uses
  the estate-equivalent stack, and TECHNIQUE.md records
  the substitution as an explicit DEVIATION. Wrap-internal
  numbers (Subdiv 3 / ICP 5 / Opt 20 / Sampling 5→0.2,
  Draco 30/30/30/7) are UNTESTABLE-IN-ROUTE and were not
  faked; what transfers is the contract, the grammar, and
  the lie-zone map.

## 1. The pair and the pipeline (as built)

- **Source (template):** Prima_Body evaluated at
  Body_Bust_Size = 0 (canon, m 1.00): 3,084 verts, UVs,
  named groups. **Target ground truth (GT):** the same
  body at key = 1.0 (m 1.50, builder amp 0.045 m).
  **Target as wrapped onto ("scan"):** GT decimated to
  1,771 verts (ratio 0.55) — independent topology,
  surface-faithful. (Voxel remesh was tried first and
  REJECTED with evidence: it lost Prima's entire
  z 0.4–0.6 leg slab — 0 verts in band — and put the scan
  floor at global p95 189 mm; `diag2.log`,
  `metrics-v1voxel-stage1.json`. Decimate floor: bust
  band mean 1.26 mm → the wrap numbers below are wraps,
  not scan artefacts, except where the floor is cited.)
- **Correspondence:** the fleet's own §6 anchors, derived
  by `place_anchors.py:compute_anchor_points` (the estate
  tool, imported unmodified except its `main()` call —
  see BLOCH friction F-6) on both states; used as the
  measurement landmarks and to build the named groups.
- **Exclusions (W-3/W-4 realised as named groups):**
  `VG_WrapInclude` / `VG_Exclude_EyeMouthFold`, built by
  rule from positions (eye radius 0.030 m around
  rule-derived eye centres; mouth radius 0.024 m;
  underbust fold band): include 2,783 / exclude 301 verts.
- **Stack:** Shrinkwrap (PROJECT, ON_SURFACE, all axes,
  ± directions, offset 0, subsurf_levels 2 — Plan 22
  preset values) onto the decimated scan, group-limited
  → bake → refine: second Shrinkwrap onto the
  **triangulated true GT** → Data Transfer custom
  normals from GT. All stages baked via evaluated-mesh
  extraction (topology of the source preserved exactly —
  required by W-10).
- **Surface Deform could not be used** (Plan 22 stack
  deviation, evidence-bound): bind refused three times —
  "Target has edges with more than two polygons"
  (`gb-run1.log`). Prima's GT body is itself non-manifold
  (36 edges with >2 faces, 576 non-manifold edges —
  `diag3.log`), and every derived target inherits it;
  sparse bind refuses too. The refine stage was
  substituted as above. This is a genuine estate finding:
  **Plan 22's preset presumes manifold targets; fleet
  bodies are not manifold**, so the preset cannot be
  applied to fleet bodies unmodified.

## 2. Fidelity (run1 = run2; artifacts in build/)

Full stack, GT-anchored distances to the wrapped surface:

| Metric | Value | Artifact |
|---|---|---|
| Global mean / p95 / max | **0.180 / 0.849 / 14.31 mm** | metrics-run1-stage2.json |
| Bust band mean / p95 / max | 1.148 / 6.726 / 10.469 mm | same |
| Apex zone mean (n=3 GT verts) | ~14.2 mm at stage 1 → anchors below | metrics-run1-stage1.json |
| Anchor Nipple.L / .R | **11.11 / 8.89 mm** (incl. the anchors' 2 mm proud offset → surface ≈ 9.1 / 6.9 mm) | stage2 |
| Anchor Chest | 10.47 mm | stage2 |
| Anchor Mouth | **2.00 mm** = the proud offset exactly → mouth surface exact | stage2 |
| Anchor Pelvis | 1.99 mm | stage2 |
| Anchor Hand.L / .R | 1.73 / 0.04 mm | stage2 |
| Silhouette delta (512², Workbench) | **front 0.381 % of pixels, side 0.020 %** | stage2 `silhouette_delta` |
| Determinism | run1 vs run2: vertex-coords SHA-256 **identical** (86f95926…), all four render **decoded-pixel** hashes identical | metrics-run{1,2}-stage2.json |
| W-10 integration | wrapped positions loaded as shape key `Wrapped_m150` on a fresh canon body: max delta **0.0001 mm** | stage2 `w10_shapekey_max_delta_mm` |

The apex is this pair's lie zone (see §4): the bust band
holds only 48 GT verts, so the cage chords inside the
mound; the ~9–11 mm anchor error is a cage-density floor,
not a solver failure — the same structural lie as the
video's ear, priced in advance by the map (curvature
change ≫ local cage density).

**Correction stage (W-8 realised):** shape key
`Correction` added; Laplacian smoothing (25 iters, λ 0.5)
restricted to the underbust seam-analog zone (7 verts at
this cage density). **Basis hash unchanged** (mechanical
proof the raw wrap survives cleanup). Effect: underbust
mean 2.31 → 2.15 mm, max 3.93 → 4.59 mm — **within noise;
the zone is underpowered at 3,084 verts**. Recorded as
measured, not spun: on this pair the Correction layer's
value is the audit property (Basis intact), not the
millimetres. A blanket Smooth polish was tried and
REMOVED with attribution (§5, row 2).

## 3. Checklist validation — the gate's core

One precondition skipped at a time on scratch copies
(shrinkwrap stage; metrics-exp-*.json). Main stage-1
reference: bust mean 1.349 mm, nipples 11.12/8.86 mm,
global mean 0.439 mm.

| Item | Experiment | Result | Verdict |
|---|---|---|---|
| W-1 interchange contract | By construction: UVs + named groups carried through every bake; W-10 topology proof (§2). E5 bounds it (below). | Holds. | **CONFIRMED-BY-CONSTRUCTION** |
| W-2 pre-alignment (scale) | E1: target scaled ×1.10, no re-alignment | Nipples 45.3/46.4 mm, chest 51.1 mm, bust mean 13.02, global 5.45 | **VALIDATED** |
| W-2 pre-alignment (pose) | E6/E6B: target forearm bent 40° | Hand anchor instrument too weak (closest-surface to a tube); decisive metric = hand-region centroid: wrapped centroid moved **0 mm toward the bent pose** (9.97 mm from both GT and canon centroids; wrist displacement in target ≈ 170 mm). The wrap silently keeps the source pose. | **VALIDATED** (pose mismatch is ignored, not corrected — the dangerous kind of failure) |
| W-3 named sets | By construction: all masks are the two named rule-built groups; sizes recorded (2,783/301). | Holds. | **CONFIRMED-BY-CONSTRUCTION** |
| W-4 exclusion subsets | E2: projection with NO exclusions | Anchors identical to main (11.12/8.86), bust mean 1.349 = main, global 0.458 vs 0.439 | **STRUCK as a universal precondition** — does not reproduce on this pair. Re-issued as CONDITIONAL: required when a side carries deep non-corresponding cavities (Feng's mouth bag/eye sockets in the source video; Prima's face is shallow and low-poly, so the exclusion has nothing to protect). The video itself cannot prove the counterfactual either (its cleanup at eyes/mouth happened WITH subsets in place). |
| W-5 point-set/geometry binding | E4 (analog): stale SOURCE (m 0.50 body, built by exact key linearity: 2·canon − GT) wrapped onto the m 1.50 target | Wrap "succeeds" (global mean 0.455) while bust anchors land at 17.4/14.7 mm, chest 18.5 mm, bust mean 2.08 — only the anchor gate catches the staleness | **VALIDATED** (analog form — the estate has no stored point sets to go stale; its stored GEOMETRY states are the stale-able asset, and the failure signature matches the video's 127-point near-miss: silent, plausible, caught by correspondence checks only) |
| W-6 correspondence grammar | E3: bust band excluded from projection (correspondence removed for the bust) | Nipples degrade to exactly the parameter gap (14.43/14.43 mm), chest to 15.00 mm (= full amp delta); with correspondence: 11.12/8.86 and 10.44 | **VALIDATED** — correspondence buys back ~3.3–5.6 mm at the landmarks it pins; its ceiling here is the cage floor (§2), not the grammar |
| W-7 multi-resolution solve | E7: single NEAREST_SURFACEPOINT projection only | **Beat** the stack on this pair: bust mean 0.759, nipples 7.61/7.71, global 0.375 | **STRUCK as stated** for gentle morphs — the predicted folding does not reproduce at Δamp = 15 mm on a smooth cage. Re-issued as CONDITIONAL: the multi-stage solve is priced for large-displacement / cavity wraps (the video's head retarget class) and articulated targets (Plan 22's elbow failure class), not for single-parameter variant morphs. For bust-variant production the simple projection is the correct, cheaper tool — an evidence-priced scoping, recorded with its numbers. |
| W-8 correction layer | By construction + mechanical proof: Basis hash identical before/after Correction (§2) | Holds. | **CONFIRMED** (audit property); its millimetre effect on this pair is within noise (recorded) |
| W-9 textures as a separate pass | E5: source UV layer deleted before wrapping | Wrapped coords hash **byte-identical** with/without UVs (f2615798…) | The candidate claim "UVs are a wrap precondition" is **STRUCK** (as predicted in TECHNIQUE): UVs belong to the texture pass, exactly as the video's two-graph structure shows. W-9 itself **CONFIRMED-BY-CONSTRUCTION** |
| W-10 blend-don't-swap | §2 shape-key load proof | max delta 0.0001 mm | **CONFIRMED** |

Checklist census: 10 items → **4 validated by experiment
(W-2 scale, W-2 pose, W-5, W-6), 4 confirmed by
construction/mechanical proof (W-1, W-3, W-8, W-9 +
W-10), 2 struck as universals and re-issued as
conditionals with their evidence (W-4, W-7).** No item
is kept on faith.

## 4. Lie zones for this pair (before/after cleanup)

| Zone | Before | After Correction | Class |
|---|---|---|---|
| Bust apex | anchors 11.1/8.9 mm (surface ≈ 9.1/6.9) | unchanged (Correction does not touch it — smoothing a fit error is the wrong medicine; §5 row 2 is the proof) | INHERENT (cage density) |
| Underbust fold | mean 2.31 mm, max 3.93 | mean 2.15, max 4.59 (7-vert zone; within noise) | seam-analog; pre-emptable in degree |
| Eye/mouth (excluded zones) | mouth surface exact (2.00 = offset); no cavity artefacts at this cage | — | pre-empted by scoping (W-4 conditional) |
| Pelvis/hands (un-retargeted) | 2.0 / ≤1.7 mm | — | no lie, as the map predicts for untouched regions |

## 5. Per-edit attribution rows (build-level)

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| Scan construction | voxel remesh 8 mm → decimate 0.55 | scan floor global p95 189 mm → bust-band floor mean 1.26 mm; leg slab restored | curative |
| Refine stage | Surface Deform (Plan 22 stack) → Shrinkwrap-2 onto triangulated GT | SD bind refused ×3 (non-manifold target, 36 edges >2 faces); substitute refine: bust mean 1.349 → 1.148 | curative (deviation, evidence-bound) |
| Polish | Smooth (0.25 ×2, group-limited) added, then removed | in isolation (polish-decomp.json): bust mean 1.148 → 3.088, nipples → 16.4/12.9 (Laplacian mound shrinkage); projection-only keeps 1.148 | curative (removal) |
| Correction zone | apex radius dropped from the smoothing zone | apex is a fit error, not roughness; zone = underbust only (7 verts) | design correction, pre-measurement |
| E6 instrument | hand anchor → hand-region centroid | anchor read 0.47 mm (false pass); centroid shows 0 mm pose transfer (true fail) | curative (metrology) |

## 6. Gate verdict (against the plan's own gate)

Plan gate: "PASS = contract checklist validated by the
rebuild (each skipped precondition's failure either
reproduced or the item struck), and fidelity gates met."

- Checklist: every item is validated, confirmed by
  mechanical proof, or struck-with-evidence and re-issued
  as a conditional (W-4, W-7). **Met, in the gate's own
  terms** — the two strikes are the gate working as
  designed, not exceptions to it.
- Fidelity: silhouette delta front 0.381 % / side
  0.020 % of pixels at viewing size; landmark deltas:
  5 of 7 anchors ≤ 2.0 mm, bust anchors at the
  documented cage floor (9.1/6.9 mm surface); global
  mean 0.180 mm. Determinism exact (coords + decoded
  pixels). **Met** for the variant-morph class; the
  apex floor is recorded as the pair's known limit.
- **Overall: PASS** — with the W-4/W-7 conditional
  re-issues and the Surface-Deform deviation carried
  into the technique sheet as its permanent record.
  (Owner eye items are queued in PASS4; no Owner PASS
  is declared here.)
