# Plan 11 — Pass 1 Timed Observation

Source: pinned capture (MANIFEST.md), 1,154.944 s, 720p
(1280×720 — the highest rendition the page offers; no 1080p
exists for this video). Blender **5.0.1** (title bar, every
frame). Screen-governed: grid frames at 30 s steps (39 frames,
`frames/grid/`) + native frames and native-res crops at every
AOV/light-group setting and the compositor tree
(`frames/t1035.jpg`, `t1065.jpg`, `t1095.jpg`, `t1125.jpg`,
`frames/crops/`). Transcript: single-chunk whisper lane,
tier **UNCONFIRMED**; narration points are added in the
addendum at the end and never override the screen.

## The subject

A finished still render of **Tifa** (Final Fantasy VII;
Genesis 8 Female based figure, file `Tifa_better_new.blend`)
standing before a photographic FFVII Remake background
(Square Enix "ff7 background wallpaper", sourced on screen at
2:30 via Google Images). Scene collections [SCREEN, 0:00]:
`chars > Tifa`; `env > background_geo`; `lights > test_setup
> a > {fill_lgt_01, fill_lgt_02, key_lgt, rim_lgt}`;
`cameras > Camera`; `volumes > fogbox`. Render engine
Cycles (device shown GPU Compute at 0:00, CPU in later
frames — the panel is toggled between takes; sampling
settings are never expanded, see UNREADABLE 4).

## Timed log

