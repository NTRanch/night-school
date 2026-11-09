# Plan 15 — Pass 1 Timed Observation

Source: pinned 720p capture (MANIFEST.md), 4,991.333 s.
Tool on screen: **Source Filmmaker [Beta]** (window title:
`...\sessions\artwork\nsfw\tutorial.dmx`), Windows desktop,
session recorded **19/03/2021** (taskbar clock, frames g02/g08).
Observation base: 42 grid stills @120 s + 166 grid stills @30 s
+ targeted sets (opening 15 @4 s, open 6, cuts1 10, cuts2 9,
tail 7) + native crops — **255 stills** — plus the chunked
transcript (UNCONFIRMED tier; §1). Screen governs.

## 0. Premise + safety verdicts (taken before Pass 2)

**Premise: TUTORIAL — confirmed, as titled.** This is not a
Plan 14 case. Evidence:
- The file is a screen recording of a complete SFM animation
  session (`tutorial.dmx`) in which a two-character scene is
  posed, keyed, lit and exported, with continuous narration
  (transcript §1) and teaching furniture: an opening showcase
  of the finished animation (6–34 s), a "12 Principles of
  Animation" title card (≈48–52 s, all twelve listed), and an
  end card ("Thanks for watching!", ≈4,965 s) with a
  "Finished product" credits frame (≈4,980 s).
- Page corroboration: categories include **Tutorials**; the
  session file is literally named `tutorial.dmx`.
- SHOULD-BE-SEEN check: "long-form tutorial of a POV scene
  build: viewpoint rig, head-bob/body-presence method, partner
  animation relative to a moving camera, render/review loop" —
  SEEN in substance (see §2–§5); the tool is SFM, not Blender
  (the plan named no tool).

**Safety clause: PASS — proceed.** The depicted partner is
Bonnie the Bunny (FNAF): an animatronic robot rendered at adult
humanoid proportions (tall, long-limbed, adult female secondary
characteristics on the female variant — frames s01185, s03915).
The viewpoint character is a matching adult male animatronic.
No figure reads as a child or age-ambiguous in any of the 255
sampled stills; the depiction is of adult-proportioned robots.
The barred-plan ground (canon minor / age-ambiguous depiction)
does not obtain.

## 1. Transcription record

Method per the chunked-transcription skill: whisper.cpp
1.9.2 (`whisper-cli`), model ggml-large-v3-turbo
(`/usr/share/whisper.cpp-model-large-v3-turbo/`), audio
extracted from the canonical capture (16 kHz mono WAV,
primo `plan-15/audio.wav`), chunk map: chunk1 0.0–3300.0 s,
chunk2 3300.0–4991.3 s. Tier: **UNCONFIRMED** (single
transcriber; screen governs).

**Coverage at this plan's close-out (snapshot 2026-11-06
~19:52 PST) — PARTIAL, stated plainly.** Programme-wide
transcription contention (8–10 concurrent whisper jobs
across plans 11/13/15/16/17/19 + tenants; load ≈ 40 on 16
threads) throttled every job to ~0.1× realtime. Transcribed
and cited here, from the streamed segment logs
(`dl/chunk1-partial.log`, `dl/sliceB-partial.log` on primo
under `plan-15/chunks/`, `plan-15/slices/`):

- chunk1 stream: segments through **285.4 s** (of 0–3300)
- sliceB stream (head/aim segment, offset +3280 s):
  segments through **3361.0 s** absolute (81.0 s of span)
- sliceC stream (offset +1500 s): through **1526.6 s**
  absolute (26.6 s of span)

Unique coverage ≈ **393 s of 4,991 s (7.9%)**. The covered
spans were chosen at the decisive points (opening + method
setup; the head/aim-constraint segment; the cycle-keying
segment head) and every [SPEECH] claim in §7 cites its
span. The full transcription continues detached on primo
(`ns15-whisper`, chunk1 → chunk2; slices2 ladder behind
it); `dl/stitch.py` (offset stitch with `[SEAM]` marker at
3300 s) and the skill's `loop_census.py` (rule
normalized-segment-v1, threshold >8) are staged in `dl/` —
the stitch + census harvest is mechanical once the jobs
land, and no claim in this plan waits on it: the two
load-bearing speech items (C-05's counter-phase method,
C-09's aim-weight narration) are inside the covered spans
and screen-corroborated. Loop census: NOT RUN on a partial
record (a census of 7.9% would be a false statistic);
recorded here as an open mechanical step, not a finding.

## 2. Session anatomy (screen)

Animation sets in the session (Animation Set Editor, frames
g02, s03405, s03525, s04335):
- `bonnie_male1` — the viewpoint character's body (male
  Bonnie): control groups RigBody (rig_root, rig_pelvis,
  rig_hips, rig_spine_0, rig_spine_1, rig_neck, rig_head),
  RigLegs (rig_knee/foot/toe L/R), RigArms, Unknown.
