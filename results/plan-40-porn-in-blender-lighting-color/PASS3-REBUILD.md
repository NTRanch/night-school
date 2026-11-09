# Plan 40 — Pass 3 Rebuild: the NS40-ResolveFirst variant

Method: extend a COPY of the Plan 02 template of record with Plan 40's
measured rig + grade; render Prima through BOTH; per-group energy by
the Plan 11 method; determinism by twin decoded-pixel hash. All
artifacts on primo `~/.local/share/pax/night-school/plan-40/rebuild/`,
mirrored to this run dir's `rebuild/`. Blender 5.2.3 LTS, `-Y`,
CPU + seed 0 throughout.

## 1. The control is a verified copy

The Plan 02 template was rebuilt fresh from `prima.blend` by its own
`build_template.py --variant nswfw --no-render` on primo
(`rebuild/build-control.log`): **FINGERPRINT
ca585ca41656ea6e3a80c504143eb1d504ee717cecb8034b4d9b199bcbb5570a —
identical to the template of record.** The template file itself was
never opened for writing.

## 2. The variant: NS40-ResolveFirst

Built by `rebuild/p3_build_variant.py` on the template copy (the copy
only): the NS02 rig is removed and replaced with a 7-lamp translation
of OBSERVATION §3.3's reads onto the template stage (positions are
estate translations; every power/size/angle/colour is a screen read):

| Variant lamp | Type | Power | Size / angle | Colour | Group |
|---|---|---|---|---|---|
| NS40_Key_Area | Area ellipse | **8.8 W** | 1.0×1.0 m | pink (1.0, 0.55, 0.85) | NS40Key |
| NS40_Fill_Area | Area ellipse | **10 W** | 1.0×1.0 m | white | NS40Fill |
| NS40_Strip_Area | Area ellipse | **10 W** | 0.16×0.45 m | white | NS40Strip |
| NS40_Key_Spot | Spot | **25.7 W** | 14.2°, blend 0.732 | white | NS40SpotKey |
| NS40_Rim_Spot | Spot | **25.7 W** | 14.2°, blend 0.732 | white | NS40SpotRim |
| NS40_Fill_Point | Point | **10 W** | radius 1 cm | white | NS40Points |
| NS40_Accent_Point | Point | **1 W** | radius 0.1 cm | white | NS40Points |

The rim spot sits at y = +1.0 — camera-side of the backdrop wall
(y = +1.3) — unobstructed by construction, the C-40-3 test. Exposure
0.0 (the template's −1.8 is Plan 02's estate fill; the variant's lift
lives in the grade, as his does). Variant fingerprint (final build):
**d95fa6e57d455670feaa29e59c049b456f6c5b4c7d301fc3053d92d42181a4c2**
(`variant/fingerprint-variant.json`).

**The grade** (compositor translation of his Resolve contract,
TECHNIQUE §3) — six stages, all present in the final build's readback
with zero build notes: FilmicBlend (RGB Curves S, toe lifted to 0.10)
→ TealOrange (ColorBalance lift (0.94,1.03,1.05), gain (1.07,1.0,0.93))
→ Contrast (gentle S) → Glow (Glare Bloom, threshold 1.0, strength
0.6) → Vignette (ellipse 0.85, blur 240, gain floor 0.72) → Sharpen
(Box Sharpen, factor 0.5). Denoise maps to render-side OIDN (the
template's estate choice), standing in for his two-stage
OptiX+Resolve NR. **Iteration honesty:** the first build silently
dropped three stages to Blender 5.2's socket-driven compositor API
(readback caught it); a second build's vignette (0.62 ellipse, 0.42
floor) produced a visible halo ring and was rejected on sight; the
third build is the variant of record. Superseded renders are kept as
`beauty-variant-graded-v1-partial.png` / `-v2` measurements in the
measure JSONs — the attribution rows live in BLOCH-CANDIDATE.md.

## 3. Per-group energy (probe EXR, 540×960 @ 0.0100/128)

`measure-probe-out.json` / `measure-v3-out.json`, Plan 11 `lum()`
(Rec.709), shares of group-sum mean luminance:

| Group | Control share | Variant group | Variant share |
|---|---|---|---|
| Key | **0.7558** | NS40Fill (10 W area) | **0.2706** |
| Fill | 0.1611 | Backdrop | 0.2657 |
| Rim | **0.0000** | NS40Points (10+1 W) | 0.1695 |
| Accent_1..4 | 0.0277 (total) | NS40Strip (10 W) | 0.1374 |
| Backdrop | 0.0554 | NS40Key (pink 8.8 W) | 0.1228 |
| | | NS40SpotKey (25.7 W) | 0.0334 |
| | | **NS40SpotRim (25.7 W)** | **0.000663** |

- **Cross-validation:** the control's shares reproduce Plan 11's
  published numbers to 3–4 decimals (Key 0.7558, Fill 0.1611 vs
  0.1612, Backdrop 0.0554, accents 0.0277, Rim 0.0000) — the copy,
  the groupify, and the method are all verified against the
  triangulation record. **The dead rim reproduces exactly: 0.0.**
- **Backdrop absolute energy is identical on both sides** (mean lum
  0.033778) — same emissive backdrop; only the rig changed.
