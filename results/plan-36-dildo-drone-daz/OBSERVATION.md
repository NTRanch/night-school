# Plan 36 — Pass 1 Timed Observation

Source: pinned 720p capture (MANIFEST.md), 265.833 s.
Tool on screen: **DAZ Studio 4.21 Pro** (window title),
Windows desktop, session recorded **01/12/2023** (taskbar
clock, all frames). Observation base: 53 grid stills @5 s
(native 1282×720) + 14 targeted native stills + 15 panel
crops — **82 stills** — plus the single-pass transcript
(§1). Screen governs.

## 0. Premise + the run's central surprise

**Premise: TUTORIAL — confirmed, as titled.** The file is a
screen recording of a DAZ Studio session in which the
creator loads one prop asset and tours its library:
variants, fan parts, material presets, an animated pose
preset, and a hand-keyed hover animation he describes
while scrubbing it. Narration runs the whole file
(transcript §1).

**Surprise vs the plan's SHOULD-BE-SEEN:** the plan expects
the prop "positioned and kept registered against a
character". **No character is ever loaded.** In all 82
sampled stills the scene contains only the drone prop, the
DAZ default grid, Tonemapper Options and Environment
Options. There is no Genesis figure, no body, no contact
set at any timestamp. The registration this video actually
teaches is therefore **inside the prop**: loose parts
(the four rotor fans) are thrown into the scene and
**parented to the prop's root node** (creator's own words,
§5, C-02), and the finished assembly is then placed and
animated as one node. Prop-to-body registration is neither
shown nor mentioned; §6 and Pass 2 state the consequence
honestly instead of inventing one.

## 1. Transcription record

Method per the chunked-transcription skill §3: the media
(265.833 s) is under the 3,600 s single-pass cap, so one
pass: whisper-cli (whisper.cpp 1.9.2), model
ggml-large-v3-turbo, primo CPU, nice 19, detach
`ns36-media` (.done reads 0). Audio census first:
volumedetect mean −28.8 dB / max −4.9 dB (speech present,
quiet). Loop census (rule normalized-segment-v1, threshold
>8) over the stitched single-pass SRT: **segments=36,
loop_segments=0, loop_share=0.0%, recoverable=36 (100.0%)**
— `transcript.srt` in this run dir; last segment ends
263.36 s ≤ 265.833 s media duration — PASS.
Tier: **UNCONFIRMED** (single transcriber; screen governs).
Whisper renderings normalised in citations: "desk studio"
= DAZ Studio, "matte presets" = material (MAT) presets,
"post presets" = pose presets, "genetator" = genitalia,
"nvidia highway" = NVIDIA Iray; each is flagged where it
matters and every load-bearing claim is screen-corroborated
or marked speech-only.

## 2. Session anatomy (screen)

- Scene (Scene pane, t=48 onward): root node
  **`dildo_drone_one`** with exactly four child nodes —
  **`drone_faninstfour`, `drone_faninstone`,
  `drone_faninstthree`, `drone_faninstdtwo`** — plus the
  scene-level `Tonemapper Options` / `Environment Options`.
  Nothing else is ever in the scene.
- The root is a **single geometry** (a prop, not a figure):
  its Surfaces list (Shader Baker pane, t=62/t=248) names
  the surface groups **camerasection, Dildobody, dildotip,
  dronearmcone, dronearms, dronebody, fanprotectors** and
  at least two more partially legible entries ("dronearm…"
  and "poles"/"metal" at the list tail — §7 item 2). The
  device appendage (body + tip) is part of this same mesh,
  hanging below the body on the arm section.
- Content Library path (t=32/48): Props >
  shadowyartsdirty > sextoys > dildo > Dildo_drone >
  **dildo_drone_one** { data, **dronefans**,
  materialpresets, posepresets } and sibling folder
  **dildo_drone_two** (never opened — §7 item 3).
- The dildo_drone_one folder holds two scene files
  (t=32): **`dildodroneone`** (the one loaded) and
  **`dildodronesimplev`** (a "simple version" — never
  loaded or described further).

## 3. Structure of the 266 seconds (screen + speech)

