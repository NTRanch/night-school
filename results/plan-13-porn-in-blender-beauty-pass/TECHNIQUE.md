# Plan 13 — Pass 2 Technique Sheet (Distillation)

Source: `OBSERVATION.md` (Pass 1). Every Pass 1 claim is
distilled below. Estate context: Blender 5.2.3 (source video:
Blender 5.0.1 — version drift recorded where it bites),
scripted/headless discipline, keeper-still finishing for the
Plan 02 template lane. The presenter's own source is the
Chaos V-Ray "Back to Beauty" documentation; the Cycles form
below coincides with Blender's documented pass-combining
example, and Pass 3 verifies it by measurement rather than
by authority.

## Target 1 — The recombination recipe (exact pass math)

**Named estate form — NS13 "Back-to-Beauty" recreation.**
Enable before rendering (View Layer → Passes): Combined;
Denoising Data; Diffuse Direct/Indirect/Color; Glossy
Direct/Indirect/Color; Transmission Direct/Indirect/Color;
Volume Direct/Indirect; Emission. (Ambient Occlusion may be
enabled — the source tree carries the socket — but it is
**not** part of the beauty sum. No Subsurface passes, no
Environment pass in this recipe.)

In the compositor, from the Render Layers node (all Mix
nodes at Factor 1.000, Clamp Factor on, **Clamp Result
off** — HDR survives):

```
Diff  = (Diffuse Direct + Diffuse Indirect) × Diffuse Color
Gloss = (Glossy Direct + Glossy Indirect) × Glossy Color
Trans = (Transmission Direct + Transmission Indirect)
        × Transmission Color
Rest  = Volume Direct + Volume Indirect + Emission
Beauty_recreated = Diff + Gloss + Trans + Rest
```

One line each, as the brief asks:
- Diffuse branch: (Dir + Ind) × Color — the albedo-weighted
  diffuse light.
- Glossy branch: (Dir + Ind) × Color — the reflection/
  specular light, tint in the Color pass.
