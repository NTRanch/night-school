# Plan 09 — Pass 4 Application: the Blender-native route vs the Plan 07 route

- **Agent reads are labelled as agent reads.** The Owner's eye remains
  the admission verdict for every look claim below (eye items E-1…E-4).
- **Evidence:** Plan 09 Pass 3 (`PASS3-REBUILD.md`, renders + run
  record) against Plan 07's record (`runs/plan-07/PASS4-APPLICATION.md`:
  preset `preset-torogao-flip-viscous-ch1.json` + `CACHE-CONTRACT.md`;
  its gate read 7 PASS / 1 FAIL, the FAIL being droplet separation).
- Pre-registered class predictions (EXPECTED-VS-SEEN.md, written
  before the rebuild ran) are scored at the foot.

## The two routes, side by side

| Axis | Plan 07 — Mantaflow FLIP (solver) | Plan 09 — GN strand (posed) |
|---|---|---|
| What you author | Physics: domain, emitter, viscosity, surface tension | The path itself, drawn/authored on the body |
| What you get | Whatever the physics does (incl. surprises) | Exactly the path, fused (incl. no surprises) |
| Motion | Native: emission, fall, pooling, travel | None simulated; authored curve states re-evaluate per frame (Pass 3 probe) |
| Droplet separation | **Refuted in-route** (Plan 07 C-02: islands stayed 1) | Not applicable — strands are continuous by construction; a "droplet" is a separate small closed curve, posable but not emergent |
| Contact with bodies | Partial in the source (ground + mutual only); estate adds colliders approximately | Exact by construction: the path is authored on the surface (Draw, Depth = Surface; or anchor pairs) |
| Bridging two bodies | A jet must cross and may miss/break up | One curve, fused at both ends (Pass 3 v3, C-11) |
| Cost per configuration | ~54.5 s bake (Plan 07 record) + working cache + 477 MB Alembic handoff for one export | **~2 s total for four variants + animation probe; zero cache** |
| Determinism | 8/8 decoded-pixel hashes identical (Plan 07 gate) | 5/7 identical; the two-body shots differ by 2/518,400 px at one contact edge (F-3) — vertex counts identical |
| Parameter honesty | Viscosity has an API trap (base/exponent inert in 5.2); surface tension was spoken-only in its source | Radius is nominal: the Smooth finish delivers ≈half the set girth (F-1) unless budgeted |
| Failure modes | Overfill (90 f emission floods the 4.6 m domain by ~f120), unmapped parameters (9 of 24), separation failure | Zero-input collapse (guarded, T-16), lump states when sampling starves (T-02), girth contraction (F-1), strands intersect a *moving* body silently (no collision) |
| Skill to operate | Solver tuning, cache management | Curve drawing/posing; two knobs (Radius, Resolution) |

## Verdict by shot class (the plan's gate question)

- **Class A — posed strand / drape / bridge shots** (the fluid is
  already where the drama needs it: strands on skin, drips about to
  fall, bridges between bodies): **Plan 09 route is the default.**
  Exact path control, exact contact, no bake, trivially
  re-posable per frame, and its two weaknesses (no emergence, girth
  calibration) are known and budgeted in the preset. This class covers
  the bulk of the D-1 demonstrator's fluid layer as designed.
- **Class B — emission / travel shots** (fluid arrives from somewhere):
  **Plan 07 route remains the default**, with Plan 06's ratified
  contact-interface extrusion (D-1069) owning the contact moment. Plan
  09 can *finish* such a shot (a strand posed at the contact patch in
  the frames after arrival) but cannot produce the arrival.
- **Class C — free dynamics** (splash, breakup, pooling physics):
  **Plan 07 route alone.** Plan 09 is structurally excluded (T-12);
  no preset wording may imply otherwise.

**Named default (the gate asks for one):** for Torogao strand-class
work, the estate's default fluid route is now the **Plan 09
geometry-nodes strand route** (`preset-torogao-gn-strand-ch1.json`),
with the Plan 07 Mantaflow preset retained as the documented
alternative for emission/dynamics classes. This is a change of default
from the position after Plan 07 (when the solver route was the only
route) — the A/B record the plan exists to produce. The two presets
are siblings, both shipped in the results; neither deletes the other.

