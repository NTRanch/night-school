# Plan 04 — Clean-Room Rebuild (Pass 3)

Built FROM TECHNIQUE.md ALONE (the video was not reopened).
Estate-authored stage **"Harbor Steps"** — a rating-neutral
night waterfront (sky, stars, skyline, promenade plate, beacon
statue), all layers procedurally drawn by script
(`stage/make_layers.py`, seeded). No source art.

## Stage record (MUGEN .def terms — this is the spec)

`stage/harbor-steps.def` — viewport/localcoord 640×480,
zoffset 390 (floor contact line), [Bound] screenleft 30,
screenright 30 (his one read bound value, mirrored),
boundleft −480 / boundright +480 (camera travel budget).
Layers in declaration order (= draw order, claim C1):

| # | Element | Type | Delta | Tile | Scale | Layerno | Blend |
|---|---------|------|-------|------|-------|---------|-------|
| 1 | sky | normal | 0.25, 0.25 | 0,0 | 1,1 | 0 | — |
| 2 | stars | anim (Action 1) | 0.25, 0.25 | 0,0 | 1,1 | 0 | — |
| 3 | skyline | normal | 0.5, 0.5 | 0,0 | 1,1 | 0 | — |
| 4 | plate (water+railing+floor) | normal | **1, 1** | **1,0** | 1,1 | 0 | — |
| 5 | beacon | normal | 1, 1 | 0,0 | 1.5 | 0 | — |
| 6 | beacon solid | normal | 1, 1 | 0,0 | 2.0 | 0 | — |
| 7 | beacon trans | normal | 1, 1 | 0,0 | 2.5 | **1** | addalpha 100,120 |

Action 1 (stars): 8 frames, 10 ticks each except frame 7 at
50 ticks — his timing copied as a *rule* (120-tick loop).
The floor is delta-pinned (C2); depth ranks descend 0.25 →
0.5 → 1 (C3) — the differentiation his build states but bakes
away (DG1) is exercised here, because the estate grammar
adopts the doctrine where layers are authored separately.
The beacon trio mirrors his Cookwitch trio (C6/C7): same
element at two scales behind the actor plane, one enlarged
addalpha copy in front at alpha 100,120.

## Two runs of the same record

- **Run A — MUGEN-model compositor** (`stage/compositor.py
  --model mugen`): screen_x = start − c·delta per axis;
  declaration-order drawing; layerno=1 after the actor plane;
  tile wraps by sprite width. Direct implementation of the
  TECHNIQUE.md §2 model.
- **Run B — estate depth-plane renderer** (`stage/compositor.py
  --model depth`): each layer is a fronto-parallel textured
  plane at depth z in a pinhole scene, focal f = 640, with
  **z = f·(1/delta − 1)** (sky z=1920, stars z=1920, skyline
  z=640, plate/beacon z=0). Rendering is an independent
  per-pixel ray→plane projection (numpy), not a paste: a world
  feature at depth z projects with apparent scale f/(f+z) and
  shifts c·f/(f+z) under camera translation c. If the estate
  depth convention and the MUGEN delta convention describe the
  same motion, per-layer displacements agree to rounding.

Camera path (both runs): c = 0, 60, …, 480 (9 frames), at
anim tick 0 unless stated. Layer-only renders at c=0 and c=480
carry one unique bright marker per layer; displacement is the
marker centroid shift.

## Gate criteria — WRITTEN BEFORE THE FINAL SWEEPS

1. **No layer-separation artefacts.** (a) In every composite
   sweep frame, the floor band (rows 390–479) has 100% opaque
   coverage — no clear-colour pixel. (b) Tile-seam test: at
   every plate seam column inside the viewport, the floor-band
   column mean differs from its neighbour columns' mean by
   < 25 grey levels (no visible seam line).
2. **Bounds hold.** The camera path stays inside the wired
   bounds (0 ≤ c ≤ 480 ≤ boundright budget) and every layer's
   coverage inequality holds at both path ends:
   layer_width ≥ 640 + delta·480 (sky 800 ≥ 760, stars 800 ≥
   760, skyline 1200 ≥ 880, plate tiled = unbounded).
