# Plan 11 — Pass 3 Clean-Room Rebuild

Rebuilt from `TECHNIQUE.md` alone (video closed). Estate
toolchain: Blender 5.2.3 (Arch build `/usr/bin/blender`,
Python 3.14.8; source video: Blender 5.0.1 — version drift
is a measured part of this rebuild, see "Version drift"),
primo headless, canonical argv (`-b -Y --factory-startup
--offline-mode -noaudio --python-exit-code 1`), file-mediated
detached runs (`ns11-*`). Primo ran a parallel wave
throughout (up to four other lanes' whisper jobs + tenants;
load 19–28 on 16 threads): every heavy stage of this run
was niced and its wall time is contention-inflated —
recorded, not hidden.

## Deliverable mechanism

- Variant script: `rebuild/build_aov_variant.py` — extends
  a **copy** of the Plan 02 template. Plan 02's files were
  only ever read: the template copies in this run's
  `rebuild/` were produced by running Plan 02's own
  `build_template.py` (read-only) with `--outdir` pointed
  at this run; the NSFW copy's scene fingerprint is
  **ca585ca41656ea6e3a80c504143eb1d504ee717cecb8034b4d9b199bcbb5570a**,
  identical to Plan 02's recorded value — the copy is the
  same scene, byte-for-byte in scene-data terms.
- Variant outputs per lane: `template-<variant>-aov.blend`,
  `fingerprint-aov-<variant>.json`,
  `parameters-aov-<variant>.json`. Fingerprints: NSFW
  **f3fa4926d3d3071221c34b77c906adde66bc9bd3ca1c80dfa6e6f43ab168a2cd**;
  SFW **ca43b4b80fe079567b33e30b0d1084bb926a06e47370ca38c9fba0585476fad9**.
- Variant parameters AS BUILT:
  - Light groups (one per lamp, sheet rule): **Key**
    (Key_Area), **Rim** (Rim_Spot), **Fill** (Fill_Area),
    **Accent_1…4** (Accent_Point_1…4), **Backdrop**
    (Backdrop emissive cyclorama — the Adapt term: his
    backdrop is ungrouped and rides Emission; the estate
    groups it so the ground is itself relightable).
    Script asserts every LIGHT object carries a group.
  - Render Layers outputs on the built tree (printed by
    the build): Image, Alpha, Emission, Noisy Image,
    Combined_Key, Combined_Rim, Combined_Fill,
    Combined_Accent_1…4, Combined_Backdrop.
  - Compositor tree (in order, recorded in the fingerprint):
    RenderLayers → per group [RGB gain/tint node →
    Mix MULTIPLY] → Mix ADD chain → Denoise (terminal) →
    Group Output + Viewer + File Output (PNG comp-beauty);
    plus a second File Output writing the **passes EXR**
    (items: Combined, Emission, Combined_<each group>).
  - Pass contract: multilayer OpenEXR via the compositor
    File Output node, **32-bit full float, ZIP**; renderer
    denoise **OFF** (sheet C-11-4 — denoise is the tree's
    terminal node); Cycles preset inherited from Plan 02
    (adaptive 0.0100 / max 4096, seed 0, CPU, 1080×1920).
