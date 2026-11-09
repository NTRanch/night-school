# Plan 35 — Pass 4: Application Record

## 1. Taxonomy × current gate checklists — the mapping

**Checklist artifacts inventoried in the workspace** (read for
this mapping; none edited):

1. `~/workspace/custom-skills/local-face-plausibility-gate/SKILL.md`
   — the 8-item plausibility checklist (§2.1 singularity, §2.2
   layer order, §2.3 positional possibility, §2.4 state
   possibility, §2.5 temporal consistency, §2.6–2.8 closed-state
   purity set).
2. `~/workspace/custom-skills/local-face-state-measurement/SKILL.md`
   — the metric set (aperture, iris centroid, heart mass/solidity,
   pupil-visibility grade, mouth class, fluid census) + the
   small-read gate (wink test, pupil findability, set
   differentiation).
3. `~/workspace/custom-skills/local-character-art-production/`
   — Stage 3 measurement gates (human read → structural audits →
   numeric floors) and `references/04-failure-taxonomy.md`
   (design/reference, generation-mechanics, service, and review
   failure classes).
4. Per-round benchmarks, e.g.
   `~/workspace/full-rigs-20261103/keeper-art-reanchor/round-tg4/SHOULD-BE-SEEN.md`
   — the TG gate order (backgrounds/leak first, identity second,
   rig-cut fitness third) and its per-girl spec lines.

**Doctrine caveat, stated plainly:** the visual evaluation
doctrine itself (D-221 expected-vs-seen, D-629 verdict-pack
format) lives in estate memory, not in an artifact-side
checklist; the mapping below is against the four artifact-side
sources above, which is what a gate runner can actually hold.

### Mapping table (taxonomy class → coverage)

| Taxonomy class (TECHNIQUE §3) | Coverage | Where / gap |
|---|---|---|
| L-1 Skin-block wash | **Already caught — TG lane only** | TG4 benchmark: "no salmon/unshaded skin blocks". No standing cross-programme checklist carries it; outside a TG-style round benchmark it is written nowhere durable |
| L-2 Flat/unlit read | **GAP** | No checklist artifact found names it. The estate's 3D/Blender render lane has no artifact-side gate checklist at all |
| A-1 Hand defect | **Already caught — TG lane; partial elsewhere** | TG4 benchmark: "both hands visible with five fingers each". Character-art Stage 3 structural audits cover figure counts/framing, not finger-level hands |
| A-2 Non-neutral stance | **Already caught — TG lane only** | TG4 benchmark stance line ("neutral standing stance… arms at sides visibly separated"). Per-round, not durable |
| A-3 Proportion/register break | **Already caught** | TG4 benchmark per-girl proportions + register line; character-art Stage 3 landmark segment audit (bbox-pass/plan-fail counter in 04-failure-taxonomy) |
| M-1 Garment spec violation | **Already caught — TG lane** | TG4 benchmark outfit-exact lines incl. named fails ("a white skirt fails", "grey or white shirt fails outfit") |
| M-2 Print errors | **Already caught — TG lane** | TG4 benchmark: "(no print)", "cow-print must be on the DRESS, not migrated". The spec-relative subtlety (specified text is not a fire) is implicit in the benchmark's per-girl lines, stated nowhere as a rule |
| M-3 Invented motif | **Already caught — TG lane** | TG4 benchmark: "no floating hearts", "no glyph/text shapes" |
| C-1 Background leak | **Already caught** | TG gate (1), checked FIRST: "no tiled or giant faces, no floating or duplicate heads, no hair-mass blob…" |
| C-2 Framing crop | **Already caught — TG lane** | TG4 benchmark: "full body head-to-feet in frame with margin… no cropped head/feet". The benchmark-scoping lesson (partial crops are legitimate in other classes) is not written as a rule anywhere — Pass 3's prune evidence is its first record |
| F-1 Identity-feature defect | **Already caught (faces); partial (hair)** | Face-state measurement metrics + plausibility §2.1 cover eyes/pupils deterministically; hair-colour drift is caught only by TG benchmark identity lines |
| **(not in taxonomy) Two-body contact / interpenetration** | **GAP — class absent** | No checklist artifact found gates body-body interpenetration or contact plausibility for stills. The plausibility gate asks "could this face exist" for faces only; nothing asks it of two bodies in contact. (The class is estate-central: the two-body scene is the programme's named stress test, and the Plan 35 video's one finished render shows exactly this failure family incidentally — observer read, OBSERVATION §4.3, not a video claim.) |

