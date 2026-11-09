# Plan 10 — Animation Bootcamp 1 — Run Report

Agent: df278bb4-2e93-43b1-9097-667f7822377e (subagent, direct
lane, D-1073 all-hands). Run: 2026-11-06 17:44– PST.
Plan: `repo/plans/10-animation-bootcamp-1.md`. Source:
rule34video 4331646, kaitou3d / NSFW Blender Dojo, 25:52.

## Outcome in one paragraph

The episode is not the principles lecture the plan expected:
it is a **tooling lesson** — Timeline / Dope Sheet / Graph
Editor — taught end-to-end on one 14-frame two-body loop
(torso Z channel of a pre-rigged scene, Blender 4.5.7). The
plan's gate is met on the agent side: the principle inventory
is mapped against the estate grammar (10 items: 4 Adopt,
4 Adapt-with-parts, 2 Reject-in-part — TECHNIQUE.md), the
exercises were rebuilt clean-room and measured (Pass 3), and
the named form **NS10 "Three-Layer Loop"** was applied and
gated (Pass 4: 4 PASS, 1 FAIL against its own benchmark
wording with the defect signature absent). Admission verdicts
are the Owner's eye — see eye items. One claim (C-10-8,
speech-side content) is resolved in the addendum below from
the transcript when it lands.

## Pass outcomes

- **Pass 0 (INTAKE.md):** metadata of record — uploader
  kaitou3d (member 91300), upload 2026-04-13, 4,769 views,
  no licence stated (study-only posture). The intake caught
  the premise disagreement *before viewing*: the creator's
  description bills Week 1 as timeline + graph editor
  introduction, not a principles lecture.
- **Pass 1 (OBSERVATION.md, MANIFEST.md):** pin 555,026,396 B,
  SHA-256 30ec7b4b…, decode-verified at 4 points; the hybrid
  two-egress capture is documented in the manifest. Screen
  log at 30 s grid + 17 native frames: rig Shani_IK_Rig,
  action Shani_IK_RigAction, torso channels (Loc/Quat/Scale),
  frame range 1–14, keys at 5/7/9, Z curve ≈ −0.49 → −0.657
  (trough, f7; cross-checked against the Transform read
  −0.65698 at the same frame), Motion Paths settings read at
  native res, the MOTION EDITORS theory slide transcribed
  from a native frame (12:44), and the handle-type menu of
  record (Free / Aligned / Vector / Automatic / Auto Clamped,
  24:30).
- **Pass 2 (TECHNIQUE.md):** inventory mapped. Headline
  findings: the estate used the timing/spacing split and
  overshoot-as-feature unnamed; it lacked the three-layer
  editor model, the five-name handle vocabulary, and the
  two-level authoring discipline (family first, then pulled
  handles) as named forms; overshoot-as-*defect* (an
  interpolation side-effect at settle keys) is a new gate
  class; unseeded Noise modifiers rejected (determinism law),
  their legitimate use already covered by Plan 03 C3.
- **Pass 3 (PASS3-REBUILD.md, stage/):** a clean-room
  Bezier F-curve evaluator (pure Python; no Blender, no video
  open) + two exercises, all measured in
  `stage/measurements.json`, all 4 strips determinism-verified
  (decoded-pixel hash, twice-rendered, 4/4 identical):
  - C-10-3 REPRODUCED with measured difference: identical
    keys, Vector gives piecewise-constant spacing with jumps
    at keys; Auto gives continuously varying spacing.
  - C-10-4 REPRODUCED (the 14-frame construction closes,
    wrap step 0.0 in both modes).
  - C-10-6 REPRODUCED as a defect: Auto interpolation crosses
    rest by +0.002222 after a settle key with no key past
    rest — overshoot nobody keyed, now a metric.
  - C-10-2's discipline exercised: family-first + one pulled
    handle steepens the settle approach by +23% with keys
    unmoved.
  - C-10-1 / C-10-7 ADOPTED-AS-MODEL (Blender-UI workflow
    claims; their estate content is the three-layer model,
    exercised structurally). C-10-5 ADAPTED (check-form
    seeded; full two-body trajectory render is the named
    follow-on with Plan 35 GAP 2, D-1071).
