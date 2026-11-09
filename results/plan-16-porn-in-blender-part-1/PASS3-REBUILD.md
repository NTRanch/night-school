# Plan 16 — Pass 3 Record (per the plan: no scene build)

The plan forbids a separate scene build ("Rebuild is shared
with Plans 01/02… duplication would waste the gate"). This
record is therefore the Pass 3 deliverable as the plan
scopes it: **the list of convergent techniques NOT in the
estate rebuild set**, each named as this plan's contribution
with its evidence and the specific estate artifact it would
amend. Amendments are PROPOSALS filed here; editing those
artifacts is a later gated step and was not done.

The estate rebuild set audited: Plan 01 PASS3-REBUILD (the
31-frame loop construction on the 54-bone standard, gated),
Plan 02 PASS3-REBUILD (the NS02 "Neon Backdrop" template +
its parameter block and assertions), and SIX-GIRL-STANDARD
§§2–7 as the standing rig/clip law both rebuilds cite.

## Contribution list (3)

### P3-1 — Textures-completeness is an intake gate, not a repair

- **Convergence:** AGREE row R1. Plan 01 (Anime Nyan):
  the Sombra **Textures_Sombra.rar** "must be downloaded
  and extracted or the model renders pink". Plan 16
  (Divinity Studio): "You're going to need the textures
  and the latest version here. You need both of them.
  They're important." Two independent creators state the
  same requirement in the same place: AT DOWNLOAD.
- **What the estate set has today:** Plan 01 T-01 files
  the fix under repair — File → External Data → Find
  Missing Files — and rules it "source-file hygiene for
  third-party downloads" that "does not transfer". There
  is no intake-side completeness check in either rebuild:
  a model enters the pipeline and its missing textures are
  discovered as a defect (pink render) after the fact.
- **The contribution:** promote completeness from repair
  to gate — a third-party model is not intake-complete
  until its texture payload is present and counted beside
  the model file, checked BEFORE first open.
- **Would amend:** (a) Plan 01 TECHNIQUE T-01 — the
  hygiene note gains the intake form ("completeness is
  checked at intake; Find Missing Files is the failure
  path, not the workflow"); (b) the Strobe asset-intake
  screen (`local-strobe-asset-intake` skill) — a
  textures-present line in the screening checklist.
- **Evidence:** OBSERVATION §1 (SmutBase listing: model
  zips + `Domina_textures.zip` 79.55 MB as separate
  downloads), §4 (the "you need both" passage); Plan 01
  OBSERVATION §1 (textures requirement, [BOTH]).

### P3-2 — Pristine-copy preservation precedes versioned saves

- **Convergence:** AGREE row R5. Plan 02 (RamFutaNSFW):
  the working file is saved incrementally Fixed →
  Fixed1…Fixed6 across the session. Plan 16 (Divinity
  Studio): "Typically when I download models, I'll save a
  copy. In case I make changes that messes up the file" —
  stated BEFORE any edit, as the first file operation
  after opening.
- **What the estate set has today:** Plan 02's TECHNIQUE
  adopts "incremental versioned saves… as template
  versioning practice" — versioning of BUILD OUTPUTS. The
  pristine-source half (a preserved, unedited copy of
  what was downloaded, made before the first change) is
  not named anywhere in the set.
- **The contribution:** versioned saving gains a step 0 —
  the pristine copy — so every later version has a known
  origin to diff or retreat to.
- **Would amend:** Plan 02 PASS3-REBUILD's template
  practice (the versioning note in TECHNIQUE Target 2's
  context) — one line: the template's first act on any
  external file is a preserved pristine copy.
- **Evidence:** OBSERVATION §4 (save-a-copy passage);
  Plan 02 OBSERVATION §1 (Fixed…Fixed6 title-bar trail).

### P3-3 — Pole-target placement is a named pre-posing step for every IK chain, arms included

- **Convergence:** AGREE row R12. Plan 01: leg IK pole
  targets aim the knees (T-03's posing context). Plan 16:
  an arm pole is placed on screen as its own step
  (`POLE-UpperArm.L`, a −0.569 m Z placement), and the
  narration generalises: "The legs have pole targets that
  allow you to move the knees… The hands have pole targets
  as well."
- **What the estate set has today:** Plan 01 T-03 names
  leg poles only, as a source-rig observation on the way
  to the FK translation. No entry states the general
  authoring step — place each chain's pole deliberately
  BEFORE posing the chain — and the arm/hand chains are
  not mentioned.
- **The contribution:** the general step, stated once:
  in any IK-assisted authoring pass, pole placement for
  every chain in use (legs, arms) precedes posing that
  chain; a pole left at its default is an unposed limb
  waiting to flip.
- **Would amend:** Plan 01 TECHNIQUE T-03 (the posing
  discipline entry) — the pole note widens from legs to
  all chains, as an authoring-scene practice. (The fleet
  itself stays FK per §2.1; this amends the AUTHORING
  discipline, not the skeleton — the same seam T-03
  already draws.)
- **Evidence:** OBSERVATION §3 (POLE-UpperArm.L move
  values), §4 (pole passages); Plan 01 OBSERVATION §2
  (leg pole targets).

## What was checked and found ALREADY in the set (not contributions)

- Never move the model / object-at-identity (R6): already
  a Plan 02 template ASSERTION and a Plan 01 T-03 rule.
- Gross→fine order, fingers last with contact as the check
  (R7, R9): Plan 02 Target 2 items 3–4, adopted.
- Simplify / performance-while-posing (R17): Plan 02's
  scripted Simplify-OFF pre-render assertion + ON-while-
  working discipline.
- Reference-first posing (R10): present in both rebuilds'
  disciplines.
- Solve outfit failure by visibility (R24): Plan 02
  Target 2 item 5 (Adapt form: variant selection).
- Render pair 0.0100/4096 (R22): adopted by BOTH prior
  sheets — and Part-2-pending for 16, so it cannot be
  this plan's contribution in any case.
- Loop/contact grammar (R19, R20): Plan 01's set owns it;
  Part 2 may add evidence but the set is not missing it.

## The empty-finding check

The list is NOT empty (3 contributions), but it is short,
and that is itself the finding's shape: **two prior plans
had already absorbed most of what a third creator
converges on.** Plan 16's marginal value sits exactly
where triangulation predicts — small, specific, and at
the seams (intake completeness, source preservation,
authoring generality) rather than in the core grammar.
