# Plan 17 — Pass 3 Record: Dispositions, Not a Build

Per the plan, this plan has **no separate scene build**:
"any unmatched finishing technique gets a scoped test
there [the Plan 11/13 template work]". This record is
therefore the disposition table the gate requires:
every technique in the video is either a **CONFIRMATION**
(it has a counterpart in the estate set — Plans 02/11/13
as landed) or **UNMATCHED**, and every unmatched
technique is dispositioned **SCOPED TEST** (a runnable
proposal handed to the Plan 11/13 template programme)
or **REJECT** (reason from evidence).

## Confirmations (counterpart exists — no new test)

| # | Technique (OBS ref) | Estate counterpart |
|---|---|---|
| K-1 | Adaptive sampling pair as template default (0.0100/4096, OIDN) (OBS §2) | Plan 02 NS02 preset (Adopt); Plan 01 T-21 — third workflow confirmation |
| K-2 | Production retune to 0.0300/512 GPU (OBS §7) | Plan 13's production render (0.0300/512, C-13-A) — cross-confirmed within the creator's own set |
| K-3 | Emissive environment geometry as backdrop (OBS §3) | Plan 02 backdrop (Adopt/Adapt-procedural); Plan 11 photo plane; Plan 13 backplate Emission 5.000 |
| K-4 | Role-named lamp grammar, fills 50 W/6500 K (OBS §5) | Plan 11 C-11-1 scene family; Plan 02 role system |
| K-5 | Silhouette-first lamp build against the live render (OBS §5) | Plan 02 Target 1 (Adopt) |
| K-6 | Volume fog cube for atmosphere (OBS §5) | Plan 11 fogbox / Plan 13 fogbox (same scene family) |
| K-7 | Pass solo-inspection before comp work (OBS §8.1) | Plan 11 solo previews (OBS 3:30/4:00); Plan 02 clay check (analogue) |
| K-8 | HSV as the universal adjuster node (OBS §8.3) | Plan 11 C-11-3 (per-group); Plan 13 HSV in finishing chain |
| K-9 | Glare Bloom in the finishing tail (OBS §8.4) | Plan 11 Glare groups; Plan 13 Bloom add-back (C-13-7) |
| K-10 | Outfit-component toggling for delivery variants (OBS §5) | Plan 02 Target 2 item 5, Adapt form (outfit-variant selection at build time) |

## Unmatched techniques — dispositions (8)

### SCOPED TEST (5) — proposals to the Plan 11/13 template programme

**ST-17-1 — Enclosing environment dome (OBS §3, C-17-2).**
No estate counterpart: NS02's environment is a curved
cyclorama *behind* the subject; a UV-sphere dome
*encloses* the scene (backdrop in every direction,
including reflections and above-frame).
- Input artifact: Plan 02 NS02 template
  (`runs/plan-02/rebuild/template-nswfw.blend` +
  `render-nswfw.png` as the control).
- Procedure sketch: variant build adding a scaled
  UV-sphere with the template's procedural neon texture
  wired as at OBS §3 (image → Principled, emission
  effect verified via an Emission-pass solo); camera
  orbited to three angles (front / three-quarter /
  low) that the cyclorama cannot cover.