- **Pass 4 (PASS4-APPLICATION.md):** NS10 applied to a
  12-frame companion-form idle gesture (NSFW lane) and the
  identical curves on a lane-neutral mannequin (SFW
  translation). Benchmark written before the run. Items:
  closure PASS (wrap −0.0; first/last pixel-identical with
  label glyphs masked — the unmasked confound is measured
  and recorded), dead frames PASS (0 duplicates, both
  strips), settle overshoot PASS (0.002222 ≤ 0.0025 bound;
  pull effect +23%), SFW form-identity PASS. **Key-jump
  audit FAIL against its own strict wording** (two 2-step
  constant spacing pairs from segment symmetry) with the
  Vector contamination signature absent (max run 2 vs the
  signature's 4–5 + jumps); the correction (runs ≥ 3 =
  signature) is proposed in PASS4 for the NS10 form, not
  silently applied.
  Two-body follow-on fixed by procedure: the same audit over
  the D-1 demonstrator's Plan 01 loop curves when the
  coordinator next opens that tree (this lane does not write
  into another lane's active tree).

## Eye items for the Owner (agent reads only — no PASS declared)

- **E-1:** Pass 4 strips (`stage/pass4-strip-nsfw.png`,
  `stage/pass4-strip-sfw.png`): does the anticipation rise
  (frames 2–3) read at viewing size, or is +0.012 too subtle
  against the −0.030 drop?
- **E-2:** Loop strips (`stage/strip-loop-vector.png` vs
  `strip-loop-auto.png`): the Vector/Auto difference is a
  spacing difference only at this subject scale — visible in
  the numbers, subtle in the strip. Worth a look before the
  spacing-audit gate is trusted on real loops.
- **E-3:** Cosmetic, recorded not gated: in the gesture
  strips the support stem renders as a small post above the
  disc on below-ground frames (frames 5–7). Drawing artifact
  of the exercise renderer; the trajectory read is unaffected.

## Friction (D-1064) — answered in BLOCH-CANDIDATE.md

/tmp tmpfs size, silent background-scp death, per-segment
resets wanting ranged resume / ≤20 MB segments. The bloch
candidate also carries the two lessons: interpolation-
manufactured overshoot as a gate class, and Plan 10 as the
second instance of the premise-is-a-claim pattern.

## Cleanup

Working media in `dl/` (segments, WAV, sandbox assembly)
removed at task end; the canonical pin + transcript outputs
stay on primo; run-dir deliverables + `frames/` + `stage/`
are the record. EXECUTION-STATE.md untouched (coordinator
reconciles from this report), per brief.

## Addendum — transcript resolution (C-10-8)

**C-10-8 RESOLVED** from the whisper log harvest (the lane
streams segments to its log progressively; the harvest is a
first-class read of that stream, not a summary of it):
segments 0:00–8:33 of 25:52, 87 segments, loop census
**0.0% loop share / 100% recoverable** on the harvested span,
single-transcriber tier **UNCONFIRMED**. The exercise is set
verbally: the **bouncing-ball tutorial, converted** to the
cowgirl loop; method named **pose-to-pose**; loop closure by
Shift+D duplication of the first key to frame 15; no separate
homework is set in the harvested span. Full detail:
OBSERVATION.md "Narration addendum" (7 points, incl. one
recorded narration/screen tension where the screen governs).

**Transcript file state (honest partial):** the primo whisper
job (detach `ns10-whisper`, PID 4128922 at last check) was
still running at report time — the all-hands contention (two
other lanes' whisper jobs, one at 213 CPU-min) held it to
~0.6× realtime. The harvested span is saved in the run dir as
`transcript-partial.txt`, labelled partial. **Coordinator
harvest item:** when `~/.local/share/pax/detach/ns10-whisper.done`
lands on primo, copy `~/.local/share/pax/night-school/plan-10/transcript.srt`
+ `transcript.txt` into this run dir and `repo/results/plan-10-animation-bootcamp-1/`,
run the loop census over the full file, and extend the
narration addendum for 8:33–25:52 (expected content per the
screen log: motion-path detail, handle-type work, student
Q&A). No claim in this run rests on the unharvested span.

## Harvest close-out (2026-11-06) — the item above is CLOSED

The whisper job finished (`ns10-whisper.done` on primo,
exit 0). `transcript.srt` (29,252 B, SHA-256
8646359f383cacbb44b1abd5faeb310ced47e53e365064845896170036f40550)
and `transcript.txt` (18,596 B, SHA-256
9d3d1a6fd1d1e4c4b2ba8bb56a6e85070332424c8738a68aef869c1f68f60274)
are copied into this run dir and
`repo/results/plan-10-animation-bootcamp-1/`, byte-identical
to the primo originals (hash-verified after transfer, cmp
run/results pair identical). This close-out supersedes the
"still running at report time" state recorded above; that
text stands as the report-time record.

- **Coverage:** 299 segments; last cue ends 25:47.840
  against the media's 1,551.53 s (25:51.53) — the closing
  3.7 s carry no cues. Near-complete, recorded as measured,
  not rounded up to full.
- **Full-file loop census** (normalized-segment-v1,
  `loop-census.txt` in this run dir): 299 segments, 12
  loop segments, **4.0% loop / 96.0% recoverable**,
  1 loop phrase (the instructor's rhetorical "right?",
  ×12 — a speech habit, not a silence hallucination). The
  harvested-span figure (87 segments, 0.0% / 100%) stands
  labelled by its span in OBSERVATION.md.
- **Addendum extended:** OBSERVATION.md's "Narration
  addendum" now carries a dated continuation (points
  8–17) for 8:33–25:52: motion-path colour code and
  spacing judgement, the handle-type worked fix (Vector
  one side / Free the other) and the keyframe-symbol
  vocabulary, the splining discipline's stated rationale,
  a deliberate keyed overshoot distinct from C-10-6's
  defect, and two new narration/screen tensions (swapped
  axis labels; mid-build frame numbers vs the finished
  file's UI). The expected student Q&A does **not**
  materialise in this span — instructor monologue only.
- **Claims:** no verdict changes. C-10-8 stands resolved,
  its "no separate homework" clause now covering the full
  file (the span closes on a next-session preview, not an
  assignment); C-10-3 / C-10-5 / C-10-7 gain narration
  corroboration. Detail and evidence: OBSERVATION.md
  continuation, points 8–17.
