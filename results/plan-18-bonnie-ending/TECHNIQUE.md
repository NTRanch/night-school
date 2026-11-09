# Plan 18 — Pass 2 Technique Sheet: the ending grammar + estate comparison

Distilled from OBSERVATION.md alone. The plan's distillation
question: *does the ending grammar match the estate's
reaction/apex design, or improve on it anywhere?* The honest
answer has three parts: the grammar this artefact actually
exhibits (§1), the comparison against the estate's built apex
beat (§2), and what is untestable (§3).

## §1 The ending grammar (as exhibited by the artefact)

**Name: TERMINAL-TAKE + FINISHING PASS + CARD HOLD.**

| Phase | Span | Share | What happens |
|---|---|---|---|
| 1. Terminal take | shot-time 0–20.000 s (one clip, no cut) | 100% of the shot | The scene's ending is authored as a single continuous shot, selected and treated as one unit |
| 2. Finishing pass | recording 25–982 s of work over the parked shot | 93.8% of the recording | A craft phase *after* the beat exists: rim/three-point-style lighting by eye (C-2/C-3), volumetric radius work (C-4), camera surveys — authored against a frozen frame-0 tableau, reviewed by scrubbing (C-5) |
| 3. Parked hold | recording 982–1005 s | 2.3% | The finished scene sits as a true freeze (viewport energy 0.0047 — compression-noise class, no breath, no micro-motion) |
| 4. Card hold | recording 1005–1020.07 s | 1.5% | Three sequential credit cards (~5 s / ~4 s / ~6 s) over the blurred frozen frame: thanks → editor credit → links |

Proportions that transfer: the *shot* is a single take; the
*ending as published* is take → freeze → cards, with the
freeze+cards tail at 38 s of recording time against a 20 s
take — the published tail is ~1.9× the take's own length
(counting the parked review; cards alone 15.07 s ≈ 0.75×).

Mechanism, in system terms: the ending's *timing* work and
its *presentation* work are fully separated. The beat is
built first (in earlier series sessions); this session never
re-opens its timing — it spends 100% of its effort on how the
already-timed beat reads (light, atmosphere, camera) and on
the publishing wrapper. The frozen tableau is the working
surface for the whole pass because SFM lighting is evaluated
per-frame, not per-motion.

## §2 Comparison against the estate apex beat (Plan 01, built)

Estate artefact of record: Plan 01's built loop
(`runs/plan-01/PASS3-REBUILD.md`): 78 samples @ 60 Hz (1.30 s),
Contact at sample 38; follower Spine holds 10.0° at Contact,
peaks **14.0° at sample 45 — a +7-sample (+0.117 s) reaction
lag** — then settles; both endpoints are the same mid-recovery
pose (amplitude 0.45 = 0.45, seam pixel-identical); leader
phase: entry pause 0–15, thrust 15–38, long recovery 38–78.
Design context (cited as design, not as a build): the
Crescendo ladders — 12 steps per heroine, peaks at steps
3/6/9/12.

### Matches (2)

- **M-1 — Single continuous take, no internal cut.** The
  estate loop is one 78-sample cycle with no cut; the Bonnie
  ending is one 20.000 s clip with no cut (C-1). Both grammars
  carry the beat on sustained registered contact inside one
  unbroken take rather than on editing.
- **M-2 — Contact-carried beat.** In the estate build the
  beat's carrier is the locked contact (Child Of, drift max
  0.0001 mm) with reaction layered on top. In the Bonnie
  artefact the only pose ever reviewed — across 17 minutes of
  finishing work — is the contact tableau itself; the entire
  finishing pass is spent making that sustained contact read.
  The beat's centre of gravity is the contact in both.

### Differences (4, named)

- **D-1 — Loop vs terminal.** The estate beat is a *cycle*:
  endpoints are rest-equivalent by construction (seam law),
  designed to repeat forever. The Bonnie ending is a
  *terminal* segment: a 20 s take that closes a longer scene
  and is followed by a freeze and credits, not by its own
  first frame. The estate has no terminal grammar in the
  Plan 01 artefact at all — its "ending" is a seam.
- **D-2 — Timescale, 15.4×.** Estate cycle 1.30 s vs source
  take 20.000 s. The estate's build/peak/settle lives *inside*
  one cycle (38/45/78 samples); the source's take is
  scene-length, so its build/peak/settle — whatever they are
  (U-1) — live at scene scale, the scale the Crescendo design
  (12 steps, 4 peaks) also addresses. The built estate beat
  and the source ending operate at different levels of the
  same hierarchy: cycle vs ladder-run.
- **D-3 — The hold.** The estate loop *forbids* a hold: its
  endpoints are mid-recovery (amplitude 0.45, Spine 11.8° at
  both ends) precisely so nothing parks. The source artefact's
  terminal state is the opposite pole: a parked freeze
  (measured 0.0047 residual motion — no breath, no
  micro-motion) extended by credit cards. Whether the *shot's
  own* last seconds hold is UNREADABLE (U-3), but the ending
  *as published* terminates in a still, which the estate's
  seam law would reject inside a loop and has no rule for
  outside one.
- **D-4 — Where the craft effort sits.** Plan 01's record is
  timing-first: keys, phases, lags, cures — presentation
  (lighting) is inherited from the fleet scene. This
  artefact is presentation-first: 93.8% of its length is a
  finishing pass (light/volumetrics/camera, C-2…C-5) over a
  beat whose timing is never re-opened. The estate pipeline
  has no named equivalent phase between "beat built" and
  "scene shipped".

### Untestable (1)

- **X-1 — Reaction lag.** The estate's signature number —
  follower reaction peak +7 samples after Contact (10.0° →
  14.0°) — can be neither matched nor refuted here: the
  source's reaction is never displayed (U-2). Recorded as
  UNTESTABLE-IN-ARTEFACT, not as a match or a difference.
  The same applies, at design level, to the Crescendo peak
  placement (3/6/9/12): nothing in this artefact speaks to
  peak placement inside the take.

## §3 Does it improve on the estate anywhere? (candidate-grade)

Two elements are *absent* from the estate's built grammar and
present here, each a proposal for Plans 19/20, not an adoption
(full candidacy record in PASS4-APPLICATION.md):

1. **The finishing pass as a named phase** (D-4's flip side):
   a dedicated lighting/volumetrics/camera pass over the
   frozen beat, after timing is locked. The estate currently
   folds this into scene setup; the artefact shows it working
   as a separable, reviewable phase with its own failure/fix
   moments (the self-flagged bad rim light, C-3).
2. **The card hold as a publishing ending** (C-6): freeze the
   final frame and run short sequential cards over it. As
   scene craft this is SFW-universal (any scene's published
   ending); as a *beat* it gives a terminal scene an ending
   shape the loop grammar cannot express (D-1/D-3).
