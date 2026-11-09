# Plan 02 — Pass 3 Clean-Room Rebuild

Rebuilt from `TECHNIQUE.md` alone (video closed). Estate
toolchain: Blender 5.2.3 (Arch build `/usr/bin/blender`,
Python 3.14.8 — recorded per the two-build rule; this job class
— scripted scene build + Cycles render, no IK/Rigify
generation — is not the official-binary class), primo headless,
canonical argv (`-b -Y --factory-startup --offline-mode
-noaudio -t 8 --python-exit-code 1`), one heavy job at a time.

## Deliverable mechanism

- Build script: `rebuild/build_template.py`
  (SHA-256 85151f396641ecbdfd327e995b41b79edc9b8efc934aaf65fa681d86c22ae2c7).
  A parameter block at the top carries every distilled value;
  ESTATE-CHOICE entries fill Pass 1 UNREADABLEs and are marked
  as choices in the script header comments.
- Inputs: a COPY of Prima's conformed rig
  (`prima-src/prima.blend`, SHA-256
  50dfd83c9d5c409af9e1d5e2046f1a9b49d3384ea942ecf059f783cd137d3f92,
  byte-identical to the fleet file; fleet files never modified).
  Census of the rig (this run, primo): Armature 54 Mixamo bones;
  Prima_Body 3,084 verts, 38 shape keys; objects Prima_Hair,
  Prima_Outfit (Shirt+SkirtP — the clothed variant),
  Prima_OutfitEnd (DressPink); Skin material = single
  Principled, Roughness 0.85, Subsurface Weight 0.0 at rest.
- Outputs per variant: `template-<variant>.blend`,
  `parameters-<variant>.json`, `fingerprint-<variant>.json`,
  `render-<variant>.png`. Named collections: NS02_TEMPLATE →
  LIGHTING_RIG (Key_Area, Fill_Area, Rim_Spot,
  Accent_Point_1…4), CAMERA (Template_Camera), BACKDROP
  (Backdrop), CHARACTER (the Prima objects).
- Template parameters AS BUILT (numeric core):
  - Camera: 1080×1920, lens 35.0 mm, loc (0.8, −2.1, 1.42),
    target (0, 0, 1.02).
  - Key_Area: AREA RECTANGLE 0.6×1.0 m, 1000 W, colour
    (0.85, 0.92, 1.0), loc (−2.6, −3.2, 3.0).
  - Rim_Spot: SPOT 1000 W, spot 55°, blend 0.150, colour
    computed from backdrop hue HSV (0.90, 0.932, 1.0) →
    RGB (1.0, 0.068, 0.612), loc (1.6, 1.5, 2.1).
  - Fill_Area: AREA RECTANGLE 4.0×3.0 m, 150 W (estate choice
    filling UNREADABLE 2), white, loc (0.2, −3.6, 1.7).
  - Accent_Point_1…4: POINT 5 W, white, radius 0, at
    (±~1.0, ±~1.2, 0.9–1.8).
  - Backdrop: curved cyclorama mesh 12 m × 5 m; Principled
    Roughness 0.5 with procedural neon gradient (teal → blue
    → magenta) into Base Color AND Emission Color, Emission
    Strength 0.7 (estate choice, UNREADABLE 1). World
    Background Strength 0.0.
  - Skin pass (copy only): Roughness 0.50, Subsurface Weight
    0.20, Subsurface Radius (1.0, 0.35, 0.20).
  - Render: Cycles, CPU, Max Samples 4096, adaptive Noise
    Threshold 0.0100, Denoise ON (OpenImageDenoise — estate
    choice, UNREADABLE 3), seed 0 fixed, Simplify asserted
    OFF, exposure −1.8 (estate choice), view transform = the
    running version's default (UNREADABLE 4).
  - Pose (Target 2 order; degrees in `parameters-nswfw.json`):
    hips yaw −6° with weight offset (0.015, 0, −0.008), spine
    counter-yaw +4/+3/+2°, head turned −12° Z / −5° X toward
    camera, left arm raised bent (Arm −55° X, ForeArm −78° X,
    hand at shoulder height), right arm relaxed, legs lightly
    staggered. The three-quarter turn is the CAMERA's (C-02-2).
    Pose signs were measured with a numeric probe on this
    armature (rest hand (0.276, 0.008, 0.862); LeftArm X−35 /
    ForeArm X−55 → hand (0.337, −0.392, 1.130)) after two
    render probes showed axis/sign errors — recorded here as
    the iteration cost of an undocumented rig convention
    (Prima's own build script's strain pose was the cross-check:
    X = bend, Z = yaw).

## Determinism (the Pass 3 gate)

