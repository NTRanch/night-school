# Plan 09 — Pass 2 Technique Sheet

- **Distilled from:** `OBSERVATION.md` (final merged record: frame record
  + speech record; claims C-01…C-17).
- **Counts: Adopt 7 · Adapt 7 · Reject 2**, of 16 entries covering claims
  C-01…C-17 (C-13/C-14 provenance-only, dispositioned at the foot).
- **Route in one line:** a hand-authored Bézier curve fused into a smooth
  strand mesh by a two-knob Geometry Nodes group (Curve to Points → Points
  to Volume → Volume to Mesh), finished with shade-smooth, a set material,
  and a Smooth modifier. No solver, no bake, no cache.

## Binding findings (carry into every entry; do not soften)

1. **This route and Plan 07's route solve different problems.** Plan 07
   (Mantaflow FLIP) simulates: you state physics and get whatever motion
   comes out, at bake cost, with C-02 separation REFUTED in-route. Plan 09
   poses: you state the exact strand path and get exactly that shape, at
   zero bake cost, with no motion at all until an artist (or a driver)
   moves the curve. Any A/B that scores them on one axis only is rigged;
   Pass 4 scores them per shot class.
2. **The fusion is a volume union, and that is the whole trick.** Points
   along the curve become overlapping VDB spheres; Volume to Mesh at
   Threshold 0.100 extracts one continuous surface. Where strands cross,
   touch a body, or end, they *merge* like liquid because the union has no
   seams — the visual property (clinging, bridging, spreading feet) that
   the estate otherwise chases with solver viscosity and surface tension
   is here a geometric identity, free and exact.
3. **Sampling density is the quality knob the tutorial discovers live.**
   Count 10 / Radius 0.5 m = blob; Radius 0.25 m = lumps; the final form
   samples every 0.001 m so continuity never depends on radius. The estate
   preset takes the final form only; the failure states are kept as the
   sensitivity exhibits in Pass 3 (v1/v2).
4. **Nothing in this route collides, falls, or flows.** Every apparent
   physical behaviour in the finished frames — drape, drip, spread — was
   placed by the artist's hand on the curve. Transferred to the estate,
   the route inherits Plan 06's problem (paths must be authored against
   the bodies) and Plan 06's answer (anchor-to-anchor paths, GAP 2
   contact checklist), and it must never be sold as simulation.

## Entries

**T-01 — ADOPT. The strand-builder chain itself** (C-01). Curve to Points →
Points to Volume (Density 1.000) → Volume to Mesh (Threshold 0.100,
Adaptivity 0.000) → Set Shade Smooth (Face) → Set Material. Mechanism:
millimetre-spaced points give the VDB union a continuous spine; the
threshold sets strand girth against the radius. This becomes the estate's
*posed-strand* construction, sibling to Plan 07's preset, under the name
`strand` in the Pass 4 preset file.

**T-02 — ADAPT. Sample by length, never by count** (C-02, C-03, C-04).
The tutorial's own iteration refutes Count mode for strands of unknown
length: a fixed point count starves long curves into lumps. Estate form:
Length mode at 0.001 m is the preset default; Count mode is kept only as
the Pass 3 sensitivity exhibit. Adaptation note: 0.001 m spacing on long
paths is heavy (a 4 m path = 4,000 points); the preset exposes spacing
through the Resolution knob's voxel size, not by relaxing the length rule.

**T-03 — ADOPT. Two artist knobs: Radius and Resolution** (C-05, C-08).
The group hides the whole chain behind Radius (strand girth, fed to
Points to Volume) and Resolution (voxel size = Radius ÷ Resolution via a
Divide node; operand order spoken explicitly and wiring-verified). Every
other value is a locked constant of the group. This is the same preset
philosophy as Plan 07's JSON (few knobs, named), and the two files should
be readable side by side.

**T-04 — ADAPT. Radius is a per-shot-class value** (C-06). Screen record:
0.100 for drape over Ø 2 m proxy spheres; 0.025 for detail strands on a
full character — a 4× range across shot classes at the same Resolution
2.000. Estate form: the preset ships both as named classes (`drape`,
`detail`), expressed in metres at character scale and flagged for
re-measurement against a Torogao girl's proportions in Pass 4's
application, because the tutorial's character is Daz-proportioned, not
fleet-proportioned.

**T-05 — ADOPT. Finish the stack with a Smooth modifier** (C-07). GN
modifier first, then Smooth (Factor 1.500, Repeat 20, XYZ): the volume
mesh's residual faceting is ironed *after* meshing, in the modifier stack,
non-destructively. Cheap, deterministic, and it keeps the group itself
minimal.

**T-06 — ADOPT. One group, many curves, organised in a curves collection**
(C-08). The character stage runs BézierCurve and BézierCurve.001 through
the same group with different Radius inputs. Estate form: strand curves
for a shot live in one collection, share the group, and differ only in
path + Radius class — the file organisation the D-1 fluid layer can
consume directly.