| Time | What happens [SCREEN] |
|---|---|
| 0:00–1:30 | **Cold open on the finished work.** Layout workspace: scene tour (above); then Compositing workspace with the completed tree: two Glare node groups, each → Hue/Saturation/Value node → Add. Lower HSV reads Hue 0.667 (being edited; at 1:30 the value 0.216667 is typed), Saturation 1.000, **Value 2.000**, Factor 1.000; upper HSV neutral (0.500 / 1.000 / 1.000 / 1.000) |
| 1:30–2:30 | (in the cold-open segment) hue tweak on the boosted branch tints the figure's shadows/rim visibly magenta-purple in the viewer |
| 2:30 | Browser: Google Images "ff7 background wallpaper"; the Square Enix FFVII Remake background is saved — the backdrop photo's source |
| 3:00 | `background_geo`: a plane whose material is Image Texture (`ffviir-zoo….header.jpg`, sRGB) → **Emission** Color, Emission Strength **1.000** — the photo is an emissive backdrop, not a world/HDRI |
| 3:30 | `key_lgt` (Point.003) is grabbed and moved in the viewport; the small image-editor preview shows that light's solo contribution (dark directional modelling on a transparent ground) |
| 4:00 | `fill_lgt_01` (Point.001) properties read in full: **Point light, Temperature 6500 K, Power 50.000, Exposure 0.000, Radius 0.5 m, Soft Falloff ✓, Normalize ✓**. Its solo preview is a dim frontal wash |
| 4:30–5:30 | Compositor again (the finished tree): the two Glare branches + HSV nodes (upper Hue 0.500/Value 1.000; lower Hue 0.450, Value 2.000) → Add; a third wire drops out of frame (toward the remaining passes) |
| 5:30 | View Layer → Passes → **Light** panel fully expanded: Diffuse {Direct ✓, Indirect ✓, Color ✓}, Glossy {Direct ✓, Indirect ✓, Color ✓}, Transmission {Direct ✓, Indirect ✓, Color ✓}, Volume {Direct ✓, Indirect ✓}, Other {**Emission ✓**, Environment ☐}; Alpha Threshold 0.500 |
| 6:00 | Same panel, lower part: Cryptomatte (collapsed), **Shader AOV (collapsed — never opened)**, **Light Groups list: `rim`, `key`, `fill_01`, `fill_02`** (native crop `frames/crops/crop-0360-lightgroups.png`) |
| 6:30 | Light Groups list being edited (only `rim` visible mid-edit); key_lgt selected |
| 7:00 | `key_lgt` Object properties → Shading: **Light Group field** with the group dropdown open (`rim` / `key`) — assignment is a per-object Shading property. Light Linking and Shadow Linking sections sit directly above it, unused |
| 8:00 | `rim_lgt` Object → Shading → Light Group = **`rim`** (set). rim_lgt is a Point light (shader-editor header at 2:00) |
| 9:00 | Compositing: a fresh/emptied tree — Render Layers node + Viewer. RL outputs (full list read at 9:30 zoom): **Image, Alpha, Volume Direct, Emission, Ambient Occlusion, Noisy Image, Denoising Normal, Denoising Albedo, Denoising Depth, Combined_rim, Combined_key, Combined_fill_01, Combined_fill_02** — the list terminates at Combined_fill_02 (scene selector directly below). Passes panel: Data {Combined ✓, Denoising Data ✓; Depth/Mist/Position/Normal/Vector/UV/Grease Pencil ☐} |
| 9:30–11:00 | The rebuild: Add nodes (Blender 5 "Mix Color · Add", Clamp Factor ✓) chain the passes pairwise; at 10:00–11:00 the viewer shows the summed figure **on black** — the group passes alone contain no backdrop |
| 11:30 | **Combined_rim → Hue/Saturation/Value (Hue 0.500, Saturation 1.000, Value 2.000, Factor 1.000)** — the rim branch is the doubled one. Combined_key / fill_01 / fill_02 wires run to the Add chain unmodified |
| 12:00 | The rim branch detailed: Combined_rim → **Glare node group (Bloom, Quality Medium, Highlights Adjust Strength 1.000 / Saturation 1.000, Tint white, Glare Size 0.500)** → HSV (Hue 0.467, Sat 1.000, **Value 2.000**) → Add |
| 13:00 | RL node again, backdrop viewer nearly white while a single pass is solo-viewed (pass soloing is part of the workflow — cf. 3:30/4:00 solo previews) |
| 14:00 | An Add node at Factor **0.858** (Clamp Factor ✓) blends a branch into the Viewer; the viewer now shows the figure **with** the photo backdrop — the Emission/Volume wires have joined the sum |
| 15:00 | **Full tree, full-screen node editor** (order in §"Compositor tree" below); a Multiply node (Factor 0.500) sits unconnected mid-canvas — a branch-gain node being placed |
| 16:00 | RL node left edge: all four Combined_<group> outputs wired; one branch passes a **Color Balance** node (seen fully at 18:00); an Add at Factor 0.500 is being dragged into place |
| 17:00 | Viewer zoomed on the backdrop region; Sample Color active — he inspects the backdrop's blend/grain in the comp |
| 17:15 | RL wires read again: **Volume Direct ✓ wired, Emission ✓ wired**, Combined_rim/key/fill_01/fill_02 ✓ wired; a **Denoise node sits unconnected** mid-canvas (being placed) |
| 17:30 | Tree tail: Add chain → **Multiply** → final **Add (Factor 1.000)** → Viewer; the Denoise node below receives two long guide wires |
| 17:45 | Denoise node close (native `frames/t1065.jpg`): **Image ← the sum chain, Albedo ← Denoising Albedo, Normal ← Denoising Normal; HDR ✓, Accurate, Follow Scene** → Viewer |
| 18:00 | Tail again: two Add nodes + Color Balance branch → Denoise at the right edge; viewer = the finished still (bright, warm, soft) |
| 18:45–19:15 | Final tree state (native `frames/t1125.jpg`): Glare branch 1 → HSV (0.467 / 1.000 / **2.000** / 1.000) and Glare branch 2 → HSV (0.500 / 1.000 / 1.000 / 1.000) → Add; the fills Add (bottom) and that Add both feed the final merge at frame right → (Denoise) → Viewer. End |

## Light-group configuration, exactly as set [SCREEN]

