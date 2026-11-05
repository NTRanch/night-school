# Plan 06 — How to Make 3D Porn Cum Sims, Part 2: Adding Cum to Animations

- **Source:** https://rule34video.com/video/3213824/how-to-make-3d-porn-cum-sims-part-2-adding-cum-to-animations/
- **Video ID:** 3213824 · **Creator:** Mushen (sponsored by Anime Nyan) · **Duration:** 1:30:42 · **Views at intake:** 25,949 · **Licence:** stated CC0 on the video page — the tutorial itself may be reused; the rebuild still proceeds clean-room so the estate version carries its own provenance
- **Lane:** NSFW-only in subject / SFW translation: the *timing and compositing* method — effect passes synced to action peaks — is medium-general
- **Estate targets:** Torogao fluid/contact systems, animation effect passes, the game-feel/juice toolkit's timing grammar
- **Status:** PLANNED — run after Plan 07 (Part 1) so the simulation being composited is understood first

## Why this video

Part 2 is the integration half: a finished fluid simulation meets a
finished character animation. The estate has the same shape of problem
wherever an effect must land on a moving body at a story beat — sync,
attachment, interaction with skin and gravity, and not breaking the
underlying performance. The subject is specific; the integration
discipline is the study.

## SHOULD-BE-SEEN (written before viewing)

The sim output (cache/mesh sequence) imported into the animation
scene, aligned to the action's timing, adjusted where it intersects
or floats, rendered/composited so it reads as belonging to the same
world and light as the bodies.

## Timed observation focus

- Import format and scale/orientation reconciliation between the sim
  scene and the animation scene.
- Timing method: how emission frames are matched to the animation's
  peaks — by frame numbers, by markers, by eye.
- Attachment: what is parented, what is hand-offset per frame, what
  is left to the sim.
- Collision aftermath: how fluid-on-skin behaviour is faked or fixed
  after the fact (decals, mesh edits, shader tricks).
- Material and render: the fluid's shader settings, and render-pass
  separation if any.
- Failure fixes shown on screen — logged verbatim; this is where the
  integration knowledge lives.

## Distillation targets

1. **Sync method** — the mechanism tying effect timing to performance
   timing. Question: does it survive retiming the animation, or is it
   welded to one take?
2. **Contact believability kit** — the tricks that sell fluid/body
   contact. Question: which are geometry, which are shading, which
   are timing?
3. **Pass structure** — what is rendered together vs composited.
   Question: what does the split buy, and what does it cost?

## Clean-room rebuild spec

- On an estate two-body scene (Plan 01's rebuild output): attach a
  Part-7-rebuilt simulation using only the distilled sync method,
  scripted and re-runnable; retime test — shift the animation by a
  known offset and show the effect follows by the method, not by
  hand repair.

## Application

- **NSFW application:** Torogao's fluid/contact seam gets a named,
  tested integration method instead of per-scene improvisation.
- **SFW translation:** the sync method is the same one juice effects
  need (impacts, splashes, bursts on action peaks); the retime test
  is written lane-neutrally so the SFW toolkit can adopt the method
  without the subject matter.

## Gate

Retiming test is the gate: PASS = effect stays registered after the
offset with zero hand edits; FAIL = the method was keyed illusion, and
the plan records it as such.

## Deliverables

- `results/plan-06-cum-sims-part-2/` — technique sheet, integration
  record, retime test evidence.
