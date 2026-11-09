# Plan 12 — Pass 2 Distillation: Claims Table, Factory Shape, Comparison

Marks: **VERIFIED** = seen working / corroborated by a second
source · **UNVERIFIABLE** = claimed, not shown · **ABSENT** =
expected in a character-factory artefact, nowhere present.
Provenance classes: [demo] on-screen demonstration · [page]
rule34video description text · [itch] linked itch page copy ·
[title] the video's title · [voice] the video's own voiceover
(transcript in the run dir; quotes are whisper's rendering,
checked against the frames where the frames can check them).

## 1. Claims table

### 1a. Demonstrated in the video [demo] — all VERIFIED as editor-level fact

| # | Claim (as demonstrated) | Evidence |
|---|---|---|
| V1 | A character is an assembly of separate hand-painted part polygons — Body, LArm, RArm, Head, LLeg, RLeg — individually toggleable | f036 (limbs off → torso only); f044/f047 tree |
| V2 | All parts skin to ONE shared Skeleton2D (bones: root, spine×4, boobs×2, head, ass L/R, hair, arms, legs) with painted per-vertex bone weights | f001/f005 skeleton overlay; f047 Weights panel, bone list |
| V3 | Hair = 4 parts (HairBack, HairLSide, HairRSide, HairFront) animated by a wave shader (Frequency 10.0, Amplitude 7.0, Wave Length 200.0, Speed 0.5; tuned live) | f017, f021 |
| V4 | Face = separate parts: Brows, Eyes, Blush, Mouth, Shadow | scene tree, f021/f025 |
| V5 | Eyes are shader-rendered (shader `character_eyes` + `eye_shader_controller` script): parameter groups Blink, Idle Motion, Pupil Control, Gaze Deform, Angle Control, Advanced Blink, Soft Shadow; tints for Sclera / Pupil / Highlight | f025, f031 |
| V6 | Blink is a shader state: Blink Amount 1.0 + Lower Lid Ratio 0.4 → fully closed, shaped eyes; no sprite swap | f028 |
| V7 | Eye color is a live tint parameter (red → magenta HDR Color(4.869, 0.0, 5.898) → blue across the segment) | f030–f033 |
| V8 | Anatomy deformation is a parameterized shader (`hole_deformer`) on the Pussy polygon: Stretch Amount 36.0, Stretch Power 1.0, Center Offset 0.984, Bend Multiplier 0.55, Curve Power 1.0, Visibility Scale 1.0, Shrink Vertically on, Shrink Rotation Deg −19.0, Shrink Center (15.0, 0.0) | f012 |
| V9 | Soft-body jiggle is a parameterized script system (`body_physics.gd`): Stiffness 120.0, Damping 13.0, Wobble Strength 0.12, Wobble Stiffness 55.0, Wobble Damping 45.0, Follow Strength 0.35, Friction Drag 0.001, Velocity Smooth 10.0, plus Pull-out and Impact groups (Thrust Threshold 250.0, Thrust Impulse 150.0, Thrust Cooldown 0.02, Impact Depth 0.9); per-part jiggle nodes (HairsJiggle, BoobsJiggle under SoupGroup) | f042 |
| V10 | A character's variable data is a SKIN resource: skins live as `.tres` files under `res://src/data/characters/skins/`; the Character root exposes an Editor Skin field + a custom "Save Skin" editor button, and skin-carried color parameters (NSFW Colors: Ass Color, Pussy Color) | f001 |
| V11 | Runtime structure is modular with named module nodes — SexModule {BodyPhysics, LimbsModule, HeadModule, OpeningModule, FluidModule, CumLine}, IK targets (LArmIK, RArmIK, LLegIK, RLegIK, HeadIK), RemoteTransform2D links (BodyRemote, FaceRemote, DickFollow), interaction masking (DickMask > DickPath > DickFollow) | f012, f021, f042 |
| V12 | Toolchain: Godot 4.6.stable (2D editor), GDScript (`character.gd`, `body_physics.gd`, `eye_shader_controller`), custom shaders, one editor plugin visible (SceneTreeAsText) | all frames |

Caveat carried with every V-claim: these verify the EDITOR
surface — parameters exist and visibly change the character
in the editor. Runtime (in-game) behaviour of the same
parameters is not shown anywhere in the 94 s.

### 1b. Claimed in text, not shown [page] / [itch] / [title]

| # | Claim | Source | Mark |
|---|---|---|---|
| C1 | "WaifuFactory is a small NSFW RPG simulator" — the game exists | [page] + [itch] page live at v0.4.0 | **VERIFIED** (existence only) |
| C2 | "explore multiverses of fandoms / discover new worlds" | [page], echoed [itch] "Multiverse unlocking" | UNVERIFIABLE (copy on two pages; nothing shown) |
| C3 | "craft items, gather resources" / crafting & economy, essences | [page] + [itch] | UNVERIFIABLE |
| C4 | "customize characters" | [page] | **VERIFIED at editor level** (V1–V10 are customization machinery, demonstrated); player-facing in-game customization UNVERIFIABLE |
| C5 | Game link resolves to the developer's page | [page] | **VERIFIED** (fetched; SilentCherry, v0.4.0) |
| C6 | Character system: level, mood, preferences affect effectiveness | [itch] | UNVERIFIABLE |
| C7 | RPG progression/leveling, skill system, content collection, gradual expansion | [itch] | UNVERIFIABLE |
| C8 | Windows + Android builds (controls listed for both) | [itch] | UNVERIFIABLE |
| C9 | This is "DevLog #1" of a series | [title] | UNVERIFIABLE (no series evidence in the artefact or on the video page) |
| C10 | "Game Character Design" is the video's subject | [title] | **VERIFIED** (that is literally what the 94 s show — one character, designed in the editor) |