- **Groups (View Layer → Passes → Light Groups):** `rim`,
  `key`, `fill_01`, `fill_02` — one group per lamp, named
  after the lamp's role; the two fills get separate groups.
- **Assignment:** per-object, Object Properties → Shading →
  Light Group (key_lgt → `key` at 7:00; rim_lgt → `rim` at
  8:00; fills by the same pattern — their assignment frames
  are not separately screen-read, see UNREADABLE 5).
- **Lamps:** all four are **Point** lights (fill_lgt_01 =
  Point.001, key_lgt = Point.003, rim_lgt = Point).
  fill_lgt_01 as read: 50 W, 6500 K, radius 0.5 m, soft
  falloff, normalize on. Other lamps' powers: UNREADABLE 1.
- **Passes enabled (View Layer):** Combined + Denoising Data
  (Data section); the full Light component set (Diffuse /
  Glossy / Transmission × Direct/Indirect/Color, Volume
  Direct/Indirect, Emission, AO); Environment OFF; Data
  utility passes (Depth/Normal/Position/…) OFF.
- **Passes the compositor actually consumes:** Combined_rim,
  Combined_key, Combined_fill_01, Combined_fill_02,
  **Emission**, **Volume Direct**, Denoising Normal,
  Denoising Albedo. (AO is enabled and a wire count at
  17:15 is consistent with AO also feeding the tree, but
  no frame isolates an AO wire — counted UNREADABLE 6,
  not claimed.)

## Compositor tree, in full order (as evidenced 9:00–19:15)

