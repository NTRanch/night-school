# Plan 20 — Pass 3 Clean-Room Rebuild Record

- **Date:** 2026-11-06 · **Route:** Blender 5.2.3 LTS headless on
  primo, scripted, deterministic. **Sources used:** the gated
  TECHNIQUE.md in this run dir + Plan 19's PASS3-REBUILD.md
  protocol + Plan 01's PASS3 record (measures of record). Video
  closed throughout the builds.
- **Casting:** Prima = Follower, Yui = Leader (Plan 01's
  casting). Rigs are the CONFORMED fleet blends staged to primo
  by hash (prima.blend md5 `2dc75c2f…`, yui.blend md5
  `45ecd804…` — identical to Plan 01's staging). Fleet files
  never modified; builds append/copy only.
- **Build host discipline:** primo, one heavy job at a time for
  this plan (tenants: the programme's whisper fleet, load
  28–49); file-mediated detached runs (`ns20-*`), completion
  read from `.done` files + build records. Nothing audible.

## (a) METHOD BUILD — the Bonnie method on the estate pair

**Build:** `rebuild/build_method.py` — Plan 01's build script
adapted with the method deltas marked `[P20]`: (1) blocking
changed to the series' ALL-FOURS arrangement (Prima low on
hands+knees on the platform, Yui kneeling behind — Plan 15
C-13); (2) the Child Of contact empty is NOT created — no
constraint, no per-keyframe registration solve; (3) Hips
locations are AUTHORED from the phase tables with the frame-0
Jacobian applied once, keyed DENSE at every sample 0–78 (the
SFM baked-field form); (4) hands are never solved — Prima's
hands are measured against frozen frame-0 floor-plant points,
Yui's against frame-0 offsets in Prima's UpLeg frames;
(5) the same measurement code as Plan 01 (drift, two-axis
penetration test, seam, hand dev) runs unchanged, and the
same T-13 cure procedure stands ready (not invoked — see
penetration). Phase tables, follower grammar and face
channels are Plan 01's, deliberately: the comparison isolates
the contact/blocking METHOD.

**Gate — both methods × Plan 01's measures, side by side**
(all numbers from `method/runA/build_record.json` /
`records/measurements.json` here and Plan 01's
`PASS3-REBUILD.md` §2 / `records/build_record.json`):

| Measure (identical terms) | Plan 01 method (solved) | Bonnie method (authored) |
|---|---|---|
| Contact drift, constraint form | **0.0001 mm max** | no constraint exists |
| Contact drift, shipped keyed form | **0.393 mm max** / 0.087 mean | **9.853 mm max / 3.969 mean** |
| Interpenetration, pre-cure max | 5.97 mm | **0.0 mm** (every sample) |
| Interpenetration, post-cure max | **5.46 mm** (mean-of-maxima 3.76) | **0.0 mm** — cure stood ready, nothing to cure |
| Seam (108 bones) | 0.000 mm / 0.000° | **0.000 mm / 0.000°** |
| Hand dev, follower max | 0.49 mm (frame-0 resid ≤0.46) | **49.04 mm** (floor plants, unsolved) |
| Hand dev, leader max | 4.94 mm (frame-0 resid ≤0.39) | **33.22 mm** (grip offsets, unsolved) |
| Follower grammar | hold→Contact, peak +7 (14.0° @45) | hold→Contact, peak +7 (26.0° @45) — grammar is method-independent |
| Oval (leader contact-point path) | PC2/PC1 0.232 | 0.089 (flatter authored path) |
| Determinism | clips bit-identical ×2; pixels identical | clips bit-identical ×2 (prima `3c2038d6…`, yui `8bb9044a…`); decoded-pixel hashes identical runA/runB: f_0000 `0011a4e6…`, f_0038 `2cb25c1f…`, f_0045 `5861ede6…`; seam f_0000 ≡ f_0078 |

**Reads.** The authored method's registration is 25× looser
than the solved keyed form and its unsolved hands leave their
plants by centimetres — while its BLOCKING carries a
clearance Plan 01's seated arrangement never achieves (0.0 mm
penetration with no cure). Both halves are the comparison's
point, and TECHNIQUE.md's verdicts are written from exactly
this table. Per-edit attribution for the build's iterations
is in BLOCH-CANDIDATE.md.

**Benchmark (expected-vs-seen, agent reads — Owner's eye is
the verdict of record):** frames `method/runA/f_*.png`.
1. All-fours blocking reads as the series' arrangement —
   **PASS (agent read)**: Prima on hands+knees, back low,
   Yui kneeling behind, hands at her hips (f_0000/f_0038).
2. Contact held at Contact (f_0038) — **PASS (agent read)**:
   pelvises meet with no visible gap or breakthrough; the
   measured drift (9.85 mm) is a registration looseness, not
   a visible separation at this framing.