### 1c. Claimed by the voiceover [voice]

| # | Claim (whisper transcript, timestamps from the whisper log) | Mark |
|---|---|---|
| SP1 | 0:00–0:06 "the character is built using standard godot nodes, Skeleton 2D, along with a few plugins" | **VERIFIED** (V1/V2/V12; the plugins are named in SP2/SP10) |
| SP2 | 0:07–0:18 "the first one is Soup IK — it allows you to create higher quality IK and wiggle animations, though I modified it to better fit my needs" | **VERIFIED** for presence/purpose (IK targets V11; jiggle nodes HairsJiggle/BoobsJiggle under **SoupGroup**, f042); the author's modification of the plugin is asserted only — noted, not separable on screen |
| SP3 | 0:22–0:27 "the NSFW parts are just sprites layered on top of the main character" | **VERIFIED** (Ass/Pussy are separate layered Polygon2D nodes, f012) |
| SP4 | 0:28–0:31 "they open and close using simple animations and shaders" | UNVERIFIABLE — the deform shader's parameter surface is verified (V8), but no open/close ANIMATION is witnessed; the segment shows static parameter editing |
| SP5 | 0:32–0:40 "the hair is driven by a simple shader that deforms polygons, creating a soft wind and swaying effect" | **VERIFIED** (V3; shader + live tuning seen; the sway itself is implied by the wave parameters, not distinctly frame-visible at 2 s sampling) |
| SP6 | 0:43–0:56 "the eyes and eyebrows are also controlled and adjusted through shaders" | **VERIFIED** for eyes (V5/V6); eyebrows ride along unproven — Brows is a separate Face part and no brow inspector is ever shown |
| SP7 | 1:05–1:11 "overall the character is made up of separate parts — arms, legs, head and body" | **VERIFIED** (V1) |
| SP8 | 1:12–1:18 "all deformed by bones, which together create a cohesive and visually appealing result" | **VERIFIED** for bone deformation (V2); "cohesive and visually appealing" is an evaluative claim, recorded as opinion, not evidence |
| SP9 | 1:19–1:23 "all bones are controlled procedurally via scripts" | UNVERIFIABLE — scripts and IK/remotes exist (V11/V12), but the totality ("all") is not demonstrable, and S1 simultaneously shows bones being dragged by hand in the editor |
| SP10 | 1:24–1:30 "the second plugin is Poly Rig — it's a paid plugin, I bought it for six dollars" | UNVERIFIABLE — a purchase/identity claim about a plugin; nothing on screen names it (the S7 panels are its alleged workplace) |
| SP11 | 1:31–1:34 "it allows you to create a high-quality mesh" | UNVERIFIABLE as attribution (mesh authoring itself is witnessed, V2/V10 — that the PLUGIN is what enables it cannot be separated from stock Godot panels on this evidence) |

### 1d. ABSENT — expected of a character factory, nowhere in the artefact

| # | Absent element | Why it was expected |
|---|---|---|
| A1 | A second character / any cast variety | A "factory" claim implies >1 product; 94 s show exactly one |
| A2 | Procedural generation, random variation, or body/proportion sliders producing a new character | The plan's core question (procedural? template? generation?) — no generation action of any kind occurs |
| A3 | Gameplay footage of any system (C2/C3/C6/C7 in action) | The page copy promises a game; the video is 100% editor |
| A4 | A skin SWAP — loading a different skin to produce a different character | The skin system is the factory's variation claim (V10); its fields are shown, a swap is never performed |
| A5 | Any consistency/governance mechanism across characters (shared-design rules, review, versioning of designs) | The estate's factory question; only per-character data (skins) is visible |
| A6 | Export / handoff / in-game result of the edited character | The design never leaves the editor |

### Counts (39 claim rows)

- VERIFIED: **23** — 12 demonstrated (V1–V12) + 4 text (C1, C4-editor-half, C5, C10) + 7 spoken (SP1, SP2, SP3, SP5, SP6, SP7, SP8)
- UNVERIFIABLE: **10** — 6 text (C2, C3, C6, C7, C8, C9) + 4 spoken (SP4, SP9, SP10, SP11)
- ABSENT: **6** (A1–A6)

## 2. Factory shape (the distillation)

**WaifuFactory's character factory is template-plus-parts,
hand-authored, with parameter-carried variation — not
procedural and not generative.**

