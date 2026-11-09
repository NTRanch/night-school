# Plan 08 — Eviction, DevLog Episode #1 — Run Report

Run by: Pax subagent, night-school parallel lane
(agent/session 339becda-0bc1-4d14-b8de-5c8e53498b40),
claimed 2026-11-07 01:44 UTC, under the Owner's all-hands
Night School finish order (D-1073). EXECUTION-STATE.md was
not edited; the coordinator reconciles from this report.

## Outcome in one paragraph

Plan 08 is **complete, all five passes**, with its gate met
in the plan's own terms. The episode is not what the plan's
framing expected: it is an adult **comic** project's first
devlog (the correction is the creator's own description,
recorded at intake), and its 89 minutes contain ~5.6 minutes
of recoverable narration wrapped around a single
look-development session — two DAZ→Blender test scenes
iterated to two finished test renders. The Pass 3 diff
against the jam BUILD-PLAN produced 8 judged differences
(1 adopt, 2 adapt, 4 reject, 1 no-equivalent), and the
episode's most valuable datum is the dev's own sentence at
his render review: **"I don't remember what I did"** — the
narration-filter question the plan posed, answered by
measurement (79.9% of transcript segments are whisper loops
over music; zero problem statements in the narration).

## Gate outcomes (agent reads — the Owner's eye is the verdict of record)

| Gate item | Result |
|---|---|
| G-1 Diff document exists (episode sequence plan-shaped vs jam BUILD-PLAN) | PASS |
| G-2 Each difference judged adopt/reject with reason (Df-1…Df-8) | PASS |
| G-3 No technique claims beyond what the episode shows (C-1…C-8 carried with verdicts; C-2 untestable, C-8 licence leg unreadable, C-1 partial) | PASS |
| G-4 NSFW application: named candidate changes NC-1…NC-4 offered to next Strobe/Torogao programme plan | PASS |
| G-5 SFW translation named: SF-1 (risk order is domain-dependent), SF-2 (episode unit for audience-facing jam work) | PASS |

Detailed gate table: PASS4-APPLICATION.md.

## Key numbers (each traces to a run artifact)

- Capture: 1,902,231,620 B, SHA-256
  7a88eb29ac4aef7d97d5d5ff59db90f5245b528a40b696a5d820d254abc1e72c
  (MANIFEST.md; size = CDN Content-Range total exactly).
- Media: h264 1920×1080 30 fps + AAC, 5,329.966667 s.
- Transcription: 204 stitched segments; loop census 163
  loop / 79.9% loop share, 20.1% recoverable
  (records/loop-census.txt). Stitch verify FAIL on loop
  overshoot only (last end 5350.92 vs 5329.984; all
  substantive segments in-media) — recorded, not repaired.
- Substantive narration: 00:00–04:17 + 58:30–59:37 ≈ 5.6
  min ≈ 6% of runtime (chunks/chunk1.srt, chunk2.srt).
- Audio energy present in all 18 five-minute windows but
  one silent window (records/rms-5min.txt) — loops are a
  no-speech signature over a music bed.
- Wall clock: capture ≈ 7 min (8-segment parallel, primo);
  transcription 39:51 + 20:18 on the shared box.

## Eye items for the Owner (queued, not verdicted)

1. **The two final renders** (frames/native/t3540 =
   test_render_005.png portrait; the pool render in the
   final frame, grid sheet-08): do they read as
   keeper-grade character look-dev to your eye? This is
   the quality anchor for T-2/T-5 if the programmes borrow
   the episode unit.
2. **The pyramid-stud wall + pool set** (grid sheet-07/08,
   frames/native/t5040, t5280): a hand-built primitive set
   with a grafted water material — worth a look as a
   Strobe bathroom/pool scene reference pattern, or not.
3. **The premise adaptation pattern** (OBS §2 N1): the dev
   adapts a named live-action scene's premise openly
   ("borrow ideas from this"). Whether estate adaptation
   briefs should cite their reference works this explicitly
   is a judgement call the run surfaces but does not make.

## Friction (D-1064 — yes; full text in BLOCH-CANDIDATE.md)

1. get_file 403 cured by UA+Referer, not cookies (~10 min
   of probing; send UA+Referer first next time).
2. Stitch verify fails on whisper loop overshoot alone —
   check which segment class overshoots before doubting a
   stitch on music-heavy sources.
3. Contact-sheet-scale reads mislead (versions, light
   types, names); pull native frames at structure-bearing
   timestamps before drafting.

## Files

Run dir `~/workspace/night-school-20261105/runs/plan-08/`:
CLAIM.txt, INTAKE.md, MANIFEST.md, OBSERVATION.md,
TECHNIQUE.md, REBUILD-DIFF.md, PASS4-APPLICATION.md,
BLOCH-CANDIDATE.md, REPORT.md, transcript.txt/.srt,
chunks/, frames/ (sheet-01…08.jpg, native ×7), records/
(loop-census.txt, rms-5min.txt), dl/ (page.html, cookies).
Results copies: `repo/results/plan-08-eviction-devlog-1/`
(same doc set + frames + records).
Canonical media + lane artifacts: primo
`~/.local/share/pax/night-school/plan-08/`.
No commits, no pushes. Primo intermediates deleted
(≈ 2.24 GB: download segments + WAVs; MANIFEST.md cleanup).
