# Plan 17 — Pass 1 Timed Observation

Plan: `repo/plans/17-porn-in-blender-part-2.md`
Intake: `runs/plan-17/INTAKE.md` (Pass 0; SHOULD-BE-SEEN
adopted verbatim from the plan, written before viewing).
Capture: `runs/plan-17/MANIFEST.md`; canonical media on
primo at `~/.local/share/pax/night-school/plan-17/plan17-source-720p.mp4`
(916,337,092 B, SHA-256
6501528046641b23f9b1593c000e2203c434515a0b8d6a871d5b16bc7422da72).

## Media and transcript of record

- Media: h264 1280×720 (the highest rendition offered) +
  AAC, duration **3669.845 s (1:01:09.8)** — ffprobe. The
  plan's stated 1:19:12 is wrong; the page's PT1H1M10S and
  the file agree (MANIFEST.md).
- Frames in `runs/plan-17/frames/`: 31 grid frames every
  120 s (`grid/g0005…g3605`), 62 native frames every 60 s
  (`native/t0030…t3660`), 5 native-resolution crops of
  parameter-bearing panels (`crops/`). Every numeric value
  below names its frame.
- Transcript: chunked lane (2 chunks @3,300 s; map in
  `chunk-map.txt`), tier **UNCONFIRMED**; the run's
  transcription is RUNNING detached on primo at delivery
  (MANIFEST.md — wave contention; stitch/census staged
  as `finish.sh` on primo). **The screen governs**: every
  setting below is tagged [SCREEN] (read off a named
  frame). The only narration used is the preliminary
  addendum at the end of this document, from segments
  the in-progress whisper had flushed at delivery,
  marked [SPOKEN-PRELIM].

## 1. What this video actually is — premise check

The plan's premise **holds in scope, fails in kind**. The
SHOULD-BE-SEEN promised "polish passes, lighting
finalisation, render settings, and delivery format
choices" — all four occur. But this is not the finishing
half of an *animation* course: **no animation is polished,
keyed, or rendered at any point**. The subject is a single
still: the character **Domina** (an Overwatch-derived
figure; page tags name "domina (overwatch)"), already posed
when the video opens, in Blender **5.0.1** [SCREEN, title
bar in every frame: `Domina_1.0.1_TUT
[E:\Divinity.Studio\chars\Domina\Domina_1.0.1_TUT.blend]`].
Part 2's "finishing" = environment + lighting + render +
compositor + external upscale of one portrait still.
Classified proportionately: the plan's gate (finishing
comparison table + unmatched dispositions) is unaffected —
the finishing order of operations below is complete for
what the video is — but any expectation of animation-polish
technique in Part 2 is REFUTED by the screen, and the
reconciliation note in TECHNIQUE.md carries this to the
Plan 16 join (Part 1 presumably carries the pose/setup
half; this run has not seen it).

The creator is **Divinity Studio** — the same series as
Plans 11 and 13. The scene is built on the same standing
scene family as Plan 11's Tifa scene: collections
`chars / cameras / lights / env / volumes`, lamps named
`fill_lgt_01 / fill_lgt_02 / key_lgt / rim_lgt`, a
`volumes` fog cube, an emissive photo environment. Part 2
is that pipeline run end-to-end on a new character; Plans
11/13 are deep-dives into two of its stages. That is what
makes the comparison in Pass 2 sharp: where Part 2's
integrated workflow *skips* the deep-dive techniques, the
skip is the creator's own revealed preference.

Section map (global timestamps):
- 0:00–2:00 — opening state: posed Domina, inherited
  lights (Sun + Rim1), the template render settings.
- 2:00–12:00 — environment: a UV-sphere dome built around
  the scene and textured with a starfield image.
- 12:00–14:30 — lighting theory, live: a Google Images
  search for "3 point lighting" and diagram study.
- 14:30–47:00 — the lighting build: five lamps placed and
  tuned one at a time against the camera render, a
  gradient world, the volume fog cube, an outfit pass.
- 47:00–48:30 — render settings retuned for production;
  the render itself happens at a cut (never watched).
- 48:30–58:30 — compositor: pass inspection, an
  atmosphere boost, a global grade, two Glare stages,
  chromatic aberration.
- 58:30–61:10 — delivery: EXR output settings shown, then
  a Google search for "ai upscaler" and the final image
  upscaled in a free web AI upscaler.

