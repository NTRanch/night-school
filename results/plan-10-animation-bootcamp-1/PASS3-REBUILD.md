# Plan 10 — Pass 3 Clean-Room Rebuild

Rebuilt from `TECHNIQUE.md` alone (no video open): the episode's
exercise surface in estate form — a deterministic, scripted,
headless F-curve evaluator (`stage/fcurve_exercises.py`, pure
Python + PIL; a keyframe segment evaluated as a cubic Bezier in
(frame, value) space, handle types as constraints on the two
control points) plus the two exercises the sheet specifies.
Blender itself is not the estate's shipping form for this
material; the mechanism (keys + handle semantics) is, and the
evaluator implements the mechanism from its definition.

## Exercise 1 — the 14-frame loop, Vector vs Auto (C-10-3, C-10-4)

Keys (sheet abstraction of the episode's channel form, metres):
(1, −0.490) (5, −0.560) (7, −0.657) (9, −0.560) (14, −0.490) —
sparse keys, matched ends, trough at the mid key, exactly the
shape read off the screen (OBSERVATION 22:00).

- **Vector:** spacing is piecewise-constant per segment
  (−0.0175 ×4, −0.0485 ×2, +0.0485 ×2, +0.0140 ×5) with jumps
  at the keys — constant speed, corners at keys. The demo's
  V-curve, reproduced numerically.
- **Auto:** spacing varies at nearly every step
  (−0.0156, −0.0143, −0.0169, −0.0233, −0.0555, −0.0415,
  +0.0425, +0.0545, +0.0203, +0.0148, +0.0116, +0.0108,
  +0.0124) — ease into and out of the trough.
- Both close the loop identically (wrap step 0.0): handle type
  changes the motion **without moving a single key** —
  **C-10-3 REPRODUCED with measured difference**, **C-10-4
  REPRODUCED** (the construction itself).

## Exercise 2 — companion idle gesture, family + one pulled handle (C-10-2, C-10-6)

12-frame gesture, keys (1, 0) (3, +0.012 anticipation) (6,
−0.030 drop) (9, 0 settle) (12, 0). Two-level authoring per
the slide's TIP: Auto family for the action, then ONE Free
handle pulled (into the settle key, pull −0.55).

- Keys identical in both runs; only the handle differs.
- The pull **holds the drop longer, then arrives faster**:
  frame 7 −0.021444 (pull) vs −0.024222 (auto-only); approach
  spacing into the settle key **0.012889 vs 0.010444 (+23%)**.
- **Settle overshoot (C-10-6) REPRODUCED as a defect:** with
  NO pull and no key past rest, the Auto curve still crosses
  rest after the settle key: **+0.002222** at frame 10,
  decaying by 12 — the auto tangent at a flat key after a
  moving segment manufactures an overshoot nobody keyed. This
  is the episode's "removing unwanted overshoots" item,
  measured in the estate's own evaluator.

## Claims not rebuilt here

- **C-10-1 / C-10-7** (editor division of labour; Dope Sheet
  bulk timing): UI-workflow claims about Blender itself.
  Their estate content is the three-layer model + the
  timing/spacing split, adopted in TECHNIQUE and exercised
  structurally above (keys moved = timing layer; handles =
  curves layer; the evaluator keeps them separate by
  construction). Marked **ADOPTED-AS-MODEL**, not reproduced —
  there is no Blender UI in the estate's shipping form to
  reproduce them in.
- **C-10-5** (Motion Paths): Adapt verdict in TECHNIQUE; the
  estate check-form (trajectory strip + spacing series) is
  seeded by the exercise strips; the full two-body
  trajectory-with-keys render is the named follow-on with
  Plan 35 GAP 2 (D-1071), not built in this run.
- **C-10-8**: PENDING-TRANSCRIPT at rebuild time (see
  REPORT.md for final status).

## Determinism

All four exercise strips rendered twice: decoded-pixel SHA-256
identical run-to-run, 4/4 (`measurements.json` → determinism).
The evaluator is a pure function of the key list — no seed, no
clock, no Blender. Full measurements: `stage/measurements.json`.
