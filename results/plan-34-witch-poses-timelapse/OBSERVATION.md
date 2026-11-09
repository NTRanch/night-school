# Plan 34 — Pass 1 Observation (Decision Log)

Plan: `repo/plans/34-witch-poses-timelapse.md`
Intake: `runs/plan-34/INTAKE.md` (Pass 0; SHOULD-BE-SEEN
adopted verbatim from the plan, written before viewing).
Capture: `runs/plan-34/MANIFEST.md`; canonical media on primo
at `~/.local/share/pax/night-school/plan-34/plan34-source-720p.mp4`
(261,605,970 B, SHA-256
7eabbadfe6612446b3f69942dc0005c31a77b419991b1bf316ceed8b550b268f).

## Media and transcript of record

- Media: h264 1282×720 @60 fps + AAC 48 kHz stereo, duration
  **904.400 s (15:04.4)** — ffprobe. The plan's stated 15:04
  and the page's PT0H15M04S both verify against the file
  (0.4 s container tail). Decode clean (ffmpeg null pass,
  rc=0, no error output); packet span 0.000 → 904.367 s.
- Tool on screen: **DAZ Studio 4.21 Pro** [SCREEN, title bar
  in every frame], figure **Genesis 8 Female** (untextured
  silver-grey viewport shading throughout), outfit/prop set
  "Charming Witch" (Pretty3D), second subject **Daz House
  Cat**. A witch-silhouette poster (moon, cat on broom) is
  pinned as a picture-in-picture reference in the lower right
  for the entire session [SCREEN, all frames].
- Frames in `runs/plan-34/frames/`: 90 grid frames every 10 s
  (`grid/g0001…g0090`, t=(n−1)×10 s) + 74 targeted native-res
  frames every 10 s over t=40–390 and t=490–860
  (`native/n<t>.jpg`), read as viewport + Scene-pane crops
  (crop-sheets 1–13). The Scene pane's yellow node highlight
  is this log's primary evidence: it names the exact node(s)
  the artist has selected at each sampled instant. The screen
  governs; there is no narration to cross-check (below).
