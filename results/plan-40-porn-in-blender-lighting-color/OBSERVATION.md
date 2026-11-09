# Plan 40 — Pass 1 Observation (screen-governed, timed, frame-evidenced)

Source: "How to Make Porn In Blender: Basics - Lighting and Color
Grading", rule34video ID 3213694, creator/uploader/presenter **Anime
Nyan**, uploaded 2023-12-23, licence **CC0 as seen** (MANIFEST.md).
Capture: 1080p, 2,898,146,377 B, SHA-256 0b3eebdd…, verified duration
6884.033 s, full decode 0 error bytes (MANIFEST.md).
Frame base: grid `g(n)` ≈ (n−1)×120 s, 640 px; native `t(n)` =
2280+(n−1)×60 s, 1920×1080; targeted `x<sec>` = exact second. Presenter
picture-in-picture bottom-right throughout; he works in **Blender 4.0**
(title bars) and **DaVinci Resolve Studio 18** (footer).
Pre-registration: INTAKE.md (Q40-L1/L2/C1/G1/G2, TQ-1…TQ-5) — written
before frame viewing.

## 0. SHOULD-BE-SEEN check

INTAKE adopted the plan's expectation: "a basics course treatment:
light types and placement for bodies, exposure discipline, then colour
grading in render/compositor — with the reasoning shown on examples."
**Seen, with two structural corrections.** (1) The lighting teaching
(46:20–~1:24) is done on a *worked example character* — the lighting is
demonstrated by dissecting and re-tuning an existing lit scene, not by
lecturing light theory; the first ~46 min are character
download/pose/face/camera work outside this plan's scope. (2) The
grading does **not** live in the Blender compositor at all — it lives
entirely in **DaVinci Resolve**, fed by a deliberately dark linear EXR.
The "reasoning shown on examples" expectation holds: every setting
below was read off a panel while he worked, not stated in a slide.

Two files alternate on screen and must not be conflated:
- **Reference file** "Yoruichi thumbnail 2.blend" (Mushen Thumbnail
  project): a finished, multiply-camerad lit scene, opened to show
  where the method lands (t0010, 47:00).
- **Build file** "Yoruichi_v1_FltdLh!.blend" (environment tutorial
  folder): the scene actually built and re-lit across the video
  (x2790 onward). All build-sequence reads below are the build file
  unless marked "reference file".

## 1. Chapter map vs screen (page chapters are approximate)

The page's chapter list (MANIFEST.md) is a viewer's map (credited to
vadimbanshee405) and the screen deviates from it: Resolve is already
open with a full grade applied at 84:00 (t0047), *before* the listed
"Render Settings 1:24:50 / DaVinci Resolve Start 1:27:00"; face-posing
work recurs inside the lighting chapters (t0034, 71:00). **The screen
governs; chapter times are ±several minutes.** Sections below use
screen timestamps.

## 2. Scene assembly (0:00–46:20) — context only

- 0:00 (g0001): the delivered thumbnail still: low-key bathroom scene,
  kneeling figure, warm circular-mirror practical behind, cool
  blue-purple suit light, teal pool edge. This image is the lesson's
  target look.
- Downloads/add-ons/character chapters (3:37–29:35): DAZ Genesis 8
  Female character (MHX-style rig panel, g0019), pose and face work
  (g0006, g0011, t0034), PureRef for reference images.
- Environment (29:35–39:50): a pre-built bathroom set is appended from
  .blend assets (file explorer over "environment tutorial" folder,
  g0016) into a **"Whole Environment" collection** — the set is a
  separate collection from the character from birth, which is what
  makes the lighting method of §3 possible.
- Camera (39:50–46:20): camera views of the posed character against
  transparency (t0005, 42:00). The reference file carries **two
  cameras** (Camera.001, Camera.002 in its outliner, t0010). Focal
  length: UNREADABLE (U2 — Lens section never expanded in any sampled
  frame).

## 3. Lighting build (46:20–~1:24) — the plan's core

