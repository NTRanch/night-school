# PASS 4 — Application and gate: Plan 28 (Headhack Models)

## Expected-vs-seen benchmark (written from the plan's gate)

SHOULD-BE-SEEN at the gate: (1) both joins built on the same
donor pair; (2) both bend-tested identically, with frames;
(3) the estate practice either CONFIRMED or AMENDED with the
reason written; (4) if their method wins a failure class, it is
stated plainly.

## Gate items (agent reads; the Owner's eye is the verdict of record)

| # | Item | Agent read | Evidence |
|---|------|-----------|----------|
| 1 | Both joins built on one pair (Alma head → Prima body) | **PASS** | `rebuild/headhack_both.blend`; build_record: rings 24 = 24, A snap max 5.121 mm, B scale 0.9145/0.9106 + snap 0.447 mm |
| 2 | Bend test, identical poses, achieved angles measured | **PASS** | flexion 45.0°, extension 30.0°, yaw 50.0°, lateral 27.0°; `measures.json` |
| 3 | Seam evidence per pose (gap/strain, tear proxy, shading) | **PASS** | PASS3 table: weld strain, corridor kink, normal-step per pose; 20 renders |
| 4 | Determinism | **PASS** | Two independent processes: measures + build record identical |
| 5 | Estate practice confirmed or amended with reason | **AMENDED (proposal)** | Below — core confirmed, three amendments proposed with reasons |
| 6 | Their win stated plainly | **PASS** | Identity/proportions class: theirs wins (C-12, TECHNIQUE scoreboard) |

**Gate read: PASS** — both joins bend-tested with frames, and
the estate practice is confirmed in its core and amended in
three named particulars (proposals below; the skill is NOT
edited by this run).

## Verdict on the estate practice

**CONFIRMED in its core.** The reconstruction at the heart of
`local-headhack-modelled-heads` — donor head, armature fusion
as the core step, a dedicated face/jaw/eye fix pass as the
deliverable — is the source tutorial's actual procedure,
verified operation by operation against the source itself
(OBSERVATION). The estate's fleet form of the seam (welded ring
+ template weight field) beats the source's hand method on
every bend measure taken (weld strain ~88× lower at flexion;
kink smaller and at the weld rather than above it; shading
normal-step excursion 8–11° vs 36–39°).

**AMENDED — three proposals (for the Owner/Pax to land; this
run does not edit the skill):**

1. **Re-found §5 (the honesty marker).** The skill marks
   separation/fitting/weighting as "NOT evidenced… awaiting
   HEADHACK-METHOD.md". They are now evidenced by the D-609
   source itself (this video): fitting = snap-to-active ring
   correspondence after a ring-parity check; separation =
   delete-above-a-ring with the donor neck left long; weighting
   = group renaming onto body bones + repeated smoothing +
   low-weight hand touch-ups modelled on the body's own
   painting. *Reason: the evidence the skill was waiting for
   exists and has now been read; leaving §5 as "not evidenced"
   would be a stale claim.*
2. **Add the stray-bone sweep to the fusion step.** After any
   armature fusion (add-on or manual), enumerate bones whose
   names belong to the donor rig but drive no graft vertices —
   the source's own final failure was one leftover donor torso
   bone (`joint_torso_C_01`) destroying neck deformation.
   *Reason: a named, observed failure class with a cheap
   deterministic check; the skill's step 3 currently has no
   post-fusion audit.*
3. **Add the correspondence choice, priced.** For foreign
   donors, ring correspondence can be had two ways: global
   scale (estate default; head resized −8.6%/−8.9% here) or
   snap-to-active (donor proportions exact; weld strain 88×,
   kink concentrated above the weld). The skill should name
   the choice and its price so it is made per graft, not by
   habit — snap correspondence is the right call when the
   donor head's identity *is* the product. *Reason: measured
   trade, currently invisible in the skill.* (Companion
   checklist items from the same source: UV-map names must
   match before an object join, C-04; a pose-check crease hunt
   belongs in the fix pass, C-08.)

