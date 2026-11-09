# Bloch candidate — D-1 Stage 2 lactation module

- origin_lane: ntranch
- content_label: nsfw
- evidence: `runs/d1-lactation/GATE-RECORD.md`, `MODULE.md`,
  `probes/` (round-1 + revision probe records on primo staging
  `~/.local/share/pax/nslac/out/probe_*`), Plan 06
  `runs/plan-06/PASS3-REBUILD.md` §5–§6.

## Candidate lessons

1. **Mantaflow FLIP particle locations are world-space in the
   estate route; the mesh is not.** In Blender 5.2.3, for a fluid
   domain created at a non-origin location, `particle.location`
   already reads in scene/world coordinates, while evaluated mesh
   vertices are domain-local. Applying `matrix_world` to particle
   locations double-counts the domain translation (here +0.72 m
   in z, −0.40 m in y) and silently displaces every
   particle-space measurement — centroid, cone, landing, and any
   interior test built on the shifted points reads a phantom
   scene. Verification is one landmark: newborn particles must
   cluster at the known emitter position. (Process note for the
   coordinator: Plan 06's `ns06_measure.py` applies
   `mw @ p.location` with a domain centred (0, 0.025, 0.65); if
   the same space rule held there, its interior gate measured
   points shifted +0.65 m in z. Its other gates — counts, mesh,
   pixels — are unaffected. Flagged for coordinator review, not
   asserted as a defect without a re-probe of that scene.)

2. **Birth-velocity transfer at fine cells is ≈ 30 %, and it is
   a transfer, not a failure.** At cell 0.0125–0.0136 m on the
   locked viscous preset (viscosity 0.05632), young-particle
   forward velocity measures a sustained ≈ 0.30 × authored
   `velocity_coord` in open geometry — flight with a reduced,
   stable ratio, distinct from the Plan 06 pocket creep
   (≈ 0.05 m/s, no travel). Authored velocities for an
   open-geometry emitter must be sized by the measured transfer
   (≈ ×3) when a landing point matters; judging flight by
   authored-vs-achieved at face value mislabels a working
   emitter as a creep.

3. **Splash tunnelling is the interior-defect class for
   open-geometry emitters, and `delete_in_obstacle` is its
   cure.** With a body effector at surface_distance 0, subframes
   2, a falling stream's ground-splash particles tunnel into the
   shin volume (onset when the splash crown reaches the legs;
   ≤ ~1.6 % of particles; they persist once inside). Moving the
   emitter +12 mm did not cure it (onset moved 2 frames, counts
   same class). `delete_in_obstacle = True` (the Plan 06
   particle-death cure class, held on standby there) reads
   interior 0 at every frame with counts otherwise in class.
   Pre- and post-cure numbers must both be recorded; the cure
   deletes, it does not deflect.

4. **Gate-off stops sourcing, not the total particle count.**
   With the gate channel OFF from frame 25, a near-emitter census
   (< 60 mm of the emitter centres) goes 157–177 (gate open) →
   partial at 25 → **0 from frame 26** — sourcing stops exactly.
   Yet the total particle count keeps growing after gate-off
   (Alma stream 3,983 @ f24 → 4,305 @ f28): Mantaflow reseeds
   particles into newly wetted cells to hold `particle_number`
   per cell as the fluid spreads. A gate audit that reads only
   total counts will falsely report a leaking gate; audit
   sourcing at the emitter, not at the total. (Plan 06's "counts
   frozen" gate form held for its confined geometry because the
   fluid stopped spreading; open-geometry spreading does not
   freeze totals.) Evidence: `clips/alma_m100_stream_A/
   sourcediag.log`, `applicability/appl_*/sourcediag.log`,
   per-clip `measurements.json`.

5. **Preset meshing multipliers do not travel across cell
   scales.** `mesh_particle_radius` 2.933, calibrated at a
   0.152 m cell (Plan 07) and serviceable at 0.019 m on a thin
   interface layer (Plan 06), inflates a free column at a
   0.0125 m cell to 50–70 mm ropes; 1.2 reads ≈ 35–40 mm with
   natural mid-fall beading. A preset's dimensionless multipliers
   are calibrated against its cell size and fluid geometry
   class; re-derive them when either changes, and record the
   value as a module parameter, never as a silent edit.
