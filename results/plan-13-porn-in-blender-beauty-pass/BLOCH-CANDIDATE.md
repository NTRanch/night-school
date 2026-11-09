# Bloch candidate — from Night School Plan 13 (beauty-pass recreation)

origin_lane: ntranch
content_label: nsfw

(Propose-only candidate, filed per the standing clause.
The technique content is lane-neutral compositing; the
label follows the plan's lane of record, per the birth-
metadata rule — reclassification is a gated act, not the
filer's.)

## Lesson candidates

1. **A match claim needs a measurement gate, and the
   honest answer has three tiers, not two.** The source
   video asserts its recreation "matches" by toggling a
   Switch node — and its own first toggle visibly failed
   (a missing branch). Measured in the estate rebuild, the
   recreation is (a) exact at float32 precision for the
   raw sum (mean |Δ| 1.78×10⁻⁷), (b) *not* bit-for-bit
   (summation order; decoded hashes differ), and (c) an
   approximation at the denoised endpoint, because two
   different denoise implementations are being compared
   (mean |Δ| 1.77×10⁻³, 23.2% of pixels beyond 1/255).
   Any future "recreate X and compare" gate should state
   in advance which tier it is claiming.
   Evidence: `runs/plan-13/PASS3-REBUILD.md` (measurement
   tables), `runs/plan-13/rebuild/runA/measurements.json`,
   `runC/measurements.json` (primo canonical copies under
   `~/.local/share/pax/night-school/plan-13/rebuild/`).

2. **The match/modify boundary is a place in the graph,
   and the artist named it**: everything before the
   Denoise node is the reconstruction; everything after it
   is optional grading (his words, and his own practice —
   AO multiply and a deliberate *second* volume addition
   "because it looks better" both live after it). When a
   studied workflow mixes reconstruction and grading,
   locate the boundary node first; grade steps found
   inside the "matching" region are findings, not details.
   Evidence: `runs/plan-13/OBSERVATION.md` rows 22:41,
   25:39, 26:32.

3. **A silent fallback in a measurement tool manufactures
   perfect results.** The first `measure.py` passed an
   invalid enum (`OpenEXR.FLOAT`) into a try/except that
   substituted an array of ones — every file then "hashed
   identical," a fake determinism PASS. It was caught only
   because identical hashes across *different* images are
   themselves implausible. Rule reinforced: measurement
   code fails loudly or not at all; a too-perfect result
   is a defect signal.
   Evidence: `runs/plan-13/PASS3-REBUILD.md` (tool defect
   section), `runs/plan-13/rebuild/measure.py` (fixed
   reader).

## Friction log (D-1064 clause — including silent workarounds in successful runs)

- **F-1 (silent workaround, caught):** the `measure.py`
  ones-array fallback above. Cost: one full measurement
  pass discarded and re-run. The next agent hits this
  anywhere a reader wraps parsing in a bare except.
- **F-2 (Blender 5.2 compositor API drift):** four build
  iterations were spent on 5.2 API changes vs the
  documented/older surface — compositor tree as node
  group, `ShaderNodeMix` socket indices, File Output
  `media_type` defaulting to multilayer, the main render's
  `media_type='MULTI_LAYER_IMAGE'`, pass sockets requiring
  `update_render_passes()` *after* the engine is set, and
  the Noisy Image socket existing only when render
  denoising is on. Each was resolved by a small probe
  script before touching the build (`/tmp/probe2..14.py`,
  referenced in `build_recreate.py` comments). The next
  agent scripting the 5.2 compositor will hit all of
  these; the probes are the shortcut.
- **F-3 (capture egress flakiness):** the source host
  returns an intermittent database-error 503 (roughly one
  request in three) and a hard 403 from the sandbox egress;
  primo + retry landed the page, and the media required
  ranged parallel segments (single stream ≈0.89 MB/s).
  Recorded in INTAKE/MANIFEST; no new workaround invented.
- **F-4 (wave contention):** the single-chunk transcription
  shared primo with up to six other whisper jobs (load
  peaked at 27/16 threads); wall time stretched to hours
  at ~0.35× realtime in the worst stretch. No action
  taken beyond patience — flagging because "one heavy job
  at a time programme-wide" was not the observed reality,
  and plan ETAs should assume contention.
- **F-5 (frame-reading limit):** at 720p, three
  wire-attribution questions in the compositor tree could
  not be settled from frames (U-3); all three were settled
  by narration instead. Not a workaround — a reminder that
  for node-graph videos, the transcript is a *co-governing*
  surface for wire-level facts, and harvesting it late
  (transcription is the slowest stage) delays exactly the
  claims that need it.

## Per-edit attribution rows (Pass 3 build)

| component / change | observed difference | verdict |
|---|---|---|
| `measure.py` reader: header-declared channel type, loud failure (was: `OpenEXR.FLOAT` + silent ones fallback) | identical-hash artefacts disappeared; recreated/beauty hashes separated (84c73632… vs 0976a3fa…); stats became non-trivial | fix confirmed |
| build: `media_type` set on render + File Output nodes | multilayer/main outputs wrote at all (was: rejected enum / wrong media type) | fix confirmed |
| build: `update_render_passes()` after engine set | pass sockets (Volume, Denoising, Noisy) materialized on the Render Layers node | fix confirmed |
| build: Noisy Image link guarded by socket presence | run A (denoise off) builds; run C (denoise on) exposes and writes the socket | fix confirmed |
| recipe: volume summed pre-denoise (Rest branch) | raw match at float precision on both scenes; denoised endpoint gap attributable to denoise implementation alone | adopted (matched form) |
| variant: Gloss ×1.6 + Emission ×2.0 in-sum | branch arithmetic verified ×1.6000 (runD); variant stats measured on both scenes | adopted |
| template application: gated settings reduced in the COPY only (64 samples, 25% res) | template match statistics at float precision; input blend hash unchanged | confounded — reduced settings change the noise field, so the template match numbers describe the gated render, not a full-quality render (the recipe claim is settings-independent; the numbers are not) |
