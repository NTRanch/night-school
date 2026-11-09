# Plan 36 — Pass 2: Technique distillation

Source: OBSERVATION.md (screen-governed; transcript
UNCONFIRMED tier). Clean-room: mechanisms only — no source
asset, mesh, texture, or preset is reproduced; the estate
rebuild (Pass 3, `rebuild/`) was built from this sheet
alone. The subject of the source asset does not transfer;
the mechanics do (plan's own instruction).

## 1. PROP CONTROL DESIGN — what the asset exposes, vs
what an estate prop exposes

### 1a. Their asset (DAZ drone prop), inventoried in Pass 1

The control surface is **library-first, transforms-only**:

- **Nodes:** 1 root + 4 child nodes (the rotor fans as
  separate parented nodes). Per node the animator gets
  exactly the DAZ transform block — Translation / Rotation
  / Scale, XYZ each = **9 channels × 5 nodes = 45**.
- **Morphs: 0. Pose controls: 0. Bones: 0.** The creator's
  own on-screen PowerPose check returns DAZ's empty state
  ("Where Are The Controls?") — a prop is not a figure and
  carries no figure control layer.
- **Materials as controls:** ≥9 Iray surface groups on the
  single root geometry, driven not by sliders in the
  workflow but by **13 named material presets** (4
  whole-asset, 7 device body/tip, 2 fan protector) plus a
  fan-blade preset folder — colour/look is a *library
  choice*, not a dial.
- **Motion as a preset:** 1 animated pose preset
  (fanbladeposeone) that spins the fans; whole-prop motion
  beyond that is hand-keyed on the root (the 61-frame bob).
- **Variants as files:** 2 scene files in the main folder
  (full + "simple"), a whole second asset folder unopened.

Design read: the asset's author put the animator-facing
surface in **the library** (presets for look, spin, and
variants) and left the in-scene surface at raw transforms.
An animator never touches a custom control because none
exists; they compose presets and key the root.

### 1b. The estate prop (Sloane's Mala), inventoried the
same way

Instrument: the same census script as the rebuild
(`rebuild/census.py`, Blender 5.2.3 headless) run over the
fleet files of record — `sloane.blend` (SHA-256
`b86e5e8f…`, staged copy) and her spec
(`torogao-models-20261104/build/sloane_spec.json`).

- The Mala is **not an object**. Sloane's fleet file has
  14 objects (1 armature, Body/Hair/Outfit/OutfitEnd
  meshes, 2 cages, 7 fluid anchors) and **no prop object,
  no prop armature, no beads, no pendant** anywhere in it.
- Its entire existence in the shipped artifact is:
  (i) a **build-time boolean** in the character spec —
  `"mala": true` in both garment records; (ii) a
  **palette entry** — `"Mala": [0.3, 0.19, 0.1]` — used
  when the builder bakes the strand into the Outfit
  geometry; (iii) whatever skinning the Outfit mesh
  carries (the Outfit mesh has 2 shape keys total,
  Basis + 1, neither Mala-specific).
- **Animator-facing controls: 0.** No node to select, no
  channel to key, no preset to apply. The Mala moves
  because the body moves; it cannot be posed, lengthened,
  re-strung, hidden per-shot, or registered to a hand —
  any of those is a rebuild of the character, not an
  animation act.

The estate CHARACTER surface is rich by contrast (the same
census: 54 bones, 38 shape keys on the Body mesh — 37
`Fac_*` + Basis — 46 shape keys across the file), which is
exactly the asymmetry: **the estate spends its whole
control budget on the character and gives props none;
the DAZ asset spends nothing on a character (there is
none) and gives the prop a library.**

### 1c. Side-by-side (the comparison is the deliverable)

| Class | DAZ drone prop | Estate Mala (worn prop) |
|---|---|---|
| Selectable nodes | 5 (root + 4 parts) | 0 (baked into Outfit mesh) |
| Transform channels | 45 (9 × 5 nodes) | 0 |
| Bones in prop | 0 | 0 |
| Morphs / pose controls | 0 / 0 | 0 / 0 |
| Look controls | 13 named material presets + ≥9 surface groups | 1 palette entry, build-time |
| Motion controls | 1 animated preset (fan spin) + root keying | none (rides body skinning) |
| Variants | 2+ scene files | spec boolean (rebuild to change) |
| Registration | parts parented to root (§2) | none — geometry is welded at build time |

**Answer to the plan's question:** our prop format exposes
*fewer* controls — in the worn-prop case, none at all. The
gap is not DAZ-vs-Blender; it is **prop-as-asset vs
prop-as-baked-geometry**. The estate's characters prove it
can build rich control surfaces when the thing is a
character; its props are not yet assets.

- **Adopt:** the library-first surface for props —
  a prop ships with named material presets and (where it
  moves) an animated preset, because that is what made a
  transforms-only prop feel controllable in the tutorial.
- **Adapt:** the estate form of "node with transforms" is
  a small prop armature (root + segment bones) whose bones
  ARE the control surface (Pass 3 builds one: 21 animator
  channels — root transforms 9 + 4 bones × rotation 3 —
  between the DAZ prop's 45 and the Mala's 0, and every
  channel keyable in a clip).
- **Reject:** variants-as-separate-scene-files (their
  dildodroneone / dildodronesimplev split). Estate form is
  one prop asset with a spec switch, per the fleet's own
  spec-driven builds — two files for one prop is drift
  waiting to happen. Also rejected: shipping an asset with
  broken file references (their load/preset dialogs,
  C-10) — an estate prop's gate includes a clean-load
  check in a fresh library, which their asset would fail.

## 2. REGISTRATION DISCIPLINE — prop-to-body, stated
against the Plan 01/15 body-to-body discipline

### 2a. What the video's method actually is

One act: **loose parts are parented to the prop root**
(C-02), done once, before any animation (C-12). There is
no body in the video, so the video demonstrates
**prop-internal registration only**. Stated as a rule:

> **R-36-1 (parent the parts to the root, once, first).**
> An articulated prop is assembled by parenting every
> part node under one root node; after that act the
> assembly is a single transformable unit and is never
> re-registered. Placement and animation address the
> root only.

### 2b. Same classes as Plan 01/15, or different?

Plan 01/15's body-to-body discipline has three elements:
(1) a **constraint form** (Child Of with a verified set
inverse — Δ 0.000008 mm class — whose live drift is
≤0.0001 mm), (2) a **shipped keyed form** (the lock
re-expressed as solved keys; drift = interpolation
residual, max 0.393 mm on the contact set), and (3)
**authored curves only** above the lock (Plan 15's bob:
no simulation anywhere).

Prop-to-body under R-36-1 compares as follows:

- **Same class as (1), weaker instrument.** DAZ parenting
  *is* the constraint form's plain parent case: a child
  node's world transform is its parent's transform
  composed with its local offset, so a correctly parented
  part has **zero drift by construction** — the same
  guarantee Child Of gives, without an inverse to verify.
  The estate translation is literal parenting (part →
  prop root) inside the prop, and — for the step the
  video does not show — Child Of / bone parenting of the
  prop root to the body bone, measured in Pass 3 in both
  the constraint form and the keyed form.
- **Same class as (2).** When the estate ships animation
  as clips (torogao-motion-clip/1 carries no constraints,
  Plan 01 §7.2), a registered prop must be baked to keys
  exactly like Plan 01's lock was; the expected error
  class is the keyed class (sub-mm interpolation
  residual), and Pass 3 measures it at the clip format's
  own 15-frame key density.
- **Same class as (3).** The video's hover is authored
  curves only (root keys: bob + drift + tilt, C-07) — no
  solver, no simulation — which is Plan 15's authored-bob
  discipline wearing a prop. The 20-frames-up /
  20-frames-down bob at 30 fps is a phase-table entry,
  directly expressible in the estate's clip grammar.
- **Different in one respect that matters: no contact
  set.** Body-to-body registration is judged at a contact
  interface (interpenetration, gap). A worn/held prop has
  a **register point** instead (where the prop root sits
  on the body), and a floating prop has none at all — its
  "registration" is to the fiction (rotor spin + bob),
  not to a surface. The discipline therefore splits:
  **worn/held props inherit Plan 01/15 wholesale** (lock,
  key, measure at the register point); **floating props
  inherit only the authored-curves rule**, plus the
  presentation devices of §3.

### 2c. Ordering vs Plan 34

Plan 34's T10 (contact is terminal — the prop is moved to
the body LAST) and R-36-1 are the same instinct at
opposite ends: **registration is settled exactly once, at
the end of assembly and before animation** — Plan 34
settles body-then-prop at the end of posing; the video
settles parts-into-prop at the start of the session,
before materials, presets, and keys. Neither re-opens
registration downstream. Estate rule as proposed in
Pass 4: assemble → register → animate, in that order,
for props as for contacts.

## 3. Hover presentation (distilled)

> **H-36-1.** A floating prop reads as supported when
> (i) its lift mechanism is visibly working (here: rotors
> spinning, via an animated preset), and (ii) the root
> carries a small authored bob — rise ≈20 frames, fall
> ≈20 frames at 30 fps, with slight lateral drift and a
> few degrees of tilt (frame-20 read: X −5.0°, Z 8.5°) —
> and for no other reason. No shadow, tether, or camera
> device is required, and none was used (C-08).

- **Adopt:** (i) + (ii) as the estate's floating-prop
  default; the numbers are a sane starting envelope for
  any drone/orb/hover prop at this scale.
- **Adapt:** in clip form the bob belongs on the prop
  root's channels keyed to the scene's phase table (the
  Plan 15 bob pattern), not baked into the body clip.
- **Reject:** nothing in the hover method; the *absence*
  of a grounding shadow is recorded as a property of
  their unlit viewport context, not as a recommendation
  for lit scenes (Pass 4 keeps a contact-shadow option
  open for lit work — proposal only).
