# Plan 36 — Pass 4 Application and Gate

Application target (plan): the registration approach
rebuilt on one estate prop with drift measured, plus the
control-surface comparison written. Executed in Pass 3 on
a copy of Prima's conformed rig: a Mala-class articulated
prop (21 animator channels) registered to the chest bone
and measured across a 2 s segment of the estate prima-arc
clip in both estate forms.

## Gate (per plan: PASS = drift measured AND the
control-surface comparison written. The subject of the
source asset does not transfer; the mechanics do.)

- Drift measured: **YES** — per-frame (n=121) at the
  register point, both forms, from `build_record.json`:
  constraint (Child Of) form **max 0.0002 mm / mean
  0.0001 mm**; shipped keyed form (15-frame density,
  LINEAR) **max 0.0073 mm / mean 0.0031 mm**; internal
  parenting **≤0.0001 mm**. Determinism pair identical.
- Control-surface comparison written: **YES** —
  TECHNIQUE §1: their prop (5 nodes × 9 transform
  channels = 45; 0 morphs / 0 pose controls / 0 bones;
  13 named material presets + 1 animated preset + ≥9
  surface groups) vs the estate worn prop of record,
  Sloane's Mala (**0 animator channels** — a build-time
  spec boolean + palette entry, baked into the Outfit
  mesh; census-measured from the fleet files), with the
  rebuild prop (21 channels) placed between them as the
  proposed estate form.

**Gate: PASS** (agent-scoped; the Owner's eye items are
queued below — this is never an Owner PASS).

## What the study actually found (one paragraph)

The tutorial's registration content is **parenting**:
loose parts are thrown into the scene and parented to the
prop root, once, before anything is animated — and there
is no character in the video at all, so prop-to-body
registration exists only as the estate translation this
run built and measured. That translation holds at the
Plan 01/15 classes (constraint ≈ exact; keyed = a
motion-dependent sub-mm band, 0.007–0.39 mm across the
two programmes' measured cases). The second finding is
the control-surface asymmetry: the DAZ prop is
library-first (presets carry look and motion; in-scene
controls are raw transforms), while the estate's worn
props are not assets at all — zero channels, baked at
character-build time.

## NSFW application (Torogao device / worn props)

- **Device and worn props become prop assets**, on the
  rebuild's pattern: a prop root + a small bone chain
  (segments for bend/length), parts parented under the
  root (R-36-1), registered to the target body bone by
  Child Of and shipped as 15-frame-density keys in the
  clip (measured cost at this motion class: ≤0.0073 mm —
  three orders below visible).
- **Registration order is assemble → register → animate**
  (TECHNIQUE §2c): the prop is fitted to the finished
  body pose, terminal in the posing order (Plan 34's T10
  applied to props), and never re-registered after keys
  exist.
- **Floating device props** (the source asset's own class)
  take H-36-1: visible working mechanism (spin) + an
  authored root bob on the phase table (rise/fall
  ≈20 frames at 30 fps, drift, a few degrees of tilt) —
  no solver, per the authored-curves-only rule (Plan 15).

## SFW translation

Identical mechanisms, lane-neutral: any articulated prop
in an SFW scene — a held tool, a worn satchel or strand,
a hovering companion drone — takes the same three rules:
parts parented to one root; the root registered to its
carrier (body bone, hand, or world) in the constraint
form and shipped keyed; look and idle motion carried by
named presets in a library rather than by ad-hoc per-shot
settings. The hover recipe (H-36-1) is the SFW floating
prop's default presentation exactly as written.

## Proposals (enter estate practice as PROPOSALS only —
nothing here is adopted by this run)

1. **Prop-asset minimum surface:** an estate prop ships
   with (a) a root + articulated chain where it bends,
   (b) ≥1 named material preset set driven from the
   character palette, (c) where it idles, an animated
   preset or a phase-table entry — the library-first
   surface that made a transforms-only DAZ prop usable.
2. **Worn-prop registration standard:** Child Of to the
   named body bone with a world-anchored register point
   (bone-space constants do not survive mixamorig axis
   conventions — Pass 3 §5), shipped keyed at clip
   density; drift budget: ≤0.05 mm at the register point
   for chest/worn props at ordinary motion (this run
   measured 0.0073 mm; Plan 01's 0.393 mm contact case
   stays the bound for solved pelvis channels, a
   different construction).
3. **Clean-load gate for props:** an estate prop must
   load in a fresh library with zero missing-file errors
   (the source asset fails this twice in its own
   tutorial, C-10).
4. **Mala retrofit (named, not scoped here):** Sloane's
   Mala is the first retrofit candidate — from baked
   outfit geometry (0 channels) to the rebuild's prop
   form (21 channels) — so it can be posed, lengthened,
   and registered to a hand. The rebuild in this run IS
   the prototype, on Prima's rig as host.

## Eye items (for the Owner)

1. `rebuild/formA_mid.png` — the Mala-class strand on
   Prima at the arc window's midpoint: does it read as
   *worn* (hanging on the garment, pendant at the hem),
   or as pasted on? (Agent read: worn; the upper beads
   pass behind the garment's collar line, which is the
   one ambiguous span.)
2. `rebuild/formA_start.png` vs `formA_end.png` — the
   strand's register across the window: any visible
   slide against the garment would contradict the
   measured ≤0.0002 mm; the agent read is none.
3. `rebuild/prop-only.png` — the prop alone (12 beads +
   pendant, forward bow): is this bead scale / strand
   length the right class for a Mala, or should the
   estate prop carry more, smaller beads?
4. Source-video frame `frames/native/t-212.jpg` — the
   DAZ timeline mid-bob (root X −5.00° / Z 8.50°): the
   hover envelope H-36-1 proposes adopting; the Owner's
   eye is the gate on whether that tilt amplitude reads
   as "alive" or as "loose" for Torogao's floating props.

## Numbers behind the verdict (one line each)

- Capture: target serves 200 on both egresses
  (control-proven); file 67,884,878 B, sha256 `72b62b81…`,
  duration 265.833 s = plan's 4:26 verified; decode rc=0.
- Their control surface: 45 transform channels, 0/0/0
  morphs/pose-controls/bones, 13 material presets,
  1 animated preset, ≥9 surface groups (82 stills).
- Estate Mala: 0 channels (census of the fleet files:
  14 objects, no prop object; spec boolean + palette only).
- Rebuild drift: A 0.0002/0.0001 mm; B 0.0073/0.0031 mm;
  internal ≤0.0001 mm; n=121; determinism pair identical
  (measurements + decoded-pixel hashes).