- Relight lane: `rebuild/relight.py` (primo system python3,
  OpenEXR 3.5.3 + numpy 2.5.4) — pass algebra on the EXR,
  no renderer involved; `rebuild/exr_to_png.py` converts
  relight EXRs to PNGs through Blender's own colour
  management (AgX + the template's −1.8 exposure).

## Version drift (5.0.1 video → 5.2.3 estate), probed not assumed

Each item cost a census probe on primo (`/tmp/ns11-census*.py`,
findings applied in place):

1. `scene.node_tree` no longer exists; the compositor is
   `scene.compositing_node_group`.
2. Node types renamed: Composite → **NodeGroupOutput**;
   MixRGB → **ShaderNodeMixRGB** (Factor/Color1/Color2);
   a hand-made group needs an **interface output socket**
   or the render is black.
3. The render-format enum lost `OPEN_EXR_MULTILAYER`;
   multilayer EXR output lives on the **compositor File
   Output node** (`file_output_items.new('RGBA', name)`
   creates each pass's input; the written file is a
   **multi-part EXR**, one part per pass).
4. The ViewLayer exposes **no denoising-data passes** on
   5.2.3 (no `use_pass_denoising_data`; RL node never
   lists Denoising Albedo/Normal, with or without a
   Denoise node, with or without renderer denoise). His
   5.0.1 guide wiring (C-11-4's Albedo/Normal feeds) has
   no direct 5.2.3 equivalent at build time; the variant's
   Denoise node runs on the sum unguided. Recorded as
   drift, not silently absorbed.

## Probe validation (540×960, 128 samples — the lane proven before the full render)

- Probe EXR (`rebuild/passes-probe-nswfw.exr`, 51,778,653 B):
  **10 parts** — Combined, Emission, Combined_Key,
  Combined_Rim, Combined_Fill, Combined_Accent_1…4,
  Combined_Backdrop. SFW probe identical in structure.
- **Beauty-match (C-11-2 identity), probe NSFW:**
  Σ (8 group passes) vs the EXR's Combined layer, linear
  space: mean |diff| **1.47e-07**, RMSE 2.56e-07, max
  |diff| 4.29e-06, **0.0% of pixels above 1e-3**. The
  unmodified comp reproduces the renderer's beauty from
  the passes alone — float-assembly noise only.
  SFW probe: mean |diff| **1.20e-07**, max 3.81e-06, 0.0%
  above 1e-3.
- **The remainder rule, measured:** adding the Emission
  layer on top of the group sum *overshoots* (mean |diff|
  0.0460; result mean 0.7502 vs Combined 0.7042) — because
  this variant groups its emissive backdrop, that energy
  is already inside Combined_Backdrop. His scene needs
  Emission added precisely because his backdrop is
  ungrouped. The contract's rule is therefore: **Emission /
  Volume terms enter the sum exactly for the emissive /
  volumetric sources that belong to no group** — grouping
  an emissive moves its energy from the remainder into
  its group pass. (Relight lane implements this: base =
  group sum; Emission carried as a diagnostic layer.)
- **Per-group base shares (probe NSFW, mean-luminance
  share of the group-sum base):** Key **0.7558**, Fill
  0.1611, Backdrop 0.0554, Accents total 0.0277
  (Accent_1 0.0051 / _2 0.0056 / _3 0.0139 / _4 0.0031),
  **Rim 0.0000**. SFW probe: Key 0.7623, Fill 0.1424,
  Backdrop 0.0664, Accents 0.0290, Rim 0.0000.

## The dead rim (the rebuild's headline measurement)

`Combined_Rim` is **identically zero**: mean 0, max 0,
**0 nonzero pixels** of 518,400 — in both variants, at
probe sampling. The Plan 02 template's Rim_Spot
(1000 W Spot, 55°, at (1.6, 1.5, 2.1), aimed at the
figure) sits **behind the backdrop cyclorama wall**
(the wall stands at y = +1.3, spanning z 0–5); the
backdrop mesh occludes the spot completely, so the lamp
has never contributed a single pixel to any Plan 02
render. The summed beauty hides this entirely — Plan
02's Pass 4 credited a "rim-side edge light" that was in
fact the backdrop's own emission gradient (Backdrop
group share 5.5%, reading as edge separation because the
rim colour was sampled from the backdrop hue). **Only
the per-group split can see a dead lamp.** Consequences
carried into this run's gate: the planned rim-dominant
relight is impossible from this render's passes (a gain
on zero is zero — measured, PASS3 claim table), and the
third relight is driven by the Backdrop + Accents passes
instead. A bloch candidate for the Plan 02 lane is filed
in this run's BLOCH-CANDIDATE.md; fixing the template
itself is Plan 02's call, not this run's (the variant
extends a copy, it does not repair the original).

## Full render (the one input render) — close-out record

- Detach `ns11-render`, rc 0. Launched 19:15 PST,
  outputs written 19:34 PST (~19 min wall at nice 10,
  −t 6, under parallel-wave load 20–35; the process
  accumulated ~65–80 CPU-minutes — Plan 02's unloaded
  comparable was 07:12.710 wall at −t 8. Contention is
  the difference; the render is otherwise the template's
  own final settings: 1080×1920, adaptive 0.0100 / max
  4096, seed 0.)
