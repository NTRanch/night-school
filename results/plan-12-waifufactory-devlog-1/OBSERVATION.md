# Plan 12 — Pass 1 Timed Observation

Method: dense frames at 2 s intervals (47 frames, `frames/`),
each read at full 1920×1080 where the segment turns on UI
detail. Timestamps are frame-derived (±2 s). The video is a
single continuous screen capture — scene-change detection at
threshold 0.35 finds no hard cuts; segments below are
activity changes, not cuts.

## 0. What the artefact actually is (surprise, first)

The title and the estate's expectation suggest a design
showcase. The artefact is something more specific and more
useful: **94 seconds inside the Godot Engine editor (4.6.stable,
UI language Russian), editing ONE character** — a green
pixel-pattern anime girl (a Minecraft-Creeper parody; the open
scene tabs include `minera_boomia_bg`) — in the game's own
`character` scene. There is no caption, no title card, and no
gameplay anywhere in the 94 s. There IS a quiet English
voiceover under a loud music bed (11 segments; transcript in
the run dir) — found by transcription, not by the silence
census, which missed it (see INTAKE). The video's claims
therefore come in two classes: what the editor demonstrates
(node trees, inspector fields, numeric parameters) and what
the voiceover asserts. They are tabled separately in
TECHNIQUE.md and never merged. Tool identification: **Godot 4.6.stable** —
VERIFIED (version string in the editor's bottom-right corner,
every frame). An editor plugin menu "SceneTreeAsText" is
visible in the top bar. No other tool appears. Nothing on
screen is UNIDENTIFIED.

## 1. Timed log

### S1 · 0:00–0:14 — Full-body rig posing (frames f001–f007)

- The character stands reclined, legs raised, arms up, in the
  2D canvas with a **Skeleton2D** bone overlay visible.
- Scene tree (skeleton view): `Temp > Skeleton2D > root >
  spine`, with `BodyRemote` (RemoteTransform2D), bones
  `L_ass` / `r_ass`, `spine`, `boobs` ×2, `spine`, `head >
  hair > hair, hair`; `FaceRemote`; `L_arm`… A separate
  top-level node `DickFollow` and a separate penis sprite sit
  posed at the character's right.
- Inspector on the root `Character` node (script
  `character.gd`): **Editor Skin: `bombia.tres`** with a custom
  **"Save Skin"** button, and an **"NSFW Colors"** property
  group: **Ass Color**, **Pussy Color** (color fields).
- FileSystem dock path: `res://src/data/characters/skins/akira.tres`
  (the dock's selected file; the loaded Editor Skin is
  bombia.tres — both names recorded as seen).
- Asset tree visible: `assets/audio/{ambients,music,sfx}`,
  `assets/character_1`, `assets/ui/*.ogg` (buy, click, error,
  hover, intro, random_box_open, shower, spin_1…).
- f005 (t≈8 s): the `boobs` Bone2D is selected; the status bar
  reads "Вращение: −2.447°" (Rotation: −2.447°) — a bone is
  being rotated live. The segment is posing/rig demonstration.

### S2 · 0:14–0:26 — Anatomy polygon + deform shader (f008–f013)

- Camera zooms to the genital area. The selected node is a
  Polygon2D named **`Pussy`**; its polygon outline (vertex
  diamonds) is being edited at 499.6% zoom (f012, t≈22 s).
- Scene tree (module view): `… LLegIK, RLegIK, HeadIK`;
  `Remotes > Body > SexModule` containing **BodyPhysics,
  LimbsModule, HeadModule, OpeningModule, FluidModule,
  CumLine**; an `NSFW` group with Polygon2D nodes **Ass** and
  **Pussy**; `Zones`; `DickMask > DickPath > DickFollow`.
