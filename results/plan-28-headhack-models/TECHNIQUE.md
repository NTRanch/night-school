# TECHNIQUE — Plan 28 Pass 2: Seam practice comparison (distillation)

Distilled from OBSERVATION.md (frames + two transcript windows).
"Theirs" = Anime Nyan's tutorial method (Blender 3.0.0, Genesis 8
body + DBD donor head). "Estate" = the fleet practice of record:
`local-headhack-modelled-heads` (donor head, fused armature, fixed
face) as realised in the conformed Torogao fleet builders — one
welded Body mesh per girl, 24-vert neck weld ring, weight field
generated as a smooth analytic profile of the body template
(measured on Prima_Body: Spine2 0.65→0.03 across z 1.390–1.414,
Neck ≈0.99 at the weld ring 1.418–1.426, Neck→Head ramp
0.97/0.03 → 0.26/0.74 across 1.436–1.459, Head 1.0 above 1.478).

**The one-line answer to the plan's question:** their join method
is **snap-to-active ring correspondence + Ctrl+J + Merge-by-Distance
weld** — a weld, like the estate's. The methods do not differ in
whether the seam is welded. They differ in *where correspondence
comes from* and *where the weight field comes from*.

## Step-by-step comparison

| # | Step | Theirs | Estate | Failure each invites |
|---|------|--------|--------|----------------------|
| 1 | Recipient prep | Delete the body's head faces above a hand-chosen ring, in wireframe, point by point; even the line with G Z | Template cut at the authored weld ring (both parts derive from one parametric template; the ring exists by construction) | Theirs: an uneven cut line propagates into every later step (they spend minutes evening it). Estate: none at this step — the cut is not a step. |
| 2 | Donor prep | Donor neck left deliberately LONGER than the body cut (back higher than front) so each point has less distance to travel (C-01) | Donor head cut at its own weld ring; no stump | Theirs: interior stump geometry rides along inside the body (inert, but it is dead geometry at the seam). Estate: — |
| 3 | Correspondence | **By hand, per point:** select body point, shift-select donor point, Snap Selection to Active; symmetrically, ~24–33 points; parity repaired by deleting points / F-fills / knife midpoints (C-02, C-03) | **By construction + one transform:** identical ring counts (24 = 24); the whole donor head is scaled (XY by ring-radius ratio, Z by head-height ratio) so its ring lands on the body ring; residual snap ≤0.45 mm (measured, PASS3) | Theirs: each ring point is dragged the full radial mismatch (5.12 mm max on this pair) — the mismatch is absorbed as *local stretch in the ring band*, the failure they name themselves ("last time that was a huge, huge problem"). Estate: the mismatch is absorbed as a *global, uniform* size change of the head (−8.6% XY here) — no local stretch, but the donor head's proportions change. |
| 4 | Object join | Ctrl+J, head first / body second (active = body: name, materials, UVs follow). UV-map names must match first (C-04) | Data-level concatenation in the builder; one UV/palette convention by construction | Theirs: the UV-name break is a real, shown failure (textures gone until renamed + redone). Estate: class absent. |
| 5 | Weld | **Merge by Distance** on the coincident ring (33 verts merged, theirs; operator default distance) | Merge by distance 0.1 mm on the snapped ring (24 ring merges of 148 total on this pair; the rest are pre-existing coincident construction pairs) | Shared: an unwelded seam is not on either menu. Their weld distance (1 mm default) would also weld near-coincident interior pairs; estate's 0.1 mm is surgical. |
| 6 | Seating | G/GY tucks + proportional editing until it "looks semi-decent" by eye | Nothing to seat: ring-exact by construction | Theirs: eye-only acceptance; a bad tuck is a shading seam kept. Estate: — |
| 7 | Colour seam | Texture space: Photoshop-recolour the *body* maps toward the donor + paint a vertex-colour mask at the neck for the shader blend (C-06) | One palette per character record; head and body are textured from the same palette at build time | Theirs: hours of texture work per graft; mask edges are a painted gradient (soft, forgiving). Estate: class absent for fleet girls — but for a *foreign* donor head with its own texture, the estate has no equivalent step at all (gap, see verdict). |
| 8 | Weights — provenance | **The donor's own field, renamed:** donor vertex groups renamed onto body bone names one at a time (`joint head 01`→`head`, jaw→`lower jaw`, neck→`neck-1-twk`), each rename pose-checked (C-07) | **The body's field, generated:** seam weights are the body template's analytic profile, sampled at each vert's z; the donor's field is discarded | Theirs: the field was authored for a *different skeleton's* proportions; wherever donor and body blend zones disagree, the seam inherits the disagreement (their neck needed the next step precisely because of this). Estate: field continuity is exact by construction — but it assumes the body template's blend zones are right for the grafted head's geometry. |
| 9 | Weights — seam repair | **Smooth ×3** on the neck group + hand touch-ups at weight 0.1–0.2, X-symmetry, *copying the original body's painting by eye*; pose, find the crease ("cracking"), repaint, re-pose (C-08) | None: no repair pass exists, because no discontinuity is created | Theirs: the repair loop is the method's conscience — it catches real creases, one pose at a time, by eye. Estate: a template/geometry mismatch would pass silently — the fleet's gate is numeric + Owner eye on renders, not a per-seam pose inspection. |
| 10 | Armature | **Manual fusion:** Ctrl+J the two skeletons; reparent donor head chain to the body `head` bone; delete the redundant donor bone (C-09). The distributed alternative is the author's Fuse-Skeletons add-on (installed, listed, never operated on screen) | One armature by construction (fleet girls share the 54-bone template); the skill's fusion step targets foreign rigs (Genesis + game rip) and names Fuse-Skeletons as the mechanism | Theirs: fusion by hand leaves **stray bones** — and the tutorial's own final bug is one: a leftover donor `joint_torso_C_01` (+ clavicles) made the neck "all screwed up" until deleted (C-10). Estate: the class is real for any fused-rig work and the skill does not currently name a stray-bone sweep. |
| 11 | Face / jaw / eyes | Donor face bones ride the fusion; body face bones repositioned into the donor head in armature Edit Mode (`neckhead` head Z 1.5433 m read at native res); distributed end state = "Fixed Face, jaw and eye bones" (C-11) | Skill step 4: dedicated fix pass over face, jaw, eye bones, with the eye discipline as named work (ganged motion, aperture, closed state) | Agreement, not divergence: both treat the face fix as separate named work after fusion. The estate's eye checks are stricter (the skill's §2.6–§2.8 closed-state purity has no counterpart in the video). |
| 12 | Acceptance | Pose it and look: "good enough, honestly" | Bend test with measures + verdict pack; Owner's eye is the gate of record | Theirs ships on the maker's eye in the room. Estate: slower, reproducible, and the eye is the Owner's. |

