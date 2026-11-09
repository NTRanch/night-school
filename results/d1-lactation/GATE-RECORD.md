# GATE RECORD — D-1 Stage 2: the lactation module

Status: COMPLETE (build + gates), 2026-11-06. All numbers below trace
to a named artifact in this run dir (`records/gate-table.json` is the
machine summary; per-clip `run_record.json` / `measurements.json` /
`pixelhash*.txt` / `meshhash.txt` / `*.abc` + `abc_probe.log` are the
primary records). Primo staging (Tier-1 caches + baked blends) remains
at `~/.local/share/pax/nslac/` — the Plan 06 two-tier working record.

CASTING (resolved): the Owner ruling names Alma as the
lactation demonstrator lead (D-1055, 2026-11-07; SIX-GIRL-
STANDARD §6.3 names Alma the fleet's reference implementation
— Torogao canon; her D-798 core kink is lactation).
Demonstration clips are shot on **Alma (lead)** + **Prima
(control)**. The "PENDING OWNER CASTING CONFIRMATION" flag
this block originally carried is retired: the earlier
Amendment 2 casting named "Maren" (a Strobe-cast name with NO
rig in this fleet; Maren keeps her Strobe-lane lactation canon
but leads nothing here), and D-1055 settled the fleet casting
on Alma. Nothing anywhere is named Maren. (Header updated
2026-11-08 per D-1088 repair.)

## Foundations consumed (verified by sha256 BEFORE and AFTER the work)

| Artifact | sha256 (unchanged) |
|---|---|
| `night-school-20261105/SIX-GIRL-STANDARD.md` | b6806f55ea721e0a… |
| Plan 06 `runs/plan-06/rebuild/fluid-layer-record.json` | 14cc68544494f6a7… |
| Plan 07 `runs/plan-07/rebuild/preset-torogao-flip-viscous-ch1.json` | 010cc8b8978a63d0… |
| Fleet blends prima / alma / yui / sloane / lux / piper | 50dfd83c… / 3e2cd41d… / d766d925… / b86e5e8f… / d7ce10e5… / 07873e14… |

Look register consulted (look only): cast end-sheet
`torogao-cast-rigs-20261026/art-candidates/STYLE-AUTHORITY-20261028/
cast-end-sheet-nsfw.jpg`; Maren's D-802 cell
`strobe-kink-stylesheet-20261103/stills/still-maren.png` — opaque
white, thin coherent strands/beads of a few mm leaving the nipples,
beading on skin.

Tenancy at build time: primo carried light tenants only (a tokenizer
job ≈1 core, ComfyUI on :8191, Azoth jobs); all bakes ran single,
`nice -n 10`, `OMP_NUM_THREADS=8`. Nothing audible at any point.

## The module as built (MODULE.md Revision 1 — as-built spec)

- Emitters: paired UV-sphere INFLOW objects (r = 0.016 m) centred
  30 mm from the derived nipple point along the emission direction
  (the one mechanism revision, at its stated bound — see probes).
  Nipple points DERIVED in-scene per §6.2 (+2 mm proud), never from
  the stored anchor, never hand-moved.
- Gate rule: `use_inflow` keyframing only (T-19). Drip: ON windows
  6–9, 18–21, 30–33 @24 fps. Stream/spray: ON 6–24.
- Modes: **drip** vel (0, −0.20, −0.30), random 0 — gravity-driven
  pulses. **stream** vel (0, −2.20, −0.40) (‖·‖ 2.24), random 0.
  **spray** carrier (0, −2.60, −0.35), `velocity_random` 0.90
  (authored cone ≈ 19.0°).
- Locked core kept on every build (read back per build in each
  `run_record.json.preset_readback`): viscosity_value 0.05632,
  surface_tension 10.0, FLIP ratio 0.97, particle_radius 1.43,
  particle_number 2. Domain resolution_max 110 (cell 0.0136 m) over
  dims (0.75, 1.30, 1.50) m centred (0, −0.40, 0.72).
- Two recorded module-parameter deviations from the shared-layer
  defaults, both evidence-driven (MODULE.md §2/§5):
  `mesh_particle_radius` **1.2** (2.933 produced 50–70 mm ropes at
  this cell size; 1.2 reads ≈ 35–40 mm strands with natural beading)
  and `fluid.delete_in_obstacle = True` (the Plan 06 particle-death
  cure class; cures the splash-tunnelling interior defect below).

