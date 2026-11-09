# Plan 36 — Intake (Pass 0, written BEFORE viewing)

Plan: `repo/plans/36-dildo-drone-daz.md` — "How to Use Dildo
Drone Asset for Daz Studio", rule34video video 3352555.
Lane: NSFW-primary (device prop) / SFW translation:
articulated prop rigging and interaction registration.

## Source as stated by the plan (NOT yet verified firsthand)

- URL (plan): https://rule34video.com/video/3352555/how-to-use-dildo-drone-asset-for-daz-studio/
- Video ID (plan): 3352555 · Title (plan): "How to Use Dildo Drone Asset for Daz Studio"
- Duration (plan): 4:26 (266 s) — **plan-stated only at intake.
  Corpus durations are unreliable; verification requires the
  captured file / watch page (see MANIFEST.md).**
- Creator (plan): "(category listing shows none — record at
  intake)" — to be recorded from the watch page if it exists.
- Licence: to be recorded AS SEEN from the watch page. No
  licence is assumed at intake.

## SHOULD-BE-SEEN (from the plan file, written before viewing)

> "An asset walkthrough: the drone prop's controls,
> articulation, and how it is positioned and kept registered
> against a character."

The plan's own instruction governs this run: strip the
subject to the mechanics. This is a prop-integration study —
an articulated DAZ asset's control surface, its registration
method against a character, and how a floating prop is made
to read as supported by its fiction. The subject of the
source asset does not transfer; the mechanics do.

## Pre-viewing claims to test (P0 hypotheses)

These are the claims Pass 1 must confirm, refute, or mark
UNREADABLE. None is asserted as fact at intake.

### (a) The asset's control surface (morphs / bones / pose controls)

- **H-a1:** The asset exposes a named control surface in DAZ
  Studio (Parameters / Pose Controls / Shaping panes):
  expect some combination of pose-control sliders, morph
  dials, and a bone hierarchy (rotors / arms / body joints).
  Pass 1 must INVENTORY every exposed control that is legible
  on screen — name + class (morph / bone rotation / pose
  control / transform) — and count UNREADABLE entries rather
  than guessing them.
- **H-a2:** The control surface is animator-facing (sliders
  and bone selection in the viewport), not script-only. If
  the video shows only transforms on a root node, that is
  itself the finding (a thin control surface).
- **H-a3:** Rotor / flight articulation, if present, is
  exposed as continuous controls (spin / tilt), not only as
  static poses. Pass 1 records which, with timestamps.

### (b) The registration method (parenting / constraints / hand-keyed offsets)

- **H-b1:** Registration of the prop against the character
  is by one named mechanism per step — DAZ parenting
  (prop parented to a body node), a DAZ constraint / "Point
  At" / follow behaviour, or hand-keyed transform offsets
  per pose. Pass 1 must name the mechanism PER STEP in
  order, not summarise it as "positioned".
- **H-b2:** The registration is TERMINAL in the working
  order (Plan 34 precedent: the prop is moved to the body
  LAST, after the multi-angle read). Hypothesis: the body is
  posed first and the prop is fitted to the finished body.
  Pass 1 tests the actual order.
- **H-b3:** No live constraint solves drift in the DAZ form;
  if the method is hand-keyed offsets, drift under body
  motion is expected to be non-zero and the rebuild must
  measure the translated method honestly against the
  Plan 01/15 discipline classes (see below).

### (c) Hover / flight presentation — how support is faked or justified

- **H-c1:** A floating prop needs a support fiction. Candidate
  devices to look for: (i) camera framing that never shows
  the unsupported gap, (ii) continuous small motion (bob /
  rotor blur / vibration) that sells thrust, (iii) a cast
  shadow or contact shadow that grounds it, (iv) an explicit
  in-fiction justification (the "drone" fiction itself:
  rotors = lift), or (v) NONE — the prop simply floats and
  the video does not address it. Pass 1 records devices AS
  SEEN, including "none observed" if that is the truth.
- **H-c2:** If rotors exist, their spin state in stills vs
  motion distinguishes a modelled rotor from a blurred disc /
  texture trick. Pass 1 notes which.

## Registration-discipline precedents this run is judged against

- **Plan 01 (keyed-lock reference class):** Child Of contact
  lock drift max 0.0001 mm (constraint form); the shipped
  keyed form of the same lock — Hips registration error
  against the frozen offset — **max 0.393 mm, mean 0.087 mm**
  across the loop (pure interpolation residual). Hand solves
  at frame 0 ≤ 0.46 mm. Source: `runs/plan-01/PASS3-REBUILD.md` §2.
- **Plan 15 (constraint record):** Child Of set-inverse
  reproduced by the manual inverse matrix with delta
  **0.000008 mm** (Plan 01 form; Plan 15 head-lock build
  measured the same class: set-inverse delta 0.000008 mm,
  head-lock drift ≤ 0.0001 mm); the POV head motion is
  **authored curves only** — keyed bob layer, no simulation,
  no capture. Source: `runs/plan-15/rebuild/PASS3-REBUILD.md`.
- **Plan 34 (contact-terminal finding):** the prop is moved
  to the body LAST (T10: contact is terminal; broom
  repositioned under the seated figure at t=310, AFTER hands
  begin), after a mid-build multi-angle distance read (T8).
  Source: `runs/plan-34/TECHNIQUE.md` §1.

Pass 2 must state the prop-to-body discipline against these
three: same classes (constraint / keyed / terminal ordering)
or different, with the difference named.

## Licence posture (protocol)

Study only, never redistribute. No video file, transcript,
or frame enters any shipped artifact. What ships is the
distilled technique, re-derived.

## Audio posture

Audio as files only; nothing played aloud (AUDIO SILENCE
RULE). Transcription, if a file is captured, is file
processing only; single-transcriber output is UNCONFIRMED
tier and the SCREEN GOVERNS over narration.