## Failure-class scoreboard (what Pass 3 could measure)

- **Gaps at bend:** neither method can gap — both weld. (The
  unwelded-overlap strawman is not their method; the transcript
  kills it. Recorded in PASS3 as a corrected first read.)
- **Weight tears / kink concentration:** theirs concentrates
  deformation error at and above the weld (ring drag + foreign
  weight field); estate distributes it. Measured in PASS3.
- **Shading seams:** theirs is managed twice (geometry seating by
  eye + texture/mask work); estate's is a non-event for fleet
  girls and an unhandled case for foreign textured donors.
- **Scale drift:** estate *is* scale drift, deliberately: the head
  is resized to the body (identity cost). Theirs preserves donor
  proportions exactly and pays at the ring instead. **On this
  failure class, theirs wins, plainly** — for a graft whose whole
  point is *that specific head*, their correspondence is the
  honest one and the estate's is a quiet identity change.

## Adopt / Adapt / Reject

- **Adopt (into the skill, as proposals — PASS4):** the stray-bone
  sweep after any armature fusion (C-10); the UV-name precondition
  before any object join (C-04); the pose-check crease hunt as a
  named step in the fix pass (C-08's loop, estate-gated).
- **Adapt:** their correspondence — for foreign donors whose
  proportions must survive, snap-to-active ring correspondence is
  the estate-shaped alternative to global scaling; Pass 3 prices
  it (weld strain) so the choice can be made per graft.
- **Reject:** hand-painting seam weights by eye as a *primary*
  mechanism where a template field exists (non-reproducible,
  unmeasurable); texture-recolour as a seam strategy for fleet
  work (the fleet's single-palette construction removes the
  problem instead of solving it per graft).
