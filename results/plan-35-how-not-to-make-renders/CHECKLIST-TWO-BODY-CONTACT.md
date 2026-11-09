# GATE ARTIFACT — Two-Body Contact / Interpenetration Checklist (STILLS) (NS35-NC series)

- **Commission:** D-1071 (2026-11-06). **Status: LANDED** for
  the Night School programme's own use and the estate's
  candidate shelf. Adoption into skills/doctrine is a later
  gated step.
- **Closes:** Plan 35 PASS4 GAP 2 — "no checklist artifact
  gates body-body interpenetration or contact plausibility
  for stills" (`runs/plan-35/PASS4-APPLICATION.md` sha256
  `cadf0029…`).
- **What this gate is:** a **stills** gate. Each check is
  answerable from a single frame (plus the crops it names)
  **without the 3D scene**. Where the truth lives only in the
  scene (measured penetration depth), this checklist says so
  and defers to the measurement gate — it never claims a
  millimetre read from pixels.
- **Measured anchors (the severity scale is built from these,
  not from imagination):**
  - **Subsurface tolerance class:** post-cure residual
    penetration ≤ **5.4582 mm** is the estate's known-good
    class — D-1 demonstrator, 7 castings, post-cure maxima
    1.4420–5.4582 mm (`runs/d1-demonstrator/records/
    gate-table.json` sha256 `2c13a1d0…`). In stills this class
    is **invisible** (this commission's exercise: 0 FAIL
    signatures in 7/7 castings; Plan 01 benchmark item 4
    concurs). It is NOTE-grade at most, never a stills FAIL.
  - **Cure class:** the T-13 `ContactFix` sculpt-key cure
    (scene-side key, value 1.0, never Basis; 3–11 verts,
    max delta 2.734–8.000 mm per casting) is what brings raw
    contact into the tolerance class. Pre-cure maxima in D-1:
    1.7343–14.9120 mm.
  - **Visible class:** Plan 01's first-attempt pose geometry —
    **66 mm** penetration at every sample (leader's raised
    knees through the follower's torso), refuted by the
    measurement gate before any evidence frame was rendered
    (`runs/plan-01/PASS3-REBUILD.md` §7.2, sha256 `7c70b91c…`).
    66 mm = **12.1× the tolerance class**; penetration of
    this order is grossly visible in a still. FAIL-grade
    signatures below are calibrated to this side of the line.
  - **Drift classes:** Child Of lock drift 0.0001 mm max
    (constraint form) / keyed-form interpolation residual
    ≤ 0.4116 mm max across D-1 — both far below stills
    visibility. A stills-visible gap is therefore never
    "drift-class"; it is a posing/contact failure.
  - **Hand classes:** solved hand contacts — frame-0 solve
    residuals ≤ 0.46 mm; across-loop deviation max 4.94 mm
    (leader hands, interpolation between solve keys; Plan 01
    PASS3 §2/C-15). Hand hover at the low-mm scale is a
    NOTE; intersection/swallow is a FAIL.

## How a verdict pack runs this checklist (GATE note)

1. **Applicability first:** the frame must show (or claim) two
   bodies in contact. Single-body frames: every check is N/A
   (recorded, not passed). If the contact interface is fully
   occluded from the camera, record **INTERFACE NOT VISIBLE**
   per check — the Plan 01/D-1 ¾ evidence camera occludes the
   pelvis interface in every casting; in that case this gate
   gates the *visible* junctions only and the measurement
   gate carries the interface. A stills PASS never overrides
   a measurement FAIL.
2. **Reads:** full frame at viewing size, then a ≥3× crop of
   each visible contact junction. Per check: PASS / NOTE /
   FIRE with the junction named.
3. **What a fire does:** any FAIL-grade FIRE fails the frame
   at this gate. NOTEs accumulate in the gate report; two or
   more NOTEs on the same junction escalate to a re-render /
   measurement referral, not a silent pass.
4. **The Owner's eye is the verdict of record**; this
   checklist structures the read, it does not replace it.

## The checks

### NS35-NC01 — Visible interpenetration — **LANDED**
- **Look at:** each visible contact junction at viewing size,
  then the ≥3× junction crop. FIRE when one body's surface
  boundary visibly passes **into** the partner's filled
  volume — a limb, torso edge, or tail crossing the partner's
  silhouette and continuing inside it, rather than ending at
  its surface.
- **Severity:** FAIL-grade. A boundary that merely overlaps
  in projection and ends at the partner's surface (normal
  occlusion) is PASS — projection overlap is not penetration.
