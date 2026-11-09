# Plan 34 — Pass 2 Technique Sheet (Distillation)

Source: `OBSERVATION.md` (Pass 1). Estate context: Blender
5.2.3, Prima's conformed rig (54-bone Mixamo armature),
scripted/headless posing; the source session is DAZ Studio
4.21 on a Genesis 8 Female — every mechanism below is
stated tool-neutrally, with the DAZ form noted.

## 1. The posing-order grammar (their order, T)

Stated as an ordered rule set, distilled from Pose A's
first-touch log (OBSERVATION §2), with B and C as the
conformance tests:

> **T1. Context before bones.** Load/fit outfit and props
> and pin the reference first; place the hero prop roughly
> (broom at the feet) before any bone moves.
> **T2. Legs establish the seat/stance.** Thighs (then
> shins) are the first bones touched — the support chain
> decides where the body is.
> **T3. Pelvis as a block.** The pelvis is set with the leg
> block (here: a stock sitting preset applied to the
> selected pelvis+leg nodes only), not as a root-first
> translation.
> **T4. Spine/chest next** (Chest Upper before Chest
> Lower revisits; torso direction follows the legs).
> **T5. Head/neck after chest** (neck block + head as one
> selection).
> **T6. Feet as their own late pass** (L foot, shin
> correction, R foot) — feet are finished after the head,
> not with the legs.
> **T7. Arms after feet** (collar+shoulder block, both
> sides together).
> **T8. READ AT DISTANCE before hands.** Create/apply
> cameras; read the full pose from front, side, and top;
> keep an auxiliary full view open during close work.
> **T9. Hands/fingers next-to-last**, worked as a chain
> (collar→shoulder→forearm→hand→fingers when captured or
> applied), via a hand-specific control view.
> **T10. Contact is terminal.** The prop is moved to meet
> the body (broom repositioned under the seated figure at
> t=310, AFTER hands begin) and every hand/paw is finished
> in close-up against what it touches.

**Conformance (poses following the modal order / total):**

