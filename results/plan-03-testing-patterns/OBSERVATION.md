# Plan 03 — Observation (Pass 1, adapted per the re-scope)

Reference-only run: Pass 1 observation + Pass 2 distillation
(TECHNIQUE.md). Pass 3 = none (the plan's clean-room spec is
"None — reference-only item"); recorded in
PASS4-APPLICATION.md. All reads below are agent reads from the
captured file; the Owner's eye is the verdict of record for any
watchability judgement (queued in PASS4-APPLICATION.md).

Frame numbering: the file is 60 fps, 4,963 frames, 82.716667 s.
Frame f at time t = f/60 s. Grid stills `grid_NNN.png` are at
t = NNN−1 s. Every number traces to `records/` (see
MANIFEST.md).

## §1 What the file actually is (the surprise, stated first)

The plan's intake correction called this "a 1:23 Virt-A-Mate
performance clip". The capture refines that: **it is a screen
recording of the VaM editor in Edit Mode while the creator
tests a parametric animation pattern live.** Evidence, readable
in every grid frame:

- The VaM UI bar is on screen throughout (bottom-left):
  "VaM: 1.22.0.1 vamX: 1.29", **Edit Mode (E) checked**, Play
  Mode unchecked, "Add vamX To Scene" button.
- A floating in-scene panel carries three sliders labelled
  **depth**, **bias**, **speed** and a toggle button that reads
  **stop** while the pattern runs and **play** while it is
  stopped (both states photographed: grid_005 "play",
  grid_001 "stop").
- The driven motion path is drawn in the scene: a horizontal
  line through the female's head height with magenta square
  waypoints, two red dots near the contact end, orange dots,
  and a green gear-shaped target marker that travels the line.
- A mouse cursor is visible in many frames, repeatedly on the
  sliders (t≈13 on speed, t≈25.8 on bias, t≈41 on speed,
  t≈65+ near speed); the VaM status bar names the highlighted
  control ("UISlider#2.control", "UISlider#3.control").
- The title is literal after all: the creator is **testing
  patterns** — one pattern, swept across its parameter space.
  (Plan-file errata filed on the local plan copy.)

Scene content: one standing male (cropped by the frame at
mid-torso; head never visible), one kneeling female in a dark
two-piece outfit, hair in a bun, hands planted on the male's
hip/thigh, performing a cyclic oral motion driven along the
pattern line. Black void background; two light-atom icons
(green bulb glyphs) float in the scene. No set, no costume
change, no second shot.

## §2 Loop structure — there is no single loop; there are eight regimes

The pattern runs continuously except for one stop (§3), but
its parameters change under the operator's hand, so the clip
segments into regimes. Boundaries are from the 10 Hz slider
record (`records/slider-fills.json`); periods and amplitudes
are from the template-tracked head position
(`records/segment-periods.json`; amplitude = peak-to-peak head
travel in 480-wide analysis pixels; multiply by 4 for native).

| Seg | t (s) | depth | bias | speed | Cycle period | Head amp |
|-----|-------|-------|------|-------|--------------|----------|
| S1 | 0–11.4 | ~0.52–0.57 | ~0.50 | ~0.20 | — (contains the stop, §3) | 39 px (incl. stop transient) |
| S2 | 12.5–17.7 | ~0.01 | ~0.50 | ~0.20 | 104 f = 1.73 s (ac 0.61) | 16 px |
| S3 | 19.1–25.0 | ~0.90 | ~0.50 | ~0.20 | 107 f = 1.78 s (ac 0.70) | 30 px |
| S4 | 25.8–33.2 | ~0.95 | ~0.00 | ~0.20 | 107 f = 1.78 s (ac 0.74) | 30 px |
| S5 | 34.2–40.8 | ~0.95 | 0.94→0.45 sweep | ~0.20 | 110 f = 1.83 s (ac 0.72) | 32 px |
| S6 | 40.9–58.6 | 0.87→0.32 (stepped) | ~0.50 | ~0.03 | 150 f = 2.50 s (ac 0.74) | 45 px* |
| S7 | 58.7–65.3 | ~0.36 | ~0.50 | ~0.18 | 105 f = 1.75 s (ac 0.72) | 28 px |
| S8 | 65.4–82.7 | 0.17→0.74 at 71.6 | ~0.50 | ~0.65 | 63 f = 1.05 s (ac 0.86) | 37 px |

*S6 amplitude is a max-min over a 17.7 s window in which depth
itself was stepped down; read it as an upper bound, not a
steady-state amplitude.

Parameter events (all from the slider record, spot-verified
against native frames):

- **11.5–12.5 s** — depth dragged ~0.52 → ~0.01. Head travel
  collapses to the smallest measured amplitude (16 px) while
  the cycle period barely moves (104 f vs 107 f): **depth
  scales travel, not rate.**
