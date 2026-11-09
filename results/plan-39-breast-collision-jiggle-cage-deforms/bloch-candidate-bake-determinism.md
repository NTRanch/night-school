# Bloch candidate — Plan 39 bake-determinism lesson (2026-11-06)

- origin_lane: ntranch
- content_label: nsfw
- Claim: **A Blender cloth bake is bit-deterministic — and that
  proves nothing about the sim.** Five independent bakes of a
  byte-identical scene (cloth-on-cage + Surface Deform, Blender
  5.2.3) produced 96/96 bit-identical point-cache files
  (combined sha256 stable across every bake), including a
  parameter set under which the solver *diverges to NaN by
  frame 4*: the explosion itself reproduced bit-identically,
  and replays of two baked copies agreed to 0.0 m at every
  finite cell. Determinism gates for baked physics must
  therefore pair the cache-hash check with a viability check
  (finite at every frame, cage-level deviation bounded) — a
  hash-identical cache can be a hash-identical failure.
  Companion harness claims: (1) toggling a cloth modifier in a
  process holding a baked scene frees the bake — in-process
  A/B isolation by toggle silently measures the un-simulated
  state (read 0.0 mm), and cache files are deleted on disk
  (96 → 10); measure secondary motion by replaying the baked
  scene and a separately built no-cloth reference scene in
  fresh, toggle-free processes, stepping sequentially.
  (2) A body-level render/displacement gate can mask a dead
  cage entirely: with its target NaN, Surface Deform's
  contribution collapses and the body reads as clean skeletal
  follow — cloth gates must measure the cage, not only the
  body it drives.
- Evidence: `~/workspace/night-school-20261105/runs/plan-39/
  BAKE-DETERMINISM.md` (§§2–4 determinism tables, §3 divergence
  measurements, §6 route findings R-1…R-3); artifacts in the
  same run dir (`bake/runB/blendcache_cloth_scene/` — 96 cache
  files, sandbox-rehashed to the recorded combined hash;
  `bake/{runA,runB,varA}/` bake records; `bake/ref/replay.json`
  reference replay); build/bake/replay scripts in
  `runs/plan-39/work/`.
