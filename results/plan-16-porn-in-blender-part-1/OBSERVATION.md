# Plan 16 — Pass 1 Observation

Plan: `repo/plans/16-porn-in-blender-part-1.md`
Intake: `runs/plan-16/INTAKE.md` (Pass 0; SHOULD-BE-SEEN adopted
verbatim from the plan, written before viewing).
Capture: `runs/plan-16/MANIFEST.md`; canonical media on primo at
`~/.local/share/pax/night-school/plan-16/plan16-source-720p.mp4`
(432,178,972 B, SHA-256
fd0277d2f95106cee7b4d198123319ca96eae0b2594e6dca685bd7e61b6f8e6b).

## Media and transcript of record

- Media: h264 1280×720 @ 30 fps + AAC, duration 1668.074 s
  (27:48.07) — ffprobe, primo detach log `ns16-dl.log`;
  matches the watch page (PT0H27M48S). **The plan's stated
  duration (1:14:03) is an intake error** — see INTAKE.md.
- Frames: 14 grid frames every 120 s from t=0
  (`runs/plan-16/frames/`, g001–g014), 14 targeted frames at
  t = 60…1620 s (`runs/plan-16/frames60/`), 4 native-resolution
  panel crops (`frames/crops/`) — 32 files. Frame index at
  the end of this file.
- Transcript: single-pass lane (1,668 s < the 3,600 s cap,
  so no chunking; chunk map: one chunk, 0–1668.074 s) —
  whisper-cli (whisper.cpp 1.9.2, OpenChatCut bundled),
  model ggml-large-v3-turbo, primo CPU, 8 threads (a first
  2-thread run was killed at 294 s of audio for pace under
  wave contention and restarted at 8 threads; the shipped
  transcript is the 8-thread run alone, primo detach log
  `ns16-whisper2.log`, done rc=0). Stitch verify: **284
  segments**; last in-range segment end 1667.36 s ≤ media
  duration 1668.074 s — PASS, with one flagged exception:
  the single terminal segment ("Thank you.", 27:47.36→
  27:48.36) overshoots the media by **0.286 s** (a whisper
  end-estimate, the Plan 02 terminal-segment pattern at
  smaller scale). Loop census (rule normalized-segment-v1,
  output in `loop-census.txt`): **284 segments, 15 loop
  segments = 5.3% loop share, recoverable share 94.7%**
  (269 segments), 1 loop phrase ("I'm not going to be
  exact" — the creator does repeat the thought, and whisper
  loops it further over the hands passage; counted, not
  deleted). Tier: single-transcriber, **UNCONFIRMED**. The
  screen governs: every setting below is tagged [SCREEN],
  [SPEECH], or [BOTH]. Whisper name renderings are
  normalised only where the screen decides them (Domina,
  DAZ, Diffeomorphic, Reallusion); one rendering stays
  unresolved — see UNREADABLE 3.

## What this video actually is

A single-session, narrated Part 1 of a two-part Blender course
by **Divinity Studio**, in **Blender 5.0.1** [SCREEN, title bar
in every Blender frame]. The session has two halves:

1. **A browser survey of the tool landscape** (≈0:00–9:30):
   the creator walks vendor/documentation pages — Houdini,
   the Diffeomorphic DAZ Importer, drawing tablets, Character
   Creator — before touching Blender.
2. **A single-character setup-and-pose session** (≈9:30–27:48):
   a SmutBase model (Domina, Overwatch) is opened in Blender,
   its DAZ-importer rig is oriented, ONE pose is built at
   frame 0 with IK controls and pole targets, a camera is
   placed (50 mm), fingers are conformed to the thigh, and
   the character's robot-arm prop is posed last.