- **Template:** one shared character scene — a fixed
  Skeleton2D, a fixed part taxonomy (6 body polygons, 4 hair
  parts, 5 face parts, anatomy polygons), a fixed module
  tree (SexModule, IK, remotes), and fixed shader set
  (`character_eyes`, `character_hair`, `hole_deformer`).
- **Parts:** each character's art is hand-painted part sheets
  cut into Polygon2D meshes and weight-painted to the shared
  skeleton (authoring shown in S7).
- **Variation:** what differs per character is carried by
  (a) the painted part set itself and (b) a **skin resource**
  (`.tres`) bundling the parameter values — colors (incl.
  NSFW Colors), tints, and by extension the shader/physics
  parameter surfaces, which are all inspector data.
- **Consistency mechanism:** the shared skeleton + part
  taxonomy + shared shaders/modules. Every character built
  on the template inherits the same rig, face system, and
  interaction modules by construction. What is NOT present:
  any check that two characters look like they belong
  together — consistency of *structure* is enforced by the
  template; consistency of *design* is unevidenced (A1, A5).
- **Toolchain dependency:** the template stands on two
  third-party Godot plugins named only in the voiceover —
  **Soup IK** (IK + wiggle; author-modified) and **Poly Rig**
  (paid, $6; mesh/rig authoring) — plus the author's own
  scripts (`character.gd`, `body_physics.gd`,
  `eye_shader_controller`). The factory is therefore partly
  rented: its rig quality depends on plugins the author does
  not own outright (one of them modified, which forks it).

One-line answer: **characters are hand-painted part sets
skinned onto one shared Godot Skeleton2D template, with
per-character variation stored as data-resource skins and
live behaviour (eyes, hair, anatomy, jiggle) driven by
parameterized shaders and physics scripts.**

## 3. Comparison against the estate's character factory

Estate references: `local-character-art-production` (two-model
rule + canonical-design governance; anchors; gated generation;
deterministic repair; keeper chains) and
`local-lumen-sprite-to-3d` (parametric factory: 2D sprite →
identity lock → projection onto one canonical rigged 3D base,
morph-target expression set, glTF out).

| Dimension | WaifuFactory (as evidenced) | Estate (as documented in the two skills) |
|---|---|---|
| Production mode | Hand-painted parts, hand-authored in the engine editor | AI generation from approved anchors + deterministic pixel repair |
| Consistency mechanism | Shared skeleton/template + shared shaders (structural) | Canonical governance: two-model rule, governing references, quarantine, keeper chains, human eye gate (design-level) |
| Per-character data | One skin `.tres` resource + editor Save Skin round-trip | Identity/keeper records as staging documents + measured locks (sprite-to-3D: proportions/palette hashed) |
| Face/expression | Parametric eye shader: continuous blink, gaze, pupil, tints — one quad, no per-state art | Baked sets: face sets (emotions × base/talk/blink) and morph-target emotion templates |
| Motion | 2D skeletal puppet + parameterized jiggle physics + IK in-engine | 2D strips/GIFs and 3D skeletal via the canonical base; jiggle treated in the 3D lane |
| Output | The game itself (Godot scene) — design never leaves the engine | Engine-neutral: glTF/GLB canonical, per-engine adapters; 2D deployables to repos |
| Determinism | None evidenced — GUI hand work | Seeded/scripted, re-runnable, gate numbers on record |
| Cast scale evidenced | 1 character | Fleets (10 companions; 6-girl Torogao standard) |

### What WaifuFactory evidences that the estate's documented factory lacks

1. **A parametric eye/face shader** — continuous blink, gaze
   deform, pupil control and tints as uniforms on one quad,
   driven by a controller script. The estate's expression
   systems are discrete (baked face-set images; morph-target
   emotion set). A continuous eye rig is a genuinely
   different mechanism, and it is demonstrated working.
2. **Skin-as-one-resource with an editor save round-trip** —
   a character's variable parameter bundle is a single
   loadable `.tres` with a Save Skin button in the inspector.
   The estate keeps equivalent knowledge in documents and
   staging records, not in one engine-loadable resource per
   character for its 2D lane.
3. **A named, numeric jiggle parameter block per character**
   (stiffness/damping/wobble/impact groups) as skin-level
   data in the 2D lane — the estate's jiggle work lives in
   the 3D lane (cage deforms); no equivalent 2D parameter
   block is documented in the two skills compared.

### What the estate has that WaifuFactory does not evidence

1. **Design governance** — two-model rule, canonical
   references, quarantine of non-canonical designs, keeper
   chains, human-eye gates. WaifuFactory shows no governance
   surface at all.
2. **Deterministic, gated production** — seeded pipelines,
   measurement gates, verdict records. The video is
   unrepeatable GUI work by construction.
3. **A 2D→3D route and engine-neutral output** — WaifuFactory
   characters exist only as Godot 2D scenes.
4. **Cast-scale consistency practice** — fleets produced and
   audited as fleets; WaifuFactory evidences n=1.

### What neither evidences

- Procedural/generative production of new characters (the
  estate generates IMAGES from anchors, but that is
  anchor-locked generation under governance, not a character
  generator; WaifuFactory shows no generation at all).
- Automated cross-character design-consistency checking.
