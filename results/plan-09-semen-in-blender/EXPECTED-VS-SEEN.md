# Plan 09 — Pass 4 Expected-vs-Seen (rebuild predictions, pre-registered)

Written BEFORE the Pass 3 build runs (2026-11-06, ahead of primo execution).
Each item states what the sheet predicts the rebuild will show; the SEEN
column is filled from run artifacts only (renders + run_record.json), and
mismatches are reported as-is, never re-worded.

| # | EXPECTED (from TECHNIQUE.md / OBSERVATION.md) | SEEN (filled after the run) |
|---|---|---|
| E-1 | v1_firstform (Count 10, Voxel Amount 64, Radius 0.5 m) renders as a blobby volume mass swallowing the proxy sphere — the sheet's 660 s failure state (C-02). | SEEN in shape class — v1 renders an oversized dimpled fused mass arching the sphere (6,432 verts), not a strand. His 660 s state was a fog-blob around a scribble path; mine is the same failure on an arc path. |
| E-2 | v2_lumps (Count 100, Radius 0.25 m) renders as a chain of distinguishable fused lumps along the path — continuity visibly broken vs v3 (C-03). | NOT SEEN as parameterised — v2 at Count 100 renders a SMOOTH rope: at ≈0.04 m spacing the lumps cannot form. Corrected by probe v2b (Count 24, same radius): ribbed/lumped as predicted. The prediction's mechanism was right; its count was wrong (the 720 s count was never pane-read). |
| E-3 | v3_final (Length 0.001 m, Voxel Size = 0.100/2.000, Radius 0.100, Smooth 1.5×20) renders as ONE continuous smooth strand draped over the sphere, with a drip descending the front — matching the sheet's ~840 s / 1740 s states in shape class. | SEEN — v3 is one continuous smooth strand over the sphere with a descending drip (1,162 verts), shape class matching the sheet's 840 s/1740 s states. Girth caveat under E-5/F-1. |
| E-4 | v3's bridge curve fuses to BOTH spheres with no seam/gap at either contact (C-11) and sags as authored (no solver sag added). | SEEN — the bridge is a single mesh fused at both spheres in the v3 render, sagging exactly as authored (a straight-authored catenary-free span; no solver sag, as predicted). |
| E-5 | v4_bodyradius (Radius 0.025) renders the same paths as visibly finer strands (~¼ the girth of v3), still continuous (C-06). | SEEN with calibration — v4 strands are visibly finer and continuous; measured delivered girth in the final form runs ≈half the nominal diameter (F-1: Smooth-modifier contraction), so the 4:1 class ratio holds but absolute girths need the preset's 2× budget note. |
| E-6 | Evaluated-mesh vertex counts order as v1 < v2 < v3 ≈ v4 or v3 > v4 > v2 > v1 — in any case v3's count exceeds v1's by ≥2× (sampling density claim, Finding 3). The exact order is reported as measured; a violation of the ≥2× claim fails this item. | FAILED as written — counts order v1 (6,432) > v4 (7,494 total) > v2 (3,790) > v3 (1,916 total); v3 does NOT exceed v1. The prediction conflated sampling density with mesh density: coarser voxels + a thinner strand produce fewer vertices. The density claim survives only in its correct form (continuity, E-3), not in vertex counts. |
| E-7 | The whole build evaluates with NO bake step and NO cache directory created (the route's defining property); wall time for all four variants + animation probe < 10 min on primo. | SEEN — no bake step exists in the script, no cache directory was created by any run, and the full build (4 variants + probe) took 2.21 s / 1.76 s wall per process, far under the 10 min bound. |
| E-8 | Determinism: a second process running the identical script produces pixel-identical renders (decoded-pixel hashes equal) for all 7 images. | PARTIAL — 5 of 7 renders pixel-identical; v3/v4 differ by exactly 2 of 518,400 px at one contact edge, traced to build-time evaluation (a third render of the same .blend is identical), consistent with a threaded marching-cubes tie-flip. Vertex counts identical everywhere. See PASS3 F-3. |
| E-9 | Animation probe: the three growth states (0.15 / 0.55 / 1.0) render as the same strand with the drip at three lengths, re-evaluated per state with no bake — the estate-side motion mechanism (T-11) is constructible. | SEEN — anim_f01/f12/f24 show the same strand with the drip at three authored lengths, each re-evaluated independently with no bake; all three pixel-identical across processes. |
| E-10 | The strand does NOT pool, spread by physics, or separate into droplets in any variant — any appearance of those would falsify Finding 4/T-12 and must be reported as a surprise, not a feature. | SEEN (as a negative) — no pooling, spreading or separation appears in any variant; strand feet meet the sphere as authored. Nothing falsified Finding 4/T-12. |

## Application gate (Pass 4 proper, scored after Pass 3)

The NSFW application this plan exists for: **name the estate's default
route for the D-1 demonstrator's fluid layer and for Torogao strand-class
shots generally**, A/B against Plan 07's Mantaflow route on the Plan 07
evidence (preset + cache contract + its 7 PASS / 1 FAIL agent read) and
this plan's Pass 3 evidence, per shot class:

- **Class A — posed strand/drape/bridge shots** (fluid already where it
  belongs, shaped by the drama): predicted winner = Plan 09 route
  (exact path control, volume-union contact, zero bake, deterministic).
- **Class B — emission/travel shots** (fluid arrives from somewhere:
  Plan 06's shot class): predicted winner = Plan 07 route by default
  (Plan 09 has no travel), with Plan 06's ratified contact-interface
  extrusion (D-1069) owning the contact moment itself.
- **Class C — free dynamics** (splash, separation, pooling physics):
  predicted = Plan 07 route alone; Plan 09 structurally cannot enter.

Predictions are recorded here so the Pass 4 verdict can be checked
against them; if the renders contradict a prediction, the verdict
follows the renders.