| Span (s) | What happens |
|---|---|
| 0–30 | Intro [SPEECH seg 1–4]; library path narrated; `dildodroneone` loaded; **Missing Files dialog dismissed** ("i'm just going to ignore this error file", seg 4; dialog on screen t=32) |
| 30–50 | **The fans**: dronefans folder — 4 fan instance items [SCREEN t=48]; speech: *"throw these into the scene, parent all those to that"* (seg 5–6, 0:30–0:49). By t=48 the Scene pane shows all four fans as children of the root |
| 51–67 | Device body+tip materials mentioned; creator **hides the device part for YouTube** ("now it is just an ordinary drone you can fly", seg 7–9). A slim under-body rod remains visible in most frames (§7 item 4) |
| 67–84 | Draw styles: viewport switched via the DrawStyle menu (t=78: Wire Texture Shaded highlighted; speech names Filament and NVIDIA Iray, seg 10–11) |
| 84–120 | Material presets tour I: fan protector presets (folder shows **default / pink**, t=95); fan blade materials (speech: gold / silver / pink options, seg 13); all four fan nodes shown selected together (t=112) |
| 112–130 | **dildo_mat_presets folder: 7 items** — default, dildo_body_one, dildo_body_pink, dildo_body_two, dildo_tip_one, dildo_tip_pink, dildo_tip_two (t=112) |
| 120–140 | Full-asset presets folder: **allgold, allwhite, default_drone_preset, droneallpink** (t=130); gold variant seen applied ~t=125 (grid); speech: device mats exist but "i can't really show them" on YouTube (seg 14–16) |
| 140–155 | droneallpink applied (whole prop pink by t=148); **posepresets folder: exactly 1 item, `fanbladeposeone`** (t=148) |
| 155–215 | Timeline pane open (t=168): range **61 frames (0–60) @ 30 fps**, track = root node only; keys at ≈15-frame spacing. The pose preset animates the fans — *"look at that, they spin"* (seg 21–22). Creator's extension recipe [SPEECH seg 22, 25–26]: spin, then rise; **"have this rise 20 frames, have this lower 20 frames, because drones typically bob"**; drift sideways and *"rotate a bit"*. At timeline frame 20 the root reads **X Rotate −5.00°, Z Rotate 8.50°** (t=212) — the bob's tilt, mid-key |
| 215–235 | Re-applying `default_drone_preset` raises **"Unable to locate file"** for a texture under the asset's own library path (`…/Dildo/Dildodrone/teen_boy_one_torso.jpg`, dialog read at t=232); creator skips it and hurries the result off screen ("this might actually get deleted from youtube, let me quickly remove this", seg 29–30) |
| 235–266 | Surfaces re-inspected (t=248: Dildobody selected, Iray Uber property list); **PowerPose pane opened — it shows DAZ's empty state, "Where Are The Controls?"** (t=258, §4); closing speech: the appendage parts — *"i just called them rolling pins"* — **"you can extend these parts… you can lengthen"** them (seg 34–35); sign-off at 4:21 (seg 36); last ~2 s black |

## 4. The control surface INVENTORIED (plan focus 1)

Every control legible on screen, named and classed.
Counts are of what the video exposes; §7 lists what could
not be read.

**Nodes (5):** root `dildo_drone_one` + 4 fan child nodes.

**Per-node animator controls (screen-verified, t=48/62/95/
112/130/148/212/248/258):** with any node selected, the
Parameters pane shows exactly **General > Transforms >
Translation (X/Y/Z) / Rotation (X/Y/Z) / Scale (X/Y/Z)** —
**9 channels per node, 45 across the assembly**. The
"Currently Used" filter shows no other parameter group on
any node at any sampled time. Specifically absent in
every frame: **no morph dials, no pose-control sliders,
no bones** (a DAZ prop has no bone hierarchy; the fan
nodes are plain child nodes, not bones), **no Shaping-pane
entries**.

**The PowerPose verdict (t=258):** late in the video the
creator opens the PowerPose pane and DAZ answers with its
empty state — *"Where Are The Controls? 1. Load a figure
into the scene. 2. Select the figure in the scene. NOTE:
Only selection of a node within the hierarchy of a figure
will cause controls to be displayed here."* The asset
exposes **no figure-style pose controls at all** — the
pane that would list them is empty because the prop is
not a figure. This is the video's own control-surface
audit, performed on screen by its creator while hunting
for the length control (§7 item 5).

**Surfaces (material control):** ≥9 Iray surface groups
on the single root geometry (§2), each carrying the
standard Iray Uber (MDL) property set — the visible
subset at t=62/248: Normal Map, Metallic Flakes Weight,
Top Coat Weight, Thin Walled, Emission Color, Cutout
Opacity, Displacement Strength, Horizontal/Vertical
Tiles and Offsets, UV Set (~15 properties per surface).

