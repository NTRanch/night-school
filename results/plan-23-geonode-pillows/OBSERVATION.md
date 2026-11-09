# OBSERVATION — Plan 23 Pass 1: KenFurFox, Geonode for Pillows (rule34video 3881817)

Observer: Pax (subagent run, 2026-11-06). Sources: 141 frames at
a 5 s grid (`frames/full/f_0001` = t≈0 … `f_0141` = t≈700 s),
18 native-resolution node-editor crops (`frames/crops/nodes_*`),
panel/status crops, watch-page metadata (INTAKE.md), MANIFEST.md.
Frame timestamps below are grid times (frame index − 1) × 5 s,
±5 s. Transcription: see MANIFEST — the audio is transcribed on
primo (whisper lane); this observation is screen-first per the
census-is-a-screen lesson, and any speech claims are marked as
pending the transcript census where they matter. Blender in
frame: **4.4.3** (status bar, every frame). Estate Blender:
5.2.3 LTS — drift recorded in PASS3-REBUILD.md.

## Premise verdict — the plan's premise is twice wrong

1. **Duration.** Plan says 2:04. Page JSON-LD says PT0H11M46S
   and the acquired file probes at **706.048 s (11:46)**. Plan
   erratum filed in the local plan copy.
2. **Subject.** The plan expects pillow *construction* (seam
   pinch, plump falloff, fabric subdivision). The creator's own
   description (as seen): "Just a short tut abou how to use the
   set position geonode for deforming on 'collision'". The screen
   confirms the description, not the plan: **the pillow form is
   never constructed** — the cushion is a subdivided box whose
   plump/dent behaviour comes entirely from a Geometry Nodes
   **Set Position** offset driven by **Geometry Proximity** to a
   character mesh. There is no seam, no seam pinch, no fabric
   subdivision anywhere in 141 frames. SHOULD-BE-SEEN scoring:

   - "GN setup turns a base shape into a pillow" — PARTIAL: a GN
     setup makes a box *behave* like a soft cushion under a
     sitter; the pillow silhouette itself is just the box.
   - "seam pinch" — CONTRADICTED (absent).
   - "plump falloff" — SEEN, in mechanism if not in name: the
     falloff is a Map Range + Color Ramp curve over proximity
     distance (below).
   - "fabric subdivision" — CONTRADICTED as fabric; the density
     is plain edit-mode mesh subdivision of the box.
   - "parameterised" — PARTIAL: parameterised by node values
     inside the group; **no Group Input parameters are exposed**
     — the Group Input carries only Geometry (and the default
     Selection feed). Every control is an internal node value.

## The scene (what the demo is)

A pre-built scene: a rigged cartoon crocodile character
("Gummigoo", Metarig + "Gummigoo Rig", 807 bones per status bar)
and a chair built from boxes (collection `chair`: seat block +
tall backrest). Two cushions are treated in sequence:

- **Demo A (≈0:00–6:00) — the tail cushion.** A thin slab box on
  the seat block, under the seated character's tail.
- **Demo B (≈6:00–11:46) — the seat cushion.** A larger slab the
  character sits on directly; the same node group (named
  **`kissen`** — node-editor header, f_0115/f_0127; Dutch/German
  for "pillow/cushion") is tuned further and finally driven live
  in Pose Mode: posing the tail/hip bones dents the cushion in
  real time (f_0135: header "(1) Gummigoo Rig : tail", Rotate
  gizmo active, cushion dented under the sitter).

## Timed log (screen evidence; frame refs are the 5 s grid)

- **0:00–0:55 (f_0001–f_0011).** Character in T/A-pose variants;
  a default cube at the character's feet is moved/scaled. The
  chair (seat block + backrest) is present/assembled. Outliner:
  `char` (Gummigoo, Metarig, Gummigoo Rig, Hat), camera, light.
- **≈1:00–2:30 (f_0013–f_0030).** Character seated on the chair;
  the thin slab (the future tail cushion) sits on the seat block
  under the tail. The seat block carries a **Subdivision Surface
  modifier, Simple, Levels Viewport 1 / Render 2** (f_0033,
  properties breadcrumb for the seat-block object) — note this
  modifier is on the *chair block*, not proven for the cushion.