1. **Render Layers** node (outputs listed at 9:00 above).
2. **Per-branch treatment:**
   - Combined_rim → Glare group (Bloom / Medium / Strength
     1.000 / Saturation 1.000 / Tint white / Size 0.500) →
     Hue/Saturation/Value (Hue ≈0.467, Sat 1.000,
     **Value 2.000**, Factor 1.000).
   - A second Glare group → HSV (0.500 / 1.000 / 1.000 /
     1.000) — neutral; its source pass is UNREADABLE 3
     (the key branch is the only other treated branch
     visible; the two Glare groups head the tree at 0:00
     before any rebuild, so both belong to the finished
     tree's design).
   - One branch passes a **Color Balance** node (16:00,
     18:00; its lift/gamma/gain values never readable —
     UNREADABLE 7).
   - A **Multiply** node (Factor 0.500) appears as a branch
     gain at 15:00/17:30 (transient placement; its final
     branch is UNREADABLE 3).
3. **Summation:** Mix-Color **Add** nodes (Clamp Factor ✓;
     factors seen: 1.000, 0.858, 0.500) chain: fills
   (fill_01 + fill_02) added as a pair; treated branches
     added; **Emission and Volume Direct added** — this is
     what returns the photo backdrop and the fog to the
     image (before they join, at 10:00–11:00, the sum is a
     figure on black).
4. **Denoise (terminal):** the summed image → **Denoise**
   node (Image = sum; Albedo = Denoising Albedo; Normal =
   Denoising Normal; HDR ✓; Accurate; Follow Scene) →
   Viewer / Composite. The renderer's own denoise is not
   the mechanism — denoising data passes are enabled
   precisely so the comp can denoise the *relighted* sum.

## Comp vs re-render — what the video demonstrates

- **Adjusted in comp, no re-render (all shown live against
  the existing render result):** per-group brightness
  (HSV Value 2.000 on rim), per-group hue/tint (Hue
  0.216667 typed at 1:30; 0.467 on the rim branch), glare /
  bloom per branch, branch blend factors (Add 0.858 /
  0.500), colour balance, final denoise of the sum.
- **Still forces a re-render (by construction, and shown
  as scene work, not comp work):** lamp position (key_lgt
  is moved in the 3D view at 3:30), lamp type/power/
  temperature/radius, backdrop image swap (2:30–3:00),
  anything geometric or material. The video never claims
  otherwise: the group passes encode *which lamp* lit each
  pixel, not where lamps are.
- **The render itself is never re-run on screen.** Every
  comp edit re-evaluates against the one existing render
  result ("Compositing… 0%" status ticks). Solo previews
  of single lights (3:30/4:00) are read off the same
  session's render/viewport state.

## File format and colour pipeline for the passes

**Not shown — UNREADABLE-by-absence (UNREADABLE 2).** No
Output Properties panel, no File Output node, no EXR /
multilayer setting, and no Colour Management panel appears
in any of the 39 grid frames or the targeted natives. The
workflow as demonstrated is **session-resident**: passes
exist inside the render result and are consumed by the
compositor in the same session; nothing is written to disk
on screen. Persistence of passes (the estate's EXR
contract) is therefore not a technique this video teaches
— it must be supplied by the estate (Pass 2, Adapt).

## UNREADABLEs (counted: 7)

1. key_lgt / rim_lgt / fill_lgt_02 numeric settings (only
   fill_lgt_01's panel is read: 50 W, 6500 K, r 0.5 m).
2. Output format / EXR / colour-management settings —
   absent from the video entirely (see above).
3. The second Glare branch's source pass, and the final
   branch placement of the Multiply (0.500) node.
4. Sampling settings (Samples panel never expanded;
   device shown as both GPU Compute and CPU across cuts).
5. fill_lgt_01/02's Light Group assignment frames (the
   pattern is proven by key/rim; the fills' own assignment
   is inferred from the Combined_fill_01/02 passes
   existing — inference, labelled).
6. Whether Ambient Occlusion feeds the comp tree.
7. Color Balance node values (node visible; values never
   in a readable frame).

## Claims list (Pass 3 test list)

- **C-11-1** One light group per lamp, named for its role
  (rim / key / fill_01 / fill_02), assigned per-object via
  Shading → Light Group, yields one Combined_<group> pass
  per group on the Render Layers node. [SCREEN 6:00–9:30]
- **C-11-2** The beauty is reconstructible in comp as a sum:
  Σ Combined_<group> **plus Emission plus Volume Direct**
  (ungrouped energy lives outside the groups — the group
  sum alone is a figure on black). [SCREEN 10:00–17:15]
- **C-11-3** Per-group relighting in comp: HSV Value scales
  a group's contribution (rim ×2.000), Hue retints it —
  no re-render for intensity or colour of an existing
  lamp. [SCREEN 0:00–1:30, 11:30–12:00]
- **C-11-4** Denoise belongs after the sum, in comp, guided
  by the Denoising Data passes (Normal/Albedo), HDR +
  Accurate — the relighted sum is denoised as a whole.
  [SCREEN 17:15–18:00]
- **C-11-5** Position/type/power of a lamp still force a
  re-render; group passes cannot move light. [SCREEN
  3:30 + construction of the mechanism]
- **C-11-6** (the creator's framing claim, from the page
  description) Light Groups let you "instantaneously change
  lighting properties without the need to re-render".
  Scoped by C-11-5: true for intensity/colour/treatment of
  existing lamps; false for lamp geometry. [INTAKE +
  SCREEN]

## Surprises vs the SHOULD-BE-SEEN (premise evidence)

1. **"AOV" is a title word, not the mechanism.** The panel
   literally named "Shader AOV" sits collapsed and is never
   opened; no AOV is created. The mechanism is Cycles
   **Light Groups** and their Combined_<group> passes —
   matching the creator's own description ("that's 'Light
   Groups'"), not the title. The plan's name ("Light AOVs")
   inherits the title's misnomer; recorded as plan errata.
2. **Σ groups ≠ beauty.** The plan's SHOULD-BE-SEEN implies
   "the compositor build that relights the beauty from
   passes" — true only once Emission (the emissive photo
   backdrop) and Volume Direct (the fogbox) are added back.
   A group-pure rebuild drops the background entirely
   (seen on screen, 10:00–11:00: figure on black).
