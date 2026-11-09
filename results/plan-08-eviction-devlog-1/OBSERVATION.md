# Plan 08 — Pass 1 Timed Observation Record

- **Plan:** `repo/plans/08-eviction-devlog-1.md`
- **Video:** DivinityStudio, "Eviction - DevLog - Episode #1" —
  rule34video 4601875, page-stated licence **none**, duration
  1:28:50 (5,329.966667 s file).
- **Media of record (primo):** `~/.local/share/pax/night-school/plan-08/plan08-source-1080p.mp4`
  — SHA-256 `7a88eb29ac4aef7d97d5d5ff59db90f5245b528a40b696a5d820d254abc1e72c`,
  1,902,231,620 bytes, h264 1920×1080 30 fps + AAC.
- **Transcript:** primo `~/.local/share/pax/night-school/plan-08/transcript.txt`
  (+ `.srt`; copies in this run dir; provenance in
  `MANIFEST.md`). Chunked lane (duration over the 3,600 s
  cap): chunk1 0–3300 s, chunk2 3300–5330 s, seam at 55:00.
  **Stitch verify: FAIL, mechanism named** — whisper stamps
  its repetition-loop segments in exact 30.00 s blocks that
  run past the media end (chunk1 last end 3315.00 s vs its
  3300 s cut; stitched last end 5350.92 s vs duration
  5329.984 s). Every *substantive* segment ends inside the
  media; the overshoot is confined to loop segments and is
  recorded, not repaired. **Loop census** (normalized-segment
  rule, `records/loop-census.txt`): 204 segments, 163 loop
  (79.9%), recoverable 20.1%. Single-transcriber output
  (UNCONFIRMED tier); on-screen values are corroborated
  against sampled native frames wherever cited, and
  narration-vs-screen disagreements are resolved for the
  screen.
- **Frames:** 89 grid stills at 60 s spacing + 8 contact sheets
  (primo `frames/grid/`, run dir `frames/sheet-01…08.jpg`) and
  7 native 1920×1080 frames (run dir `frames/native/`):
  t180, t840, t1020, t2700, t3540, t5040, t5280.
- **Agent read notice:** every read in this document is an
  agent read of sampled frames + the machine transcript. The
  Owner's eye has not seen this material; eye items are queued
  in REPORT.md.

## What this video actually is (read first)

The plan's premise needs one correction, already recorded at
intake: **the project is an adult comic, not a game** — the
creator's own page description says "a simple adult comic in
Blender", and the screen bears it out end to end. There is no
game engine, no interactivity, no playable slice anywhere in
the 89 minutes. What the episode actually documents is a
**look-development session**: the dev takes two pre-existing
DAZ-derived characters into Blender, builds two test scenes
(`test_01` portrait, `test_02` pool), and iterates lighting +
compositing until he has two finished test renders, which he
reviews side by side in the final minute. Almost nothing the
plan expected to see (premise pitch, scope calls, problem
narration as the spine) is the episode's centre of mass; the
centre of mass is parameter-level craft iteration, most of it
unverbalised (see §5, the narration filter made measurable).

## 1. Screen record (timed, from the 60 s grid + native frames)

All times are video times. "File" = the Blender title bar.

### Block A — framing and prior work (00:00–05:00)

- 00:00 Browser: his rule34video "My Videos" page. Prior
  catalogue visible: "The Office — Gameplay (!)" Parts 1–8,
  "How to Make 3D Porn" parts, "Make 3D Porn" — a working
  back-catalogue of gameplay-style videos and tutorials
  predates this project.
- 01:00 An image view of a fantasy game render (mecha/angel
  still) — reference browsing.
- 02:00 His rule34video profile: "divinitystudiox", 115
  subscribers; Patreon / SubscribeStar / X links in the banner.
- 03:00 A live-action adult video playing on EPORNER
  (on-screen caption visible) — reference study of a real
  scene; native frame t180 pulled (see §5 note on reference
  use).
- 04:00 His rule34video videos page again: "Continuum —
  Gameplay (Demo)", "How to make Semen in Blender",
  "The Office" parts 5–10.

