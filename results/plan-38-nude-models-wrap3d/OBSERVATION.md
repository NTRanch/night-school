# Plan 38 — Pass 1 Timed Observation

Frames: `frames/view/f_NNNN.jpg` at 60 s intervals (201 frames,
0–12000 s, 960 px), `frames/d_NNNNN.jpg` at 30 s intervals over
1800–8400 s (220 frames, 1280 px), `frames/f10/f_NNNN.jpg` at
10 s intervals over 0–1200 s (120 frames). Times are frame
times (±30 s on the grid, ±15 s dense, ±5 s f10). Tool on
screen: Blender (3.2-era UI) + **R3DS Wrap 2021.11.3**
(title bar: "Wrap 2021.11.3 TRIAL PERIOD (30 Days Left)").
Screen governs; narration is a separate provenance class (§6).

## §1 Premise check — what this video actually is

The plan expects "a full Wrap3D workflow … at working length,
with the failures left in." The screen shows a **live
co-taught working session** (the creator teaches a second
person, audible in the narration slices) inside his Feng
Headhack project (Blender file: "Feng Headhack Live Tutorial
2/Chase Feng Smiley Packed Checkpoint 3.blend"; subject =
Feng Min, Dead by Daylight — the page tag). The Wrap3D arc
proper is **~30:00–~85:00** (geometry wrap) plus a second
Wrap arc at **~135:00** (texture transfer). The remaining
~2 h is the Blender-side preparation before and the
finishing/cleanup after — which is exactly the plan's
(a) preparation contract and (e) finishing pass, shown at
full working length. The wrap's product is a **nude body**:
the DAZ-template body ("GBF") conformed to the Feng head,
then blended into the host body and textured — "how to make
nude models through Wrap3D" is literal.

Project naming as seen (flagged, §5 U-3): Wrap title bars
read "[GBF to Rogue Mesh*]" for the geometry project and
"[wrapping rogue head textures*]" for the texture project;
SaveGeom writes "$PROJECT_DIR/GSF Wrapped Rogue.obj"; the
Blender object is "GBF Wrapped Feng". The template geometry
node loads "$PROJECT_DIR/GBF.obj"; the target node loads
"$PROJECT_DIR/Feng Head.obj".

## §2 Timed log (screen)

