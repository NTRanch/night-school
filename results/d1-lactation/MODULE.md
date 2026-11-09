# D-1 Stage 2 — Lactation Module (fluid layer, six-girl standard §6.3)

- **Date:** 2026-11-06 · **Route:** Blender 5.2.3 LTS, Mantaflow FLIP,
  scripted headless on primo, one heavy job at a time, `nice -n 10`.
- **Casting flag (binding on every record in this run):** the Owner
  ruling names **Maren** as canon lead. Maren is a Strobe-cast name
  with **no rig in this fleet** and nothing in this run is named for
  her. Per SIX-GIRL-STANDARD §6.3, **Alma is the fleet's reference
  implementation**; demonstration clips are shot on **Alma (lead,
  reference implementation) + Prima (control girl)**, labelled
  **PENDING OWNER CASTING CONFIRMATION** (coordinator recommendation:
  Alma). The module itself ships for **all six girls** on evidence
  (§7 of GATE-RECORD.md).
- **Foundations consumed, not modified** (sha256 verified before and
  after; see GATE-RECORD §1): SIX-GIRL-STANDARD §§4/6 (nipple anchors
  `Anchor_Fluid_Nipple.L/.R` exist on every conformed rig and track
  `m` by the §6.2 derivation); Plan 07 locked preset
  (`preset-torogao-flip-viscous-ch1.json`); Plan 06 fluid machinery
  of record (`fluid-layer-record.json`, PASS3-REBUILD.md).

## 1. Emitters

- One inflow emitter per breast, seated at the **derived** nipple
  point: the §6.2 rule (per-x-half front apex of the bust band,
  centreline guard |x| > 0.005·RS per Errata E-1, +2 mm proud along
  −Y) evaluated on the body mesh **at the scene's bust setting m**
  in-scene at build time — never from stored coordinates (§4.4).
  The stored anchor empty is read back and compared (record field
  `anchor_vs_derived_mm`); at m ≠ 1.00 the empty does not track
  (it is Spine2-parented) and the derived point governs — that is
  the §4.4 rule, recorded per clip.
- Emitter geometry: UV sphere, **radius 0.016 m**, centre offset
  **+30 mm** from the derived point along the mode's emission
  direction, so the sphere does not intersect the body surface
  (Plan 06 route finding: emitting-side effector overlap kills
  inflow velocity; the offset keeps the source in open space —
  the geometry lesson this module is built around). Offset was
  revised 18 → 30 mm in probe round 1 (the one allowed revision;
  bound ≤ 30 mm met exactly).
  Radius justification (solver floor, measured in Plan 06 §7):
  sources under ~1.5 cells seed ≈ nothing; at this module's cell
  (0.0125 m, §3) r = 0.016 m spans 1.28 cells — the Plan 06 working
  point (r 0.024 m at cell 0.019 m = 1.26). The radius is a solver
  parameter, not an anatomical claim.
- Both breasts emit symmetrically in every mode (no mode in this
  spec is asymmetric).

## 2. Modes (mechanical definitions, Mantaflow terms)

Common: `flow_behavior = INFLOW`, `use_initial_velocity = True`,
`velocity_coord` = the mode velocity (sampled once at bake start
by Mantaflow — the body is at rest in these scenes, so the static
hold costs nothing; Plan 06 §5 deviation does not bind here).
Sourcing is switched **only** by the threshold gate: `use_inflow`
keyed ON exactly while the mode's gate schedule is open (Plan 06
T-19 — a magnitude-0 flow value alone does not stop sourcing;
this module never keys flow magnitude, only the gate channel).

| Mode | Gate schedule (24 fps samples) | `velocity_coord` (m/s) | `velocity_random` | Character |
|---|---|---|---|---|
| **drip** | 3 pulses: ON 6–9, 18–21, 30–33; OFF elsewhere | (0, −0.20, −0.30) | 0.0 | Low gated flow; discrete droplets detach under gravity between pulses |
| **stream** | Continuous ON 6–24 | (0, −2.20, −0.40) (speed 2.24) | 0.0 | Continuous gated inflow at authored velocity, open-geometry flight, parabolic fall to the ground plane |
| **spray** | Continuous ON 6–24 | (0, −2.60, −0.35) (speed 2.62) | **0.90** | Inflow with authored velocity spread: random component 0.90 m/s on a 2.62 m/s carrier ⇒ authored cone half-angle ≈ atan(0.90/2.62) ≈ **19.0°** |

