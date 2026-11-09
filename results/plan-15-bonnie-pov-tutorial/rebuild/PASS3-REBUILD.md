# Plan 15 — Pass 3: Rebuild (viewpoint rig on the Plan 01 loop)

Date: 2026-11-06. Blender 5.2.3 LTS (`/usr/bin/blender`, primo).
Clean-room: built from TECHNIQUE.md's sheet alone. The Plan 01
scene was COPIED, never edited in place:
`plan01-scene-copy.blend` sha256
`0bcd3bcd9149b0972769a83fce6a0313c894890ebb1d9e890a37432faf97d6ab`
(matches the Plan 01 record). Scene census on the copy: two
54-bone armatures (Prima = Follower, Yui = Leader/viewpoint
character), ContactEmpty, NSCam (fixed camera), fluid anchors,
lattice cages; 60 fps, loop = samples 0–78 (Contact 38,
follower peak 45).

## The rig (final, runC/runD)

- **POVAnchor** (Empty): Child Of constraint →
  `Armature_Yui:mixamorig:Head`, all location/rotation/scale
  axes, Influence 1.000. Inverse set manually to the frame-0
  head-bone world matrix inverted; measured set-inverse delta
  **0.000008 mm**. The anchor's frame-0 pose places the eye at
  the head-bone matrix applied to the bone-space offset
  (0, +0.10, +0.09) → world (0.00389, −0.10648, 1.21056),
  aimed at the frame-0 contact target (Prima Hips head +
  (0, 0, 0.05)) = (0, 0.0618, 0.7509). The camera therefore
  rides the viewpoint character's head bone exactly — the
  SFM-sheet mechanism (shot camera bound to the viewpoint
  character's head set), with the estate's bone in place of
  the separate head model.
- **POVBob** (Empty, plain child of POVAnchor, identity
  parent-inverse): the authored head-motion layer, keyed on
  the Plan 01 Leader phase table {0: 0, 15: 0.12, 26: 0.55,
  38: 1.0, 45: 0.92, 53: 0.38, 65: 0.15, 78: 0} — forward
  0.012 m and dip 0.006 m at p = 1, pitch +1.1° at p = 1,
  roll 0.35° × sin(2 cycles/loop). 6 f-curves, LINEAR +
  CYCLES(REPEAT). Frame-78 keys equal frame-0 keys (seam law).
- **POVCam**: plain child of POVBob, identity local — the
  camera frame IS the bob frame. Lens **21 mm**,
  clip_start 0.02, 960×540, BLENDER_EEVEE. Body presence is
  not faked: the viewpoint character's real body (head
  excluded by the eye position at the face plane) is in the
  scene and in frame wherever the sightline reaches it.

Saved scene: primo
`plan-15/rebuild/runC/scene/pov_scene.blend` (active camera
POVCam). Build script: `rebuild/build_pov.py` (identical for
runC/runD).

## Runs and per-edit attribution

| Run | Change vs previous | Observed difference | Verdict |
|---|---|---|---|
| A | First build: eye offset in WORLD axes (head0 + (0, 0.055, 0.045)); bob f-curve access via legacy path | Camera landed inside Yui's hair mesh — all POV frames blank brown; `bob_fcurves: 0` | FAIL — two defects, each isolated below |
| B | Eye offset moved into head-BONE space (head_mat0 @ (0, 0.10, 0.09)); f-curves via `strip.channelbag(slot)` | Eye at world (0.00389, −0.10648, 1.21056), clear of the hair bbox; `bob_fcurves: 6`; frames render the partner's back at ~0.17 m | PASS as a rig; framing finding below |
| C/D | Lens 28 → 21 mm AND aim target Hips+0.10 → Hips+0.05 (both in one step) | Wider framing, contact anchor centred (480.0, 291.5 mean); occlusion unchanged | `confounded` between the two edits for framing differences vs runB; determinism pair C≡D (below) |

## The framing finding (measured, not impressionistic)

Ray-cast record (runC build record, `occlusion`): at every
evidence frame (0/19/38/45/58/78) the first render-visible
surface on the eye→contact ray is **Prima_Body at
0.056 / 0.111 / 0.158 / 0.046 / 0.055 / 0.056 m**, while the
contact point itself is 0.47–0.49 m from the eye. At the
follower peak (s45) her back comes within **4.6 cm** of the
eye. The Plan 01 blocking — partner seated upright, back to
the leader — puts her torso across the sightline at every
phase; a head-locked camera on this scene cannot frame the
contact set, and the rig was NOT cheated off the head to see
around her (benchmark item 6). The source's all-fours blocking
keeps the partner's back low and the sightline open; that
difference is a Pass 2/Pass 4 finding, not a rig defect.
Partner-hidden diagnostic (`diag38_nopartner.png`): with the
partner removed, the same framing shows the viewpoint
character's own chest edge, both forearms and both hands at
the grips — the presence geometry is in frame; the partner's
silhouette and the inherited single-material evidence setup
are what hide it in the full render.

