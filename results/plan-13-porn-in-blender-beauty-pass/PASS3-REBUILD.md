# Plan 13 — Pass 3 Clean-Room Rebuild

Rebuilt from `TECHNIQUE.md` alone (video closed). Estate
toolchain: Blender 5.2.3 LTS on primo, headless, CPU,
deterministic (seed 0, fixed samples, no adaptive sampling),
file-mediated detached runs (`ns13-buildA/B/C`, `ns13-branch`,
`ns13-template`; `.done` files read as evidence). One heavy
job at a time was observed against the parallel wave: the
builds ran at `-t 2`, nice 15, beside other plans' whisper
jobs, and were serialized among themselves.

## Dependency record (Plan 11 rule)

The plan's rebuild spec says "extend the Plan 11 template
variant." At this run's Pass 3 start, `runs/plan-11/` held an
INTAKE and a build script (`build_aov_variant.py`) but **no
produced AOV template variant** — Plan 11 was still in
flight in the parallel wave. Per the brief's dependency
rule, the recreation was therefore built **on the Plan 02
template directly** (the template application in
PASS4-APPLICATION.md) plus a self-contained synthetic scene
for the measurement gate, and the substitution is recorded
here as a **deviation**. The recreation — passes +
recombination math — is self-contained; the AOV variant is
an input convenience, not the technique. Neither Plan 02's
nor Plan 11's files were modified: the template application
consumed a byte copy of Plan 02's `template-nswfw.blend`
(SHA-256 6ce16d71bc028946bbe090132ccd580fd4336e9cef2c34bc6af46ed2474d4bf3,
verified identical before and after the run).

## Deliverable mechanism

- Build script: `rebuild/build_recreate.py` (the synthetic
  gate scene + full compositor), `rebuild/measure.py` (the
  difference gate), `rebuild/branch_energy.py` +
  `rebuild/branch-energy.json` (component shares),
  `rebuild/apply_template.py` (the Plan 02 template
  application). All runs on primo under
  `~/.local/share/pax/night-school/plan-13/rebuild/`
  (`runA`/`runB`/`runC`/`runD`/`template/out`), copied into
  this run dir.
- Synthetic gate scene (designed so every recipe branch
  carries real energy): diffuse ground + cube; a glossy
  metal sphere (Gloss max 62.4 — specular firefly-class
  values); a transmission sphere; an emissive panel
  (strength 6.0); an emissive backplate (strength 2.5 — the
  background enters via Emission, as in the source scene);
  a density-0.25 volume fog cube; key/fill/rim lights;
  world strength 0. 384×288, 64 samples, seed 0.
