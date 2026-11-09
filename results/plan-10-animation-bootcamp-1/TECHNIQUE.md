# Plan 10 — Pass 2 Technique Sheet (Distillation)

Source: `OBSERVATION.md` (Pass 1). The episode is a tooling
lesson — Timeline / Dope Sheet / Graph Editor — taught on one
14-frame two-body loop (torso Z channel, Shani_IK_Rig). Its
distillable content is an **editing model**: three layers of an
animation artifact, each with its own editor, its own operation
class, and its own failure modes. Principles of motion appear
as consequences of curve shape. Speech-side claims are
PENDING-TRANSCRIPT (OBSERVATION C-10-8); nothing below rests
on narration.

## Target 1 — Principle inventory vs the estate grammar

The estate grammar as it stands (animation-grammar atlas +
sprite-acting + game-feel + companion-idle skills, Plans 01/03
findings) measured against what the episode teaches:

| # | Episode item (mechanism) | Estate status | Verdict |
|---|---|---|---|
| 1 | **Three-layer division of labour**: Timeline owns range/playback/markers; Dope Sheet owns key placement across channels; Graph Editor owns interpolation between keys | Used unnamed — Blender work moves between the editors without the model; the scripted lane collapses all three into code | **Adopt** the model as names for the three layers of every estate animation artifact: *range*, *keys*, *curves*. A defect is filed against exactly one layer |
| 2 | **Timing vs spacing split**: moving keys (Dope Sheet, G/S) changes WHEN; handles (Graph Editor) change HOW — spacing is the curve's derivative, read between keys | Used in measurement (atlas frame-diff series = spacing) but not as an *editing rule* | **Adopt** as the editing rule: retiming and re-easing are separate operations, separately gated |
| 3 | **Handle-type vocabulary**: Free / Aligned / Vector / Automatic / Auto Clamped (menu of record, 24:30) | Partial — code lanes name easings; Blender-side work had no recorded handle discipline | **Adopt** the five names as the estate's easing vocabulary in Blender-facing work; Pass 3 implements Vector + Auto semantics exactly |
| 4 | **Vector = constant spacing + corners at keys** (the V-curve demo) | Known in effect (linear segments in code), never named as a *defect signature* | **Adopt** as a diagnostic: piecewise-constant spacing series with jumps at keys = Vector/linear contamination in a curve meant to be smooth |
| 5 | **Overshoot as a curve defect**: smooth (auto) interpolation can cross a key's value near flat neighbours; fixing it is Graph Editor work (slide bullet; dip demo ~22:30) | Game-feel lane knows overshoot only as a *feature* (anticipation → overshoot) | **Adapt**: add the dual — in baked loops, excursion past a settle key is a measurable defect class (metric in Pass 3: settle overshoot, and its ratio to the preceding drop). Feature-overshoot stays deliberate and keyed, never an interpolation side-effect |
| 6 | **Motion Paths** (In Range, keyframe numbers on, thickness 6): trajectory + key placement judged together in space | Not used — the headless lane inspects numbers and strips, never a trajectory with keys marked | **Adapt**: the *check* ports, the viewport doesn't. Estate form = trajectory strip with key frames marked + spacing series beside it (Pass 3 strips are the seed form). **Reject** literal viewport paths for the headless lane |
| 7 | **Loop construction**: sparse keys (5, 7, 9 in view; range 1–14), matched end values, one channel carried end-to-end before others | Used (Plan 01 loop; atlas E8 closure gate; companion idle 12-frame form) | **Adopt** as confirmation + one sharpening: build loops one channel end-to-end first (the episode never keys a second channel) |
| 8 | **F-Curve modifiers** (Cycles, Noise, Envelope, Limits — slide) | Cycles: used in effect (cyclic closure). Noise: deliberately absent — determinism law | **Adopt** Cycles-by-name for loop extrapolation in Blender-facing work. **Reject** the Noise modifier as-is (unseeded); its legitimate use is already covered by the seeded-variation candidate (Plan 03 C3, commissioned D-1072) |
| 9 | **Markers / story beats** in the Timeline; keyframe *types* (coloured breakdown keys, menu ~25:00) | Beats exist as *measured* objects (atlas), not authored markers; key types unused in the scripted lane (keys are data) | **Adapt** markers → named beats in shot specs. **Reject** keyframe types for the estate form — no consumer |
| 10 | **Bulk interpolation via T in the Dope Sheet**, then per-handle refinement (slide TIP) | No equivalent discipline recorded | **Adapt**: in scripted form this is "set the easing family for the whole action, then pull individual handles" — a two-level authoring rule, implemented in Pass 3's exercise 2 (family first, one pulled handle) |

**Principles the plan went hunting for** (anticipation, arcs,
squash-and-stretch as named principles): **not taught as
principles in this episode.** Anticipation appears only as
curve shape before a drop; arcs appear only as the motion-path
ellipse. Recorded as a plan-expectation miss (OBSERVATION
"Surprises"), not an episode defect — the Dojo's Week 1 is
tooling; the plan's principle inventory is answered by the
table above instead: the estate uses #2/#5 unnamed, lacked
#1/#3/#10 as named discipline, and deliberately refuses
unseeded #8.

## Target 2 — Exercise value (which expose estate weaknesses fastest)

1. **Handle-type spacing audit** (episode's V-vs-smooth demo,
   as measurement): run any estate loop's spacing series; jumps
   at keys expose linear contamination. Fastest first because
   it is pure measurement on existing artifacts — Pass 3
   exercise 1 builds the reference signatures.
2. **Settle-overshoot audit**: excursion past settle keys in
   baked loops (defect #5). Exposes interpolation side-effects
   nobody keyed — Pass 3 exercise 2 builds the metric.
3. **Trajectory-with-keys strip** for the two-body loop
   (adapted Motion Paths, #6): spacing judged in space at the
   contact interface — joins the Plan 35 GAP 2 territory
   (commissioned D-1071); not built here, named as the
   follow-on with the highest value.

**The exercise, resolved:** the narration (OBSERVATION
addendum) names the episode's exercise — the **bouncing ball,
converted**: the torso-Z bob is a bounce cycle taught
pose-to-pose. Pass 3's exercise subjects (a ball bob for the
loop; a gesture for the idle) were chosen from the plan's
generic rebuild spec before the transcript existed; the
episode's own atom and the estate rebuild's atom are the
same, which is why the rebuild's measurements speak directly
to the episode's claims. **Pose-to-pose** is Adopted as a
named term alongside it (estate-used, now sourced).

## The named estate form — NS10 "Three-Layer Loop"

Range (1..N, matched end values) → Keys (sparse, one channel
end-to-end first) → Curves (easing family set for the action,
then individual handles pulled deliberately; Vector only where
constant spacing is intended; every settle key audited for
interpolation overshoot). Each layer separately gated:
closure for range, spacing series for keys+curves, overshoot
metric for curves. Pass 3 implements and measures it.