- `bonnie1` — the partner (female Bonnie): same rig groups
  plus model bones under Unknown (bip_vagina, bip_urethra,
  bip_breast_L/R, bip_buttock_L/R, bip_tail_1–3, bip_jaw,
  bip_eyebrow/eyelid/lip family, bip_ear1_L, bip_paw… —
  frame s01185) and, inside RigBody under the spine chain,
  three **aim constraints**: `aimConstraint_rig_head -
  axis_helper_Gam…`, `aimConstraint_rig_neck -
  axis_helper_Game…`, `aimConstraint_rig_spine_1 -
  axis_helper_Ga…` (frame s03405 + crop; helper name truncated
  on screen — UNREADABLE register item 1).
- `camera2` — the shot camera (the session's scene camera;
  viewports label it "camera a2").
- **Separate head/eye models**: `Bonnie head` (Body →
  rootTransform), `Male Bonnie head`, `Bonnie eyes`,
  `Male Bonnie eyes` (frames s03405, s03525, s04335). The
  bodies' heads are not the only heads in the session: head
  models are independent animation sets with their own keyed
  rootTransform channels (graph editor, s04335).
- Lights (light4's attribute list read at g41: intensity,
  ambientIntensity, horizontalFOV, verticalFOV, radius,
  shadowFilterSize, shadowAtten, minDistance, maxDistance,
  constantAttenuation, linearAttenuation,
  quadraticAttenuation, shadowDepthBias,
  shadowSlopeScaleDepthBias, farZAtten, nearEdge, farEdge,
  cutOn, cutOff, volumetricIntensity, noiseStrength, width,
  edgeWidth, height, edgeHeight).

Scene: a FNAF pizzeria hallway (checkerboard wainscot,
red/black check floor). Shot: "Tutorial / shot1". Shot time
readouts seen: 0.133 (g08), 0.206 of 0.800 (s01185), 1.016
(s03405), 8.233 (s02085), 2.933 (tail frames) — the shot is a
short loop (seconds), worked across the whole 83-minute
session.

## 3. Structure of the 83 minutes (screen, 30 s grid)

| Span (s) | What happens |
|---|---|
| 0–6 | HSTUDIOS logo card |
| 6–34 | Finished animation playing in a maximised viewport (lit, third-person showcase angle); camera attribute list open (fieldOfView, aperture, toneMapScale, bloomScale, SSAO family) |
| 38–52 | "ANIMATION" title card; **12 Principles of Animation** card |
| 42–~1500 | Posing pass: bodies arranged in the doggystyle blocking; long detailed work on feet/toes, hands/fingers, legs (work camera close-ups; shot camera in primary viewport) |
| ~1125–1245 | Contact posing at the pelvis (work camera behind partner, transform gizmos at the contact set) |
| 1513–1521 | **Desktop break** (scene-cut cluster 1): YouTube + Patreon page ("Hi, HStudios", 10 patrons) — not technique |
| ~1545–2100 | Partner head/face work (face close-ups, eyelid/ear controls); breasts keyed in the graph editor (bip_breast channels, s01185 region); the thrust cycle's dense keys visible on rig_pelvis/rig_hips (s02085) |
| ~2100–3270 | Continued keying/refinement: hands planted beside partner, fingers, feet; motion-editor (green) time selections from ~3165 |
| 3269–3273 | **Desktop break** (scene-cut cluster 2): VEGAS Pro timeline + Audacity — the narration/edit layer, not technique |
| ~3285–4400 | Head-model work: `Bonnie head` / `Male Bonnie head` rootTransform keying; aim-constraint controls visible in bonnie1's tree; camera copy-to-work-camera menu (s04335) |
| ~4400–4830 | Graph-editor refinement of the cycle; export dialogs (~4695–4730); lighting pass (dark lit views ~4785–4830) |
| 4860–4960 | SFM export/render dialog open over the final lit scene |
| ~4965 | "Thanks for watching!" card |
| ~4980 | "Finished product" credits card (editor credit @OpacityNSFW; Patreon credits) |

## 4. The viewpoint rig (plan focus 1)

(Transcript-anchored claims are numbered in §7; screen facts
here.) What the screen alone establishes:

1. **Two viewports, two cameras, always.** Primary viewport =
   the shot camera (camera2); secondary viewport = the work
   camera. The creator poses in the work camera while the shot
   camera's framing stays on screen — the POV framing is
   checked continuously, not at render time (every SFM frame
   in the grids shows this split).
2. **The shot camera is a first-person camera.** In the
   primary viewport the view sits at the male's head position
   looking down at the partner: his own legs, arms and hands
   enter the frame edges (o00070: his legs + reaching hands;
   g02: his leg/arm mass at frame left; s01185: partner's back
   filling the frame from immediately behind). No frame shows
   the male's head or face in the shot camera — the camera
   occupies the head.
3. **Head motion is authored on a separate head model.** The
   male's head is its own animation set (`Male Bonnie head`,
   single rootTransform), and its graph-editor curves are
   hand-keyed smooth curves (s04335: rootTransform Position/
   Rotation channels, sparse keys, spline mode). The body
   (bonnie_male1) carries its own rig_head control and dense
   cycle keys (s02085).
4. **Aim constraints ride the partner's spine chain.** bonnie1
   carries aimConstraint entries on rig_head / rig_neck /
   rig_spine_1 pointing at axis_helper objects (s03405 crop) —
   constraint-driven orientation in the partner's upper body,
   present as rig furniture in the session.

## 5. Body presence (plan focus 2)

- The viewpoint character's body is IN the shot: knees/legs at
  the frame edges, his arms reaching past the camera to plant
  hands on the partner's back/hips and on the floor beside
  her (o00070, g02, s02535 region, opening showcase). His
  hands are posed finger-by-finger in the work camera
  (~2535–3015 s span: repeated hand/finger close-ups).
- The partner's hands are likewise planted on the floor with
  finger-level posing (same span) — her support points are
  authored, not defaulted.
- Registration method (screen): the creator poses from the
  work camera but verifies in the shot camera (primary
  viewport is always the shot camera); contact at the pelvis
  is posed with the work camera directly behind the partner
  at close range with gizmos on the contact controls
  (~1125–1245 s).

## 6. Partner blocking + contact under a moving viewpoint (plan focus 3)

- Blocking: partner on all fours (hands + knees planted),
  viewpoint character kneeling behind, hands on her
  back/hips; the arrangement is held for the whole session —
  one act, one loop, refined for 83 minutes (cf. Plan 01's
  single-loop discipline).
- The thrust cycle is **dense-keyed** on the male's
  rig_pelvis/rig_hips graph channels: at s02085 the graph
  editor shows a repeating cycle pattern of keys across the
  full shot span (period ≈1 s at the graph's scale) — the
  loop is baked keys, not a two-key interpolation.
- Comparison thread vs Plan 01 (fixed camera): Plan 01's
  contact was constraint-locked (Child Of) and measured from
  a fixed external camera; here the camera rides the action,
  so registration is maintained by (a) the dense shared cycle
  keys and (b) continuous shot-camera verification while
  posing — the creator never poses blind from the work camera
  alone. (Distillation §: TECHNIQUE.md.)

## 7. Claims list (numbered; Pass 3 test list)

Provenance: [SCREEN] = the 255-still record; [SPEECH] =
transcript, UNCONFIRMED tier (§1 — partial coverage under
programme-wide contention; every load-bearing claim below
is screen-corroborated or flagged). UNREADABLE dependencies
reference §8.

- **C-01** [SCREEN] Premise: this is a genuine tutorial —
  a Source Filmmaker session building one scene start-to-
  finish, with an opening finished-animation showcase
  (6–34 s), a "12 Principles of Animation" card (~48–52 s),
  narration throughout, and end/credits cards (~4965 s,
  ~4980 s).
- **C-02** [SCREEN] Safety clause PASS: the depicted
  character is Bonnie the Bunny (FNAF) — an animatronic
  robot at adult humanoid proportions; the viewpoint
  character is a matching adult male animatronic. No child-
  like or age-ambiguous figure appears in any of 255
  sampled stills.
- **C-03** [SCREEN] Session anatomy: animation sets
  `bonnie_male1` (viewpoint body), `bonnie1` (partner),
  separate `Bonnie head` / `Male Bonnie head` and
  `Bonnie eyes` / `Male Bonnie eyes` sets, `camera2` (shot
  camera), plus lights (§2).
- **C-04** [SCREEN] The action cycle is authored as dense
  baked keys on rig_pelvis/rig_hips at ~1 s period (graph
  editor) — keyed, not simulated and not captured.
- **C-05** [BOTH] Authoring order: select the key parts
  first (pelvis/hips/spine/neck/feet), set the loop length,
  pose the middle, then key pelvis and hips in counter-
  phase — narration: *"as the pelvis moves down the hips
  move up… as the body hip pelvis moves back up the hips
  move down"* [SPEECH, chunk1 log 3:55–4:12]; the graph
  editor's dense counter-phased channels corroborate.
- **C-06** [SCREEN] The viewpoint character's head is an
  authored performance: `Male Bonnie head` rootTransform
  curves are sparse, smooth, spline-mode (s04335) — no
  capture noise, no solver output.
- **C-07** [BOTH] rig_head / rig_neck / rig_spine_1 carry
  aim constraints toward axis-helper targets — screen-
  listed on the partner's set (full helper names
  UNREADABLE — §8 item 1), and the narration (C-09)
  applies the identical setup to the viewpoint
  character's head: upper bodies are aim-oriented over
  their keyed animation, not purely FK-keyed.
