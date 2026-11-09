# Plan 20 — Pass 1 Timed Observation

Artefact as captured (INTAKE.md): a 724.400 s Source
Filmmaker screen recording (21,732 frames @ 30 fps) — the
FIRST sitting of the 2021-03-19 `tutorial.dmx` build
(taskbar 11:26 AM → ~11:39 AM, immediately before Plan 19's
instalment). **World: SESSION** (INTAKE premise verdict).
The brief's observation focus — rig/constraint setup in
full, in Plan 01's observation terms — is exactly what this
segment contains: it is the only instalment of the four that
shows the rigs being CREATED. Blocking / contact setup /
first loop are NOT in this segment; where the comparison
needs them, the series record (Plans 15/18/19, same sitting)
carries them and OBSERVATION says so per claim.

Observation base: 24 grid stills @30 s (640 px) + 12 grid
stills @60 s (native 1280×720) = **36 stills**, plus
transcribed speech slices (UNCONFIRMED tier; §1). Screen
governs.

## §0 Safety-clause verdict (taken before Pass 1)

Depicted figures are the SFM elements `bonnie_male1` and
`bonnie1`: adult-proportioned FNAF animatronic robots in
every sampled frame (tall jointed robot bodies; the female
figure with breasts and purple lip/eye makeup — g003, g008,
grid60_05, grid60_12). **Clause NOT triggered** — this run's
own capture concurs with Plans 15/18/19's findings of record
(full record in INTAKE.md).

## §1 Transcription record

- Route: chunked-transcription skill lane, **single pass**
  (724 s < 3,600 s cap; chunk map: "single pass"),
  whisper.cpp large-v3-turbo, primo CPU, nice 19, `-t 2`
  (detach chain `ns20-slices` → `ns20-whisper`).
- Programme-wide contention at launch (~11 sibling whisper
  jobs; load ≈ 30–49 on 16 threads) throttled every job.
  Per the brief's slice-ladder provision, three targeted
  slices were queued FIRST on the same lane (`-t 1`):
  A = 0–150 s (opening / redo framing), B = 280–450 s
  (survey + rig-setup span), C = 560–724 s (rig finalisation
  + tail). The full pass runs behind them.
- Coverage at filing: recorded in the addendum at the end of
  this file when the slices land. Every [SPEECH] claim below
  names its slice and span. Loop census: NOT RUN unless the
  full transcript completes (a census of slices would be a
  false statistic) — recorded as an open mechanical step.
- Speech EXISTS from the opening (slice A, first segments):
  the creator frames this instalment as a REDO — "yesterday
  and I don't know the version I did it was just too long all
  over the place needlessly complicated. It was just a mess
  so I'm redoing it at least part one. I'm probably gonna
  make a…" [SPEECH, slice A ~0:09–0:27, UNCONFIRMED]. The
  series' tutorial posture (Plans 15/18/19) is therefore a
  second, tightened attempt — context for the method's
  economy, carried as speech-tier evidence only.

## §2 Session anatomy (screen)

Animation sets at the segment's start (Animation Set Editor,
g003, grid60_02, grid60_05):

- `bonnie_male1` — the viewpoint character (male Bonnie):
  Body group with the model's OWN bones — `rootTransform`,
  `bip_pelvis`, `bip_spine_0`, `bip_spine_1`, `bip_neck`,
  `bip_head` — plus Arms / Fingers / Legs / Unknown groups.
  These are model bones, not animation controls: before the
  rig pass there is no `rig_` anything in the session.
- `bonnie1` — the partner (female Bonnie): same structure;
  her Unknown group additionally carries the flex/model
  inventory the series record names (`bip_vagina`,
  `bip_breast_L/R`, etc. — Plan 15 OBSERVATION §2, from this
  same sitting's later spans; in THIS segment her flex
  inventory is visible as channel groups at ~105 s class
  frames, cf. Plan 19 E-04 which samples the same state).
- `camera1` — the session camera (this segment's set list
  shows `camera1` where Plan 15's later spans show
  `camera2` also present; the shot camera of record for the
  sitting is camera2 per Plan 15 C-03 — in this segment only
  camera1 is listed in the sampled frames).