| Unit | Verdict | Why |
|---|---|---|
| A (broom-sit) | Defines the grammar | First-touch log §2 follows T1–T10 in sequence |
| B (re-application) | **Conforming** | Gross order executed by the full preset (order collapsed, not violated); every MANUAL act follows the grammar: partial applied proximal→distal (T9's chain direction), camera preset read before final (T8), broom preset after (T10) |
| C (cat) | **Non-conforming on first-touch order** | Torso/head block (Chest/Neck/Shoulders) touched BEFORE hip/legs — T2/T5 inverted. Conforming on the tail: contact late (paws t=750–770 after gross), secondary (tail) after contact chains, face dead last |

**Score: 2 / 3 conform** (A definitional, B conforming,
C deviating on the head/legs inversion while keeping the
contact-late tail). The deviation is itself informative:
for a small second subject placed ON an existing
composition, the artist anchors the visible torso/head
first and fits the support legs to the prop second — the
grammar's legs-first rule serves the FIGURE THAT CARRIES
THE WEIGHT; the cat's weight is carried by the broom, so
its "support chain" is arguably its placement (T2's
intent) and the inversion is smaller than it looks. The
grammar is recorded as observed, with this note, not
smoothed.

## 2. Revision triggers

Every sampled revisit in the session follows a nameable
check. Taste-only revisits observed: **0** (at sample
resolution; see OBSERVATION §6 for the floor caveat).

| Trigger | Mechanism | Instances (sampled) |
|---|---|---|
| **Contact failure** — a hand/paw/body part does not meet what it must touch | Close-up inspection of the interface; the part (or the prop) is moved until contact reads. Hand↔thigh (n340–360, checked from back AND side), broom↔body (n310–330: prop moved to body, not body to prop), paws↔broom crystal (n760–770), hand↔cat (n820–830) | **4 blocks** (A: 2, C: 2) |
| **Distance read** — the full pose, from a created camera, disagrees with the close-up impression | Camera block T8 (4 cameras, front/side/top reads n220–250) is followed immediately by arm re-work (n260) and the hand phase; in B, camera-preset reads (n590–620) close the build | **2 blocks** (A: 1, B: 1) |
| **New subject** — a new element enters the composition | The cat's arrival sends the artist back to the WITCH's finished hand and re-poses it finger by finger onto the cat (n820–830) | **1 block** (C) |
| **Library verification** — a saved artifact must prove itself | The partial hand preset is applied to a RESET figure via chain selection (n530–580) — a test of the artifact, which re-touches the collar/shoulder chain | **1 block** (B) |

Trigger discipline, distilled: **a chain is revisited when
a CHECK names it** — contact (close), silhouette/distance
(far), composition change (new subject), or artifact test
(library). The artist does not orbit-and-fiddle: between
checks, work moves strictly forward through the grammar.

## 3. Point-by-point vs the estate order

Estate order (INTAKE operationalisation of the
sprite-acting skill; the skill states principles —
primary-first layers — not a chain sequence):
E: Hips/Weight → Spine → Head → Arms → Hands/Contact →
Secondary → Ambient → Verify-at-end.

| Point | Their T | Estate E | Verdict |
|---|---|---|---|
| First chain | **Legs** (support chain) | Hips/weight | **T improves it for seated/prop poses**: the seat exists because thighs bend; hip translation alone cannot make a sit. For standing work the two nearly coincide (thighs ≈ weight). |
| Spine position | After pelvis block (4th) | 2nd | Equivalent in effect (both early); T's pelvis-with-legs block is one gesture, E splits it. |
| Head position | 5th, after chest | 3rd | **E's look-leads-head insight is absent in T** — DAZ posing has no look-target layer; in the estate's 2D/animation work the eye-lead stays. For static pose construction T's later head costs nothing observed. |
| Feet | Own late pass (6th), after head | Inside legs/hips (1st) | **T improves it**: feet finished after the body's mass settles reads as a deliberate rule (both feet + a shin correction in one pass, n170–190). |
| Arms | 7th, after feet | 4th | T later; no cost observed — arms hang off a settled torso. |
| Hands | 9th, after the distance read | 5th (with contact) | **T improves it**: hands are the most contact-dependent chain; doing them after the camera read means they are done once, against the final body. E does contact before any full read. |
| Reading distance | **Mid-build, multi-angle, before hands (T8)** + persistent aux view | Once, at the end (verify step) | **T improves it decisively** — this is the largest single difference. E's end-only verify discovers problems after the most expensive chain (hands) is done. |
| Contact | Terminal step; prop moves to body | Mid-sequence (with hands) | **T improves it** for prop work; the n310 broom move is only possible because the body is final. |
| Secondary/ambient | Tail (cat), face morphs last; no ambient layer in a stills tool | Secondary then ambient, before verify | Tie in spirit: fine/secondary work is last in both. |
| Library capture | **During the session**: full + chain-scoped partials + prop/camera presets, verified by re-application | Not addressed by the skill at all | **T adds a whole mechanism E lacks.** Partial presets (chain-scoped, proximal→distal) are the session's most transferable artifact. |

**Answer to the plan's question:** their order does NOT
match the estate's (weight, spine, head, hands) — it
differs at five points, and on the evidence of this
session it **improves it for static pose construction** at
four of them (legs-first support, feet as a late pass,
hands after the distance read, contact terminal), ties at
two, and loses at one (look-leads-head, an animation
concern the stills context cannot exercise). The
mid-build distance read (T8) and chain-scoped partial
presets (C-34-4) are improvements at any point of
comparison.

- **Adopt:** T8 (mid-build multi-angle read before hands);
  T10 (contact terminal, prop-to-body); partial-preset
  capture as a session step (chain-scoped, verified by
  re-application).
- **Adapt:** T2 (legs/support first) — in estate terms:
  "the chain that carries the weight is posed first"
  (standing: hips+legs together; seated: thighs first;
  second subjects: placement first). T6 (feet late pass)
  folds into the same rule.
- **Reject:** nothing in T is rejected outright; T5's
  head-after-chest is NOT adopted over the estate's
  look-lead for animated work — it is recorded as
  stills-context-neutral.

## 4. Failure modes of the grammar (as observed)

- Preset dependence: A's gross sit arrives via a stock
  preset applied to a node block — the grammar assumes a
  preset/base exists for the gross shape; from-zero posing
  would stretch T2–T3 (unobserved here).
- The distance read costs cameras: four cameras were
  created for one pose (n210–250). In scripted estate
  work the same read is one Workbench render per angle —
  cheaper, but the step must be scheduled, not skipped.
- Contact-terminal means a late prop change invalidates
  finished hands: when the cat arrived, the witch's hand
  had to be redone anyway (C trigger 3) — the grammar
  accepts this cost openly.