**Revision 1 (probe-driven, 2026-11-06; probes in `probes/`):**
round-1 probes at the originally drafted velocities (stream 1.20,
spray 1.58 m/s) measured young-particle forward velocity at
≈ 30 % of authored (stream −0.31…−0.39 of −1.15 m/s, sustained —
flight, not creep; Plan 06's open-geometry class) and a
near-vertical fall landing on the legs. Authored velocities were
raised (stream ×1.9, spray ×1.7) so the achieved arc lands clear
of the body on the ground plane. The 30 % birth-velocity ratio at
cell 0.0125 m on the locked viscous preset is recorded as the
route's measured transfer, not hidden. Gate window shortened
30 → 24 (bake-cost bound; emission character unchanged).

Flow parameters of record (defaults; named, per clip in its
`run_record.json`): gate on/off samples (above), inflow velocity
(above), emitter radius 0.016 m, emitter offset 18 mm, seed 7.

## 3. Shared layer settings (locked preset, unchanged)

From `preset-torogao-flip-viscous-ch1.json`, read back per build:
`viscosity_value` **0.05632** (set ONLY — the 5.2 base/exponent
trap), `surface_tension` **10.0**, FLIP ratio 0.97, particle
radius 1.43, particle number 2, particle randomness 0.1,
mesh particle radius 2.933, mesh generator IMPROVED,
`resolution_max` **110** on this module's domain (dims
0.75 × 1.30 × 1.50 m, centre (0, −0.40, 0.72)) ⇒ **cell 0.0136 m**
(emitter spans 1.17 cells; probes at res 120 seeded ≈ 290
particles/frame for the pair and the res-110 builds seed in the
same class — per-clip counts in GATE-RECORD). Resolution is an
integration-layer choice per Plan 06 T-15's rule (chosen against
the smallest surface — the 16 mm emitter — not a preset change;
the preset's own 50 was its floor for a 24 mm emitter in a
0.95 m domain; at cell 0.0208 m (res 72) this emitter spans
0.77 cells and would seed ≈ nothing, per Plan 06 §7's measured
collapse 467 → 20 particles for a comparable shrink). Domain was
widened after round-1 probes (stream front reached the −0.80 m
wall; spray reached +0.29 m of a ±0.30 m wall). Domain covers the
bust + full fall zone to the ground plane (z ∈ [−0.03, 1.47]);
the body effector is the girl's full evaluated `<Girl>_Body`
(collision active in-domain; fluid exists only in-domain,
recorded as the domain-scope note in the gate record). Ground
plane effector at z = 0. Effectors: `<Girl>_Body` (subframes 2,
surface_distance 0.0), ground plane.

**Two recorded deviations from the preset's letter, both
module parameters (stated here, evidenced in GATE-RECORD):**
(1) `mesh_particle_radius` **1.2**, not 2.933 — at cell
0.0125–0.0136 m the preset multiplier (calibrated at Plan 07's
0.152 m cell) inflates the surface to 50–70 mm columns
(round-1 probe renders), against the look register's thin
strands; 1.2 yields ≈ 35–40 mm columns with natural mid-fall
beading. (2) `delete_in_obstacle` **True** — the Plan 06
particle-death cure class, invoked after round-1 probes measured
splash-tunnelled interior particles inside the shin volume
(onset f18–20, ≤ ~1.6 % of particles, pre-cure numbers in
GATE-RECORD §5); with the cure, interior reads 0 (verified per
clip). Neither deviation touches the locked physical core
(viscosity 0.05632, surface tension 10.0, FLIP 0.97, particle
radius 1.43).

**Per-mode viscosity:** the locked value 0.05632 is used for
**all three modes** — no per-mode deviation is taken. Justification
from the look register of record (cast end-sheet + Maren's D-802
cell, read 2026-11-06): the effect reads as opaque white strands
and beads that hold together and run down in thin coherent
rivulets — the viscous, strand/droplet-forming class the locked
preset was built for (Plan 07 purpose line). A sensitivity strip
(viscosity ×0.1 / ×1 / ×10 on Alma stream at canon, frame 22) is
run and recorded in GATE-RECORD §6 so the choice is evidence, not
assertion; any future per-mode tune enters as a recorded module
parameter amendment, not a silent build change.