3. Follower head — **FLAG**: Prima's head bows deep (hair
   covers her face at f_0038); the all-fours head pitch
   (−16° base + reaction) is the first tuning item if the
   Owner adopts this blocking for a scene. Eye item E-2.

## (b) 60-SECOND TEST — Plan 19's protocol, executed as written

**Construction (protocol §1, tiling form):** Plan 01's
78-sample pair tiled to 3,600 samples (46 cycles + 12-sample
head of cycle 47), built twice — in clip space
(`build_60s_clip.py`, D-1072 machinery consumed unmodified:
C2 spring, C3 draws, clip_lib) and in Blender
(`build_60s_blender.py`: the clips keyed onto a copy of Plan
01's scene, 194,454 + 187,252 keys inserted; checkpoint
measures + renders). Grammar mapping per protocol §2:
V-1/V-2/V-4 = C3 seed **2020** with the two-block schedule
(cycles 24–46: small parts ±2%, large families ±1%); reaction
= C2 τ=3; tempo = C1 (see deviation D-2); V-3 = the §3
checkpoint reads themselves; V-5 discharged in INTAKE; V-6
diagnostic-mode survey and V-7 still checkpoints are the
hand items — V-7's stills are the checkpoint renders filed
here; V-6 was executed as a workbench-class visual pass over
the middle checkpoint frame during the Blender build's
benchmark reads (agent-executed, recorded here, not a tool).

**Recorded deviations (not improvised — stated with
mechanism):**
- **D-1 (C2 composition):** the protocol maps reaction life
  to C2 τ=3 AND expects the peak at +7±1 after Contact. On
  this loop both cannot hold: Plan 01's follower ALREADY
  peaks at +7 by authored grammar, and the τ=3 spring adds
  its own +8-sample signature (measured in clip space before
  building: drive peak 45 → lagged 53). The build applies C2
  as written and reports both numbers per checkpoint.
- **D-2 (C1 form):** C1's period/dwell time-warp is not
  applied — protocol §3 fixes checkpoint sample ranges on
  the 78-grid, which a period warp destroys. C1's TRAVEL
  component is applied instead (R1_mid 30 mm → R2_slow
  45 mm, deviations about the bit-preserved contact pose),
  as the middle-boundary regime change. First build STEPPED
  the factor at the boundary; the gate measured a
  90.25 mm / 9.0° seam break; the shipped build RAMPS it
  across the boundary cycle (cure verified below).

**Checkpoint table** (cycles 1 / 23 / 46; starts 0 / 1716 /
3510; clip-space measures from
`records/measurements-60s-clip.json`, mesh measures from
`run60/records/build60-record.json` + the build log):

MUST DIFFER (life):
| # | Criterion | Cycle 1 | Cycle 23 | Cycle 46 | Verdict |
|---|---|---|---|---|---|
| 1 | C3 distance vs cycle 1 (max >0.1°, RMS >0.01°) | — (self) | **0.789° / 0.061°** | **0.416° / 0.030°** | **PASS** both |
| 2 | Spine RX peak after Contact = +7±1 | +16 (peak s54) | +14 (s52) | +15 (s53) | **FAIL as written** — D-1: the C2 signature (lagged − drive) is +8 at every checkpoint, τ-consistent; the absolute placement is +15±1 because the authored +7 and the spring's +8 compose. A no-C2 control tiling holds +7 exactly (Plan 01's record). The minute is neither unlagged nor double-counted by accident: it is the literal composition, measured |
| 3 | Contact-phase pixel hashes differ across cycles | `4745d2d2…` | `224d4116…` | `718711b5…` | **PASS** — all distinct (post-pass renders; pre-pass cycle-1 `66660628…` also distinct from its post-pass twin, see A-1) |

MUST NOT DRIFT (integrity):
| # | Criterion | Cycle 1 | Cycle 23 | Cycle 46 | Verdict |
|---|---|---|---|---|---|
| 4 | Contact-anchor drift ≤0.393 mm | **0.393** | **0.393** | 0.589 | PASS / PASS / **FAIL** — cycle 46's residual is the base 0.393 scaled by the tempo factor (0.393×1.5=0.589, exact): drift under this construction is travel-relative; the protocol's absolute bound does not survive its own tempo mapping. Reported, not normalised away |
| 5 | Interpenetration ≤5.46+0.5 mm and end−start ≤+0.5 | 0.0 | 0.0 | 7.31 | **FAIL** at cycle 46 on both readings — mechanism: tempo-scaled travel drives the pelvis pair into deeper grazing in the end regime (Contact-frame value is 0.0 at every checkpoint; the max lives mid-cycle); Plan 01's static ContactFix was tuned at base travel and this build does not re-cure (a re-cure at the end regime is the named fix; not executed — the item failed in both 60 s builds, stepped and ramped, and is recorded per the two-failure rule) |
| 6 | Seam 0.000 + C3 bounds clean, zero exempt diffs | bounds: **0 OOB / 50,403 checked; exempt diffs 0**; all-bones seam step 0.65 mm / 0.10° | 0.84 mm / 0.12° (post-cure; stepped build: 90.25 / 9.0°) | 0.62 mm / 0.13° | **MIXED** — the exempt-channel seam is exact (clip-space proof: pre-tempo periodicity violations 0, exempt diffs 0); the all-bones seam carries the per-cycle variation steps themselves (≤0.84 mm / 0.13°), which a literal 0.000 reading forbids and the C3 mapping requires. The tempo-step defect (90 mm class) is cured and verified gone |
| 7 | Hand residuals at Contact ≤0.46 (follower) / ≤0.39 (leader) | 0.40/0.42 · 3.05/3.06 | 0.34/0.35 · 3.94/3.95 | 0.41/0.42 · 1.87/1.87 | **Follower PASS ×3; Leader FAIL ×3** — mechanism: the leader's hand chains are C3-exempt, but her hands ride her C3-varied SPINE (eligible), so their world registration against the follower's thigh frame moves 1.9–4.0 mm. Exempting the chain does not exempt its carrier |

