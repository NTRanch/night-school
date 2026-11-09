# Plan 12 — Pass 3 Branch + Pass 4 Application

## Pass 3 branch taken: MECHANISM FOUND → record + proposal only, NO build

The plan's rule: "None unless the intake finds a real
mechanism; if it does, the rebuild is scoped then and this
plan is amended." The intake DID find real mechanisms —
parameterized, named, and demonstrated in the editor:

1. **Shader eyes** (`character_eyes` + controller script):
   blink (amount/lower-lid ratio), gaze deform, pupil
   control, idle motion, sclera/pupil/highlight tints as
   uniforms on one quad.
2. **Skin-as-resource**: per-character variation bundled in
   a `.tres` skin with an editor Save Skin round-trip on the
   character root.
3. **Numeric jiggle block** (`body_physics.gd`): stiffness /
   damping / wobble / impact parameter groups as
   per-character data, with per-part jiggle nodes.
4. **Anatomy deform shader** (`hole_deformer`): nine numeric
   parameters driving an opening deformation on a layered
   sprite part. (NSFW-lane mechanism; recorded, not proposed
   across lanes.)

Per the plan, a rebuild is NOT built from this run: the plan
must be amended first, and that amendment is the
coordinator's/Owner's, not this run's. What this run files
instead is the scoped proposal below.

### Scoped rebuild proposal (for a future amended plan)

- **Candidate:** a parametric eye rig for the estate's 2D
  puppet lane (lumen rig stack): one quad per eye pair,
  shader uniforms for blink amount, lower-lid ratio, gaze
  offset/deform, pupil scale, and sclera/pupil/highlight
  tints, driven by a small controller that maps the estate's
  canonical emotion set onto uniform values.
- **Why it might earn its place:** the estate's 2D expression
  system is discrete baked sets; a parametric eye layer would
  give continuous blink/gaze between baked states without
  new art per state.
- **Scope guard:** eyes only. The jiggle block and the skin
  resource shape are recorded as candidacy notes (§ below),
  not proposals — one mechanism per amended plan.
- **Gate if amended:** the estate way — expected-vs-seen on
  a named character, blink/gaze states at viewing size,
  determinism check (same uniform set → same frame, twice).

## Pass 4 application: the comparison record + candidacy

The application the plan names is the comparison itself:
"Any consistency mechanism found is compared against the
estate's two-model rule and canonical-design governance"
(NSFW application), with the comparison as the lane-neutral
SFW translation. That comparison is TECHNIQUE.md §3. Its
operative conclusions:

- WaifuFactory's consistency mechanism is **structural**
  (one template: skeleton, part taxonomy, shaders, modules —
  every character inherits them by construction). The
  estate's is **governance-based** (canonical references,
  two-model rule, quarantine, keeper chains, eye gates) on
  top of its own structural templates (canonical rigged base
  in the sprite-to-3D lane). Neither evidences automated
  design-consistency checking. The two mechanisms answer
  different failure modes: template consistency stops rig
  drift; governance stops design drift. WaifuFactory has no
  visible answer to design drift (n=1 evidenced); the estate
  has no equivalent of the single-resource skin in its 2D
  lane.

### Candidacy register (candidate only, evidence attached)

| Candidate | For which estate factory | Evidence | Status |
|---|---|---|---|
| Parametric eye shader (blink/gaze/pupil/tints as uniforms + controller) | lumen 2D puppet lane | V5, V6, V7, SP6; f025/f028/f031 | CANDIDATE — rebuild proposal above; needs plan amendment |
| Skin-as-one-resource (single loadable parameter bundle per character + editor save round-trip) | character-art production (2D lane records) | V10; f001 | CANDIDATE — note only; estate keeper records are documents, this is a data shape worth borrowing if the 2D lane gains an editor surface |
| Numeric jiggle parameter block as per-character data | lumen 2D lane (3D lane already has jiggle work) | V9, SP2; f042 | CANDIDATE — note only |
| Anatomy deform shader | Torogao NSFW lane | V8, SP3/SP4; f012 | CANDIDATE (NSFW lane only) — note only; its animated behaviour is UNVERIFIABLE from this source (SP4), so candidacy rests on the parameter surface alone |

No candidacy is an adoption. Each would need its own
amended plan, rebuild, and gate.

## Gate (per plan)

PASS = intake record complete with claims listed and each
marked verified / unverifiable / absent.

- Claims tabled: **39 rows** — VERIFIED 23, UNVERIFIABLE 10,
  ABSENT 6 (TECHNIQUE.md §1).
- Every number in the table traces to a frame or a page
  artifact named in the row.
- No technique was inflated from this 94-second source: the
  four mechanisms are recorded at exactly the strength the
  artefact supports (editor-surface verified; runtime
  behaviour explicitly not claimed), and Pass 3 stopped at a
  proposal, per the plan.

**Gate: PASS.**

## Eye items queued for the Owner (minimal, per instructions)

1. The design-language read (OBSERVATION §2) is an agent
   read of one character — the green pixel-pattern
   Creeper-parody design, painted part puppet, adult
   proportions. One look at frames f001/f017 confirms or
   corrects it.
2. Nothing else in this run needs an eye: all other verdicts
   rest on UI text and numbers read from frames.
