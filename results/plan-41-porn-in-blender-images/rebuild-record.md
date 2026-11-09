# Plan 41 — Pass 3 Rebuild Record

Two records per the plan: (a) an AUDIT of one existing estate
keeper set against the Pass 2 grammar, measured; (b) one NEW
still composed by the grammar from the start, measured
against its own pre-registered checklist, with a determinism
check. Tools: Blender 5.2.3 LTS (estate pin) on primo,
`-Y` discipline (autoexec off) on every invocation; frame
fractions by visual grounding (bounding boxes) converted to
frame fractions, cross-checked by alpha-channel analysis
where the image has an alpha channel.

## §A — AUDIT: Plan 02's template stills vs Plan 41's grammar

**Pick, justified.** The audit set is Plan 02's own keeper
candidates — `runs/plan-02/rebuild/render-nswfw.png` and
`render-sfw.png` (both 1080×1920). Three reasons: (1) Plan 02
is this plan's commissioned triangulation counterpart, so
auditing ITS stills against Plan 41's grammar closes the
triangulation loop with measurements instead of impressions;
(2) they are the estate's standing stills template ("Neon
Backdrop"), i.e. the artifact whose habits the estate would
actually inherit; (3) they exist in two lane variants of ONE
composition, which lets the audit show the grammar is
rating-blind in application (same numbers, both lanes).
The D-802 keeper pair was the alternative; it was not picked
because it belongs to a different pipeline (2D keeper art)
and the plan asks which rules the keeper set obeys "by
instinct" — the template stills are the set the estate
re-uses, hence the set whose instincts matter.

**Method note (a friction find, recorded in the Bloch
candidate):** threshold segmentation (value/saturation masks)
FAILED on these stills — the neon backdrop saturates the
same channels as the figure — and on the source video's
frames (viewport overlays). All fractions below are from
visual-grounding bounding boxes, the same method used for
the source video's delivered still, so the comparison is
method-consistent. Fractions are of each still's own frame.
Image coordinates: y measured from the TOP, as in the
OBSERVATION §A arithmetic.

**Reference — the grammar's own example (Plan 41's delivered
still, frame g0001, measured in OBSERVATION):** camera frame
x 439–788 / y 144–930 of the 1920×1080 frame; figure
x 440–786 / y 148–929; head x 564–654 / y 148–352. Derived:
figure width fill **0.991**, height fill **0.994**, headroom
**0.005**, head centre x **0.487**, face centre y **0.135**
(face centre = head-box centre y as the measurable proxy).
Audit bands (TECHNIQUE, Adapt dispositions): fill ≥0.90 on
the dominant axis, headroom ≤0.03, head centre x in
0.45–0.55, face centre y ≤0.20.

**render-nswfw.png (1080×1920):** figure x 268–776 /
y 213–824 (of the still's own 1000-normalised grounding
frame, converted): width fill **0.508**, height fill
**0.611**, headroom **0.213**, bottom gap **0.176**; head
x 412–602 / y 213–350: head centre x **0.507**, face centre
y **0.282**.
**render-sfw.png (1080×1920):** figure x 271–785 /
y 214–822: width fill **0.514**, height fill **0.608**,
headroom **0.214**, bottom gap **0.178**; head x 413–602 /
y 214–352: head centre x **0.508**, face centre y **0.283**.
The two variants are one composition (fractions agree to
≤0.006 on every measure) — counted as ONE composition
audited twice.

**Per grammar item (auditable items only):**