**Harvest append (2026-11-06, transcription finisher —
appended to §1; no existing text above or below is
altered, and no claim verdict in this document changes).**
The detached chunked transcription (`ns17-tr2.done` on
primo, exit 0) landed, and the staged finisher
(`finish.sh` on primo: `stitch.py`, then the loop census)
was read and run. Its first census path
(`~/workspace/…` on primo) does not exist there; the
script's own fallback — the `loop_census.py` copy in the
primo plan-17 dir — produced the census of record.
Outputs are in this run dir and in
`repo/results/plan-17-porn-in-blender-part-2/`,
byte-identical to the primo originals (hash-verified
after transfer): `transcript.srt` 48,810 B, SHA-256
3868f3c5ec39ba77793b768d3836bd52315cfcd03fa568e1171c4abbc207964d;
`transcript.txt` 24,383 B, SHA-256
270b0dfddd21d16213a07b3646a0de7b173372b6b50c0a22cf5fd28887998a31;
plus `stitch-verify.txt` and `loop-census.txt`.

- **Stitch verify** (`stitch-verify.txt`): chunk1 664
  segments + chunk2 36 segments + the seam marker =
  **701 stitched blocks**; chunk1 last end 3300.00 s;
  chunk2 first start at the +3300 s offset; **0 overshoot
  segments**; last in-range end **3668.98 s** against the
  media's 3669.845 s — coverage reaches 1:01:08.98 of
  1:01:09.845, the closing 0.87 s carrying no cue.