- **C-08** [SCREEN] Dual-viewport discipline: the primary
  viewport is the shot camera (camera2) throughout the
  session while posing happens in the work camera —
  framing is verified in-camera continuously, not after.
- **C-09** [BOTH] The POV is embodied by binding the shot
  to the viewpoint character's head, and the head itself
  is a two-layer performance: (a) its own keyed animation
  on the separate head set (C-06), plus (b) an **aim-
  constraint layer whose weight blends pointing against
  the keyed motion**. Narration in the head-work segment
  (sliceB, video 3280–3361 s): with the aim weights full
  *"he doesn't move anymore… lower how much it'll point…
  now the head can move… you can animate the head with
  this while also having the head already have
  animation… we just apply it to the other body… they
  have animation on their head but we can still point
  their head in different directions."* Screen
  corroboration: the aim constraints listed in the set
  editor (C-07, on the partner; the narration applies the
  same setup to both bodies) and the separate head/eye
  sets (C-03). The camera rides the head that this stack
  produces. (The constraint targets' full names remain
  UNREADABLE — §8 item 1 — but the mechanism is now
  speech-confirmed, not inferred.)
- **C-10** [SCREEN] Presence is staged: the viewpoint
  character's legs/arms enter the shot frame in the
  finished piece; his hands and the partner's hands are
  posed finger-by-finger (~2535–3015 s); contact is posed
  with the work camera behind the partner (~1125–1245 s).
- **C-11** [SCREEN] Registration under the moving
  viewpoint is maintained by (a) the dense shared cycle
  keys and (b) continuous shot-camera verification while
  posing (C-08) — there is no separate registration
  mechanism to find.
- **C-12** [SCREEN] No simulation anywhere in the session:
  no solver, ragdoll, or capture device appears in 255
  frames; the Procedural panel (Smooth/Jitter/Stagger/
  Hold…) is SFM's curve-shaping presets applied to keyed
  channels.
- **C-13** [SPEECH] The loop is short and bookmarked:
  narration sets the loop length at the start ("how long
  do you think the loop is going to be… I'd say about
  0.45", chunk1 log ~3:01–3:15) and shot-time readouts on
  screen run to 0.800 s — read as a ~0.8 s shot with the
  0.45 figure its approximate half-cycle; flagged
  ambiguous, UNCONFIRMED, not load-bearing.
- **C-14** [SCREEN] The recording is otherwise continuous:
  the scene-cut scan finds only 7 cuts in 4,991 s — a
  desktop break (1513.6–1520.3 s: YouTube + Patreon page)
  and a VEGAS Pro/Audacity switch (3269.3/3273.3 s), both
  edit-layer, not technique.
- **C-15** [SCREEN] The tail is a lighting pass (light4
  attributes, ~4785–4830 s) and an export dialog
  (~4860–4960 s) whose settings are UNREADABLE at 720p
  (§8 item 3).

## 8. UNREADABLE register

1. The aim-constraint helper names are truncated on screen
   (`axis_helper_Gam…` / `axis_helper_Game…` / `axis_helper_Ga…`)
   in every frame that shows them — the full target names are
   UNREADABLE from the capture.
2. Graph-editor numeric values (curve amplitudes for the head
   rootTransform and the cycle channels) are visible as shapes
   only; no axis scale is legible at 720p — magnitudes are
   UNREADABLE, key placement/shape are not.
3. The SFM export dialog settings at 4860–4960 s are
   UNREADABLE beyond the dialog's presence (small text at
   720p).
