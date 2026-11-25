# Plan 44 — Pass 2 Technique Sheet (Distillation)

Source: tppo, "Why ZZZ's Art Looks So Good… And How to Draw Like
Them!" (YouTube y08Wek1FgOU, 12:59). Study run: 2026-11-24, fathom
route. **Confidence: CONFIRMED** (full transcript; frames
spot-checked). Timestamps from the transcript. Admitted: paint/toon
craft (the 2D side of the R6 problem).

- **T1 — One colouring ladder, three tiers (00:01:00–00:02:00).**
  Mindscape, Splash and Story art are the *same process* at three
  levels: Splash = Mindscape + shadow + rim light; Story = Splash +
  brushwork. Build the simple tier first; each level adds exactly one
  class of thing.
  → **Adapt (corroboration)** of the estate's own structure
  (paint-first base → ramp → SDF): one base, each level adding one
  class of thing. No change.
- **T2 — No soft shadows, anywhere (00:02:32).** ZZZ art uses
  hard-edged shadow shapes exclusively. Soft/blurred shadow was his
  core early mistake — his word for it: blur is "hiding a lack of
  understanding" of the light.
  → **Adopt as a paint rule**: FaceSDF thresholds and painted shadow
  shapes are authored hard-edged; softness in the terminator comes
  from the ramp, never from blurred paint. Speaks directly to the
  hero review's SDF distribution finding — paint the shapes, don't
  gradient them (R6).
- **T3 — Depth from stacked multiply shadows (00:04:00).** Instead of
  gradients, shadow shapes are layered over shadow shapes
  (multiply), above all in hair. Depth is *accumulated shapes*, not
  blended tones.
  → **Adopt as the hair-paint mechanism**: shell-hair depth =
  overlapping painted shadow shapes (the brief's "painted
  separations"), stacked, not blended (R5 atlas paint).
- **T4 — The signature back rim (00:04:07).** Every splash piece
  carries **blue or purple light from behind** the subject. The cool
  back rim is a house signature, not an accident of palette.
  → **Candidate for the R6 lighting pass**: the estate's cubic rim is
  colour-neutral today; a cool (blue/purple) rim tint is the
  reference art's house signature. The Owner's eye decides at the
  full-stack rung (C6).
- **T5 — Expression carries the close-up tier (00:01:45).** Mindscape
  composition is an intimate close-up and the expression is what
  carries the piece — and the element most easily lost while
  polishing everything else.
  → **Adapt (corroboration of priority)**: the face-kit finish items
  (brow arc, mouth taper, double-eyelid keys) are expression
  geometry — highest-value work in the face kit.
- **T6 — Linework that disappears (00:05:30).** At the painterly
  tier, line art is selectively erased and merged into the paint,
  and only a *few* soft edges are introduced. Restraint is the
  technique: painterly ≠ soft everywhere.
  → **Adopt** as a paint-route note: at the finished tier, painted
  lines (brow/lash) partially dissolve into shading instead of
  staying uniform strokes (R6 paint).
- **T7 — Puppet-pin animation of a still (00:07:46–00:08:13).**
  After Effects route: **layer separation first** (the most
  time-consuming step — the illustration must be cut into movable
  layers), puppet pins at the joints, keyframe, then **F9 Easy
  Ease** on the keys to turn linear timing into flow.
  → **Reject — not applicable** (After Effects 2D route). The estate
  analogue — bones + eased curves in scene specs — already exists.
- **T8 — Squash-and-stretch on the eyeball (00:08:41).** On a blink,
  the eyeball itself squishes slightly as the eye closes and
  stretches as it opens — squash & stretch at the smallest possible
  scale.
  → **Candidate finish item** (face kit): a 1–3% eyeball squash at
  the closed frame of the blink (pairs with Plan 42's blink
  envelope). Cheap key addition; the Owner's eye at the full-stack
  rung.
- **T9 — Scripted hair spring (00:09:10).** The **AFP Hair Rig**
  script: place puppet pins along the hair, **delete the keyframes
  on the parts that must stay still**, run the script — instant
  secondary hair motion. Repeat per strand group.
  → **Adapt — concept corroboration only** (pins ≈ chain bones;
  deleting keys on held parts ≈ static root segments). Tool
  **Rejected** (AE script).
- **T10 — The graphic-identity layer (00:05:50–00:06:40).** Each
  piece also gets a design DNA (retro colour scheme, sci-fi themes,
  gothic accessories, bright graphic elements), and the art is
  designed to live a second life as posters, magazines, vinyl,
  stickers — layout pulled from design references.
  → **Reject — not applicable** to the rig programme
  (presentation/merch layer).

## Conflicts — flagged, not silently adopted

- **After Effects routes (T7, T9).** Puppet pins and the AFP script
  live outside the estate pipeline entirely; only their concepts
  (layer separation before animation; scripted secondary hair
  motion) transfer. Neither tool appears in the curriculum as a
  recommendation.