- Compositor (built by the script, node inventory in each
  run's `node-inventory.json`): the TECHNIQUE recipe —
  Diff_/Gloss_/Trans_ (Add → Multiply) branches, Rest_
  (Volume Add → +Emission), unity/unclamped Mix nodes
  (ShaderNodeMix, RGBA, Clamp Factor on, Clamp Result off),
  one Denoise node (HDR on; Prefilter Accurate and Quality
  Follow Scene are the node's defaults, as in the source),
  a Switch A/B (Off = renderer Image, On = denoised
  recreation) feeding the composite output, File Outputs
  for every measured image as 32-bit EXR.
- **Blender 5.2 API findings** (each probed on primo before
  use; probes `/tmp/probe2..14.py` in the run's build logs):
  the compositor tree is `scene.compositing_node_group`
  (a CompositorNodeTree); the Mix node is `ShaderNodeMix`;
  File Output items are created per-name with their own
  format (node format defaults to MULTI_LAYER_IMAGE and
  must be switched to IMAGE first); the main render's
  multilayer output is `media_type='MULTI_LAYER_IMAGE'`;
  pass sockets (Noisy Image / Denoising / Volume) only
  materialize on the Render Layers node after
  `view_layer.update_render_passes()` **with the Cycles
  engine already set**; the **Noisy Image socket exists
  only when render denoising is enabled** (it is the render
  denoiser's input). 5.2's Denoising socket set adds
  Specular Albedo and Roughness beside the source's
  (5.0.1) Normal/Albedo/Depth — version drift, unused by
  the recipe.

## The measurement gate (in the brief's order)

### (a) MATCH — recreated beauty vs renderer beauty, same render

Run A (render denoise OFF; the renderer's Image is the raw
Combined), synthetic scene, recreated (raw sum) vs Image:

| stat | value |
|---|---|
| mean abs diff | **1.78×10⁻⁷** |
| max abs diff | **2.67×10⁻⁵** |
| RMS diff | 3.28×10⁻⁷ |
| % pixels beyond 1×10⁻⁶ (per-pixel max channel) | 4.29% |
| % pixels beyond 1×10⁻⁴ | **0.00%** |
| % pixels beyond 1/255 | **0.00%** |
| decoded-pixel hash equal | **no** (recreated 84c73632…, beauty 0976a3fa…) |

Verdict: **MATCH at float32 precision — not bit-for-bit.**
The recipe reproduces the renderer beauty exactly up to
summation-order rounding in float32 (the compositor adds
the branches in tree order; the kernel accumulates in
sample order). Bit-equality is not achievable through the
compositor and is not claimed; the measured distance from
it is the table above.

Cross-checks that pin the cause to rounding, not recipe:
- Run C (render denoise ON) writes the Noisy Image socket;
  recreated vs **Noisy Image**: identical statistics
  (mean 1.78×10⁻⁷, max 2.67×10⁻⁵, 0.00% beyond 1×10⁻⁴), and
  run C's Noisy Image decoded hash **equals** run A's
  beauty hash (0976a3fa…) — the raw Combined is the same
  object whether or not the renderer denoises it.
- Run C's recreated / recreated_denoised / variant decoded
  hashes equal run A's exactly — the compositor result is
  independent of the render-denoise flag, as it must be.

**The denoised endpoint (the comparison the video actually
makes): APPROXIMATION, recorded with its gap.** Run C,
compositor-denoised recreation vs renderer-denoised beauty:

| stat | value |
|---|---|
| mean abs diff | 1.77×10⁻³ |
| max abs diff | 0.124 |
| RMS diff | 3.63×10⁻³ |
| % pixels beyond 1/255 | 23.21% (76.79% within 1/255) |

Cause: not the recipe (proven exact above) — the two
denoises are different runs: Cycles' internal denoise vs
the compositor Denoise node, with different guide-feature
sets (5.2's renderer-side denoising can use specular
albedo/roughness weighting; the compositor node receives
Albedo + Normal only). The gap concentrates where guides
differ most (speculars/edges). Per the plan gate, the
denoised recreation is adopted **as an approximation with
this measured gap**, not silently as a match.

### (b) MODIFY — one graded variant the renderer alone could not produce

Variant (same render, passes only): **Gloss ×1.6 and
Emission ×2.0** inside the sum, then the same Denoise node.
The renderer alone cannot re-weight components of a
finished render — the components exist only as passes.

| pair | mean abs diff | max abs diff | % px beyond 1/255 |
|---|---|---|---|
| variant vs recreated_denoised (synthetic) | 0.999 | 41.1 | 99.22% |
| variant vs recreated_denoised (template) | 0.149 | 0.710 | ~100% |

(HDR scene values: the synthetic's large mean is the
doubled emissive backplate, which is 74.7% of the sum's
energy — see branch shares. The template's beauty-scale
values are the keeper-relevant read.)
Branch verification (runD, synthetic): branch mean shares
of the recreated sum — Diffuse 17.34%, Glossy 6.75%,
Transmission 1.18%, Rest 74.73% (of which Emission 0.945
mean, Volume 0.064 mean, derived exactly from the boosted
run: rest_v − rest = Emission; gloss_v / gloss = **1.6000**
— the boost lands arithmetically exact).

### Determinism

The comp is deterministic: runs A and B are two independent
processes rendering the same script; **decoded-pixel hashes
are identical for recreated (84c73632…), recreated_denoised
(af1ae4a2…) and variant (1d6e2a71…)**. (Hashes are of decoded
pixels, never of PNG/EXR files — PF-2.)

## Claims scorecard (from OBSERVATION.md)

- **C-13-1** (recipe) — **REPRODUCED.** The measured match
  is the recipe's proof: any wrong branch math would show
  as structured difference; the residual is float rounding.
- **C-13-2** (recreation reproduces the beauty) —
  **REPRODUCED with the honesty amendment**: exact at
  float32 for the raw sum; the *denoised* comparison the
  video performs is an approximation (measured above).
  His first-attempt failure (missing Volume) also
  reproduced the recipe's completeness condition in the
  source itself.
- **C-13-3** (one end-of-chain Denoise with Albedo/Normal
  guides) — **REPRODUCED** (the node runs at defaults and
  produces the clean endpoint measured in run C).
- **C-13-4** (passes must be enabled pre-render) —
  **REPRODUCED by construction** (the build enables the
  set before rendering; sockets for disabled passes do not
  exist — probed directly in the 5.2 API probes).
- **C-13-5** (background enters via Emission) —
  **REPRODUCED**: the synthetic's backplate is emissive
  geometry over a black world; omitting Emission from the
  sum would remove the background (branch share: Emission
  mean 0.945 of a 1.350 total — the background *is* the
  largest single component).
- **C-13-6** (uniform branch grammar, duplicate per
  component) — **REPRODUCED as form**: the script builds
  one component function and instantiates it three times.
- **C-13-7** (finishing moves) — **PARTIALLY REBUILT**:
  the graded variant (the gate's named modify) is built
  and measured; the video's whole-image finishing chain
  (Glare/Streaks/Curves/Lens Distortion/Scale/Sharpen) is
  distilled in TECHNIQUE as the finishing menu but not
  re-run — it is post-match grading, not the recreation
  technique under gate. Recorded as a scope decision, not
  a silent omission.
- **C-13-8** (no clamping; HDR survives) — **REPRODUCED**:
  all Mix nodes Clamp Result off; recreated EXR max values
  reach 62.4 (the glossy branch's specular peak) unclamped.

## Measurement-tool defect (filed, fixed in-run)

The first measurement pass reported **identical hashes for
every output** — `measure.py` passed `OpenEXR.FLOAT`
(invalid in the installed OpenEXR 3.5 binding) and a
try/except silently substituted an array of ones. The
identical-hash smell caught it; the reader now uses the
header-declared channel type and fails loudly. All numbers
in this record come from the fixed reader (its output is
`rebuild/runA/measurements.json` and siblings on primo).
The lesson is filed in BLOCH-CANDIDATE.md.