| t | What the screen shows |
|---|---|
| 0:00 | Blender, Feng file: full clothed Feng rig in A-pose; outliner "Neko Meshes" (FM_PigTail_Acc002_REF.mo selected). Status: scene 150,233 verts. |
| 1:00 | Head closeup: FM_Head00_REF.mo selected; face paint mask mesh on the head. |
| ~3:00 | Blender File View **Install Add-on** dialog open over an empty default scene — an add-on install is performed (identity UNREADABLE, §5 U-1). |
| 6:00 | Head closeup; FM_Head00_REF.mo census (status): **Verts 17,806 / Faces 29,875**. Lasso tool; mouth/face region under inspection. |
| 12:00 | FM_PigTail_Acc002_REF.mo (hair accessory) transform work (Loc Z 1.5136 m); "Ctrl+Z / Middle Mouse" keystroke overlay — the session is a recorded live tutorial with key display. |
| 20:00 | Edit Mode on FM_Head00_REF.mo: mouth interior closeup — teeth and lip interior of the game head mesh inspected (Verts 26?11,836 / Edges 26,203 in status — selection-dependent read; recorded as seen). |
| 24:00 | Edit Mode: **mouth/teeth region selected** (orange) on the wireframe head — the mouth bag is being isolated/inspected before export. |
| 29:00–30:00 | FM_Head00_REF.mo with Armature modifier (Object: rig, Bind To Vertex Groups ✓); head census now reads **Verts 10,094 / Faces 19,593** (a different object state — the REF head with modifiers; both censuses recorded as seen). |
| 32:30 | **OBJ export dialog**: file "GBF.obj"; folder already holds "Feng Head.obj" (275 KB) + "Feng Head.mtl". Export options read in full: Selection Only ✓; Scale 1.00; Path Mode Auto; Forward **−Z**, Up **Y**; Geometry: **Apply Modifiers ✓**, Smooth Groups off, **Write Normals ✓, Include UVs ✓, Write Materials ✓**, Triangulate off, **Keep Vertex Order ✓**. |
| 35:00 | Wrap graph (full): LEFT chain GBF → SelectPolygons → Subset; RIGHT chain Feng → SelectPolygons1 → Subset1; Subset+Subset1 → SelectPointPairs → Wrapping → ApplySubset → SaveGeom. A frame group encloses the GBF chain + points + wrapping. |
| 37:30 | GBF LoadGeom editor: File Name **$PROJECT_DIR/GBF.obj**, Translation 0/0/0, Rotation 0/0/0, **Scale 1** — no in-Wrap alignment transform. |
| 40:00 | Feng LoadGeom editor: **$PROJECT_DIR/Feng Head.obj**, transforms likewise zero. GBF body visible: a full nude female template body, clean quad topology, arms slightly down (A-pose). Preferences dialog open (camera: Perspective, Angle 35, Near 0.01, Far 1000). |
| 42:30–47:30 | **SelectPolygons on GBF** (Display Mode: **Polygroups**, Source: User Input): the template's polygroups render blue/red; the creator works the **− Material** list (50:00/55:00, dropdown read in full): **Torso-2, Face-2, Lips-2, Teeth-2, Ears-2, Legs-2, EyeSocket-2, Mouth-2, Arms-2, Pupils-2, EyeMoisture-2, Fingernails-2, Cornea-2, Irises-2, Sclera-2, Toenails-2, GP_Torso-1** — subset definition is by named material/polygroup, not lasso. (Red/blue here is polygroup display colour, NOT a selection binary — see §4 note.) |
| 57:30 | **SelectPointPairs: Left point count 127, Right point count 0**, warning banner: **"Points does not match geometry. Do you want to reset points selection?"** — a stale point set from the recycled project. The cursor is on **Clear All**. The stale set is cleared (next frames restart at 5). |
| 60:00 | Point count **5** — first pairs on the **nose** (nostril wings/tip), both viewports. Panel: Sync Views ✓, Symmetry **No Symmetry**, Source User Input, **Points Format: Point on Triangle**. |
| 65:00 | Point count **20** — lip ring, mouth corners, chin, nose complete. |
| 70:00 | Point count **Left 42 / Right 43** (mid-placement); **Symmetry now X** — eye rings being placed with mirroring on. |
| 72:00 (grid) | Point count **26**?? — see §4 D-1: the grid frame at 72:00 reads 26 while dense frames bracket it at 20 (65:00) → 42/43 (70:00). The 72:00 grid read is of a different viewport state (the counter in that frame's pane reads 26 — likely a stale pane or a second points node state). Dense sequence governs: counts are monotonic 5→20→42→52→69. The grid frame is recorded as a disagreement, not averaged. |
| 75:00 | Point count **52** — **ear** placement (closeup of both ears). |
| 80:00 | Point count **69** — final set: forehead, jaw, neck fill added; Symmetry reads **No Symmetry** again in this frame. |
| 82:30 | **Wrapping node editor** (the only full read): **Compute** button, **Auto-Compute OFF**; Parameters tab: **Subdivisions 3 · ICP Iterations 5 · Optimization Iterations 20 · Sampling initial 5 · Sampling final 0.2**. An "Advanced parameters" tab exists (never opened on screen — §5 U-2). Viewport: the wrapped GBF (purple) conformed onto the Feng face, point markers still shown. |
| 84:00 | **SaveGeom editor**: File Name **$PROJECT_DIR/GSF Wrapped Rogue.obj**; Save Normals ✓, Include Transform ✓, Create Intermediate Directories ✓; **Draco Params: Vertex Quant 30, Tex Coord Quant 30, Normal Quant 30, Compression 7**. Wrapped head+bust shown (eyes closed, lips parted — the Feng face in GBF topology). |
| ~85:00 | Back in Blender. (Wrap segment ends; no second geometry compute occurs anywhere in the remaining 115 min — the wrap ran **once**.) |
| 90:00 | New Blender file "Checkpoint 1.blend": **GBF Wrapped Feng** — the full wrapped nude body (head = Feng), census **Verts 18,675 / Faces 18,494 / Tris 36,974**. |
| 95:00 | **Correction shape key** work begins: object carries **Basis + Correction (1.000)**; Edit Mode on Correction with **proportional editing (Smooth, size 0.0923 m)** moving the **neck/shoulder blend zone** (header: Dx 0.002441 m …). The **ear region shows a tangled dark patch** — the wrapped ear is visibly mangled. |
| 97:30 | Material slots on the wrapped mesh read: Torso-2.001, Face-2.001, Lips-2.001, **Teeth-2.001**, Ears-2.001 (the DAZ groups carried through the OBJ round-trip). |
| 100:00–102:30 | **Eye-socket cleanup** in Correction: eye-cavity verts selected via Mouth-2.001/EyeSocket-2.001 material selection; micro-moves (G, Dx −0.00005 m class) re-seat the socket verts. |
| 105:00 | **Mouth interior** closeup in Correction: the mouth cavity is a collapsed dark region — inspected, worked. |
| 108:00 | The wrapped body lies beside the host **Neko Mesh** body; the host's shape-key stack includes **"GBF Wrapped Feng" at 1.000** among anatomical keys (Vagina_Shrink 0.000, Xia Body 0.000, dCM_V03_Thighs…): the wrap enters the host **as a shape key**. Host vertex groups include the anatomical set (Left Small Labia 4, Vagina, Rectum, Hip, Graft…). |
| 110:00 | Checkpoint 2: wrapped body rotated (Rotation 17.92°) to align with the host placement — post-wrap alignment is a Blender-side manual step. |
| 115:00–125:00 | **Eyes/lashes fitting**: LAM_Eyes set into the wrapped head's sockets; LAM_Lashes adjusted (vertex groups squintOuter.L/R, eye.L, head). |
| 132:00 | File → Export menu with **Wavefront (.obj)** highlighted, GBF Wrapped Feng selected (Verts 18,675) — the corrected wrap is exported again for the texture stage. Correction key still 1.000. |
| 135:00 | **Second Wrap project — texture transfer**: graph = LoadImage → Feng; Feng + GBF → **TransferTexture** → **ExtrapolateImage** → SetTexture; **SaveImage**: "…e Wrapped Textures/Rogue Wrapped Torso Diffuse.png", **Quality 80**, Create Intermediate Directories ✓. Viewport: the wrapped mesh wearing the transferred Feng skin texture (purple = untextured/no-UV regions at scalp/shoulders). |
| 144:00 | Blender shading workspace: material **"Lips Wrapped"** built from transferred textures; outliner/mesh list shows per-region wrapped materials: Fingernails-2, Cornea-2, Irises-2, Sclera-2, Toenails-2… |
| 156:00 | Neko Mesh material slots: **Face Wrapped, Lips Wrapped, Torso Wrapped, Arms Wrapped** (DAZ Dual Lobe Uber family) — the transferred texture set lands as per-region materials on the host. |
| 168:00–180:00 | Host body with Censor Cubes (the creator's in-editor censor blocks); "Face Wrapped" material node tree: "Feng Wrapped Head Diffuse.png" + RGB Curves → Principled BSDF (Subsurface IOR 1.400, Specular 0.500…). |
| 192:00–200:54 | Final assembly: hair + face-paint mask restored; last minutes pose the finished rigged character in Pose Mode (beauty check). The session ends mid-work — it is a live session recording, not a packaged finale. |

## §3 SHOULD-BE-SEEN scorecard

| Plan expectation | Verdict |
|---|---|
| Source/target preparation shown | YES — Blender-side: mesh inspection (mouth bag isolated), OBJ export contract in full (32:30), zero in-Wrap transforms. |
| Correspondence placement | YES — complete: stale-set clear (57:30) + full placement sequence with live counts 5→20→42/43→52→69, feature order readable. |
| Wrap parameters numerically | YES — one full read (82:30): Subdiv 3 / ICP 5 / Opt 20 / Sampling 5→0.2. Whether they were *changed* from defaults is NOT visible (no edit is seen; narration may speak — §6). Advanced tab never opened (U-2). |
| Re-wraps, which variable changed | **NONE** — exactly one Compute in 3:20:54. The plan's "each re-wrap" expectation is CONTRADICTED by the screen: the workflow is single-shot at these settings; iteration happens in Blender cleanup, not in re-wrapping. |
| Cleanup at hands/face/joints | PARTIAL vs plan — cleanup is face/neck-centric (neck blend, eye sockets, mouth interior, ears), all inside the **Correction shape key**. Hands/joints of the body are never cleaned on screen (the body below the neck needed none — the template body was already the destination body; only the head was re-targeted). |
| Blender finishing pass | YES — extensive: Correction key, shape-key blend into host, eye/lash fitting, texture-transfer round trip, per-region materials, posing. |

## §4 Disagreements & reading notes

- **D-1 (point count at 72:00):** grid frame reads 26, dense
  neighbours read 42/43 at 70:00 and 52 at 75:00. The dense
  monotonic sequence governs; the grid frame's pane is
  recorded as an unexplained stale/alternate read. Counts
  are NOT averaged.
- **Polygroup colours ≠ selection:** at 42:30–55:00 the
  red/blue viewport colours are Wrap's Polygroups display
  mode (panel-read), not a selected/unselected binary. Any
  claim about "which polygons were excluded" must rest on
  the Subset/ApplySubset structure + the wrapped result
  (full head present at 84:00), not on frame colours. What
  the screen DOES prove: subset definition is driven from
  the named-material list (− Material dropdown), i.e. by
  polygroup, on both chains (SelectPolygons + SelectPolygons1
  → Subset + Subset1).
- **Screen vs plan title:** the product name in-session is
  GBF/GSF inconsistently (title bar "GBF", SaveGeom "GSF
  Wrapped Rogue"). Recorded as seen; no resolution invented.

## §5 UNREADABLEs (counted)

1. **U-1** The add-on installed at ~3:00 (file dialog only;
   no name legible). 1 item.
2. **U-2** Wrapping **Advanced parameters** tab — exists,
   never opened in any sampled frame. Its contents are
   unreadable; the five main parameters ARE read. 1 item.
3. **U-3** Template/target naming (GBF vs GSF; "Rogue") —
   the names as seen are mutually inconsistent; which mesh
   "Rogue" denotes cannot be settled from the screen.
   (Narration may resolve; if not, it stays unreadable.)
   1 item.
4. **U-4** The exact polygroup exclusion list for the two
   Subsets (dropdown interactions seen; the final subset
   membership is not displayed as a list anywhere). 1 item.

Total UNREADABLE: **4**.

## §6 Narration (provenance class: voice, whisper large-v3-turbo)

Slice ladder (per brief): A 1800–3600 s, B 3600–5400 s,
C 5400–7200 s, D 600–1800 s — chunked-lane route on primo,
file-mediated (`whisper.sh`), single-transcriber =
**UNCONFIRMED** tier. Two voices (creator + student).
Landed claims are appended here as slices complete; the
screen record above stands without them.

- **V-1 (slice A, ~32:30 relative 0:10–0:27):** the export
  narration confirms the screen read verbatim: "you need to
  export as not experimental… selection only… apply
  modifiers is on… and keep vertex order as well, keep
  vertex order."
- **V-2 (micro M1, absolute 57:00–59:40):** the stale-set
  clear is a NARRATED teaching point, matching the screen
  at 57:30 word for word: "points does not match
  geometry — what we can do is you can actually click on
  this clear all button… just clear all points."
- **V-3 (micro M1, absolute ~57:55–59:35):** the grammar
  is taught explicitly: "we're just going to make some
  points on key areas because we need to advise the ai or
  machine program how to or where what points should
  wrap… start off by making some key points like on the
  middle of the nose… you want to make sure your points
  always match up." (Nose first, pairs matched in order —
  the screen's sequence is the taught sequence.)
- **Coverage accounting (honest):** primo whisper
  contention (many sibling jobs at 70–265 % CPU) made
  full-slice transcription crawl. Landed at record
  close: slice A relative 0:00–12:58 of 30:00
  (absolute 30:00–42:58, in `whisper.log` on primo);
  micro M1 relative 0:00–~2:40 of 4:00 (absolute
  57:00–~59:40, `micro.log`). Still queued/running on
  primo at record close: slices B, C, D (whisper.sh
  chain) and micros M2 (wrap compute, 81:00–85:00) and
  M3 (Correction start, 94:00–98:00) — their .txt
  outputs land in `slices/` when they finish. No claim
  in this record depends on the unlanded spans: every
  decisive span (export contract, subset work, stale
  clear, placement grammar, wrap parameters, compute,
  SaveGeom, cleanup, texture graph) is established by
  the SCREEN record (§2–§3), and the two narration
  checks that did land (V-1…V-3) agree with the screen
  on every point. No screen↔narration disagreement was
  found in the landed spans.

## §7 Claims list (for Pass 3 verification)

- **C-1** A polygroup-carrying clean-topology template +
  an OBJ contract (Selection Only, Apply Modifiers, Keep
  Vertex Order, Write Normals/UVs/Materials, −Z/Y) is the
  preparation that makes the wrap work.
- **C-2** Alignment (scale/pose) is a precondition discharged
  BEFORE Wrap (both LoadGeom transforms are identity).
- **C-3** Subsets defined by named polygroups on both sides
  keep non-corresponding anatomy (eye/teeth/mouth-interior
  groups) out of the correspondence problem.
- **C-4** A point set is geometry-bound: a stale set from
  another project must be cleared ("Points does not match
  geometry"), not reused.
- **C-5** Feature-ordered placement (nose → lips/chin →
  eyes with X-symmetry → ears → jaw/neck/forehead fill),
  ~69 pairs for a head, Point-on-Triangle format, is
  sufficient for a single-shot wrap at the read parameters.
- **C-6** One compute at Subdiv 3 / ICP 5 / Opt 20 /
  Sampling 5→0.2 conforms the template's head to the
  target within hand-cleanup distance (no re-wrap needed).
- **C-7** The wrap's lies concentrate at: ears (tangled),
  eye sockets (mis-seated verts), mouth interior
  (collapsed), neck blend zone (seam) — and are repaired
  in a **Correction shape key** (Basis preserved), with
  proportional-edit smoothing (0.0923 m) at the neck.
- **C-8** ApplySubset + OBJ round-trip preserves polygroups
  as material slots and the template's UVs; textures are
  then transferred in a separate Wrap graph
  (TransferTexture → ExtrapolateImage) into template UV
  space (SaveImage PNG Q80).
- **C-9** The wrapped body integrates into a host rig as a
  **shape key** (host key "GBF Wrapped Feng" = 1.000),
  not as a mesh replacement.