3. **No file pipeline exists in the video.** A tutorial
   titled as a production technique never saves a pass to
   disk; the entire workflow evaporates with the session.
   The estate's contribution is precisely the missing
   contract (EXR multilayer), not a copy of his.
4. **The rig is four Point lights.** Against Plan 02's
   area/spot studio rig, this artist lights a portrait
   with points only (fill read at 50 W / 6500 K / 0.5 m
   radius) — light groups are orthogonal to lamp class.
5. **Structure:** the video opens on the finished tree
   (0:00–2:30, including the backdrop's Google-Images
   sourcing), tours the scene (3:00–9:00), then rebuilds
   a comp from an emptied tree (9:00–19:15). The "setup"
   half is a tour of an already-built scene, not a build.

## Addendum — narration (transcript landed at close; screen still governs)

Narration quotes are from `transcript.srt` (UNCONFIRMED
tier, single transcriber; used only where they gloss what
the screen shows):

- 0:08–0:51: "we will employ a feature called light
  groups which allow us to change properties of our
  lights after [render]… we could change the intensity…
  we could change the color… without having to
  re-render." The cold-open demo is a statement of
  C-11-3/C-11-6 in the creator's own terms.
- 1:43–4:10: "I have four lights… a key light here which
  is above the camera… fill light… second fill light… the
  rim light, it's a point light over here… and I got a
  fog box here… a volume shader, volume scatter."
  Confirms the four-lamp + fogbox scene read.
- 2:12–2:49: the backdrop — "I downloaded it off Google…
  Final Fantasy 7 background wallpaper… it's just an
  image that's on the plane here… plugged into the
  emissive channel." (Estate Rejected term, TECHNIQUE §4.)
- 6:16–7:10: "you create the group first, give it a
  helpful name… we go to object properties and then under
  shading, light group, we assign the light… **you could
  assign multiple lights to one group by the way**." —
  the mechanism allows N lamps per group; his as-built
  configuration is one group per lamp (screen). The
  estate variant follows the as-built granularity.
- 8:06 (narration): "**the render took one minute and
  19 seconds.**" **Correction to the screen record
  above:** §2's "the render itself is never re-run on
  screen" stands as a screen statement, but a render DID
  occur between the passes setup and the comp build —
  stated in narration, executed off-screen (between
  cuts). The claim table's C-11-3/C-11-6 readings are
  unaffected: his relight loop proper (9:00 on) consumes
  that one render's passes and never renders again.
- 8:22: "enabling some AOVs — direct volume, emission,
  ambient occlusion, and just the light groups." The
  title's "AOVs" is his umbrella word for the enabled
  pass set (Surprise 1).
- 8:34: of the cold-open tree — "This is the network
  node I already have. It's very complicated. I don't
  remember every little thing I've done. It's a scratch.
  Don't worry about that." The 9:00 build is from an
  emptied tree; the opening tree is disowned scratch.
- 9:18–10:40: "Our light groups are over here… Rim, key,
  fill one and two… To incorporate them you'll have to
  add… **Just add, add, add**… We added the rim to the
  key and then added both fill lights and then we added
  everything together… Combine rim, we'll have to put a
  HSV node." The summation grammar + per-branch HSV, in
  his words; 12:22 adds "We also have ambient occlusion
  and emission" (the remainder terms joining the sum).
- 16:29 / 18:59: "it's like layers in Photoshop"… "the
  changes we make are instantaneous — that's the upside
  to all this." His own summary of the value proposition.
- 17:2x: denoise narration names the albedo feed ("to
  the albedo") — consistent with the Denoising Albedo
  wiring read off the screen.

No narration statement contradicted a screen reading;
the single correction is the 1:19 render's existence
(off-screen, above). UNREADABLE count unchanged (7).