## Flight probes (probes/, Alma canon, actual bust geometry)

Round 1 (emitter offset 18 mm, res 120, pre-revision velocities) and
revision probe r1 (offset 30 mm, meshR 1.2, widened domain) —
`probes/probe_*/measurements.json`, `run_record.json`:

- **Flight, all three modes — no creep.** Young-particle forward
  velocity sustains ≈ 27–32 % of authored across modes and clips
  (stream −0.58…−0.70 m/s of −2.20; spray −0.65…−0.82 of −2.60;
  round-1 probes same class at lower authored values). This is the
  open-geometry regime Plan 06 predicted (its V1/V10 probes): real
  travel (centroids 0.6–0.97 m by late frames), NOT the pocket creep
  (≈ 0.05 m/s, no travel). The ≈ 30 % transfer is a stable solver
  property at this cell size on the locked preset — authored
  velocities in Rev 1 are sized ×~3 for it (BLOCH candidate lesson 2).
- A measurement-space trap was found and fixed first: Mantaflow
  particle locations are WORLD-space here; the first probe reads
  double-counted the domain translation. Newborn-cluster checks now
  anchor every particle-space measure (BLOCH lesson 1).
- **Interior defect found in probes (pre-cure):** stream interior 0
  through f16, then 26 @ f18 … 82 @ f24 — localised inside the RIGHT
  SHIN volume: ground-splash particles tunnelling through the body
  effector. The +12 mm offset revision did NOT cure it (r1: 20 @ f20
  → 95 @ f32). `delete_in_obstacle` DID (all clips below: 0 at every
  measured frame, both builds). Drip never showed the defect.

## Per-clip gates (twin builds A/B; artifacts in clips/<id>_{A,B}/)

Gate criteria per clip: interior = 0 at gated frames (loop-wide max
also reported); particle counts identical A/B at every measured
frame; decoded-pixel hashes equal at the first two gated frames;
Tier-1 mesh cache byte-identical at the first gated frame; Tier-2
Alembic exported + round-trip probe.

| Clip | Interior gated A/B | Loop max A/B | Counts A=B | Pixels (2 gated) | Mesh byte-eq | Bake A/B (s) |
|---|---|---|---|---|---|---|
| alma_m100_drip | 0/0 @12,24,36 | 0/0 | YES | EQUAL | YES (b5ec452b…) | 353.8/353.8 |
| alma_m100_stream | 0/0 @14,20,28 | 0/0 | YES | EQUAL | YES (e381ee41…) | 363.0/358.4 |
| alma_m100_spray | 0/0 @14,20,28 | 0/0 | YES | EQUAL | YES (e01028b5…) | 375.9/372.6 |
| alma_m150_stream | 0/0 @14,20,28 | 0/0 | YES | EQUAL | YES (47dc4e33…) | 327.1/324.9 |
| prima_m100_stream | 0/0 @14,20,28 | 0/0 | YES | EQUAL | YES (978d59d8…) | 372.5/372.7 |
| prima_m100_drip | 0/0 @12,24,36 | 0/0 | YES | EQUAL | YES (1f7be77d…) | 312.2/312.5 |
| prima_m150_stream | 0/0 @14,20,28 | 0/0 | YES | EQUAL | YES (d6be6f66…) | 334.2/332.9 |

Determinism verdict: STRONGER than the fleet's recorded scope —
counts identical AND pixel-equal at gated frames on all seven clips,
with the body static (no mo-cap in scene, the Stage 1 divergence
driver is absent). Late-window behaviour recorded per clip in
`measurements.json` (counts keep growing post-gate by reseeding —
see below — identically in both builds at every measured frame).

Alembic round-trip (Tier 2): reimported verts/bbox MATCH the
in-scene measurements exactly at probed frames (e.g. alma stream
f14/f20/f28: 4,378 / 8,764 / 12,022 verts, identical bboxes) —
`clips/<id>_A/abc_probe.log`; ABC sha256 in `records/gate-table.json`
(alma stream A: 6f5380d759471b9d…; 34,328,803 bytes).

### Gate-timing proof (all stream builds + all applicability builds)

`use_inflow` evaluates OFF from f25 on both emitters
(`scripts/gatediag2.py` readback). Sourcing census
(`sourcediag.log` per build): particles within 60 mm of the emitter
centres = 98–177 during the gate, partial at f25 (last cohort
leaving), **0 from f26** — on Alma stream and on Yui/Sloane/Lux/
Piper alike. Total counts keep growing after f25 by solver
reseeding into newly wetted cells (Alma stream 3,983 @ f24 →
4,305 @ f28) — recorded as BLOCH lesson 4; it is not gate leakage.

