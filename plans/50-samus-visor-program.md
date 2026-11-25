# Plan 50 — Samus Visor Program (5722675)

- **Source:** https://rule34video.com/video/5722675/
- **Video ID:** 5722675 · **Creator:** NopeNotMeNo / nopenotmeno · **Duration:** 0:24
- **Lane:** NSFW-primary / SFW translation: the two-layer text-display mechanism is register-free and named as such in the technique sheet
- **Estate targets:** Prima's display programme (mb-02-class), the shared `iris_state` machine, Torogao scene-spec authoring — third shelf, the favourites performance studies
- **Status:** PLANNED
- **Status after run:** EXECUTED through Pass 2 on 2026-11-24 (favourites follow-on wave; dossier of record in the extraction audit) — Passes 3–4 open; the display state machine and occlusion-reveal transition landed as Prima programme inputs

## Why this video

Twenty-four seconds that contribute the set's first **device-side**
signifier: the induction state is carried not by the eyes but by a
worn display running a two-layer text programme (a legible primary
word at 1–3 s holds over a subliminal ghost layer crossfading beneath
it), plus a HUD state meter with a telegraphed 1 Hz countdown. It
also supplies the third eye-transition type for the shared state
machine — **occlusion-reveal**: the panel covers the face for the
entire transition and the reveal is the proof. And its camera grammar
maps one-to-one onto the camera set Prima's programme already
carries, including a fourth position the set hadn't named: the
camera inside the display.

## Intake notes (2026-11-24)

Fail-closed screen PASS on coding (Samus Aran / Zero Suit Samus,
canonically an adult; no death/gore/snuff tags, full arc in scope).
Silent file (no audio stream). Method: ffprobe census, contact
sheets at 1 s and 0.5 s, a 0.25 s fine strip over the onset, 15
full-resolution beat frames. Reference only (Tier A).

## SHOULD-BE-SEEN (written before viewing)

A segmented montage — not a continuous take — in which a descending
display panel performs the induction in public: command cards against
compliance close-ups, the state change hidden behind the panel, and
a surveillance-style finale where a numeric counter, not the body,
carries the escalation read.

## Timed observation focus

- Panel behaviour: descent timing, vocabulary shift (imperatives →
  state words), emissive level as content vs as furniture.
- Text layers: primary hold durations; ghost crossfade timing.
- The reveal: eye parameters before vs after the occlusion.
- The counter: values against time; the countdown's placement.
- Camera classes and what each is *for*.

## Distillation targets

1. **Display state machine** — spiral carrier, primary holds, ghost
   layer, the command → label → praise → state assertion →
   instruction sequence shape. Question: spec-able as-is?
2. **Occlusion-reveal** — Question: a third transition type for the
   shared `iris_state` machine, beside ramp and consolidation?
3. **Glyph contact markers** — emissive markers bound to active
   hand targets. Question: a staging device, or this fiction's
   furniture?
4. **The counter and countdown** — a visible state value; a peak
   converted from event to appointment. Question: which parts are
   mechanism and which are the operator register that must not
   transfer?

Findings: `results/plan-50-samus-visor-program/TECHNIQUE.md`.

## Clean-room rebuild spec

Pass 3 (open): the display programme is authored in Prima's mb-02
display layer — two text channels at two opacities, hold timings
and sequence shape preserved, vocabulary re-authored in her voice —
and occlusion-reveal added to the `iris_state` transition set,
exercised in a scene spec.

## Application

- **NSFW application:** Prima's display programme and corruption-sim
  scene grammar; the self-rewatch conditioning loop's staging.
- **SFW translation:** the two-layer display mechanism itself is a
  general presentation device; its vocabulary here is not.

## Gate

Pass 4 (open) is discharged in the Prima programme's verdict packs:
the state readable off the display and the reveal without any
operator fiction, the countdown authored as anticipation in her
register, and no clinical telemetry voice anywhere in frame.

## Deliverables

- `results/plan-50-samus-visor-program/` — technique sheet (landed 2026-11-24), rebuild record and gate result when Passes 3–4 run.
