# GATE ARTIFACT — Render-Lane Checklist (NS35 series)

- **Commission:** D-1071 (2026-11-06). **Status: LANDED** for the
  Night School programme's own use and the estate's candidate
  shelf. Adoption into skills/doctrine is a later gated step;
  nothing here edits any skill.
- **Closes:** Plan 35 PASS4 GAP 1 — "no artifact-side checklist
  for the 3D render lane incl. flat/unlit" (`runs/plan-35/
  PASS4-APPLICATION.md`, sha256 `cadf0029…`).
- **Provenance (honest, per Plan 35 TECHNIQUE.md §1, sha256
  `bbada5f2…`):** these checks are **re-sourced** — the Plan 35
  video yielded zero defect classes; every check below is
  sourced to the plan's pre-viewing categories × estate-evidenced
  defect classes (TG-round censuses, face-gate catalogues,
  character-art failure taxonomy). No check is attributed to the
  video or its creator.
- **Exercise evidence of record:** Plan 35 Pass 3 exercise
  (`runs/plan-35/PASS3-CANDIDATE-CHECKS.md`, sha256 `2591f385…`;
  sheets `gate-exercise/sheet-keepers-d802.jpg` sha256
  `eba3978c…`, `sheet-middle-tg4.jpg` sha256 `b6474c06…`,
  `sheet-bad.jpg` sha256 `c4356ed5…`) **plus** this commission's
  re-exercises in `EXERCISE-RECORD.md` (same dir): the C01
  manufactured-instance exercise (§A) and the scoped-C07
  re-exercise incl. round-TG originals (§B). Per-check pointers
  below name artefact + revision (sha256) per the D-1064 clause.

## How a verdict pack runs this checklist (GATE note)

1. **Source = the final delivered artifact** (the render/plate
   as shipped), never a viewport grab or pre-encode frame.
2. **Order:** C06 first (background leak — the TG gate order;
   a leaked ground poisons every later read), then C01
   (lighting — a flat/unlit frame makes shading-dependent
   checks unreadable), then C02, C10, C03, C04, C05, C07, C08,
   C09, C11.
3. **Who reads:** a vision evaluator reads each in-scope check
   at viewing size, plus native crops where the check names
   one (C02 limbs, C09 hands at ≥2×, C10 face). Per-item
   PASS / FIRE with the observed evidence named (feature,
   location) — impressions are not verdicts. The Owner's eye
   remains the verdict of record for adoption decisions.
4. **What a fire does:** any FIRE on an in-scope check fails
   the artifact at this gate with the defect named; the
   artifact returns for cure, it is not "noted and shipped".
   N/A (scope condition excludes the artifact) is recorded as
   N/A, never as PASS. Spec-relative checks (C03/C04) are run
   against the artifact's own written spec/benchmark; a check
   run spec-blind is an invalid run (see C04).
5. **Numbers are support only** (D-221): any numeric proxy
   rides under the visual read and never carries a verdict.

## The checks

### NS35-C01 — Flat/unlit figure read — **LANDED (proven, this commission)**
- **Defect (taxonomy L-2):** the figure carries no directional
  shading — form reads by silhouette only; no cast shadow
  consistent with the scene's other lit elements.
- **Detection:** visual at viewing size. Supporting proxy
  (never decisive): tight torso-core luminance spread —
  manufactured instance std 5.65 / 14 levels vs its lit
  original std 10.21 / 37 levels (`EXERCISE-RECORD.md` §A.3).
- **Scope:** all render classes. Cel-register plates are NOT
  fires: cel shading with directional tone + cast shadow is
  shaded (the TG/D-802 pools read no-fire, Plan 35 §3).
- **Exercise evidence:** Plan 35 pools — 0 fires on 20
  artifacts and **no instance existed** (UNPROVEN there).
  This commission: hunt found no genuine instance (record
  §A.1); manufactured instance `c01-instance/c01-flat-f0038.png`
  sha256 `38776c4b…` (Plan 01 scene copy, lights zeroed,
  world-only illumination; source scene sha256 `0bcd3bcd…`,
  variant script `c01-instance/ns71_c01.py` sha256 `04109c8b…`)
  — **C01 FIRES**; lit original `runs/plan-01/rebuild/frames/
  f_0038.png` sha256 `6588cddc…` — no fire. Proven both ways.

### NS35-C02 — Skin-block wash — **LANDED (proven, Plan 35)**
- **Defect (L-1):** unshaded salmon/tan blocks or gradient wash
  on skin where the cast register shades skin.
- **Detection:** visual at viewing size + native crop of limbs.
  **Scope:** shaded-register artifacts.
- **Evidence:** fires 2/7 known-bad, 3/3 rulable-middle
  (TG4-P1/Y2/A1 salmon knee patches, concording with
  REPORT-TG4 census), 0/10 keepers (PASS3 §3–§4).

### NS35-C03 — Garment/appearance spec violation — **LANDED (proven, Plan 35)**
- **Defect (M-1, F-1 hair):** specified colour, construction,
  or hair colour wrong.
- **Detection:** visual against the artifact's written spec.
  **Scope:** spec-bearing artifacts.
- **Evidence:** fires 5/7 bad (the Yui white-shirt class across
  TG2-Y2/TG3-Y1/TG4-Y1 et al.), 1/3 middle, 0/10 keepers.
  Highest-yield check in the Plan 35 exercise.

### NS35-C04 — Print error — **LANDED in spec-relative form only (proven, Plan 35)**
- **Defect (M-2):** print/glyph present where spec says none,
  or specified print migrated off its garment.
- **Detection:** visual against spec. **Scope:** spec-bearing
  artifacts. **Load-bearing clause:** specified body text /
  tattoos are NOT fires (Katya's specified "FREE USE" marking;
  Cordelia's D-799 corruption tattoo). The spec-blind form is
  **invalid** — it false-fires 2/10 keepers (PASS3 §3).
- **Evidence:** fires TG3-Y1 glyph print + TG4-Y2 alien print
  (shared with C03), 0/10 keepers in spec-relative form.

### NS35-C05 — Invented motif/accessory — **LANDED (proven, Plan 35)**
- **Defect (M-3):** floating hearts, invented crown/headpiece,
  unlisted props. **Detection:** visual census of the whole
  frame. **Scope:** all.
- **Evidence:** fires 2/7 bad (TG2-A2/A4 floating hearts),
  0/10 keepers.

### NS35-C06 — Background leak — **LANDED (proven, Plan 35) — run FIRST**
- **Defect (C-1):** tiled/giant faces, floating heads,
  hair-mass blobs, anchor elements in the ground.
- **Detection:** visual; checked first (TG gate order).
  **Scope:** plain-ground-spec artifacts.
- **Evidence:** fires 1/7 bad (TG2-Y1 face-pattern ground),
  0/10 keepers. Low frequency, gate-first severity.

### NS35-C07 — Framing crop — **LANDED in scoped form (proven, this commission); unscoped form PRUNED**
- **Defect (C-2):** head/feet cropped, figure incomplete.
- **Detection:** visual/measurable.
- **Scope (the landed form — the scope IS the check):** ONLY
  where the artifact's benchmark specifies full-body-in-frame.
  Where no such spec exists the check is N/A — deliberate
  partial crops are legitimate compositions.
- **PRUNED form:** the unscoped check — fires on 3/10 D-802
  keepers' deliberate crops (Kaisa hip crop, Maren bust crop,
  Manon waist-up crop). Pruned with that evidence (Plan 35
  PASS3 §3; re-verified this commission, `EXERCISE-RECORD.md`
  §B).
- **Exercise evidence (scoped form, this commission):**
  FIRES on round-TG originals under their full-body benchmark
  (`round-tg/SHOULD-BE-SEEN.md`: "full body head-to-feet… No
  cropped head/feet") — TG-P3 (head cropped out of frame)
  sha256 `0c909a85…`, TG-A2 (waist crop) sha256 `1bbc7397…`;
  no fire on 12/12 TG4 candidates (same benchmark, all full
  body with margin; cast sheet sha256 `bcd57241…`); 0 fires /
  3 N/A on the D-802 keeper pool. Proven both ways.

### NS35-C08 — Non-neutral stance — **LANDED (weak-proven, Plan 35 — flagged)**
- **Defect (A-2):** crossed/wide/dynamic stance where neutral
  is specified. **Detection:** visual against the benchmark
  stance line. **Scope:** neutral-stance-spec artifacts only.
- **Evidence:** fires 1/3 middle (TG4-A1 splayed arms), 0/7
  bad, 0 keepers (N/A on kink poses). Landed with its weak
  evidence stated: one concordant fire, no bad-pool instance.
  A future exercise with a bad-pool stance instance should
  re-gate this check.

### NS35-C09 — Hand defect — **LANDED (proven, Plan 35)**
- **Defect (A-1):** hands merged, hidden, claw-like, or not
  five-fingered. **Detection:** visual + native hand crop at
  ≥2×. **Scope:** hands-visible-spec artifacts.
- **Evidence:** fires 1/7 bad (TG2-A2 hands hidden in hair
  mass), 0/10 keepers.

### NS35-C10 — Face/identity defect — **LANDED (proven, Plan 35)**
- **Defect (F-1):** void eyes, missing pupils, wrong eye
  colour. **Detection:** visual + face-gate measurement where
  applicable. **Scope:** all.
- **Evidence:** fires 2/7 bad (TG2-A2/A3 solid black void
  eyes), 0/10 keepers.

### NS35-C11 — Proportion/register break — **LANDED (proven, Plan 35)**
- **Defect (A-3):** proportions or register contradicting the
  cast spec. **Detection:** visual; segment ratios as support.
  **Scope:** cast-spec artifacts.
- **Evidence:** fires 2/7 bad (TG2-A2 chibi register vs cel
  cast; TG2-A3 rough register), 0/10 keepers.

## Status summary

| Status | Count | Checks |
|---|---|---|
| LANDED (proven) | 10 | C01, C02, C03, C04 (spec-relative), C05, C06, C07 (scoped), C09, C10, C11 |
| LANDED (weak-proven, flagged) | 1 | C08 |
| PRUNED (form) | 1 form | C07-unscoped (3/10 keeper fires) |
| DROPPED | 0 | — (C01 was prove-or-drop; it proved) |

Final landed checklist: **11 checks** (NS35-C01…C11), every one
exercised against estate artifacts with fire and no-fire sides
of record in `EXERCISE-RECORD.md`.
