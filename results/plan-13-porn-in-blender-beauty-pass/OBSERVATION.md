# Plan 13 — Pass 1 Timed Observation

Source: pinned capture (MANIFEST.md), 2,058.35 s, Blender
**5.0.1** (title bar, every Blender frame). Screen-governed:
grid frames at 60 s steps (35 frames) + targeted frames at
30 s steps (30 frames) + native crops of the formula page,
the whiteboard, the full compositor tree (t=1260 crop), the
Glare node (t=1320 / t=1890) and the finishing chain
(t=1920 / t=2040). Transcript: single-chunk whisper, tier
UNCONFIRMED (MANIFEST.md); narration is tagged [SPEECH] and
never outranks the screen. The presenter teaches live,
thinking aloud; repetitions and filler are not claims.

## The subject

A single still: **Grace Ashcroft** (the Resident Evil 9
protagonist), a SmutBase model the presenter credits to
"kenju nsfw" [SPEECH 1:58–2:33; UNCONFIRMED spelling], in the
presenter's own scene file `Grace Ashcroft_MINE.blend`
(`E:\Divinity Studio\chars\Grace\…`, title bar). Scene
inventory [SCREEN, outliner at 2:00–5:00]: character append
collection; `env` → `backplate_geo`; `lights` → `fill_lgt_01`,
`fill_lgt_02`, `key_lgt`; `cameras` → Camera; `volumes` →
`fogbox`. Three light sources [SPEECH 3:10]: a key light —
"a square light down here, a subtle pink orangey type color"
(the fill_lgt_01 object selected at 4:00 is a Point light in
the properties editor; the key is described as square/area) —
and two fills. The background is a **plane with an emissive
material**: a screenshot taken from the game, plugged into
the emission slot [SPEECH 4:38–6:05; SCREEN 5:00: backplate
material — Principled, Base Color black, Roughness 1.000,
Emission Color = `wallpapers-screen…` texture, **Emission
Strength 5.000**]. Light colours are sampled to match the
background so "the subject is in the room even though there's
no actual room, it's just a plane" [SPEECH 6:10–6:44]. A fog
box gives the scene its volume [SPEECH 4:22–4:33].

## Timed log