- Lights: none yet in the sampled frames — lighting is a
  later-sitting phase (Plan 18's finishing pass).

Scene: the FNAF pizzeria hallway (checkerboard wainscot,
red/black check floor). Shot: "Tutorial / shot1". Every
legible playhead readout in the 36 stills is **0.000** — the
whole segment works on the parked frame-0 tableau (the
series' consistent discipline: Plans 18/19 §no-playback).

## §3 Structure of the 12 minutes (screen, 30 s + 60 s grids)

| Span (s) | What happens |
|---|---|
| 0–~30 | Opening: feet/toe close-up work in the work camera (g001: foot bones/channels selected, shot camera shows the hallway) — detail setup before the wide survey |
| ~30–150 | Survey: the female model alone in T-pose (g003), then both models side by side in T-pose (g008, grid60_02); rootTransform channels open (pos/rot) — placement/scale state inspected |
| ~150–300 | Continued survey + model detail: male figure from behind with transform gizmos (g012); channel-level work in the set editor (bip_ lists, Procedural panel visible: Zero/Half/One/Playhead/In/Out/Paste/Drop/Jitter/Smooth/Stagger/Hold) |
| ~300–420 | **Auto-Rigger pass 1** (g016 @ ~450 s class; grid60_08 @ ~420 s): Auto-Rigger V1.9 dialog, full bip_ mapping, **2 spine bones** selected (see §4) |
| ~420–540 | **Auto-Rigger pass 2** (grid60_09 @ ~480 s): the dialog again, mapping identical, **1 spine bone** selected — a per-figure rig difference (§4, with its ambiguity recorded) |
| ~540–660 | Rig sets live: both figures now carry `rig_` control groups (grid60_11 @ ~600 s: RigBody = rig_root/rig_pelvis/rig_hips/rig_spine_0/rig_spine_1/rig_neck/rig_head; RigLegs, RigArms, Unknown); first manipulation — gizmo on the male's `rig_pelvis` |
| ~660–724 | Rig finalisation (grid60_12 @ ~660 s): both figures in T-pose wearing visible rig-control widgets; context menu open on bonnie1's groups — Utilities submenu with **Bake Procedural Bones** highlighted (siblings: Reattach To Model, Rebuild Control Groups, Add Scale Control To Models); timeline shows the shot's dense channel lanes. A "HOME - CAT" overlay sits at the segment's late frames (g020) — a post-edit credit-class overlay, not technique |

## §4 The rig setup in full (brief focus 1 — Plan 01's terms)

Plan 01's observation terms for a rig are: what bones exist,
what constraints/locks exist, what is keyed vs solved, and
what the setup order is. In those terms, this segment
establishes the series' ENTIRE rig layer:

1. **There is no hand-built constraint setup.** The rig is
   GENERATED: the SFM **Auto-Rigger V1.9** script takes the
   model's bip_ bone names as inputs and emits a `rig_`
   control set. The full mapping, legible at native
   resolution in grid60_08 (and identically in grid60_09):
   - Head `bip_head` · Neck `bip_neck` · Pelvis `bip_pelvis`
   - boneUpperLegL/R `bip_hip_l/r` · boneCollarL/R
     `bip_collar_l/r` · boneLowerLegL/R `bip_knee_l/r` ·
     boneUpperArmL/R `bip_upperarm_l/r` · boneFootL/R
     `bip_foot_l/r` · boneLowerArmL/R `bip_lowerarm_l/r` ·
     boneToeL/R `bip_toe_l/r` · boneHandL/R `bip_hand_l/r`
   - Spine Options (radio): 4 / 3 / **2** / 1 spine bones —
     pass 1 selects **2 spine bones** (spine0 `bip_spine_0`,
     spine1 `bip_spine_1`; the spine2/spine3 dropdowns read
     `bip_LowerEyelid_l` — unused slots carrying a leftover
     default, recorded as seen); pass 2 selects **1 spine
     bone** (spine0 `bip_spine_0`; spine1 `bip_spine_1`
     greyed).
   - Misc options: "Toggle IK Chain Auto-Find" UNCHECKED;
     "use toe bones" ✓; "use collar bones" ✓; "add footroll"
     unchecked; "rig fingers" ✓. Buttons: "Load Rig Script",
     "Create Script".
2. **The generated control set** (grid60_11, both figures):
   RigBody (`rig_root`, `rig_pelvis`, `rig_hips`,
   `rig_spine_0`, `rig_spine_1`, `rig_neck`, `rig_head`),
   RigLegs, RigArms, Unknown. This is the control vocabulary
   every later instalment poses with (Plan 15 §2's session
   anatomy is this same list, one sitting later).
3. **Setup order** (the segment's own sequence): models in
   scene → survey/scale at rootTransform → Auto-Rigger per
   figure → rig manipulation begins (pelvis first) →
   procedural-bones bake at finalisation. Pose-before-rig is
   impossible here by construction: nothing is posed until
   the rig exists — the inverse of Plan 01's taught order
   (pose → constrain → Set Inverse), because Plan 01's rigs
   arrive pre-built and this series BUILDS its rigs on
   camera.
4. **What the rig is NOT:** no IK chains are auto-found
   (the toggle is off), no constraint is authored anywhere
   in the segment, and the aim constraints Plan 15 found on
   the partner's spine chain in later spans are NOT present
   yet in any sampled frame of this segment — they belong to
   the posing phase, not the rig phase. In Plan 01's terms:
   at the end of the base build, the series has FK-style
   `rig_` controls + model flex channels, and zero locks.
   Every lock-like behaviour in the finished scene is
   authored curves over these controls (Plan 15 C-04/C-11).

## §5 SHOULD-BE-SEEN scored

Plan's expectation: *"The base build: rigs, blocking,
contact setup, and the first full loop of the act the later
instalments extend."*

| Item | Verdict | Evidence |
|---|---|---|
| Rigs | **SEEN, in full** | §4: Auto-Rigger mapping, spine options, generated rig_ sets, bake step |
| Blocking | **NOT SEEN in this segment** | Both figures stand in T-pose for all 724 s; the all-fours blocking is built in the sitting's later spans (Plan 15 OBSERVATION §3: posing pass ~42–1500 s of ITS file) |
| Contact setup | **NOT SEEN in this segment** | No contact is posed; the segment ends at first rig manipulation. The series' contact method (dense authored keys + shot-camera verification) is Plan 15 C-04/C-11's record |
| First full loop | **NOT SEEN in this segment** | No cycle is keyed yet; the loop's dense-key construction is Plan 15 §3/C-04's record (~1 s period on rig_pelvis/rig_hips) |
| Surprise (per protocol) | The premise again: duration (4.24×), type (rig-creation segment, not a full build), and the redo framing — this published "base build" is a RE-build of a discarded first attempt [SPEECH slice A] | INTAKE; §1 |

## §6 Claims list (numbered; Pass 2/3 test list)

Provenance: [SCREEN] = the 36-still record; [SPEECH] =
transcript, UNCONFIRMED tier (§1). Series claims carried
from Plans 15/18/19 are marked [SERIES] with their home
claim IDs — they are evidence for the comparison, not
re-claims of this segment.

- **C-01** [SCREEN] Premise: this is a genuine tutorial
  segment — an SFM session building the scene's rigs from
  the raw models, with continuous narration, in the same
  `tutorial.dmx` session the whole series shares.
- **C-02** [SCREEN] Safety clause PASS: Bonnie the Bunny
  (FNAF) animatronic robots at adult proportions; no
  child-like or age-ambiguous figure in any of 36 stills.
- **C-03** [SCREEN] Pre-rig anatomy: both figures enter as
  model-bone sets (`rootTransform`, `bip_pelvis`,
  `bip_spine_0/1`, `bip_neck`, `bip_head` + Arms/Fingers/
  Legs/Unknown) — no `rig_` controls exist before the
  Auto-Rigger pass.
- **C-04** [SCREEN] The rig is generated by Auto-Rigger
  V1.9 from the bip_ name mapping in §4.1 — full table
  legible at native resolution (grid60_08/09).
- **C-05** [SCREEN] Spine configuration differs between
  the two sampled Auto-Rigger passes: 2 spine bones, then
  1 spine bone, mapping otherwise identical. (Which figure
  each pass rigged is UNREADABLE — U-1.)
- **C-06** [SCREEN] Rig options as set: IK Chain Auto-Find
  OFF; toe bones ON; collar bones ON; footroll OFF; rig
  fingers ON (§4.1).
- **C-07** [SCREEN] The generated control vocabulary is
  RigBody (rig_root/pelvis/hips/spine_0/spine_1/neck/head)
  + RigLegs + RigArms + Unknown, on both figures
  (grid60_11) — the same vocabulary Plan 15's session
  anatomy lists for the posing phase.
- **C-08** [SCREEN] Setup order: survey/scale at
  rootTransform → Auto-Rigger per figure → first
  manipulation at rig_pelvis → Bake Procedural Bones at
  finalisation (context menu, grid60_12).
- **C-09** [SCREEN] No constraint, lock, or IK setup is
  authored anywhere in this segment; playhead parked at
  0.000 in every legible readout (36 stills).
- **C-10** [SPEECH, slice A] The creator frames the
  instalment as a redo of a discarded, over-complicated
  first version ("I'm redoing it at least part one") — the
  series' method posture is economy-after-excess, stated
  by the creator at the segment's open.
- **C-11** [SERIES — Plan 15 C-04/C-05] The act's cycle is
  dense baked keys on rig_pelvis/rig_hips at ~1 s period;
  authoring order: select key parts, set loop length, pose
  the middle, key pelvis/hips in counter-phase.
- **C-12** [SERIES — Plan 15 C-09/C-11] Contact registration
  under motion is maintained by (a) the dense shared cycle
  keys and (b) continuous shot-camera verification while
  posing — there is no solver/constraint registration
  mechanism anywhere in the series' record.
- **C-13** [SERIES — Plan 15 §6] Blocking: partner on all
  fours (hands + knees planted), viewpoint character
  kneeling behind, hands on her back/hips — held for the
  whole sitting; Plan 15's central finding is that this
  blocking is what makes the POV sightline work.
- **C-14** [SERIES — Plan 15 C-07/C-09] Head/gaze: separate
  head/eye animation sets; head = sparse spline keys +
  weight-blended aim constraint; the shot camera rides the
  head (Child-Of-style lock in the estate rebuild).
- **C-15** [SERIES — Plan 19 TECHNIQUE §4] Series
  invariants: one session, one shot, one act, one
  arrangement; playhead discipline = endpoint inspection,
  never playback.

## §7 UNREADABLE register

| ID | Item | Why |
|---|---|---|
| U-1 | Which figure each Auto-Rigger pass rigged | The dialog names no target set; both passes show bonnie_male1's channel list behind the dialog at 720p. C-05 therefore claims the DIFFERENCE, not the assignment |
| U-2 | rootTransform_scale numeric values | Channel rows legible as names; values not legible at 720p in any sampled frame |
| U-3 | Narration outside the transcribed slices (until the full pass lands) | Slices A/B/C bound the speech claims; the remainder is UNCONFIRMED-pending, not absent |
| U-4 | Whether a second camera (camera2) exists in this segment's session state | Only camera1 is listed in sampled frames; Plan 15's later spans list camera2 — creation time of camera2 is below this segment's sampling |

## Addendum — transcription state at filing (2026-11-06)

- Slice ladder (`ns20-slices`, nice 19, `-t 1`) still
  running at filing under programme-wide contention
  (11–13 concurrent whisper jobs; load 28–49). Read span at
  filing: **slice A segments through ~1:31** (12 segments,
  streamed in `ns20-slices.log` on primo). Every [SPEECH]
  claim in this run (C-10; §1's redo framing) traces to
  inside that span.
- Slices B (280–450 s) and C (560–724 s) and the full
  single-pass transcription (`ns20-whisper`, `-t 2`) are
  queued behind slice A on the same detached chain and land
  in the primo plan dir (`slices/`, `transcript.*`) on
  completion. No claim in this run depends on them.
- Loop census: not run — the census operates on a completed
  transcript (skill §5), and none exists at filing. With 12
  segments read, any loop share would be fiction.
- When the full transcript lands, U-3 narrows; no other
  finding in this run is speech-dependent (the rig record
  is entirely screen-carried).