## SFW translation

The same group is a general **strand/rope/gel builder**: hair clumps,
cables, icing, slime, vines — anywhere a smooth fused tube along an
authored path is wanted. The SFW preset is the identical file; only the
material and the paths differ. (The technique's origin is an NSFW
tutorial; the construction is content-free, and the lane law governs
the *lesson transfer* — this application note is the SFW-safe form of
it: geometry only, no source imagery.)

## Gate (agent reads)

1. Route identified and evidenced end-to-end — **PASS** (agent read).
2. Rebuild from the sheet alone reproduces the route — **PASS**
   (11 REPRODUCED / 3 UNTESTABLE-IN-ROUTE / 1 UNTESTED; F-1/F-3
   recorded, not hidden).
3. Determinism — **PASS WITH NOTE**: bit-exact for single-strand work;
   2-px evaluation variance on two-body wide shots (F-3).
4. A/B verdict names a default with the loser kept — **PASS**.
5. Look of the final material (C-09b) in a rendered scene — **not
   gated here** (Workbench lane); queued as eye items.

## Eye items for the Owner

- **E-1:** Pass 3 render set (v1/v2/v2b/v3/v4 + anim states) — do the
  v3 strand and the bridge read as fluid at viewing size, or as rope?
  (Shape gate; the material in these renders is the debug green.)
- **E-2:** The source's own finished frames (OBSERVATION demo-reel and
  character-stage frames) against the D-1 demonstrator's needs — is
  this the strand look the demonstrator's fluid layer should carry?
- **E-3:** F-1's calibration: delivered girth ≈ ½ nominal under the
  full stack — accept the preset's 2× budget rule, or direct a
  Smooth-reduction variant as the estate standard?
- **E-4:** Class A default change (Plan 09 route as Torogao's default
  for strand-class shots) — ratify or hold at Plan 07 default.

## Pre-registered prediction scoring (from EXPECTED-VS-SEEN.md)

Class A → Plan 09: **confirmed by the renders.** Class B → Plan 07
with Plan 06 owning contact: **stands** (nothing in Plan 09's evidence
touches travel). Class C → Plan 07 alone: **stands.** No prediction
was contradicted by the rebuild; the two evidence-level misses
(E-2 count, E-6 vertex order) are recorded in EXPECTED-VS-SEEN and do
not bear on the class verdicts.


## Errata (2026-11-08, per D-1088 repair) — the D-1 landing claim in this record did not occur

Two claims above are corrected as statements about the shipped
D-1 demonstrator:

1. "This class covers the bulk of the D-1 demonstrator's fluid
   layer as designed." — FALSE as a landing claim. The D-1
   demonstrator's fluid layer is Plan 06's extrusion, ratified
   as form of record by D-1069; grep of the D-1 records and
   SIX-GIRL-STANDARD for the strand route = 0 hits.
2. The "Named default" statement that the estate's default
   fluid route "is now the Plan 09 geometry-nodes strand route
   (`preset-torogao-gn-strand-ch1.json`)" — the strand preset
   did not ship in D-1 and is not the shipped default. The
   shipped D-1 fluid default is the Plan 06 extrusion (D-1069),
   over Plan 07 FLIP foundations (STD §6).

The Plan 09 strand route remains a gated Pass 3 / Pass 4 result
inside this plan, and its per-shot-class verdicts stand as
plan-internal findings. What is withdrawn is only the claim
that the route landed in D-1. (Adoption audit
ADOPTION-AUDIT-20261108.md, Plan 09 row + Surprise 1; repair
commissioned by D-1088.)

## Disposition (2026-11-08, per D-1088 repair) — adopt set CLOSED

With the errata above: the Plan 09 strand route's adopt set
is closed as studied-not-adopted for estate production. Its
named landing (D-1) did not occur and no other consumer is
named in this record; the route remains a gated plan-internal
result (per-shot-class verdicts stand) and the preset remains
on file in this plan for any future commission that names a
landing first.