## Application

- **NSFW application (per plan):** model fleet production —
  the Torogao/Strobe rosters. The fleet's welded, template-field
  construction is confirmed as the right default for
  own-character production; the priced snap alternative and the
  stray-bone sweep are the transferable gains for any future
  foreign-donor graft (e.g. a studied game head under the
  fathom/headhack lane).
- **SFW translation (per plan): identical** — headhacking is
  general model surgery; the same comparison, measures, and
  amendments apply to SFW fleets unchanged. The crossing is
  named here per protocol: the study source sits in the NSFW
  lane; the technique content is lane-neutral, and the bloch
  candidate carries ntranch/nsfw labels per the brief (the
  run's subject is the estate's adult-lane character work).

## Eye items queued for the Owner (pose frames, from `rebuild/renders/`)

- **Q-1 (flexion, side) — the notch.** `A_flexion_side.png` vs
  `B_flexion_side.png`: A's back-of-neck shows a visible
  notch/step where B's curve is continuous. Agent read: A's
  seam fails the eye at 45° flexion; B's passes with a hairline.
- **Q-2 (flexion, front) — the collar.** `A_flexion_front.png`:
  collar step + throat crease; `B_flexion_front.png`: soft
  hairline only. Confirm the agent read that B's remaining line
  is acceptable at production distance or whether the weld ring
  needs a normal-blend band in the builder.
- **Q-3 (identity) — head size.** A keeps Alma's head at donor
  size (reads slightly large on Prima's body in
  `A_rest_front.png`); B's is 8.6% smaller and reads
  proportionate. This is the C-12 trade in one frame: rule
  whether "proportionate" or "donor-exact" is the fleet's
  standing preference for foreign grafts.
- **Q-4 (extension, front).** `A_extension_front.png` /
  `B_extension_front.png` — the normal-step numbers (36° vs
  9°) say A shades worse; confirm by eye whether it reads as a
  seam or as neck anatomy at this stylisation level.

## Residuals

- Transcripts: two windows transcribed (join + weights/fusion,
  base.en). The sourcing/shader window (0:00–30:00) and the
  Photoshop window (55:00–90:00) are grid-read only; a full
  large-v3-turbo transcript remains queued behind sibling jobs
  on primo and is NOT required by any claim above (every
  seam claim rests on a transcribed window or a native frame).
- Their hand touch-up weight painting (C-08's second half) is
  unscriptable by design; Method A omits it and the omission is
  recorded wherever A's numbers are used. It can only narrow,
  not widen, A's measured deficit — their own pose check still
  ended at "good enough" with a visible crease noted.
- Method A's Merge-by-Distance used the Blender default
  0.001 m (their operator distance is never stated on screen —
  UNREADABLE item, OBSERVATION); at the estate's 0.0001 m A's
  weld would remove 148 verts instead of 189, with no expected
  change to the seam measures (the extra 41 are interior
  construction pairs).

## Landing (2026-11-08, per D-1088 repair)

LANDED into `local-headhack-modelled-heads`: (1) the evidenced
seam method written as `references/HEADHACK-METHOD.md` in the
skill (from this plan's TECHNIQUE/OBSERVATION, C-01…C-12);
(2) SKILL.md §5 re-founded on that evidence (the "awaiting
HEADHACK-METHOD.md" marker superseded); (3) the stray-bone sweep
(C-10) added to step 3, with the UV-name join precondition (C-04);
(4) the priced correspondence choice (scale vs snap-to-active)
named in the skill; (5) the pose-check crease hunt (C-08) added
to the step-4 fix pass. Verified from the target side: SKILL.md
grep `stray` 0 → present; `HEADHACK-METHOD` references present;
references/HEADHACK-METHOD.md on disk (6,570 B).