### Block B — character intake, DAZ → Blender (05:00–12:00)

- 05:00 DAZ Studio: empty viewport; a DAZ-to-Blender bridge
  panel is docked ("Export Blender", "Mesh Stat", "Readme",
  "Save Paths", "Setup Menus" buttons).
- 06:00 DAZ Studio: a bald Genesis female head/shoulders in
  the viewport.
- 07:00 Same character with strand hair fitted.
- 08:00 Blender 5.2.0 LTS: the character is in, red hair;
  a "Make Hair" menu is open over the hair settings.
- 09:00–11:00 Blender: full-body inspection of the imported
  character (red two-piece outfit), armature/rig visible,
  outliner checks.

### Block C — test_01: scene organisation and first lighting (12:00–24:00)

- 12:00–13:00 `test_01`: character standing in an empty scene;
  render settings panel (Cycles).
- 14:00 Windows Explorer over the project: folder `Eviction`
  with subfolders incl. comp / misc / renders / tex / uploads
  / vlog (grid frame, partially legible). Native t840 shows
  the companion structure inside Blender: file
  `all [E:\Eviction\geo\chars\all.blend]`; outliner
  geo > chars > **Claire**, plus rig **HID Julia**;
  cameras > Camera; lights. Colour management AgX, Exposure
  0.000, Gamma 1.000. Scene stats: 184,642 verts / 362,560
  tris, VRAM 1.5/4.0 GiB.
- 15:00–16:00 `test_01 [E:\Eviction\geo\scenes\test_01.blend]`:
  camera framing on the character; camera panel open.
- 17:00 (native t1020) Pose Mode on rig **HID Julia** (Rigify
  bone collections Tweak/Widgets/Custom/Root/Spine; 294
  bones): head/neck pose adjustment. In this and several
  setup frames the character's eyes read white/rolled; in
  every finished render the eyes are normal — a posing-stage
  artefact of the eye rig, recorded as seen.
- 18:00–23:00 World/lighting: Shader Editor world chain —
  Environment Texture **`DTHDR-RuinsB-500`** → Background
  (Strength 2.000) → World Output (grid frame 17:00 block);
  then spot lights aimed at the portrait, repeated
  render-preview checks of the face.

### Block D — test_01: look iteration (24:00–48:00)

- 24:00–28:00 A plane is placed behind/above the head
  (light-shaping), positions nudged in orthographic views;
  hair colour walked white → ash-brown across the block
  (several distinct hair colours are tried on the same
  character: red, blonde, white, ash, and later lavender).
- 29:00–30:00 Hair particle/strands editing ("Hair Romantic
  Middle Parting Ponytail Strands Mesh" object; styling curve
  editor visible).
- 31:00–35:00 Light rig grows: multiple spots, beam angles,
  a visible cone/falloff check; one frame (33:00) shows the
  render preview fully blurred while a lens/DoF value is
  mid-edit.
- 36:00 File/material work (DAZ Top Coat node visible in the
  shader editor strip).
- 37:00–43:00 **Compositor block**: editor switched to
  Compositing; chain assembled on the rendered portrait —
  Render Layers → Glare-family node → RGB Curves → Color
  Balance (Lift/Gamma/Gain) → Lens Distortion → Viewer, with
  a film-look thumbnail strip docked under the backdrop
  (third-party film-emulation looks browser). Values are
  nudged node by node with the backdrop live.
- 44:00–47:00 Back in Layout: spot temperature/exposure
  adjustments; one wireframe pass with hand-drawn yellow
  measurement curves over the torso (45:00, grid); render
  Performance panel — Threads Mode Auto-Detect (native
  t2700). test_01 outliner at 45:00: lights = **face_lgt**
  (Spot), **overhead_lgt**; fx = **fogbox**; cameras = Camera.

### Block E — test_01: grade finish and render review (48:00–60:00)

- 48:00 Hair colour picked live from the colour wheel —
  settles on lavender/purple.
