# Bloch candidate — Night School Plan 37

- origin_lane: ntranch
- content_label: nsfw
- source: Night School Plan 37 triage run, 2026-11-06
  (`~/workspace/night-school-20261105/runs/plan-37/` —
  INTAKE.md classification, OBSERVATION.md full-span log,
  TECHNIQUE.md claim record, PASS4-APPLICATION.md census)

## Lesson (a self-refuting tutorial is a classification, not a gap)

An item can wear the full furniture of a tutorial — title
in "How to draw X" form, numbered "(Step N)" cards, a
construction drawing — and still assert **no claim at all**,
because its own final card retracts the premise ("you
learned nothing ~ ♥", rule34video 3285544, creator
Telepurte; page description: "Haha u learnt nothing").

**Transferable rule:** in triage, read the item's own last
card and its page description before budgeting any
distillation. A source that disowns its claim leaves
nothing to test: Pass 3's correct output is "no build,
recorded why", and manufacturing a testable claim from the
visible fragments (here: two-sphere construction) in order
to have something to rebuild is inflation, not rigour.
This is the fourth named instance for the shelf census
(Plans 03 / 35 / 14 / 37): Tutorials-shelf placement
carries no presumption of instruction.

Artefact embodying the lesson: this run's TECHNIQUE.md
§"The claim" + the tutorial-marker checklist
(`runs/plan-37/TECHNIQUE.md`, this revision, 2026-11-06).

## D-1064 friction log

- **Primo contention (time cost, no workaround available):**
  at capture time primo carried ~8 concurrent whisper-cli
  jobs from sibling plan workers (load ≈27). This run's
  single whisper pass over **18 s** of audio took
  **114,642 ms** total per whisper's own timings block
  (encode 109,332 ms) — roughly 100× the audio's length in
  wall time for the encode alone. The result was unaffected
  (single segment, "*outro music*"), but a micro-plan's
  transcription should not queue behind full-length jobs:
  for sub-minute audio, a sandbox-local small-model pass or
  deferring to the audio-stream evidence (silence census +
  volume) would have carried the same verdict faster. The
  full pass was still run, per the brief, and is the record
  of record.
- **Scene-scan thresholds under-detect on white-card items
  (silent workaround, now explicit):** the standard 0.4
  scene threshold found only 1 of this item's transitions
  (cards are mostly white; the drawings are sparse black
  line-work). The record was rescued by dropping the
  threshold to 0.12 (3 cuts) **and** anchoring boundaries
  jointly to a 2 fps dense frame grid — segment boundaries
  are therefore stated at ±0.3 s in OBSERVATION.md rather
  than with false precision. Future micro-plans with
  card-based structure should start from the dense grid,
  not the scene scan.
- **Two samplers disagree by ~0.5 s at boundaries:** the
  per-second `-ss` stills and the `fps=2` grid land on
  different frames at segment edges (e.g. second 6 shows
  spheres in one sampler, the Step 2 card in the other).
  Resolved by classifying per second from BOTH grids plus
  the cut anchors, and recording the tolerance — noted so
  the next run doesn't burn time hunting a phantom
  discrepancy.
- **Contact-sheet tile reading misleads at first pass:**
  the 6×3 tile sheet initially read as if frames carried
  picture-in-picture layouts (step card + drawing in one
  tile); full-resolution per-second stills showed each
  frame is a single full-frame card or drawing. Verdict on
  the sheet: orientation aid only; never evidence. (Caught
  and corrected inside this run; no document cites the
  sheet for content.)
- No capture friction: sandbox egress took both the watch
  page and the file on the first attempt (page HTTP 200,
  224,172 B; file 3,416,637 B = Content-Range total), and
  primo's page fetch independently returned the identical
  byte count.

## Per-edit attribution rows

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| `repo/plans/37-how-to-draw-sexy.md` (LOCAL copy only) | Appended ERRATA line + Status updated to TRIAGE-CLOSED (JOKE) | Plan file now records creator Telepurte / uploader 69inch, verified duration, and the joke classification; duration claim unchanged (it was correct) | applied |
| Run documents (`runs/plan-37/`) | INTAKE.md appended with as-seen metadata + classification after capture; MANIFEST / OBSERVATION / TECHNIQUE / PASS4 / this candidate written | The pre-viewing claim list (H1–H5) is preserved unedited above the appended sections, so the before/after of the viewing stays auditable | applied |
| Capture scratch (`runs/plan-37/dl/`) | Probe artifacts (`probe.bin`, `headers.txt`, raw token-URL files, cookie jars) deleted at close | Token-bearing scratch does not persist beyond the run; the page of record (`dl/page.html`, per programme precedent) and the pinned media remain | applied |