**T-07 — ADOPT the practice. Debug-contrast materials while shaping**
(C-09). M_ShowerGel's first form (green, Roughness 0.500) is a *working*
material: maximum contrast against the red proxy bodies so shape errors
are visible. The practice transfers verbatim (the estate's own builds
already use debug colours; this names and normalises it). The final
recipe is a separate entry (T-15) — the merged record recovered it, so
nothing about the material remains a matter of taste-by-default.

**T-15 — ADAPT. The final material structure** (C-09b). White base,
Roughness 0.000, **Transmission Weight 1.000**, a **Principled Volume
(Density 30)** in the volume socket, and **Alpha driven by Light Path
Ray Length** so thin parts read clearer than thick ones. Structure
transfers; values do not transfer blindly: Transmission 1.0 + volume
density is a Cycles-class look whose cost and behaviour in the estate's
 Eevee/Workbench gates differ, the Ray-Length→Alpha transfer curve is
UNREADABLE, and the estate's own fluid-material direction (Plan 02
template lane) stays of record. Estate form: rebuild this structure in
the Pass 3 file for reference, gate the *look* by Owner eye, and keep
the geometry preset material-agnostic (Set Material takes the shot's
material as data).

**T-16 — ADAPT. Guard the zero-input state** (C-17). In the tutorial's
group the float sockets default to 0, which collapses voxel size to 0
and errors the mesh node until real values are typed. Estate form: the
shipped group defaults Radius 0.100 / Resolution 2.000 (the tutorial's
own working values) so a fresh modifier instance renders a sane strand
before any tuning — a tool that errors on first attach will not be
reused, which defeats the group's entire point (T-03).

**T-08 — ADAPT. Drips are authored branches of the path** (C-10, C-16).
The tutorial grows drips by extruding curve points downward (E ×5), and
the paths themselves are drawn onto the body with the Draw tool at
Depth = Surface — projection is a tool setting, so a path can be
authored *on* a posed body in seconds. Estate
form: a drip is a path segment authored from the strand's low point —
in the D-1 pipeline these paths come from the scene's anchor pairs
(Plan 06's anchor-to-anchor record) and lumen's path authoring, not from
manual extrusion; the geometry lesson (a drip is the same curve, fused by
the same union) is what transfers.

**T-09 — ADOPT. Bridging strands between two bodies** (C-11). A single
curve spanning the gap fuses to both bodies through the volume union —
no emitter, no collision solve, no travel time. For the estate's
two-body contact shots this is the cheapest correct-looking construction
that exists in either route, and it is exact where Plan 07's solver
route is weakest (its C-02 separation failure and its one-way travel,
Plan 06 Finding 1).

**T-10 — ADAPT. HDRI look-check discipline** (C-12). Look judgements in
the tutorial are made under a Poly Haven studio HDRI
(`studio_small_04_1k.hdr`) in rendered preview, not under flat workbench
light. Estate form: strand look gates use a fixed studio HDRI + rendered
preview *in addition to* the pixel-hash determinism lane (which stays
Workbench); the HDRI file itself is a look-check tool, never shipped.

**T-11 — REJECT (as taught) / the gap is named. Motion** (absence 2).
The tutorial teaches no animation: no keyframes, no growth, no playback.
As a complete route for animated shots the teaching is rejected — not
because the route cannot move, but because the video does not show it
moving. The estate adaptation is commissioned in Pass 3 as a probe
(curve-path growth states re-evaluated per frame, no bake) and is
recorded there as ESTATE work, fenced from the video's claims.

**T-12 — REJECT. Any reading of this route as simulation** (absences 1,
3, 4). If a future brief cites Plan 09 for viscosity behaviour, droplet
separation, pooling dynamics, or collision response, that citation is
wrong: none of those exist in this route. The sheet records the rejection
so the A/B in Pass 4 cannot be misread later.

**T-13 — ADOPT. The input → function → output teaching frame** (C-15).
The whiteboard segment teaches node thinking as function composition
before any Blender work, and the creator returns to it all video ("a
glorified function", "a reusable tool"). Adopted as the explanation
frame for the estate's own GN tooling documentation: a group is a
function; its sockets are the signature; the modifier panel is the call
site. (For this estate's beginner-facing material especially, this is
the order to teach in: function first, nodes second.)

**T-14 — ADAPT. Teach in the open: failure states first** (C-02, C-03).
The tutorial shows the blob and the lumps before the good strand, and
the parameter story is only legible because it does. Estate form: the
Pass 4 preset ships with its sensitivity exhibits (Pass 3 v1/v2 renders)
referenced, following the estate's FAIL-exemplar rule for verdict packs.

## Provenance notes (not techniques)

- C-13 (proxy scale, grid-read Ø 2 m) and C-14 (lineage: FrostBound3D per
  the watch page; DivinityStudio as producing studio) are evidence for
  the observation record; they dispose no technique and are not counted.
- The tutorial's Blender is 5.0.1; the estate pin is 5.2.3 LTS. No node
  in the chain changed semantics between them that this sheet relies on;
  Pass 3 verifies by construction.
