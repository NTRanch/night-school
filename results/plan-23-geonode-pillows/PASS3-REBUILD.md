# PASS 3 — Clean-room rebuild: PillowSquish (Plan 23)

Rebuilt from TECHNIQUE.md alone (the sheet), in a fresh scene,
on primo, **Blender 5.2.3 LTS**. Video's Blender: 4.4.3.
Scripts + outputs in `rebuild/` (this run): `pillow_core.py`,
`build_pillow.py`, `sweep_pillow.py`, `compare_det.py`,
`out/` (asset .blend, measures, renders, sweep.json,
determinism.json). Primo working copies + run logs:
`~/.local/share/pax/night-school/plan-23/`, detach runs
`ns23-buildA`, `ns23-sweep`, `ns23-sweep2` (file-mediated,
D-567 pattern; nice 10, `--threads 4`, `--factory-startup`,
sequenced behind sibling whisper jobs).

## Version drift (4.4.3 → 5.2.3), recorded

- All seven node types exist with identical names/semantics:
  Set Position, Object Info, Geometry Proximity, Map Range,
  Color Ramp (ValToRGB), Combine XYZ, Group Input/Output.
  No node was renamed or re-socketed between the video's
  version and 5.2.3.
- **API drift (found by failure):** Blender 5.2's
  `NodesModifier` rejects ID-property writes for group inputs
  (`TypeError: id properties not supported for this type` —
  first buildA run, exit 1). The supported route is the
  interface socket's `default_value`; the build uses it for
  the Collider object input. In the editor the same value is
  set in the modifier panel as usual — asset behaviour is
  unaffected.
- The asset therefore carries the demo collider as the
  Collider input's default; re-targeting is a panel change.

## The asset