**Library-level controls (presets = the asset's real
control surface):**

| Folder | Items (as seen) | Count |
|---|---|---|
| dronefans | drone_faninstone/two/three/four | 4 instance presets |
| materialpresets (full) | allgold, allwhite, default_drone_preset, droneallpink | 4 |
| dildo_mat_presets | default, dildo_body_one, dildo_body_pink, dildo_body_two, dildo_tip_one, dildo_tip_pink, dildo_tip_two | 7 |
| fan_protector_presets | default, pink | 2 |
| fan_blades_presets | folder exists; contents never opened (§7 item 1) | UNREADABLE |
| posepresets | fanbladeposeone (animated — fans spin) | 1 |
| scene variants | dildodroneone, dildodronesimplev (+ whole dildo_drone_two folder unopened) | 2 + UNREADABLE |

**Total inventoried:** 5 nodes × 9 transform channels =
45 channels; ≥9 surface groups; 13 named material presets
+ 4 fan instances + 1 animated pose preset + 2 scene
variants = **20 library items**; morphs **0**; pose
controls **0**; bones **0**.

## 5. Registration steps, in order, mechanism per step
(plan focus 2)

1. **Load the root alone** (0:16–0:30). The scene file
   brings in `dildo_drone_one` by itself; the Missing
   Files dialog is dismissed, not fixed.
2. **Throw the parts in** (0:30–0:40) [SPEECH seg 5]:
   the four fan instances from the dronefans folder are
   merged into the scene as separate nodes.
3. **Parent every part to the root** (0:40–0:49)
   [SPEECH seg 6]: *"parent all those to that"* — DAZ
   parenting (each fan node parented under
   `dildo_drone_one`). Screen corroboration: from t=48
   onward the Scene pane shows the four fans as children
   of the root, and every later whole-prop move/rotation
   carries them. **This is the only registration act in
   the video.** No constraint, no "Point At", no
   per-pose offset keying against anything external is
   shown or mentioned, because there is nothing external
   in the scene.
4. **Place + animate the root as one node** (2:35–3:27):
   the assembly is thereafter a single transformable
   unit; its motion is keyed on the root (§6).

Against INTAKE H-b2 (contact-terminal ordering): the
ordering question is **not applicable as posed** — there
is no body to pose first. The nearest analogue holds in
spirit: the parts are registered to the root **before**
any animation is keyed, and the animation is keyed last,
on the finished assembly (cf. Plan 34's T10: contact —
here, registration — is settled before the expensive
downstream work; and nothing is re-registered after).

## 6. Hover / flight presentation (plan focus 3)

Devices AS SEEN, in the order the video presents them:

1. **Rotor spin (fiction made visible).** The single
   shipped pose preset, `fanbladeposeone`, is an
   *animated* pose preset: applied, the fan blades spin
   (speech seg 21–22: *"look at that, they spin"*). The
   lift fiction is carried by the fans actually rotating,
   not by a blur disc or texture trick visible at this
   resolution (§7 item 6).