Determinism: clip-space build byte-identical ×2 in-process
(prima60 `ebe8abcd…`, yui60 `8f1ddd54…`); the two independent
Blender builds (stepped + ramped clips) produced IDENTICAL
decoded-pixel hashes at all three post-pass Contact frames —
the checkpoint poses at Contact are build-independent.

**Protocol verdict: FAIL (as written) — alive but not
intact under its own absolute bounds.** The minute DIFFERS
at every checkpoint (items 1, 3 PASS; the reaction is
present and τ-consistent) and its contact core does not
drift at base tempo (item 4 PASS ×2, item 7 follower PASS
×3, exempt seam exact). It fails where the protocol's
absolute numbers meet its own machinery: C2 composes onto
an already-lagged grammar (item 2), the tempo regime scales
the drift and outruns the static cure (items 4/5 at cycle
46), and carrier-channel variation moves exempt chains'
world registration (item 7 leader). Each failure is
mechanised above with the fix named; none is a tiling or
determinism failure. Plan 19's gate is therefore reported
as: **grammar machinery MAPPED and EXECUTED; aliveness
half PASS; integrity half FAIL at the end checkpoint** —
the honest composite, per part.

## (c) ADOPTED ITEMS A-1 / A-2 / A-3

- **A-1 Finishing-pass separation — EXECUTED as a named
  pipeline step.** In `build_60s_blender.py` the step
  boundary is logged in the build record (`steps`: "motion
  lock" → renders → "A-1 FINISHING PASS START" → changes →
  "A-1 FINISHING PASS END"). Pass content: Sun 3.0→3.6,
  Fill 1.1→0.7, rim sun added (2.4), camera lens 44→40 mm,
  world background darkened. Proof it moved no timing key:
  clip SHA-256 identical before/after (prima60 `ebe8abcd…`,
  yui60 `8f1ddd54…` both reads) and checkpoint Contact-frame
  drift re-measured post-pass at 0.0003 mm (unchanged
  class). Presentation effect is visible: pre-pass cycle-1
  Contact hash `66660628…` vs post-pass `4745d2d2…`.
- **A-3 Card hold — EXECUTED (mechanism).** The 60 s scene's
  render tail holds the take's true final frame (sample
  3599, post-pass presentation; decoded-pixel hash
  `f765ea54…`) under sequential cards (thanks → editor
  credit → studio card) built by `make_card.py` into
  `run60/cards/card1-3.png` over the Gaussian-blurred frozen
  frame — Plan 18's mechanism at Plan 19's noted scale (a
  single-card-class tail, ~7 s class, not Plan 18's
  15 s three-card timings; card count here is 3 stills for
  the publishing check, durations are an authoring choice
  at publish time). First card render's text was
  undersized; re-rendered at display size — card1 is
  legible at viewing size (agent read; Owner eye item E-4).
  The frozen frame IS the take's final frame by
  construction (the card script consumes
  `final_post_f3599.png` directly; its hash is the record).
- **A-2 Terminal take — DESIGN NOTE (not a second build).**
  Shape of record: one continuous **20.000 s** take, no
  internal cut, no loop seam (Plan 18 C-1; Plan 19's
  correction of the length to the record). Origin:
  performance-driven — the creator cut 60.000 → 20.000 s
  inside the sitting because the IK rig's evaluation lag
  made the long form unworkable, and narrated the decision
  ("I'll make this a 20 second animation", Plan 19 C-03):
  the terminal take's length is a TOOL-LIMIT artefact
  promoted to a form, and its estate translation is: a
  terminal scene is authored at the longest length the
  estate's evaluation path holds interactively, as ONE
  clip, and is never assembled from loop tiles. This plan's
  gate is the loop test (per brief); the terminal form is
  filed here as the series rebuild's ending design, to be
  built when the Torogao apex scene is authored.
