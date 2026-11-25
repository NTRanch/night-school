# Plan 42 — Pass 2 Technique Sheet (Distillation)

Source: Cynological, "How to Import, Animate, and Render Genshin Impact
Models in Blender (2026 UPDATED!) | Tutorial #1" (YouTube b2ITmmWXMBc,
14:39), with the superseded 2024 version (a12ebfnm3oI, 5:44) as companion.
Study run: 2026-11-24, fathom route. **Confidence: PARTIAL** — both
transcripts void (music bed; see the plan's intake notes); techniques
taken from the creator's burned-in captions + frame study. Timestamps
are approximate (frame-based). Blender 3.6.23, Character Setup Wizard
v2.7.3 (2024: 3.6.17 / v2.6.3). Estate pin is Blender 5.3 — mechanisms
are re-verified on the pinned build before becoming checklist items.

## 2026 update

- **T1 — Staged one-click character setup (≈01:00–03:00).** Install the
  addon as a zip, never unzipped; it appears as an N-panel sidebar tab.
  Global settings first: Cache ✓, BetterFBX ✓, Rigging Enabled ✓. Then
  run the stages in order: **Set Up Character → Set Up Materials → Set
  Up Outlines → Finish Setup → Rig Character**. The wizard creates two
  helper objects, **Head Origin** and **Light Direction** — the shader's
  light response is sampled relative to the head, not the world. The
  flat, untextured look after Set Up Materials is a normal mid-state,
  not an error. Why it works: the shader stack is assembled in
  dependency order (geometry/materials before outlines before rig), so
  each stage consumes a complete previous stage.
  → **Adapt (corroboration).** Character → materials → outlines → rig is
  the estate's own rung order. Head-relative light direction is
  literally the FaceSDF sampling basis — the reference ecosystem
  confirms the design. The wizard itself is **Rejected** (see Conflicts).
- **T2 — Rigify fitted to the imported skeleton (≈03:00).** Rig
  Character generates a Rigify control rig fitted onto the model's own
  imported bones — the game skeleton is kept, the control layer is
  generated.
  → **Adapt (corroboration, reference intake only).** Prima's skeleton
  is authored (R1 census, 72-bone fleet standard) — never
  Rigify-generated.
- **T3 — Rest pose pinned by keyframe (≈05:00).** Before posing: select
  the rig, Insert Keyframe → **Whole Character** at frame 1. The rest
  pose becomes a keyed pose, so every later edit has a defined home to
  return to.
  → **Adopt** as scene-authoring discipline: every scene spec's frame 0
  carries the full rest pose.
- **T4 — Blink from the model's own shape keys (≈06:30–08:00).** Facial
  keys ship with the model (e.g. Eye_WinkC_R). Blink = open value keyed
  at both ends of the range, closed value keyed at the **exact middle
  frame** (frame 20 of 1–40): a symmetric open→closed→open envelope, no
  in-between keys.
  → **Adopt** the envelope rule for blink curves: open at both ends,
  closed at the exact middle, no in-betweens. Applies to Prima's blink
  keys and to scene-spec blink authoring (face kit).
- **T5 — Hair posed in chain runs (≈08:30).** Shift-click successive
  bones up a hair chain to select the run, then rotate the run together
  instead of bone-by-bone.
  → **Reject — not applicable.** Operator ergonomics; estate keys are
  authored by script (D-1397).
- **T6 — Damped Track follow-through on hair (≈09:30–10:30).** Each
  hair bone gets a **Damped Track** constraint targeting the next bone
  in the chain, Track Axis **Y**, Influence **0.700**. The chain lags
  the head's motion with smooth damping — sway and follow-through with
  zero per-bone keyframing. Why: damped tracking is a first-order lag
  filter; 0.7 influence keeps the chain attached to the pose while
  letting it trail.
  → **Adapt — preview mechanism only.** Constraint lag inside Blender
  while tuning spring feel. Do **not** ship it: the R5 contract is
  springs; constraints do not survive VRM export parity (R7/R8). The
  0.700 influence is a useful starting feel-target for the spring
  damping ratio.
- **T7 — Camera framed by eye (≈10:30).** Toggle Camera View, move the
  camera until the character fills the frame; framing is judged in the
  render view, not the viewport.
  → **Reject — not applicable.** Scene specs carry cameras
  deterministically.
- **T8 — EEVEE finishing settings (≈11:30–14:39).** Bloom: threshold
  **0.597**, knee **0.500**, radius **6.500**, intensity **0.064**.
  Motion Blur shutter **0.50** (the default, deliberately kept). Render
  samples **64** (viewport 16). 30 fps; output via Render → Render
  Animation (FFmpeg).
  → **Reject — not applicable to the build** (the creator's taste, EEVEE
  pipeline). Verdict packs are judged in the estate toon stack.

## 2024 version — SUPERSEDED (unique deltas only)

Superseded by the 2026 update wherever they overlap.

- **T1 — Scene prep: a dedicated camera collection (≈00:00).** The
  camera gets its own collection before setup begins — scene hygiene
  that keeps wizard-generated objects separate from framing objects.
- **T2 — Outlines as a shared appended asset (≈01:00).** Outlines come
  from appending a shared **"Genshin Impact Outlines v3.blend"** — one
  outlines file reused across every character. (The 2026 version folds
  this into the wizard.)
  → **Adapt (corroboration).** Outlines are per-build infrastructure
  reused across characters — the estate's A4 outline system already
  works this way (R6).
- **T3 — Driver control boards on the rig (≈02:00).** The Festivity rig
  exposes its material controls as in-viewport panels riding with the
  armature: a **Lighting** board (Fresnel, Ambient, Soft Lit, Sharp
  Shadow, Rim X / Rim Y colour wheels) and **Brows / Eyes / Mouth**
  slider boards — shading and face state are posed from driver panels,
  not the node editor.
  → **Noted, not adopted.** The reference ecosystem exposes face/shading
  state as driver panels; the estate's surface is shape keys + bones +
  the verdict panel. A driver-board test rig is an optional ergonomics
  idea for R6 bring-up, not a mechanism.
- **T4 — Sparse-key posing (≈03:00–04:30).** Poses are set at isolated
  keys (frames 20 and 60) and interpolation carries the motion; posing
  is done on the control rig (Pose → Transform/Rotate), never on the
  deform bones.
  → **Noted.** The scene-spec compiler owns timing; sparse keys +
  interpolation is its default shape already.
- **T5 — Direct FFmpeg output (≈05:00).** 30 fps, FFmpeg video muxed
  straight out of Blender.

## Conflicts — flagged, not silently adopted

- **The one-click wizard + Festivity shader stack.** Adopting the
  shader itself would replace the estate's A3 contract and R6 stack
  with a third-party node network, and a GUI one-click setup is not a
  deterministic authoring script (D-1397). Mechanisms adopted (stage
  order, head/light helper objects, blink envelope); the tool and its
  shader are **Rejected**.
- **Damped Track hair (T6)** is a Blender-side preview only. Shipping
  it would put constraint-driven hair in the rig, which the R5 spring
  contract and R7/R8 VRM parity forbid.
- **Version drift.** The videos run Blender 3.6.x; the estate pins
  Blender 5.3 (official build for IK-carrying files, per the two-build
  rule). UI paths in the videos do not transfer verbatim.