2. **Keyframed bob (the support substitute).** The
   creator's stated recipe [SPEECH seg 25–26]:
   *"have this rise 20 frames, have this lower 20 frames,
   because if you look at that, drones typically bob"*,
   plus lateral drift ("move off to the side") and slight
   rotation ("rotate a bit… move into this side, rotate a
   bit"). Screen: the Timeline shows a **61-frame
   (0–60) @ 30 fps** animation on the root node only,
   keys at ≈15-frame spacing; at frame 20 the root's
   rotation reads **X −5.00°, Z 8.50°** (t=212) — a
   gentle rocking tilt mid-bob. The prop never touches
   the grid floor in any sampled frame; it floats over
   the origin for the whole session.
3. **NOT used:** no cast/contact shadow is staged (the
   viewport is an unlit grid view; no ground shadow is
   visible under the prop in any still), no camera trick
   (a single Perspective viewport throughout), no tether,
   cable, stand, or operator figure, and no physics —
   DAZ has no solver in this session and none is
   simulated by hand beyond the bob keys. The "drone"
   fiction itself (rotors = lift) is the justification;
   the bob is what sells it.

## 7. UNREADABLE register (counted, never guessed)

1. **fan_blades_presets contents** — the folder is listed
   (t=95/112) but never opened in any sampled frame.
   Speech names blade colours (gold/silver/pink) without
   a count. Count: UNREADABLE.
2. **Two surface-group names** at the Surfaces list tail
   are only partially legible across frames ("dronearm…"
   truncated; the last entry reads "poles" at t=62 and
   "metal" at t=248 — the list is scrolled differently).
   7 of ≥9 names are certain; 2 are UNREADABLE as exact
   strings.
3. **dildo_drone_two's contents** — the sibling asset
   folder is never opened; its node structure, presets,
   and differences from _one are UNREADABLE from this
   video.
4. **The hidden device + the visible rod.** Speech says
   the device part is hidden for YouTube (seg 7–9), yet a
   slim rod hangs under the body in most frames. Whether
   that rod is the device at a hidden/low-profile state,
   the "poles" surface, or the arm section is UNREADABLE
   at 720p; recorded as a discrepancy, not resolved.
5. **The length channel.** Closing speech claims the
   appendage parts ("rolling pins") can be extended /
   lengthened (seg 34–35), but no slider, morph, or scale
   operation that performs it is legibly performed on
   screen — the creator's own PowerPose search comes up
   empty (t=258). The channel's name/class is UNREADABLE;
   the claim itself is speech-only (C-11).
6. **Rotor geometry in motion** — whether the spinning
   fans are the modelled blades rotating (vs a swapped
   blur prop) cannot be distinguished at 720p in sampled
   stills; the spin itself is speech-asserted and
   consistent with the animated preset + timeline.
7. **Timeline key count** — keys are visible at ≈15-frame
   spacing across 0–60 (5 keys) at sheet resolution; the
   exact per-channel key placement (which of TRA channels
   are keyed) is UNREADABLE beyond the frame-20 rotation
   values read at t=212.
8. **Missing-file paths at load** — the t=32 dialog's two
   paths are truncated in the dialog ("D:/My second daz
   3d library/My DAZ 3D Library/…"); the later dialog
   (t=232) is fully legible and is the one cited.

## 8. Claims list (numbered; Pass 3 test list)

Provenance: [SCREEN] = the 82-still record; [SPEECH] =
transcript, UNCONFIRMED tier (§1); [BOTH] = each
corroborates the other.

- **C-01** [SCREEN] Premise: a genuine DAZ Studio 4.21
  asset tutorial; one prop, empty scene, narration
  throughout, no character at any timestamp.
- **C-02** [BOTH] Registration = **parenting**: the four
  fan instances are thrown into the scene and parented
  to the root node ("parent all those to that",
  0:40–0:49); the Scene pane shows the parented
  hierarchy from t=48 on.
- **C-03** [SCREEN] The assembly's animator control
  surface is transforms only: 5 nodes × Translation/
  Rotation/Scale XYZ = 45 channels; zero morphs, zero
  pose controls, zero bones; PowerPose empty state on
  screen at t=258.
- **C-04** [SCREEN] The root is one geometry with ≥9
  Iray surface groups (7 names certain); the device
  (body+tip) is part of that same mesh.
- **C-05** [SCREEN] Library: 4 fan instance presets, 13
  named material presets (4 full / 7 device / 2
  protector), 1 animated pose preset, 2 scene variants
  in folder _one.
- **C-06** [BOTH] The shipped pose preset is animated:
  applied, the fans spin.
- **C-07** [BOTH] Hover = keyframed root bob: rise
  20 frames / lower 20 frames at 30 fps, lateral drift,
  slight rotation; timeline 0–60 frames, root track
  only; frame-20 rotation X −5.00° / Z 8.50°.
- **C-08** [SCREEN] No shadow device, camera device,
  tether, or physics is used to support the float; the
  prop floats over the grid origin throughout.
- **C-09** [BOTH] The device part is hidden by the
  creator for the YouTube cut ("just an ordinary
  drone"); its material presets exist but are not
  demonstrated.
- **C-10** [SCREEN] The asset ships with broken
  references in the creator's own library: a Missing
  Files dialog at load and a missing-texture dialog
  when `default_drone_preset` is applied; both are
  dismissed, not repaired.
- **C-11** [SPEECH] The appendage parts ("rolling
  pins") can be extended/lengthened — channel
  UNREADABLE (§7 item 5); not demonstrated legibly.
- **C-12** [SCREEN] Registration precedes animation:
  parts are parented (0:40) long before any timeline
  work (2:35+); nothing is re-registered afterwards.
