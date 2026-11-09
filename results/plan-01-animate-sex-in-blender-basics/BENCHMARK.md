# Plan 01 Pass 3 — Expected-vs-seen benchmark (written BEFORE final renders)

Date: 2026-11-06. Artifact under gate: the two-body contact loop built by
`build_loop.py` (Prima = Follower, Yui = Leader), 78 samples @ 60 Hz,
Contact at sample 38, rendered evidence frames in `frames/`.

What the loop SHOULD read as, at viewing size (960×540 evidence frames),
before any frame is looked at:

1. **Contact held.** In the Contact frame (sample 38) and at every phase
   point, the two pelvises read as in registered contact — no visible air
   gap at the contact set from the side camera, and no visible mesh
   breakthrough. (Measured counterpart: drift + penetration lines in
   PASS3-REBUILD.md; the camera tolerance of the source does NOT apply —
   binding finding 3.)
2. **Follower phase lag visible.** Comparing sample 19 (pre-contact),
   sample 38 (Contact) and sample 45 (follower peak): Prima's spine/head
   reaction is absent at 19, still at rest at 38, and visibly peaked at
   45 — she answers after contact, she does not move with Yui. Yui's
   advance is the only motion before 38.
3. **Leader reads as rotation, not sliding.** Yui's advance into Contact
   reads as a lean/pivot over her knees (torso counter-rotation, head
   comparatively still), not as her whole body translating toward Prima.
4. **No visible penetration at the contact set at viewing size.** At
   samples 38 and 45, no body mesh visibly passes through the other at
   the pelvis contact set in the side view.
5. **Seam invisible.** Frame 0 and frame 78 are the same image (pixel
   hash check backs this), and Prima at the seam is mid-recovery, not
   parked at a rest pose.
6. **Hands stay planted.** Prima's hands stay on her own thighs and
   Yui's hands stay on Prima's thighs at 19 / 38 / 45 — no floating or
   sliding grip.
7. **Faces alive, phased with the follower.** Prima's expression at 45
   (half-close + mouth + heart pupils for the trio girl) is visibly
   stronger than at 19; Yui's stays comparatively steady.

Per-item PASS/FAIL with the agent's reads lands in PASS3-REBUILD.md §6;
items needing the Owner's eye are queued there as eye items (frames are
the gate; the rendered clip is a bonus).