### Headline gap list

1. **GAP — flat/unlit read (L-2)** and, with it, the whole
   3D-render lane: no artifact-side gate checklist exists for
   Blender/3D renders, the very medium the plan's video works
   in.
2. **GAP — two-body contact/interpenetration:** no checklist
   gates it for stills in any lane found.
3. **Partial — body-level classes (L-1, A-1, A-2) live only
   inside per-round benchmarks.** They are re-written per round
   rather than held in one durable checklist; the Pass 3
   candidate file (`PASS3-CANDIDATE-CHECKS.md`) is the first
   single artifact that holds them together. Adoption is a
   later gated step; nothing was edited here.
4. **Confirmations (not padding), per the plan's gate:** M-1,
   M-2, M-3, C-1, C-2, A-3, F-1(face) are already caught in the
   TG keeper-art lane — the exercise's highest-yield candidate
   (C03) duplicates the benchmark's outfit lines, which is why
   it fired most: the estate already gates what the plan's
   categories predict.

**SFW translation (per the plan):** the taxonomy is
rating-blind; every candidate check is garment/spec-relative
and applies unchanged to SFW render gates. Nothing in the
candidate file is NSFW-specific except its exercise pools.

## 2. Worked example — final candidate checklist × TG4-Y1, end-to-end

Artifact: `~/workspace/full-rigs-20261103/keeper-art-reanchor/round-tg4/candidates/TG4-Y1.png`
— the round's single FAIL plate; benchmark:
`round-tg4/SHOULD-BE-SEEN.md` (Yui: midnight bob, violet eyes,
heart pupils, fitted BLACK t-shirt no print, dark shorts, teal
accent, sneakers, plain ground, neutral stance).

| Check | Result | Evidence |
|---|---|---|
| C01 flat/unlit | no fire | Cel shading reads normally |
| C02 skin wash | no fire | Legs evenly shaded at viewing size (round census: likewise clean) |
| C03 garment spec | **FIRE** | Shirt is WHITE; benchmark names grey/white shirt as an outfit FAIL |
| C04 print error | no fire | Shirt is plain; TG3's glyph print is gone (round census concurs) |
| C05 invented motif | no fire | No hearts/glyphs/props in frame |
| C06 background leak | no fire | Plain light ground (TG3's face-pattern class absent; round census concurs) |
| C07 framing (scoped) | no fire | Full body head-to-feet in frame with margin |
| C08 stance | no fire | Neutral standing, arms at sides separated |
| C09 hands | no fire | Both hands visible, simple but formed |
| C10 face/identity | no fire | Violet eyes present; bob midnight, jaw length |
| C11 proportion/register | no fire | Petite mature proportions, cast cel register |

**Outcome: 1 fire (C03) → the checklist reproduces the round's
FAIL verdict and its exact basis** (the benchmark's named outfit
fail), with no false fires on the plate's clean dimensions.
Verdict concordance: round FAIL = checklist FAIL, same cause.

## 3. Gate (per the plan)

PASS = taxonomy written, mapped against current gate
checklists, gaps named; already-caught classes recorded as
confirmations. **PASS, with the premise correction of record:**
the taxonomy's video-derived half is empty by evidence
(TECHNIQUE §2), the estate-side half is written and mapped
(TECHNIQUE §3, §1 above), gaps are named (§1 headline list),
and the merged candidate checklist exists as a standalone
adoptable artifact (`PASS3-CANDIDATE-CHECKS.md` §1) with its
exercise record (§3) and pruning record (C07-unscoped,
C04-spec-blind) attached.
