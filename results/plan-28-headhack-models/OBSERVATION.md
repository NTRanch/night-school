# OBSERVATION — Plan 28 Pass 1: Anime Nyan, How to Headhack Models (rule34video 3644780; plan ID 3655211 is a 404 — see INTAKE)

Observer: Pax (subagent run, 2026-11-06). Sources: 102 frames at a
60 s grid (`frames/coarse/`), 225 dense frames at 10–15 s in the four
working segments (`frames/dense/`), native-resolution reads of 9 key
frames, watch-page metadata (INTAKE.md), MANIFEST.md, and two bounded
whisper transcripts (base.en, primo): the join segment (video
30:00–55:00, `transcript-join-slice.txt`) and the weight/fusion
segment (90:00–102:49, `transcript-tail-slice.txt`). Frame timestamps
below are video times. Blender in frame: **3.0.0** (status bar,
native reads). Estate Blender: 5.2.3 LTS — drift in PASS3-REBUILD.md.
Narration exists throughout (English); the two transcribed windows
cover every seam-relevant operation. The untranscribed windows
(0:00–30:00 sourcing/shaders, 55:00–90:00 texture recolour) are
screen-read at the grids; speech claims from those windows are not
relied on.

## Premise verdict — the plan's premise is twice wrong, and the audit is better than planned

1. **Duration.** Plan says 1:58. Page JSON-LD says PT1H42M49S and
   the acquired file probes at **6169.23 s (1:42:49)**. Plan erratum
   filed in the local plan copy.
2. **Identity.** The plan's video ID (3655211) is a 404 on the site.
   The title-exact match (3644780) is provably the intended video:
   its description lists the estate headhack skill's asset inventory
   item for item (INTAKE.md). Stronger: this is the very tutorial
   the estate's `local-headhack-modelled-heads` skill was
   *reconstructed from* — the skill's D-609 "recovered full tutorial"
   (~6,224 s) is this video (~6,169 s; encode differs). So Pass 2 is
   not "theirs vs ours" in the abstract: it is the estate's
   *reconstruction* audited against its *source*, finally available.
   SHOULD-BE-SEEN scoring:
   - "head separated" — SEEN (body head deleted above a chosen ring;
     donor head already separate as an imported mesh).
   - "donor body prepared" — SEEN, inverted: the *body* is the
     recipient (Genesis 8 Female); the donor is only a head.
   - "neck join handled" — SEEN, and it is the tutorial's centre of
     gravity (~25 min of the 103).
   - "weights at the seam fixed" — SEEN, as its own late pass
     (renaming + smoothing + hand touch-ups), plus an armature
     fusion and a stray-bone failure the plan did not predict.

## The scene (what the demo is)

Blender 3.0.0, file "Spirit Headhack Tutorial". Recipient: **Genesis
8 Female Mesh** (Victoria 8) imported via Diffeomorphic, MHX rig.
Donor: a Dead by Daylight head (**HK_Head01_REF** mesh + its own
skeleton), imported via PSK/PSA + UEShaderScript, sourced through
SmutBase / a DBD-rips Discord (0:00–15:00 is sourcing, importer
documentation, and Discord screens — no seam content). Donor
preparation and shader reconstruction run ~15:00–23:00.

## Timed log (screen + transcript evidence)

- **≈23:00–28:00 — placement.** Donor head moved onto the body
  (G ×2 overlays, coarse f_1320–f_1500); blue donor material against
  the tan body makes the neck intersection line visible all round.