- **Loop census** (rule normalized-segment-v1, threshold
  >8; `loop-census.txt`): **701 segments, 34 loop
  segments, loop share 4.9%, recoverable 667 segments /
  95.1%, 1 loop phrase** (chunk1 5.1%, chunk2 0.0%). The
  loop phrase is "and we're going to be working on the
  surface" ×34, segments 616–649 at **52:49–53:29** —
  a whisper loop over a quiet compositor stretch, inside
  §8's pass-inspection window. Narration resumes
  coherently at 53:29 ("I will apply a glare node over
  everything, not just the emission… M for before and
  after"), which corroborates §8 step 4's global-glare
  posture. The recoverable share (95.1%) is the narration
  estimate of record; the loop span itself supports no
  narration claim, and none in this run rests on it.
- **Corroboration, no tension:** chunk2's narration
  confirms the node-chain posture of §8 ("You could go
  back in the chain and make changes. The changes will
  propagate forward… the advantage of a node-based
  workflow", 55:51–56:12), the Color Balance's subtle
  use (57:31–58:14, within UNREADABLE 5's family — its
  values remain screen-unread), the glare nodes as
  stylistic and optional, and the §9 closing comparison
  (original vs AI-upscaled face sharpness, 60:07–60:33).
- **TENSION T-1 (recorded, verdict unchanged — screen
  governs):** at 57:03–57:31 the narration says of the
  Lens Distortion, "I'll try 0.06. It's supposed to be a
  subtle effect." The screen read of record (§8 step 5,
  t3450 = 57:30, inside that same window) is
  **Dispersion 0.040**. Either 0.06 was tried and then
  settled to 0.040 without a narrated adjustment, or the
  whisper mis-heard the number. The §8 value and C-17
  claims stand on the screen read: **0.040**.
- **TENSION T-2 (recorded, verdict unchanged):** chunk2
  opens (55:00–55:22) on the Streaks glare: "this effect
  is too aggressive, obviously, so I'll reduce it to 2,
  and adjust to fade". No screen-read Streaks field in
  §8 carries a value of 2 (Threshold 1.000, Smoothness
  0.100 read clean; the node's remaining fields sit in
  UNREADABLE 5's family). The narration's "2" is not
  mapped onto any §8 value, and no §8 value is altered
  for it.
- **TENSION T-3 (recorded, verdict unchanged — the
  sharpest of the three):** the delivery narration
  (58:23–59:20) describes an **in-Blender upscale route**
  — "I'm going to upscale it, dropping down a scale
  node… this is our final image. Composite it" — and
  saving the result from the Image Editor as "PNG or
  JPEG or whatever", with the web AI upscaler framed as
  **optional** ("you could take your rendered image to…
  [an] AI image upscaler… Again, completely optional.
  You don't have to do this.", 59:20–59:39). §8's screen
  order carries no Scale node, §9's screen record shows
  the web upscaler actually used for the delivered
  still, and the output format of record is the EXR
  setting at t3510. The screen record stands: C-17-7's
  verdict (delivery via the web AI upscale of the
  composited still; in-Blender format of record OpenEXR
  DWAA) is **not** altered. What the narration adds is
  that the creator *also presented* an in-Blender
  scale-and-save route and framed the web upscale as a
  choice, not a necessity — recorded here as a framing
  tension against §9's delivery-only read, for Pass 2 /
  the Plan 16 join to weigh with the screen governing.

## 2. Opening state (0:00–2:00)

- The file opens mid-pipeline: Domina posed (seated,
  leaning on her mech arms), camera framed, left pane a
  flat-lit camera render [SCREEN t0030]. Outliner:
  `CH-Domina {Domina-rig, Domina-geometry}`, `PR-Domina
  {PR-Domina-Weapon}`, `Camera`, `Rim1`, `Sun` — the
  inherited lamp set is one Sun + one rim.
- Render Properties as inherited [SCREEN t0030, crop
  `crops/crop-t0030-sampling.png`]: Cycles; Noise
  Threshold ✓ **0.0100**, Max Samples **4096**, Time Limit
  0 s; **Denoise ✓ — OpenImageDenoise, Passes "Albedo and
  Normal", Prefilter Accurate, Quality High, Use GPU**;
  Light Tree ✓, Light Threshold 0.01. Performance:
  Threads Mode Fixed, **Threads 10**, Tile Size 2048
  [SCREEN t0090]. These are the
  creator's standing template values (the same adaptive
  pair as Plans 01 and 02 — §9), **not** the values the
  final render uses (§7): the video changes them on
  camera at ~48:30.

## 3. Environment dome (2:00–12:00)

- A UV Sphere is added around the whole scene and scaled
  to enclose character, camera-side space and lamps
  [SCREEN t0330 wireframe sphere; t0690 textured sphere].
- The sphere (later `Sphere` in collection `env`, with a
  sibling `Sphere.001`) takes an image texture
  **`starfield-17.png`** [SCREEN t2070 shader editor,
  crop `crops/crop-t2070-dome-shader.png`]: Image Texture
  Color → Principled BSDF (Metallic 0.000, Roughness
  0.000, IOR 1.500 as read). The dome renders as the
  visible starfield backdrop in every later camera frame
  [SCREEN t0690, t2310].
- The dome is **emissive in effect**: at 50:30 the
  compositor's Emission pass, soloed, shows the starfield
  dots and the character's teal mech rings on black
  [SCREEN t3030] — the dome's stars live in the Emission
  pass, so the starfield texture also drives emission
  (the exact second wire is below the visible node area —
  partial UNREADABLE 1).
- With the dome in, the character starts as a dark
  silhouette against the stars, lit only by the inherited
  Sun/Rim1 and her own emissive rings [SCREEN t0690] —
  the build proceeds from near-black, exactly as in Plan
  02's silhouette-first rig build and Plan 11's scene.

## 4. Lighting theory, live (12:00–14:30)

- The creator leaves Blender and Google-searches
  **"3 point lighting"**, studying the Frameforest diagram
  (Key light / Fill Light / Back light) full-screen
  [SCREEN t0870]. The lighting build that follows is
  explicitly the textbook three-point scheme, expanded:
  key + two fills + two rims (§5). The estate records this
  as method, not colour: the rig's *roles* are the
  transferable content (compare Plan 02 Target 1: a rig
  assembled by role per shot).

## 5. The lighting build (14:30–47:00)

Built one lamp at a time in top view against the live
camera render, lamps collected under `lights`. All lamps
read **[SCREEN]**; object names are the creator's
(`fill_lgt_01` etc. — the same names as Plan 11's scene).

| Lamp (final name) | Type as read | Values as read | Frame |
|---|---|---|---|
| key/fill candidate `Point.001` | **Area**, Rectangle 0.5 m × 1 m, Spread 180° | Temperature 6500 K, Power **100.000**, Exposure 0.000, Normalize ✓ | t1230 (20:30) |
| `fill_lgt_01` (`Point.002`) | **Area**, Rectangle 1 m × 2 m | Temperature 6500 K, Power **50.000**, Exposure 0.000, Normalize ✓ | t1350 (22:30) |
| rim source (pre-duplication) | **Point** | Temperature 6500 K, Power **1000.000**, Exposure 0.000, Normalize ✓, Radius 0 m, Soft Falloff ✓ | t1050 (17:30), t1590 (26:30) |
| `rim_lgt.001` (`Point.006`) | **Point** | Power **500.000** mid-tune → **250.000** final read, Radius 0 m, Soft Falloff ✓, Normalize ✓ | t1950 (32:30), t2790 (46:30) |

- The rim is **duplicated** to make the second rim
  (`rim_lgt` → `rim_lgt.001`, Duplicate Objects dialog
  [SCREEN t1590]) and the copy is then tuned *down* in
  steps — 1000 → 500 → 250 W across the build — while the
  camera render is watched. The halving sequence is the
  balancing method: duplicate at full strength, then
  attenuate against the render.
- A **gradient world** is built alongside: World nodes
  `World_OW2` with a Gradient Texture feeding the
  Background [SCREEN t1230/t1350 bottom shader editor] —
  the world is a designed gradient, not a flat colour and
  not an HDRI (contrast Plan 02: world strength 0.000 and
  NO environment light at all; here the dome is geometry
  and the world still carries a gradient).
- The **volume fog cube** (`volumes > Cube` [SCREEN
  t1830]) is present and tuned in this phase: at 30:30
  the camera render is washed in haze; by 34:30 the haze
  reads as atmosphere over the starfield [SCREEN t1950].
  The cube's density/anisotropy values are never shown in
  a readable panel — UNREADABLE 2.
- `key_lgt`'s own final panel is never isolated in a
  readable frame — UNREADABLE 3 (its existence, name and
  role are certain from the outliner at t1350/t1830/
  t1950/t2790; its wattage is not claimed).
- **Outfit pass (∼41:30):** the character's custom panel
  toggles outfit components for the final look (Coat ✓,
  Shins ✓, Heels ✓, Steel Plate ✓, Stockings ✓, Long
  Nails ✓, Wings ✓, Arms ✓; Vest/Skirt/Sports set to
  None) [SCREEN t2490]. The delivered still is the
  open-coat variant; a fully clothed variant exists as
  the video's thumbnail image (`tutorial_thumbnail.jpg`,
  3840×2160, shown at t1350) — two outfit states of one
  scene, compared in §8.

## 6. Passes enabled (44:30, before the render)

View Layer → Passes → Data [SCREEN t2670]: **Combined ✓,
Depth ✓**; Mist / Position / Normal / Vector / UV /
Grease Pencil / **Denoising Data ☐**. The fuller pass
panel at 53:30 [SCREEN t3210, right] adds: Volume
**Direct ✓** (Indirect ☐), **Emission ✓**, Environment
☐, **Ambient Occlusion ✓**, Shadow Catcher ☐;
Cryptomatte present, Levels 6; Shader AOV collapsed,
never opened (the same tell as Plan 11: the panel named
AOV is not the mechanism). The Render Layers node's
complete output list, read at 52:30 [SCREEN t3150]:
**Image, Alpha, Depth, Volume Direct, Emission, Ambient
Occlusion, Noisy Image** — the list terminates there.
**There are no `Combined_<group>` outputs**: this scene's
View Layer carries no light-group passes, although the
creator's own Plan 11 video is a light-groups tutorial.
Pass 2 draws the comparison; Pass 1 records the fact.

## 7. Render settings — the retune (48:30)

At the Compositing workspace the Render Properties read
[SCREEN t2910, crop `crops/crop-t2910-sampling.png`]:

- Engine Cycles, Device **GPU Compute**.
- Viewport: Noise Threshold ✓ **0.1000**, Max Samples
  **64**, Min Samples 0, Denoise ✓.
- Render: Noise Threshold ✓ **0.0300**, Max Samples
  **512**, Min Samples 0, Time Limit 0 s, **Denoise ✓**
  (section present, checked; its denoiser/passes detail
  is below the visible area — the inherited template
  state was OpenImageDenoise "Albedo and Normal" /
  Accurate / High [t0030]; whether the retune changed
  the denoiser is UNREADABLE 4).

Against §2's inherited 0.0100/4096, the production render
is **8× fewer ceiling samples at 3× the noise threshold**.
The render execution itself is never watched (it happens
across a cut between the Layout phase and the
Compositing phase); the compositor works on the resulting
render result in-session, the same session-resident
posture as Plan 11 (no pass is saved to disk on screen —
but see §8: an EXR output is configured, unlike Plan 11).

Format [SCREEN t2490, t3510]: Resolution **1280×720 px,
100%**, Aspect 1.000/1.000, Frame Rate 24 fps, Frame
Range 0–250 (inherited animation-scene defaults, unused
by a still).

## 8. Compositor (48:30–58:30) — in full order

The tree is built live on the one existing render result.
Order as evidenced frame-to-frame (all [SCREEN]):

1. **Pass inspection by soloing.** Render Layers outputs
   are wired to the Viewer one by one; at 50:30 the
   **Emission** pass is solo-viewed (starfield + teal
   rings on black) [t3030]. Inspection precedes any node
   work — the same solo-check habit as Plan 11.
2. **Atmosphere/glow boost — passes as effects, not
   reconstruction.** A Mix node in **Add** mode (Clamp
   Factor ✓) sums **Volume Direct + Emission** at
   Factor **0.492** [t3150]. The Combined image already
   contains both terms; adding them again at ≈½ strength
   is a deliberate double-count: more fog, more glow.
   This is the opposite algebraic posture from Plan 13's
   faithful beauty recreation (Pass 2, row C-6).
3. **Global grade on the combined image.**
   Brightness/Contrast (Brightness 0.000, Contrast
   1.000 — placed, at neutral as read) → **Hue/Saturation/
   Value (Hue 0.500, Saturation 1.025, Value 1.000,
   Factor 1.000)** [t3210, t3270]. A **Color Balance**
   node is also present in the tail (Lift/Gamma/Gain
   fields partially read at t3510's left edge: 0.133 /
   0.000 / a magenta lift swatch / 1.000 / 1.000) — its
   exact chain position and full values are UNREADABLE 5.
4. **Glare ×2.** First **Glare — Bloom, Quality High,
   Highlights Threshold 1.000, Smoothness 0.100, Size
   0.500** [t3270]; then **Glare — Streaks, Quality High,
   Threshold 1.000, Smoothness 0.100** (a second Glare
   node's partial values at t3390 read …0.750 / …0.100 —
   counted within UNREADABLE 5's family; the Streaks
   node's own headline values are read clean at t3450).
   The viewer shows the effect: star points and emissive
   rings bloom and streak [t3390].
5. **Chromatic aberration, last.** **Lens Distortion —
   Radial, Distortion 0.000, Dispersion 0.040, Jitter ☐,
   Fit ✓** → Viewer [t3450]. A simulated lens flaw is
   the final image operation inside Blender.

**Output configuration** [SCREEN t3510, crop
`crops/crop-t3510-output.png`]: Output path `/tmp\`;
File Format **OpenEXR (.exr)**, Color **RGBA**, Color
Depth **Float (Full)**, Codec **DWAA (lossy)**. No
File Output node is shown; the EXR is the scene's
render-output setting. (Contrast Plan 11: no output
format appears at all; contrast Plan 02's estate
contract in Plan 11 Pass 2: multilayer EXR 32-bit ZIP —
his single-layer DWAA full-float is a different point
on the same trade-off; Pass 2 row C-7.)

## 9. Delivery (58:30–61:10)

- The creator Googles **"ai upscaler"** and surveys free
  web upscalers (ImgUpscaler, Upscale.media, ImgUpscaler
  AI) [SCREEN t3570], then uploads the finished still to
  **imgupscaler.ai** ("ImgUpscaler"), which shows the
  upscaled result with a Download button [SCREEN t3630].
- The delivered artifact of the whole course is therefore
  a **1280×720 render, composited, then AI-upscaled by a
  third-party web service**. The 3840×2160
  `tutorial_thumbnail.jpg` seen at t1350 is consistent
  with a 3× upscale of a 1280×720 master (3840 = 3×1280,
  2160 = 3×720) — recorded as a consistency observation,
  not a claim about that file's provenance (it shows the
  *clothed* variant; the upscaled frame at t3630 shows
  the open-coat variant — two deliveries or one
  re-dressed re-render, the video does not say:
  UNREADABLE 6).

## 10. The finishing order of operations (primary extraction)

Numbered F-17-n; each step names its evidence. This list
JOINS Plan 16's Part-1 list as its second half (INTAKE.md
records the join: Plan 16 had not landed at this run's
P2, so the join is a cross-reference, not a renumbering —
when Plan 16 lands, Part 1's setup steps precede F-17-01
unchanged).

| # | Step | Evidence |
|---|---|---|
| F-17-01 | Open the posed scene; confirm the inherited template render state (Cycles, 0.0100/4096 adaptive pair, OIDN denoise) before touching anything | t0030 |
| F-17-02 | Build the environment as geometry: UV-sphere dome enclosing the scene | t0330 |
| F-17-03 | Texture the dome with the environment image (starfield-17.png → Principled; the texture also feeds emission, so the backdrop is a light source in the Emission pass) | t2070, t3030 |
| F-17-04 | Set the world to a designed gradient (Gradient Texture → Background, World_OW2) — environment light is authored, not an HDRI | t1230 |
| F-17-05 | Study the lighting scheme before placing lamps (three-point diagram, live reference search) | t0870 |
| F-17-06 | Place lamps by role, one at a time, in top view against the live camera render, starting from the near-black silhouette: Area key/fill candidates first (100 W / 50 W, 6500 K, rectangular Areas 0.5×1 m and 1×2 m) | t1050–t1350 |
| F-17-07 | Add Point rims at high power (1000 W, radius 0, soft falloff); duplicate the rim and attenuate the copy in halvings (1000 → 500 → 250 W) while watching the render | t1590, t1950, t2790 |
| F-17-08 | Add the volume fog cube; tune atmosphere against the lit render (haze that reads, not whiteout) | t1830, t1950 |
| F-17-09 | Final outfit/visibility pass on the character panel (components on/off for the delivered look) | t2490 |
| F-17-10 | Enable the finishing pass set (Combined, Depth, Volume Direct, Emission, AO) — and no others; Denoising Data stays OFF because denoise is a render-time stage here | t2670, t3210 |
| F-17-11 | Retune render economics for production: GPU Compute, render 0.0300/512 adaptive pair, viewport 0.1000/64; render the still | t2910 |
| F-17-12 | In comp, solo-inspect the passes before building anything (Emission solo shown) | t3030 |
| F-17-13 | Boost atmosphere additively: Add (Volume Direct + Emission) at Factor 0.492 into the combined image | t3150 |
| F-17-14 | Grade the combined image globally: Brightness/Contrast → HSV (Saturation 1.025) → Color Balance | t3210–t3510 |
| F-17-15 | Glare twice: Bloom (High, Thr 1.000, Smooth 0.100, Size 0.500), then Streaks (High, Thr 1.000, Smooth 0.100) | t3270, t3390, t3450 |
| F-17-16 | Finish with a simulated lens flaw: Lens Distortion Dispersion 0.040, Fit ✓ | t3450 |
| F-17-17 | Configure image output as OpenEXR, RGBA, Float (Full), DWAA | t3510 |
| F-17-18 | Deliver by external AI upscale: search, choose a free web upscaler, upload the composited still, download the upscale | t3570, t3630 |

**18 finishing steps.** The order is load-bearing in the
creator's hands: environment before lamps (the dome is
the ground the lamps carve the figure out of), lamps
before volume (fog is tuned against finished light),
render before any comp, inspection before adjustment,
additive boost before grade, grade before glare,
aberration last, upscale after everything.

## UNREADABLEs (counted: 6)

1. The dome material's emission wiring (the second wire
   from the starfield texture leaves the visible node
   area at t2070; emission *effect* is proven by the
   t3030 Emission solo, the wire's destination node is
   not read).
2. Volume cube density / anisotropy values (the cube is
   seen and its effect is seen; its panel never is).
3. `key_lgt`'s final numeric panel (power/size). The
   100 W Area at t1230 is a key/fill candidate mid-build;
   naming it `key_lgt`'s final state would be a guess.
4. Whether the 48:30 retune changed the denoiser (the
   Denoise section is checked at t2910; its expanded
   detail is off-frame; the inherited state at t0030 is
   OIDN / Albedo-and-Normal / Accurate / High).
5. Color Balance node's full values and exact chain
   position; the second Glare node's secondary values
   (…0.750 / …0.100 at t3390).
6. The relationship between the 3840×2160 clothed
   thumbnail (t1350) and the upscaled open-coat delivery
   (t3630): one pipeline, two outfit states; whether the
   thumbnail is this scene's earlier delivery is not
   stated on screen.

## Claims list (Pass 3 disposition list)

- **C-17-1** The finishing workflow is a fixed order:
  environment → lamps → volume → outfit → passes →
  render → comp (inspect, boost, grade, glare, aberrate)
  → EXR → external upscale. [SCREEN, §10]
- **C-17-2** The dome-as-environment: a textured sphere
  enclosing the scene serves as backdrop AND as an
  emission source; no HDRI is used at any point.
  [SCREEN t0330–t2070, t3030]
- **C-17-3** Three-point lighting, expanded to five
  lamps (key + 2 fills + 2 rims), placed by role against
  the live render, is sufficient to finish the portrait;
  rim balancing is done by duplicate-and-halve.
  [SCREEN §5]
- **C-17-4** The creator's template render pair is
  0.0100/4096 with OIDN denoise, but the production
  still is rendered at 0.0300/512 on GPU — quality is
  carried by lighting/comp, not by sample count.
  [SCREEN t0030 vs t2910]
- **C-17-5** In this integrated workflow, light groups
  are NOT used: the View Layer's pass list contains no
  Combined_<group> outputs, and all comp adjustment is
  applied to the combined image (plus an additive
  Volume+Emission boost). [SCREEN t2670, t3150, t3210]
- **C-17-6** Volume Direct + Emission, re-added at
  Factor 0.492 over a Combined that already contains
  them, is used as an atmosphere/glow *effect*, not as
  reconstruction. [SCREEN t3150]
- **C-17-7** Delivery resolution is manufactured in
  post: a 1280×720 master is AI-upscaled by a free web
  service; the in-Blender output format of record is
  OpenEXR RGBA Float (Full) DWAA. [SCREEN t3510, t3570,
  t3630]
- **C-17-8** (the plan's framing claim) Part 2 is "the
  finishing half" of the course: animation polish,
  lighting, render, output. **Scoped by §1: lighting /
  render / output HOLD; animation polish is absent —
  the video finishes a still.** [SCREEN, whole run]

## Surprises vs the SHOULD-BE-SEEN (premise evidence)

1. **Duration errata.** The plan states 1:19:12; the
   video is 1:01:10 (page and file agree). Recorded in
   INTAKE.md / MANIFEST.md; errata applied to the LOCAL
   plan copy only.
2. **A still, not an animation.** Nothing moves. "Part 2"
   finishes the portrait Part 1 posed. The finishing
   curriculum is environment/lighting/render/comp/
   delivery — see §1 for the proportionate close.
3. **The light-groups creator doesn't use light groups
   here.** The same studio's Plan 11 video teaches
   per-group relighting as "a powerful mechanism that
   every serious blender user should utilize"; in the
   integrated Part 2 workflow the pass list has no group
   passes and the grade is global. The deep-dive
   technique and the production workflow diverge — the
   sharpest comparison fact in this run (Pass 2).
4. **The template is not the production setting.** The
   file opens at 0.0100/4096 (the pair Plans 01/02 also
   use) and is deliberately retuned DOWN to 0.0300/512
   for the delivered render. Sample-count ceremony is
   spent only until lighting and comp can carry the
   image (Pass 2, render-economics rows).
5. **Delivery is a web service.** The final quality
   step is not in Blender at all: a free AI upscaler
   found by a live Google search manufactures the
   delivery resolution from a 720p master.

## Preliminary transcript addendum [SPOKEN-PRELIM]

From the in-progress chunked transcription (primo detach
`ns17-tr2.log`, segments flushed at delivery; tier
UNCONFIRMED; the stitched transcript + census complete
via `finish.sh` when the job lands — MANIFEST.md):

1. **An opening retune precedes F-17-02.** At
   0:17–0:47 the creator narrates changing the render
   device to CPU and reducing viewport sampling to 64
   ("I'll reduce the sampling the viewport down to 64
   you can use any value you want… this is just a
   viewport render this is not the final render"). This
   refines §2/§7's chronology: the inherited GPU /
   0.0100/4096 state (t0030) is immediately retuned for
   the *interactive* phase (CPU device — consistent
   with the CPU device read at t2310, 38:30), and the
   GPU + 0.0300/512 state at t2910 is the *production*
   retune (F-17-11). F-17-01 should therefore be read
   as "confirm the inherited state, then retune for
   interaction (CPU, viewport 64)"; the step table's
   count is unchanged (the opening retune folds into
   F-17-01's confirmation act, the production retune
   remains F-17-11).
2. **Asset provenance is via the companion PDF.** At
   ≈2:45, over the environment-dome work: "I have a
   link to it in the pdf file" — the starfield asset
   (or its source) is linked from the tutorial's PDF
   companion (the Mega PDF link in the page
   description, INTAKE.md). Recorded as provenance
   colour for §3; no estate action (reference only).