- 49:00–53:00 A second camera setup is tried and the
  compositor chain re-checked (Brightness/Contrast,
  RGB Curves).
- 54:00–58:00 **Glare node deep-dive**: Glare type walked
  (Highlights/Bloom/Streaks variants visible in successive
  frames), then Bloom settings, then Lens Distortion →
  Brightness/Contrast as the final two nodes.
- 59:00 (native t3540) Windows Photos opens
  **`test_render_005.png`** — the finished test_01 portrait:
  lavender hair, overhead soft light, dark ground. The render
  counter proves at least five saved test renders for
  test_01 alone.

### Block F — test_02: second character, studio HDRI (60:00–72:00)

- 60:00 New file `test_02`: a second, nude character (the
  scene's subject is Claire per the outliner at t5280);
  camera blocked.
- 61:00–64:00 Planes added as floor/backdrop candidates;
  character repositioned.
- 65:00 World shader: Texture Coordinate → Mapping →
  **`studio_small_08_1k.hdr`** environment (a small-studio
  HDRI), Background strength nudged.
- 66:00 An external image viewer shows a finished couple
  render (not from this session's files) — a target/reference
  image consulted mid-build.
- 67:00–71:00 Wall colour picked; two spots placed and
  walked (exposure, angle), render preview checked after
  each move.

### Block G — test_02: set build, water, final (72:00–88:50)

- 72:00–75:00 Lighting continues; a **Volume Scatter +
  Volume Absorption → Mix Shader** chain is built for the
  fogbox (grid frame 75:00: Volume Scatter Density 0.050,
  Anisotropy 0.000; Volume Absorption Density 1.000; Mix
  factor 0.500 — as read at grid scale, marked approximate).
- 76:00–78:00 **Set construction**: a plane is subdivided
  into a grid and alternate faces extruded into a
  pyramid-studded acoustic-panel wall (`back_wall_geo`).
- 79:00–83:00 Wall coloured (red pass, then grey), a cylinder
  placed (pool-side prop/light), floor and water plane
  blocked; character positioned waist-deep.
- 84:00 (native t5040) **Blendkit** panel open in test_02,
  search "wa…": he pulls the **"Shimmering Pool Water"**
  material (by Paco Salas, per the asset card) onto
  `water_plane_geo`. Scene at this frame: 135,567 verts /
  266,286 tris.
- 85:00–87:00 Pool scene lit: magenta/pink area light bars
  behind the character, water reflections live; spot tuned
  (final read at t5280: **key_lgt Spot, Temperature 7500 K,
  pink tint, Power 200.000, Exposure 1.000, Radius 0.25 m,
  Beam Angle 45°, Blend 1.000**).
- 88:00 Final minute: file saved ("Saved test_02.blend" in
  the status bar, native t5280); both finished renders are
  opened side by side in the image viewer —
  test_render (portrait) and the pool render, the character
  now posed (hand to body) where the session frames showed
  a neutral stance. Roll credits: none; the video ends on
  the review.

## 2. Narration record (from the stitched transcript)

The recoverable narration is **two blocks totalling ≈ 5.6
minutes of an 88.8-minute video (≈ 6%)**. Everything else is
music under sped-up footage (the format the narrator states
at ~04:00: "The video will be sped up... it's gonna be long
and boring"). Audio energy is present in every 5-minute
window (RMS −34…−39 dB, `records/rms-5min.txt`), so the
loops are a no-speech signature, not missing audio; any
speech buried under the music after 04:17 is UNRECOVERABLE
by this lane and is marked so, never reconstructed. Quotes
below are the transcript's (UNCONFIRMED tier); proper nouns
are governed by the screen (DAZ Studio, not "Das Studio").

### Block N1 — spoken intro, 00:00–04:17 (video time)

- **Format/premise (0:00–0:49):** "This is a first episode
  of a development log. I will develop a comic in Blender.
  This will be a small scale project which will probably be
  done within a week or so. It's nothing too serious. I will
  try to post updates whenever I can. I will document the
  whole process from concept to final render... That will
  be long and boring."
- **Studio/roadmap (0:49–2:16):** Divinity Studios "is not
  an actual studio. It's a one man band. I'm working by
  myself. Of course the end goal is to make a large scale
  game similar to Final Fantasy... making a game of such a
  caliber would require a team. Of course a team requires
  money. But for now I'll just work by myself. Making small
  scale games. And over time perhaps each game I work on
  will increase in complexity." — note the slide: the stated
  ladder is *games*, while this project is a comic.
- **Project premise (2:16–2:53):** "My first project will
  be a comic tentatively titled Eviction. The protagonist
  will be an attractive young woman who has trouble paying
  her rent. Of course our sleazy landlord takes advantage
  of the situation. As some of you may know this is a
  common trope in pornography."
- **Reference (2:53–3:52):** he plays the live-action
  reference scene (screen: EPORNER, 03:00 grid frame;
  browser tabs in the opening frames name the performer
  Brooklyn Chase) and comments on its dialogue/premise:
  "She got her tits out. She has a pay to run [rent]. You
  know it's a basic story... some of the dialogue is cut
  but that's the basic premise... So my comic will borrow
  ideas from this."
- **Episode scope (3:52–4:17):** "So first episode of the
  devlog. I will create the first character. Female. In
  DAZ Studio. Bring her over to Blender. And do a couple
  of things like that... The video will be sped up."

### Block N2 — render-review voiceover, 58:30–59:37

Over the Photos viewer showing the test_01 renders:
"I've done a couple of renders, as you see. I think I did
four or five. And this is what I ended up with. **I don't
remember what I did, but I think I added more point lights
near her face.** I like this one. The previous renders are
over, but I added more lights behind her. This is just a
promotional image. Her purple hair, some people might find
it strange, but I think it's cool. I might, I don't know,
maybe I'll change it, but this is what I'm going with."

### Narration-vs-screen disagreements (resolved for the screen)

1. **"Point lights" (N2) vs the screen's spot lights.** The
   visible rig is named Spot objects — `face_lgt` is
   "Spot.001" in the shader strip at t2700, `key_lgt` is a
   Spot with beam angle/blend at t5280. If point lights were
   also added, they are not the named rig the screen shows.
   Screen governs: the portrait rig is spots.
2. **"Four or five" renders (N2) vs the screen's
   `test_render_005.png`** (t3540). The file counter says
   the numbering reached at least 005; the narration's
   uncertainty is the dev's, the filename is the harder
   evidence. Substance agrees (≈5 renders); precision goes
   to the screen.
3. **"I don't remember what I did" (N2)** — not a
   disagreement but a confession the screen corroborates:
   ~50 minutes of parameter iteration (Blocks D–E) left no
   record the dev himself can replay a minute later. This
   is the episode's single most transferable datum (see
   TECHNIQUE.md T-3).
4. **No narration exists for Blocks F–G at all.** The whole
   test_02 build — set construction, volume fog, Blendkit
   water, final pose — is un-narrated. Anything a viewer
   "learns" from the back half is inference from watching
   hands, which is exactly the estate's narration-filter
   question answered by measurement: the filter removes
   ~94% of the process, including every reason.

## 3. Claims list (Pass 1 close-out)

A devlog makes few explicit technique claims; these are all
of them, numbered for Pass 3 (REBUILD-DIFF.md judges each
against the episode's own record and the estate diff — a
process claim is "reproduced" when the screen shows the
claimed behaviour, "refuted" when it does not).

- **C-1** The whole process, concept to final render, is
  documented. (N1)
- **C-2** The project is small-scale and finishable "within
  a week or so". (N1)
- **C-3** Episode 1 = create the first (female) character
  in DAZ Studio and bring her to Blender. (N1)
- **C-4** The comic borrows its premise from the named
  live-action reference scene. (N1 + screen)
- **C-5** The work footage is sped up; the episode is a
  compressed record, not real-time. (N1 + screen)
- **C-6** The test_01 look was reached by adding lights
  near/behind the face; the purple hair is a deliberate,
  kept choice; the render is "a promotional image". (N2)
- **C-7** (implicit, structural) One character file feeds
  multiple scene files; scenes are numbered tests
  (test_01, test_02) under a fixed folder discipline.
  (Screen only — the dev never states it.)
- **C-8** (implicit) A purchased/asset-library material
  (Blendkit "Shimmering Pool Water") is acceptable inside
  an otherwise hand-built scene. (Screen only.)

## 4. Build sequence of record (screen-derived)

1. Back-catalogue and audience surfaces exist first (prior
   series + tutorials; Patreon/SubscribeStar linked).
2. Reference gathering (game still, live-action scene).
3. Character intake in DAZ Studio; strand hair fitted there.
4. Bridge export to Blender 5.2.0 LTS; import inspection.
5. Project skeleton: `E:\Eviction\` with geo\chars\all.blend
   (all characters in one chars file) and geo\scenes\test_NN
   scene files; renders/uploads/vlog folders at top level.
6. test_01: camera → HDRI world (DTHDR-RuinsB) → spot rig
   (face_lgt, overhead_lgt) → fogbox → hair iteration →
   compositor grade (Glare/Curves/Color Balance/Lens
   Distortion) → saved test renders (≥5) → review.
7. test_02: second character → studio HDRI
   (studio_small_08) → primitive set build (extruded pyramid
   wall, cylinder) → volume fog → Blendkit water material →
   pink key/face spots → pose → save → review.
8. Episode closes on the two renders reviewed side by side —
   no comic page, panel, or lettering appears anywhere in
   the episode.

## 5. Surprises and narration-filter evidence

- **The "first episode" contains no comic.** For a series
  billed "ideation to final product" of a comic, episode 1
  ends at character look-dev test renders. Sequencing lesson
  either way (see TECHNIQUE.md): the dev front-loads
  character look before any page exists.
- **The devlog shows the tool, not the clock.** Nothing on
  screen prices any step in time; the only duration evidence
  is the video's own 89 minutes of edited footage for a
  session of unknown real length.
- **Reference use is shown but unexplained on screen:**
  a live-action scene (03:00) and a finished couple render
  (66:00) are consulted; what was taken from either is not
  visible in the frames sampled.
- **Failures are nearly invisible:** the sampled record shows
  one blurred-preview moment (33:00) and repeated small
  corrections, but no crash, no failed import, no abandoned
  approach. Either the session went unusually clean or the
  edit removed the friction; the frames cannot distinguish —
  recorded as an open read, not a conclusion.
- **The sketch cube (23:00 grid frame):** a cube textured
  with a hand-drawn figure sketch appears in one frame —
  the only drawn/storyboard-like artefact in the episode;
  its role is not determinable from the sampled frames.

## 6. SHOULD-BE-SEEN scoring (against INTAKE.md)

1. *Project premise* — **PARTIAL.** The premise exists on the
   page (adult comic "Eviction", in Blender) and the project
   folder/files carry the name; the episode's sampled frames
   never state a story premise, character names in dialogue,
   or a plot beat. (Narration may add premise; §2 rules.)
2. *Tooling choices* — **SEEN.** Blender 5.2.0 LTS as the
   stage; DAZ Studio + bridge (Diffeomorphic-class panels:
   DAZ Setup / DAZ Runtime / MHX tabs visible at t5040) for
   character intake; Blendkit for a production material;
   HDRI worlds; Cycles. Reasons are narration territory (§2).
3. *The first playable slice* (intake-corrected: first
   finished page/spread) — **NOT SEEN.** No page, panel, or
   lettering exists in the episode; the slice-equivalent
   delivered is the pair of test renders.
4. *The problems the dev chooses to narrate* — **SEEN, and
   the answer is: none.** The full recoverable narration
   (§2) contains no problem statement, no failure, no fix.
   The single process admission is retrospective and about
   memory, not difficulty: "I don't remember what I did"
   (58:30 block). The plan's hypothesis — that a dev
   narrates the problems that cost them time — is REFUTED
   for this episode: the narration filter removes problems
   entirely, not selectively.
