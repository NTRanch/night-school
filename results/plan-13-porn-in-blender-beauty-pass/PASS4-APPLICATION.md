# Plan 13 — Pass 4 Application and Gate

Application named in the plan: **keeper-still finishing —
grade variants per render for verdict packs.** SFW
translation: shared with the SFW render lane unchanged
(the recipe, the pass contract, and the measurement gate
are content-neutral; nothing in them references the
subject).

## Expected-vs-seen benchmark (written before the application run)

The recreation, applied to one real estate render (a copy
of the Plan 02 template's nswfw still, re-rendered at
64 samples / 25% resolution for the gated run), SHOULD:

1. match the renderer beauty from the same render at
   float precision (the Pass 3 gate, repeated on estate
   geometry — specifically on a scene whose skin material
   carries **Subsurface Weight 0.20 with no Subsurface
   passes enabled**, the recipe's open SSS question);
2. produce the graded variant (Gloss ×1.6, Emission ×2.0)
   from the same render's passes with no re-render;
3. leave the input template byte-identical.

## Seen (agent reads; measurements from `template/out/measurements.json`)

1. **MATCH on estate geometry: PASS.** Recreated vs
   renderer beauty (270×480): mean |Δ| **1.69×10⁻⁷**, max
   |Δ| **3.34×10⁻⁶**, RMS 2.69×10⁻⁷, **0.00% of pixels
   beyond 1×10⁻⁴**. The SSS question is answered by
   measurement: with Subsurface passes disabled, the SSS
   contribution lands inside the enabled passes (diffuse),
   and the recipe still closes. A scene that needed SSS
   *separately graded* would need the SSS passes enabled
   and a fifth branch — the recipe's extension rule, not a
   defect of the match.
2. **MODIFY: PASS.** Variant vs recreated_denoised on the
   template render: mean |Δ| **0.149**, max |Δ| **0.710**,
   ~100% of pixels beyond 1/255 — a strong, legible grade
   at beauty scale (agent read of `variant_png.png` vs
   `recreated_denoised_png.png`: the emissive backdrop
   gradient lifts visibly, speculars brighten; the figure
   read is otherwise unchanged). Produced from the passes
   of the same render; no re-render occurred.
3. **Non-interference: PASS.** Input copy SHA-256
   6ce16d71bc028946bbe090132ccd580fd4336e9cef2c34bc6af46ed2474d4bf3
   before and after; the primo original was never opened
   for writing.

The application render itself: 39.6 s (Cycles CPU, 2
threads, 64 samples, 270×480) — against the source video's
8:23 full render, the point of the technique: after one
render, variants are compositor-cheap.

## Gate read (plan gate)

PASS = match-then-modify both demonstrated with
measurements; a recreation that cannot match is recorded
as an approximation, not adopted silently.

- **MATCH: PASS** — raw recreation = renderer beauty at
  float32 precision on both scenes (synthetic + estate
  template), statistics in PASS3-REBUILD.md. Not
  bit-for-bit (decoded hashes differ); the distance from
  bit-equality is measured and attributed to summation
  order. **The denoised endpoint is recorded as an
  APPROXIMATION** (mean |Δ| 1.77×10⁻³ vs the renderer's
  own denoise, run C) — the one endpoint the source video
  compares by eye is the one that cannot be exact, because
  it compares two different denoise runs.
- **MODIFY: PASS** — one graded variant per scene from the
  same render's passes, measured; branch boosts verified
  arithmetically exact (gloss ×1.6000).
- **Determinism: PASS** — decoded-pixel hashes identical
  across two independent build+render processes for all
  three compositor outputs.
- **Overall: PASS (agent read)**, with the denoised-endpoint
  approximation carried as a standing caveat wherever this
  technique is cited: *the recreation matches; the
  re-denoise approximates.*

## Eye items (Owner's eye is the verdict of record)

- **E-1** Grade quality of the template variant
  (`rebuild/template/out/variant_png.png` beside
  `recreated_denoised_png.png`): is the Gloss ×1.6 /
  Emission ×2.0 direction a keeper-finishing direction
  for verdict packs, or should the estate's standing
  variant use smaller gains? Agent read: legible but
  strong; the backdrop lift dominates.
- **E-2** The synthetic gate scene is a measurement probe,
  not a still (its emissive panel occludes frame-left at
  strength 6.0 and clips in display). No eye verdict is
  asked on it; it exists so every branch carries measurable
  energy.
- **E-3** The source video's own finishing chain (Glare
  bloom/streaks, RGB Curves, dispersion 0.060, Scale 1.5×,
  Box Sharpen) is distilled but not re-run; if the Owner
  wants it as the estate's standing finishing preset, that
  is a follow-on build, not part of this gate.