- Inspector: the Pussy node carries a **ShaderMaterial** with
  shader file `hole_deformer…`, parameters read numerically:
  **Stretch Amount 36.0, Stretch Power 1.0, Center Offset
  0.984, Bend Multiplier 0.55, Curve Power 1.0, Visibility
  Scale 1.0, Shrink Vertically = on, Shrink Rotation Deg
  −19.0, Shrink Center (15.0, 0.0)**.

### S3 · 0:26–0:44 — Hair parts + hair shader (f014–f022)

- Face close-up. Hair is four Polygon2D parts under `Hairs`:
  **HairBack, HairLSide, HairRSide, HairFront**; `Face` group:
  **Brows, Eyes, Blush, Mouth, Shadow**; `IK` group:
  **LArmIK, RArmIK, LLegIK, RLegIK, HeadIK**.
- f017 (t≈32 s): `HairFront` selected; its material
  `character_hair.t…` uses shader `character_hair…` with
  parameters **Enabled = on, Frequency 10.0, Amplitude 7.0,
  Wave Length 200.0, Speed 0.5**; the Frequency slider is
  being dragged (value reads 8.345 in f017) — a vertex/wave
  sway shader on the hair parts, tuned live.
- f021 (t≈40 s): the whole `Hairs` group is visibility-off —
  the character is bald; the green pixel pattern is painted
  on the head/body art itself, not on the hair. The hair
  style as worn: pixel-block bob with twin side buns and
  black bows (f017).

### S4 · 0:44–1:04 — Shader eyes: blink + tints (f023–f032)

- The `Eyes` node is a single quad with a **ShaderMaterial**,
  shader **`character_eyes`**, and an attached controller
  script **`eye_shader_controlle…`**. The material's texture
  preview is a plain green quad (f025) or two lid shapes
  (f028) — the eyes are rendered BY the shader, not painted
  as a finished texture.
- Parameter groups on the eye shader (f025/f031): **Textures
  (3 changed), Colors (4 changed), Blink, Idle Motion, Pupil
  Control, Gaze Deform, Angle Control, Advanced Blink, Soft
  Shadow**.
- f028 (t≈54 s): **Blink** group open — **Blink Amount 1.0,
  Lower Lid Ratio 0.4** — and the character's eyes are fully
  closed with shaped lower lids. Blink is a shader state, not
  a swapped sprite.
- f031 (t≈60 s): the color picker is open on **Sclera Tint**,
  HDR value **Color(4.869, 0.0, 5.898)** — the sclera glows
  magenta. **Pupil Tint** (red) and **Highlight Tint** (white)
  sit beside it. Across f030–f033 the eyes cycle red →
  magenta → blue: eye color is a live tint parameter set.

### S5 · 1:04–1:12 — Part-assembly state (f033–f036)

- f036 (t≈70 s): the limb polygons (`LArm, RArm, LLeg, RLeg`
  under `Polygons`) are visibility-off; the figure is a
  torso + head only, floating over the still-visible penis
  sprite and selection handles. The demo is showing the
  assembly structure: the character is a sum of toggleable
  part polygons.

### S6 · 1:12–1:26 — Posing + body physics parameters (f037–f043)

- Full body returns; the reclining pose varies across frames
  (limbs repositioned — the rig in motion, frame-sampled).
- f042 (t≈82 s): **`BodyPhysics`** node selected, script
  **`body_physics.gd`**. Parameter surface read numerically:
  **Follow Strength 0.35, Friction Drag 0.001, Stiffness
  120.0, Damping 13.0, Wobble Strength 0.12, Wobble
  Stiffness 55.0, Wobble Damping 45.0, Velocity Smooth
  10.0**; group **Dynamics & Pull-out**: **Pull Out Force
  35.0, Intensity Stiffness Mult 1.6, Bottom Out Mult 1.1**;
  group **Impact**: **Thrust Threshold 250.0, Thrust Impulse
  150.0, Thrust Cooldown 0.02, Impact Depth 0.9**.
- Scene tree lower section: bone chains `L_arm/r_arm/L_leg/
  r_leg`, and a **`SoupGroup`** containing **`HairsJiggle`**
  and **`BoobsJiggle`** nodes — jiggle is a named subsystem
  with per-part nodes.

