# Plan 42 — How to Import, Animate, and Render Genshin Impact Models in Blender (2026 UPDATED!) | Tutorial #1

- **Source:** https://www.youtube.com/watch?v=b2ITmmWXMBc
- **Video ID:** b2ITmmWXMBc · **Creator:** Cynological · **Duration:** 14:39
- **Lane:** SFW-primary (YouTube pipeline study) / NSFW application: the Prima canonical-base programme, named per technique in the technique sheet
- **Estate targets:** Prima canonical base (R6 toon stack), face kit, the reference/census pipeline — second shelf, YouTube track
- **Status:** PLANNED
- **Status after run:** EXECUTED through Pass 2 on 2026-11-24 (fathom study run, Owner-supplied set) — Passes 3–4 open; adoptions landed as Prima programme inputs, recorded in the technique sheet
- **Companion (superseded):** the 2024 version of this tutorial — https://www.youtube.com/watch?v=a12ebfnm3oI · Video ID a12ebfnm3oI · Duration 5:44 — is folded into this plan as a superseded companion, not a standalone plan: the 2026 update replaces it wherever they overlap, and its unique deltas are recorded in the technique sheet. One plan, one study object — the current tutorial; the old one is its errata.

## Why this video

The estate's reference ecosystem — the one the ZZZ grammar corpus and the
Prima canonical base are measured against — sets characters up in Blender
through this exact route: a staged wizard, a generated control rig over
the imported game skeleton, blink from the model's own shape keys. The
estate does not adopt the tooling (see the conflicts in the technique
sheet), but the *order of operations* and the helper-object design are
the reference pipeline's own grammar, and Prima's R6 rung order and
FaceSDF sampling basis are either corroborated by it or corrected by it.

## Intake notes (2026-11-24)

Owner-supplied YouTube set, studied by the fathom route (download,
transcribe, frame study, distill). This video's served audio track was
a music bed with no decodable narration (YouTube served only a
`[hi]`-labelled track set via the study egress; slices decoded to loops
under every language setting). The transcript is therefore **void — not
a record** — and the study basis is 59 frames at 15 s intervals plus the
creator's burned-in English captions, which carry the full instruction
text. **Confidence: PARTIAL** (steps reliable — they are the creator's
own captions; no spoken nuance available). The 2024 companion was
studied the same way (23 frames + captions; its "transcript" was music
markers and a whisper hallucination loop, flagged so it is never quoted
as content). Confidence: PARTIAL. Versions on screen: Blender 3.6.23,
Character Setup Wizard v2.7.3 (2024: Blender 3.6.17, wizard v2.6.3) —
the estate pins Blender 5.3 and mmd_tools 4.5.14; UI paths do not
transfer verbatim and every adopted mechanism is re-verified on the
pinned build before it becomes a checklist item.

## SHOULD-BE-SEEN (written before viewing)

A complete beginner route from a raw game-model import to a posed,
blinking, rendered character: staged character setup, materials,
outlines, a generated control rig, and EEVEE finishing settings — with
the numbers shown.

## Timed observation focus

- Wizard stage order and global settings (Cache, BetterFBX, Rigging) —
  what each stage consumes from the previous one.
- The helper objects the wizard creates (Head Origin, Light Direction)
  and what samples against them.
- Rig generation: how the control rig is fitted to the imported
  skeleton; what happens to the game bones.
- Blink construction: which shape keys, where the closed key sits in
  the frame range.
- Hair posing and follow-through: selection method, constraint type,
  axis, influence value.
- Render finishing: bloom, motion blur, samples, frame rate — numerically.

## Distillation targets

1. **Staged setup order** — character → materials → outlines → finish →
   rig. Question: is the order load-bearing (dependency) or cosmetic?
2. **Head-relative light direction** — the shader samples light relative
   to the head, not the world. Question: how does that compare to the
   estate's FaceSDF sampling basis?
3. **Blink envelope** — open at both ends, closed at the exact middle
   frame, no in-betweens. Question: does the symmetric envelope survive
   as a scene-spec authoring rule?
4. **Damped Track hair** — per-bone Damped Track, Y axis, influence
   0.700. Question: preview mechanism or shippable rig content? (The R5
   spring contract answers this — see the technique sheet's conflict.)

Findings: `results/plan-42-genshin-blender-tutorial-cynological/TECHNIQUE.md`
— 8 techniques from the 2026 update, 5 unique deltas from the superseded
2024 version, each marked Adopt / Adapt / Reject with the reason.

## Clean-room rebuild spec

Pass 3 (open): rebuild the *adopted mechanisms only* from the technique
sheet — the blink envelope rule applied to an estate blink key set, and
the staged-setup order checked against the R6 bring-up script's own
stage order. The wizard and its shader stack are **not** rebuilt: a
one-click GUI setup is not a deterministic authoring script (D-1397),
and the Festivity shader would replace the estate's A3 contract.
Damped Track is rebuilt as a Blender-side preview only, never as rig
content.

## Application

- **NSFW application:** the Prima canonical-base programme — blink
  envelope rule to the face kit; stage-order and head-relative-light
  corroboration to R6.
- **SFW translation:** the same mechanisms are lane-neutral Blender
  craft; the blink envelope and setup order apply to any estate
  character work.

## Gate

Pass 4 (open) is discharged by the Prima programme's own rung gates:
the blink envelope is judged in the face-kit's verdict pack at judging
size, expected-vs-seen, and the R6 stage order is checked line-by-line
against the bring-up record. A technique that only works inside the
wizard has not passed — it was never adopted.

## Deliverables

- `results/plan-42-genshin-blender-tutorial-cynological/` — technique sheet (landed 2026-11-24), rebuild record and gate result when Passes 3–4 run.
