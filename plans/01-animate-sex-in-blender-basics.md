# Plan 01 — How to Animate Sex in Blender: Basics

- **Source:** https://rule34video.com/video/3213799/how-to-animate-sex-in-blender-basics/
- **Video ID:** 3213799 · **Creator:** Anime Nyan · **Duration:** 3:23:51 · **Views at intake:** 179,096
- **Lane:** NSFW-primary / SFW translation: two-body contact mechanics for any paired-character scene
- **Estate targets:** Torogao two-body scenes, the cross-medium animation pipeline, the rig evaluator
- **Status:** PLANNED

## Why this video

The estate's universal animation stress test is a believable two-body
scene, and it is still the open problem: the lift mechanism is proven,
but no believable two-person scene has been authored yet. A basics-level
walkthrough of exactly this, in Blender, is the most direct external
reference available for the contact, timing, and posing discipline the
estate's own attempts keep missing.

## Intake notes (2026-11-05)

Sponsored tutorial; the description links companion downloads (a first
sex-loop tutorial pack and a second oral tutorial) hosted off-site.
Those packs are study references only if ever fetched — the video
itself is the curriculum item. Character in the demo: Sombra
(Overwatch) — the technique, not the character, is the study.

## SHOULD-BE-SEEN (written before viewing)

A beginner-oriented Blender workflow: how the two rigs are set up
relative to each other, how contact points are kept from drifting or
interpenetrating across a loop, how the cycle is timed, and what the
creator does about hands, weight shift, and secondary motion — or
conspicuously doesn't.

## Timed observation focus

- Rig preparation: bone naming, IK/FK choices, which constraints carry
  the contact (child-of, copy-location/rotation, floor, limit-distance)
  and their influence values over time.
- Root placement: which character's root drives, how the second root is
  slaved or independently keyed, pelvis alignment method.
- Loop construction: cycle length in frames, where keys sit, how the
  first and last poses are matched, graph-editor handling at the seam.
- Contact discipline: how penetration/drift is detected and corrected —
  by eye, by constraint, by offset keys.
- Secondary motion: what moves besides the primary action (spine,
  head, hair, soft tissue), and whether it is keyed, simulated, or
  baked from a modifier.
- Camera and export: framing choices, render settings, loop export.

## Distillation targets

1. **Contact-keeping method** — the mechanism that holds two bodies in
   registered contact across a cycle. Question: is it constraint-solved
   every frame, or keyed illusion that only holds from one camera?
2. **Cycle timing grammar** — key spacing, ease distribution, where the
   accents fall. Question: does the timing read as weight and intent,
   or as a metronome?
3. **Corrective practice** — what the creator checks and fixes. Question:
   which of our known failure classes (drift, clipping, dead upper
   body, frozen face) does their practice catch, and which does it
   never look at?

## Clean-room rebuild spec

- Rebuild the cycle in Blender from the technique sheet alone, on two
  estate rigs (a Torogao cast pair), 60 fps canonical, loop seamless
  over at least 3 repetitions.
- Deterministic: scripted scene setup (bpy), seeded, headless render of
  the evidence frames; the interactive session is not the artifact.
- Tests: each Pass-1 claim; plus estate gates — contact-point drift
  measured in pixels across the loop, interpenetration check on the
  contact set, loop-seam frame difference.

## Application

- **NSFW application:** one Torogao two-body scene built with the
  rebuilt method, gated against the Laplace-parity bar.
- **SFW translation:** the same contact method applied to a non-sexual
  paired action (the proven lift, a dance hold, a carry) — contact is
  contact; if the method only works for one act, it was never a method.

## Gate

Expected-vs-seen on the rebuilt scene: contact holds, weight reads,
faces alive. FAIL on drift or seam sends the technique back to Pass 2
with the measurement attached.

## Deliverables

- `results/plan-01-animate-sex-basics/` — technique sheet, rebuild
  record, gate result, drift measurements.
