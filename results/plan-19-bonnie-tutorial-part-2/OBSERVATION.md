# Plan 19 — Pass 1 Timed Observation

Artefact as captured (INTAKE.md): a 1177.033 s Source
Filmmaker screen recording (35,311 frames @ 30 fps) — the
middle sitting of the 2021-03-19 `tutorial.dmx` build
(taskbar 11:40 AM → 12:02 PM, the same sitting Plans 15/18
sample). **World: SESSION** (INTAKE premise verdict). The
variation log below therefore logs what the creator varies
*in the session*: work target, channel family, editor,
shot-time span, camera, and finishing state. All times are
recording seconds unless marked "shot-time". Every number
traces to `records/` in this run dir or to a named frame.

Observation base: 21 grid stills @60 s + 40 grid stills
@30 s + 19 targeted frames/crops + 4 sheets @2 fps
(267–282, 388–404, 92–110, 1150–1177) = **84 stills**,
plus per-second full-frame and primary-viewport motion
energy over all 35,311 frames, plus transcribed speech
slices (UNCONFIRMED tier; §1). Screen governs.

## §0 Safety-clause verdict (taken before Pass 1)

Depicted figures are the SFM elements `bonnie_male1` and
`bonnie1`: adult-proportioned FNAF animatronic robots in
every sampled frame (tall jointed robot bodies; the female
figure with breasts and purple lip/eye makeup — g01, g05,
s00015, s00105, g20). **Clause NOT triggered** — this run's
own capture concurs with Plan 18's finding of record
(full record in INTAKE.md).

## §1 Transcription record

- Route: chunked-transcription skill lane, **single pass**
  (1177 s < 3,600 s cap; chunk map: "single pass"),
  whisper.cpp large-v3-turbo, primo CPU, nice 19, `-t 2`
  (detach `ns19-whisper`). Primo was saturated by sibling
  jobs (11 whisper-cli processes live at check); at this
  run's close the full pass had reached ~0:01:06 and was
  still running — it lands in the primo plan dir on
  completion, as Plan 18's did.
- To bound speech claims inside this run, three targeted
  slices were transcribed on the same lane (`ns19-slices`):
  A = 0–150 s, B = 460–580 s, C = 1080–1177 s. Slice
  results and the loop census are recorded in the
  addendum at the end of this file when they land; every
  [SPEECH] claim below names its slice and span.
- Confirmed from the full pass's own log before slicing:
  speech EXISTS from the opening (narration at 0:39–1:06
  on map-entity drawing for lighting/render tests — §6
  C-02). The audio census alone (mean −30.4 dB) would have
  suggested near-silence; transcription is the verdict,
  per the Plan 12/18 lesson.

## §2 Session anatomy (screen, measured)