### 3.1 Starting state: world zeroed, silhouette first

At Light Start (x2790, 46:30) the build file's world panel reads:
**World "Yoruichi World", Background Color = texture
"DTHDR-RuinsB-500" (an HDRI is loaded), Strength 0.000.** An HDRI is
present in the file and deliberately zeroed — the character renders as
a **pure black silhouette** on transparency (x2790, t0013, t0016) and
every lamp is added against that black. The environment collection is
hidden from the render (outliner eye states, t0020): **the character
is lit alone; the set contributes nothing while the rig is built.**

### 3.2 The rig (outliner census across frames)

Build-file outliner, union of reads (t0013 → t0020 → x3300 → t0040 →
t0044): **Area, Area.001, Area.002, Area.004** (objects; data up to
**Area.005**), **Point, Point.001, Point.002**, **Spot, Spot.001,
Spot.002** — i.e. **≥10 lamps: ~5 Areas, 3 Points, 3 Spots**, plus a
**Plane** object placed in the light path (§3.4) and the cameras.
Growth is incremental and *replacement-friendly*: at 50:00 (t0013)
only **one Area** exists; by 53:00 (t0016) the outliner shows 3 Areas
+ 2 Points + 2 Spots, and the same frame's status bar reads "Deleted
1 object(s)" while he adds another Spot — lamps are deleted and
swapped freely while tuning, never treated as precious.

### 3.3 Lamp panel reads (every value the screen showed)

Common to **every** panel read: Max Bounces 1024, Cast Shadow ✓,
Multiple Importance ✓ (defaults, never changed on screen).

| Lamp | When | Type / Color | Power | Geometry | Source |
|---|---|---|---|---|---|
| Area.003 (reference file) | 47:00 | Area, **pink/magenta** swatch | **8.8 W** | Ellipse 100×100 cm, Spread 180° | t0010 |
| Spot | 65:00 | Spot, white | **25.7 W** | Radius 0 cm, **Spot Size 14.2°, Blend 0.732** | t0028 |
| Point.001 | 62:00 | Point, white | **10 W** | Radius 1 cm | t0025 |
| Point.001 (retuned) | 70:00 | Point, white | **1 W** (typed on screen) | Radius 0.1 cm | x4200 |
| Area.005 (data, obj Area.004) | 74:00 | Area, white | **10 W** | Ellipse **16×45 cm** (strip), Spread 180° | t0037 |

Scale verdict: the largest lamp ever read is **25.7 W**. The rig is
*many small, close, low-power lamps*, each placed within roughly a
body-length of the subject (viewport gizmos, passim) and tuned one at
a time against the live rendered pane. No lamp approaches the
kilowatt class of Plans 02/11/13/17's fixtures. Colour lives in
individual lamps (the pink Area.003) and in the grade, not in a
coloured backdrop.

### 3.4 Placement practice and the rim question (TQ-2)

- Lamps are aimed by dragging in the viewport while watching the
  rendered pane (G/R key overlays, passim); positions are sculptural,
  not measured — no transform values are ever typed for a lamp in any
  sampled frame.
- **Rim/back practice (x3300, 55:00):** Spot.002 is placed *behind*
  the character and rotated (−170.74° about Z in the header) from a
  top view; the rendered pane at that instant shows the silhouette
  with a thin vertical edge of light — the spot is being walked onto
  the body's camera-side edge from behind. Nothing in the scene
  stands between this spot and the character: the environment
  collection is hidden, and no backdrop wall exists in the build
  file's character space. **His rim geometry cannot repeat Plan 11's
  dead-rim failure, because there is no wall** — the failure mode is
  designed out by lighting the character in empty space, not by any
  stated rim rule (he never mentions occlusion; the protection is
  structural, not verbal).
