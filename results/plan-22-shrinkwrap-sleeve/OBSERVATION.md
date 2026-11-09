# Plan 22 — Pass 1 Timed Observation

Frames: `frames/full/f_NNNN.png` at 5 s intervals (149 frames,
0–745 s, native 1920×1080), `frames/view/` scaled copies,
`frames/axis/a_NN.png` at 1 s intervals over 238–268 s,
native-res panel crops in `frames/crops/`. Times below are
frame times (±2.5 s). Blender version on screen: **4.4.3**
(status bar). Screen governs; narration is a separate
provenance class (§5, added when the transcription landed).

## §1 Premise check — the surprise

The plan expects "sleeve mesh, shrinkwrap settings, fixes for
offset/pinching at the joint" on a garment. What the screen
shows instead:

- The scene's subject asset lives in a collection named
  **"Horse Cock – CC BY NC SA"** (outliner, every frame): an
  armature-animated shaft model. The "sleeve" is a
  thick-walled tube worn over that shaft — an adult-toy /
  anatomy sleeve, not a garment sleeve.
- The stated purpose (page description + narration §5) is
  **"responsive sleeves"**: the sleeve must stay conformed
  while the underlying mesh is posed by its bone.
- There is **no hinge joint and no garment** anywhere in the
  747 s. The bent-joint question in the plan is therefore
  NOT demonstrated by the source; Pass 3 supplies it.

The technique itself (shrinkwrap fit) is exactly the plan's
target mechanism, so the run proceeds at full scope with the
premise correction recorded — this is a classification
correction, not a CAPTURE-BLOCKED case: the video IS a
shrinkwrap sleeve tutorial, with "sleeve" in the other sense.

## §2 Timed log (screen)

| t | What the screen shows |
|---|---|
| 0:00 | Existing scene: `sleeve.001` selected (status: 3,649 verts / 3,691 faces), target asset + armature + "trash" collection. The tutorial rebuilds a fit rig that already exists in draft. |
| 0:25 | `Armature.001` inspected: single long bone visible, object scale 0.300. |
| 0:50 | Right-orthographic view; armature transform panel (scale 0.300). |
| 1:15 | A fresh **Cylinder** in Edit Mode at the shaft's end — the new sleeve blank starts here. |
| 1:40 | White cylinder blank positioned over the shaft. |
| 2:05 | **Loop Cut and Slide: Number of Cuts 14** — the blank gets its longitudinal resolution. |
| 2:30 | End-on view: blank's open end flared around the shaft tip. |
| 2:55 | Cylinder linked/renamed into the sleeve data ("Data-block renamed to sleeve.001", status bar). |
| 3:20 | **Solidify panel on sleeve.001** (crop_0041): Simple, Thickness **−0.5 m**, Offset **−1.0000**, Even Thickness OFF, Rim Fill ON, Only Rim OFF, no vertex group. |
| 3:45 | Add Modifier menu open on **collider.001** (Deform category highlighted) — a separate proxy object carries the fit. |
| 4:05 | Shrinkwrap Wrap Method dropdown (a_08): **Nearest Surface Point → Project** chosen (tooltip visible). Status: collider.001 = 4,213 verts / 4,203 faces. |
| 4:10 | Project panel full read (crop_0051 + a_14): Snap **On Surface**, Limit **0 m**, Subdivision Levels **0** (not yet set), Negative ✓ Positive ✓, Face Cull **Off**, Target **Horse_Cock_JawsEdition**, Aux none, Offset **0 m**, Vertex Group none. |
| 4:15 | **Subdivision Levels set to 2** (a_16 shows "2" being committed; a_20/crop_0066 confirm 2 in the settled panel). |
| 4:35 | **SurfaceDeform panel on sleeve.001** (crop_0056): Target empty, Falloff **4.000**, Strength **1.00**, no vertex group, Sparse Bind OFF. Stack order: SurfaceDeform **above** Solidify. |
| 5:00 | SurfaceDeform Target = collider.001; button reads **Unbind** → bind completed at rest (v_0061). |
| 5:25 | Shrinkwrap panel re-opened on collider.001 (crop_0066): all values as at 4:10 with Subdivision Levels **2** — the settled preset. |
| 5:50 | Bone edited/moved; the sleeve's proximal end deforms with the target (v_0071). |
| 6:15 | Pose Mode: target crumples in black/white stripes near the bone while the sleeve sits displaced (v_0076) — an on-screen stress moment; the creator resets/re-seats the sleeve rather than repairing verts. |
| 6:40–7:30 | Sleeve re-seated and **slid along the shaft**; it conforms over the shaft's bulges (v_0081/0086/0091). |
| 7:55 | Sleeve parked mid-shaft (v_0096). |
| 8:15–8:50 | Material work: sleeve gets a **green translucent** material (Mix Shader / Transparent BSDF read in panel, v_0106). |
| 8:50 | Close-up: the sleeve's base rim flares/stretches around the base anatomy (vb_0015) — the opening deforms, recorded as seen. |
| 9:25 | Bone moved in Edit Mode with sleeve bunched toward the tip (vb_0022). |
| 9:35 | Pose Mode move: **white jagged artefact** at the sleeve rim's contact line (f_0116) — a visible fit artefact during a move, not repaired on screen. |
| 10:25 | **Move Y 0.1187 m** (operator panel, f_0126): sleeve slides, stays conformed. Armature object scale now reads 0.120 (creator rescaled the rig mid-demo — noted, not technique). |
| 11:15 | **Move Y 0.30049 m** (f_0136): larger slide, sleeve still conformed end-to-end. |
| 12:05–12:25 | Area light (200 W, Square, 1 m) placed; final beauty framing: green sleeve conformed over the shaft (f_0146/f_0149; scene census 4,757 verts). |