- **17.8–19.1 s** — depth dragged back up to ~0.90.
- **25.1–25.7 s** — bias dragged ~0.50 → ~0.00 (cursor on the
  bias slider in f1548, t=25.8). Period and amplitude do not
  measurably change (S4 = S3: 107 f, 30 px): within this
  tracker's resolution (±3 f, ±2 px), **bias changes neither
  rate nor travel** — what it changes is not visible in head
  position alone (dwell/phase shape is the plausible seat;
  recorded UNATTRIBUTED, §4).
- **33.3–34.2 s** — bias dragged up to ~0.94, then stepped
  down to ~0.45 by 46.9 s.
- **40.9 s** — speed dragged ~0.20 → ~0.03 (visually empty
  slider at t=50, grid_051). The pattern does **not** stop:
  period lengthens only to 150 f (2.50 s). Speed's zero is
  not zero rate — the slider's floor maps to a slow cycle.
- **65.4 s** — speed dragged up to ~0.65–0.70. Period shortens
  to 63 f (1.05 s) — the fastest cycling in the clip, and the
  highest sustained motion energy (per-second adjacent MAD
  0.46–0.51 for t=72–82 vs the clip median 0.309).
- **71.6 s** — depth stepped 0.17 → 0.74 for the final regime.

Speed↔period mapping as measured (three points, no law
claimed): fill ~0.03 → 2.50 s; ~0.20 → 1.75–1.83 s;
~0.65 → 1.05 s.

**What repeats exactly vs what varies** (cycle-corresponding
frame pairs at the segment period vs off-cycle control lag
+17 f; `records/cycle-variation.json`):

- Background/UI field: cycle MAD 0.007–0.009, **100% of pairs
  below 0.1** — repeats at encoder-noise level (see §5,
  camera).
- Moving regions: **zero of the cycle-corresponding pairs in
  S3, S4, or S8 are near-identical** (fraction with MAD < 0.1
  = 0.0 in head, body, and full-frame regions; best pair in
  the head ROI is MAD 1.52). Corresponding frames are
  2.3–2.6× closer than control-lag frames (head ROI cycle MAD
  8.87–9.72 vs control 20.37–25.01), so the cycle is real and
  phase-stable — but no two cycles are pixel-equal. The
  variation is continuous (physics follow + a real-time
  pattern clock that is not frame-locked to the 60 fps
  capture), not a cycle-to-cycle re-roll.
- The clip has **no edit points**: maximum adjacent-frame MAD
  in the whole file is 1.48 (f1958, mid-cycle) — two orders
  below any cut signature. One continuous capture.

## §3 The stop (the clip's only hard seam)

- Adjacent MAD falls below 0.05 from **f213 (3.55 s)** and
  stays at ~0.01 per-second means through t=6 s; motion
  resumes across **f421–446 (7.02–7.43 s)**. Total frozen
  span ≈ **3.9 s**, head held at the pattern's back extreme
  (template track pinned at tx=289, peak-to-peak 0 px for
  t=3–6 s; the button reads "play" in grid_005).
- The freeze is broken every ~30 frames by a single-frame
  MAD blip above 0.05 — consistent with cursor/UI highlight
  updates over an otherwise frozen scene; the scene content
  itself does not move (template score constant 0.833–0.836
  across the span).
- The operator's cursor hovers the stop button again at
  t≈35 s (grid_036) but the pattern never stops a second
  time (no further frozen run ≥20 frames exists in the
  file).

## §4 Contact & physics — attribution table

Each visible behaviour, attributed to a VaM system or to
authored/procedural motion, with the evidence. Anything the
evidence cannot carry is UNATTRIBUTED, per the gate.

