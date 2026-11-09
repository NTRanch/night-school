# Plan 15 — Pass 4: Application gate

Date: 2026-11-06. Gate per plan: **PASS = the POV evidence
reads as embodied (presence + registration); a floating-
camera feel = FAIL.** Benchmark: `rebuild/BENCHMARK.md`
(written before the final renders). All reads below are
agent reads from the final artifact (runC frames +
`runC-measurements.json` + ray-cast occlusion record);
embodiment is ultimately an eye verdict — see eye items.

## Gate reads

- **Floating-camera test — PASS (it is the opposite of
  floating).** The camera is hard-locked to the viewpoint
  character's head bone (Child Of, influence 1.000, lock
  drift ≤ 0.0001 mm across the loop) plus a small authored
  bob keyed to the action's own phase table. Nothing in any
  evidence frame reads as a detached or smoothed camera: at
  the follower peak the partner's back crowds to 4.6 cm from
  the eye and fills the frame — a floating camera never gets
  crowded out by the action.
- **Registration — PASS.** Contact anchor holds the central
  box at every named peak (s38 (480.07, 295.83), s45
  (479.96, 297.18) at 960×540); hand screen error at the
  grips ≤ 1.14 px (nominal) / ≤ 1.88 px (frozen-offset);
  world hand registration identical to Plan 01's fixed-
  camera record (below).
- **Presence — FAIL as a visible read.** The viewpoint
  character's body does not visibly enter any final frame:
  her hands project in-frame at the grips but are not
  visually distinguishable (partner silhouette + the
  inherited single pale material for both characters), and
  the contact set itself is occluded by the partner's back
  at every phase (first surface 0.046–0.158 m vs contact at
  0.47–0.49 m — PASS3-REBUILD ray record). The partner-
  hidden diagnostic proves the presence geometry IS in this
  framing (chest edge, forearms, both hands); the failure is
  blocking + materials, not rig placement.

**Gate verdict: FAIL on the plan's letter (presence leg),
with the failure localised and measured** — the rig is
correct and the registration is exact; what fails is the
Plan 01 scene's blocking transplanted into POV. The
tutorial's own blocking (partner on all fours, back low,
sightline over the back to the contact and to the viewpoint
character's hands at her hips) is precisely the condition
the Plan 01 seated blocking violates. Adopted as the plan's
central application finding: **POV is a blocking discipline
before it is a camera discipline** — a fixed-camera scene
cannot be re-shot from the head without re-blocking; the
camera mechanism (head lock + authored bob) transfers
exactly, the composition does not.

## Registration comparison vs Plan 01's fixed case (numeric)

| Measure | Fixed camera (Plan 01) | Moving POV (Plan 15) |
|---|---|---|
| Contact lock drift | ≤ 0.0001 mm (Plan 01 record) | ≤ 0.0001 mm (Child Of head lock) |
| Hand registration, world (frozen def) | L 4.9388 / R 4.9276 mm max | L 4.9389 / R 4.9277 mm max — unchanged; the camera cannot degrade a world-space registration, and the measurement chain reproduces Plan 01 to ~0.0001 mm |
| Contact anchor screen travel | range (1.096, 0.762) px | range (0.180, 9.231) px — the anchor stays centred by construction (it sits near the view axis); travel is ~12× vertically, ~0.2× horizontally |
| Follower reaction screen read (Spine2 range_y) | 1.918 px | 100.727 px (~52×) — the embodied camera amplifies the partner's reaction into the dominant in-frame motion |
| Viewpoint pelvis screen travel (range_y) | 9.170 px | 10.911 px — comparable; the thrust reads at similar scale, the reaction does not |

What is actually harder under motion (itemised in
TECHNIQUE.md): sightline occlusion becomes phase-dependent;
presence must be staged (grips inside the frustum at the
partner's silhouette edge); the near plane and hair/head
geometry become framing constraints; verification needs the
shot camera open while posing, not after.

## SFW translation note

The mechanism is lane-neutral: for first-person SFW scenes
(tutorial/over-the-shoulder work cameras, first-person
exploration, character-POV cutscenes in the estate's SFW
games) the transferable unit is **head-bone lock + a small
authored bob keyed to the action's phase table + presence
staging** (the character's own hands/body entering frame at
registered points), with two disciplines carried over:
(1) block for the sightline — keep the eye→subject line
clear at every phase, or name the occlusion as a deliberate
beat; (2) verify in the shot camera while posing, never
only in the work camera. The bob amplitudes used here
(12 mm forward, 6 mm dip, 1.1° pitch at peak) are a sane
default envelope for SFW first-person work at this scene
scale; the micro-roll (0.35°, 2 cycles/loop) is optional
seasoning, not structure.

## Eye items (Owner's eye is the gate for embodiment)

1. `rebuild/runC-frames/pov_0038.png` + `pov_0045.png` —
   does the partner's back crowding the frame at Contact /
   follower peak read as *embodied closeness* or as a
   *camera fault*? (Agent read: embodied; the s45 frame is
   the strongest presence evidence in the set.)
2. `rebuild/runC-frames/pov_0000.png` vs `pov_0019.png` —
   the loop's in-frame silhouette shift; does the motion
   read as the viewpoint character's own movement?
3. `rebuild/diag38_nopartner.png` — the presence the full
   render hides: chest edge, forearms, hands at the grips.
   If this framing reads as embodied to the Owner's eye,
   the presence FAIL is a materials/blocking fix (partner
   re-block or material separation), not a rig redesign.
4. The source's opening showcase (video 6–34 s, third-
   person) vs its working shot — the tutorial itself
   presents the finished piece from outside the POV; the
   Owner may want the estate's POV evidence standard to
   require a paired external view for exactly the occlusion
   reason this plan measured.