`rebuild/out/pillow_asset.blend` — contains:
- Node group **`PillowSquish`** (the estate adaptation from the
  sheet): the video's 7-node chain with **Collider** (object)
  and **From Min / From Max / To Min / To Max** (floats,
  defaults = the video's final values) exposed as group
  inputs; Color Ramp internal (stops 0.714 black / 0.982
  white), Combine XYZ Z-only, Proximity Faces, Object Info
  Relative — all per spec.
- Demo scene: cushion (box 1.20 × 0.80 × 0.25 m, 16 segments
  per edge = 1,536 faces / 1,538 verts — the video's measured
  density) + squashed-sphere sitter proxy pressed 0.06 m into
  the top, Workbench camera for the demo render.

## Demo-settings form measures (run A = run B, see determinism)

From `out/measures_demo_A.json` (Blender 5.2.3 LTS):

| Measure | Value |
|---|---|
| Vertices / faces | 1,538 / 1,536 (topology unchanged by the group) |
| Bounding box after deform | 1.200 × 0.800 × 0.369 m |
| Contact patch: min Z / mean Z | 0.4639 / 0.4755 m (rest top 0.25) |
| Apex (far-field top) Z | 0.6728 m |
| **Dent depth (apex − contact min)** | **0.2089 m** |
| Contact lift (mean) | 0.2255 m |
| Min column thickness | 0.142 m (ratio 0.57 of 0.25) |
| Inverted columns / NaN / flipped / degenerate / non-manifold | 0 / 0 / 0 / 0 / 0 |
| Poke depth | 0.000 m |

**Claim tests (Pass 1 list):**
- C-1 (deforms live, no sim): **REPRODUCED** — the evaluated
  mesh deforms from the collider's evaluated geometry alone;
  the demo render (`out/demo_A.png`) shows the cradled dent.
- C-2 (distance-only, no weights/groups/drivers): **REPRODUCED
  by construction** — the rebuilt chain has no other input.
- C-3 (relative dent; ≈0.48 m at full separation): **REPRODUCED
  in mechanism, scale-adjusted in magnitude.** The sheet's
  0.48 m figure assumed far-field verts ≥1 m from the
  collider; on this 1.2 m cushion the far field sits 0.35–0.6 m
  from the collider surface, and the sheet's own transfer
  function predicts lift 0.36–0.52 there vs 0.21 at contact —
  a dent of 0.15–0.31 m. Measured dent 0.2089 m, contact lift
  0.2255 m vs the function's 0.21 at d = 0 (the small excess
  is the contact disc's mean distance being > 0 at its rim).
  The relative-dent mechanism — contact lifts *least*, never
  pushed down — is confirmed by contact_min_z (0.464) >
  rest top (0.25): nothing dips below rest, anywhere.
- C-4 (one tree, two cushion sizes): **REPRODUCED by the
  sweep's G axis** — thickness 0.05–0.50 all produce the same
  dent (0.2089) with the same tree; only the scene changed.
- C-5 (density contract): **PARTIALLY REFUTED as a hard
  floor** — dent depth is 0.205 even at 4 segments/edge; what
  low density actually costs is *form resolution* (the seg-4
  render's dent is a coarse faceted dip — agent eye read),
  not depth. The contract is rewritten in PASS4 as a
  resolution guideline (≥16/edge for a smooth pocket), not a
  breakage threshold.
- C-6 (Z-only final form): **REPRODUCED** — Combine XYZ
  X = Y = 0 in the asset, per spec.

## Classification rules: pre-registered, then Revision 1

Pre-registered (before the sweep): CLIFF = NaN / inversion /
non-manifold / >0.5 % degenerate; DEGRADED = dent outside
0.02–0.75 m, thick_ratio < 0.30, flipped > 0, **penetration
verts > 2 % of verts**.

Round 1 ran with those rules and **the video's own demo
configuration classified DEGRADED** (penetration 126 > 2 % of
1,538). That falsifies the penetration rule, not the demo:
penetration count measures how many verts sit inside the
collider volume — i.e. the size of the contact patch, the
mechanism working as designed. **Revision 1** (applied before
round 2, recorded here and in `pillow_core.classify`):
penetration rule removed; two strain signals added —
**poke_depth** (collider's lowest point below the lifted
contact surface > 0.02 m = visible interpenetration) and
**contact_lift > 0.60 m** (over-inflation: the cushion leaves
its seat). All other rules unchanged. A second measurement
fix landed in the same revision: inversion is tested
**per (x, y) column** (bottom vert vs its own column's top
vert); the round-0 global test false-fired at demo settings
because far bottom corners legitimately lift above the
pressed contact patch (bottom_max 0.472 > contact_min 0.464
with zero inverted columns).

## The sweep (39 steps, round 2; `out/sweep.json` governs)

Each step rebuilt the group from its parameter vector alone.
Renders at axis corners + every CLIFF (`out/sweep_renders/`,
17 kept; 13 stale renders from the killed round-0 run were
pruned and are not evidence).

| Axis | Values | SAFE span | DEGRADED | CLIFF |
|---|---|---|---|---|
| A From Min | −4 … +0.5 | −4.0 … −1.6 (dent 0.13–0.25) | −1.0, −0.5 (contact lift collapses → poke 0.06); 0.0, +0.5 (dent 0 — whole scene inside ramp's black plateau) | — |
| B From Max | 0.2 … 4.0 | 0.2 … 1.0 (dent 0.13–0.25) | 2.0 (weak dent 0.125 + poke); 4.0 (dent 0 — window too wide, P-6 graceful fade confirmed) | — |
| C To window | (0.5,0.9) demo … (1.2,1.6) | demo (0.5,0.9); (0.8,0.9) shallow dent 0.052 | (0,1) deepest dent 0.389 but thick_ratio 0.13 (near-cliff thinning); (0,0.3) dent 0 (below ramp knee, P-2); (1.2,1.6) dent 0, uniform +1.0 lift — floating slab (P-2) | — |
| D Ramp start | 0 … 0.99 | 0.714 (demo) only | 0.0 / 0.3 over-inflation (contact lift 0.79 / 0.70 — render shows the cushion lifted clean off the collider); 0.9 / 0.99 dent 0 (Fac never reaches the knee) | — |
| E Press | −0.10 … +0.30 | −0.10 … +0.15 (dent 0.19–0.22 throughout) | +0.30 poke 0.073 (collider sinks through the lifted surface) | — |
| F Segments/edge | 4 … 32 | 4 … 32 numerically (dent 0.205–0.209) | — (seg-4 form resolution is an eye item, Q-3) | — |
| G Thickness | 0.05 … 0.50 | all (dent constant 0.209; thick_ratio 0.55–0.59) | — | — |
| H Inversion hunt | windows (0,1)+To(0,1); (−0.5,0.5)+To(0,1); (−0.2,0.2)+To(0,1) | — | H1 dent 0 (window sits in the black plateau) | **H2: 182 inverted columns, thick_ratio −1.21, dent 0.831. H3: 159 inverted columns, thick_ratio −3.00, dent 1.000 (saturated)** |

Totals: **SAFE 20 · DEGRADED 17 · CLIFF 2** of 39 steps.

**Predictions scored:** P-1 (inversion cliff exists) —
CONFIRMED but located by the *product* of both windows, not
the From window alone: no A/B/C step inverted; the hunt
needed To (0,1) *and* a ≤1.0-wide From window positioned over
the scene's distance band. Breakage mode: bottom verts lift
past their own top verts (the through-thickness gradient
exceeds the thickness), the slab crumples into a torn V
(render `sweep_H_inversion_hunt_1_w1p0_to0m1.png` — agent eye
read: jagged flipped walls, form destroyed). P-2 (Fac-window
cliffs at both ends) — CONFIRMED as DEGRADED modes (dead box /
floating slab), not geometric breaks. P-3 (ramp cliff) —
CONFIRMED as effect-loss/over-inflation, no break. P-4
(press cliff) — REFUTED as a dent effect (dent is
press-invariant once touching); the real deep-press failure
is poke-through, DEGRADED. P-5 (density cliff) — REFUTED
numerically; survives only as an eye-level resolution loss.
P-6 (wide window = graceful fade) — CONFIRMED (B 4.0, A −4.0).

**Safe ranges (the asset's documented envelope):**
From Min ∈ [−4.0, −1.6] with From Max ∈ [0.2, 1.0] (demo
−2.1 / 1.0); To window inside the ramp's active band with
To Max − To Min ≤ ~0.4 at demo-like widths — wider To windows
thin the cushion toward the H-cliff; ramp start ∈ (0.3, 0.9)
exclusive-ish, demo 0.714; press ∈ [hover −0.10, +0.15];
segments ≥ 8 (16 recommended); thickness 0.05–0.50 free.
**Hard cliff:** combined window gradient — From width ≤ 1.0
positioned over the contact distance band *with* To (0,1) —
inverts the mesh. Rule of thumb written into the asset doc:
keep (To Max − To Min) / (From Max − From Min) ≤ 0.13 (demo:
0.4/3.1 = 0.129; H2: 1.0/1.0 = 1.0 → cliff; C(0,1) at demo
From width: 1.0/3.1 = 0.32 → ratio 0.13 thickness, strained
but standing).

## Determinism

Two independent Blender processes at demo settings
(build A / build B): **vertex-hash identical**
(73fa0f9e68b67665…), every compared measure identical,
**render pixel-hash identical** (3c20ac17e0a844d04…,
decoded pixels, 640×480) — `out/determinism.json`. The group
is stateless (no simulation, no seed), so this is the
expected result, now evidenced.
