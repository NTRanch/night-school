# Plan 09 — Pass 3 Clean-Room Rebuild

- **Built from the sheet alone** (TECHNIQUE.md / OBSERVATION.md), Blender
  **5.2.3 LTS** on primo, headless, scripted: `rebuild/scripts/ns09_gn.py`
  (sha256 in `rebuild/run_record.json`). Two full processes (runA, runB)
  for the determinism gate; renders 960×540 Workbench, PF-2 decoded-pixel
  hashing (`rebuild/pixelhash_ab.txt`).
- **Scene:** two Ø 2 m proxy spheres (the sheet's C-13 scale), paths
  authored programmatically on the surface — an arc over sphere A with a
  descending drip branch (C-10's authored-drip form) and a bridge path
  spanning to sphere B (C-11). Debug material per C-09 (green Principled,
  Roughness 0.5) so shape, not shading, is what the renders judge.

## Variants (sheet states)

| Variant | Configuration (sheet source) | Evaluated verts | Read |
|---|---|---|---|
| v1_firstform | Count 10 · Voxel Amount 64 · Radius 0.5 m (660 s) | 6,432 | Oversized dimpled mass arching the sphere — the sheet's "obviously too big" state, in shape class. |
| v2_lumps | Count 100 · Voxel Amount 64 · Radius 0.25 m (1380 s count; 720 s radius) | 3,790 | Smooth rope — at 100 points the spacing (≈0.04 m) is far below the radius, so no lumps form. |
| v2b_lumps24 | Count 24 · Voxel Amount 64 · Radius 0.25 m (probe, not a sheet state) | 3,830 | **Ribbed, visibly lumped** strand — spacing ≈0.17 m approaches the radius and the fusion period appears. |
| v3_final | Length 0.001 m · Voxel Size = 0.100/2.000 · Radius 0.100 · Smooth 1.5×20 (final form) | 1,162 + 754 (bridge) | One continuous smooth strand + fused bridge to sphere B. |
| v4_bodyradius | v3 with Radius 0.025 (2030 s) | 4,666 + 2,828 | Same paths at detail girth, still continuous. |
| anim probe | v3 form; drip growth 0.15 / 0.55 / 1.0 | 966 / 1,056 / 1,162 | The drip lengthens across the three states; per-state re-evaluation, **no bake, no cache** (none exists to delete). |

Whole build (4 variants + probe): **2.21 s / 1.76 s wall** in the two
processes — against Plan 07's ~54.5 s bake for one configuration, and
zero cache files (Plan 07's Alembic handoff alone was 476,974,171 B).

## Claims scored (against OBSERVATION.md)

**REPRODUCED 11 · UNTESTABLE-IN-ROUTE 3 · UNTESTED 1** (of the 15
rebuildable claims; C-13/C-14/C-15 are provenance/teaching, not builds).

- C-01 chain → REPRODUCED. The five-node chain evaluates to a strand
  mesh exactly as sheeted.
- C-02 first-form blob → REPRODUCED in shape class (v1).
- C-03 lump mechanism → REPRODUCED as a mechanism: at fixed Radius
  0.25 m, Count 100 renders smooth and Count 24 renders ribbed (v2 vs
  v2b) — continuity is controlled by point spacing ÷ radius, as sheeted.
  The tutorial's exact 720 s count was never pane-read, so the specific
  frame is matched in kind, not in parameters.
- C-04 Length-0.001 sampling → REPRODUCED (v3/v4 continuous by
  construction).
- C-05 Voxel Size = Radius / Resolution → REPRODUCED (Divide wired as
  spoken + cropped; evaluation confirms the semantics).
- C-06 radius classes 0.100 / 0.025 → REPRODUCED with the F-1 correction
  below (delivered girth ≠ nominal radius under the full stack).
- C-07 Smooth modifier → REPRODUCED, and its cost measured (F-1).
- C-08 one group, many curves → REPRODUCED (both v3 curves share one
  group definition via separate modifier instances).
- C-09 debug material practice → REPRODUCED (used for all renders).
- C-09b final transmission material → UNTESTABLE-IN-ROUTE: the
  Workbench pixel lane cannot show transmission/volume behaviour; the
  recipe is recorded in the preset for the Owner-eye look gate, not
  asserted here.
- C-10 authored drips → REPRODUCED (drip branch + growth probe).
- C-11 bridge fusion → REPRODUCED (one mesh, both contacts continuous
  in the v3 render).
- C-12 HDRI look-check → UNTESTABLE-IN-ROUTE in this lane (practice
  adopted in T-10; not exercised by the determinism gate).
- C-16 Draw-tool surface authoring → UNTESTABLE-IN-ROUTE in a headless
  lane (no interactive session); the estate equivalent — paths authored
  on the surface by construction — is what the rebuild exercises.
- C-17 zero-input collapse → UNTESTED (the estate group ships non-zero
  defaults per T-16, so the failure state was not re-created).

## Findings earned by the rebuild (not in the source)

- **F-1 — The Smooth finish eats the strand.** With the sheet's full
  stack (final form + Smooth 1.5×20), delivered girth measures
  **0.078–0.106 m diameter at nominal Radius 0.100** (cross-sections cut
  from the evaluated mesh: apex 0.078 × 0.098; drip 0.106 × 0.087). The
  identical group *without* the Smooth modifier measures **0.189–0.197 m**
  at Resolution 2/4/8 (probe `probe_res` series) — i.e., the volume stage
  delivers ≈ nominal girth, and Laplacian smoothing at 20 iterations on
  the coarse final-form mesh (voxel 0.05 m) contracts it to ~half.
  Estate consequence, written into the preset: **the Radius knob is
  nominal; budget ~2× radius, cut Smooth iterations, or raise
  Resolution (finer mesh shrinks less) when a target girth matters.**
  TECHNIQUE T-03/T-05 stand, with this calibration attached.
- **F-2 — Blender 5.2 scripting API for this chain differs from every
  pre-5.0 tutorial** (three separate traps, each probed to ground):
  (1) NodesModifier takes **no IDProperties** — `mod["Socket_N"] = v`
  raises TypeError; inputs live at
  `mod.properties.inputs.<identifier>.value`.
  (2) Points to Volume's Amount/Size choice is an **input enum**
  ('Resolution Mode'), not a node property.
  (3) Set Shade Smooth's geometry socket is named **'Mesh'**.
  The build script encodes all three; the next agent scripting GN on
  this pin should read `ns09_gn.py` before reaching for remembered API.
- **F-3 — Determinism is exact except one raster-scale tie.** Five of
  seven renders are pixel-identical across the two processes; the
  evaluated vertex counts are identical for **all** variants. v3/v4
  differ by **exactly 2 of 518,400 pixels** (0.0004%), at the same
  coordinates (502–503, 433) — a strand–sphere contact edge. A third
  render of runA's saved .blend is pixel-identical to runA, so the
  variance enters at build/evaluate time, not render time: consistent
  with a threaded marching-cubes tie-flip in Volume to Mesh at one
  marginal voxel. Bounded and named: single-strand shots (the route's
  primary use) are bit-exact; the two-body wide shot carries a 2-px
  evaluation variance. (Plan 07's Mantaflow gate, for comparison, was
  8/8 bit-exact — the solver route is *more* bit-stable at its contact
  edges than the volume-union route. Recorded against any assumption
  that procedural = perfectly deterministic.)

## Deviations from the sheet (declared)

- v2's Count 100 was my interpolation between the 660 s (Count 10) and
  1380 s (Count 100) panes for the 720 s radius; it falsified the lump
  expectation at that count, which is why v2b exists and is labelled a
  probe, not a sheet state.
- Paths are computed (deterministic arc/drip/bridge coordinates), not
  hand-drawn — the headless lane's equivalent of C-16.
- The final material (C-09b) is present in the preset JSON but the
  renders use the C-09 debug material deliberately: this gate judges
  geometry; the look is an Owner-eye item.