- Transmission branch: (Dir + Ind) × Color — glass/refraction
  light (in the source scene: the character's glasses).
- Volume branch: Dir + Ind added raw — scattering has no
  Color pass; there is nothing to multiply by.
- Emission branch: added raw — emissive geometry (in the
  source scene: the background itself, an emissive
  screenshot backplate) enters the beauty *only* here.
- Sum: the four branches added at unity, unclamped.

Branch grammar is uniform — build one (Add → Multiply)
pair, Shift+D-duplicate it per component; chain further
components into the sum on the **B** input ("whatever new
thing we're bringing in, we plug it on B").

Completeness is the failure mode: **omit a branch and the
recreation visibly diverges** — demonstrated in the video
itself, where the first A/B comparison failed because
Volume was missing ("well it's not quite the same — we're
missing volume"). The recipe is exact only as a *complete*
sum over the components the scene actually uses; the
V-Ray page's own caveat applies: elements the scene does
not use may be excluded.

**The honesty question, answered from evidence:** does the
recreation reproduce the renderer beauty bit-for-bit before
modification?
- *In the video:* never measured. The artist's evidence is
  a Switch-node A/B viewed by eye, twice — the first attempt
  **failed** (missing Volume), the second was declared
  "successfully reconstructed" by eye. No numbers exist in
  the source.
- *In the estate rebuild (Pass 3, measured):* the **raw**
  recreation matches the renderer's raw Combined to float
  precision — mean |Δ| 1.78×10⁻⁷, max |Δ| 2.67×10⁻⁵, 0.00%
  of pixels beyond 1×10⁻⁴ (synthetic scene) and mean
  1.69×10⁻⁷ / max 3.34×10⁻⁶ / 0.00% beyond 1×10⁻⁴ on the
  Plan 02 template. Decoded-pixel hashes are **not** equal:
  the match is exact at float32 rounding (summation order),
  not bit-for-bit. The **denoised** endpoint — the one the
  video actually compares — is an **approximation**: the
  compositor Denoise node and the renderer's internal
  denoise are different runs with different guide features,
  measured at mean |Δ| 1.77×10⁻³, 23.2% of pixels beyond
  1/255 on the synthetic scene (see PASS3-REBUILD.md).
  Recorded as approximation with its measured gap, per the
  plan gate — never adopted silently.

## Target 2 — Denoise strategy

- The constituent passes are **raw**: only the Combined the
  renderer ships has been denoised (source render: render
  Denoise ON, 512 samples, adaptive threshold 0.0300,
  min 120). A recreated sum is therefore noisy by
  construction and **must be re-denoised** — this is the
  recreation's cost, not one of its benefits.
- Placement: **one Denoise node, once, at the end of the
  sum** — never per pass. Every branch, Volume included,
  is summed *before* it, on the artist's own reasoning:
  "I think we have to do it before the denoise, because the
  volume AOV could be noisy."
- Guides: the render's **Denoising Albedo → Albedo** and
  **Denoising Normal → Normal** sockets; Denoising Data
  must be enabled before rendering or the guides do not
  exist. Node settings are the defaults: **HDR ✓,
  Prefilter Accurate, Quality Follow Scene**.
- Cost in detail: whatever a single OIDN-class denoise
  costs — the same cost the renderer already paid on the
  Combined, paid a second time on the recreation, with a
  measurable (small) divergence from the renderer's own
  result because the guide-feature set differs (Pass 3
  numbers above). Per-pass denoising is rejected: it would
  pay the cost per branch and break the sum's noise
  statistics.

## Target 3 — The control surface (what becomes adjustable)

Once the recreation matches, every branch is an independent
gain/tint in the sum — changes that otherwise need a
re-render (the source render took 8:23 on the artist's GPU):

- **Per-component gain** — demonstrated in the video: fog
  (Volume) reduced in comp, "instantaneously"; any branch
  can be scaled, soloed (Emission soloed: "this is the
  emission — the background"), or muted.
- **Per-component tint** — demonstrated: the background
  (Emission branch) re-hued green → purple in comp ("I
  could change the hue, I could change the saturation").
- **Component re-addition** — demonstrated: the Volume sum
  added a *second* time after the denoise and the AO
  multiply as a fog boost ("we already incorporated volume
  here, but I'm doing it again because it looks better").
  This is a grade, not recipe: the matched form counts
  every component exactly once. Estate rule: any
  re-addition downstream of the match must be labelled a
  grade in the record (the image it produces is graded,
  not matched).
- **AO multiply** — demonstrated post-denoise ("it has to
  go at the end of the chain, after the denoising"; his
  eye verdict: "makes the model more realistic"). Also a
  grade, on the same labelling rule.
- **Finishing on the matched sum** — demonstrated: Glare
  Bloom add-back (Medium, Size 0.500; HSV node at neutral
  in its feed), Glare Streaks (High, Threshold 1.000,
  Smoothness 0.100, 4 streaks @0°, Iterations 3, Fade
  0.900, Color Modulation 0.250), RGB Curves, Lens
  Distortion dispersion (previewed at 1.000, settled at
  **0.060**), Scale 1.5×, Box Sharpen; output 720×1280 PNG
  (16-bit selected).
- What still forces a re-render: anything that changes the
  passes themselves — geometry, materials' base properties,
  light placement/energy (per-*light* relighting is Plan
  11's light-group AOVs, a different decomposition), sample
  count, and any pass not enabled before the render.

## Adopt / Adapt / Reject

- **Adopt:** the complete-sum recipe with the exact pass
  set and unity/unclamped Mix discipline; denoise-once-at-
  the-end with Albedo/Normal guides at defaults; the
  Switch-node A/B as the *qualitative* check (never as the
  gate); branch-gain as the keeper-finishing control.
- **Adapt:** the estate form is **scripted** (compositor
  built by code in the render script, branches named
  Diff_/Gloss_/Trans_/Rest_), and the A/B is replaced as
  the gate by **measured difference statistics** against
  the renderer's Combined from the same render (mean/max
  |Δ|, % pixels beyond stated tolerances, decoded-pixel
  hashes) — the video's eye-only comparison is the one
  part of its method the estate does not inherit. The
  recreation is applied to the Plan 02 template as the
  estate's template render (Plan 11 dependency rule,
  PASS3-REBUILD.md). Blender 5.2 notes: the compositor
  tree is a node-group data-block; the Mix node is
  ShaderNodeMix (RGBA); Denoising sockets additionally
  include Specular Albedo / Roughness in 5.2 (unused by
  the recipe, as in the source).
- **Reject:** per-pass denoising (breaks the sum, pays the
  cost per branch); clamping anywhere in the recipe (the
  source keeps Clamp Result off throughout — HDR headroom
  is what makes branch gains safe); AO as part of the
  recreation sum (AO is a utility pass, not a beauty
  component — the sum must match *before* any AO touches
  it); treating the denoised endpoint as "the match" (it
  is an approximation of the renderer's denoise, measured
  as such).
- **Adapt (the AO multiply):** the source *does* multiply
  AO in — as a post-match grade, "at the end of the chain,
  after the denoising." Estate form: permitted only as a
  labelled grade step downstream of a measured match,
  never inside the recreation, and any image it touches is
  reported as graded, not matched.