**Material:** opaque white fluid — Workbench diffuse
(0.96, 0.95, 0.93, 1.0) on the domain mesh (the Plan 06/07
evidence-material route), roughness read as matte-opaque at
viewing size; the look register's droplet scale (beads/strands
of a few mm) is what the mesh particle radius 2.933 at cell
0.0125 m produces (≈ 4–8 mm surface features) — recorded as the
scale correspondence, judged as an eye item.

## 4. Scene & bake protocol (identical to Plan 06)

- Solo-girl scene per clip: her conformed `.blend` (primo staging
  copy, hash-verified), rest pose, outfits/hair/cages
  `hide_render` (bodies-only evidence, Plan 01/06 precedent),
  `Body_Bust_Size` set to key value **2(m−1)** on Body + Outfit +
  OutfitEnd, anchors re-derived in-scene (§1), camera pair
  (full frame + bust camera), Workbench 960×540, threads fixed 4,
  24 fps, frames 1–36 (stream/spray) / 1–40 (drip).
- **Tier 1 working cache:** `<clip>/cache/` on primo (Mantaflow
  `data/` + `mesh/`), never edited in place; a parameter change
  is a new variant directory.
- **Tier 2 Alembic:** mesh-only `.abc`, frames 1–end, scene
  metres, exported per clip and round-trip probed (verts + bbox
  vs sim-side measurement at gated frames) per Plan 06 §3.
- **Determinism scope (fleet limitation, carried):** particle
  counts reproduce exactly; mesh/pixel determinism is claimed
  only for the gated window (per clip, §5), late frames recorded
  honestly. Twin build = second independent Blender process,
  identical inputs.

## 5. Gates per clip (as tasked)

1. **Interior:** particles inside the girl's real Body mesh
   (two-axis ray parity, Plan 06 measure route) = **0 at gated
   frames**; loop-wide counts reported, transients judged by the
   Plan 06 rule (no two consecutive frames with interior > 0 in
   the gated window is a fail; any interior event is reported).
2. **Determinism (twin build):** particle counts identical at
   every measured frame; decoded-pixel hashes equal at gated
   frames; Tier-1 mesh cache byte-identical at the first gated
   frame (the layer's Contact-equivalent) where behaviour
   allows, reported per Plan 06 scoping.
3. **Mode legibility (measured):**
   - drip: mesh island count + detachment record across the
     pulse cycle (discrete bodies separating from the emitter
     column between pulses);
   - stream: continuous mesh column (single island spanning
     emitter→landing) across the gate-open window + landing/
     spread record on the ground plane;
   - spray: particle cone half-angle measured from positions
     (90th-percentile angle about the carrier axis, gated
     frames) vs authored 29.6°.
4. **Anchor verification:** derived nipple points at the clip's
   m equal the §6.2 derivation (z pinned at bust.z·ZS ±2 mm;
   Δy vs canon in the fix step's recorded track class).

Gated frames: drip {12, 24, 36}; stream/spray {14, 20, 28};
determinism pixel/mesh gates judge {first two gated frames}.

## 6. Proposed standard §6.3 amendment text (standard NOT edited)

> §6.3 (add): The lactation module of record is
> `runs/d1-lactation/MODULE.md`: emitters at the derived
> `Anchor_Fluid_Nipple.L/.R` points (sphere r 0.016 m, +18 mm
> along the emission direction, open-space seating per the
> Plan 06 overlap finding), modes drip (3 gate pulses,
> v (0, −0.20, −0.30) m/s) / stream (gate 6–24 at 24 fps,
> v (0, −2.20, −0.40) m/s) / spray (gate 6–24, carrier
> (0, −2.60, −0.35) m/s, velocity_random 0.90, authored cone
> ≈ 19.0°), on the locked Plan 07 preset (viscosity 0.05632,
> surface tension 10.0) at module resolution 110 (cell
> 0.0136 m), mesh_particle_radius 1.2 and delete_in_obstacle
> as recorded module parameters. Sourcing is gate-switched only (T-19). Bake
> protocol and determinism scope are Plan 06's. Casting:
> Maren is lead-as-ruled; Alma is the fleet reference
> implementation (see the casting note above) — demonstration
> evidence in `runs/d1-lactation/GATE-RECORD.md`, pending
> Owner casting confirmation.
