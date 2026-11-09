# Plan 11 — Pass 4 Application Gate

## SHOULD-BE-SEEN (from the plan)

"PASS = three distinct, credible relights from one
render's passes. FAIL = name which adjustment still
needed the renderer, and why."

Evidence: `rebuild/passes-nswfw.exr` (the one input
render, full template settings) → `rebuild/relight-*.exr`
(pass algebra only — no renderer run between the input
render and the relights) → `rebuild/relight-*.png`
(Blender colour management, AgX + template exposure).
Measurements: `rebuild/relight-measurements.json`
(probe-scale rehearsal of every number:
`rebuild/relight-probe-measurements.json` — probe and
full figures agree to the third decimal throughout).
Full-EXR beauty-match: Σ groups vs Combined mean |diff|
**2.59e-07**, 0.0% of pixels above 1e-3.

## Gate — three relights from one render's passes

| # | Relight | Distinctness (measured, full-EXR numbers at close) | Agent read |
|---|---|---|---|
| 1 | **key-warm** — Key ×1.45, warm tint (1.25, 1.02, 0.72); backdrop down | Full EXR: luminance ×1.3712 vs base, Key share 0.756→0.843, RMS 0.4583 | Brighter, pinker key light; the same shot at a warmer hour |
| 2 | **low-key** — Fill ×0.12, Key ×0.80, Backdrop ×0.35, Accents ×1.80 | Full EXR: luminance ×0.6932, Fill share 0.161→0.028, RMS 0.3320 | Shadow side closes down; accent glints carry; mood over information |
| 3 | **neon-backdrop** — Backdrop ×2.00, cool-magenta tint; Key ×0.55, Accents ×1.60 | Full EXR: luminance ×0.6685, Backdrop share 0.055→0.167, RMS 0.3979 | The neon ground becomes the dominant source; figure reads cooler against it |

**Gate verdict (agent read; Owner eye queued): PASS** —
three distinct, credible relights produced from one
render's passes with zero additional renderer runs,
against a base comp that reproduces the renderer's
Combined from the same passes at float precision
(probe: mean |diff| 1.47e-07, 0.0% of pixels above 1e-3;
full-EXR confirmation in PASS3's close-out block).

## FAIL drivers named (what still needed — or would need — the renderer, and why)

1. **The rim relight that cannot exist.** The planned
   rim-dominant relight is IMPOSSIBLE from this render:
   `Combined_Rim` is identically zero (0 nonzero pixels)
   because Plan 02's Rim_Spot stands behind its own
   backdrop mesh and is fully occluded. No gain, tint, or
   grade applied to a zero pass yields rim light. The
   adjustment that fixes this — moving the lamp (or the
   backdrop) — is a scene change and forces a re-render
   by C-11-5's rule. This is the gate's named FAIL
   driver, and it is a defect of the *input template*,
   not of the AOV technique: the technique is what
   exposed it. The third relight slot was refilled with
   neon-backdrop (Backdrop + Accents driven), which the
   passes do support.
2. **Lamp geometry, generally.** Position, type, power
   curve / radius (falloff *shape*), backdrop image,
   geometry and materials remain re-render territory —
   gains rescale a pass but cannot move a shadow or
   change a falloff (sheet, Target 2 boundary).
3. **Guided denoise on 5.2.3.** His terminal Denoise is
   guided by Denoising Albedo/Normal passes; Blender
   5.2.3 exposes no denoising-data passes to wire
   (PASS3 drift item 4), so the estate tree's denoise
   runs unguided. A quality difference, not a relight
   blocker; named so the drift is visible.

## SFW translation record

The variant is **lane-shared by construction**: the same
script, the same groups, the same pass contract and the
same tree were built for the SFW template
(`template-sfw-aov.blend`, fingerprint ca43b4b8…), which
differs from the NSFW variant only by Plan 02's own
outfit-visibility parameter. Double-duty demonstration
(run, at probe scale 540×960 / 128 samples — the SFW
lane's passes do not exist at full settings because
Plan 02's SFW still is a PNG with no passes; the probe
render is this run's own input cost, recorded): SFW
probe EXR beauty-match mean |diff| **1.20e-07** (0.0%
of pixels above 1e-3); the **key-warm** recipe applied
to the SFW passes yields luminance ratio **1.369**
(NSFW: 1.371 — the same recipe, the same effect, other
lane). One SFW relight PNG: `rebuild/relight-sfwprobe-key-warm.png`
beside its base comp `rebuild/relight-sfwprobe-basecomp.png`.
A full-settings SFW pass render was NOT run (primo's
heavy slot was wave-contended throughout; the probe
demonstrates the lane-sharing the gate asks about).

## Eye items queued for the Owner (no Owner PASS declared)

1. The three full-res relights (`rebuild/relight-key-warm.png`,
   `relight-low-key.png`, `relight-neon-backdrop.png`)
   beside the base comp (`relight-basecomp.png`) —
   credibility of each relight as a verdict-pack option
   is an eye verdict.
2. The dead-rim finding (PASS3): Plan 02's template
   carries a lamp that has never lit a pixel. Owner call:
   repair the Plan 02 template (move Rim_Spot in front of
   the backdrop plane / re-aim) and re-issue, or record
   the rim as backdrop-emission-only by design.
3. The SFW probe relight pair — lane-sharing judged at
   probe scale only.