- **The Plane (gobo):** a single large Plane object sits in the light
  path above-left of the character in the solid view (x2790, t0020,
  t0044 black triangle). Its placement is deliberate and it is moved
  with the rig. Its material/purpose is never shown in the Shading
  workspace in sampled frames — **UNREADABLE (U6)**; placement is
  consistent with a shadow-flag/gobo (or matte card). Recorded as
  placement-only evidence.

### 3.5 Environment reunion and the interior fix (~76:39–83:00)

- The environment collection is switched back on (t0040, 77:00): the
  set's own practicals — the **warm mirror ring** and a **hanging
  lamp** — become the scene's warm sources in the render, against the
  cool lamp rig on the character. A Point.001 appears in the outliner
  alongside the rig (set-side point tuning is part of this section).
- **Interior Light Fix, mechanism (x4700, 78:20):** in the Shading
  workspace he edits a set material — "01_Wall-Key" on a wall-trim
  mesh (Line034.001/Mesh.025; Quixel-class 2K albedo
  `ugcoeg0s_2K_Albedo.jpg`, Principled, Metallic 1.000 / Roughness
  0.553 mid-edit) — and wires a **Light Path node into a Transparent
  BSDF**, the standard construction for making set geometry stop
  blocking light/camera rays. A ceiling mesh ("Ceiling.002") is the
  selected object in the adjacent frames (t0040). Read: **the
  "interior light fix" is a ray-visibility fix — set geometry that
  was eating the light is made ray-transparent — not a lamp change.**