- **Anchor:** visible class (66 mm) FAILs; tolerance class
  (≤5.4582 mm) produced 0 fires in 7/7 D-1 castings.
- **Provenance:** Plan 01 contact record (penetration classes
  + T-13 cure class); D-1 gate-table.

### NS35-NC02 — Surface-intersection line — **LANDED**
- **Look at:** the ≥3× junction crop. FIRE when a hard
  crease/edge line runs **across** a body surface at the
  contact patch — a line that belongs to neither body's
  anatomy or garment construction and reads as the partner's
  surface slicing through.
- **Severity:** FAIL when the line crosses a limb/torso
  surface; NOTE when a short seam sits exactly at an occluded
  interface edge (may be an occlusion boundary, not an
  intersection).
- **Anchor:** no instance in the D-1 post-cure pool (0/7);
  the signature is the stills-visible form of the pre-cure /
  visible penetration classes.
- **Provenance:** Plan 01 penetration-test record (the
  two-axis ray-parity class exists precisely because surfaces
  intersect measurably before they intersect visibly);
  Plan 03 B5 ("no visible interpenetration" as the contact
  behaviour of record).

### NS35-NC03 — Floating-contact gap — **LANDED**
- **Look at:** any junction where the pose claims contact
  (hands planted, bodies pressed, weight borne). FIRE when a
  visible air gap — background or floor sliver, or an
  unshadowed separation line — separates surfaces that the
  pose says are touching, at viewing size or in the 3× crop.
- **Severity:** FAIL-grade. Sub-pixel / low-mm separations
  are below this gate's floor by design (drift classes
  ≤0.4116 mm; Plan 01's measured 3.0 mm frame-0 registration
  gap was not visible in its evidence frames).
- **Provenance:** Plan 01 drift record + benchmark item 1
  ("no air gap at the hip line" as the expected-vs-seen
  line); D-1 drift table.

### NS35-NC04 — Contact-shadow absence — **LANDED (NOTE-grade)**
- **Look at:** the contact patch vs the frame's own lighting:
  where the scene casts shadows elsewhere, a contact junction
  with **no** occlusion darkening at the touching surfaces
  reads as pasted-on / floating.
- **Severity:** NOTE alone (lighting-dependent; cel and flat
  registers may legitimately lack contact shadow — see the
  2D applicability record in `EXERCISE-RECORD.md` §C.4).
  Escalates NC03: gap + no contact shadow on the same
  junction = FAIL by combination.
- **Provenance:** Plan 01/D-1 evidence frames (contact held
  AND platform contact shadows present in 7/7 castings —
  the positive form); estate lighting classes (Plan 35 L-1/L-2
  adjacency).

### NS35-NC05 — Occlusion-order inconsistency — **LANDED**
- **Look at:** any single limb / appendage / body part that
  meets the partner at two or more points along its length.
  FIRE when the part is in **front** of the partner at one
  junction and **behind** at another, with no wrap geometry
  (a visible pass around the body) explaining the change.
- **Severity:** FAIL-grade.
- **Exercise note:** the positive instance of record is
  external — Plan 35's g27 finished render (screen-captured
  WIP scene; observer read per OBSERVATION §4.3: the tail
  crosses in front at the waist, disappears into the body
  mass, and its limb reads behind the leg) — `EXERCISE-
  RECORD.md` §C.3. No D-1 instance (0/7).
- **Provenance:** Plan 35 OBSERVATION §4.3 observer read
  (explicitly an observer read of an unfinished scene, not a
  video claim); face-plausibility gate's layer-order item
  (§2.2) generalised from faces to bodies.

### NS35-NC06 — Contact-deformation absence (hard-shell read) — **PRUNED**
- **Candidate form:** FIRE when pressed masses show zero
  surface flattening / soft-tissue response at the junction.