- **≈28:00–35:00 — body preparation (transcript).** A ring on the
  body's neck is selected and hidden; everything above the line is
  deleted in wireframe, leftover points deleted one by one
  (d_1680: Delete at the back of the neck). The cut is checked
  "even"; the line is smoothed with **G Z** moves. Stated rule:
  *"I made sure that the neck was higher than the other one…
  because I want this to fit in nicely… the back of this neck is
  much higher than it is at the front… it'll be a lot easier to
  stretch these."* The donor neck is deliberately left LONGER than
  the body cut (a stump that will be dragged down point by point).
  Ring parity is checked obsessively ("I have an extra point
  here") — point counts must correspond before snapping.
- **≈35:00–46:00 — THE JOIN (transcript + dense frames).** The core
  operation, point by point around the ring, symmetrically:
  select a body (bottom) point, shift-select the donor (top)
  point, **Spacebar → Search → "Snap Selection to Active"** — the
  donor point is dragged exactly onto the body point. Preference
  setup is part of the method (spacebar set to Search, not Play).
  Failure handling, all shown:
  - a point that "sticks out" is **deleted** and the hole closed
    with **F** (a new face between three points) — "press F, in
    fact I can just hide this skeleton… and make a face between
    these ones here" (whisper slice at video ≈40:38);
  - where counts mismatch, the **Knife (K)** adds a midpoint
    (d_2580, native: knife active on HK_Head01_REF at the body
    surface, status bar shows knife controls);
  - selecting the top of two coincident points instead of the
    bottom makes faces "really really weird" — check by pressing
    G to see which point moves.
  Self-check in material preview: *"nothing's too stretched… last
  time that was a huge, huge problem"* — stretching at the seam is
  their known failure mode, and the snap method is the cure they
  settled on.
- **≈46:00 — object join (d_2760, native).** Head selected first,
  body second, **Ctrl+J**; the joined object is "Genesis 8 Female
  Mesh". Shown failure + fix: textures break because the donor's
  UV map name ("UV single") differs from the body's ("Base
  Female"); Ctrl+Z, rename the donor UV map to match, redo.
- **≈47:00–52:00 — THE WELD + seating (transcript).** The seam ring
  is lasso-selected (both coincident points everywhere), Spacebar →
  **Merge by Distance**: *"I moved [merged] 33 vertices in here…
  when I pull this point it won't separate into two things
  anymore, there'll be just one complete mesh."* Then G/GY tucks
  and proportional-editing nudges until the seam "looks
  semi-decent… it doesn't need to be perfect, it just needs to
  look semi-decent" (d_2880–d_3060).
- **≈52:00–90:00 — colour seam, in texture space.** The geometry
  seam is done; the *colour* seam is not touched geometrically.
  Body diffuse maps are unpacked and recoloured in Photoshop
  toward the donor's blue-grey (torso/arm/legs), teeth maps
  likewise; ~77:00 a **vertex-colour mask is painted at the neck**
  (d_4620, native: Vertex Paint, Mix, Strength 0.375, Radius
  248 px, pink band on the neck; a "Col" vertex-colour layer is
  present in later panels) feeding the shader blend. Long,
  mostly mechanical; grid-read only.
- **≈90:00–98:00 — weights (transcript + d_5520–d_5820).** The
  joined head does not move with the rig at all ("If I rotate it
  forward, you can see the head is not moving"). The fix is
  **vertex-group renaming**, one bone at a time, each followed by
  a pose check: donor group `joint head 01` → renamed to the body
  bone `head` (the empty original deleted first); `joint jaw 01`
  → `lower jaw`; the neck group is **Smoothed repeatedly**
  (Spacebar → Smooth, "again… and again", ×3 on the record) and
  renamed to `neck-1-twk`; `neck-twk` is then hand-painted at
  brush weight **≈0.1–0.2** (d_5700, native: Weight 0.135, Radius
  93 px, Strength 1.000, X-symmetry; operator panel shows Smooth
  Vertex Weights, Factor 0.500, Iterations 1) — painted *by
  copying the original Victoria 8 model's own weight painting*
  ("I just looked at the original model… and followed how they
  did the weight paint"). A sharp crease found on one side in a
  pose check ("it's cracking a little bit") is repainted greener
  and re-checked: "good enough, honestly."
- **≈98:00–101:00 — armature fusion + the stray-bone failure
  (transcript + d_5880–d_6060).** Donor skeleton selected, Genesis
  skeleton shift-selected, **Ctrl+J joins the armatures**; in Edit
  Mode the donor's head-bone chain (`joint_HeadA_01`) is
  **reparented to the Genesis `head` bone** and the donor's
  redundant bone deleted — "we still have the face controls"
  (d_5940, native: bone `neckhead`, parent `neckLower(drv)`, head
  Z 1.5433 m — Genesis face bones seated in the donor head).
  Then the tutorial's final bug, stated plainly: on rotation
  "the neck was just all kind of screwed up… because of just one
  bone" — a leftover donor **`joint_torso_C_01`** (and the donor
  clavicles) inside the fused rig; deleting them in Edit Mode
  fixes the neck completely. Close: MHX panel drives the finished
  rig FK/IK (d_6060, native: MHX Head/Face/Tweak panel; sidebar
  tabs include DAZ Importer, MHX, Fuse Skeletons, PSK/PSA,
  UE Shaders — the Fuse-Skeletons add-on is installed and
  distributed with the tutorial's files, but the fusion *shown*
  is the manual Ctrl+J + reparent sequence above).

## What is NOT in the video

- No shrinkwrap, no bridge-edge-loops operation, no weight
  *transfer* (no Data Transfer / transfer weights anywhere in the
  transcribed windows or the grids). The join is snap + weld.
- No bend test as a gate: pose checks are eyeball checks inside
  the weight pass ("twist this bone around a little bit").
- No numeric settings for Merge by Distance (operator invoked by
  search; the count "33 vertices" is the only number given).
- The Fuse-Skeletons add-on's own UI is never operated on screen
  in the frames read (UNREADABLE as a procedure; the manual
  sequence is what is evidenced). **UNREADABLE count: 1** (this
  item) + merge-distance value (folded into the same item's
  family). All other seam operations were read at native
  resolution or from narration.

## Claims (numbered for Pass 3)

- **C-01** A longer donor neck (back higher than front) makes the
  fit easier — less stretch per point.
- **C-02** Ring point parity is a precondition; mismatches are
  repaired by deleting points or knifing in midpoints.
- **C-03** Snap-Selection-to-Active per point joins the rings
  without stretching the topology ("nothing's too stretched";
  stretching was the previous attempt's "huge problem").
- **C-04** UV map names must match before Ctrl+J, or the joined
  mesh's textures break.
- **C-05** Ctrl+J + Merge by Distance yields one complete mesh
  that will not separate at the seam (33 verts merged, theirs).
- **C-06** The colour seam is a texture problem: recolour the
  body maps toward the donor + a vertex-colour mask at the neck.
- **C-07** Donor weights are made live by renaming donor vertex
  groups onto body bone names — no transfer, no repaint-from-zero.
- **C-08** Neck weights need repeated smoothing + low-weight
  (0.1–0.2) hand touch-ups, or the neck creases/"cracks" at bend;
  the model for the painting is the original body's own weights.
- **C-09** Armature fusion = Ctrl+J the skeletons, reparent the
  donor head chain to the body head bone, delete the redundant
  donor bone; face controls survive.
- **C-10** A leftover donor torso/clavicle bone in the fused rig
  destroys neck deformation; delete stray donor bones.
- **C-11** Face/jaw/eye function rides on the fused donor bones +
  repositioned body face bones (the distributed file's "Fixed
  Face, jaw and eye bones").
- **C-12** The head's proportions are never rescaled: correspondence
  is achieved at the ring only; the donor head keeps its size.