- Audio census: AAC track is loud (volumedetect mean
  −10.4 dB, max 0.0 dB) — not silent. Bounded whisper slices
  (3 × 30 s at t=60/450/840, large-v3-turbo, primo): slice
  t=60 transcribed as **song lyrics** ("With someone else's
  mind / He moves and touches like a treat … I just wanna
  kiss you, baby / Tough decision") — a music track with
  vocals, not artist commentary. Remaining slices and the
  final no-commentary verdict are recorded in MANIFEST.md.
  SHOULD-BE-SEEN's "commentary absent" holds for slice 1;
  the plan's premise otherwise HOLDS with one correction
  (§1).

## 1. What this video actually is — premise check

The plan expects "a set of character poses" built in
sequence. What the screen shows is more specific and more
valuable: **one hero pose built from scratch, then turned
into a pose LIBRARY (full preset + partial-chain presets +
prop preset + camera presets), then a second subject posed
against it.** Segmentation (boundaries by subject/artifact
change + frame evidence):

| Unit | Window (video t) | What happens |
|---|---|---|
| S0 Setup | 0–~75 s | Figure load, reference poster pinned, Charming Witch outfit/prop items loaded and fitted (hat, underwear, broom) |
| **A — Broom-sit construction** | ~80–360 s | The one from-scratch pose: seated on the broom, built chain by chain (§2) |
| L1 Library capture | ~370–480 s | Save folder created ("Patreonposesaves", t=390 Explorer); full pose saved as `witch poses one.duf`; partial (arm/hand chain) preset saved via node-subset save dialog (t=450–470) |
| **B — Library re-application** | ~490–670 s | Figure reset; full preset + `witch poses partial hand pose one` re-applied via node selection (t=530–580); camera preset + broom preset saved/applied (t=590–630); a cylinder primitive ("hypothetical", t=640–670) used as a stand-in prop to test placement |
| **C — Cat companion** | ~680–860 s | Daz House Cat loaded onto the broom head; posed chain by chain; the witch's right hand/fingers are RE-posed onto the cat (cross-subject revision, t=820–830); cat face morphs last (t=840–850) |
| F Final save | ~860–904 s | Scene/group saved over the Sexywitchposes folder (save dialog t=860 lists the artifact set, §4); timeline panel open |

So "poses" for the decision log = construction units
**A, B, C** (B is a pose build whose gross order is executed
by preset, with manual partial-chain work on top). Counts
below are sampled at 10 s: they are **floors** — touches
that begin and end between samples are UNREADABLE by
construction (§6).

## 2. Pose A — Broom-sit: first-touch order (named-node evidence)

| # | Chain first touched | t (s) | Evidence [SCREEN, native frame] |
|---|---|---|---|
| 1 | **Props/outfit** (hat → underwear → broom at feet) | 50–70 | n50: "Charming Witch Hat" selected, hat gizmo on head; n60/n70: "Charming Witch Underwear" selected; broom gizmo at feet n70 |
| 2 | **Legs** — Left Thigh Bend | 80 | n80: Scene highlight "Left Thigh Bend"; thigh rotation gizmo, leg swinging forward. First BONE touched is a thigh, not the hip/root |
| 3 | **Pelvis + leg block** (as preset selection) | 130–140 | n120: library "Base Pose Sitting B" highlighted + Reading-asset dialog; n130: "Pelvis" selected; n140: Pose Preset Load Options (Nodes: Selected) with Pelvis + L Thigh Bend/Twist + L Shin + R Thigh Bend selected — a stock sitting preset applied to the leg/pelvis block only |
| 4 | **Spine/chest** — Chest Upper | 150 | n150: "Chest Upper" selected, torso gizmo on seated figure |
| 5 | **Head/neck** — Neck Lower, Neck Upper, Head | 160 | n160: three-node yellow block Neck Lower/Upper + Head; head gizmo |
| 6 | **Feet** — Left Foot, then Right Foot | 170, 190 | n170 "Left Foot"; n190 "Right Foot" (Left Shin revisit between, n180) |
| 7 | **Arms** — Collar + Shoulder block (L+R) | 210 | n210: Left Collar, Left Shoulder Bend, Right Collar, Right Shoulder Bend selected; same frame opens Create New Camera |
| 8 | **Hands/fingers** — via PowerPose hand diagram | 280–300 | n280/n290: hand-joint diagram pane open; finger gizmo work, hand at hip; n300 back view, hand behind back |
| 9 | **Prop contact final** — Broom repositioned under body | 310 | n310: "Charming Witch Broom" selected, broom gizmo at pelvis/legs, front view |

First-touch sequence A: **Props → Legs → Pelvis(block) →
Chest → Head → Feet → Arms → Hands → Prop-contact.**
Note what is NOT first: the hip/root translation and the
spine — the estate's assumed starting pair. The seat is
established by the LEGS (thigh bend) plus a preset pelvis,
and the broom is placed under the result at the end.

## 3. Pose A — revisits and reading distance

Revisit = chain selected again in a later sampled frame
after a different chain intervened (sampled floors):

| Chain | First | Revisit(s) | Count |
|---|---|---|---|
| Legs (shin) | 80–140 | Left Shin n180 (after head) | 1 |
| Spine/chest | 150 | Chest Lower n200 (after feet) | 1 |
| Arms (collar/shoulder) | 210 | shoulder gizmo work n260; Left Collar n330 (after broom) | 2 |
| Hands | 280–300 | contact close-ups n340, n350, n360 (hand flat on thigh, checked from back and side) | 1 episode (3 sampled frames) |
| Broom (prop) | 50–70 | reposition n310 | 1 |
| Head, feet, pelvis | — | none sampled after their blocks | 0 |

**Total sampled revisit episodes in A: 6.**

Reading-distance behaviour in A (sampled full-figure reads:
figure shown whole, no active close-up): t=90 front full
(root check), t=220 side full through Camera (2), t=230 top
view through Camera (4), t=240 camera side + top inset,
t=250 side profile ("Camera for our scene"), t=330 full
side on the finished broom = **6 full reads**, PLUS a
persistent second viewport: from t=260 to t=310 a small
auxiliary view shows the full seated pose while the main
view works close (n260, n270, n280, n290, n300) = **5 inset
reads**. The camera block (t=210–250, four cameras created:
Camera (2), (3), (4), "Camera for our scene") sits BETWEEN
the arm block and the hand block — the pose is read at
distance, from several angles, before any finger work.

## 4. The library (L1 + B) — the session's second technique

- Save dialog t=450–470 (Pose Preset Save Options): the
  node checklist shows the LEFT ARM CHAIN being saved as a
  subset — Left Collar, Left Shoulder Bend/Twist, Left
  Forearm Bend, Left Hand, Left Thumb 1… — i.e. a **partial
  preset** is a chain-scoped artifact, saved deliberately.
- Artifact inventory [SCREEN n550 tooltip + n860 save
  dialog, Sexywitchposes folder]: `witch poses one.duf`
  (preset_pose, 14–15 KB, created Thu 28 Mar 2024 16:51,
  author shadowyartsdirty), `witch poses partial hand pose
  one.duf` (14 KB), `camera pose preset` (1 KB), broom pose
  preset (1 KB), default camera pose preset (1 KB).
- Re-application mechanics [SCREEN n530–n580]: figure reset
  to standing; the partial is applied by SELECTING the
  chain in the Scene pane (n540: yellow block Left Collar →
  Left Shoulder Bend/Twist → Left Forearm Bend/Twist → Left
  Hand → Left Thumb 1/2) and loading with Nodes: Selected.
  The selection order in the pane is proximal→distal —
  collar first, fingers last — the same gross→fine
  direction as the from-scratch build.
- The cylinder episode [SCREEN n640–n670]: a Cylinder
  primitive is created and renamed ("hypothetical") and
  laid on the ground before the seated figure — a cheap
  stand-in used to test prop placement/camera before
  committing the real prop preset. (Read: proxy-prop
  rehearsal; marked as read, the rename is the evidence.)

## 5. Pose C — Cat: first-touch order

| # | Chain | t (s) | Evidence |
|---|---|---|---|
| 1 | Cat root/group placement on broom head | 690–710 | n690 "Daz House Cat" selected, root gizmo at broom crystal; n710 "Group for the cat" |
| 2 | Torso/head block — Chest, Neck, lShldr, rShldr (selection block) | 720–730 | n720/n730 yellow block Chest + Neck + lShldr + rShldr; "Turn Around" stock preset highlighted in library |
| 3 | Hip | 740 | n740 "Hip" selected |
| 4 | Leg — rThigh (via Pose Preset Load Options, Nodes: Root) | 750–770 | n750 load-options dialog + rThigh; n760/n770 paw-on-crystal close-ups |
| 5 | Shoulder — rShldr | 780 | n780 "rShldr" |
| 6 | Forepaw — rWrist | 790–800 | n790/n800 "rWrist" (cat IK chain); tooltip "Daz House Cat : Head" n800 |
| 7 | Tail (secondary) | 810 | n810 "Tail6" selected, tail gizmo |
| 8 | **Witch cross-revision**: right hand + Right Mid 1/2/3 fingers onto cat | 820–830 | n820 hand close-up on cat's back; n830 finger nodes yellow + PowerPose hand diagram |
| 9 | Cat face/head morphs | 840–850 | n840 face close-up, hand draped over cat; grid g85: Head shaping sliders |

Cat first-touch sequence: **Root → Chest/Neck/Shoulders →
Hip → Leg → Shoulder → Paw → Tail → (partner's hand) →
Face.** Deviations from A: the torso/head block comes
BEFORE hip/legs (A: legs first, head fifth), and the face
is dead last (A: no face work at all — the witch's head is
posed at step 5 and her expression is never touched in any
sampled frame).

Reading distance in C: full-composition reads at n700
(front), n790–800 (wide) = 2 sampled, plus constant
reference-poster presence. In B: camera-preset reads
n590–n620 = 4 sampled full views.

## 6. UNREADABLE accounting

- Sampling: 164 frames read (90 grid + 74 targeted). At
  timelapse speed each 10 s sample interval contains
  minutes of real work: individual slider drags, undo/redo,
  and any chain touched and left inside one interval are
  UNREADABLE. All first-touch times are therefore "first
  SAMPLED touch"; all revisit counts are floors.
- Chains never sampled as selected in A: abdomen nodes
  (visible in lists, never highlighted), eyes, toes as
  individual selections (feet were), individual finger
  nodes in A (fingers were worked via the PowerPose hand
  diagram, whose per-joint dots are below readable
  resolution in the crops — the hand BLOCK is readable,
  per-finger order inside it is UNREADABLE in A; in C the
  witch's Right Mid 1/2/3 selection at n830 IS readable).
- The witch's expression/face morphs: never sampled —
  recorded as "not observed", not "absent" (could have
  happened inside an interval; no frame shows a face pane
  for the witch).
- Exact preset contents (which nodes `witch poses one`
  carries) are UNREADABLE from the screen beyond the save/
  load selection blocks actually shown.

## 7. Claims list (for Pass 3 verification)

- **C-34-1** A repeatable posing order exists and is
  legs-early / hands-late: Props → Legs → Pelvis → Chest →
  Head → Feet → Arms → Hands → Contact.
- **C-34-2** Revisions are triggered by nameable checks
  (contact, camera read, new subject), not free taste.
- **C-34-3** A mid-build multi-angle camera read (before
  hands) is part of the order, not an afterthought.
- **C-34-4** Poses are captured as chain-scoped partial
  presets (proximal→distal selection) and re-applied by
  selection — the library is built during the session, not
  after it.
- **C-34-5** Contact is the terminal check: hands and paws
  are finished against what they touch (thigh, broom,
  cat), in close-up, after the camera read.
