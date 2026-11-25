# Plan 43 — Pass 2 Technique Sheet (Distillation)

Source: Professor Goo / DillonGoo, "Animator Explains Why ZZZ
Cinematics Look So Good" (YouTube 76jIDBfOQT4, 14:33). Study run:
2026-11-24, fathom route. **Confidence: VERIFIED** (full recoverable
transcript; frames agree). Timestamps from the transcript. Admitted:
animation craft; several items carry rig implications.

- **T1 — Hand-drawn impact frames (00:00:58).** At the moment of a
  hit, a hand-drawn impact frame is cut into the 3D sequence. The
  drawn frame sells force the geometry cannot.
  → **Adopt** as a scene-spec device class (1–2 frame impact inserts
  at hits) for the Laplace3D-bar animation work. Not a rig feature.
- **T2 — Universal secondary drag (00:01:19).** *Everything* drags:
  hair, cloth, props lag the body's rotation with matched spin, and
  FX (an air-tunnel streak) are added to accentuate the drag.
  Secondary motion is the default state, not a garnish.
  → **Adopt as the R5 acceptance read**: hair + cloth chains drag with
  matched spin against body rotation. Springs are tuned until the
  motion gate reads this way.
- **T3 — The anticipation drag beat (00:01:38).** Before the payoff
  slash, the character does *not* rise immediately — a beat of
  drag/delay is held first. The delay is what sizes the payoff.
  → **Adopt** into scene-spec beat design (delay before payoff).
- **T4 — Low focal length dynamism (00:01:34).** Wide lens, the near
  foot huge in frame: foreshortening is embraced as pose energy
  rather than corrected.
  → **Adopt** as camera craft for scene specs; no rig change.
- **T5 — The treadmill shot: character parented to the camera
  (00:01:55–00:02:24).** For a running shot the character is parented
  to the camera and the *background* moves; the pose is held and read
  in camera space, like a 2D cel. Foot sliding is accepted — because
  the shot is judged in **screen space**, not world space (doctrine
  stated at 00:05:29: the camera may spin while the character travels
  straight; what matters is how it plays on the 2D plane).
  → **Adopt** as directing doctrine: judge shots in screen space.
  **Caution for the import programme**: its error metric is
  world-space; packs must also be judged frame-vs-frame in screen
  space (the A6 comparison discipline already does this — keep both,
  never let the world-space number carry the verdict).
- **T6 — Held pose as characterisation (00:02:59).** In a held pose
  the sword does not move at all — the stillness of the held element
  reads as perfect control. Holds are acting.
  → **Adopt** as an acting note for scene authoring. No rig implication.
- **T7 — Landing without rebalancing (00:03:09).** Characters land
  already balanced — near-zero recoil and **no foot adjustment**
  afterwards. The absent settle is the statement.
  → **Adopt** as a landing-curve authoring note.
- **T8 — Silhouette is the pose criterion (00:03:45).** Poses and
  shots are judged by silhouette legibility; his single nitpick in
  the whole reel is a shoe that hides the entire silhouette behind it.
  → **Adopt (corroboration)** of the pack discipline (silhouette read
  at judging size). Add "no element hides the whole silhouette" as a
  named pack check at motion rungs.
- **T9 — Dutch angles as a system (00:04:31).** Deliberate tilt
  disorients; after a transition the tilt is *mirrored* to re-orient
  the viewer. Slope plus "screen gravity" visualises deceleration on
  landing.
  → **Adopt** as camera craft.
- **T10 — Mixed-rate smear frames (00:07:25).** Smear shapes in which
  the bright "shiny" part of the *same* shape runs at a lower frame
  count than the rest — two cadences inside one drawing.
  → **Adopt** as a scene-level device (cadence inside a shape). Smear
  meshes, if ever built, are scene assets, not base-rig parts.
- **T11 — Torso squash & stretch past anatomy, with settle
  (00:07:45).** The torso elongates and squashes far beyond anatomical
  limits for a few frames, then lands with **two small settle
  bounces**. Intensity is per-character: subtle for some, extreme for
  others.
  → **Rig verify item**: the spine must tolerate non-anatomical length
  change for a few frames without breaking the deform contract, and
  spring tuning needs a two-bounce settle profile. Check against the
  R1 skeleton before R5 closes; if spine bones are length-locked,
  that is a finding, not a preference.
- **T12 — Eyeball shake (00:08:17).** After a move, the eyeballs
  themselves overshoot and jiggle inside the head — secondary motion
  applied to the eyes, not just the head and hair.
  → **Adopt as a tuning item**: eye bones get independent
  overshoot/settle capacity (a spring channel on the eyes).
  Corroborates the estate's bone-driven-eye route.
- **T13 — Hip jut to lengthen the legs (00:10:13).** The hips are
  displaced so the leg line reads longer. In 3D space the pose looks
  broken; in screen space it is correct — and screen space is where
  it is judged.
  → **Adopt** as pose-space pelvis translation — the Hips bone already
  allows it; the parametric body's hip parameters are rest-shape and
  stay separate. No build change.
- **T14 — The 180° rule binds only at cuts (00:11:11).** Inside a
  one-take shot the camera crosses freely; the rule exists only where
  a cut forces the viewer to rebuild the space.
  → **Adopt** as a directing rule for one-take scene specs.
- **T15 — "Break their bones" anticipation (00:12:22).** Extreme
  anticipation poses with heavy drag — joints pushed past anatomical
  comfort, held briefly before the release.
  → **Rig verify item**: joint limits must not clamp below the
  anticipation range. If the rig carries hard rotation limits, they
  need headroom past anatomical comfort.
- **T16 — Momentum stopped dead (≈00:13:30).** Fluid arcs with
  trailing smears terminate in a completely still, stoic held pose.
  The contrast is the effect.
  → **Adopt** as a beat-design note (arcs → absolute hold).

## Conflicts — flagged, not silently adopted

None in this source. The two rig verify items (T11, T15) are findings
to measure, not adoptions: if the R1 skeleton fails either, the record
says so and the programme answers it — the video does not get a vote on
the skeleton.
