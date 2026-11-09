# Plan 28 — Pass 3 Clean-Room Rebuild Record

- **Date:** 2026-11-06 · **Route:** Blender 5.2.3 LTS headless on
  primo, scripted, deterministic. **Only source used:** TECHNIQUE.md
  in this run dir (video/transcripts closed during the build).
- **Donor pair (coordinator's example, per brief):** **Alma's head
  onto Prima's body** — copies staged to primo
  `~/.local/share/pax/night-school/plan-28/src/` and hash-verified
  against the fleet originals (alma.blend sha256 `3e2cd41d…`,
  prima.blend `50dfd83c…`); fleet files never modified. Distinct
  proportions, measured: Alma 1.82 m vs Prima 1.65 m overall;
  at the neck weld ring (spec z 1.452 × each girl's z-scale):
  ring radius **52.51 mm (Alma) vs 48.02 mm (Prima)** — the donor
  ring is 9.3% wider; head height above the ring **252.66 mm vs
  230.07 mm** (+9.8%). Both rings carry exactly **24 verts**
  (the fleet's `weld_rings.neck = 24`, verified in the geometry).
- **Interpretation of the estate method (stated per brief):** the
  skill's five steps target Genesis/foreign-rig grafts; on the
  conformed fleet its practice of record is the builder's form —
  ring-exact weld + template weight field — which is what
  Method B implements. The skill's fusion/fix steps are identity
  on this pair (one shared 54-bone armature) and are recorded as
  such, not simulated.
- **Method A (theirs, as distilled):** head cut at its ring; ring
  planes made coincident; each head ring vert snapped exactly
  onto its angle-paired body ring vert (Snap-Selection-to-Active
  analogue; max drag **5.121 mm**); data join (Ctrl+J analogue);
  Merge by Distance weld at the Blender default **0.001 m**
  (189 verts removed: 24 ring + 124 pre-existing coincident
  construction pairs + 41 pairs in the 0.1–1.0 mm band — their
  own run reported 33, theirs being a single 33-point ring on
  meshes without construction doubles); weights = donor field
  kept (the fleet form of their group-renaming, names already
  matching) + 3× neighbour smoothing (factor 0.5) on Neck/Head
  groups over the seam corridor (their repeated Smooth); their
  delete/F-fill/knife patch branch **did not trigger** (counts
  match 24 = 24) and their hand touch-up painting is unscriptable
  — omitted, recorded.
- **Method B (estate):** donor head scaled XY ×**0.9145** (ring
  ratio) and Z ×**0.9106** (head-height ratio) about its ring;
  ring verts snapped to the body ring (max residual before snap
  **0.447 mm** — vs A's 5.121 mm of drag); weld at 0.0001 m
  (148 verts removed: the same 24 + 124 construction pairs);
  weight field re-derived from Prima's template profile over the
  corridor (z > cut − 50 mm); smooth normals across shared verts.
- **Build host discipline:** primo, one heavy job at a time in
  this run's lane (primo-wide load ≈ 29–35 from sibling whisper
  jobs throughout; all runs `nice -n 10`, detached, file-mediated
  `ns28-*` in `~/.local/share/pax/detach/`). Nothing audible.
- **Artifacts:** `rebuild/build_headhack.py` (sha256 `c85cf6ff…`),
  `rebuild/bend_test.py` (`71638ffe…`), `rebuild/headhack_both.blend`
  (`e85980e2…`, both joins + the Prima armature),
  `rebuild/build_record.json`, `rebuild/measures.json`,
  `rebuild/renders/` (20 Workbench frames: 2 methods × 5 poses ×
  front/side). Primo copies in `~/.local/share/pax/night-school/plan-28/out1/`.

## Bend test (identical for both; poses on the Prima armature)

Poses (Neck / Head pose-bone Euler, achieved head-axis tilt
measured from the evaluated pose): **rest** 0° · **flexion**
Neck +25° / Head +20° → **45.0°** · **extension** −18° / −12° →
**30.0°** · **yaw** Y +30° / +20° → **50.0°** · **lateral**
Z +15° / +12° → **27.0°**.

Measures (from `measures.json`; corridor ladder = 3 mm z-bins,
CUT−30 mm … CUT+48 mm, centroid/radius/mean-normal tracked per
bin, posed vs rest):

| Pose | Measure | A (theirs) | B (estate) |
|------|---------|-----------:|-----------:|
| flexion | head-part kink max | **7.207 mm** @ z 1.462 | 5.041 mm @ z 1.423 (whole-mesh) |
| flexion | weld-edge strain max / mean | **0.613 / 0.092 mm** | **0.007 / 0.002 mm** |
| flexion | body-side normal-step change max | **38.78°** @ seam | 11.37° |
| extension | head-part kink max | 5.128 mm @ 1.462 | 3.672 mm |
| extension | weld strain max / mean | 0.511 / 0.057 | 0.003 / 0.001 |
| extension | body-side normal-step change | 35.98° @ seam | 8.57° |
| yaw | head-part kink max | 1.627 mm | 1.138 mm |
| yaw | weld strain max / mean | 0.532 / 0.089 | 0.007 / 0.003 |
| lateral | head-part kink max | 4.338 mm @ 1.462 | 3.037 mm |
| lateral | weld strain max / mean | 0.274 / 0.063 | 0.003 / 0.001 |
| lateral | body-side normal-step change | 37.13° @ seam | 7.65° |

Reading: **neither seam opens** (both are welded; max weld-edge
strain is sub-millimetre in both). The cost of their method is
concentration: weld edges strain **~88×** more at flexion
(0.613 vs 0.007 mm max), the deformation kink sits *above* the
weld in the dragged ring band (z 1.462, every pose) and is
28–43% larger than the estate's, and the body-side shading
normal step at the seam moves **36–39°** under flexion /
extension / lateral against the estate's 8–11°. The estate's
cost is elsewhere and is not in this table: the head was
uniformly shrunk 8.6% / 8.9% to fit (identity, C-12).

Agent seam reads from the renders (Owner eye items in PASS4):
flexion side view — A shows a visible notch/step at the back of
the neck and a throat bulge (two pieces hinged); B shows a
continuous neck curve with a faint weld line. Flexion front —
A's collar step and throat crease read clearly; B's seam is a
hairline. At rest both read clean at this camera distance except
A's slightly-too-large head (donor proportions kept).

## Determinism

Build + bend run twice as independent processes (primo `out1`,
`out2`): **`measures.json` identical, `build_record.json`
identical** (excluding the recorded pair/position lists, which
also matched in count). The .blend bytes differ between runs
(Blender session metadata); the determinism claim rests on the
measures, per estate practice.

## Claims (OBSERVATION) — verdicts

| Claim | Verdict | Evidence |
|-------|---------|----------|
| C-01 longer donor neck eases fit | ADAPTED-OUT | Fleet parts are cut at their rings by construction; the stump has no analogue. The underlying quantity (per-point travel) is what snap distance measures: A 5.121 mm max. |
| C-02 ring parity precondition | REPRODUCED | 24 = 24 on this pair; patch branch (delete/F-fill/knife) never triggered — the precondition held by construction. |
| C-03 snap correspondence avoids stretch | REFUTED as stated | Snapping *relocates* the stretch into the ring band: it reappears under bend as weld strain 0.613 mm max (88× estate) and a kink at z 1.462 in every pose. At rest it is indeed invisible — their check was a rest/material-preview check. |
| C-04 UV names must match pre-join | UNTESTABLE-IN-ROUTE | Fleet meshes share one UV/palette convention; the class is adopted as a checklist item in PASS4 instead. |
| C-05 Ctrl+J + Merge by Distance = one mesh that won't separate | REPRODUCED | Welded A seam: max separation-class strain 0.613 mm at 45° flexion — holds. (Their "33 verts" is their ring size; ours removed 189 at the same default distance, mostly construction doubles.) |
| C-06 colour seam is texture work | NOT REBUILT — by construction | Fleet girls carry one palette per character; the problem the step solves does not arise. Recorded as an estate gap for foreign textured donors (TECHNIQUE step 7). |
| C-07 weights by group renaming | REPRODUCED (analogue) | Donor field kept under matching names deforms the graft (all poses achieved); its cost is the kink/strain concentration above. |
| C-08 smoothing + touch-ups prevent cracking | PARTIALLY REPRODUCED | 3× smoothing applied; the "cracking" analogue (weld strain + normal-step excursion) remains 3–88× the estate's — smoothing mitigates, does not equalise. Their hand touch-up loop is unscriptable and was not simulated. |
| C-09 armature fusion = join + reparent | IDENTITY-IN-ROUTE | One shared armature; nothing to fuse. The step is confirmed as the source's actual procedure (transcript), which re-founds the skill's step 3 (PASS4). |
| C-10 stray donor bone wrecks the neck | UNTESTABLE-IN-ROUTE | No foreign bones exist on this pair. Adopted as a named sweep (PASS4) on the strength of the source's own failure report. |
| C-11 face/jaw/eye fix is separate named work | CONFIRMED as practice | Matches the skill's step 4 exactly; nothing to rebuild on a pair whose face bones are already the template's. |
| C-12 donor proportions never rescaled | REPRODUCED — and priced | A keeps Alma's head at full donor size; B shrinks it 8.6%/8.9%. This is A's clean win on the identity axis. |

## Corrections to my own first read (recorded per doctrine)

The frame-only first pass read the join as "overlap + Ctrl+J,
unwelded" (the donor neck visibly extends below the seam line in
d_2760). The join-window transcript refutes it: the weld
(Merge by Distance) and the snap correspondence are narrated
operations that happen between grid frames. The first build of
Method A (overlap, unwelded, profile-repainted weights) was
discarded and rebuilt to the transcript-verified method; the
discarded run's measures are not reported anywhere above.
Lesson filed in the bloch candidate (screen-first has a floor:
sub-minute operations between grid frames need the transcript
before Pass 2 is written, not after).