- **≈2:35–3:00 (f_0031–f_0036).** The slab is shown with a dense
  regular grid (edit-mode subdivision already applied to the
  base mesh). Density measured later, at f_0085's status bar:
  the cushion object in edit mode reads **Verts 44/1,538 ·
  Faces 0/1,536** — 1,536 faces = a box at 16×16 faces per side
  (subdivided ×16 per edge). Base-shape contract: a closed box
  mesh, ~16 segments per edge, no modifiers required.
- **≈3:45 (f_0046).** Geometry Nodes workspace. The cushion
  object (outliner name `Cube`) has **no modifiers at all**
  ("Add Modifier" empty) — the GN modifier is created now
  ("New" node group). So the pillow's stack starts as: base
  mesh + one GN modifier, nothing else.
- **≈4:30 (f_0055).** Tree so far: **Group Input → Set Position
  → Group Output**; Set Position Offset unwired (X/Y/Z 0 m).
  The add-node search ("obje…") is open on Object Info; the menu
  also lists the creator's installed "Bradley GN Presets" —
  none is used in the visible build.
- **≈5:00–6:00 (f_0061–f_0073).** Side chain added: **Object
  Info** (object field reads "Gummigoo…", mode **Relative**) →
  Geometry output feeds **Geometry Proximity** (target mode
  **Faces**). Proximity **Distance** → **Map Range** Value.
  At f_0073 the Map Range is still at defaults (Float, Linear,
  Clamp on, From 0.000–1.000 → To 0.000–1.000) and its Result
  wires **directly into Set Position's Offset** (scalar →
  vector promotion: equal offset on all axes — an intermediate
  form, replaced later).
- **≈7:00 (f_0085).** A **Color Ramp** is inserted: Map Range
  Result → Ramp Fac; Ramp **Color → Set Position Offset**
  (still direct, still all-axes via color→vector). Ramp at this
  moment: white at Pos 0 opening to black at Pos 1 (stop 0
  selected, Pos 0.000, white) — i.e. near = full offset. This
  polarity is **reversed again before the end** (below); the
  creator is visibly iterating on the curve, not following a
  fixed recipe.
- **≈7:30 (f_0091).** Tuning continues on the seat cushion:
  Map Range **From Min −1.600** (intermediate value). Ramp
  stop 1 at Pos 1.000, white.
- **≈8:50 (f_0107).** **Combine XYZ** inserted: Ramp Color →
  Combine XYZ **Z** only (X 0.000, Y 0.000) → Vector → Set
  Position Offset. From here the displacement is **vertical
  only**. (Color→float into Z: the ramp is grayscale, so the
  conversion is the gray value.)
- **≈9:30–10:30 (f_0115–f_0127).** Final tuning, stable across
  every later frame: **Map Range: From Min −2.100, From Max
  1.000, To Min 0.500, To Max 0.900** (Float, Linear, Clamp on).
  **Color Ramp (RGB, Linear): stop 0 black at Pos 0.714**
  (f_0115/f_0127/f_0139 all read Pos 0.714), **stop 1 white at
  Pos 0.982** (f_0115) — black plateau from 0 to ~0.71, linear
  rise to white at ~0.98.
- **≈10:30–11:46 (f_0127–f_0141).** Playback/pose demo: the
  rig is posed (tail and hip bones rotated, hand pressed onto
  the cushion in close-ups f_0129–f_0133 thumbs) and the cushion
  surface dents under the contact and stays plump elsewhere.
  Final tree (f_0139, widest readable view): Group Input →
  Set Position → Group Output, with the Object Info →
  Proximity → Map Range → Color Ramp → Combine XYZ chain
  feeding Set Position's Offset, and the Group Input's
  Selection feeding Set Position's Selection.

## What the tuned numbers actually do (screen + arithmetic)

With Clamp on, distance d (metres, ≥ 0) maps to
Fac = 0.500 + clamp((d + 2.100) / 3.100) × 0.400, so:

- d = 0 (touching): Fac ≈ 0.771 → ramp ≈ (0.771 − 0.714) /
  (0.982 − 0.714) ≈ **0.21** → Z offset ≈ +0.21 (in the ramp's
  0–1 output units, applied as metres by Set Position).
- d = 0.5 m: Fac ≈ 0.835 → ramp ≈ 0.45 → Z ≈ +0.45.
- d ≥ ~0.83 m: Fac ≥ 0.900 → ramp saturates… precisely, Fac
  reaches the ramp's white (0.982) only as d → 1.0 (From Max);
  at d = 1.0, Fac = 0.900, ramp ≈ 0.69; beyond From Max the
  clamp holds Fac at 0.900 → Z ≈ +0.69 everywhere far away.

So **the whole cushion is lifted** (+0.21 … +0.69 in Z), least
at the contact patch and most away from it: the "dent" is
*relative* — a depression at the contact carved out of a
general plumping lift. That is the video's actual mechanism,
and it is the opposite construction from "push down where
touched": nothing is ever pushed below its rest position.
(These are arithmetic consequences of the on-screen values,
marked DERIVED; Pass 3 measures the rebuilt surface directly.)

## Claims list (Pass 3 test list)

- **C-1.** A subdivided box + the `kissen` group deforms under
  a character mesh with no simulation, in real time. (Screen:
  pose demo f_0127–f_0141.)
- **C-2.** The deformation needs only proximity *distance* to
  the character's faces (Geometry Proximity, Faces mode,
  Object Info in Relative mode). No weight paint, no vertex
  groups, no drivers are used anywhere in 141 frames.
- **C-3.** With the final values (Map Range −2.100/1.000 →
  0.500/0.900; ramp black ≤0.714, white at 0.982; Z-only), the
  contact patch displaces *less* than the surround — a relative
  dent of ≈0.48 m between contact and far field (DERIVED from
  C-3's values: 0.69 − 0.21). Pass 3 measures this.
- **C-4.** The group works on two different cushion sizes
  (tail slab, seat slab) with the same tree; only values were
  re-tuned between demos (From Min −1.600 seen mid-tuning).
- **C-5.** Base-shape contract: closed box, ~16 segments/edge
  (1,536 faces measured on the tail cushion). Below that
  density the dent cannot resolve — stated as the sweep's
  resolution axis in Pass 3, not claimed by the creator.
- **C-6.** The displacement is Z-only in the final form
  (Combine XYZ, X = Y = 0). Intermediate forms displaced on all
  axes (scalar→Offset, then color→Offset) and were replaced —
  the all-axes form visibly misplaces the cushion sideways
  (inferred from the iteration; the frames show the forms, not
  a stated reason). INFERRED, evidence: f_0073, f_0085 vs
  f_0107 wiring.

## UNREADABLEs (counted honestly)

- **U-1.** Exact object name in Object Info: reads "Gummigoo…"
  (truncated in every crop). It is the character mesh object;
  whether it points at the mesh or the rig object is not
  resolvable at video resolution. (Pass 3 uses the mesh —
  proximity to faces requires geometry.)
- **U-2.** Whether the *pillow* object carries a Subdivision
  Surface modifier after the GN modifier in the final stack:
  no frame shows the pillow's full modifier panel readably.
  The smooth look is consistent with mesh density alone.
- **U-3.** The seat cushion's exact base-mesh segment counts
  (only the tail cushion's 1,536 faces are measured, f_0085).
- **U-4.** Ramp stop 1's final position: 0.982 read at f_0115;
  later crops truncate the stop readout. Treated as 0.982.
- **U-5.** Group Input interface beyond Geometry/Selection:
  no frame opens the interface panel; no extra inputs are
  visible on the Group Input node in any crop.
- **U-6.** Anything said in narration: pending the transcript
  census (MANIFEST). No claim above rests on speech.

Total: **6 UNREADABLEs**, 1 INFERRED claim (C-6's reason).
Node names/connections not listed here were not guessed:
every wire in the spec (TECHNIQUE.md) is visible in at least
one named crop.
