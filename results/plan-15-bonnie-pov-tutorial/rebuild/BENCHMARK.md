# Plan 15 Pass 3/4 — Expected-vs-seen benchmark (written BEFORE the final v2 renders)

Date: 2026-11-06. Artifact under gate: the POV viewpoint rig
built by `build_pov.py` (v2: lens 21 mm, aim at the partner's
hips +0.05 m) on a copy of the Plan 01 contact loop — Yui =
viewpoint character (Leader), Prima = partner (Follower);
78 samples @ 60 Hz, Contact at sample 38, follower peak 45.
Evidence frames: pov_0000 / pov_0019 / pov_0038 / pov_0045 /
pov_0058 / pov_0078 at 960×540.

Diagnostic evidence already in hand (runB + ray-cast record,
`records/` + PASS3-REBUILD.md): from the head-locked eye, the
partner's back is the first render-visible surface on the
eye→contact sightline at **0.167 m** (the contact surface
itself is at 0.476 m) — the Plan 01 blocking (partner seated
upright, back to the leader) puts her torso across the
sightline. The benchmark below is written for what this
blocking can honestly show; the occlusion is a finding, not
something the framing may pretend away.

What the POV frames SHOULD read as, at viewing size:

1. **Embodied closeness, not floating.** The partner's
   back/hips fill the centre of the frame at every peak; the
   platform/floor shows only at the frame edges. A frame that
   reads as a detached wide or medium shot FAILs this item.
2. **Self-presence.** The viewpoint character's own body
   enters the frame: her torso's lower edge across the top of
   frame and her arms/hands reaching to the grips at the
   partner's sides in at least two of the four named peaks
   (0/19/38/45). (Diagnostic, partner hidden: her chest edge,
   both forearms and both hands ARE in this framing —
   `diag38_nopartner.png`. Whether the partner's silhouette
   occludes the hands in the full render is what this item
   tests.)
3. **Registration under motion.** The contact anchor
   (Prima `mixamorig:Hips`) projects inside the central
   120×120 px box at every named peak, and its full-loop
   screen travel stays in the 5–25 px band (it must move —
   a frozen projection would mean the camera is not riding
   the body — and it must not wander). Measured counterpart:
   pov_measurements.json screen tracks vs the fixed NSCam.
4. **The follower's reaction reads in-frame.** Between s38
   (Contact) and s45 (follower peak) the partner's back/torso
   visibly shifts in frame (her spine reaction), larger in
   screen space than the same motion under the fixed camera.
   Measured counterpart: Prima Spine2 screen std/range, POV
   vs fixed.
5. **Seam invisible.** pov_0000 and pov_0078 are pixel-
   identical (decoded-pixel hash), and the seam pose is
   mid-recovery (inherited from the Plan 01 loop).
6. **Named occlusion (expected, not a surprise).** The
   genital contact set itself is NOT directly visible from
   the head-locked eye in this blocking — the partner's back
   occludes it (ray record). A frame claiming to show it
   would mean the camera left the head. This item PASSes if
   the frames honestly show the occluded geometry (back
   centred, contact anchor projected centre-frame behind it)
   and FAILs if the rig was cheated off the head to see
   around her.

Per-item PASS/FAIL with agent reads lands in PASS3-REBUILD.md
and PASS4-APPLICATION.md; embodiment is an eye verdict — the
Owner's reads are queued as eye items there.