### S7 · 1:26–1:34 — Polygon + bone-weight authoring (f044–f047)

- f044 (t≈86 s): the bottom panel opens the Polygon2D editor
  on **`Body`**: tabs Points / Polygons / UV / Bones. The
  Body polygon is one painted torso texture cut into a
  triangulated mesh with interior bone points. Inspector:
  Polygon2D `Body`, Offset (−829.135, −1312.295), texture
  thumbnail = the whole character sprite.
- f045–f047 (t≈88–94 s): the panel switches to **Weights**:
  bone-weight heatmap ("Full Heatmap", "Direct (No Brush)",
  Smooth / Edit Bones / Auto Weights, Normalize, Pie Chart)
  over the Body polygon; the bone list reads **root, spine,
  spine, spine, boobs, boobs, spine, head** — the same
  Skeleton2D the parts are skinned to. The video ends
  mid-authoring, in the weight painter.

## 2. Design language (agent read, from frames)

Only ONE character is shown, so cross-character commonality
cannot be assessed — that absence is itself recorded in the
claims table. For the one design shown:

- **Rendering style:** hand-painted 2D anime illustration,
  soft cel shading with glossy specular highlights, drawn as
  separate part sheets (body, limbs, head, 4 hair parts, 5
  face parts) and skinned to a 2D skeleton — a puppet, not a
  model: despite the full-screen editor, nothing in the 94 s
  is 3D.
- **Silhouette/proportions:** adult female, large bust,
  narrow waist, twin-bun hair with bangs; presented in a
  reclining pin-up pose for the whole runtime.
- **Palette/pattern:** a Minecraft-Creeper parody skin —
  mottled pixel-block greens across body AND hair, red eyes.
  The pixel pattern is painted into the part art (it survives
  the hair being hidden, f021), i.e. "skin" here means the
  painted part set + a parameter bundle, not a recolor pass
  alone — though tint parameters (eye tints, NSFW Colors)
  ride on top.

## 3. Provenance classes kept separate

- **On-screen demonstration** (S1–S7 above): what the editor
  shows working. Strongest class.
- **Page description text** (INTAKE): the game's feature
  claims in the uploader's words.
- **Linked page text** (itch): the developer's feature copy.
- **Spoken lines:** a quiet English voiceover, 11 segments
  (transcript in the run dir; timestamps from the whisper
  log). The spoken claims align with the visual segments —
  Soup IK at 0:07 while the skeleton is on screen, hair
  shader at 0:32 during S3, eyes at 0:43 during S4, parts at
  1:05 during S5, procedural bones at 1:19 during S6, Poly
  Rig at 1:24 during the S7 weight/mesh authoring. The
  voiceover names two plugins the frames alone could not
  identify: **Soup IK** (modified by the author) and **Poly
  Rig** (paid, "$6").
- **On-screen text overlays:** none in any of 47 frames. The
  only text is the Godot UI itself.

## 4. SHOULD-BE-SEEN scored item by item

Plan's SHOULD-BE-SEEN: "A devlog teaser: character designs
shown, a pipeline claimed in outline, a game promised."

| # | Expected item | Seen? | Evidence |
|---|---|---|---|
| 1 | Character designs shown | PARTIAL — exactly ONE design shown, in depth | S1–S7; no second character in 47 frames |
| 2 | A pipeline claimed in outline | EXCEEDED in kind, ABSENT in form — no outline is stated anywhere (no narration/text), but a full pipeline is DEMONSTRATED in the editor | S1–S7 |
| 3 | A game promised | YES — by page copy only (description + linked itch page, v0.4.0); the video itself shows no game | INTAKE |
| 4 | (implied by "DevLog") explanation of what changed / what was built | PARTIAL — a voiceover explains the character system in outline (11 short segments), but nothing about what changed since a previous state, and no development narrative | §3, transcript |
