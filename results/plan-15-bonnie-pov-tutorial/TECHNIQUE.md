# Plan 15 — Pass 2: Technique distillation

Source: OBSERVATION.md (screen-governed; transcript
UNCONFIRMED tier). Clean-room: mechanisms only — no source
assets, models, or session files are reproduced; the estate
rebuild (Pass 3) was built from this sheet alone.

## 1. The camera-body method — how the POV is made embodied

**Answer: authored curves all the way down — no simulation,
no capture.** Three layers, each with its evidence:

1. **The shot camera is bound to the viewpoint character's
   head, and the head is a two-layer authored performance.**
   The session carries the viewpoint character's head and
   eyes as their own animation sets (`Male Bonnie head`,
   `Male Bonnie eyes`, separate from `bonnie_male1`'s body
   rig) and a dedicated shot camera (`camera2`); the primary
   viewport shows the shot camera's view continuously while
   the body is posed from the work camera. Layer one: the
   head set's `rootTransform` channels are keyed in the
   graph editor as **sparse, smooth spline curves** (frame
   s04335). Layer two [BOTH — OBSERVATION C-09]: an **aim
   constraint** on the head whose weight blends *pointing*
   against the keyed motion — weights full, the head is
   locked to its aim target ("he doesn't move anymore");
   weights lowered, the keyed animation plays AND the head
   can still be pointed. The same setup is applied to both
   bodies. The camera reads through the stack: keyed head
   performance + weighted gaze. The rebuild (Pass 3) adopts
   the explicit head-bone lock with the authored bob as its
   keyed layer; the aim layer is carried as an Adapt item
   below (not built — the Plan 01 loop's heads are FK and
   were not re-rigged).
2. **The body cycle underneath is dense baked keys.** The
   thrust cycle on rig_pelvis/rig_hips is a dense key field
   at ~1 s period (graph editor, frames s02085 class) — the
   loop is built by keying the extremes and the middle, then
   letting SFM's procedural panel (Smooth/Jitter/Stagger/
   Hold presets visible in the session) and manual graph
   work shape the in-betweens. The narration states the
   method plainly [SPEECH]: select the key parts first
   (pelvis/hips/spine/neck/feet), bookmark the loop length
   (~0.8 s shot), pose the middle, and key the pelvis/hips
   in counter-phase — *"as the pelvis moves down the hips
   move up… as the body hip pelvis moves back up the hips
   move down."*
3. **Presence is posed, not implied.** The viewpoint
   character's hands and fingers are posed finger-by-finger
   at the partner (video ~2535–3015 s), his legs/arms enter
   the shot frame in the finished piece, and contact is
   posed with the work camera moved behind the partner
   (~1125–1245 s) — i.e. the animator stages what the head-
   locked camera will see, then verifies it in the shot
   camera. Embodiment = a locked viewpoint + an authored
   head + a body that is actually there to be seen.

Secondary mechanisms: both characters' head/neck/spine
carry **aim constraints** (`aimConstraint_rig_head/neck/
spine_1` → axis helpers; full helper names UNREADABLE) —
upper bodies are oriented by weighted aim targets over
their keyed animation, which is how the partner's back
stays presented to the camera through the cycle and how
the viewpoint character's gaze stays on her. Procedural presets (Smooth/Jitter/
Stagger/Hold) are SFM's built-in curve-shaping operators —
authoring aids applied to keyed channels, not a physics or
simulation layer; nothing in 255 sampled frames shows a
solver, a ragdoll, or a capture device.

## 2. Registration under motion — what is harder than Plan 01's fixed case, itemised

