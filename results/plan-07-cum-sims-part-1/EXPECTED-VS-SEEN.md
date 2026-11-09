# Plan 07 Pass 4 — Expected-vs-Seen Benchmark (written BEFORE final renders are inspected)

- Written: 2026-11-06 ~02:04 PST, after the Pass 3 bakes were launched on primo
  (02:02:38 PST) and **before** any main-run frame was viewed. The only frame
  seen before this benchmark is the 30-frame probe (frame 30), used solely to
  verify the build runs and to fix camera framing.
- Route: Blender 5.2.3 LTS Mantaflow FLIP (estate fallback per coordinator ruling).

## SHOULD-BE-SEEN (from OBSERVATION.md result class + plan gate)

1. **Emission**: a coherent viscous column falls ~5 m from the 2 m sphere
   source at 6 m height; the stream stays connected (1 mesh island) while
   emission is on (frames 1–90).
2. **Impact + pooling**: the column reaches the ground plane (mesh min-z ≈ 0,
   within one cell = 0.152 m), pools and spreads slowly — no bounce, no
   pass-through, no explosive splash (viscosity class, not water class).
3. **Cutoff**: after the keyframed cutoff at frame 90, the column necks,
   separates into droplet/strand islands (island count > 1 in frames
   ~100–160), and the falling remnant lands; total mesh volume stops growing.
4. **Settle**: by frame 250 the fluid is a settled pool on the plane
   (island count back to 1, min-z ≈ 0, vertex count stable vs frame 180).
5. **Sensitivity direction**: viscosity ×0.1 reads visibly thinner/faster with
   more breakup; viscosity ×10 reads visibly thicker/slower with less breakup
   and a taller standing column at matched frames. Direction, not magnitude,
   is the gate.
6. **Determinism**: identical decoded-pixel hashes for mainA vs mainB at all
   six matched frames. Any mismatch FAILs this item as measured (no rounding).
7. **Preset artifacts**: NSFW preset file + SFW delta preset exist, parse as
   JSON, and every value in them traces to either TECHNIQUE.md or a recorded
   route deviation in PASS3-REBUILD.md.
8. **Cache contract**: an Alembic file exported from the baked main run exists
   and is non-trivial in size (the estate-route handoff evidence).

## Verdict rule

Per-item PASS/FAIL is recorded in PASS4-APPLICATION.md as the agent's read.
The Owner's eye is the verdict of record for items 1–5; those are queued as
eye items regardless of the agent read.