- Camera finish (t0046, 83:00): **Depth of Field ON, Focus Distance
  121 cm, Aperture F-Stop 2.4**, Blades 0, Ratio 1.000 (the t0045
  frame catches the same panel mid-edit: 1000 cm / 2.8 being typed —
  the settled read is t0046's). Clip Start 40 cm / End 100000 cm
  (t0045). The delivered stills' soft backgrounds are **real
  render-time DoF**, not a post effect.

## 4. Render settings (84:10–86:00)

Read at x5050/x5120/t0048/t0049, in his own order of operations:

- **Format: 3840×2160 at 75% → 2880×1620 effective**, 30 fps project,
  frame range 1–250 (t0048). Landscape 4K-class — not portrait.
- **File Format: OpenEXR** (menu changed from FFmpeg Video on screen,
  x5050); saved via Save As Image as **single-layer OpenEXR, RGBA,
  Float (Full), Codec DWAA (lossy), Color Management "Follow Scene"**
  (t0049). (Single-layer, not MultiLayer — the MultiLayer menu entry
  is visible and not chosen.)
- **Cycles, GPU Compute, Feature Set Supported** (x5120):
  - Viewport sampling: **Noise Threshold 0.1000, Max 1024, Min 0**.
  - Render sampling: **Noise Threshold 0.0100, Max Samples 128,
    Min 0**, Time Limit 0.
  - **Denoise ON: OptiX, passes Albedo and Normal.**
- Render Result header at the save (t0049): "Frame: 0 | Time:
  00:20.29 | Mem: 2778.29M, Peak: 2928.58M" — recorded verbatim; a
  ~20 s render is consistent with the 0.0100/128 ceiling at
  2880×1620 on GPU, and with the heavy noise visible in his viewport
  renders (t0037, t0044): **the render is intentionally undercooked
  and the noise budget is spent downstream** (OptiX in Blender, then
  Resolve NR, §5.3).
- **Two EXRs reach Resolve** (media pool, t0051): "render 1.exr" and
  "character + enviro…" — a **character-only render and a combined
  render** are both produced. The character-only pass is a direct
  consequence of the §3.1 separability: the rig was built with the
  set hidden, so a set-free render costs one visibility toggle.
- **Blender colour management (view transform / look): never
  displayed in any sampled frame — UNREADABLE (U1).** The EXR is
  saved "Follow Scene"; what reaches Resolve is near-black (§5.1),
  i.e. the scene-referred linear data does the travelling and no
  Blender look is baked into the deliverable path that the screen
  shows.

## 5. The grade — DaVinci Resolve Studio 18 (from ~84:00 to end)

### 5.1 The raw material

The ungraded EXR in Resolve's viewer (t0051, 88:00) is **drastically
dark**: the figure is near-black; only the mirror ring and the
hanging lamp read. The delivered look (g0001, t0047 viewer) is built
in Resolve from this near-black linear plate. Exposure is therefore
a *grading* act in this pipeline, not a render act.

### 5.2 Project colour management (x6500, 108:20)

Project Settings → Color Management, read in full: **Color science
DaVinci YRGB; Timeline color space Rec.709 (Scene); Output color
space "Same as Timeline"; no input/output/monitor LUTs selected.**
The gallery's saved-look names (§5.5) carry both "YRGB -" and
"Managed Wide Ga(mut)" prefixes — he keeps looks for both colour
management modes; the project of record for this video is YRGB.

### 5.3 The two node trees

**(a) The PowerGrade tree** (clearest read t0067, 104:00; also
t0047, t0061) — a saved, reusable grade, 10 numbered nodes (+ a
grey-thumbnail corrector hanging under node 03). Labels as displayed
(truncation is Resolve's; full text UNREADABLE, U5):

01 **Base Enc…** → 02 **Filmic Bl…** → 03 **highlights** (sub-label
"correc to…") → 04 **printer li…** → 05 **primaries** → 06 (icon
node; the teal/orange step in the t0047 layout) → 07 **look to…** →
08 **look adj…** → 09 **glow** → 10 **grain**.

This is the Qazi-derived structure (the description credits Waqas
Qazi's teal-and-orange tutorial; the tab bar at t0055 shows the
sobotka/**filmic-resolve** GitHub open — "Filmic Bl…" is Sobotka's
Filmic port for Resolve). Function by position: base encoding →
filmic blend → highlight control → printer lights → primaries →
teal/orange split → look → look adjust → glow → grain.
Primaries-wheel reads inside this tree: t0061 (node 07 selected):
Lift (0.00, −0.06, 0.02, −0.03), Gamma (0.00, 0.01, −0.01, 0.05),
Gain 1.00×4, Offset 25.00, Temp 0.0, Tint 0.00, Contrast 1.000, Pivot
0.435, Sat 50.00; t0067: Lift (0.00, −0.07, 0.02, −0.04), Gamma
(0.00, 0.04, −0.02, 0.04) — small, taste-class nudges on a saved
structure, applied per image. Mid-teaching state at t0061 shows the
method's signature overshoot (image pushed strongly green-teal
before the look nodes pull it back) — the teal/orange balance is
*found by pushing past it*, with the Parade scope open (t0061,
t0067).

**(b) The compact delivery tree** (t0073, t0076, x6500) — 8 nodes,
the tree actually sitting on the delivered clip late in the video:
01 → 02 **Base Enc…** → 03 **Denoising** → 04 **Contrast** → 05
**Color** → 06 **Base Co…** → 07 **Vignette** (+ **Sharpeni…**) →
08. Node 03's settings are read in full (t0076): **Spatial NR —
Mode Faster, Radius Small, Threshold Luma 5.0 / Chroma 5.0; Temporal
NR — Frames 1, Motion Estimation Faster, Range Medium, Threshold
Luma 11.6 / Chroma 11.6 / Motion 50.0; Motion Blur 0.0.** The
Blender render's noise (§4) is finished here, in the grade, by
design.

Which tree "is" his grade: the screen shows both in use on this
project — the PowerGrade as the look library he teaches from
(§5.4/§5.5), the compact tree on the final clip. The honest record
is a **two-layer practice**: a saved Filmic/Qazi PowerGrade for look
development, and a short delivery chain (encode → denoise → contrast
→ colour → base → vignette/sharpen) for the shipped still. Any
single-tree summary would misstate the evidence.

### 5.4 The Qazi study segment (92:00, t0055)

The "Color Tutorial for DaVinci Resolve" chapter substantially
*re-teaches from* Waqas Qazi's YouTube video "Orange and Teal Look:
The Mistakes 90% of Beginners Make!" — played on screen with its
chapter list visible (Beginner's Look 3:15, Pro's Look 5:41, …) and
its subtitle line readable ("So let's subtract some magenta by
adding green"). His colour teaching is explicitly derivative of
Qazi's method plus the Sobotka Filmic port, assembled into his own
saved PowerGrade. Provenance is credited in his own video
description (MANIFEST.md).

### 5.5 The look library and delivery (107:00–end)

- Gallery "PowerGrade 1" album (t0070, x6500): saved stills named
  **"YRGB - Purple Contr…", "YRGB - Electric Satu…", "YRGB - Green
  Yellow", "YRGB - Contrast Sat…", "YRGB - Purple War…"** and a run
  of **"Managed Wide Ga…"** stills — a personal library of named
  looks, auditioned against the clip (t0070 shows a single node in
  the graph while a purple still is applied). Part of the "house
  look" is literally *which saved still he reaches for*.
- Delivery (x5560, 92:40 — file explorer over his "Anime Nyan
  environment" folder): grades are exported as **.drx + PNG pairs**,
  versioned: "environment v2…v7" (each with _1.1.x gallery suffixes),
  "new tutorial image_1.2.1.drx/.png", plus "render 1.exr" (with a
  .djv viewer sidecar). Versioned iteration, not one-shot export.

## 6. Answers to the pre-registered intake questions

- **Q40-L1 (light types/placement):** ANSWERED. Types: Areas
  (ellipse, incl. a 16×45 cm strip), narrow Spots, Points; ~10
  lamps; placement is close, sculptural, one-at-a-time against the
  live render, character isolated from the set (§3).
- **Q40-L2 (exposure discipline):** ANSWERED, inverted from the
  expectation. There is no in-Blender exposure discipline to read:
  lamps are tuned by eye, the world is zeroed, the render is
  deliberately dark/linear, and **exposure is decided in the Resolve
  grade** (§5.1). Discipline exists, but it lives downstream.
- **Q40-C1 (colour management numerically):** ANSWERED for Resolve
  (YRGB; Rec.709 (Scene) timeline; no LUTs, §5.2). Blender side:
  UNREADABLE (U1) beyond "Follow Scene" on the EXR save.
- **Q40-G1 (grading-chain location):** ANSWERED. **External tool**
  (DaVinci Resolve), two trees (§5.3); Blender compositor never
  appears in any sampled frame.
- **Q40-G2 (grading contract across scenes):** ANSWERED as a
  *saved-structure* contract: the chain survives across scenes
  because it is stored (PowerGrade + .drx + gallery stills) and
  re-applied, with per-image wheel nudges of ±0.07 class. The
  contract is the node structure + the denoise settings, not a set
  of fixed grade values.
- **TQ-1 (bake-in-render vs fix-in-comp):** THIRD POSITION (the
  intake's pre-registered third option). He neither bakes (Plan 17)
  nor fixes-in-comp inside Blender (Plans 11/13): he **renders a
  dark linear plate and finishes in an external colour tool** —
  "fix-in-Resolve". The render is a capture step; the look is a
  post step, in a different application.
- **TQ-2 (rim vs dead-rim geometry):** ANSWERED (§3.4). His
  construction makes the failure structurally impossible (no wall;
  character lit in empty space), without ever naming the risk.
- **TQ-3 (backdrop/world):** ANSWERED. HDRI **loaded and zeroed**
  (x2790) — agreement with Plan 02's zero-world *effect* by a
  different mechanism; the visible background is a real set with its
  own practicals, not an emissive cyclorama and not a gradient
  world.
- **TQ-4 (render pair):** ANSWERED. **0.0100 / 128** + OptiX +
  Resolve NR (x5120). The 0.0100 threshold now agrees across 02 and
  40; the ceilings disagree by 32× (4096 vs 128) — the ceiling is
  ceremony, the threshold is the shared constant; his missing
  samples are bought back with two denoise stages.
- **TQ-5 (rim colour):** ANSWERED by absence. His rim/spots read
  **white**; colour enters via a pink Area accent and the grade.
  Neither sampled-from-scene (Plan 02) nor neutral-by-stated-rule.

## 7. UNREADABLE register (counted, never guessed) — 7

- U1 Blender view transform + look — panel never displayed.
- U2 Camera focal length — Lens section never expanded on screen.
- U3 The main key Area's final power/colour — only Area.003
  (reference file) and Area.005 data were panel-read; the build
  file's principal key was never selected at native resolution.
- U4 Sun lamp — Add-menu hovered at 80:00 (t0043); no later panel or
  outliner confirmation in sampled frames.
- U5 Full text of truncated Resolve node labels (Base Enc…, Filmic
  Bl…, look to…, Base Co…, printer li…, teal oran…).
- U6 The Plane object's material and stated purpose (placement
  only).
- U7 Per-node values inside the PowerGrade beyond the two
  primaries-wheel reads (individual node internals never opened at
  readable size).

## 8. Speech (slice ladder — [SPOKEN], UNCONFIRMED tier)

Census rule per skill: normalized-segment-v1, threshold >8; the
census is a screen, not a verdict. No claim in §§2–7 rests on speech.

**Slice E (0–480 s) — LANDED and censused** (`slices/E.txt`,
1,446 words): 163 segments, 22 loop segments (13.5% — above
threshold; loop-class segments quarantined), 141 recoverable
segments, 1 loop phrase. [SPOKEN] confirmations from the
recoverable body:

- The presenter self-identifies — "AnimeNyan here" — corroborating
  creator = presenter (§0).
- The pipeline is stated in his own framing, verbatim in substance:
  pose the character, light the character, add an environment and
  another character, "render as EXR, and then also color grade the
  image in DaVinci Resolve" — speech confirms the screen-derived
  pipeline (§§3–5) at the video's own introduction.
- Provenance confirmed in speech: the EXR workflow is credited to
  Polyfjord (whisper renders "Polly Ford"); the colour grading was
  "stole[n] from another video" (Qazi — §5.4).
- The bathroom set is a paid Blender Market environment by "Trum
  Studio" ($19) [SPOKEN] — the set's provenance (§2).

**Slices A–D and the full chunked lane — still in flight at
delivery** (wave contention; `ns40-chain` running on primo).
`finish.sh` is staged in the primo plan dir: on chain completion it
stitches the full transcript (chunk2 offset +3300 s, `[SEAM]`
marker), censuses every slice, and writes `SPEECH-ADDENDUM.md`.
Coverage is stated honestly: at delivery, speech covers 480 of
6,884 s (7.0%), all of it introductory; every parameter claim in
this record is screen-governed.

## 9. Claims carried to Pass 3 (the rebuild's test list)

- **C-40-1 (separability):** the subject read of his stills is
  produced by the lamp rig alone over a zero world; the set adds
  background and practicals, not subject key light.
- **C-40-2 (lamp scale):** many small close low-power lamps
  (≤25.7 W read) produce a falloff/wrap pattern that a single
  kilowatt-class key at template distance does not reproduce at
  matched framing.
- **C-40-3 (live rim):** his behind-subject spots contribute
  measurable edge energy (geometry unobstructed by construction) —
  the anti-Plan-11 case.
- **C-40-4 (grade carries the look):** the delivered look is not in
  the render; from the same scene data, render-only output reads
  materially darker/flatter, and a compositor translation of his
  Resolve chain recovers the bulk of the difference.
- **C-40-5 (noise economics):** 0.0100/128 + OptiX leaves visible
  noise that his chain expects Resolve NR to finish; the pair is a
  system, not a render setting.
- **C-40-6 (real DoF):** f/2.4 at 121 cm is a look component
  (background softness in the delivered stills), where Plan 02's
  template is deep-focus.
