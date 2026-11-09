# BLOCH Candidate — Plan 34 (Night School)

- origin_lane: ntranch
- content_label: nsfw
- Candidate: **Pose in support-chain order, read at
  distance before hands, finish contact last.** Distilled
  from a DAZ posing timelapse (Plan 34) and verified in a
  controlled Blender comparison (same 4-pose set, same
  target table, two strict orders): (1) the chain that
  carries the weight is posed first — thighs for a sit,
  hips+legs for a stand, placement for a rider/second
  subject — with feet finished as their own late pass;
  (2) a scheduled mid-build distance read (front + side)
  lands BEFORE any hand/finger work — in the comparison
  it caught a seated pose's support defect while fixing
  it cost one pelvis delta, where the estate's
  verify-at-end caught the same defect only as post-build
  rework under finished hands; (3) contact is the
  terminal phase and the prop moves to the body, not the
  body to the prop — worth a measured 2.0 cm of hand
  registration on the contact pose (0.3740 m vs 0.3944 m
  hand→hip probe). Companion practice from the same
  session: capture poses as chain-scoped partial presets
  (proximal→distal selection) during the session and
  verify each by re-application to a reset figure.

## Friction log (D-1064)

- What cost time: the source host's DB-fatal 503s on the
  first sandbox fetch (retried through; known body, hash
  matched Plan 29's dossier). ~25 min of the download's
  10 min wall was two slow ranged segments (segments 3
  and 5 short-read once each and retried inside the
  script — no agent time, recorded in MANIFEST).
- What forced a guess: the estate baseline itself. The
  sprite-acting skill states layer principles
  (primary → secondary → ambient), not a body-chain
  sequence, so "the estate order" for the comparison had
  to be operationalised (INTAKE.md records the
  operationalisation and its basis, including Plan 02's
  observed gross→fine order). Any future order-vs-order
  comparison will hit the same gap until the skill names
  a chain sequence.
- Silent workarounds in successful runs: (a) the
  scene-change frame extractor fired 54,575 times on a
  screen recording (cursor motion = scene change) and
  its output was discarded — segmentation fell back to
  the 10 s grid + targeted Scene-pane crops, which
  carried the run; the discard is recorded in the run's
  detach log, not in any deliverable's headline.
  (b) The rebuild's per-stage re-touch counter resets
  with each Blender process, so the headline re-touch
  numbers were recomputed offline from the stage logs'
  phase bone lists (unified count, script in the run
  record) — the stage-local numbers (T 2, E 13) would
  have told a false story if quoted directly.
  (c) Whisper slices queued behind ~13 sibling whisper
  jobs on a saturated primo; slice 840 took ~6.6 min of
  compute (its own timing log) across ~25 min of queue.
  The no-commentary verdict waited for all three slices
  rather than concluding from two.

## Artefact pointers

- `runs/plan-34/TECHNIQUE.md` §1 (grammar T1–T10 +
  conformance), §2 (revision triggers with counts) —
  night-school-20261105, this run, 2026-11-06.
- `runs/plan-34/PASS3-REBUILD.md` — the controlled
  comparison (steps/re-touches/corrections/probe/renders
  table) + claims scored.
- `runs/plan-34/rebuild/build_pose.py` (SHA-256
  f32ecbf8faf689b0bdd034fefbe10536609754e1de808ba52fc082cc21dfcddf)
  — the two-order build script and shared target table.
- `runs/plan-34/rebuild/final-pairs-sheet.jpg` + per-pose
  `run{T,E}-pose{1..4}-s{1,2}-log.json` — renders and the
  step/re-touch source logs (primo copies in
  `~/.local/share/pax/night-school/plan-34/out/`).
- `runs/plan-34/OBSERVATION.md` §§2–5 — the decision log
  the grammar was distilled from (164 frames; named-node
  Scene-pane evidence).

## Per-edit attribution

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| Posing order (comparison run T) | Legs/pelvis before spine/head; feet as own pass; hands after a mid-build read; contact terminal | vs estate run E on identical targets: +5 phases, re-touches at parity (14 vs 13), but both read-corrections landed pre-completion (E's one correction was post-build rework); pose-4 hand probe 0.3740 m vs 0.3944 m | adapt (adopt read + contact-terminal + support-first rule; retain look-leads-head for animation) |
| Mid-build distance read | Two Workbench previews (front+side) inserted after the arm phase in run T | Caught pose 2's perch/dangle defect and pose 4's floating hand while the fixing phases were still open; cost 8 preview renders ≈ +1.42 s render wall over the set | adopt |
| Re-touch accounting | Headline counts recomputed as unified instances from concatenated stage logs | Stage-local counters (T 2 / E 13) inverted the truth; unified counts (T 14 / E 13) show parity and move the verdict onto correction timing, where the evidence actually is | adopt (as reporting practice for staged builds) |
| Scene-change segmentation | Threshold-0.35 scene extraction for pose boundaries | 54,575 hits on a screen recording — pure cursor noise; discarded, grid + Scene-pane crops used instead | reject (for screen-recording sources; frame-difference segmentation needs a cursor-masked or pane-cropped variant) |
