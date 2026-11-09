# Plan 41 — Pass 2 Technique Sheet (Distillation)

Source: `OBSERVATION.md` (Pass 1). Every claim is distilled
below or judged not-a-technique with a reason. Estate context:
Blender 5.2.3 (source video: Blender 2.93.1 — version drift
recorded at the claims; the UI paths he names — Film
Transparent, Camera to View, compositor Denoise fed by the
Denoising Data pass, Filmic Looks — all survive into 5.2.3
with the same names). Pair note: Plan 40 (the Lighting /
Grading half by the same creator) was still IN FLIGHT at
distillation time (INTAKE only in `runs/plan-40/`); the
40+41 pair fold is recorded as **PENDING** per INTAKE
TQ41-PAIR, and this sheet triangulates against Plan 02 in
full and against Plan 40's INTAKE questions only where
marked.

## (1) STILL GRAMMAR — the composition rules, measurably

Each item carries its evidence class: **stated** (the
creator says it as a rule), **demonstrated** (done on screen
as method), **measured-from-examples** (read off the
delivered still's framing by this run's measurement).

| # | Grammar item (measurable form) | Evidence class |
|---|---|---|
| G1 | **Crop-to-interest framing:** the frame is a crop into "the most interesting parts of the image — the body and the face"; standard sizes are explicitly NOT a target ("don't worry about conforming to 1920×1080"). The deliverable's aspect is whatever the crop wants (his: ≈0.79 portrait). | stated (s4, verbatim) + demonstrated (resolution retuned 3× on screen) |
| G2 | **Cropping the figure is allowed:** "don't worry about cropping things out — that's a key thing." A composition may cut the figure at the frame edges. | stated (s3, verbatim, flagged by him as key) |
| G3 | **Extreme fill:** the figure occupies ≈0.99 of frame width and ≈0.99 of frame height in the delivered still (bleeds at both sides and the bottom). Estate band for audit purposes: fill ≥0.90 on the dominant axis counts as obeying the spirit; his example sits at 0.99. | measured-from-examples (g0001 grounding; PASS3 §A) |
| G4 | **Minimal headroom:** headroom ≈0.005 of frame height in the delivered still — the head nearly touches the top edge. Audit band: ≤0.03. | measured-from-examples |
| G5 | **Centred head:** head centre x ≈0.487 of frame width. Audit band: 0.45–0.55. | measured-from-examples |
| G6 | **Face high, face is the focus:** face centre y ≈0.135 of frame height ("I just want the focus to be mainly the face"); the face sits in the top seventh, NOT on the upper-thirds line (0.333) — his framing is more extreme than thirds doctrine. Audit band: ≤0.20. | measured-from-examples + stated (s3) |
| G7 | **Low camera, looking up:** camera placed at the posed figure's hip height, tilted UP ≈19.4° (Rotation X 70.6°), yawed ≈−17° off the figure's frontal axis. The foreground (thighs) is foreshortened large; the face is seen slightly from below. | demonstrated + measured (t1350 Transform panel) |
| G8 | **Focal length ≈77 mm** — a standing personal value ("matches my previous render"), not derived per shot. The estate reads this as: pick a long portrait lens and KEEP it as house style; the number itself is his, the standing-value discipline is the technique. | stated (s3) |
| G9 | **Order: pose → camera → finish the face:** pose the body first; add the camera and frame; THEN set gaze to the lens (slightly down) and fine-tune the expression (mouth) against the final frame. | stated + demonstrated (s2/s3) |
| G10 | **Single-angle pose construction:** the pose is built to hold from the camera's side only — hands planted as ground support, legs pushed out with IK controls, no transition-safety, no back-side check. | demonstrated (s2/s3; §6 of OBSERVATION) |
| G11 | **Transparent-ground delivery:** Film Transparent ON ("very important"), PNG + RGBA + 8-bit + 15% compression, output folder set before rendering, render saved manually. The still is delivered as a cutout; background is a later/platform decision. | stated + demonstrated (s3/s4, panels) |
| G12 | **Cheap samples + compositor denoise:** Cycles GPU, Render 64 samples is "enough" for a still when the compositor Denoise node is fed by the Denoising Data pass (passes: Combined + Z + Denoising Data). Simplify OFF at render. | stated + demonstrated (s4, panels) |