## Registration measurements (runC, `runC-measurements.json`)

Screen space 960×540, full loop n = 79 (samples 0–78):

| Track | POV (21 mm, head-locked) | Fixed NSCam (Plan 01 record rig) |
|---|---|---|
| Contact anchor (Prima Hips) | mean (480.02, 291.45), std (0.055, 2.907), range (0.180, 9.231) px | mean (458.71, 266.01), std (0.307, 0.213), range (1.096, 0.762) px |
| Yui pelvis (thrust point) | std (0.192, 3.456), range (0.720, 10.911) | std (1.685, 2.629), range (5.438, 9.170) |
| Prima Spine2 (follower reaction) | std (0.560, 30.992), **range_y 100.727 px**; s38 y=66.56 → s45 y=162.84 (96 px in-frame shift) | std (2.299, 0.513), range_y 1.918 px |

Hand registration (world, inherited from the loop — the
camera cannot change it; stated for the comparison): frozen-
offset definition L max **4.9389 mm** / mean 0.7918, R max
**4.9277 mm** / mean 0.7921 — identical to Plan 01's own
hand record (4.9388/0.7918, 4.9276/0.7921) to ~0.0001 mm,
which validates the whole measurement chain against Plan 01.
Nominal-grip definition: max 6.0191/6.0108 mm.
Hand screen error under the POV camera (projected hand vs
projected grip point): nominal max **1.086/1.138 px**,
frozen max 1.881/1.877 px. Hand projections at the peaks sit
in-frame at the partner's sides (s38: L (577.2, 290.8),
R (382.9, 287.2)).
Contact-lock anchor drift under the Child Of head lock:
**≤ 0.0001 mm** across the loop (same bound as Plan 01's
contact lock).

## Determinism

runC and runD (same script, same scene copy) — decoded-pixel
sha256 (`pixelhash.py`, Blender-decoded pixels, never PNG
bytes) identical for all seven frames; runC values:
pov_0000 `074d8858…`, pov_0019 `f2253101…`, pov_0038
`8090f5cb…`, pov_0045 `98b549f5…`, pov_0058 `99f5c526…`,
pov_0078 `074d8858…` (≡ pov_0000 — the seam is pixel-
invisible), fixed_0038 `570ee7fa…` — which also matches
Plan 01's own recorded f_0038 hash prefix, proving the scene
copy bit-faithful and the fixed-camera record reproducible
inside this build.

## Benchmark reads (BENCHMARK.md, written before runC)

1. Embodied closeness — **PASS** (agent read): partner's
   back/hips fill the centre at every peak; at s45 her back
   fills nearly the whole frame; platform shows only at the
   edges. No frame reads as a detached shot.
2. Self-presence — **FAIL as a visible read / PASS by
   projection**: the viewpoint character's hands project
   in-frame at the grips (≤1.14 px screen error) and the
   partner-hidden diagnostic shows her chest/arms/hands in
   this exact framing, but in the full renders her body is
   not visually distinguishable — the partner's silhouette
   covers the arm lines and both characters share the
   inherited pale evidence material. Eye item for the Owner.
3. Registration under motion — **PASS**: contact anchor
   inside the central box at every peak (s38 (480.07,
   295.83); s45 (479.96, 297.18)); full-loop travel 9.23 px
   vertical (inside the 5–25 px band), 0.18 px horizontal
   (the anchor sits on the view axis — recorded, not hidden).
4. Follower reaction reads in-frame — **PASS**: Spine2
   range_y 100.7 px under POV vs 1.92 px fixed (~52×).
5. Seam invisible — **PASS** (hashes above).
6. Named occlusion, honestly shown — **PASS**: ray record
   above; the frames show the occluded geometry (back
   centred, contact anchor projected centre-frame behind
   it); the camera never left the head.

Evidence frames: `rebuild/runC-frames/` (pov_0000, pov_0019,
pov_0038, pov_0045, pov_0058, pov_0078, fixed_0038).