3. **Floor contact stable.** The plate's floor-top edge row is
   identical (±0 rows) in all 9 sweep frames of both runs.
4. **Ambient motion reads at playing distance.** Star-layer
   frame difference (tick 0 vs the 50-tick hold frame) at
   sweep scale: ≥ 200 changed pixels (measurable) and
   ≤ 5% of layer pixels (his alive-not-busy budget).
5. **Cross-run agreement.** Per-layer marker displacement in
   Run B within ±2 px of Run A for every layer.
6. **Determinism.** Two independent executions of each run
   produce pixel-identical sweep frames (SHA-256 of decoded
   RGB equal for all 9 frames × 2 runs).

## Results (artifacts: `stage/sweep-mugen/`, `stage/sweep-depth/`, `stage/gate-results.json`, per-run `measurements.json`)

Per-layer marker displacement, camera 0 → 480 (px, screen):

| Layer | Delta | Expected | Run A (MUGEN) | Run B (depth) | Δ A−B |
|-------|-------|----------|---------------|---------------|-------|
| sky | 0.25 | −120 | −120.0 | −120.0 | 0.0 |
| stars | 0.25 | −120 | −120.0 | −120.0 | 0.0 |
| skyline | 0.5 | −240 | −240.0 | −240.0 | 0.0 |
| plate | 1.0 | −480 | +220.0 ≡ −480 (mod 700 tile) | +220.0 ≡ −480 | 0.0 |
| beacon solid | 1.0 | −480 | −480.0 | −480.0 | 0.0 |

Claims verified by construction/measurement: **C1** (declaration
order = draw order in both renderers), **C2** (floor pinned at
delta 1; plate displacement exactly camera displacement),
**C3** (displacement strictly monotonic in delta rank),
**C6** (beacon trans drawn after the actor plane; its addalpha
halo is visible over the plate in sweep frames), **C7** (ghost
uses alpha 100,120 verbatim), **C9** (plate tiles seamlessly —
gate 1b), **C4** (negative control: with sky+stars omitted the
top region renders 99.999% black, reproducing his test-#1
failure on demand).

Gate reads (criteria written above, before the sweeps):
1. **Layer separation — PASS.** Floor-band transparent pixels:
   0 in all 9 frames × 2 runs. Worst tile-seam column difference:
   5.0 (MUGEN) / 5.3 (depth) grey levels vs the < 25 bound.
2. **Bounds — PASS.** Path 0–480 inside the wired ±480 budget;
   coverage inequalities hold (sky/stars 800 ≥ 760, skyline
   1200 ≥ 880, plate tiled).
3. **Floor contact — PASS.** Edge-proxy row identical (380) in
   all 9 frames of both runs, ±0; the contact line itself is
   the zoffset row 390 by construction.
4. **Ambient — PASS.** Stars tick 0 → hold frame: 556 changed
   px (0.18% of layer) MUGEN run; 1,080 px (0.35%) depth run
   (world-scale resampling spreads texels — noted, both inside
   the ≥200 px and ≤5% band: measurable, sub-attention).
5. **Cross-run agreement — PASS.** 0.0 px on every measured
   layer (bound was ±2). Composite agreement at c=240: mean
   absolute pixel difference 0.37 grey levels between the two
   renderers — the estate depth convention **z = f·(1/delta−1)**
   reproduces MUGEN delta motion.
6. **Determinism — PASS.** Repeat executions reproduce all 9
   sweep frames pixel-identically in both models (SHA-256 of
   decoded RGB equal, 9/9 each; hashes in `measurements.json`).

Agent visual read (NOT the gate — the eye verdict is the Owner's,
queued in PASS4-APPLICATION.md): the stage reads as a night
waterfront; the beacon trio clusters into one lamp group at
most camera positions (starts 430/455/470 at scales up to
2.5× overlap heavily) where his build keeps its foreground
figure clear of the fight zone. Recorded as a rebuild defect
of placement, not of grammar: the trio mechanism (C6/C7)
measures correctly, its composition does not. The art is a
grammar vehicle per the brief, so this is logged, not iterated.