- Scene-data fingerprint (sorted objects/lights/camera/render
  + full parameter block, SHA-256 of canonical JSON):
  NSFW variant **ca585ca41656ea6e3a80c504143eb1d504ee717cecb8034b4d9b199bcbb5570a**
  — IDENTICAL across two independent runs (final-nswfw1.out,
  final-nswfw2.out). SFW variant fingerprint
  acc3f09d2c4a627469f580a0181ee7dc05a1b543d44726c087d4d42680bdaaf9
  (differs only by the outfit-visibility parameter).
- Render determinism: two full renders of the NSFW variant —
  decoded-pixel SHA-256 **b510fafaa0a9e7268ba0813110445cbe510e8539bbfe5c6d4c3d155a7e916471**
  for BOTH (RGBA bytes via PIL). PNG file bytes differ by
  5 bytes (3,318,244 vs 3,318,249 — container metadata); the
  specified criterion is the decoded-pixel hash: PASS.
- Render wall time: 07:12.710 for the saved NSFW still
  (Blender's own timing line, final-nswfw1.log), CPU 8 threads,
  alongside a tenant GPU-training job.
- Run record: all three final runs rc=0 with the
  `OK ns02_template_<variant>` sentinel (detach log
  `ns02-final.log`: nswfw1 rc=0, nswfw2 rc=0, sfw rc=0).

## Iteration record (v1 → final)

- v1 (fingerprint 25144e34…): blown-out white figure +
  A-pose arms (wrong rotation axes) + black wedge under a
  too-short backdrop floor. Diagnosed by Workbench probe
  (materials intact — skin pixel (169,161,155); fault was
  exposure/axes/geometry, not materials).
- v2–v5 probes (128 samples, 540×960): pose rebuilt on the
  rig's measured convention; backdrop floor extended to
  y=−2.6; gradient darkened; exposure swept −2.0 → −3.0 →
  −2.6 → −1.8 (locked −1.8: backdrop keeps the video's neon
  glow class, skin stops clipping).
- Final framing fix: camera (0.95,−2.75) → (0.8,−2.1) after
  the first full render measured the figure at ~55% of frame
  height vs the video class's ~85% (final: ~72% — the video's
  DELIVERED still is additionally a crop of its render, see
  PASS4).

## Claims scored as tests

| Claim | Score | Evidence |
|---|---|---|
| C-02-1 camera-first defaults | REPRODUCED | Template opens with camera+format; still framed before posing in build order |
| C-02-2 never move the model | REPRODUCED (as gate) | Script asserts armature object location == (0,0,0); three-quarter achieved by camera |
| C-02-3 simplify discipline | REPRODUCED (as gate) | Script asserts use_simplify is False before render; interactive half is a GUI act, not scriptable — mechanism carried as the assertion |
| C-02-4 manual posing order + finger contact | PARTIAL — order REPRODUCED; finger-contact UNTESTABLE-IN-ROUTE | Pose built gross→fine in script order; Prima holds no prop in this still, so grip-contact has no object to test against (no whip prop exists in the estate rig) |
| C-02-5 emissive backdrop + world 0 + no HDRI | REPRODUCED | Silhouette-first state verified in v1 probe sequence; final still lit solely by rig + emissive ground |
| C-02-6 role rig with his values | REPRODUCED with two estate-filled values | Key/rim/accent values as evidenced; fill power and backdrop emission strength are the UNREADABLE-filled choices, named in the script |
| C-02-7 skin dials | ADAPTED-REPRODUCED | Dial intent mapped to Principled (roughness 0.50, SSS weight 0.20); DAZ dial scale does not transfer 1:1 — recorded at the claim in TECHNIQUE.md |
| C-02-8 Cycles 0.0100/4096 | REPRODUCED | Preset as built; **version drift recorded:** source Blender 4.0 → estate 5.2.3 (lamp/SSS semantics differ across versions; the preset ports, the exact pixel outcome cannot be claimed identical) |
| C-02-9 LR blur + PS signature post | UNTESTABLE-IN-ROUTE | Lightroom/Photoshop are not estate tools; the template ships the deep-focus render the post step consumes (the video's own render is likewise deep-focus — §7 of OBSERVATION). Named external step, not faked |
| C-02-10 portability | TESTED in Pass 4 | Different character (Prima vs Poison), different backdrop (procedural vs photo), same template |

Stills produced: `rebuild/render-nswfw.png` (1080×1920,
3,318,244 B, file SHA-256
e4a11af753772db0dc2e33635db60e11d609aa66d66f9e2b8757a513e1dc53a2)
— keeper-CANDIDATE, not a keeper; `rebuild/render-sfw.png`
(SHA-256 de804f3213c77abd82faf4467c46519a666eabd5f92717e618914fb8e88341a6).