- **The rim is live but faint (C-40-3):** the variant's behind-subject
  spot contributes 0.000663 of group energy (mean lum 8.43e-05) vs
  the template rim's exact 0.0. Unobstructed geometry makes his rim
  *exist*; at 25.7 W through a 14.2° cone it remains a whisper. The
  Plan 11 failure is designed out by his construction; the *strength*
  the template credits its rim with was never real on either side.
- **Structure (C-40-2):** no variant source exceeds 27.1% — a flat
  micro-source field vs the control's 75.6% single-key hierarchy.
- **Plate level (C-40-4 setup):** variant Combined mean lum **0.1272**
  vs control **0.6101** (linear) — the variant plate leaves the
  renderer **4.8× darker**, matching his own near-black EXR
  (OBSERVATION §5.1) in kind.
- Σ-vs-Combined: energy sums match (0.61022 vs 0.61014; 0.12714 vs
  0.12718) but pixel mean|diff| is 0.0139 / 0.0052, not Plan 11's
  2.59e-07 — because here the File-Output Combined is the
  render-denoised image while group passes are raw (Plan 11 denoised
  in comp from the raw sum). Named so nobody compares the two checks
  naively; shares are computed among raw passes on both sides.

## 4. Determinism

Twin probe renders of the variant: decoded Combined-pixel SHA-256
**a12557c3fe5998b3ace9b35da1bf3638f1e45009cb537e6d48f70a13e973da08
on both** (`measure-probe-out.json`, `determinism_combined_pixel_equal:
true`). Pixel hash, never file hash. (The later `measure-final-out.json`
False is a file-lifecycle artifact: beauty renders overwrote
`passes-variant.exr` at 1080×1920 — 168,771,590 B vs the probe's
42,276,636 B — before that config re-read it. The twin evidence was
copied aside as `passes-twin1.exr` before any beauty ran.)

## 5. The judged pair (beauties, 1080×1920 @ 0.0100/384, matched pair)

The beauty pair holds threshold + cap constant on both sides
(documented deviation: control's own pair is /4096, the variant's
/128 — the *pair*, not each creator's ceremony, is what's judged;
Plan 17's retune precedent). Stats from `measure-v3-out.json`
(decoded-pixel, display space):

| Plate | Mean lum | Channels (R, G, B) | % px > 0.5 |
|---|---|---|---|
| Control (NS02) | 0.3742 | 0.407, 0.357, 0.444 | 23.79 |
| Variant RAW | 0.3140 | 0.377, 0.287, 0.396 | 12.85 |
| Variant + NS40 grade | 0.3992 | 0.383, 0.400, 0.437 | 12.81 |

Pairwise: control vs graded mean|Δ| 0.1159, RMSE 0.1382;
raw→graded mean|Δ| 0.0710, RMSE 0.0892 — the grade's measured work:
**+27.1% mean luminance** (0.3140 → 0.3992), green-led
(R +0.006, G +0.113, B +0.041) — the teal-axis lift and filmic toe
doing exactly the job they were placed for, ending 6.7% brighter
than the control's own finished still.

**Named differences** (agent read of `side-by-side.png` — control /
variant raw / variant graded, in that order):

1. **Cast shadow.** Control throws a hard directional floor shadow
   (the 1000 W key). The variant raw plate has *no* cast shadow —
   the micro-sources cancel. A light-rig difference, present before
   any grading.
2. **Backdrop.** Control: saturated neon gradient + a specular
   hotspot upper-left. Variant raw: same saturation (emissive,
   unchanged) but no hotspot. Variant graded: saturation crushed to
   mauve-grey; the backdrop stops being the picture's subject.
3. **Modelling.** Control: sculpted key/fill ratio. Variant: soft
   wrap, low modelling contrast, figure reads flatter and pinker.
4. **Shadow palette.** Graded variant's floor/shadows go deep teal
   (the TealOrange lift), against the control's blue floor — the
   Qazi axis is visible, not just numeric.
5. **Anchoring.** The control figure is grounded by its shadow; the
   variant figure floats slightly — his method on THIS stage (an
   emissive cyclorama, not his dark interior) loses the practicals
   that anchor his own scenes. Set-dependence is a property of the
   method, evidenced here.
6. **Energy distribution.** Control highlights concentrate (23.8% of
   px above 0.5 lum); the variant spreads lower and flatter even
   after grading — a dusk read, not a neon read.

## 6. Claim verdicts

- **C-40-1 (separability)** — SUPPORTED by construction + his own
  two-EXR delivery; not independently measurable on this stage.
- **C-40-2 (lamp scale/structure)** — **CONFIRMED**: distributed
  shares (§3), no dominant source, no cast shadow (difference 1).
- **C-40-3 (live rim)** — **CONFIRMED, faint**: 0.000663 vs 0.000000.
- **C-40-4 (grade carries the look)** — **CONFIRMED**: raw plate
  4.8× darker (linear); the grade performs the exposure + palette
  work (§5 numbers). On his own dark-interior class of scene the
  effect is stronger (his EXR is near-black; this stage's emissive
  backdrop floors the plate at 0.314 display).
- **C-40-5 (noise economics)** — CONSISTENT, not directly measured:
  the variant probe at his pair (0.0100/128) + OIDN produced a clean
  plate on this stage; no second-stage NR was needed here, so the
  *necessity* of his Resolve NR is stage-dependent — stated, not
  overclaimed.
- **C-40-6 (real DoF)** — NOT TESTED on this stage (the template
  camera has no DoF; adding it would break the matched-pair rule).
  Carried as an observation-side difference (T-40-10), not a rebuild
  claim.