## §3 SHOULD-BE-SEEN scorecard

| Plan expectation | Verdict |
|---|---|
| Sleeve mesh shown | YES — but a toy/anatomy sleeve over a shaft asset, not a garment sleeve (§1). |
| Shrinkwrap modifier settings | YES — complete panel read at native res (§2, 4:10–5:25). |
| Fix for offset failure | PARTIAL — offset is simply 0 with On Surface snap; no failure is shown or fixed. The "fix" is architectural (collider proxy), not an offset tweak. |
| Fix for pinching at the joint | NO — no joint exists in the demo; nothing about pinching is shown. |
| Projection direction addressed | PARTIAL — Project + both directions ON is the choice; the Axis field itself is UNREADABLE (§4). |
| Vertex-group limiting | NONE — Vertex Group is empty on all three modifiers (read in every panel). |

## §4 UNREADABLEs (counted)

1. **Shrinkwrap Project Axis (X/Y/Z)** — the three toggle
   buttons read uniformly unselected in crop_0051,
   crop_0066, axis_14/16/18/20 despite the modifier visibly
   conforming the collider; the creator is never seen
   clicking one. Counted as 1 unreadable field; resolved by
   a rest-pose conformance A/B in Pass 3 (PASS3-REBUILD.md),
   per the sheet (TECHNIQUE.md §B).
2. The collider's own construction steps (it exists before
   its first clear census at 4:05; its 4,213-vert tube build
   is not shown step-by-step) — counted as 1 unreadable
   process, mitigated: its census + role are fully read.
3. Whether `sleeve.001` also carries an Armature modifier
   under the two read modifiers (panel never scrolled below
   Solidify) — 1 unreadable; Pass 3 tests the stricter
   reading (no armature on the shell).

Total UNREADABLE: **3** (1 field, 1 process, 1 stack tail).

## §5 Narration (provenance class: voice, whisper large-v3-turbo)

Speech EXISTS (silence census: 266 silence-start events at
−35 dB/0.5 s over 746.6 s — narration-shaped pauses; the
Plan 12 lesson applied: census scoped, transcription
decided). Full transcript: `transcript.txt` in this run dir
(primo pin beside the media). Verbal claims are tabled in
§6 as class V, kept separate from screen claims (class S).

Landed segments (21, covering 0:00–3:47 of 12:27;
`transcript.txt` carries the completeness note — the job
was left running on primo under sibling-plan saturation):

- **V1 (0:09–0:23)** Purpose in the creator's words: a
  tutorial for "**responsive sleeves**".
- **V2 (1:25–1:38)** "now we have two out of basically a
  longer sleeve, a longer **collider for the sleeve**" —
  the collider is a sibling copy of the sleeve blank.
- **V3 (1:46–2:14)** Cut density intent: "around **500
  faces**… around 514, this is a small model" (the screen's
  Loop Cut panel read 14 cuts for one pass at 2:05; the two
  classes are kept separate — the narration states the
  target density, the screen states one pass's count).
- **V4 (2:20–2:33)** "delete the faces we don't need, **the
  caps**" — the tube is open-ended by deletion.
- **V5 (2:33–2:53)** The collider is made by **copying the
  sleeve** ("copy this sleeve… collider, this is the name
  of this game") — mitigates UNREADABLE 2 (the collider's
  build is now: copy of the blank, densified; its settled
  census 4,213 verts is the screen's).
- **V6 (2:53–3:19)** Solidify: "I go with something **minus
  0.5, but it depends on the size of your model**" — the
  thickness is explicitly scale-relative, confirming the
  Pass 2 ratio adaptation (−0.87 × sleeve radius) as the
  creator's stated intent, not an estate invention.
- **V7 (3:28–3:47)** "then add **surface deform**… select
  the **collider**" — corroborates the sleeve's Surface
  Deform → collider wiring read from the panels.

## §6 Claims list (for Pass 3 verification)

- **C1 (S)** Project + On Surface + Offset 0 + Subdiv 2
  shrinkwrap glues a proxy tube to the target surface.
- **C2 (S)** A shell bound by Surface Deform (falloff 4,
  strength 1) to that proxy follows the proxy's
  reprojection as the target is posed/moved — "responsive".
- **C3 (S)** Solidify (Simple, −0.87×radius ratio, offset
  −1, rim fill) gives the shell an inward wall without
  moving its fitted outer surface.
- **C4 (S)** The assembly survives gross slides along the
  target (Move Y 0.1187 m and 0.30049 m shown) without hand
  repair.
- **C5 (plan's question)** The preset survives a **bent
  joint** at production angles — NOT claimed by the video;
  tested by Pass 3 at three elbow angles.