| Time | What happens |
|---|---|
| 0:00 | OBS Studio recursion (recording start; taskbar 3:00 PM 3/27/2026) |
| 0:10–0:50 | **The source of the recipe is shown first:** the Chaos documentation page "Beauty – V-Ray for Nuke" (documentation.chaos.com/…/VRAYNUKE/…/Beauty). Page text [SCREEN t=0030, native read]: "The following is the base formula for reconstructing the Beauty pass. Some Render Elements can be excluded if the scene does not utilize them." Formula as printed: **Lighting + GI + Reflection + Refraction + Specular + SSS + Self Illum + Caustics + Background + Atmospheric Effects = Beauty** |
| 0:50–1:40 | On an Excalidraw whiteboard he re-derives the formula in Cycles terms, writing and narrating: "(ind diffuse + dir diffuse) * d…" [SCREEN t=0060]. Narration [SPEECH]: "you take the indirect diffuse and add it to the diffuse [*sic* — direct] multiplied by the diffuse color… all this gets added to indirect glossy, direct glossy, glossy color and so on… then there's the transmission, of course transmission color" |
| 1:42–2:40 | The subject introduced: Grace, Resident Evil 9, SmutBase model (above) |
| 2:40–6:50 | Scene tour: light contributions toggled per light in the outliner (no lights / key only / fills / fog) [SCREEN 4:00]; backplate emission explained (above) |
| 6:50–7:40 | **Passes enabled before rendering** [SPEECH]: "render passes… I have Combined, Denoising Data, and of course the Diffuse Direct, Indirect [and Color]… these are the constituent parts that make up the final beauty render." Pass panel as finally configured [SCREEN 22:00/24:00/27:30, right panel]: Data — Combined ✓, Denoising Data ✓ (Depth/Mist/Position/Normal/Vector/UV/Object Index/Material Index/Sample Count all ✗); Light — Diffuse Direct ✓ Indirect ✓ Color ✓; Glossy Direct ✓ Indirect ✓ Color ✓; Transmission Direct ✓ (Indirect/Color ✓ by the socket list); Volume + Emission per the socket list; **no Subsurface passes, no Environment pass** |
| 7:40–8:10 | Render settings [SCREEN t=0480, native read]: Viewport sampling — Noise Threshold 0.1000, Max Samples 64, Min 0, Denoise ✓. **Render sampling — Noise Threshold 0.0300, Max Samples 512, Min Samples 120, Time Limit 0, Denoise ✓** (the renderer's own denoise is ON for the beauty he will compare against). Device GPU Compute. Resolution 720×1280 @100% [SCREEN 34:00] |
| 7:56–8:26 | The render runs 8 min 23 s by his narration [SPEECH: "that took eight minutes and twenty three seconds… using an old GPU"]; the Render Result header reads **Time 08:26.66, Mem 4821M, Peak 4821M**, slot name "Composite" [SCREEN 2:00/8:00] |
| 8:19–9:00 | Compositing workspace. Render Layers node: the Image socket is the beauty; the recreation is built next to it. First node placed is a Mix **Add** [SCREEN 9:00: node fields Color / Add / Clamp Result ☐ / Clamp Factor ✓ / Factor 0.500 (default, later set 1.000)] |
| 9:00–10:10 | Diffuse branch built first, narrated step by step [SPEECH]: "add Diffuse Direct and Indirect, and we want to multiply that by the Color" |
| 10:07–10:51 | The (Add, Multiply) pair is **duplicated with Shift+D** for Glossy and Transmission [SPEECH: "box select these two and do Shift+D"] — one branch grammar, three instances |
| 11:00–12:20 | A single raw pass viewed in the Viewer at face scale is visibly **noisy** (grain over the whole face) [SCREEN 12:00] — the constituent passes are un-denoised; only the Combined was denoised by the renderer |
| 12:20–13:10 | Transmission is not decorative here: "the glasses has a transmission material" [SPEECH] |
| 13:05–13:35 | **Emission added raw** [SPEECH]: "I mentioned earlier that the background uses an emissive material, so that's missing from our reconstruction — luckily we have an emissive channel right here, we simply have to add that" |
| 13:35–14:10 | Aside on Mix-node A/B semantics ("think of B as the layer on top… you have to keep that in mind when you perform these operations") [SPEECH] |
| 14:10–15:40 | **Denoise node added at the END of the chain** [SPEECH]: "when I rendered I had Denoising Data checked, this will help us get rid of the noise… Shift+A, Denoise — in addition to the Image I need Albedo and Normal… the Denoising Normal, Denoising Albedo, we simply connect those two." Node as configured [SCREEN 15:00/17:30, native reads]: **HDR ✓, Prefilter "Accurate", Quality "Follow Scene"** — which are the Blender compositor Denoise node's defaults |
| 15:40–19:00 | "We've successfully reconstructed the beauty pass using its constituent parts. We could confirm that by comparing our reconstruction…" [SPEECH]. The confirmation instrument is a **Switch node**: Off ← the renderer Image, On ← the denoised recreation; he toggles it while watching the Viewer [SCREEN 18:00–18:30: Switch node with both inputs wired; hover tooltip at 18:30 reads "Switch, Value: False" during toggling]. **No numeric comparison is ever shown** — the match is asserted from the A/B view, not measured |
| 16:00–18:00 | **The first A/B comparison FAILS, on screen, and he says so** [SPEECH]: "off… on… **well it's not quite the same — we're missing volume**." The Volume branch (Direct + Indirect, "we always add direct and indirect") is wired in *after* the first comparison, and he reasons out the placement aloud: "**I think we have to do it before the denoise, because the volume AOV could be noisy**"… "now we're going to feed it to the denoiser." (AOV glossed in passing: "AOV is arbitrary output variables — those are the constituent parts that make up the beauty.") Add-chain convention stated: "whatever new thing we're bringing in, we plug it on B." This is the video's one demonstrated renderer-vs-recreation difference, and it is a *missing branch*, caught by eye |
| 15:00 | The full tree in one frame [SCREEN t=0900 + crop]: per-component branches (Add then Multiply for Diffuse / Glossy / Transmission), Volume Direct/Indirect entering an Add, Emission entering an Add, branch sums combined by further Adds, the sum feeding Denoise (Image) with Denoising Albedo + Denoising Normal wired to its Albedo/Normal sockets, Denoise output toward the Viewer/Composite path, and the Image bypass line running to the Switch. **Ambient Occlusion and Noisy Image sockets exist but carry no wire into the sum**; Denoising Depth likewise unwired |
| 21:00 | The same tree, tighter crop [SCREEN t=1260 + crop-tree1260]: every Mix node in the recipe is Add or Multiply; one expanded Add shows **Factor 1.000, Clamp Factor ✓, Clamp Result ☐** — factors are unity and results are NOT clamped anywhere in the recipe |
| 18:00–19:10 | Second A/B, after the Volume fix [SPEECH]: "the moment of truth… this is off, this is on… yeah it looks like we've successfully reconstructed the beauty pass." Mechanism stated in full: "the beauty pass doesn't have any noise because when we rendered we added the [de]noiser here, but unfortunately the AOVs have noise, so after we combine all the AOVs we have to denoise it — of course to denoise it we need the extra information, the albedo and the normal; that's why I had Denoising Data checked" |
| 19:10–21:00 | **The payoff is demonstrated per-component after all**: "why would I do all this… we could make changes without having to re-render… this is the fog box — **what if I want less fog — look at that — I can make these changes very quickly without re-rendering**, because rendering [is slow]… we could see our results instantaneously." He then solos the Emission branch: "this is the emission, I believe — the background" [SPEECH]. The Viewer at 20:00 shows a visibly re-graded image (brighter, glow-heavy) against the matched state [SCREEN t=1200]. The exact widget used for the fog change (branch Add factor vs a gain node) is not readable at 720p — the *effect* and its immediacy are the demonstration; the mechanism (branch gain in the sum) is unambiguous |
| 24:46–25:39 | **Intermission** [SPEECH]: "this is a brief intermission — just a gentle reminder to check out the Patreon" (an animation course is in production, Patreon-exclusive). Screen dims to the OBS/browser desktop (tabs incl. SmutBase, a Resident Evil 9 screenshot search, his Patreon) [SCREEN t=1530]; no technique content |
| 25:39–26:32 | **The volume is added a SECOND time, deliberately** [SPEECH]: "I have the Volume Direct and Indirect — I added them together — so now I'm gonna drag it all the way out here and **add that after the ambient occlusion**. We already incorporated volume here, **but I'm doing it again because it looks better**." The bottom Add with two long lines in the 27:00 frames is this second volume sum. The final image is therefore *not* the matched recreation: it is the matched recreation (volume counted once, pre-denoise) **plus a fog boost** (the same volume sum added again, post-denoise, post-AO) — a grade he chooses by eye, with no second A/B comparison |
| 26:32–27:30 | **His own doctrine, stated** [SPEECH]: "anything you do after the denoiser — it's entirely up to you, you could do whatever you want — but **before the denoiser, we reconstructed the beauty pass**. After that point comes color grading and stylistic effects to beautify the render. So we added ambient occlusion, volume — **of course this is all optional, you could just stop here**." The match/modify boundary in this video is the Denoise node |
| 22:41–27:30 | **AO multiply, post-denoise** [SPEECH]: "we could incorporate the ambient occlusion, which is usually done with a multiplication — **it has to go at the end of the chain, after the denoising** — and you'll see what that does." This resolves the post-denoise section in frame at 27:00–27:30 [SCREEN t=1620/g1650]: downstream of Denoise, a **Multiply** node (the AO multiply) and the Glare add-back **Add** combine into the final Add to the Viewer. AO is a *finishing* move on the matched image — it is not, and in his own build never was, part of the recreation sum |
| 28:30 | An **RGB Curves** node is inserted after the final Add, before the Viewer; the image visibly darkens/moodies [SCREEN t=1710] |
| 21:30–23:00 | **Per-component tint demonstrated** [SPEECH]: "what else I could do — I could change the color — look at that — **the background was green, now it's just purple** — I could change the hue, I could change the saturation." The Hue/Saturation/Value node in the tree belongs to this move (the Emission/background branch re-hued in comp — a material change with no re-render). "I could add effects… let's add a glare node — let's add bloom — see what that looks like" |
| 30:00 | **Hue/Saturation/Value → Glare** branch in frame [SCREEN 30:00]: HSV node values as displayed (Hue 0.500, Saturation 1.000, Value 1.000, Factor 1.000 — the frame catches it at rest between adjustments) feeding a Glare node; the Glare outputs are **added back** into the main line by Add nodes. Glare configuration read at 22:00 [SCREEN t=1320 crop]: **type Bloom, Quality Medium, Size 0.500**, Highlights threshold section open |
| 31:30 | A second Glare node configured as **Streaks** [SCREEN t=1890, native read]: Quality **High**, Highlights Threshold **1.000**, Smoothness **0.100**, Streaks **4**, Streaks Angle **0°**, Iterations **3**, Fade **0.900**, Color Modulation **0.250**; its Glare output is previewed to the Viewer |
| 32:00 | **Lens Distortion** node after the Glare: Radial, Distortion **0.000**, Dispersion first previewed at **1.000** (extreme chromatic fringing fills the Viewer) and then set to **0.060** for the final [SCREEN 32:00 dispersion 1.000; 34:00 dispersion 0.060, Fit ✓] |
| 34:00 | Final chain tail [SCREEN t=2040]: Lens Distortion → **Scale (Relative, X 1.500, Y 1.500)** → **Filter (Box Sharpen)**. Output panel: /tmp\, PNG, RGBA, colour depth 16 (8/16 toggle, 16 highlighted), compression 15%. Resolution 720×1280, 24 fps, frames 1–250 (still workflow in an animation timeline) |
| 29:00–31:00 | Glare tuning is slow on his machine, and he says why [SPEECH]: "every little change you make, it takes a while to process… it's a complicated node system — every little change it has to add, multiply, add, reapply some of the effects. I'm sure there's some way to speed things up — haven't really looked into that yet — but it's a minor inconvenience." (The whole tree re-evaluates per tweak at full res.) Bloom judged "a little too aggressive" and backed off |
| 31:13–31:37 | Finishing doctrine [SPEECH]: "you want clarity — you want to be able to see the subject's face — you want to see all the details, the body and the face — **you don't want to overdo these effects**" |
| 32:00–33:11 | Dispersion at 1.000: "**this is too aggressive**" [SPEECH] → settled at 0.060 [SCREEN g1920]. Scale rationale spoken: "I rendered the image in 720×1280 — I usually render in a low resolution like that and then scale up later." Sharpen: "another thing I would do is sharpen — that produces mixed results; sometimes it looks bad, sometimes it looks good… I just want her face to be clear enough so you could see the details, the eyes and whatnot" |
| 33:33–34:18 | Close [SPEECH]: "this tutorial is about reconstructing the beauty pass — **I think we've achieved that. All these extra things I did is completely optional.**" Then the animation-course outro (Patreon) over the final settings frame [SCREEN t=2040] |

## The pass list (of record, from the Render Layers socket list)

Image (Combined) · Alpha · Diffuse Direct · Diffuse Indirect ·
Diffuse Color · Glossy Direct · Glossy Indirect · Glossy Color ·
Transmission Direct · Transmission Indirect · Transmission
Color · Volume Direct · Volume Indirect · Emission · Ambient
Occlusion · Noisy Image · Denoising Normal · Denoising Albedo ·
Denoising Depth. [SCREEN 9:00, full socket list read]

Wired into the recreation: all of the above **except** Image
(the reference), Alpha, Ambient Occlusion, Noisy Image,
Denoising Depth. Denoising Normal/Albedo feed the Denoise
node's guide sockets, not the sum.

## SHOULD-BE-SEEN check (against INTAKE.md)

- "Decomposes and recreates a beauty pass in the compositor:
  which passes feed it, in what math" — **SEEN**, in full,
  node by node.
- "What the recreation buys: control of noise" — **PARTIAL /
  reframed by the evidence**: noise control is not a benefit
  of the recreation; it is its *cost*. The passes are raw, so
  the recreation must re-do the denoise the renderer already
  did (one compositor Denoise node, guide passes, defaults).
  What the recreation buys is per-component control (below).
- "Control of fireflies" — **NOT DEMONSTRATED as such**: no
  firefly-specific step (no clamping — Clamp Result is OFF
  everywhere; no thresholding) appears. The Denoise node is
  the only noise/firefly instrument.
- "Per-component grade" — **SEEN, twice over**: first as
  component surgery (fog/volume amount changed in comp at
  ~19:30, "without re-rendering"; the Emission branch soloed
  at ~20:30), then as whole-image finishing on the matched
  recreation (Glare bloom + streaks, RGB Curves, Lens
  Distortion dispersion, Scale, Box Sharpen). The estate's
  Pass 3 variant demonstrates the component-level move
  (per-branch gains), which is the half the plan's gate
  names.

## Premise surprises (evidence, not error)

1. **The recipe is imported, not native.** The video opens on
   the Chaos **V-Ray for Nuke** "Back to Beauty" documentation
   and translates its formula into Cycles passes on a
   whiteboard. The Cycles form coincides with Blender's own
   documented pass-combining example, but the presenter's
   stated source is the V-Ray page (Google tab: "formula for
   beauty pass").
2. **The comparison beauty is already denoised.** Render
   Denoise is ON in the source render (512 samples, threshold
   0.0300, min 120), so his Switch A/B compares *his*
   compositor-denoised recreation against the *renderer's*
   denoised beauty — two different denoise runs over (nearly)
   the same data. Any visible difference he might have seen
   is denoise difference, not recipe error. He shows no
   numbers either way.
3. **SSS has no branch.** The V-Ray formula lists SSS; the
   Cycles build has no Subsurface passes enabled, so SSS
   energy rides inside the diffuse passes in this recipe.
   (Pass 3 tests this directly on the estate template, whose
   skin carries subsurface weight.)
4. **The background is Emission.** With no Environment pass
   and a black world, the emissive backplate is why Emission
   must be added for the recreation to include a background
   at all — he calls this out himself ("that's missing from
   our reconstruction").

## UNREADABLEs

- **U-1** The exact factor value on the first Mix node as
  placed (Factor 0.500 is the node default visible at 9:00;
  the expanded node at 21:00 reads 1.000) — resolved as:
  all recipe Mix nodes run at Factor 1.000 in the finished
  tree (one native read + the math requires unity). Counted
  as read, not unreadable, in the final tally: the 0.500 is a
  placement transient.
- **U-2** Transmission Indirect/Color and Volume/Emission
  checkbox states in the Passes panel are cut off at the
  panel's lower edge in every frame that shows it; their
  enablement is established instead by the Render Layers
  socket list (sockets exist only for enabled passes).
  Screen-resolved by a second surface; not a gap.
- **U-3** The post-denoise Multiply + Add at 27:00–27:30
  (t=1620/g1650): two long lines enter from off-frame left and
  wire attribution (which passes/branches they carry, and
  what the Multiply multiplies) cannot be settled at 720p.
  The narration settles every half: Volume is summed
  **before** the Denoise node for the match ("because the
  volume AOV could be noisy"), refuting candidate (a) as
  the *matched* form; the 27:00 Multiply is the **AO
  multiply**, placed by his own rule "at the end of the
  chain, after the denoising" (22:41); and the bottom Add
  at 27:00 is a **second addition of the Volume sum** after
  the AO multiply — "we already incorporated volume here,
  but I'm doing it again because it looks better" (25:39).
  Nothing of technique content remains unreadable in U-3;
  it is counted **resolved by narration**. The estate
  rebuild does not depend on the residue: Pass 3 builds the
  *matched* form (volume once, pre-denoise), and the
  double-volume is recorded in TECHNIQUE as a grade, not
  as recipe.

## Claims list (Pass 3 test list)

- **C-13-1** The recreation recipe is: for each of Diffuse /
  Glossy / Transmission, (Direct + Indirect) × Color; plus
  Volume Direct + Volume Indirect; plus Emission — all summed.
  [whiteboard 0:50 + SPEECH 0:50–1:40 + tree 15:00/21:00]
- **C-13-2** The recreation reproduces the renderer beauty
  (his claim, asserted via Switch A/B viewing; no numbers in
  the video). [SPEECH 15:40 + SCREEN 18:00]
- **C-13-3** One compositor Denoise node at the end of the
  chain, guided by Denoising Albedo + Normal, restores the
  recreated sum to a clean image (HDR ✓, Accurate, Follow
  Scene — the node's defaults). [SCREEN + SPEECH 14:10–15:40]
- **C-13-4** The passes must be enabled before rendering
  (Combined + Denoising Data + the Light pass set); nothing
  in the technique recovers a pass that was not rendered.
  [SPEECH 6:50 + panel reads]
- **C-13-5** Background/environment enters the recreation
  through the Emission pass when the backdrop is emissive
  geometry; omitting Emission loses the background.
  [SPEECH 13:05 + scene construction]
- **C-13-6** The branch grammar is uniform: build (Add,
  Multiply) once, Shift+D-duplicate per component.
  [SPEECH 10:07 + SCREEN]
- **C-13-7** Finishing moves demonstrated on the matched
  recreation: Glare Bloom add-back (Medium, Size 0.500),
  Glare Streaks (High, Threshold 1.000, Smoothness 0.100,
  4 streaks, Iterations 3, Fade 0.900, Color Mod 0.250),
  RGB Curves, Lens Distortion dispersion 0.060, Scale 1.5×,
  Box Sharpen. [SCREEN 22:00–34:00]
- **C-13-8** No clamping is used anywhere in the recipe
  (Clamp Result off, Factor 1.000) — HDR values survive the
  recreation. [SCREEN 21:00]
