# D-1 Stage 1 — Demonstrator Record (stacked two-body stack, all six girls)

- **Date:** 2026-11-06 · **Route:** Blender 5.2.3 LTS headless on
  primo, scripted, one heavy job at a time (tenants noted: Unity +
  llama-server active on primo during the window; builds ran
  `nice -n 10`, sequential, ≥27 GiB RAM free throughout — timings
  are therefore not exclusive-performance numbers). Nothing audible.
  File-mediated detached runs (prefix `nsd1-`), completion read from
  `.done` files and per-step status log (`records/status.log`).
- **The stack:** Plan 01 contact loop + Plan 39 §5.2 jiggle layer +
  Plan 06 fluid layer (gated anchor-attached contact-interface
  **extrusion** — the shipped form of record; the free jet stands
  refuted in-geometry per Plan 06 §5 and was not re-litigated),
  retargeted per girl under the six-girl standard (§7 proof:
  `RETARGET-PROOF.md`). Locked fluid preset read back in every
  build: viscosity_value 0.05632, surface_tension 10.0, resolution
  50 (cell 0.019 m).
- **Pipeline:** `scripts/build_stack.py` (loop + jiggle, adapted from
  the Plan 01/39 scripts of record), `scripts/retarget.py` (§7 clip
  retarget), `scripts/nsd1_fluid.py` / `nsd1_measure.py` /
  `nsd1_render.py` (Plan 06 scripts generalized by girl), driven by
  `scripts/run_all.sh`. Every number below traces to
  `records/gate-table.json`, assembled by `scripts/analyze.py` from
  the per-build artifacts it names. **No girl is HELD** — every
  casting passed its gates; the two fluid late-window exceptions
  are recorded in §4/§6, not hidden.

## 1. Casting matrix (7 builds + 2 Alma bust spot builds)

| # | Follower | Leader | Note |
|---|---|---|---|
| 01 | Prima | Yui | **Control** — the ingredient casting; reproduces all three ingredient records exactly (RETARGET-PROOF §5) |
| 02 | Yui | Prima | ingredient pair, roles reversed |
| 03 | Alma | Prima | |
| 04 | Sloane | Prima | troupe follower — heart channel dropped |
| 05 | Lux | Prima | troupe follower — heart channel dropped |
| 06 | Piper | Prima | troupe follower — heart channel dropped |
| 07 | Prima | Alma | **role swap** — see note |
| 08 | Alma (m=0.50) | Prima | bust spot proof (§5) |
| 09 | Alma (m=1.50) | Prima | bust spot proof (§5) |

**Role-swap note (recorded ambiguity, resolved in the open):** the
tasking's matrix already contains "Prima leads, Alma follows" as
build 03 (Alma is a follower, Prima her leader). Build 07 therefore
executes the *distinct second direction* of the pair — Alma performs
the leader-authored part, Prima the follower-authored part — so the
matrix contains both directions of Prima↔Alma, and the literal
reading is covered by 03. Fluid pairing in every build: emitter =
Leader's `Anchor_Fluid_Pelvis`, aim = Follower's (the Plan 06
pairing rule, anchor→anchor, resolved by parent armature in-scene).

## 2. Per-girl stack gates (runA artifacts; runB determinism in §3)