- Pass measure: at all three angles the figure reads
  against authored environment (no void/grey in frame),
  and the Emission solo shows the dome contributing;
  FAIL = any angle shows un-authored background, or
  dome light flattens the NS02 key/rim read (compare
  against the control's Pass-4 driver #1/#2 verdicts).

**ST-17-2 — Gradient world as a designed term (OBS §5,
C-02-B difference).** NS02 sets World 0.000;
Part 2 authors a gradient world (World_OW2) *alongside*
emissive geometry.
- Input artifact: NS02 template renders (both variants).
- Procedure sketch: variant with a two-stop gradient
  world (dark floor tone → backdrop-dominant hue),
  strength tuned so the world term is measurable but
  subordinate; render both variants.
- Pass measure: shadow-side separation improves or
  holds vs control (Pass-4 driver #1 re-scored) AND the
  world term is provably subordinate: a world-only
  render (lamps off) reads as gradient, not as a lit
  scene. FAIL = the gradient washes the silhouette-first
  read or merely duplicates the backdrop's job.

**ST-17-3 — Duplicate-and-halve rim balancing (OBS §5,
C-17-3).** The estate template tunes rim power as a
parameter; it has no *procedure* for a second rim.
- Input artifact: NS11 variant EXR of the NS02 scene
  (Plan 11 Pass 3 artifact, when landed; otherwise the
  NS02 render pair).
- Procedure sketch: add Rim_Spot_2 as a duplicate of
  Rim_Spot at full power (1000 W), then render/comp the
  halving series 1000 → 500 → 250 W; score each against
  the single-rim control.
- Pass measure: a halving step exists at which the
  two-rim read beats the single rim on edge separation
  on BOTH sides of the figure without hotspot clipping
  (pixel-stat: rim-region highlights below clip
  threshold); FAIL = every step either clips or reads
  identical to one rim (procedure adds nothing).

**ST-17-4 — Additive atmosphere boost: Add (Volume
Direct + Emission) × 0.492 over Combined (OBS §8.2,
C-17-6).** The estate's comp grammar sums passes
*instead of* Combined (11/13); adding two of them
*on top of* Combined is untested and algebraically a
double-count.
- Input artifact: one NS11 multilayer EXR (Combined +
  Volume Direct + Emission in a single file).
- Procedure sketch: comp the boost at Factors 0.25 /
  0.492 / 0.75; compare against the un-boosted Combined
  and against a re-render with the volume density
  raised (the render-side way to get the same fog).
- Pass measure: the 0.492 boost reads as atmosphere
  (depth separation up, figure contrast held within
  5% mean-luma delta on the figure mask) and is not
  distinguishable as double-exposure on the emissive
  rings (ring-region luma ≤ 1.5× the Combined's);
  FAIL = rings blow out or fog reads as a grey veil —
  in which case the estate keeps the render-side route
  and this technique is rejected with that measurement.

**ST-17-5 — The 13/17 finishing tail as a named
template stage: Glare Streaks + Lens Distortion
dispersion (OBS §8.4–8.5; Plan 13 C-13-7).** NS11's
grammar has per-branch Bloom; neither estate template
carries the master-level Streaks stage or the
dispersion finish that *both* Divinity videos apply.
- Input artifact: one graded master from the NS11
  relight programme (any verdict-pack candidate).
- Procedure sketch: append Streaks (High, Thr 1.000,
  Smooth 0.100; Plan 13's full values: 4 streaks,
  Iterations 3, Fade 0.900, Color Mod 0.250) then Lens
  Distortion Dispersion at 0.040 (17) and 0.060 (13);
  A/B against the master without the tail.
- Pass measure: star/highlight points streak without
  streaking skin highlights (skin-mask streak energy
  ≈ 0), and dispersion reads as lens character at
  frame edges only (centre-crop fringe ≈ 0 px);
  FAIL = either stage smears the subject or the two
  dispersion values are indistinguishable (then the
  stage is ceremony and is rejected as such).

### REJECT (3)

**RJ-17-1 — External web AI upscale as the delivery
step (OBS §9, C-17-7).** REJECT for the estate.
Reasons from evidence: (a) non-deterministic — a
third-party web service (imgupscaler.ai, found by a
live search) whose model/version the video never
names; the same input cannot be shown to reproduce
the same output, violating the estate's deterministic
pipeline doctrine; (b) data egress — the finished
art leaves the estate to an unrelated service, in the
NSFW lane, with no licence/privacy terms examined on
screen; (c) superseded — Plan 13 demonstrates the
in-comp alternative from the same creator (Scale +
Box Sharpen, C-13-E), and the estate's own resolution
policy is render-at-target or deterministic upscale.
The *premise* (delivery resolution is made in post)
is adopted via C-13-E/ST-17-5's lane, not via this
service.

**RJ-17-2 — OpenEXR DWAA (lossy) as the output codec
(OBS §8, C-11-F).** REJECT as the estate contract.
Reason: already decided on evidence in Plan 11 Pass 2
— DWAA spends its error in the dark gradients this
pipeline exists to adjust; the estate contract is
multilayer EXR 32-bit ZIP (lossless). His single-layer
DWAA file also cannot carry the NS11 pass contract.
No test is owed: the deciding comparison was made and
recorded in Plan 11's TECHNIQUE.md.

**RJ-17-3 — Live web search as a production step
(OBS §4, §9).** Judged **not-a-technique**: searching
Google Images for a three-point diagram, and Google
for an upscaler, are sourcing habits with no
transferable mechanism (the same judgement class as
Plan 02's reference-site note and Plan 11's
Google-Images backdrop sourcing — the latter also a
licensing hazard the estate routes around with
procedural environments). The *content* the search
delivered (three-point roles; the upscale premise) is
distilled at OBS §4 / C-13-E; the habit is not
adopted.

## Claims disposition (Pass 1 list → this record)

| Claim | Disposition |
|---|---|
| C-17-1 order of operations | Adopt as the named finishing order (F-17-01…18); joins Plan 16 per OBS §10 |
| C-17-2 dome environment | Adapt — via ST-17-1 test before any template adoption |
| C-17-3 five-lamp three-point + duplicate-and-halve | Adopt roles (K-4/K-5); the halving procedure via ST-17-3 |
| C-17-4 template pair vs production pair | Adopt as recorded correction to Plan 02's sheet reading (TECHNIQUE C-02-D): pairs are defaults + a named retune step |
| C-17-5 no light groups in production | Recorded as the convergence finding (TECHNIQUE headline); no estate action — NS11 remains the estate's relight lane, now knowingly a *specialist* tool, not the production default its creator's marketing claims |
| C-17-6 Volume+Emission boost | Adapt-pending-test — ST-17-4 decides |
| C-17-7 post-made delivery resolution | Adopt premise (via C-13-E); Reject the web-service route (RJ-17-1) and DWAA (RJ-17-2) |
| C-17-8 plan framing ("finishing half") | Scoped per OBS §1: lighting/render/output hold; animation polish absent — recorded, not a gate failure |