Plan 01 held registration under a FIXED camera: contact
lock drift ≤ 0.0001 mm, keyed-Hips registration ≤ 0.393 mm,
hands ≤ 4.94 mm from their grips (world space). Moving the
camera onto the viewpoint character's head changes the
problem in these specific ways (each item measured or
observed in this plan's rebuild):

1. **Occlusion becomes phase-dependent.** Under a fixed
   camera a clear sightline stays clear. Under the head
   lock, the eye→contact ray's first surface moved between
   0.046 m and 0.158 m across the loop (contact itself at
   0.47–0.49 m): the partner's reaction carries her back
   INTO the sightline at the peak. Registration you cannot
   see is registration you must prove by projection, not by
   eye — hence this plan's screen-projection measures.
2. **The subject's reaction is amplified ~52×.** The same
   follower spine motion that spans 1.9 px under the fixed
   camera spans 100.7 px from the head: relative motion
   (camera body + subject body) compounds. Keying that
   reads calm externally can read violent in POV; the bob
   envelope must be budgeted against the subject's motion,
   not absolutely.
3. **Presence must be staged inside the frustum.** Hands
   registered to grips in world space are worthless if the
   grips sit outside the frame or behind the partner's
   silhouette. In the rebuild the grips project in-frame at
   the silhouette edge (screen error ≤ 1.14 px) — by the
   scene's luck, not by Plan 01's design; a POV-first scene
   places grips for the frame.
4. **Head geometry becomes a framing constraint.** The eye
   must sit at the face plane: a world-axis offset put the
   camera inside the character's hair mesh (runA — all
   frames blank). Near plane (0.02 m), hair, ears and muzzle
   geometry bound where the eye may sit; the offset must be
   expressed in head-bone space.
5. **Verification doubles.** Every pose must be checked in
   the shot camera as well as the work camera — the
   tutorial's dual-viewport discipline (primary viewport =
   shot camera throughout) is not a preference, it is the
   only way registration under motion gets seen at all.
6. **What does NOT get harder:** world-space registration
   itself. The contact lock and hand errors are identical
   to the fixed case to ~0.0001 mm — the camera adds a
   *visibility and staging* problem on top of the same
   *placement* problem, and conflating the two is the error
   to avoid.

## 3. Adopt / Adapt / Reject

| Technique (from the sheet) | Verdict | Estate form |
|---|---|---|
| Shot camera bound to the viewpoint character's head; head keyed as its own performance | **Adopt** | Child Of head-bone lock + authored bob layer on the action's phase table (Pass 3 rig) |
| Dual-viewport discipline: pose in work camera, verify in shot camera, continuously | **Adopt** | Standing rule for any embodied-camera scene work |
| Dense baked cycle keys + procedural curve-shaping (smooth/stagger/hold class operators) | **Adapt** | Estate loops already key the cycle; add curve-shape passes as graph-editor discipline, phase table shared between body and bob |
| Pelvis/hips counter-phase keying ("pelvis down, hips up") | **Adopt** | Named in the loop-authoring notes; already legible in Plan 01's curve set |
| Aim-constraint layer over keyed head/spine animation, weight-blended (point vs play) | **Adapt** | Blender equivalent: Track To / Damped Track with influence keyed as the blend, on spine-neck-head toward a gaze target empty — candidate for the two-body standard, including on the viewpoint character (his gaze layer); not built in this plan (the Plan 01 loop is FK and was not re-rigged) |
| Separate head/eye animation sets (head model ≠ body model) | **Adapt** | Estate form is a separate bob/anchor layer rather than a separate model; adopt the *separation of concerns*, not the file structure |
| Finger-by-finger hand posing for presence | **Adopt** | Already estate practice from Plan 01; this plan adds: pose them FOR the shot camera's frustum |
| Blocking: partner low (all fours), sightline over the back | **Adopt as a requirement** | POV scenes must be blocked for the eye→contact sightline at every phase; a fixed-camera blocking does not transplant (Pass 4 finding) |
| SFM procedural panel presets as shipped behaviour | **Reject** | Tool-specific operators; the estate takes the curve-shaping *intent*, implemented in its own graph workflow — nothing tool-bound ships |
