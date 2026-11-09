# Plan 04 — Application and Gate (Pass 4)

## Gate (plan's gate: camera-sweep evidence, both stages)

Expected-vs-seen benchmark was written in PASS3-REBUILD.md
before the final sweeps (six measurable criteria). Results:

| Criterion | Read |
|-----------|------|
| 1. No layer-separation artefacts (coverage + seams) | **PASS** — 0 transparent floor-band px in 18 frames; worst seam 5.3 / 25 grey levels |
| 2. Bounds hold | **PASS** — path inside wired bounds; coverage inequalities hold at both ends |
| 3. Floor contact stable | **PASS** — edge row constant ±0 across all frames, both runs |
| 4. Ambient motion reads at playing distance | **PASS (measured)** — 556–1,080 changed px, 0.18–0.35% of layer: present, sub-attention. Whether it *reads* as alive is an eye item (below) |
| 5. Cross-run agreement (MUGEN model vs estate depth model) | **PASS** — 0.0 px disagreement on all 5 measured layers |
| 6. Determinism | **PASS** — 9/9 frames pixel-identical across repeat runs, both models |

Sweep evidence: `stage/sweep-mugen/`, `stage/sweep-depth/`
(9 frames each + layer-only renders), `frames/verdict-sheet.jpg`
(labelled contact sheet: both models at c=0/240/480, Pass 4
before/after). Agent reads are labelled as agent reads wherever
they appear; no eye verdict is claimed by the agent.

## NSFW application — Torogao scene background re-layered

Target: **Prima's theatre scene plate**,
`~/workspace/torogao-plates-20261028/plates/pl04-scenes-prima-v2.png`
(1280×900, existing estate artifact, read-only). A flat plate —
exactly the "before" state the grammar operates on. Re-layered
on paper and in the compositor (`stage/pass4-relayer.py`,
renders in `stage/pass4/`), a wiring exercise, not new art:

| Before | After (grammar) |
|--------|-----------------|
| 1 flat plate, no motion model | **back curtain** (truss + rear curtain band), delta 0.5 |
| | **spotlight shimmer** — 8-frame anim from the plate's own bright beam pixels, Action-1 timing (10 ticks, 50-tick hold), delta 0.5 — the one ambient system, at the back (budget rule) |
| | **side curtains** (left/right wall strips), delta 0.75 — nearer than the back, slower than the floor |
| | **floor** (tile floor + rose band), delta **1.0** — floor-pinned (C2) |
| | **curtain ghost** — darkened side strips, **layerno 1, addalpha 100,120** (C6/C7), delta 1.0 |

Measured in the compositor (camera 0 → 120): back curtain
−60.0 px (expected −60.0 at delta 0.5), floor −120.0 px
(expected −120.0 at delta 1.0) — `stage/pass4/relayer-measurements.json`.
Adaptation recorded: this interior is one-point perspective,
so its "camera sweep" is a lateral drift, not a travelling
shot; bands were cut on the plate's own depth story (rear wall
/ side walls / floor), and coverage is by width, not tiling —
an interior has no tileable floor. The grammar's treatments
transferred unchanged; only the coverage strategy (L-E) is
place-dependent, exactly as TECHNIQUE.md §2 predicts.

## SFW translation

**The rebuild stage itself is the SFW exemplar — stated
explicitly:** Harbor Steps (PASS3-REBUILD.md) is authored
rating-neutral (a night waterfront: sky, stars, skyline,
promenade, beacon lamps; no characters, no adult content), and
it is the same grammar with the same calibration sheet a
jam-game stage would ship: plate-rule compositing for static
depth, floor-pinned delta for the playable plane, depth-ranked
deltas for authored layers, one back-layer ambient system on
the 120-tick loop, and an addalpha foreground ghost for
atmosphere. For a jam game the record translates term-by-term:
MUGEN `.def` → the jam engine's scene/layer list; `delta` →
parallax factor; `layerno` → fore/back draw groups around the
actor plane; Action ticks (60/s) → the jam engine's fixed-step
animation clock. Nothing in the grammar is MUGEN-specific
(TECHNIQUE.md §1 mapping verdict).

## Eye items queued for the Owner (no agent verdict claimed)

1. **Harbor Steps as a place** — `frames/verdict-sheet.jpg`
   tiles 1–4: does the rebuilt stage read as a waterfront at
   playing distance? (Agent note: beacon trio clusters into
   one lamp group — a placement defect recorded in
   PASS3-REBUILD.md.)
2. **Ambient read** — the stars' 120-tick twinkle: alive or
   invisible at sweep scale? Measured at 0.18–0.35% of layer
   pixels; the alive-vs-busy line is an eye call.
3. **Prima re-layer** — verdict sheet tiles 5–6 + `stage/pass4/`
   frames: does the re-layered theatre hold together under
   drift (band seams at the curtain/floor cut, ghost weight)?

## Lesson filed

`BLOCH-CANDIDATE.md` in this run dir (origin_lane=ntranch,
content_label=nsfw — the study source is an adult-lane MUGEN
build; the grammar itself is lane-neutral and its SFW
translation is named above, per the lane rule the crossing is
recorded, not assumed).
