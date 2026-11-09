# Plan 04 — Technique Sheet (Pass 2): MUGEN Stage Layer Grammar + Parallax Calibration

Distilled from OBSERVATION.md (frame-anchored; claims C1–C12).
The source build is Fapmaster/Viket's "Glitter Cookie's Trial"
stream (rule34video 3417736). Nothing here copies his art, text
files, or sprites — the grammar and calibration rules are
re-derived; his .def comment phrasing is quoted in OBSERVATION.md
as evidence only.

## The headline finding

The stream's *doctrine* is a parallax doctrine; the stream's
*practice* is a **compositing doctrine**. The finished stage
carries seven BG elements and **every delta is 1,1**: all depth
is produced by (a) one composited plate, (b) file-order draw
order, (c) per-element scale, and (d) one layerno=1 translucent
foreground copy. Parallax-by-delta is the stated ideal, reserved
for elements that were *authored separately*; anything that can
be baked into the plate is baked. A calibration sheet that only
recorded the doctrine would misdescribe the build.

## 1. Layer grammar — what earns a layer

A scene element earns its own layer **iff it needs a treatment
the plate cannot give it**. Exactly five treatments appear:

| # | Treatment | Mechanism | Source instance |
|---|-----------|-----------|-----------------|
| L-A | **Different motion** | own `delta` (≠ plate) or own `velocity` | doctrine C3/C9; unused for delta in this build, velocity unused (0,0) |
| L-B | **Animation** | `type = anim` + an Action (frame list with per-frame ticks) | stars: 8 frames, 10 ticks each, one 50-tick hold, 120-tick loop |
| L-C | **Draw side of the actors** | `layerno = 1` (in front) vs default 0 (behind) | Cookwitch trans in front; Cookwitch solid behind — *the same sprite, both sides* |
| L-D | **Blend treatment** | `trans = addalpha` + `alpha` | foreground ghost at his recommended **100, 120** |
| L-E | **Coverage by repetition** | `tile = 1,0` (+ `tilespacing`) | the plate and the floor strip tile horizontally so a finite sprite covers any camera travel |

Everything else — skyline, water, railing, billboard, floor —
is **one Photoshop composite** (his working file ran ~16 layers
that ship as one sprite). Grammar rules:

- **G1 (plate rule).** If two elements share motion, draw side,
  blend, and animation state, they are one layer. Compositing is
  the default; separation must be earned by the table above.
- **G2 (order rule, C1).** Draw order = declaration order. The
  first BG element is the furthest back. "Floor at the bottom of
  the file draws above everything; floor at the top sits on the
  background."
- **G3 (anchor rule, C5).** Every element shares one floor
  anchor: `start = x, 620` in his stage (x=0 centred via the
  sprite axis; the stars sit at x=100). When an element's
  `scalestart` changes, its start must be re-derived — the
  anchor is in *scaled* space.
- **G4 (key rule, C4).** `mask = 1` keys the sprite's background
  colour (his Photoshop comps are built on a flat green for
  exactly this). No back element ⇒ black screen — seen live in
  test #1.
- **G5 (template rule).** Start from a commented template
  (.def + .sff with a measured grid sprite), never from blank.
  Sections not understood are left at template defaults and
  *labelled* as not understood (his "[I HAVE NO FUCKING CLUE
  WHAT DOES THIS PART DOES SECTION]" banner over [Reflection])
  rather than silently tuned.
- **G6 (engine-judgement rule, C12).** Correctness is judged
  in-engine (black-sky gaps, mirror seams, floor contact,
  ghost readability), not from files.

**Mapping question — Torogao/Strobe scene composition, or
fighting-game special case?** The grammar maps **one-to-one**
onto the estate's scene composition, because none of its five
treatments is fighting-specific: delta = parallax factor,
layerno = the fore/back split around the actor plane, anim =
ambient element, addalpha = atmosphere overlay, tile = coverage
invariant. What *is* fighting-specific is only the calibration
anchor (the floor the fighters stand on, §2) and the actor
plane's privilege (layerno is defined relative to it). In
Torogao terms: BG elements ↔ scene layers behind the character
plane; layerno=1 elements ↔ foreground dressing in front of it;
the plate rule ↔ the estate's plate-based scene art. **Verdict:
general grammar, fighting-game calibration.**

## 2. Parallax calibration sheet

**How factors are chosen (as evidenced).** By *rule*, not by
formula and not by per-layer eye-tuning:

1. **Pin the floor.** The element the actors stand on gets
   delta **1,1** at low-res scale, **2,2** at high-res scale
   (C2 — the 2,2 is the same physical rule expressed in a
   coordinate space twice as dense; cf. C8's ×2/×0.5 rescale
   rule). Any other floor delta and "the characters will
   appear to slide on the floor". This is the one non-negotiable
   number in the system.
