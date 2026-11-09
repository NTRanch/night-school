# Plan 22 — Pass 4 Application & Gate

## Application target

The plan names outfit fitting across the model fleet
(factory fitting, Torogao/Strobe wardrobe work). The rebuild
applied the preset to the Torogao fleet's Prima rig over a
posed elbow at three angles (PASS3-REBUILD.md). That IS the
plan's application case — a wardrobe sleeve over a bent
joint — run on a procedural test article because Prima's
shipped outfit has no extractable sleeve geometry
(probe2 evidence).

## Application record — the preset as a fleet candidate

**`NS22-RESPONSIVE-SLEEVE-FIT`** (TECHNIQUE.md) is recorded
as a fleet wardrobe-fitting candidate with this measured
envelope on Prima (Blender 5.2.3, right elbow):

- **Straight/rest pose: clean.** Gap +1.9…+4.0 mm, zero
  interpenetration, slide 0.
- **Bent joint: NOT clean as-is.** Interpenetration in the
  inner-elbow band (30–43 mm from the joint) at 70°
  (15/180 verts, worst −8.0 mm) and 120° (39/180 verts,
  worst −4.5 mm); gap mean/max, pinch ratio and slide stay
  in bounds at all angles.
- **Verdict for fleet use:** adopt the architecture
  (projected collider + surface-deformed shell + inward
  solidify) for straight and gently-posed wardrobe fits;
  do NOT ship it for bent-joint sleeves until an
  inner-elbow ease is added and re-gated at the same three
  angles. The ease is a named follow-on, not part of this
  run (the gate forbids hand repair mid-test).

## SFW translation

**Identical.** Clothing fit is rating-blind: the same
preset, the same measured envelope, and the same bent-joint
caveat apply unchanged to SFW character work. (The source
video's subject matter is adult; the distilled mechanism
contains nothing adult — the crossing is the technique, and
it is named here per protocol.)

## Gate (plan, verbatim intent)

"PASS = clean fit at all three angles with no hand repair."

**FAIL.** Clean at rest; interpenetration at 70° and 120°
with the preset running as-is (numbers in
PASS3-REBUILD.md). No hand repair was applied at any angle.

## Eye items (queued for the Owner's eye — not self-verdicted)

Fit quality at the bend is partly an eye read. The three
angle frames from the final artifact are in
`rebuild/angle_rest.png`, `rebuild/angle_flex70.png`,
`rebuild/angle_flex120.png` (also copied to
`repo/results/plan-22-shrinkwrap-sleeve/`):

1. **angle_rest** — SHOULD: a smooth cuff hugging the elbow
   region, no visible gap or dent. SEEN (agent pre-read):
   smooth cuff, hugs the arm; reads clean.
2. **angle_flex70** — SHOULD: cuff bends with the arm, mild
   inner crease acceptable, no spikes. SEEN: bends with the
   arm; faceted creasing at the inner bend and a lifted rim
   flap near the torso — consistent with the 15-vert
   penetration the numbers record.
3. **angle_flex120** — SHOULD: cuff survives deep flexion
   without folding through itself. SEEN: a spiky fold
   protrudes at the inner elbow — the visual signature of
   the FAIL; queued as the FAIL exemplar beside item 1's
   clean rest frame.

The eye items can demote, never promote: the numeric FAIL
stands regardless of the eye verdict.

## Disposition (2026-11-08, per D-1088 repair) — studied-not-adopted, CLOSED

The NS22-RESPONSIVE-SLEEVE-FIT preset is closed as a fleet
wardrobe-fitting candidate: NOT adopted. Grounds are this
record's own gate: the plan is complete-with-FAIL-leg —
shrinkwrap interpenetration at bent angles (70°: 15 verts
inside; 120°: 39 inside) — and the named follow-on (inner-
elbow ease) was never run. A gate-failed preset is not
admissible for adoption; reviving it requires a new
commission that runs the ease follow-on and re-gates.
(Plan 38 §5 records the structural reason: a LIVE modifier
stack re-conforms every frame, unlike a bake.)
