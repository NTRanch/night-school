# Plan 19 — Pass 3 (scoped): the 60-second test protocol for Plan 20

Per this plan's brief there is **no standalone rebuild**
in Plan 19. The series rebuild lives in Plan 20; this file
is the hand-off Plan 20 executes: (a) the grammar it must
apply is TECHNIQUE.md §2/§4; (b) the test protocol is
below; (c) the aliveness check is §3. If Plan 20 has not
run when this file is read, this protocol is the hand-off,
stated as such.

## §1 Test object

A 60-second sustained estate scene built from the estate's
78-sample loop (Plan 01's built pair: Prima follower /
Yui leader, 78 samples @ 60 Hz = 1.30 s per cycle, Contact
at sample 38), tiled to 3,600 samples = 46 full cycles
(3,588 samples) + a 12-sample head of cycle 47, **or**
authored directly at 3,600 samples via the C1 pattern
driver at a stated regime. Either construction is
admissible; the construction used is recorded with its
parameter record / seed, per D-1072's provenance notes.

## §2 Grammar → mechanism mapping

Estate machinery of record: D-1072's three commissioned
mechanisms, all PASS (periods/travel exact; follow-lag
peak +7 samples at τ=3 with contact drift 0.000;
seeded variation byte-identical per seed, cross-seed max
distance 1.7747°, checker-proven).

| Grammar rule | Mechanism | Status |
|---|---|---|
| V-1 Rotate by channel family | **C3 seeded variation** — per-cycle, per-eligible-channel jitter (±2% amplitude, ±1 sample phase, sha256(seed\|cycle\|channel)); family rotation is expressed as the per-cycle variation schedule over eligible channel groups | MAPPED |
| V-2 Whole-span selection | C3 applies across the full cycle span by construction; C1 bakes whole-clip regimes, never partial spans | MAPPED |
| V-3 Endpoint review | The aliveness check itself (§3): samples are taken at cycle boundaries (start/middle/end cycles), the estate form of endpoint inspection | MAPPED (as protocol) |
| V-4 Return to small parts late | C3 with a **two-block seed schedule**: cycles 24–46 drawn with the small-part eligible groups (feet/face-adjacent channels) at the full ±2% bound while large-family groups narrow to ±1% — a parameter choice inside C3's existing bounds machinery, recorded in provenance | MAPPED (parameter-level) |
| V-5 Cut length before polish | **NO MECHANISM — hand-authoring item.** The 60 s length is the test's given; the rule is discharged by the director's decision to test at 60 s, recorded in Plan 20's intake, not by a tool | HAND |
| V-6 Diagnostic mode survey | **NO MECHANISM — hand-authoring item.** Estate form: one viewport pass over the middle sample in a diagnostic shading (Blender solid/whiteout class) before the aliveness frames are judged; a human step in Plan 20's run sheet | HAND |
| V-7 Still-render checkpoint | **NO MECHANISM — hand-authoring item.** Estate form: stills rendered at the three aliveness samples at delivery settings before motion is judged (the frames §3's eye gate consumes) | HAND |
| V-8 Pose idea first | **NO MECHANISM — hand-authoring item.** The rebuild's brief states the tableau in one sentence before building ( Plan 01's record already works this way: casting + arrangement stated up front) | HAND |
| Reaction life inside the cycle | **C2 follow-lag**, τ=3 samples, Spine/Spine1/Neck/Head X-twist only, Hips and hand chains exempt — the follower's reaction peak lands +7 samples after Contact in every cycle | MAPPED |
| Tempo/travel shaping over the minute | **C1 pattern driver** — if the tiling construction is used, one regime change is scheduled at the middle sample boundary (e.g. R1_mid → R2_slow) so the minute has a stated tempo event; if C1 authors the whole 60 s directly, the regime record is the tempo statement | MAPPED |

Invariants (§4 of TECHNIQUE) map to exemptions, not
mechanisms: C3's exempt list (Hips rotation+translation,
shoulder/arm/forearm/hand + finger chains, governed face
channel) is the estate's enforcement of "the frame does
not move" — contact, hand locks, and identity channels
never vary.

## §3 The aliveness check (Plan 20 executes; this plan defines)

**Samples:** cycle 1 (samples 0–77), cycle 23 — the
middle (samples 1716–1793), cycle 46 — the end (samples
3510–3587). At each sample, two halves are judged:

**MUST DIFFER (life):**
1. C3 distance between this cycle's clip and cycle 1's,
   over eligible channels: max > 0.1° and RMS > 0.01°
   (D-1072 C3 gate values) — for the middle and end
   samples. (Cycle 1 differs from itself trivially; its
   life criterion is #2.)
2. Follower reaction present: Spine RX peak inside the
   cycle lands **+7 samples (±1) after the cycle's
   Contact sample** (C2 τ=3 signature), at all three
   samples.
3. The three samples' rendered frames are not
   pixel-identical at matched in-cycle phases (decoded-
   pixel hash at Contact-phase frame differs across
   samples) — while the seam frames (cycle starts) may
   match, per the seam law.

**MUST NOT HAVE DRIFTED (integrity), re-measured at each
sample against Plan 01's records:**
4. Contact-anchor drift within the cycle: **max ≤
   0.393 mm** (Plan 01's keyed-lock class; C2's measured
   value on this machinery is 0.000 mm). Measured at the
   contact anchor, not the Hips origin (D-1072 anchor-
   proxy note: fit RMS 0.004 mm).
5. Interpenetration on the contact set: the end sample's
   max must not exceed the start sample's max by more
   than **0.5 mm**, and neither may exceed Plan 01's
   post-cure record (**max 5.46 mm**, mean-of-sample-
   maxima 3.76 mm) by more than the same margin.
6. Seam exactness at each sample's cycle boundary:
   per-bone pose deltas **0.000 mm / 0.000°** (Plan 01's
   seam construction), and C3's bounds scan clean across
   all 3,600 samples with zero exempt-channel
   differences.
7. Hand-lock deviation: frame-0-class residuals (Plan 01:
   ≤0.46 mm follower, ≤0.39 mm leader) at each sample's
   Contact frame.

**Verdict:** the 60 s gate PASSes only if all three
samples pass both halves. A minute that is alive at the
start and drifted at the end FAILs; a minute that is
intact but identical across samples FAILs the other way.
The eye gate consumes the §2/V-7 stills at viewing size
alongside these numbers (verdict-pack discipline: numbers
support, the eye decides).

## §4 What this protocol does not claim

It tests the grammar's *machinery* mapping. The taste
residue (TECHNIQUE §1/§6 — sequencing judgement) is not
gated here; Plan 20's record should state which family
emphasis schedule it used and why, in the director's own
words, as the example index's next entry.
