# Plan 22 — Technique sheet (Pass 2 distillation)

Source: "Tutorial: Shrinkwarp Sleeve [Blender]", KenFurFox,
rule34video 3881849 (see OBSERVATION.md for the timed log and
claims; MANIFEST.md for the pinned capture).

## Premise correction (evidence in OBSERVATION.md §1)

The video is NOT a garment-sleeve-on-an-arm tutorial. It
builds a **responsive sleeve**: a thick-walled tube worn over
an armature-animated shaft asset (outliner: "Horse Cock – CC
BY NC SA"; sleeve collection `sleeve.001`). "Responsive" =
the sleeve stays conformed to the underlying mesh while that
mesh is posed/moved by its bone. The mechanism — a
shrinkwrap-projected collider proxy carrying a surface-
deformed visible shell — is exactly a clothing-fit mechanism,
and the plan's rebuild question (does it survive a bent
joint?) is answered by the Pass 3 rebuild on an estate arm.

## The named preset — `NS22-RESPONSIVE-SLEEVE-FIT`

Three objects, two modifier stacks, one parenting rule.

### A. Sleeve blank (visible shell, before modifiers)

- A plain cylinder tube, open ends, sized loosely over the
  limb segment it covers; **14 loop cuts** along its length
  (operator panel read at ~2:05: "Number of Cuts 14") so it
  has the longitudinal resolution to bend.
- In the demo the blank is built next to an already-existing
  sleeve (`sleeve.001`, 3,649 verts at 0:00) — the tutorial
  rebuilds the fit rig on a fresh cylinder, then the finished
  stack lives on `sleeve.001`.

### B. Collider proxy — the fit engine (object `collider.001`)

A dense tube around the same segment (status-bar census at
~4:11: **4,213 verts / 4,203 faces**). Per the narration
(V2/V5 in OBSERVATION.md §5) it is a **copy of the sleeve
blank**, lengthened and densified (creator's stated density
intent ≈ 500 faces at the cut stage, V3), caps deleted
(V4). One modifier read in
full at native-res crops (frames/crops/crop_0051.png,
crop_0066.png, frames/axis/a_14–a_20.png):

| Shrinkwrap field | Value (as seen) |
|---|---|
| Wrap Method | **Project** (switched from Nearest Surface Point at ~4:05, dropdown read in frames/axis/a_08.png) |
| Snap Mode | **On Surface** |
| Limit | **0 m** |
| Subdivision Levels | **2** (set at ~4:15; reads 0 before, 2 after) |
| Axis | **UNREADABLE** — X/Y/Z buttons read uniformly unselected in every crop; the creator is not seen clicking one. Resolved by the Pass 3 rest-pose conformance test (see PASS3-REBUILD.md), not by guessing. |
| Negative / Positive | **both ON** |
| Face Cull | **Off** (Invert Cull off) |
| Target | the body mesh (`Horse_Cock_JawsEdition`) |
| Auxiliary Target | none |
| Offset | **0 m** |
| Vertex Group | none |

Mechanism: Project + On Surface + both directions + no face
cull + offset 0 glues the collider to the target surface
along the projection axis; Subdivision Levels 2 projects a
2×-subdivided copy so the glue follows surface detail the
base mesh would bridge over. Because the modifier
re-evaluates every frame, the collider tracks the target as
the target's own armature poses it — that is the whole
"responsive" trick; the shrinkwrap is not a one-time fit.

### C. Visible sleeve stack (object `sleeve.001`, top→bottom)

1. **Surface Deform** → Target = `collider.001`;
   Interpolation Falloff **4.000**; Strength **1.00**;
   Vertex Group none; Sparse Bind OFF; **Bind** pressed at
   rest (~5:00; the button reads Unbind afterwards).
2. **Solidify** → Mode Simple; Thickness **−0.5 m** at demo
   scale (demo tube radius ≈ 0.57 m by grid measure, so
   thickness ≈ −0.87 × tube radius — a ratio, not an estate
   constant); Offset **−1.0000** (wall grows fully inward,
   outer surface untouched); Even Thickness OFF; Rim **Fill
   ON**; Only Rim OFF; Vertex Group none.

Mechanism: the visible shell never touches the body or the
shrinkwrap directly. It is bound to the collider, so
whatever the collider does — including re-projecting onto a
bent/posed target — the shell follows with smooth falloff
interpolation, and the solidify wall hangs inward from the
fitted outer surface. Separation of concerns: collider =
fit, shell = looks, solidify = wall.

### D. Assembly rule

The sleeve collection sits **inside the target armature's
hierarchy** (outliner, passim: `sleeve.001` collection under
`Armature.001`, containing `Armature.003`, `collider.001`,
`sleeve.001`). Gross motion comes from the rig; fine fit
comes from the collider's per-frame reprojection. The demo
then moves the bone (Pose Mode, Move Y 0.1187 m / 0.30049 m
read from the operator panels at ~10:25 / ~11:15) and the
sleeve slides along the shaft still conformed; a green
translucent material + area light close the video (beauty
pass, not technique).

## Adopt / Adapt / Reject

- **Adopt** — the three-part architecture (projected
  collider + surface-deformed shell + inward solidify) and
  every read setting in the table above.
- **Adapt** — demo scale → estate scale by ratio (solidify
  thickness −0.87 × sleeve radius); demo target (a shaft
  asset) → an estate body over a real elbow; the collider
  gets an Armature modifier (RightArm/RightForeArm hard
  weights) ahead of the Shrinkwrap so the pose can move it —
  in the demo the collider rides the armature hierarchy
  instead (same dependency, different plumbing; recorded as
  an adaptation, per-edit attribution in PASS3-REBUILD.md).
- **Reject** — nothing in the read stack. The one UNREADABLE
  (Project axis) is resolved by measurement in Pass 3, not
  rejected.

## The plan's question

Does the demonstrated case include a bent joint? **No.** The
demo's target bends only via a single bone translated/posed
along its own length (slides and tilts at ~6:00–7:30 and
~10:00–12:00); no hinge joint is flexed through angles, and
no pinch/slide measurement is taken. The bent-joint case is
exactly what Pass 3 must supply.