| # | Recording span | Share | Phase | Evidence |
|---|---|---|---|---|
| 1 | 0–25 s | 2.1% | **Intro + survey.** Post-edit credit overlay ("Edited with the help of @OpacityNSFW") over the SFM session; both figures in T-pose surveyed in the work camera (maximised at 15 s) | g01, s00015 |
| 2 | 25–477 s | 38.4% | **Posing/keying block A.** Channel-group passes over the parked shot (flex/ear ~105, length event ≤225, graph work ~211, pelvis ~245, feet 267–315, white-mode flight 388–404) | §3 log |
| 3 | 477–563 s | 7.3% | **Progressive-refinement phase.** Full-frame energy mean 0.014 (near-zero); the Progressive Refinement Settings dialog open at 495 and 555 (DOF # Samples override list to 1024; AO mode "AO Only"; at 555 the DOF override reads 1024); status bar at 546 reads "Sample: 413 of 1024" | s00495, s00555, t546; `records/motion-per-second.csv` |
| 4 | 564–1155 s | 50.2% | **Posing/keying block B.** Passes resume (survey 566; fingers in Graph Editor ~645; hand_R ~735; pelvis burst 844–870; fingers ~945; feet again ~1035; full-pose pass ~1125; fingers ~1145) | §3 log |
| 5 | 1155–1170 s | 1.3% | **Lit review.** Shot camera (camera1) shows the finished lit scene (dark, star decorations, floor reflections) over the parked act tableau; Motion Editor selection still open | t1160, tail sheet |
| 6 | 1170–1177.03 s | 0.6% | **Card.** "THANKS FOR WATCHING!" over the blurred session | g-tail, tail sheet |

Whole-file instruments: full-frame motion mean 0.961,
median 0.160; viewport-crop mean 2.771, median 0.263 —
a burst rhythm (parked inspection punctuated by camera
flights and gizmo work), never a sustained playback
rhythm (§4). Scene cuts at threshold 0.4: **zero**.

## §3 The variation event log (session world)

Counting rule (stated before counting): an EVENT is a
change, between adjacent observation points, of any of —
selected channel family, body region under work, editor
mode, shot-length state, viewport mode, session phase.
Each event is anchored to a named frame or measurement;
at 30 s base sampling these counts are **lower bounds**.

| ID | t (s) | Class | Event (what changed) | Anchor |
|---|---|---|---|---|
| E-01 | 0 | CARD | Recording opens under post-edit credit overlay over the session | g01 |
| E-02 | ~15 | CAMERA | Work camera maximised: full-body T-pose survey of both figures; camera attribute list open (fieldOfView, aperture, toneMap family) | s00015 |
| E-03 | ~92–110 | DWELL | Screen freezes on the female head close-up for ≥18 s (36/36 sheet frames identical) — narration dwell over a parked frame | earlystill sheet; energy run 92–110 < 0.05 |
| E-04 | ~105 | CHANNEL | bonnie1's **flex inventory** taken up in the Animation Set Editor: the Unknown list shows the SFW muscle/bulge family and the NSFW open/bulge flex family side by side; `bip_ear1_R` pos/rot selected | s00105 |
| E-05 | ≤225 | LENGTH | **Shot-length change: the timeline clip reads "duration 60.000" at 105 s and "duration 20.000" at 225 s** — the shot is cut to one-third (or the 60 s arrangement replaced by the 20 s shot) inside this window; the 20.000 s form is the one every later frame and both sibling instalments show | crops 105/225 |
| E-06 | ~200–220 | EDITOR | Graph Editor at deep zoom: dense channel lanes with a selection boundary; full-frame energy peaks at 211 (17.98, the file maximum) and 214 (11.54) — the session's most violent screen change is an editor/timeline operation, not scene motion | t211; motion CSV |
| E-07 | 225 | TIME | Playhead parked at shot-time **20.000** (shot end); both viewports black past the shot ("<No Current Shot>") — endpoint inspection | s00225 |
| E-08 | ~245 | POSE | Motion Editor, whole-shot green selection; work camera close behind the pair at the pelvis; bonnie_male1 RigBody (root/pelvis/hips/spine/neck/head) under work | g05 |
| E-09 | 267–282 | POSE+CAMERA | Feet pass with continuous work-camera flight around the legs/feet (resolved from the sustained-energy candidate window — camera + incremental foot posing, playhead parked) | candA sheet |
| E-10 | ~315 | POSE | Feet/toes close-up, bonnie1 RigLegs (knee/foot/toe L/R) | s00315 |
| E-11 | 388–404 | CAMERA | **Viewport shading-mode change:** the work camera flies the scene in a flat white unlit mode (lighting-preview class) — a diagnostic survey, bodies static | candB sheet |
| E-12 | 477 | FINISH | Progressive Refinement Settings dialog opens over the parked contact tableau (primary camera now camera1; timeline reads shot1, duration 20.000) | s00495 |
| E-13 | ~546 | FINISH | Refinement running at **1024 samples** (status: "Sample: 413 of 1024"); the screen shows a zoomed status view; full-frame energy blips once (8.87 at 546 — the zoom change) inside the near-zero phase | t546; motion CSV |
| E-14 | ~566 | CAMERA | Refinement done; wide survey of the posed pair (leader standing, arms out, over the crouched follower — the shot-time-0 tableau at this stage); camera1 selected | t566 |
| E-15 | ~645 | EDITOR+CHANNEL | Graph Editor: the **finger channel family** (RIG_bip_* pos/rot, both hands) under dense-key refinement — the timeline shows dense key lanes across the span | s00645 |
| E-16 | ~735 | POSE | bonnie1 `rig_hand_R` taken up in the Motion Editor; frontal work-camera survey of the pair | s00735 |
| E-17 | 844–870 | POSE | Session's largest viewport burst (27.31 at 844): close pelvis work, `rig_pelvis` pos/rot on bonnie_male1 | s00855; viewport CSV |
| E-18 | ~945 | POSE | Finger-level pass: LeftArm → Left_Fingers, `RIG_bip_index_2_L` selected; extreme close-up of the hand on the partner's head | s00945 |
| E-19 | ~1035 | POSE | **Feet again** — second feet pass, now the leader's (`rig_foot_1`, bonnie_male1 LeftLeg) | s01035 |
| E-20 | ~1125 | POSE | Whole-shot Motion Editor selection (green, full span); work camera behind the pair in the act pose — a full-pose pass | s01125 |
| E-21 | ~1145 | POSE | Finger-level posing in the primary viewport: hand planted on the partner, LeftArm finger controls listed, rotation gizmo on the hand | g20 |
| E-22 | ~1155 | FINISH | Lit review: camera1's shot view shows the finished lighting (dark scene, star decorations, reflective floor) over the parked tableau | t1160 |
| E-23 | ~1170 | CARD | "THANKS FOR WATCHING!" card over the blurred session (final ~7 s) | g-tail, tail sheet |

### Tallies (lower bounds at 30 s sampling)

| Class | Count | Events |
|---|---|---|
| POSE (region/family posing pass) | 8 | E-08, E-09*, E-10, E-16, E-17, E-18, E-19, E-20, E-21 — *E-09 counted once (POSE+CAMERA) → POSE total **9** incl. E-09 |
| CAMERA (survey / mode / flight) | 4 | E-02, E-09*, E-11, E-14 |
| CHANNEL (channel family taken up) | 2 | E-04 (flex), E-15* (fingers, with EDITOR) |
| EDITOR (mode change) | 2 | E-06 (graph), E-15* |
| FINISH (refinement / lit review) | 3 | E-12, E-13, E-22 |
| LENGTH (shot-length state) | 1 | E-05 |
| TIME (playhead state) | 1 | E-07 |
| DWELL (parked narration hold) | 1 | E-03 |
| CARD (publishing wrapper) | 2 | E-01, E-23 |
| **Total distinct events** | **23** | (E-09 and E-15 each carry two class tags; class tags sum to 25) |

**Duration economics:** 23 events / 19.62 min =
**11.7 events per 10 minutes** (1.17/min). Distribution:
posing events are spread across the whole session with no
dead zone longer than the refinement phase; FINISH events
cluster mid-session (477–563) and at the close
(1155–1170); the single LENGTH event is early (≤225 s,
inside the first 19% of the session); CHANNEL events sit
at ~105 and ~645 (the flex pass early, the finger-graph
pass just past the middle). The session's rhythm is
**steady rotation, not escalation**: no class concentrates
at a climax, because a working session has none — its
"peak" by screen energy is an editor operation (E-06).

## §4 The no-playback finding (measured, as in Plan 18)

The shot is never played through in this recording either:

1. **Playhead readouts:** every legible viewport readout
   in the 84-still base reads shot-time **0.000** or
   **20.000** — the two endpoints. The creator works from
   the endpoints inward.
2. **Candidate-window resolution:** the viewport-energy
   record admits exactly two ≥15 s sustained-motion
   windows (267–282, 388–404); both were resolved on 2 fps
   sheets as work-camera flights over parked bodies
   (candA/candB), not body-motion playback.
3. **Energy shape:** viewport median 0.263 with isolated
   bursts to 27.31 is the signature of parked inspection +
   camera/gizmo bursts; a 20 s playback anywhere in the
   file would appear as a sustained moderate window, and
   none exists.

Review method in this session = **parked-frame inspection
+ scrub fragments + camera flights + one progressive-
refinement still** — the series' consistent craft fact
(Plan 18: same finding over its finishing session).

## §5 SHOULD-BE-SEEN scored

Plan's expectation: *"Continuation of the series build:
variation strategy across a long take, secondary systems
(hair, soft-body, sound if any), and the creator's
review/fix loop at length."*

| Item | Verdict | Evidence |
|---|---|---|
| Variation across a long take | **NOT SEEN as framed** — there is no finished long take in the artefact; variation is SEEN at session level (§3) and distilled as such (TECHNIQUE) | INTAKE premise verdict |
| Secondary system: sound | **NOT SEEN** — no audio application (VEGAS/Audacity class) appears in any of the 84 sampled stills; the page's `sound` tag has no sampled referent in this instalment. (Plan 15's file does contain the series' VEGAS/Audacity break; the tag likely describes the series, not this sitting.) | full still base |
| Secondary system: hair | **NOT SEEN** — no hair system exists on these rigs in any sampled frame (rigid animatronic models) | full still base |
| Secondary system: soft-body / flex | **SEEN** — bonnie1's flex inventory (muscle/bulge/open families) is a named channel family taken up at ~105 s (E-04) | s00105 |
| Review/fix loop at length | **PARTIALLY SEEN** — review is continuous (parked inspection, camera flights, white-mode survey, a 1024-sample refinement still); no on-screen failure→fix moment is sampled in this instalment (contrast Plan 18's self-flagged bad rim light) | §2, §4 |
| Surprise (per protocol) | The premise again: duration (4.8×), type (session, not take), and the shot itself changed length mid-session (60→20) | INTAKE; E-05 |

## §6 Claims list (for Pass 2/3 disposition)

- **C-01** [SCREEN] One session, one shot: `tutorial.dmx`
  / `shot1`, two figures, one hallway set, for the whole
  1177 s; zero hard cuts at threshold 0.4.
- **C-02** [SPEECH 0:39–1:06, full-pass log] The session
  opens with rendering/lighting setup guidance: draw game
  (map) entities only when testing lighting or rendering,
  because they cost framerate and memory — setup discipline
  stated before posing begins.
- **C-03** [SCREEN + SPEECH 1:30–1:38, full-pass log] The
  shot's timeline duration reads 60.000 at 105 s and
  20.000 at 225 s and at every later read (495, 566,
  1160). The change is a **narrated decision**: discussing
  IK-rig lag (Unknown-section controls such as the ears
  cause a "massive massive framerate drop", 1:06–1:31 —
  the same ear controls selected in frame s00105), the
  creator states the fix in one line: "I'll make this a
  20 second animation" (1:31–1:38), then executes it in
  the Clip Editor (1:38–2:00): add a keyframe/bookmark
  and "shorten the whole thing down to those 20 seconds",
  noting the image-sequence render consequence. **This
  is the instalment's fix pass, logged as shown:**
  problem — laggy IK rig, worst on Unknown-section
  controls; fix — shorten the animation to 20 s in the
  Clip Editor (and the standing viewport discipline of
  C-02). The 20 s form is the series' settled shot
  length.
- **C-04** [SCREEN] All posing is hand-keyed: Motion Editor
  gizmo work and Graph Editor dense-key refinement; no
  procedural/automation tool is opened in any sampled
  frame; the only machine-driven process in the session
  is the progressive refinement render (E-12/E-13).
- **C-05** [SCREEN] The creator's variation unit is the
  **channel-group pass**: one family (flex, pelvis, feet,
  fingers, hand) is taken up, worked across the shot's
  span under a whole-shot time selection, and put down —
  9 POSE + 2 CHANNEL events, rotating for 19 minutes.
- **C-06** [SCREEN] Feet are passed **twice** (partner
  ~267–315, leader ~1035) and fingers at least three times
  (~645 graph, ~945, ~1145): small-part families recur —
  variation includes *returning* to a family late with the
  accumulated pose in place.
- **C-07** [SCREEN] Review never uses playback (§4):
  endpoints (0.000 / 20.000), camera flights, a white-mode
  diagnostic flight, and a 1024-sample progressive-
  refinement still (DOF override 1024, AO Only) are the
  review instruments.
- **C-08** [SCREEN] The finishing thread is present but
  compressed vs Plan 18: refinement still mid-session
  (477–563) + lit review at the close (1155–1170) ≈ 8.6%
  of this recording, against Plan 18's 93.8% finishing
  session — the same phase, at sitting scale.
- **C-09** [SCREEN] Publishing wrapper: credit overlay at
  the open (editor credit) and a single THANKS card at the
  close (~7 s) over the blurred session — a shorter tail
  than Plan 18's three-card 15 s sequence.

## §7 UNREADABLE register

| ID | Item | Why |
|---|---|---|
| U-1 | The finished shot's internal variation (pose/tempo/reaction changes across its 20 s) | The shot is never played (§4); only endpoint tableaux are displayed |
| U-2 | Whether E-05 was a trim of one clip or a shot swap | Both timeline reads name the session `shot1` in viewport headers; the clip's own name line is cut off in both crops at 720p |
| U-3 | Graph Editor numeric values (curve amplitudes, exact key times) at E-06/E-15 | Shapes and key density legible; axis scales not legible at 720p |
| U-4 | What the zoomed status view at ~546 s was (desktop zoom vs in-app preview zoom) | The frame shows a magnified status region; the zooming agent is not identifiable at 720p |
| U-5 | Narration outside the transcribed slices (until the full pass lands) | Slices A/B/C bound the speech claims; the remainder is UNCONFIRMED-pending, not absent |
| U-6 | Any fix pass the creator performed between sampled frames | 30 s sampling bounds the event log; sub-30 s fixes are below the sampling floor |

## Addendum — transcription state at filing (2026-11-06)

- Full pass (`ns19-whisper`) still running at filing;
  read span at filing: **0:00–2:00, 15 segments**, filed
  as `transcript-partial.txt` in this run dir. Every
  [SPEECH] claim above (C-02, C-03, V-8's evidence) traces
  to this span — the load-bearing narration (session
  framing, map-entity discipline, the IK-lag problem and
  the 20 s fix) sits inside it.
- Slices A/B/C (`ns19-slices`) were still in flight at
  filing under the same contention; they land in the
  primo plan dir (`slices/`) on completion. No claim in
  this run depends on them.
- Loop census: not run — the census operates on a
  completed stitched transcript (skill §5), and no
  completed transcript exists at filing. Recorded as an
  open item for the primo plan dir, not estimated: with
  15 segments read, any loop share would be fiction.
- When the full transcript lands, U-5 narrows; no other
  finding in this run is speech-dependent.
