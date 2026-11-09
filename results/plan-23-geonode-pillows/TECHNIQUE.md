# TECHNIQUE — Plan 23 distilled: proximity-squish cushion ("kissen")

Distilled by Pax from OBSERVATION.md (Pass 1, this run).
Parameters are the video's, verbatim where read; anything the
video leaves open is marked OPEN. The plan asked for a pillow
*construction*; the video teaches a pillow *behaviour*. This
sheet specifies the behaviour — it is the rebuild contract for
Pass 3.

## The mechanism (why it works)

A static mesh cannot dent. This setup fakes softness with a
**distance field**: every vertex of the cushion asks "how far
am I from the sitter?" (Geometry Proximity to the character's
faces), and a two-stage curve turns that distance into a
**vertical lift**. The lift is smallest at the contact patch
and grows with distance, so the surface *around* the contact
rises while the contact stays low — the eye reads the relative
depression as a dent and the general lift as plumping. Nothing
is simulated, nothing is ever pushed below rest position, and
the effect follows the collider's evaluated geometry live
(a posed armature deforms the cushion in real time).

## The node group SPEC (as built on screen, final form)

Group name on screen: **`kissen`**. Nodes in wiring order:

| # | Node | Settings (final, as read) | Wiring |
|---|------|---------------------------|--------|
| 1 | Group Input | Geometry (+ Selection) only — U-5 | Geometry → Set Position.Geometry; Selection → Set Position.Selection |
| 2 | Set Position | Position unwired; Offset from chain | → Group Output |
| 3 | Object Info | Object = the character mesh ("Gummigoo…", U-1); **Relative** mode | Geometry → Proximity.Geometry |
| 4 | Geometry Proximity | Target element **Faces** | Distance → Map Range.Value (Position, Is Valid unused) |
| 5 | Map Range | Float · Linear · **Clamp ON** · From Min **−2.100** · From Max **1.000** · To Min **0.500** · To Max **0.900** | Result → Color Ramp.Fac |
| 6 | Color Ramp | RGB · Linear · stop 0: **black @ 0.714** · stop 1: **white @ 0.982** (U-4) | Color → Combine XYZ.Z |
| 7 | Combine XYZ | X **0.000** · Y **0.000** | Vector → Set Position.Offset |

Build history visible on screen (the iteration is part of the
evidence): Map Range Result first fed Offset directly
(all-axes, f_0073), then via Color Ramp (still all-axes,
f_0085, ramp polarity white→black), then Combine XYZ restricted
it to Z (f_0107) and the ramp polarity settled black→white with
From Min tuned 0 → −1.600 → −2.100.

### Derived transfer function (from the values above)

Fac(d) = 0.500 + 0.400 × clamp((d + 2.100)/3.100), d in metres.
Lift(d) = ramp(Fac(d)). The ramp's black plateau (Fac ≤ 0.714)
would need d ≤ −0.44 m — unreachable, since d ≥ 0. So the
plateau is never actually used: Fac starts at 0.771 when
d = 0, giving lift ≈ 0.21 at contact, ≈ 0.45 at d = 0.5 m,
saturating at ≈ 0.69 from d = 1.0 m (the clamp). **Relative
dent ≈ 0.48 m at full separation** — claim C-3, measured in
Pass 3 against the rebuilt distance field.

### Base-shape contract

- Closed box mesh; density ~**16 segments per edge** (1,536
  faces measured on Demo A's cushion, f_0085). The dent is
  only as smooth as the mesh: segment pitch must be well
  under the dent's radius.
- One GN modifier carrying the group; no other modifier is
  proven on the pillow (U-2). Shade behaviour OPEN.
- The collider is any evaluated mesh (the video uses a posed
  character). Proximity is to its **faces** in the cushion's
  local frame (Object Info Relative).
- Scale is in metres and the tuning is scale-bound: the From
  window (−2.1…1.0 m) is fitted to a ~0.5 m cushion and a
  human-scale sitter. Rescaling the scene without rescaling
  the window silently retunes the effect (sweep axis G/B).

## Failure modes (named by the screen, not the narration)

- All-axes offset (the intermediate forms) displaces the
  cushion sideways/up uniformly — replaced on screen by the
  Z-only Combine XYZ form.
- Ramp polarity flips during tuning: with the wrong polarity
  the contact *rises most* — an anti-dent. The creator caught
  and corrected this by eye; no warning is stated.
- The lift gradient across the cushion's own thickness
  (bottom verts are farther from the collider → lift more)
  thins the cushion from below; steepen the From window and
  the bottom crosses the top — predicted inversion cliff,
  tested in the sweep (Pass 3).

## Plausibility question for the sweep (Pass 3)

Where are the cliffs? Predictions, from the mechanism:

- **P-1 (From-window cliff).** Compressing (From Max − From
  Min) steepens the lift gradient; at some width the
  through-thickness differential exceeds the thickness →
  inversion (bottom verts above top verts).
- **P-2 (Fac-window cliff).** To Min/To Max placed wholly
  above the ramp's white point → uniform maximum lift, dent
  gone (form reads as a floating slab, not a break). Wholly
  below the black knee → no lift at all (dead box).
- **P-3 (Ramp cliff).** Stop 0 at/after stop 1 → degenerate
  curve; lift becomes a step or constant.
- **P-4 (Press cliff).** Collider pressed fully through the
  cushion → contact distances ≈ 0 over the whole top → the
  dent swallows the surface (uniform contact lift, plump
  gone). Collider hovering (no contact) → dent detaches from
  the sitter and reads as a floating dimple.
- **P-5 (Density cliff).** Segments/edge too low → the dent
  aliases into spikes/facets; vertex count is the tell.
- **P-6 (No cliff expected).** From Min more negative / From
  Max larger (wider window) only flattens the gradient —
  graceful degradation toward "no visible effect", not a
  break.

## Adopt / Adapt / Reject

- **Adopt** — the mechanism entire: proximity-distance → curve
  → Z-only Set Position lift, relative-dent construction.
  Deterministic, stateless, real-time, DCC-native; it fits
  the estate's deterministic doctrine exactly (no bake, no
  solver state).
- **Adapt** — the estate asset exposes as group inputs what
  the video hard-codes: the **Collider object** (the video's
  Object Info is bound to one scene object — not reusable as
  shipped) and the **Map Range window** (From Min/Max, To
  Min/Max) as named float inputs with the video's values as
  defaults. The Color Ramp stays internal (ramp stops are not
  socket-drivable) and is documented as part of the spec.
  Group name for the estate asset: **`PillowSquish`** (the
  video's `kissen` recorded here as provenance).
- **Reject** — nothing in the technique. Rejected instead is
  the *plan's* framing (construction/seam/falloff): recorded
  as a plan erratum, local copy only.