| # | F/L | Drift keyed max (mm) | Pen. post-cure (mm) | Jiggle F @45 (mm) | Jiggle L @38 (mm) | Fluid interior (gated) | Seam |
|---|---|---|---|---|---|---|---|
| 01 | Prima/Yui | 0.3933 (mean 0.0865) | **5.4582** | 15.203 (100/236) | 15.025 (97/224) | 0 | 0.000/0.000° |
| 02 | Yui/Prima | 0.3938 (0.0866) | 4.0978 | 15.025 (97/224) | 15.202 (100/236) | 0 | 0.000/0.000° |
| 03 | Alma/Prima | 0.4111 (0.0905) | 2.4001 | 13.701 (116/257) | 15.202 (100/236) | 0 | 0.000/0.000° |
| 04 | Sloane/Prima | 0.4024 (0.0885) | 2.3556 | 15.279 (103/236) | 15.202 (100/236) | 0 | 0.000/0.000° |
| 05 | Lux/Prima | 0.3995 (0.0879) | 2.8064 | 15.616 (102/236) | 15.202 (100/236) | 0 | 0.000/0.000° |
| 06 | Piper/Prima | 0.3983 (0.0876) | 1.4420 | 15.783 (104/236) | 15.202 (100/236) | 0 | 0.000/0.000° |
| 07 | Prima/Alma | 0.4116 (0.0906) | 3.2959 | 15.203 (100/236) | 13.701 (116/257) | 0 | 0.000/0.000° |

Reading of the table (all from `builds/<id>/runA/records/build_record.json`
unless noted):

- **Drift:** the Child Of empty holds 0.0001 mm max in every build;
  the shipped keyed form of the lock reads 0.3933–0.4116 mm max —
  the ingredient record's 0.393 mm class, worst on the two Alma
  pairings (+4.6%). Pure interpolation residual between solve keys,
  as in Plan 01.