| # | Behaviour (timestamps) | Attribution | Evidence |
|---|------------------------|-------------|----------|
| B1 | Head target oscillates along a fixed horizontal line between magenta waypoints; gear target marker travels the line (all running segments) | **Procedural pattern driver** (the floating panel's pattern; panel family = vamX 1.29 per the UI bar) — authored motion, not a solver | Waypoints, path line, and target marker are drawn in-scene in every frame; travel/rate follow the depth/speed sliders (§2) |
| B2 | The head **lags** its target: in many frames the gear sits well ahead of the head on the line (e.g. t=50: gear ≈ x1185 native, head centre ≈ x1010); at extremes they coincide (f1548) | **VaM control-follow physics** — the head control is driven toward the target, not teleported to it | Targeted frames f1548/f1939 vs grid_051; the lag is position-dependent (zero at extremes, max mid-travel) |
| B3 | Hands stay planted on the male's hip/thigh at both cycle extremes while head+torso translate ~120 native px | **IK / control solving** (VaM person controls) — solver-side | f1548 vs f1939: hand positions on the body are unchanged; arm bend absorbs the travel |
| B4 | Spine/neck bend redistributes the translation; torso lean differs between extremes; head angle stays plausible throughout | **Joint-chain solving**; joint *limits* specifically: UNATTRIBUTED (consistent with limits, but no limit is ever hit visibly) | f1548/f1939 comparison |
| B5 | At the forward extreme the mouth meets the body with no visible interpenetration in any sampled frame (83 grid stills at 1 s spacing + 5 targeted frames, all segments) | **PARTIAL — collision/contact vs path placement**: the pattern path was placed so contact occurs; no solver push-out event is ever visible to separate the two | Absence of penetration across 83 grid + 5 targeted frames; no corrective motion observed |
| B6 | Hair (bun) moves rigidly with the head; no strand sway, no settle after extremes | **Hair solver NOT exercised** — nothing to attribute | Grid/targeted frames; bun silhouette is head-locked at both extremes |
| B7 | No visible independent soft-tissue motion (she is clothed; chest/abdomen show no jiggle separable from torso motion at this framing) | **Soft-body NOT visibly exercised** | Grid frames across all regimes |
| B8 | Male figure: no motion in any segment (adjacent MAD in his region: median 0.233 vs full-frame 0.309; residual is her planted hands crossing the region edge) | **Static posed atom** — the test isolates one driven control | `records/cycle-variation.json` stillness lines |
| B9 | Cycle-to-cycle micro-variation in all moving regions (§2: zero pixel-equal pairs) | **Solver-side non-repeatability** (control-follow physics integrated in real time, pattern clock not frame-locked to capture) | cycle-variation.json |

Net: the solvers that visibly work are the **control-follow
and IK/joint chain** — the layers between the pattern target
and the body. The systems the plan expected to star (hair,
soft-body, collision) are either absent or inseparable from
authoring in this footage.

## §5 Camera

- **Static.** The capture is a fixed editor viewport: the
  bottom-right background region is pixel-identical to frame 0
  at every 600-frame checkpoint (MAD 0.000;
  `records/ui-static.json`); top-right background MAD
  0.010–0.014 (encoder noise floor). The bottom UI bar differs
  only in its status-text line (MAD 0.87–2.70 — text changes
  and cursor passes, not camera motion).
- Framing: the male is cropped at mid-torso by the top edge,
  the female full-length kneeling at right-of-centre, the
  pattern panel upper-right, the path line across the middle.
  What it proves: the framing is chosen to keep **the panel,
  the path, and the contact point in one view** — it is a
  test-bench framing, not a presentation framing. Nothing in
  82.7 s moves it.

## §6 Performance beats

There is no acted performance to read in the usual sense —
the "performance" is the operator's test protocol, and its
beats are the parameter events of §2: the stop-and-hold
(3.55–7.43 s, the clip's only full accent — a 3.9 s freeze at
the back extreme), the depth collapse and restore
(11.5–19.1 s), the bias sweep (25.1–34.2 s, both ends of the
slider), the speed floor test (40.9 s), and the fast finish
(65.4–82.7 s at 1.05 s/cycle, the highest motion energy in
the file). Inside the pattern itself, the only readable
accent is the forward extreme: contact is reached once per
cycle and the head's dwell there is the cycle's visual beat
(dwell shape vs the bias slider: UNATTRIBUTED, §4-B5/bias
note in §2).

Head/hands/timing, as tasked: head — the sole driven element,
travel 16–45 analysis px by regime (§2); hands — planted and
static, they are the IK anchor that makes the head's travel
readable (B3); timing accents — the stop, and the final
regime's rate change.

## §7 SHOULD-BE-SEEN score (pre-written in the plan)

> "A tight looped VaM scene: performance captured or keyed in
> VaM's timeline, physics-driven contact and soft-body
> behaviour doing the work that keyframes do elsewhere, one
> camera, no edit points."

| Item | Score | Basis |
|------|-------|-------|
| Tight looped VaM scene | **PARTIAL** | A tight loop exists (1.05–2.50 s by regime), but it is a driven pattern inside an editor capture, not a finished scene (§1) |
| Performance captured or keyed in VaM's timeline | **NOT SEEN** | No timeline anywhere; the motion is a procedural pattern + live slider input (§1, §2) |
| Physics-driven contact doing keyframes' work | **PARTIAL** | Control-follow + IK visibly do the in-between work (B2–B4); contact itself is PARTIAL-attributed (B5) |
| Soft-body behaviour doing keyframes' work | **NOT SEEN** | No soft-body behaviour is visibly exercised (B7) |
| One camera | **SEEN** | Static viewport, MAD 0.000–0.014 vs frame 0 (§5) |
| No edit points | **SEEN** | Max adjacent MAD 1.48 in 4,962 pairs; one continuous capture (§2) |

**Score: 2 SEEN / 2 PARTIAL / 2 NOT SEEN** (looped scene
PARTIAL, timeline performance NOT SEEN, physics-contact
PARTIAL, soft-body NOT SEEN, camera SEEN, edit points SEEN).

## §8 Surprises against the intake (for the errata)

1. The file is an **editor screen capture**, not a scene
   render — the UI, the pattern path, and the operator's
   cursor are the content as much as the figures are.
2. The title is literal: a **pattern test** — one pattern
   swept across depth/bias/speed with a stop/play — closer
   to the QA reading the intake rejected than to the
   "performance clip" it settled on, though it teaches
   nothing in words (no narration, no description, no audio
   stream at all).
3. The expected solver stars (hair, soft-body) never appear;
   the working solvers are control-follow and IK.
