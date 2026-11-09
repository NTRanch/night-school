# Plan 03 — Technique Sheet (Pass 2 distillation)

Two targets per the plan: (1) the VaM solver inventory with
estate equivalents and gaps stated as questions; (2) the
short-loop grammar. Behaviour IDs (B1–B9) are OBSERVATION.md
§4's. The estate stack of record: the six-girl Blender
standard (keyed clips, Mesh Deform cages, Mantaflow, §7
retarget), plus lumen/torogao as relevant.

## §1 VaM solver inventory → estate equivalents

| # | Behaviour / VaM system | Estate equivalent | Verdict |
|---|------------------------|-------------------|---------|
| B1 | Parametric pattern driver — one cycle, live depth / bias / speed / play-stop (vamX pattern panel) | Keyed clips exist (Plan 01's 78-sample loop), but they are fixed recordings: one clip per (depth, rate, shape). No parametric pattern generator with separable travel/rate/shape controls exists in the standard or in lumen/torogao | **PARTIAL** |
| B2 | Control-follow lag — the head control chases its target through physics; lag is zero at extremes, max mid-travel | Keyed clips are exact by construction; the deterministic stack has no follow-dynamics layer (deliberately — determinism is the estate's gate discipline) | **NO EQUIVALENT** |
| B3 | Planted-hand IK — hands hold the partner while the torso translates | Plan 01 shipped exactly this as **solved keys** (hand locks ship as solved keys, never constraints; contact locked by Child Of in the solving pass, then baked) | **EQUIVALENT** (baked form) |
| B4 | Spine/neck joint-chain distribution of a driven translation | Authored in keyed clips; §7 retarget carries the distribution across all six girls (proven in D-1) | **EQUIVALENT** |
| B5 | Contact maintained at the forward extreme, no visible interpenetration across ~46 sampled cycles | Plan 01's contact lock + penetration cure (5.97 → 5.46 mm residual, measured) — the estate does at bake time what VaM does live | **EQUIVALENT** (baked form; the source behaviour itself is only PARTIAL-attributed, OBSERVATION B5) |
| B6 | Hair solver — not exercised in this footage (rigid bun) | The six-girl standard has no hair-dynamics layer; hair ships as mesh/shape-keyed geometry | **NO EQUIVALENT** (gap named from absence in *both* — see Q3) |
| B7 | Soft-body solver — not visibly exercised in this footage | Plan 39's Mesh Deform cage jiggle: determinism-proven, layered over the Plan 01 loop with contact-set delta 0.000 mm | **EQUIVALENT** |
| B9 | Cycle-to-cycle non-repeatability — zero pixel-equal corresponding pairs; variation is continuous physics/clock drift | The estate is deterministic by design (seam exact 0.000 mm/°, clips bit-identical across runs) — non-repeatability is the one behaviour the stack refuses on principle | **NO EQUIVALENT** (by design) |

**Count: 8 inventoried behaviours — EQUIVALENT 4 (B3, B4,
B5, B7) · PARTIAL 1 (B1) · NO EQUIVALENT 3 (B2, B6, B9).**
(B8, the static partner, is a staging fact, not a system.)

### Gap questions (the plan's gate: questions, not conclusions)

- **Q1 (from B1, PARTIAL):** Would a parametric pattern
  driver — one authored cycle exposed as travel / rate /
  dwell-shape controls, baked to keyed clips on demand — pay
  for itself in Torogao scene direction, where today every
  (depth, rate) variant is a separate clip? The clip is the
  evidence that three sliders generate a whole test reel
  (8 regimes, 82.7 s) from a single pattern.
- **Q2 (from B2, NO EQUIVALENT):** Is the follow-lag — the
  visible chase between target and head — part of why VaM
  motion reads as physical rather than keyed, and if so, can
  a *deterministic* lag (a fixed phase/response curve applied
  at bake time) capture the read without importing real-time
  non-determinism into the stack?
- **Q3 (from B6, NO EQUIVALENT):** The standard has no hair
  dynamics and this footage exercises none — is hair motion a
  gap the estate actually feels (loose-hair heroines in
  motion shots), or does the bun/ponytail canon make it a
  non-gap? This record cannot answer it; it can only show
  VaM's reference scene also declining to exercise it.
- **Q4 (from B9, NO EQUIVALENT by design):** For loops meant
  to run long (idle/ambient scenes), is the estate's exact
  repetition a ceiling — and would a *seeded* variation layer
  (variation that is itself deterministic and gate-able) be
  admissible, or is exactness the feature?

Each question, if the Owner wants it pursued, leaves as a
commission candidate — PASS4-APPLICATION.md carries them in
that form. None is a build authorisation.

## §2 Short-loop grammar — why this 83 seconds stays watchable

**Answer: not variation inside the loop, and not camera —
parameter change imposed from outside the loop.** The clip is
a sweep, not a loop performance:

- **One cycle, eight regimes.** The underlying cycle is
  63–150 frames (1.05–2.50 s) depending on regime
  (OBSERVATION §2). Nothing inside a regime changes: within
  S3/S4/S8 the cycle-corresponding frames differ only by
  physics micro-drift (head-ROI cycle MAD 8.9–9.7, zero
  exact pairs) — present, but far below what a viewer reads
  as variety.
- **The accents are the operator's, on a ~10–25 s cadence:**
  a 3.9 s full stop at the back extreme (3.55–7.43 s), depth
  collapsed to zero and restored (11.5–19.1 s), bias swept
  end to end (25.1–34.2 s), speed dropped to its floor
  (40.9 s), speed raised for a fast finish (65.4 s, period
  1.78 s → 1.05 s, motion energy the clip's highest). Every
  regime change is a visible event; the viewer's attention
  is re-bought by the *next test*, not by the loop.
- **Camera contributes nothing** — it is a fixed test-bench
  framing (MAD 0.000–0.014 vs frame 0) chosen to keep panel,
  path, and contact in one view.
- **Inside the cycle, the one accent is the forward
  extreme:** contact, once per cycle, with the head's dwell
  at the extremes (follow-lag zero at extremes, B2) giving
  the cycle its beat shape.

**Comparison point — the estate's Plan 01 loop:** a fixed
78-sample cycle at 60 Hz (1.30 s), seam-exact, whose
watchability is *authored inside the cycle* — leader/follower
phase offsets between two bodies, contact locked throughout.
Plan 03 is the opposite strategy: a single-body cycle kept
alive by *changing its parameters from outside*. The two
strategies compose (a phase-offset two-body loop whose
parameters sweep slowly is both), and that composition is
exactly Q1 above — recorded as a question, not a claim.

**Transferable form (the sheet's one portable rule):** a
short loop presented for longer than ~10 cycles needs an
event cadence outside the loop — parameter change, stop,
rate shift — at roughly 8–25 s spacing, or an internal
phase structure rich enough to substitute. This clip
demonstrates the outside-cadence route with 7 events in
82.7 s (one per ~12 s); Plan 01 demonstrates the
internal-structure route. Stated as an observation from two
records, not as estate doctrine.