- **Penetration:** the T-13 cure (scene-side `ContactFix` key on the
  follower's Body, value 1.0, never Basis) was applied per build
  (3–11 verts, max delta 2.734–8.000 mm). Every casting lands
  **at or under the 5.4582 mm record**; Prima-as-follower *is* the
  record (5.4582). Pre-cure maxima, for honesty: 01: 5.9728,
  02: 4.6989, 03: 2.4811, 04: 3.0605, **05 (Lux): 14.9120**,
  06: 1.7343, 07: 3.5995 — Lux's raw retargeted contact grazes
  deepest pre-cure and her cure hits the sculpt-class cap
  (8.000 mm); post-cure she reads 2.8064. The layered re-check
  (samples 38/45/61–67) never exceeds the loop value (worst
  layered: 5.4582 on 01; ≤3.2472 elsewhere) — the jiggle layer adds
  no penetration, per Plan 39.
- **Jiggle:** each girl's own-peak displacement matches **her own
  canon register from the conforming-fix gate**, not a single fleet
  number: Prima 15.203 (fix 15.2), Yui 15.025 (15.0), Alma 13.701
  (13.7 — her register is lower; band 257 verts), Sloane 15.279
  (15.3), Lux 15.616 (15.6), Piper 15.783 (15.8). Prima-as-leader
  reads 15.202 at *her* peak sample 38 (vs 15.203 at follower peak
  45 — a 0.001 mm sample difference, recorded as measured).
  Cross-phase values confirm the phasing (e.g. 01: follower 8.108 mm
  at the leader's peak, leader 10.117 mm at the follower's peak).
  All 12 Mesh Deform binds per build read `is_bound = true`.
- **Fluid interior (gated window):** **0 at frames 34/38/42/45/47/48
  in all 9 builds** (`fluidA/measurements.json`). Gate timing exact
  everywhere: first sourced frame 34, frozen from 48 (offset 0
  samples vs the beat-relative gate). Domain anchor margins
  0.3103–0.3219 m.

## 3. Determinism (per build, runA vs runB)

All 9 builds: scene-data fingerprint equal, clip sha256 sets equal,
decoded-pixel hashes equal at frames 0/38/45/60, identity hashes
equal. Control-casting fluid A/B: identical counts, verts, and
pixel hashes at all measured frames (RETARGET-PROOF §4). §7 verdict:
**PROVEN with two fluid late-window exceptions** (RETARGET-PROOF §6).

## 4. Fluid presence record (extrusion form, per build)

Emission totals (particles at f48, frozen thereafter) scale with the
pairing's anchor distance/geometry: 01: 467, 02: 486, 03: 555,
04: 480, 05: 489, 06: 497, 07: 519 (08/09: 555, as 03 — §5).
Mesh verts at f45: 214–248. Evidence: full frames +
`crop3x_*` crops at the contact interface in each
`builds/<id>/fluidA/renders/`. Agent read (benchmark S8): at the
peak frames the extrusion is occluded from NSCam and not
discernible at full frame (Plan 06 B5 FAIL-at-peak stands as the
form's read); at f90 a pale blue-grey patch reads at the interface
in the 3× crop (e.g. 03 crop3x_0090) — B5 PARTIAL-at-settle, as
recorded for the ingredient. **Late-window exception (02):** 35/486
particles inside Prima_Body at f90 (0 at all gated frames and at
f60/f78) — the only late interior event in the matrix.

**Peak-form stream layer (build 01 only, D-1159).** Over this
extrusion, the Prima/Yui pair shot carries the accepted stream
layer of record (§8, D-1159 disposition): a deterministic
authored curve-guided arc, generated per frame by
`runs/plan-06/stream-proof-20261110/scripts/ns06s_build.py`
under `runs/plan-06/stream-proof-20261110/stream_params.json`
(bulge 0.34 m toward normalize(+X+Z), FLOW_KEYS envelope of the
fluid gate above, head speed 2.0 m/s), sourcing f34, full at the
f45 peak, drained by f56. Gates of record for the layer:
interior 0 at all 37 measured frames (B4), timing exact (B2,
+10 retime first frame 44), vertex sha256 identical across two
generator runs at 37/37 frames. Evidence of record:
`runs/plan-06/stream-proof-20261110/REPORT.md`,
`runs/plan-06/stream-proof-20261110/verdict/VERDICT.md` (the
verdict pack), `measurements.json`, `frames/`, `masks/`,
`proof_stream_f45.blend` in the same tree. The layer applies to
build 01's pair shot only; builds 02–09 carry the extrusion
alone, and the accepted bake is unchanged (sha256
`cd361214…` — full hash in the proof report §3).

## 5. Bust-parameter spot proof — Alma (Amendment 2, stack level)

Builds 08 (m=0.50) / 09 (m=1.50) vs 03 (canon), Alma as Follower:

- **Anchors re-derived, not hand-moved** (in-scene §6.2 derivation at
  each m): Nipple.L rest position y = **−0.12610 (m 0.50) /
  −0.14555 (canon) / −0.16500 (m 1.50)** — Δ **∓19.45 mm** about
  canon, matching the fix step's recorded Alma track (±19.5 mm);
  z pinned at 1.33791 at all three settings; Pelvis anchor
  identical at all m (−0.10376, 0.93166 — m-invariant per the
  rule). In-stack rest anchors equal the fix step's verdict
  positions at the same m to the records' print precision (max err
  0.000 mm at 5-decimal coordinates, all 7 anchors, all builds).
- **Jiggle, as built:** the demonstrator scenes carry the fleet's
  canon cage binds, so their in-scene beat measures 13.701 mm at
  all three m (canon register). **§4.4-conformant re-fit**
  (`scripts/refit_beat.py`, the fix step's own bake-and-rebuild
  method, binds at rest, all binds true, 56 verts/cage): **m 0.50 →
  12.848 mm max / 5.297 mean, 116/257; m 1.50 → 16.053 / 5.405,
  117/257** — against the fix step's solo registers 12.85/5.3 and
  16.1/5.4. Two independent refits per setting produce identical
  displacement records and identical f0045 pixel hashes
  (`24534531…` at 0.50, `4075fc24…` at 1.50): **jiggle determinism
  is exact per setting, and the displacement follows m**.
- **Fluid attach follows the parameter:** the pelvis pairing is
  m-invariant by derivation, and the sim confirms it — particle
  counts and mesh verts are **identical at every measured frame**
  across 03/08/09 (555 at f48; 248 verts at f45), interior 0 gated.
  (The fluid *renders* differ across m in the chest region — the
  follower's bust in frame — while the pelvis-local sim does not;
  full-range Alembic hashes differ accordingly, late-window class
  per RETARGET-PROOF §6.2.) Nipple-anchor tracking (the lactation
  attach points) is proven by the anchor numbers above; no
  lactation emission is built in Stage 1.
- **Identity at extremes:** in-stack neutral renders at m 0.50/1.50
  are pixel-identical to pristine-rig renders at the same m
  (`edef050f…` / `e6ee3ed8…`).

## 6. Expected-vs-seen (benchmark: `BENCHMARK.md`, written before renders)

Agent reads against S1–S9, from `builds/<id>/runA/frames/` (full
frame + f_0045 contact sheet `frames/contact-sheet-f0045.png`) and
fluid renders/crops. **All eye verdicts queue for the Owner; no
Owner PASS is declared.**

| Item | Read (all castings unless noted) |
|---|---|
| S1 Contact held | **PASS** — no visible gap/breakthrough at the hip line at 0/38/45 in any casting; measurement carries the subsurface residual (§2) |
| S2 Phase lag | **PASS** — follower spine RX 10.0° at Contact → 14.0° at 45 in every build (build records `follower_spine_rx`); leader lowest at 38 |
| S3 Rotation not sliding | **PASS** — the lean-over pivot reads identically across girls (contact sheet); control reproduces Plan 01's measured swings by construction |
| S4 Jiggle phased | **PASS (measured)** — own-peak registers per girl (§2); visual amplitude at two-body framing remains the Owner's L-1 question, re-queued per girl below |
| S5 No visible penetration | **PASS at viewing size** — none visible in any evidence frame; Lux's pre-cure 14.912 mm is subsurface post-cure (2.8064) and reported in §2 |
| S6 Seam invisible | **PASS** — 0.000 mm / 0.000° over 108 bones per build; f0 = f78 by construction and by pixel hash on the control |
| S7 Faces / governance | **PASS (measured)** — troupe followers key no `Fac_Pupil_Heart` (3 face channels); trio followers key it (4). Face size at this framing is small — expression strength is an eye item |
| S8 Fluid presence | **FAIL at peak / PARTIAL at settle** — as the ingredient's B5 record; extrusion occluded at peak, pale patch readable in f90 3× crops. This is the form-of-record read, pending the Owner's jet-vs-extrusion decision (§8) |
| S9 Identity | **PASS (measured)** — §7.4 identity invariance exact per girl (RETARGET-PROOF §7); hair/iris identity reads distinctly in frames (Alma honey-blonde, Lux black/teal, Piper braid, Sloane ponytail) |

**Eye items queued per girl** (frames in each `builds/<id>/`):
- **All girls — D1-E1:** the loop as motion + the beat at two-body
  framing (Plan 01 E-1 + Plan 39 L-1, now per girl): does the
  §5.2 register read, or push amplitude for the demonstrator?
- **All girls — D1-E2:** follower expression at f_0045 (face small
  at this framing; Plan 01 E-2) — is a closer evidence camera
  wanted for Stage 2?
- **Prima (01) — D1-E3:** Plan 01 E-3/E-4 stand (toe-tip specks
  between the legs in some frames; the 5.4582 mm residual is
  subsurface at this camera, first re-cure candidate if the
  camera closes in).
- **Yui (02) — D1-E4:** the f90 fluid frame/crop — the late-window
  interior event is measured (35 particles), not visible as an
  artifact at viewing size; Owner to judge whether the settle
  endpoint matters for the demonstrator's shot length.
- **Alma (03/08/09) — D1-E5:** bust extremes legibility — the
  stack camera frames the bust small; the fix step's dedicated
  bust-camera stills (`runs/d1-conforming-fixes/evidence/alma/
  ext_m0.5|ext_m1.5/`) are the legibility evidence of record;
  the stack-level numbers are in §5.
- **Troupe (04/05/06) — D1-E6:** identity anchors are Owner-pending
  restyle candidates (§8.1) — conformance here is against the
  records as they stand; any restyle amends the record first.

## 7. Integrity & scope notes

- Ingredient artifacts and fleet files **hash-identical before and
  after** all work (layered scene `8c754671…`, Plan 01 scene
  `0bcd3bcd…`, Plan 06 Alembic `614a6f70…`, layered clips
  `5bff5c4a…`/`98805eee…`, six fleet blends — full sweep in the
  run's working notes; fleet staged to primo by hash and never
  written). Builds consumed primo staging copies
  (`~/.local/share/pax/nsd1/`, retained as the work record; Tier-1
  fluid caches live there, ~7 MB per build, not copied back).
- **HELD: none.** No casting failed a gate twice (none failed a
  gated gate once; the two §6 exceptions in RETARGET-PROOF are
  late-window fluid behaviour, recorded per girl).
- Proposed standard note filed in RETARGET-PROOF §8 (§7.4 fluid
  determinism scope). The standard itself was not edited; nor
  were EXECUTION-STATE.md or any fleet/ingredient file.

## 8. The two open Owner decisions (untouched by Stage 1, as tasked)

1. **Jet vs extrusion.** The fluid layer ships as the gated
   contact-interface extrusion in all 9 builds. Whether that read
   serves D-1, or a visible travelling stream is required (a
   different shot geometry or emission mechanism — Plan 06
   PASS4 §3.1), remains the Owner's call. Stage 1 neither
   re-litigated nor prejudged it.
2. **Lactation casting flag.** The ruling names **Maren** as the
   lactation canon lead; Maren has no rig in this fleet, and
   **Alma** is the fleet reference implementation (§6.3). Stage 1
   builds used Prima/Yui/Alma per the matrix above; the nipple
   anchors every girl carries were re-derived and tracked (§5),
   but **no lactation emission was built and the flag is
   untouched** — casting the lactation module's lead remains an
   Owner decision for a later stage.
   **RESOLVED (Owner ruling, 2026-11-09): the record is aligned
   to Alma, per D-1055.** Alma leads the lactation demonstrator
   in this lane; Maren's lactation canon stands separately in
   the Strobe lane and is untouched by this alignment. The flag
   is closed; no Maren rig is owed on this record's account.

### Section 8 disposition — superseded in part (2026-11-10, Owner ruling D-1154)

Item 1 is RE-RULED: a visible travelling stream for
the peak is required after all. (Its earlier
disposition, D-1114 — extrusion at peak, accepted
bake stands — is recorded in the runs/ copy of this
record.) The Owner commissioned a stream proof
(D-1154) on the mainA2 pair shot — different shot
geometry and/or a different emission mechanism, the
two routes §3 of the Plan 06 Pass 4 record names;
plain FLIP inflow in-pocket remains refuted (D-1069)
and is not retried. This supersedes D-1114's
extrusion-at-peak disposition. The accepted bake
stands unchanged until a stream proof passes the
Owner's eye; the proof tree is
`runs/plan-06/stream-proof-20261110/`. Item 2
(lactation casting) is unaffected.

### Section 8 disposition — accepted (2026-11-10, Owner ruling D-1159)

Item 1 is CLOSED by acceptance. The Owner reviewed the
D-1154 stream proof's verdict pack and rules (2026-11-10
02:46 PST): "the authored curve-guided arc over the
untouched extrusion is the peak form of record" for the
D-1 pair shot. The pending clause of the D-1154
disposition above ("stands unchanged until a stream
proof passes the Owner's eye") is discharged: the proof
passed. The stream layer of record is the one referenced
in §4: generator
`runs/plan-06/stream-proof-20261110/scripts/ns06s_build.py`,
parameters
`runs/plan-06/stream-proof-20261110/stream_params.json`,
report `runs/plan-06/stream-proof-20261110/REPORT.md`,
verdict pack
`runs/plan-06/stream-proof-20261110/verdict/VERDICT.md`.
The accepted bake is untouched and stands underneath
the layer (sha256 `cd361214…`, full hash in the proof
report §3); the extrusion remains the contact form at
the pocket and carries the settle.

Two qualifications ride with the acceptance, as measured
in the proof report §2 and the verdict pack's eye items:

1. **No full trace exists in this staging.** The peak
   corridor is 8.7 mm; no complete source-to-surface
   trace is achievable in this shot at any separation or
   by any mechanism (route (a) measured: +0.30 m
   re-separation caps at 0.59 visible fraction and
   destroys the contact). The accepted read is the
   strongest in-staging one: ~33 of ~69 projected px of
   arc directly visible at f45, ends anchored at the
   interface, passing behind the silhouette edges.
2. **The two eye items are admitted with the layer.**
   (a) The proof material — base (0.55, 0.68, 0.88),
   roughness 0.08, emission × 0.40 — is the stream
   layer's material of record for this shot; the shipped
   `NS06_FluidMat` is unchanged and still shades the
   extrusion. (b) The arc's form: a sideways escape
   toward normalize(+X+Z), the pocket's only open side,
   landing on Prima's exposed side at T, 0.204 m from
   the interior aim anchor (the aim-line entry T0 sits
   8.7 mm from the source, where the extrusion already
   is).

A camera/pose change for a longer, fully traced stream
is NOT commissioned; the D-1154 proof's §5 fleet
application is not commissioned either — this acceptance
covers the pair shot (build 01) only. Item 2 (lactation
casting) is unaffected.

## Addendum (2026-11-08, per D-1088 repair) — method defaults and POV direction notes landed

**Two-body method defaults (Night School Plan 20, measured on
this demonstrator's pair; gate PASS).** The two-body programme's
documented defaults, set by measurement on identical terms
(drift / interpenetration / seam / hand-dev): solved registration
(Child Of / solved keys) wherever registration is at stake;
contact lock → Plan 01; phase/reaction → hybrid (Plan 01 grammar
+ Bonnie counter-phase leader keying); hands → Plan 01 (Bonnie
finger-posing as pre-solve craft); penetration → hybrid (Bonnie
blocking-for-clearance + Plan 01 measure/cure); loop closure →
Plan 01. The lane-neutral comparison method and the 60 s
protocol's composition findings are homed in the
`local-animation-grammar-atlas` skill §10. The 60 s sustained-
scene test artefact (`plan-20/rebuild/run60/scene60.blend` on
primo) is the reference artefact for Torogao scene direction.

**POV direction notes (Night School Plan 15, complete-with-
FAIL-leg; the presence FAIL stands — blocking + materials, not
rig).** Central finding: POV is a blocking discipline before it
is a camera discipline. Rules: (1) block for the sightline —
keep the eye→subject line clear at every phase, or name the
occlusion as a deliberate beat; (2) verify in the shot camera
while posing, never only in the work camera. Default envelope
at this scene scale: bob 12 mm forward, 6 mm dip, 1.1° pitch at
peak; micro-roll 0.35° at 2 cycles/loop is optional seasoning,
not structure. Plan 15's eye items remain Owner-queued in its
own record.

## External references (2026-11-08, per D-1088 repair)

The demonstrator and SIX-GIRL-STANDARD are now referenced
from their named consumers (pointer-only; records stay here):
lumen README (primo `~/.GH/Qompass/lumen`, §"Night School D-1
reference"); torogao worktree `docs/night-school-references.md`
(cited from torogao's README); the TF Jam VALIDATION-PLAN.md
addendum of the same date. Primo-side pointers are working-
tree state, uncommitted — committing them is those repos' own
landing step.
