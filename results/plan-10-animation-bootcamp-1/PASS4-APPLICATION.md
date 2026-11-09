# Plan 10 — Pass 4 Application and Gate

Technique applied: **NS10 "Three-Layer Loop"** (TECHNIQUE.md).

## Targets

- **NSFW-lane application:** the Pass 3 gesture, finished as a
  12-frame companion-form idle cycle (the estate idle length)
  built strictly in NS10 order — range first (1–12, matched end
  values), keys second (sparse: 1, 3, 6, 9, 12), curves last
  (Auto family for the action, one deliberately pulled Free
  handle into the settle key). This is the practice-set form
  the two-body and idle programmes consume: a torso-bob cycle
  is the shared atom of both (the episode's own channel).
- **Two-body follow-on (named, procedure fixed here):** the
  same three-layer audit run over the D-1 demonstrator's Plan
  01 loop curves when the coordinator next opens that tree —
  spacing series per channel, key-jump audit, settle-overshoot
  audit. Not executed in this run: the D-1 tree is the
  coordinator's active workdir, and this lane does not write
  into another lane's tree. The audit script form is
  `stage/fcurve_exercises.py`'s measurement core, which takes
  any key list.
- **SFW translation:** the identical gesture rendered on a
  lane-neutral geometric mannequin (teal, labelled SFW) — same
  keys, same curves, same measurements. Fundamentals are
  lane-neutral by definition (plan); the translation record is
  the strip + this gate rerun on it.

## Expected-vs-seen benchmark (written BEFORE the gate run)

Expected, per item:
1. **Loop closure:** wrap step (f12→f1) = 0.000000 and the
   strip's first/last frames differ only by the bob's rest
   position (both at rest value 0).
2. **Dead frames:** 0 exact-duplicate consecutive frame pairs
   in either strip (atlas E7 form, decoded-pixel comparison).
3. **Key-jump audit (curves layer):** the Auto-family spacing
   series has no piecewise-constant runs (the Vector signature
   from Pass 3 exercise 1); spacing varies at every step.
4. **Settle overshoot:** the deliberate pull shows as a steeper
   approach into the settle key than the unpulled control
   (measured Pass 3: +23%), AND the only past-rest excursion
   is the known auto-tangent artifact ≤ 0.0025 in toy units,
   recorded — not hidden.
5. **SFW identity of form:** SFW strip's decoded-pixel hash
   differs from the NSFW strip (different subject rendering)
   while its measurement row is identical (same curves).

## Gate run (stage/pass4_gate.py, measurements in stage/pass4-measurements.json)

Agent reads (Pax's lane read, labelled as such — the Owner's
eye is the admission verdict; eye items in REPORT.md):

1. **Loop closure — PASS.** Wrap step −0.0 (f12 = f1 = rest 0).
   First/last strip frames are pixel-identical once the frame
   *label glyphs* are masked out (the unmasked comparison is
   confounded by the "A1"/"A12" text — measured confound,
   recorded, `stage/pass4-firstlast.json`: both strips true).
2. **Dead frames — PASS.** 0 exact-duplicate consecutive pairs
   in either strip (decoded pixels).
3. **Key-jump audit — FAIL as written, signature absent.**
   The strict wording ("spacing varies at every step") fails:
   the spacing series carries two 2-step constant pairs
   (+0.008556 ×2 into the settle, −0.001111 ×2 in the settle
   tail — symmetry of the pulled segment, values at 6 dp).
   The defect the item hunts — the Vector signature of Pass 3
   exercise 1 (constant runs of 4–5 with ×2.8 jumps between
   runs) — is absent (max run 2, no jumps). Recorded as FAIL
   against the benchmark's letter; the benchmark wording is
   the thing to fix in the NS10 form (runs ≥ 3 = contamination
   signature), and that correction is proposed, not silently
   applied.
4. **Settle overshoot — PASS.** Approach into the settle key
   steepened by the deliberate pull (+23% vs the unpulled
   control, Pass 3); the only past-rest excursion is the known
   auto-tangent artifact, 0.002222 ≤ the 0.0025 bound written
   in the benchmark — present, measured, and recorded as the
   episode's C-10-6 defect in miniature.
5. **SFW identity of form — PASS.** SFW strip pixel hash
   differs (cde136ee… vs 1e212b57…); the measurement row is
   the same curves by construction, and the SFW strip passes
   items 1–2 identically.

**Gate summary (agent read):** the NS10 form applies and
gates; 4 PASS, 1 FAIL-against-its-own-wording with the defect
signature absent. Plan gate (inventory mapped, exercises run,
gaps adopted or rejected with reasons) is met on the agent
side; admission is the Owner's eye (REPORT.md eye items).