- **Prune evidence:** the candidate fires on **7/7 known-good
  D-1 castings** — the estate's conformed bodies are rigid
  low-poly meshes in bodies-only evidence renders; no casting,
  good or bad, shows soft deformation at the stills scale.
  The check measures the register, not the contact. PRUNED
  with evidence (`EXERCISE-RECORD.md` §C.5); not landed in
  any severity form.

### NS35-NC07 — Hand-contact integrity — **LANDED**
- **Look at:** every hand at a contact point, in the ≥3×
  crop. FIRE when fingers visibly intersect the surface they
  grip, the hand is swallowed into the partner's mass, or
  finger order/geometry breaks at the grip. NOTE when the
  hand hovers just off the surface (visible sliver, no
  intersection) — the interpolation-deviation class
  (≤4.94 mm) lives here.
- **Severity:** intersection/swallow = FAIL; hover = NOTE.
- **Exercise:** D-1/Plan 01 frames — hands planted at thighs
  / hips in all read frames (Plan 01 benchmark item 6 PASS;
  this commission's crops concur), 0 FAIL, 0 NOTE.
- **Provenance:** Plan 01 T-11 hand-lock record (closest-
  thigh-bone class; solved keys, residuals above);
  Plan 03 B3 (planted-hand IK as the reference behaviour).

### NS35-NC08 — Single-mass merge read — **LANDED (NOTE-grade only)**
- **Look at:** the contact interface at viewing size. NOTE
  when two bodies fuse into one undifferentiated mass with
  no readable boundary where the pose claims two distinct
  bodies in contact — the reader cannot tell where one body
  ends and the other begins.
- **Severity:** NOTE only, by exercise evidence: the D-1
  ¾ evidence camera produces a partial merge read at the
  pelvis in known-good castings (interface occluded by the
  follower's torso — Plan 01 benchmark item 1). As a FAIL it
  would fire on known-good frames; as a NOTE it correctly
  routes the frame to the measurement gate / a closer camera
  (Plan 01 eye item E-4 is exactly this routing).
- **Provenance:** Plan 01 benchmark item 1 + §6 eye items;
  D-1 frame reads, this commission.

## Applicability by artifact class (exercised, §C.4)

| Class | NC01 | NC02 | NC03 | NC04 | NC05 | NC07 | NC08 |
|---|---|---|---|---|---|---|---|
| 3D two-body render (D-1/Plan 01) | applies | applies | applies | applies | applies | applies | applies (NOTE) |
| 2D generated plate, single body (TG rounds) | N/A | N/A | N/A | N/A | N/A | self-contact only* | N/A |
| 2D generated plate with drawn contact (D-802 keepers) | drawn-form† | drawn-form† | drawn-form† | register-limited‡ | applies (drawn layer order) | drawn-form† | N/A |

\* TG plates are single-body; the only contact is self-contact
(hands at sides) — NC07's grip form does not engage.
† In drawn plates, overlap is a drawing convention: a hand
drawn over a torso is occlusion by construction. NC01/02/03/07
apply only in their **drawn-form**: a surface line that cuts
*across* a form (not along its occlusion edge), or a grip the
drawing itself renders as intersecting. No D-802 keeper fires
any drawn-form check (exercise §C.4).
‡ Cel registers do not promise contact shadows; NC04 in 2D is
recorded register-limited and never fires alone there.

## Status summary

| Status | Count | Checks |
|---|---|---|
| LANDED (FAIL-grade present) | 4 | NC01, NC02, NC03, NC05 (+ NC07 mixed FAIL/NOTE) |
| LANDED (NOTE-grade) | 2 | NC04, NC08 |
| LANDED (mixed) | 1 | NC07 |
| PRUNED | 1 | NC06 (fires on 7/7 known-good) |

**Landed checklist: 7 checks** (NC01–NC05, NC07, NC08) +
1 pruned candidate carried for provenance. Concordance vs
measured truth: `EXERCISE-RECORD.md` §C.2 — classification
concordance 7/7 castings; the checklist provably does not
rank subsurface depth (by design; see §C.2 for the numbers).