Supporting lighting items (his lighting doctrine is Plan
40's subject; these are recorded here only because they are
load-bearing for the still's look and for triangulation):
- L1: many lights, varied in position/location/size — never
  one light "turned up to a million" (flat). [stated, s4]
- L2: back light for edge separation — "part of the
  three-point lighting setup"; solo each light to see its
  contribution. [stated, s4]
- L3: radius is the sharpness dial (small = sharp, large =
  soft; soft "very desirable for beauty shots"). [stated, s4]
- L4: shadow is a feature — flat light hides the 3D form.
  [stated, s4]
- C1 (colour): Look = Medium High Contrast as the default
  boost; Low Contrast / Filmic Log / Raw reserved as
  headroom when grading externally later. [stated +
  demonstrated, s4]

**Adopt / Adapt / Reject (estate disposition):**
- **Adopt:** G1, G2, G5, G9, G11 as written — they are
  tool-agnostic framing/output discipline and estate-shaped.
- **Adapt:** G3/G4/G6 as BANDS, not points: his 0.99/0.005/
  0.135 are one shot's extreme; the estate bands (≥0.90 fill,
  ≤0.03 headroom, face y ≤0.20) capture the doctrine
  (tight, face-led) without mandating edge-bleed on every
  keeper. G7: the up-angle ports, the absolute camera
  distance does not (his scene is at miniature scale). G8:
  adopt the standing-lens discipline; the estate's standing
  value is a per-series choice (Plan 02's template uses
  35 mm — see triangulation). G10: adopt for stills lanes
  only; animation lanes keep transition-safe posing (his
  own stated boundary, §6.1's family). G12: adopt the
  MECHANISM (low samples + Denoise-node finish) as a
  stills-preview economy; keeper renders keep the estate's
  existing quality gate — see triangulation TQ41-3.
- **Reject:** resolution-as-crop-dial as an estate WORKFLOW
  (G1's mechanism, not its rule): the estate sets resolution
  from the delivery target and crops with camera shift /
  render region, because resolution changes also change
  sampling cost and downstream plate sizes. His rule (crop
  to the interesting parts) is adopted; his dial is not.
  Also rejected as technique: the Word-doc hotkey sheet and
  mesh-vs-skeleton primer (Blender literacy, no estate
  delta), and the model's outfit/skin panel specifics
  (one commercial model's UI, no transferable mechanism —
  the transferable part, "work on a copy, keep the original
  clean", is adopted as file discipline).

## (2) TRIANGULATION vs Plan 02 (and Plan 40, as landed)

Plan 02 = RamFutaNSFW's pipeline (presented by Anime Nyan);
Plan 41 = Anime Nyan's own "Basics" teaching. The two voices
are different artists; Anime Nyan connects them (sponsor/
uploader of 02, teacher of 41).

| Topic | Plan 41 (Anime Nyan, Basics) | Plan 02 (RamFutaNSFW) | Reading |
|---|---|---|---|
| Camera order | Pose FIRST, camera after; face finished against the frame (G9) | Camera BEFORE pose; pose built inside the frame (C-02-1) | **DISAGREEMENT — a choice, not an error.** Both end at the same place (pose verified in the final frame; gaze/expression finished last). 02 front-loads the frame, 41 back-loads it. Estate doctrine candidate: either order is legal IF the final-frame check happens — the check is the invariant, the order is style. |
| Lens | ≈77 mm standing value (G8) | 35 mm standing default (C-02-1) | **DISAGREEMENT — choice.** Both are standing values kept across shots (the discipline agrees; the number differs). 77 mm compresses/flattens; 35 mm widens. Named per-series choice. |
| Delivery format | ≈1963×2482 (aspect 0.79), tuned as the crop (G1) | 1080×1920 (aspect 0.5625) standing | **DISAGREEMENT — choice**, downstream of G1: 02 conforms to a platform size, 41 explicitly refuses to ("don't worry about conforming"). Portrait orientation AGREES. |
| Figure fill / headroom | 0.99 / 0.005 measured (G3/G4) | Template stills measured THIS RUN: fill 0.51 wide / 0.61 high, headroom 0.213 (PASS3 §A) | **DISAGREEMENT — the audit's headline.** 02's delivered tutorial still is tighter (his render is post-cropped ≈85%+ per Plan 02 PASS4) but the estate TEMPLATE built from 02 sits far looser than either artist's delivered framing. The estate's own stills obey neither voice's fill. |
| Face placement | Face centre y 0.135, head centred (G5/G6) | Template: face centre y 0.282, head centre x 0.507 | Agreement on centring (both ≈0.49–0.51); disagreement on face height (0.135 vs 0.282). |
| Move-the-model | Armature object never transformed; pose via the rig's master control (G moved the hips THROUGH the pose) | "Never move the model" — moving the model object broke the rig on screen (C-02-2) | **AGREEMENT (doctrine candidate):** the OBJECT transform stays identity; posing happens in pose space. 41's G-on-master-bone is pose space, not an object move — the two voices state the same invariant from opposite sides. |
| Backdrop / world | World nodes DELETED (black), lights only; Film Transparent — the still is a cutout (G11) | Emissive photo backdrop IS the environment; World 0.000; no HDRI (C-02-5) | **DISAGREEMENT — choice of product:** 02 delivers a finished scene image; 41 delivers a transparent cutout for later compositing/posting. Both reject HDRI worlds and both zero the world contribution — partial agreement under different products. |
| Render economics | 64 samples + compositor Denoise node (G12) | Adaptive NT 0.0100 / Max 4096, denoise state unreadable (C-02-8) | **DISAGREEMENT — choice with a mechanism difference:** 41 buys quality with a denoise NODE on a cheap render; 02 buys it with samples. Both are Cycles/GPU. Estate note: 41's pair is the faster iteration loop; 02's is the safer keeper loop. Not merged — named per-lane. |
| Post | In-Blender compositor (Denoise node) + optional Photoshop afterwards (C-41-10) | External: Lightroom Lens Blur (synthesised DoF) + Photoshop signature (C-02-9) | **DISAGREEMENT — choice:** post lives inside Blender (41) vs outside it (02). Both are light-touch: neither retouches or composites the figure. |
| Colour / Look | Look = Medium High Contrast in render settings; headroom variants named (C1) | Colour management UNREADABLE (never shown) | No triangulation possible on 02's side (recorded, not filled). 41's C1 is a candidate for the pair fold with Plan 40, whose subject this is. |
| Simplify | OFF at render ("we want really high quality"); model's own simplify dials turned down | ON while working, OFF before render — his only on-screen caption (C-02-3) | **AGREEMENT (doctrine candidate):** Simplify is a working-state tool, never a render state. Both voices gate on it independently. |
| Solo-check discipline | Solo each LIGHT to see its contribution (L2) | Clay render to check pose+light without colour (Target 2 #7) | **AGREEMENT in spirit (doctrine candidate):** isolate one variable and look — the estate already holds both forms; 41 adds the per-light solo to the same family. |

**Tallies vs Plan 02:** agreements (doctrine candidates):
**4** — portrait orientation (counted inside format row),
object-transform invariant, Simplify gate, solo-check
family. Clean agreements excluding the partial: **3**
(object invariant, Simplify, solo-check). Disagreements
named as choices: **6** (order, lens, format-conformance,
fill/headroom, render economics, post location) + 1 partial
(backdrop/world: product disagreement over a shared
no-HDRI/zero-world base). Not determinable: **1** (colour
vs 02).

**Pair fold vs Plan 40: PENDING at distillation; LANDED as
the addendum below** (Plan 40's records arrived after this
sheet was written; the fold was then completed from
`runs/plan-40/TECHNIQUE.md` + `MANIFEST.md`).

### Addendum — Plan 40 pair fold (landed post-distillation)

Pair identity is confirmed on both sides: Plan 40's
MANIFEST records creator/uploader **Anime Nyan** (member
807029) and the identical CC0 JSON-LD wording — the two
plans are the two halves of one creator's "Basics" series,
as commissioned.

(a) **Grading (C1): NOT the series' main doctrine.** Plan
40 finishes its look in **DaVinci Resolve** — a fixed node
chain (Filmic base → teal/orange split → look + adjust →
finish), saved as a PowerGrade (§2–§5 of its sheet).
Plan 41's Medium High Contrast Look is therefore the
STILLS-side quick grade — the cheap in-render finish for a
one-off image — where the video product gets the full
external grade. Same philosophy as G12/C-41-10 (cheap
capture, budgeted finish elsewhere), different host.
C1 stands CONTESTED, sharpened: it is a stills shortcut,
not the house grade.
(b) **Lighting (L1/L2): CONFIRMED with measurements.**
Plan 40's delivered scene is a distributed micro-source
field — PASS3 shares: Fill 27.1%, Points 17.0%, Strip
13.7%, Key 12.3%, no source above 27.1%, largest lamp
25.7 W total class (its T-40-3/4). That is L1's "many low
lights, never one light to a million" measured in the
wild, against Plan 02's kilowatt hierarchy (75.6% key
share). L2 refined: his back/rim spots are white, narrow
(14.2°), and live-but-faint (0.066% share) — separation at
whisper level; the colour comes from accents + the grade,
not the rim.
(c) **Render economics (G12): mechanism CONFIRMED
cross-video.** Plan 40 renders adaptive threshold 0.0100 /
ceiling 128 + OptiX, then budgets a SECOND denoise stage
in Resolve (its T-40-7/9). Plan 41 renders flat 64 +
compositor Denoise node. The numbers differ by product;
the doctrine is one: **cheap render, denoise budgeted as
its own downstream stage** — stated by the same creator in
both halves of the series. G12's mechanism is upgraded
from single-video stated+demonstrated to pair-confirmed;
its numbers stay per-product.