### Anchor derivation per setting (in-scene, §6.2 rule)

| Build | Derived nipple L (x, y, z) | vs stored anchor |
|---|---|---|
| Alma m=1.00 | (0.04472, −0.14555, 1.33791) | 0.0 mm (== canon anchor) |
| Alma m=1.50 | (0.04472, −0.16500, 1.33791) | Δy 19.449 mm — == Stage 1's recorded −0.16500 track to the digit; z pinned |
| Prima m=1.00 | (0.04219, −0.12610, 1.21294) | 0.0 mm |
| Prima m=1.50 | (0.04219, −0.13878, 1.21294) | Δy 12.684 mm — == the fix-step Prima track (±12.7 mm) |

(§6.4's landmark table lists the pre-offset apex vertices; the
anchors sit +2 mm proud of them by construction — the derived points
reproduce the placed anchors exactly at canon on all six girls.)

## Mode legibility — measured (per-clip measurements.json)

- **Drip:** islands 2 @ f8 → 3 @ f12–36 (Alma), 2–5 (Prima) — the
  mesh body count steps UP at each pulse boundary (detachment
  events; counts frozen between pulses modulo reseeding: 330 @ f10
  = 330 @ f12). Agent read of `renders/bust_frame_0020.png`: two
  discrete white droplet bodies bead ON the torso front below the
  bust — droplets detach from the emitter, fall a short distance,
  contact the torso and bead there (the look register's "beading on
  skin" behaviour). Drip = discrete droplets, PASS on measures.
- **Stream:** mesh present every frame of the gate window; islands
  13–17 mid-window (a beaded jet, not a single glassy column —
  recorded, not dressed up); landing: Alma canon first ground
  contact f18 (73 particles z<0.03), 289 @ f20 → 2,387 @ f36, pool
  centroid y ≈ −0.66…−0.79; Prima canon lands LATER and further
  forward (first contact f30; 580 @ f36; centroid y −0.99, pool
  reaching the domain front region); **Prima m=1.50: NO ground
  contact inside the 36-frame window** (bbox z-min 0.163 @ f36 —
  the arc is still airborne/accumulating forward at window end).
  Fast-droplet outliers reach the domain front wall (−1.037 m)
  from ~f14 in stream/spray clips — a domain-extent limitation of
  record; the visible dense core lands well inside (renders).
- **Spray:** young-particle VELOCITY cone p90 = 6.5–14.5° vs
  authored 19.0° — the birth cone is NARROWER than authored; the
  visible fan develops downstream (position-cone p90 42–55° by
  f14–24, fall-conflated; islands 27–38 vs stream's 13–17; lateral
  bbox ±0.20 m). At the bust, spray reads as paired strands like
  stream (closeups3) — its differentiation is fragmentation and
  spread in flight, weaker than the authored cone implies. Spray
  ships as a measured variant, honestly below its authored claim
  (velocity_random 0.90 does not deliver a 19° birth cone at this
  cell/viscosity; the FLIP solve's own dispersion dominates).

## Sensitivity strip (Alma stream canon, frame 22; sensitivity/)

| Viscosity | Mesh verts | Islands | Lateral bbox x (m) | Read |
|---|---|---|---|---|
| ×0.1 (0.005632) | 9,162 | 13 | −0.359…+0.112 | slumps/spreads laterally, splash-back behind emitter plane |
| ×1 locked (0.05632) | 10,048 | 13 | −0.075…+0.228 | tightest coherent beaded column |
| ×10 (0.5632) | 10,908 | 50 | −0.081…+0.364 | paste-like: shatters into beads, wide scatter |

The locked value is the coherent-strand point of the three — the
module keeps viscosity at the Plan 06/07 lock for all modes, no
per-mode viscosity deviation (MODULE.md §2).

## All-six applicability (applicability/appl_<girl>/)

Short stream bakes at canon for the four girls without clips —
derived point == stored anchor (0.0 mm) for every girl; derived
points match §6.4 apex + 2 mm proud; sourcing first frame = 6
(45–61 particles); gate-off proven by the near-emitter census
(0 from f26); interior 0 at gated frames AND loop-wide max 0:

| Girl | Derived nipple L | First sourced | Interior max |
|---|---|---|---|
| Yui | (0.03966, −0.11003, 1.10268) | f6 (54) | 0 |
| Sloane | (0.04219, −0.12441, 1.23500) | f6 (61) | 0 |
| Lux | (0.04134, −0.12412, 1.21294) | f6 (49) | 0 |
| Piper | (0.04092, −0.11975, 1.24970) | f6 (45) | 0 |

The module ships for all six on this evidence.

## Benchmark reads (BENCHMARK.md L1–L7; agent reads — NOT Owner verdicts)

- L1 origin at nipples, symmetric: PASS on measures (derived points,
  symmetric sourcing counts) + closeups3 reads (strands emerge at
  the under-bust band both sides). First closeup pass framed
  mid-fall, second framed the upper chest (both kept, labelled);
  third pass frames the origin band.
- L2 material/register: PASS (agent read) — opaque white, beaded
  strands ≈ 35–40 mm at the column, droplets of a few mm in drip;
  no grey/translucent reads in any viewed frame.
- L3 stream arc + landing: PARTIAL — dense core lands in front of
  the feet on Alma canon and reads as a coherent falling column in
  `renders_gated/full_frame_0020.png`; BUT the achieved trajectory
  is steeper than the authored-arc expectation (birth transfer
  ≈ 30 %), Prima lands late/far, Prima m150 lands outside the
  window, and the island measure says beaded jet (13–17), not one
  continuous column.
- L4 drip discreteness: PASS on measures + bust-render read (above).
- L5 spray fan: PARTIAL/below authored claim — see legibility
  section; fan is a downstream fragmentation fan, birth cone
  7–14° vs 19° authored.
- L6 m-tracking: PASS — derived Δy +19.449 mm (Alma) / +12.684 mm
  (Prima) at m=1.50 with z pinned, matching the standard's tracks;
  closeups3 m150 read consistent (origin band follows the bust).
- L7 determinism evidence present per clip: PASS (table above).

## Eye items queued for the Owner (no Owner PASS is claimed anywhere)

1. Mode legibility at viewing size, per mode (Alma canon set):
   does drip read as dripping, stream as a stream, spray as a
   spray — against the D-802 register.
2. Spray's differentiation from stream: measured (islands/spread)
   but visually subtle at the bust — Owner call on whether the
   mode earns its place as specified or returns for a cone
   mechanism revision.
3. Stream arc steepness (L3): accept the ≈ 30 %-transfer arc, or
   raise authored velocity further (landing point moves forward;
   domain front wall then binds harder).
4. Prima m=1.50 stream landing outside the 36-frame window —
   accept, extend the window, or treat as a per-girl arc note.
5. Casting confirmation: Alma as lead (this record's labelling).

## Deviations & limitations of record

- mesh_particle_radius 1.2 and delete_in_obstacle=True are module
  parameters (MODULE.md §5), not edits to the shared preset; the
  Plan 07 preset file is untouched.
- Domain front wall at y = −1.05 m clips fast-droplet outliers
  (stream/spray) and Prima's late pool; gated-frame gates are
  unaffected (interior/determinism judged on the body, not the
  wall), but a production domain should extend forward.
- Renders are bodies-only Workbench evidence frames (outfits/hair
  hidden per the Stage 1 route), not presentation renders.
- `nslac_measure.py` interior test uses particle positions against
  the evaluated body mesh — the D-1 Stage 1 method; counts of
  record are particles, per the fleet convention.

Artifacts: MODULE.md (spec + proposed §6.3 amendment text — the
standard itself was NOT edited), BENCHMARK.md, scripts/ (all build/
measure/render/abc/hash scripts + drivers), probes/, clips/,
applicability/, sensitivity/, records/gate-table.json,
BLOCH-CANDIDATE.md (origin_lane ntranch, content_label nsfw —
5 lessons, incl. a flagged-for-review note on Plan 06's measure
script, not asserted as a defect).

## Code home (2026-11-08, per D-1088 repair)

The module's code is homed at `repo/results/d1-lactation/
scripts/` (canonical copy, beside MODULE.md in the results
tree); the `runs/d1-lactation/scripts/` copy is the original
working copy and carries a CODE-HOME pointer. Module status
unchanged: all hard gates PASS; spray legibility stands BELOW
AUTHORED CLAIM (cone p90 6.5–14.5° vs 19° authored) — a
residual of record, not repaired here.