| Item | Grammar (band) | NSFW still | SFW still | Verdict |
|---|---|---|---|---|
| G1 crop-to-interest / no standard-size conformance | deliverable aspect is the crop's (≈0.79 his) | 1080×1920 = 0.5625, a platform size | same | **BROKEN** (by construction — the template conforms to a platform size, the exact habit G1 refuses) |
| G2 cropping the figure allowed | figure may bleed at edges | figure fully inside frame on all sides | same | **BROKEN** (not exercised — no bleed anywhere) |
| G3 extreme fill | ≥0.90 dominant axis (his 0.99) | 0.611 high / 0.508 wide | 0.608 / 0.514 | **BROKEN** by 0.29–0.39 |
| G4 minimal headroom | ≤0.03 (his 0.005) | 0.213 | 0.214 | **BROKEN** by 0.18 |
| G5 centred head | x in 0.45–0.55 (his 0.487) | 0.507 | 0.508 | **OBEYED** |
| G6 face high / face is the focus | face centre y ≤0.20 (his 0.135) | 0.282 | 0.283 | **BROKEN** by 0.08 |
| G7 low camera looking up | camera below eye level, up-tilt ≈19° | not measurable from the still alone (no camera record in the still; Plan 02's record states camera at z 1.30 looking at a standing figure — an eye-level family shot, not a low up-angle) | same | **NOT-APPLICABLE from the still**; by Plan 02's own record, not the grammar's geometry |
| G8 standing long lens | ≈77 mm standing value | Plan 02's record: 35 mm standing | same | **BROKEN as numbered, OBEYED as discipline** (a standing value exists and is kept — the triangulation names this a per-series choice, not an error) |
| G9 pose → camera → face finish | order + final-frame face finish | not decidable from stills (process item; Plan 02's record shows the OPPOSITE order with the same final-frame check) | same | **NOT-APPLICABLE to a still audit** |
| G10 single-angle pose construction | pose holds from camera side only | the template pose is a neutral standing A-family pose, readable from many angles | same | **BROKEN** (not exercised) |
| G11 transparent-ground delivery | Film Transparent, PNG RGBA cutout | opaque composited scene PNG (backdrop IS the image) | same | **BROKEN** (different product — see triangulation: 02 delivers a finished scene, 41 a cutout) |
| G12 cheap samples + compositor denoise | 64 + Denoise node | render economics not recorded in the still; Plan 02's settings record reads adaptive 0.0100 / 4096 | same | **NOT-APPLICABLE from the still**; by record, a different economy (triangulation) |

**Audit tally (per still, identical for both variants):**
OBEYED **1** (G5) + G8's discipline half; BROKEN **6**
(G1, G2, G3, G4, G6, G10, G11 — that is 7 counting G11;
recount: G1, G2, G3, G4, G6, G10, G11 = **7 broken**);
NOT-APPLICABLE **3** (G7, G9, G12). Headline: **the estate
template obeys the grammar's centring instinct and breaks
its tightness doctrine on every axis** — fill 0.61 vs 0.99,
headroom 0.213 vs 0.005, face height 0.28 vs 0.135. The
template stills are composed like portraits WITH a room
around them; the grammar composes like a crop INTO the
figure.

**Method disagreement, recorded not resolved:** Plan 02's
PASS4 states its figure occupies "≈72% of frame height";
this run's grounded measurement of the same still reads
0.611. The difference is method (Plan 02's figure extent
likely counted hair/hat mass or used a different extent
rule). Neither number is withdrawn; the audit's comparisons
use THIS run's method consistently on both sides of every
comparison, which is what the obeyed/broken verdicts rest on.

## §B — COMPOSED STILL: Prima by the grammar

Subject: Prima on the conformed fleet rig (copy at primo
`~/.local/share/pax/night-school/plan-41/rebuild/prima.blend`,
SHA-256 `50dfd83c9d5c409af9e1d5e2046f1a9b49d3384ea942ecf059f783cd137d3f92`,
verified identical to Plan 02's recorded fleet copy).
Pre-registered checklist (written in `build_composed.py`'s
header BEFORE any render): G1 aspect 0.79 (1580×2000);
G2 height fill ≥0.90; G3 width fill ≥0.85; G4 headroom
≤0.03; G5 head centre x in [0.44, 0.56]; G6 face centre y
≤0.20; G7 camera below subject eye level, tilted up (his
19.4°); G8 PNG RGBA 8-bit, Film Transparent. Cycles, CPU,
128 samples, seed 0 (iteration economy; the grammar's G12
mechanism — denoise finish — is ON via `use_denoising`).

### Iteration 1 — FAILED, kept as evidence
Script `build_composed.py`. Three defects, in the order hit:
1. `KeyError: 'World'` — prima.blend carries no World data-
   block; fixed with a create-if-absent guard.
2. argv parsing read `--outdir` itself as the output dir
   (renders saved into a literal `--outdir/` folder); fixed.
3. The in-Blender measurement read `bpy.data.images
   ["Render Result"]`, whose pixels are NOT populated in
   headless mode (size [0,0], pixel hash = the SHA-256 of
   the empty string, `e3b0c44…`). The empty measurement
   reported fill 0.0, and the one-adjustment framing rule
   dutifully scaled the camera distance to 0.0. That run's
   internal "determinism: pixel_identical true" compared
   two empty hashes and is **void** — recorded here so no
   later reader cites it.
With the measurement fixed to load the SAVED PNG back as a
file image, iteration 1's actual renders measured (local
PIL, alpha >128, rows/cols >2% occupancy): probe (dist
1.35 m) height fill **1.000**, width fill 0.996; final
(dist 1.421 m after the one adjustment) height fill
**1.000**, headroom **0.000**, width fill **0.949**. The
agent read of the final still: frame holds the pelvis and
crossed legs; the HEAD IS OUT OF FRAME; the dress variant
flares unphysically. Root causes: (a) the framing rule's
signal saturates — fill reads 1.000 whenever the figure
bleeds at both ends, so the ratio cannot size the move;
(b) the camera aim point (z 0.62) sat at pelvis height
while the 77 mm vertical field at ~1.4 m covers only
≈0.75 m — the head was never in the solved frame; (c) the
blind pose's leg spread (Z ±16°) crossed the legs. The
grammar was not at fault; the framing MECHANISM was.
Iteration 1 files: `rebuild/run1/composed-probe.png`,
`rebuild/run1/composed-still.png` (kept, labelled failed).

### Iteration 2 — bbox-analytic framing
Script `build_composed2.py`: same checklist, same pose
family with traced trims (leg Z ±16°→±8°, hips drop
0.52→0.40 m, spine lean deepened, outfit = shirt+skirt
variant), framing solved from the posed figure's measured
world-space bounding box (figure h 1.2317 m, w 0.7161 m,
z 0.4101–1.6418): distance from the camera's own angle_y so
the figure spans 0.95 of frame height, headroom target
0.01, camera at 25% of figure height looking up.
**Result:** solved distance 4.1598 m was too far — measured
height fill **0.5735**, headroom **0.2555**, width fill
0.3582 (record `run3/composed2-record.json`). Cause:
Blender's `cam.data.angle_y` under sensor-fit AUTO is not
the render's true vertical field of view for this portrait
aspect, so the analytic distance overshot by ≈1.66×.
**Determinism (the run's clean result):** two renders,
decoded-pixel SHA-256 `98a777e93e815ebea81e83e474a47fa759a514ad8e0da1e57bff4abfc7c30174`
— **pixel-identical, real hashes** (loaded-PNG route).
Agent read of the still: whole figure in frame, seated
pose, head grounded at centre x **0.501**, face centre y
0.307 — coherent but loose; not the grammar's tightness.

### Iteration 3 — iteration-2 measurements applied (final)
Script `build_composed3.py`: identical scene; only the
camera constants change, derived arithmetically from
iteration 2's record: distance 4.1598 × (0.5735/0.95) =
**2.511 m** (the probe-ratio rule, valid here because the
probe is unsaturated), aim lowered 0.123 m so the head top
lands at 0.99 after scale-up. Measured on the delivered
still (`run4/composed3-still.png`, 1580×2000, RGBA; alpha
metrics from the build record; head by grounding):
**height fill 0.899, headroom 0.045, width fill 0.571,
head centre x 0.500, face centre y 0.121.** Determinism:
two renders, decoded-pixel SHA-256
`57e0f7c204bcba06ef249068b9962070c5064b72cbe60038cb5d16e0a27d33c6`
— **pixel-identical**.

**Checklist score (iteration 3, the delivered still):**

| # | Item | Target | Measured | Verdict |
|---|---|---|---|---|
| G1 | aspect | 0.79 | 0.790 | PASS |
| G2 | height fill | ≥0.90 | 0.899 | MISS by 0.001 (at threshold; recorded as a miss, not rounded up) |
| G3 | width fill | ≥0.85 | 0.571 | MISS — geometrically capped: this pose's figure aspect (w/h 0.58) in a 0.79 frame caps width fill at ≈0.70 when height fill is 0.95. The checklist item was over-registered for a narrow pose; his example reaches 0.99 because the floor-recline pose is wide. Checklist-design finding, carried to Pass 4. |
| G4 | headroom | ≤0.03 | 0.045 | MISS by 0.015 |
| G5 | head centre x | [0.44, 0.56] | 0.500 | PASS |
| G6 | face centre y | ≤0.20 | 0.121 | PASS |
| G7 | low camera, up-tilt | below eye level, tilted up (his 19.4°) | cam z 0.718 vs eye level ≈1.52; up-tilt 4.6° (the record's −4.63 is a sign artifact of the 90°−x formula in the script) | PASS in kind; tilt weaker than his |
| G8 | output discipline | PNG RGBA 8-bit, Film Transparent | RGBA PNG, transparent film | PASS |

**Score: 5 PASS, 1 at-threshold miss (G2), 2 misses
(G3 by geometry, G4 by 0.015).** Agent read of the still:
tight, centred, face-led framing that visibly IS the
grammar's shape; limits queued as eye items — the pose
reads seated-on-air (no ground contact; his ground shadow
catcher was not reproduced), materials render washed-out
near-white under this build's lights, legs together rather
than in his floor-recline spread, and the face is smaller
in frame than his example's (his 0.99 fill is a half-body
crop; a full-figure 0.90 fill inherently shrinks the face
share — head width here 0.147 of frame vs his ≈0.26).

**What the three iterations establish about the grammar:**
the grammar's target state is well-defined and reachable
by measurement; the failure modes were all in the framing
MECHANISM (saturating probe signal, a wrong FOV source, an
over-registered width item), not in the grammar. His
human loop (fly camera, look, retune resolution) silently
absorbs all three.