2. **Rank the rest by depth.** "The further the element is in
   the background, the lower its delta must be" (C3). No
   formula is given or used; depth rank is judged from the
   composed image, and delta is assigned monotonically with it.
3. **Or bake it.** If the depth separation can be painted into
   one plate, delta differentiation is skipped entirely — this
   build's actual choice (all 1,1). Calibration effort is spent
   only on elements that earned a layer under §1 L-A.

**Does it survive a different stage width?** Split answer, and
the split is the useful part:

- **Delta itself is width-invariant.** Delta is a ratio of
  layer motion to camera motion; widening the stage changes
  neither the ratio nor the floor rule. The calibration
  *transfers unchanged*.
- **Coverage does not transfer.** What breaks at a new width is
  the sprite, not the factor: his plate had to be
  **mirror-widened 1035→1396 px** when the stage outgrew the
  art, and the grammar's answer is L-E (tile) or mirror-extension,
  both art-side fixes. Likewise `start` anchors are
  scale-relative (G3), so a rescale re-derives them.
- Calibration rule of record: **factors are portable; anchors
  and coverage are per-stage.** A width change re-checks
  coverage and seams (in-engine, G6), never the deltas.

Formal statement of the MUGEN model used in Pass 3: for a
camera at world offset `c`, an element with start `s` and delta
`d` renders at screen position `s − c·d` (per axis), drawn in
declaration order, with layerno=1 elements drawn after the
actor plane. Tile repeats the sprite every `width + tilespacing`
screen px. Animation advances one frame per its tick count at
60 ticks/s, looping; `resetBG` (his: 0) decides whether it
restarts per round.

## 3. Ambient budget — alive vs busy

Evidence: exactly **one** animated background system in the
finished stage — the stars (8 frames × 10 ticks, one frame held
50 ticks, 120-tick = 2.0 s loop), plus two *engine-side* motions
that cost no frames: the floor [Reflection] (intensity 50) and
the [Shadow] system. A second animation (billboard bulbs /
asset frames) passes through Photoshop but no second anim BG
element is read in the final .def (UNREADABLE #5 stands).

The principle as evidenced: **ambient motion is budgeted to one
system, at the furthest layer, at sub-attention timing.** The
twinkle is slow (a 2 s loop whose longest hold is its brightest
beat, 50 ticks), small in screen share, and behind everything;
the fighters' plane and everything near it stays still, so
motion never competes with the action. "Alive" = the furthest
layer breathes; "busy" = anything at the actors' depth moving
without being gameplay. His second available motion channel —
`velocity` + `tile` (scroll without frames, C9) — is the budget
valve: if an element must move, prefer engine motion over frame
animation, and spend frame animation only on the back layer.

## Adopt / Adapt / Reject

**Adopt**
- The five-treatment layer grammar (§1) as the estate's scene
  layer rule, with the plate rule as default.
- Floor-pin calibration (delta 1,1 at scene scale; C2) and
  depth-rank assignment (C3) for estate parallax work.
- The alpha recipe for foreground atmosphere: addalpha at
  100,120 as the starting point (C7), tuned by eye after.
- Template-first authoring with not-understood sections
  labelled, not silently tuned (G5).
- In-engine judgement as the gate (C12/G6): sweeps, not files.

**Adapt**
- MUGEN's file-order draw order → the estate compositor's
  explicit layer list (same semantics, named list instead of
  text position).
- `start`-anchor discipline → a single named floor-anchor
  constant per stage record, from which all layer starts are
  derived (his 620, re-derived on rescale per G3).
- The 8-bit palette/mask-key workflow → alpha-channel layers in
  the estate pipeline (same keying intent, modern encoding).

**Reject**
- Mirror-widening a sourced plate as a coverage strategy for
  estate work: it ships a visible symmetry (seen in his own
  test frames) — the estate tiles or authors wider. (His use is
  rational for a stream-speed build; rejected as estate
  practice, with the evidence being his own FIGHT frame.)
- Copy-paste layer duplication without a liveness check: his
  duplicated `[BG stars]` (normal + actionno) is inert weight
  that survived because nothing validated it. Estate stage
  records validate every layer has a live treatment (§1).
- Leaving malformed values (`xscale = .3.5`) in a shipped
  record because the engine tolerates them: the estate record
  is the spec, and the spec parses strictly.

## Pass 3 test list (claims → rebuild checks)

C1 order, C2 floor pin, C3 delta rank, C6 layerno split,
C7 ghost recipe, C9 tile coverage — exercised and measured in
the rebuild (PASS3-REBUILD.md). C4 (mask/black) is exercised by
construction (alpha layers; a no-back-layer render is produced
as the negative control). C5/C10 anchor/zoffset discipline is
carried into the stage record. C8 is a documentation rule (no
second resolution is built). C11 is the rebuild's own control:
the estate stage uses differentiated deltas per C3 *and* the
record states where his build baked instead. C12 is the Pass 4
gate's method.