**Premise check against the plan:** the plan scopes Part 1 as
"scene and model setup through posing/animation
fundamentals". Setup and posing ARE the content. **Animation
fundamentals are NOT in Part 1**: in every Blender frame the
timeline sits at frame 0 (Start 0, End 250, the default), no
keyframe is ever set, and there is no second character, no
contact work, no lighting build, and no render. Those belong
to Part 2 (Plan 17, not yet run) — every comparison row that
needs them is marked PART-2-PENDING in TECHNIQUE.md rather
than scored from absence. The video is a genuine workflow
course (contrast the shelf's mislabel cases); it is simply
half of one — Part 1 of 2, as titled.

## Timed record

### 1. Tool-landscape survey, in the browser (≈0:00–9:30)

- **Houdini** (≈0:00–2:00): the SideFX homepage / Houdini
  Learning Portal is shown [SCREEN g001, t60]. Browser tabs
  open in the session: Gmail ("divinitystudiox@"), a
  "diffeomorphic" Google search, SmutBase, a Blender search,
  "Buy Autodesk Maya 2026", a Houdini product page [SCREEN
  g001 tab bar].
- **DAZ Importer (Diffeomorphic)** (≈2:00–4:00): the add-on's
  Bitbucket wiki — "DAZ Importer. The DAZ Importer is a
  Blender add-on for importing native DAZ Studio files
  (.duf, .dsf) into Blender. It also contains some tools to
  make the assets more animation friendly." Download links:
  **Stable version 5.0.0**; quick instructions (save zip,
  copy Scripts folder to a DAZ directory, set up menus in
  DAZ Studio, save DAZ root paths) [SCREEN g002, t180].
- **Drawing tablet** (≈4:00–6:00): Google shopping results
  for "wacom pad" — Wacom Intuos $39.95, Intuos Bluetooth
  $64.95 (sale), XPPen Artist 13.3 Pro $195.99, Wacom Cintiq
  16 $564.95, Huion Kamvas 13 $179.00 [SCREEN g003, t300].
- **Character Creator 5** (≈6:00–8:00): the Reallusion
  product page — "CHARACTERIZE ANY ACTOR TO CC… Any rigged
  biped models can be imported, characterized, and facial
  rigged in Character Creator" [SCREEN g004, t420].
- **Model sourcing** (≈8:00–9:30): SmutBase project page for
  **Domina 1.0** (Overwatch): `Domina_textures.zip`
  79.55 MB, `Domina_1.0.2.zip` 22.65 MB, `Domina_1.0.1.zip`
  22.64 MB, `Domina_1.0.0.zip` 22.6 MB, each with a Checksums
  button [SCREEN g005, t540]. (An Excalidraw whiteboard tab
  and a ZBrush page tab are also open in this stretch
  [SCREEN t300 tab bar].)
- What the narration RECOMMENDS from this survey (vs merely
  shows) is carried in §8's claims — [SPEECH] items pending
  the transcript of record.

### 2. Blender setup: the DAZ-imported rig (≈9:30–13:00)

- The worked file is `Domina_1.0.1.blend` (title bar path:
  `E:\Divinity.Studio\chars\Domina\`) in **Blender 5.0.1**
  [SCREEN g006+].
- Preferences → Add-ons is opened on the **DAZ Importer**:
  enabled, **Version 5.0.0**, maintainer Thomas Larsson,
  website bitbucket.org, settings directory
  `C:\Users\George Bonny\Documents\DAZ Importer`, "Rigging
  Tools" feature unchecked [SCREEN g006, t660 + crop]. Also
  enabled: BioVision Motion Capture (BVH) format, BlenderKit
  Online Asset Library, Cycles Render Engine [SCREEN g006].
  (The BVH and BlenderKit add-ons are never used on screen
  in Part 1.)
- Scene structure the model file ships [SCREEN g006 outliner]:
  collection `CH-Domina` → `Domina-rig` (children:
  `Domina-widgets`, `Domina-physics`, `META-Domina`,
  `RIG-Domina`), `Domina-geometry`, `PR-Domina`,
  `PR-Domina-Weapon`, and two lights, `Rim1` and `Sun` —
  **the file arrives with a rim light and a sun already in
  it; no light is placed or tuned in Part 1.**
- Mesh census of record: "Domina Nude Body | RIG-Domina |
  Verts: 42,135 | Faces: 43,815 | Tris: 82,560 | Objects:
  0/29" [SCREEN g006 status bar]; later "Bones: 1/1,870"
  [SCREEN g012 status bar] — a 1,870-bone DAZ/MHX-class rig.
- The rig's UI panel (viewport sidebar) [SCREEN g007, t780 +
  crop]: outfit/accessory toggles — Skirt: None; Shins ✓;
  Heels ✓; Steel Plate ✓; Arms: Left Bracelet ✓, Right
  Bracelet (Extra) ☐, Ring ✓; Body: "Futa (Replace body)",
  Long Nails ✓; Accessories: Sports Panties: None, Sports
  Bra: None, Stockings ✓, Garterbelt: Curvy (value 1),
  Strap ✓; Pants: None; a Face section; Bone Collections;
  **IK: IK Controls, IK Secondary, Spine IK Secondary;
  FK: FK Controls.** Rig custom properties include
  `cloudrig_ui` and `generation_date 2026-2-22` [SCREEN
  g012] — the rig UI is CloudRig-generated.
- The armature OBJECT sits at the origin with identity
  transform in every frame: Location 0/0/0, Rotation 0°,
  Scale 1.000 [SCREEN g006–g014 properties]. The model is
  never moved as an object; all work is Pose Mode bone work.

### 3. Posing: one pose, gross to fine (≈13:00–27:48)

- Posing opens on the torso: Pose Mode, bone
  `TORSO-Spine1` grabbed with G — D: Dx 0.002312 m,
  Dy −0.03152 m, Dz −0.05077 m (0.05981 m) [SCREEN g008,
  t900]. A rig note floats in the viewport: **"UI disabled
  for posing performance"** [SCREEN g008] — the rig's own
  performance mode while posing.
- The pose is built seated, legs together and raised, over
  ≈14:00–19:00: torso/spine first, then limbs via the IK
  controls; fine moves use **Shift** held during Move
  (Move X 0.036851 m, Local orientation) [SCREEN g009,
  t1020].
- **IK pole placement** is its own step: `POLE-UpperArm.L`
  moved in Global orientation — X −0.049585 m,
  Y −0.036696 m, Z −0.568511 m [SCREEN g010, t1140].
- **Camera** (≈20:00–22:00): a Camera object is added and
  the layout splits into Camera Perspective + Top
  Orthographic views. Camera of record [SCREEN g011, t1260
  + crop]: **Focal Length 50 mm**, Clip Start 0.001 m /
  End 1000 m, Location (−0.2094, −2.8432, 1.1063) m,
  Rotation X 90.491° / Y 0° / Z 0°; 3D Cursor at
  (0.6515, −1.759, 0) m. Posing continues INSIDE the split
  camera/user view for the rest of the session.
- **Fingers last** (≈24:00–26:00): close-up on the left hand
  resting on the thigh — fingers conformed to the thigh
  surface, `IK-Wrist.L` active, Move Y 0.009264 m in
  **Local** orientation [SCREEN g013, t1500 + crop].
- **Prop last of all** (≈26:00–27:48): the character's robot
  arm (`IK-Robot_Wrist.L`) is posed — Move X 0.07352 m,
  Y −0.068301 m, Z −0.026704 m, Global [SCREEN g014, t1620].
- The timeline never leaves frame 0; no auto-key state, no
  dopesheet, no graph editor, and no marker appears in any
  frame. The deliverable of Part 1 is the posed, framed
  still-in-waiting — animation is Part 2's subject.

### 4. The narration's own account (speech of record)

- **Course shape** [SPEECH]: "This will be a two-part
  tutorial on how to make NSFW art with Blender… for
  beginners, of course not complete beginners, you have to
  have some familiarity with Blender." The intro promises
  the pair's arc — "we'll download a 3D model, bring it to
  Blender, set up a lighting scenario" — and the close
  assigns the halves: "So, that's it for part one. Part two
  will set up the lighting. Have optimized render settings
  and do a little post processing." [SPEECH 27:30–27:42]
- **Why Blender** [SPEECH]: Houdini is "a node-based
  application, characterized by having a steep learning
  curve… used in Hollywood"; Maya is "an industry standard…
  like Blender's big brother"; Blender is chosen because it
  is "free, of course. No subscription, no account." Version:
  "we'll be using Blender 5.0, which is the latest version,
  as of this recording" [SPEECH; SCREEN 5.0.1].
- **Diffeomorphic is a hard prerequisite** [BOTH]: "we'll be
  using a very important plugin called Diffiomorphic…
  because the model will download off the internet, needs
  this installed in Blender. It won't work without
  Diffiomorphic, so it's really important. The installation
  for this is quite involved. I'll leave a link in the
  description to another video made by someone else who
  explained how to install this." Install is outsourced, not
  taught.
- **Three ways to source a character** [SPEECH, pages
  SCREEN]: (1) **From scratch** — a sculpting tool like
  ZBrush and "a tablet of some sort"; "the hardest way…
  a significant time investment… not something you can
  learn over the weekend." (2) **Character-creation
  software** — MetaHuman ("typically used with the Unreal
  Engine… high fidelity"), Character Creator 5 ("costs
  money, I believe, but there's a free trial"), and DAZ
  Studio ("what's primarily used with NSFW art. This is the
  main one… and DAZ is free") — "You're not creating
  characters from scratch. You're using sliders, knobs… a
  friendly user interface"; DAZ characters are exported to
  Blender through Diffeomorphic. (3) **Download ready-made**
  — "one such site is SmutBase… if you're just getting
  started, this is probably the recommended way… later on,
  when you get more skilled, you'll want to create
  characters from scratch… you could just use other
  people's models to practice animation lighting."
- **Opening the model** [SPEECH]: "Inside the zip file
  should be a blend file. You open up Blender, and then you
  open up the file. You'll be presented with this. **You
  should allow execution. It's just a Python script that
  allows the rig to work.**" Then: "Typically when I
  download models, I'll save a copy. In case I make changes
  that messes up the file. This is completely optional."
- **Rig-type self-correction** [SPEECH]: he first places the
  rig in the MHX family — "it comes with the MHX Runtime
  System. That's the type of rig that this model uses" —
  then corrects himself in the same breath: "Wait. No,
  that's not right. Actually, no, it doesn't use MHX. It
  uses something else. It uses the Cloud Rig, but MHX comes
  with the Daz Importer." The screen agrees (cloudrig_ui
  custom property, §2): **CloudRig** is the rig of record.
- **Posing doctrine** [SPEECH]: "We want to recreate
  this. We see that the character is seated with her head
  tilted, right? **When we pose a character, we want to
  move the torso first. Then the limbs.** I mean, that's
  how I do it, at least." Approximation is doctrine, stated
  repeatedly: "What we make won't be exactly a replication
  of this… It's just a tutorial"; "If I were to exactly
  replicate the reference, the tour [tutorial] will be a
  lot longer."
- **Symmetry as a toggle, not a rule** [BOTH]: X-Mirror is
  switched ON to move both hands with one control ("We have
  three things selected, but we're moving six things. See
  how convenient that is"), then OFF for the legs ("The
  symmetry thing is still on, so we have to turn that off"),
  reactivated for the hands ("I'll reactivate symmetry
  again. I'll move both hands"), and enabled again for the
  robot wrists at the end. No asymmetry principle is ever
  stated.
- **Camera doctrine** [BOTH]: after the gross pose, he goes
  to Object Mode (Ctrl+Tab), splits the editor into two
  panes, creates a camera, and enables **Camera to View**:
  "We want to see what the camera sees. When we make
  changes… we want the camera to move around too… As I'm
  posing the character, I could look at the other pane and
  see what I'm doing. To see how I'll get an idea of the
  final render for the camera."
- **Camera-occlusion tolerance** [SPEECH]: of the far hand
  — "Because of how the camera is positioned, we won't see
  her [right] hand. So, it doesn't really matter what we
  do… I think in the reference, we see both hands. But,
  you know, again, this is a tutorial. We just want to take
  some shortcuts."
- **Fingers by hand, on purpose** [SPEECH]: "There's
  probably something in here that will make posing their
  fingers a whole lot easier. But, you know, there's so
  many options here. I'd rather just do it manually… We
  want the hand to look like it's on the fly [sic — see
  UNREADABLE 3]. It's not going to be perfect, but as long
  as it looks convincing."
- **Orientation teaching** [SPEECH]: "There's global and
  local space… Local is different. It moves along its own
  axis. So, you'll often find yourself switching between
  those." — stated while tilting the head toward the camera
  (rotation along Z).

## Order of operations (the plan's primary extraction)

Each step with its evidence. [S] = screen frame, [T] =
transcript passage. Part 2 steps are the creator's announced
plan, not observation.

1. **Choose the DCC: Blender** (free, no subscription /
   account), version 5.0 — [T intro; S title bar 5.0.1].
2. **Install the Diffeomorphic (DAZ Importer) add-on** —
   a hard prerequisite for downloaded DAZ models; install
   itself is delegated to another creator's video — [T;
   S g002 wiki, g006 add-on panel v5.0.0].
3. **Survey character sources and pick the beginner route**:
   scratch (ZBrush + tablet) vs character-creator software
   (MetaHuman / Character Creator 5 / DAZ Studio) vs
   download — download recommended for beginners — [T;
   S g001–g004 pages].
4. **Download the model AND its textures** from SmutBase
   (Domina: model zip, latest version, + textures zip —
   "You need both of them") — [T; S g005 download list].
5. **Open the .blend and allow Python execution** so the
   rig's script (its UI) runs — [T; S rig UI live in g006+].
6. **Save a working copy** of the downloaded file before
   changing anything (stated habit, "completely optional")
   — [T].
7. **Verify the DAZ Importer is enabled** in Preferences →
   Add-ons ("Otherwise, it won't work") — [T; S g006].
8. **Configure the character in the rig UI**: outfit and
   accessory toggles (earrings/headset off, stockings,
   garterbelt, coat, wings, jewelry…) — [T; S x800/x840,
   g007 panel + crop].
9. **Pose against the reference — torso first, then
   limbs** — [T doctrine; S g008 TORSO-Spine1 first grab].
10. **Gross placement with X-Mirror ON**: select paired
    controls, move both sides at once (3 selected → 6
    moved) — [T; S g009].
11. **Legs: symmetry OFF, cross the legs** with
    axis-restricted moves (GX) in orthographic views
    (Numpad 1 front) — [T; S x1150 screencast keys].
12. **Aim the knees with the legs' pole targets** (hands'
    poles likewise, step 15) — [T; S g010 POLE-UpperArm.L].
13. **Split the editor into two panes; add the Camera**
    (50 mm of record); enable **Camera to View** — [T;
    S g011 camera panel + crop].
14. **Keep posing inside the split view**, judging the
    pose in the camera pane as a preview of the final
    render — [T; S g012–g014 split layout].
15. **Hands next**: place the wrists (IK controls + pole
    targets); deprioritise the camera-invisible hand —
    [T; S g013 IK-Wrist.L].
16. **Fingers manually**, conformed on the thigh, to a
    "looks convincing" standard — rig finger tooling
    deliberately not used — [T; S g013/t1500 + crop].
17. **Tilt the head toward the camera**, switching
    Global/Local orientation as needed — [T; S g012+].
18. **Pose the robot-arm prop last** (IK-Robot_Wrist.L),
    symmetry enabled for the pair — [T; S g014].
19. **Stop at approximate**: the pose is a tutorial-grade
    match to the reference, explicitly not an exact
    replication — [T].
20. **[Part 2, announced]** Set up the lighting —
    [T close 27:32].
21. **[Part 2, announced]** Optimized render settings —
    [T close 27:36].
22. **[Part 2, announced]** A little post-processing —
    [T close 27:36].

**Step count: 19 observed steps (Part 1) + 3 announced
Part 2 steps = 22.**

## Transcript ↔ screen disagreements (screen governs)

1. **Rig family.** Narration first claims the MHX Runtime,
   then self-corrects to CloudRig within the same passage;
   the screen's `cloudrig_ui` property agrees with the
   correction. Ruling: CloudRig; the MHX sentence is a
   caught-and-fixed error, recorded as such (the fix is
   part of the evidence — he verifies rig type against the
   add-on's contents, not from memory).
2. **Course focus.** The intro says "we'll just focus on
   lighting", but Part 1 contains no lighting work at all;
   the close reassigns lighting to Part 2. Ruling: the
   intro sentence describes the two-part course, not
   Part 1; no contradiction once the close is read.
3. **Blender version.** Narration says "Blender 5.0"; the
   title bar and status bar read **5.0.1**. Ruling: 5.0.1
   (screen), narration rounding.

## UNREADABLE register (counted, never guessed)

1. **The reference's medium and location.** The narration
   leans on "the reference" at least six times (the seated
   pose, the head tilt, both hands visible in it), but no
   frame in the 36 captured shows a reference image — not
   in Blender, not in a browser tab (an Excalidraw
   whiteboard tab is open in the survey stretch; its
   contents are never shown). Whether the reference is a
   photo, a render, or a sketch is UNREADABLE from this
   capture.
2. **Render-resolution and output settings.** No render
   panel is ever opened in Part 1; the only camera numbers
   of record are the 50 mm focal length and the transform
   in §3. (Part 2 territory, but counted here so the gap
   is named, not filled.)
3. **Whisper renderings left unresolved.** "on the fly" in
   the finger passage (context — a hand posed on the
   thigh, in close-up on screen — suggests "thigh"; the
   transcript is quoted as rendered and the suggestion is
   recorded as a suggestion only). Name garbles the screen
   DOES decide (Domina, DAZ, Diffeomorphic, Reallusion)
   are normalised in this record with the screen as the
   decider.
4. **Whether any keyframe was ever inserted.** The rig
   panel carries a "Keyframe All Settings" button
   [SCREEN x800]; no frame shows it pressed, the timeline
   playhead never leaves frame 0, and no key diamonds are
   visible in any frame. Recorded as NOT SEEN — the
   session is a still-pose session on this evidence, and
   the button's presence is not evidence of its use.

**UNREADABLE count: 4.**

## Numbered claims (for the convergence map)

1. The course is two parts: Part 1 = model, setup, pose;
   Part 2 = lighting, optimized render settings, post —
   per the creator's own close. [SPEECH]
2. Blender is the course DCC because it is free (no
   subscription/account); version of record 5.0.1.
   [BOTH]
3. Diffeomorphic / DAZ Importer is required for the
   downloaded model to work; its install is involved and
   is taught by another creator's video, linked in the
   description. [BOTH]
4. Characters are sourced three ways — scratch (ZBrush +
   tablet; hardest), character-creator software
   (MetaHuman, Character Creator 5, DAZ Studio — DAZ the
   NSFW-main and free), or download (SmutBase) — and
   download is the recommended beginner route, scratch
   deferred until skilled. [SPEECH + SCREEN pages]
5. The model download requires BOTH the latest model zip
   and the textures zip. [BOTH]
6. Opening the downloaded .blend requires allowing Python
   execution; the rig's UI is that script. [SPEECH;
   SCREEN rig UI live]
7. A copy of the downloaded file is saved before changes
   are made (stated habit, optional). [SPEECH]
8. The DAZ Importer add-on must be verified enabled in
   Preferences → Add-ons or the rig will not work.
   [BOTH]
9. The rig is a CloudRig rig (creator's on-record
   self-correction from MHX); the DAZ Importer also ships
   the MHX Runtime, which this model does not use.
   [SPEECH correction + SCREEN cloudrig_ui]
10. Posing recreates a reference (seated, head tilted)
    approximately; exact replication is explicitly
    declined as too slow for a tutorial. [SPEECH]
11. Posing order is torso first, then limbs. [SPEECH;
    SCREEN first grab is TORSO-Spine1]
12. X-Mirror is toggled per subtask (on for paired gross
    moves, off for legs, on again for hands and robot
    wrists); no asymmetry rule is stated. [BOTH]
13. Axis-restricted moves (GX) and numpad orthographic
    views are working tools while posing. [BOTH]
14. Legs and hands have pole targets, used to aim knees
    and elbows. [SPEECH; SCREEN POLE-UpperArm.L move]
15. The camera is added AFTER the gross pose: editor
    split into two panes, Camera to View enabled, posing
    continued under camera supervision; focal length of
    record 50 mm. [BOTH]
16. The hand the camera cannot see is deprioritised —
    "it doesn't really matter what we do" with it.
    [SPEECH]
17. Fingers are posed manually by deliberate choice over
    the rig's tooling, to a "looks convincing" standard.
    [SPEECH; SCREEN finger close-up]
18. The head is tilted toward the camera AFTER the hands;
    Global/Local orientation switching is taught as a
    working habit. [BOTH]
19. The robot-arm prop is posed last. [BOTH]
20. The model file ships with lights (Rim1, Sun) and a
    physics collection already in it; no lighting is
    placed or tuned in Part 1. [SCREEN]

**Claims count: 20.**

## SHOULD-BE-SEEN check (against INTAKE.md, Pass 0)

Expectation (verbatim): "Part 1 of a start-to-finish
workflow: scene and model setup through posing/animation
fundamentals, per this creator's order of operations."

| # | Expectation element | Verdict | Evidence |
|---|---|---|---|
| 1 | Scene and model setup | **SEEN** | Survey, sourcing, download (model + textures), add-on verification, script-execution allowance, working copy, rig-UI configuration (§§1–2, steps 1–8) |
| 2 | Posing fundamentals | **SEEN** | Torso-first order, X-Mirror toggling, axis restriction, pole targets, camera-supervised posing, hands/fingers/head/prop sequence (§3, steps 9–19) |
| 3 | Animation fundamentals | **NOT SEEN — deferred by the creator** | No keyframe, no timeline work, frame 0 throughout (§3, UNREADABLE 4); the creator's close assigns lighting/render/post to Part 2 and never promises animation in Part 1 beyond the intro's course-level arc |
| 4 | The creator's order of operations, as a list | **SEEN** | 19 observed steps + 3 announced, each with evidence (above) |

Tally: **SEEN 3, NOT SEEN (deferred to Part 2) 1,
CONTRADICTED 0.** The plan's premise holds for a Part 1;
its "animation fundamentals" phrase over-promises for this
half — a plan-wording erratum, filed with the duration
erratum in INTAKE.md.

## Frame index (runs/plan-16/)

Grid frames (every 120 s from t=0), `frames/`: g001 0:00
Houdini portal · g002 2:00 Diffeomorphic wiki · g003 4:00
tablet shopping · g004 6:00 Character Creator 5 · g005
8:00 SmutBase Domina downloads · g006 10:00 DAZ Importer
preferences · g007 12:00 rig panel, model · g008 14:00
TORSO-Spine1 grab · g009 16:00 seated pose, Shift fine
move · g010 18:00 POLE-UpperArm.L · g011 20:00 camera
50 mm, split top view · g012 22:00 split camera/user,
IK-Wrist.L · g013 24:00 finger close-up on thigh ·
g014 26:00 IK-Robot_Wrist.L.

Targeted frames, `frames60/`: t60, t180, t300, t420,
t540, t660, t780, t900, t1020, t1140, t1260, t1380,
t1500, t1620 (same subjects at +60 s offsets).
Targeted frames, `framesX/`: x800 rig panel (upper:
Quality/Physics/Skin/Head/Cybernetics) · x840 rest pose,
panel · x870 panel, three-quarter · x1150 front
orthographic, screencast keys, crossed-leg pose.

Crops (native resolution), `frames/crops/`:
crop-t660-daz-importer.png (DAZ Importer 5.0.0 panel) ·
crop-t780-rig-panel.png (outfit/IK/FK toggles) ·
crop-t1260-camera.png (Camera transform) ·
crop-t1500-fingers.png (hand-on-thigh close-up).

Totals: 14 grid + 14 targeted + 4 extra targeted = **32
frames**, **4 crops**, 36 files.