- `rebuild/passes-nswfw.exr` — **204,337,142 B,
  SHA-256 304ee9696a1323383a68fca0dc0af1afd6f24fbdfd20ef49eec528c6d22dbc5a**;
  **10 parts** (verified by re-opening): Combined,
  Emission, Combined_Key, Combined_Rim, Combined_Fill,
  Combined_Accent_1…4, Combined_Backdrop — each
  1080×1920, ZIP. `rebuild/comp-render-nswfw.png` —
  4,270,160 B, SHA-256 1bc6da3c03bdc703397ed0e9d600a654c8366f4240a041cd6d1987a6bb99cd39
  (the tree's denoised comp of the same render).
- **Beauty-match at full sampling:**
  Σ (8 group passes) vs Combined — mean |diff|
  **2.59e-07**, RMSE 5.08e-07, max |diff| 3.77e-05,
  **0.0% of pixels above 1e-3**. The identity holds at
  production settings (probe: 1.47e-07).
- **Per-group base shares (full):** Key **0.7558**,
  Fill 0.1612, Backdrop 0.0554, Accents total 0.0277
  (0.0051 / 0.0056 / 0.0139 / 0.0031), **Rim 0.0000 —
  identically zero at full sampling too** (0 nonzero
  pixels of 2,073,600; the dead-rim finding is not a
  probe-sampling artefact). Probe↔full shares agree to
  ≤0.001 on every group.
- **Production relights** (`rebuild/relight-measurements.json`,
  PNGs `relight-{key-warm,low-key,neon-backdrop}.png`
  beside `relight-basecomp.png`):

| Relight | Lum. ratio vs base | RMS vs base | Share movement |
|---|---|---|---|
| key-warm | 1.3712 | 0.4583 | Key 0.756 → 0.843 |
| low-key | 0.6932 | 0.3320 | Fill 0.161 → 0.028; Accents 0.028 → 0.072 |
| neon-backdrop | 0.6685 | 0.3979 | Backdrop 0.055 → 0.167 |

  Probe rehearsal predicted every figure to the third
  decimal (1.371 / 0.693 / 0.668; shares identical) —
  the probe-then-production ordering validated itself.

## Claims scored as tests

| Claim | Score | Evidence |
|---|---|---|
| C-11-1 one group per lamp, role-named | REPRODUCED | Variant build: 8 groups, RL outputs Combined_<group> ×8, script-asserted assignment for every lamp |
| C-11-2 beauty = Σ groups + ungrouped remainder | REPRODUCED, with the grouping rule measured | Probe: Σ groups == Combined at 1.47e-07 with the backdrop grouped (remainder = 0 by construction); his ungrouped form needs Emission + Volume added — the rule "remainder = energy in no group" covers both |
| C-11-3 per-group gain/tint in comp, no re-render | REPRODUCED | Three relights from the probe EXR by pass algebra alone (below); gains to 2.0× and a hue-class tint (key-warm) applied without any renderer run |
| C-11-4 denoise after the sum, in comp | ADAPTED-REPRODUCED | Tree carries the terminal Denoise on the summed passes; the guided (Albedo/Normal) form is 5.0.1-only — 5.2.3 exposes no denoising-data passes (drift item 4) |
| C-11-5 lamp geometry still forces a re-render | CONFIRMED BY CONSTRUCTION + a measured corollary | No pass algebra can move a shadow; corollary: no pass algebra can resurrect a lamp whose pass is zero (the dead rim) — the boundary is not just geometric, it is *energetic*: a group with no energy is not relightable |
| C-11-6 "change lighting without re-render" (scoped) | REPRODUCED as scoped | Intensity/colour/treatment of every *live* group changed post-render; the unscoped claim fails on the dead rim and on all geometry |

## Probe relights (validation of the three recipes; production relights come from the full EXR)

Recipes (linear gains × tints per group; Rim carried at
1.00 — it is zero) and measured outcomes vs the probe base
comp (mean-luminance shares; RMS in linear space):

| Relight | Recipe (essence) | Lum. ratio vs base | RMS vs base | Share movement (headline) |
|---|---|---|---|---|
| key-warm | Key ×1.45 tinted (1.25, 1.02, 0.72); Rim ×0.70; Backdrop ×0.75 | 1.371 | 0.4576 | Key share 0.756 → 0.843 |
| low-key | Fill ×0.12; Key ×0.80; Backdrop ×0.35; Accents ×1.80 | 0.693 | 0.3318 | Fill share 0.161 → 0.028; Accents 0.028 → 0.072 |
| neon-backdrop | Backdrop ×2.00 tinted (1.05, 0.95, 1.10); Key ×0.55; Accents ×1.60 | 0.668 | 0.3971 | Backdrop share 0.055 → 0.167 |

All three are pairwise distinct by construction and by
measurement (each moves a different group's share by
≥ 0.08 while moving total luminance in a different
direction or by a different amount). Agent visual read of
the probe sheet (`relight-probe-*.png`): key-warm reads
brighter and pinker; low-key darker with the accent glow
relatively stronger; neon-backdrop's ground goes saturated
magenta with the figure relatively cooler — credible
relights of the same shot, pending the Owner's eye at
full resolution.
