# Bloch candidate — Night School Plan 08

- origin_lane: ntranch
- content_label: nsfw
- source: Night School Plan 08 (Eviction — DevLog Episode #1,
  DivinityStudio, rule34video 4601875) —
  runs/plan-08/OBSERVATION.md §§2/5/6, TECHNIQUE.md T-3/T-7,
  REBUILD-DIFF.md Df-2/Df-3/Df-7.
- artefact: runs/plan-08/OBSERVATION.md + TECHNIQUE.md
  (this run's working tree, 2026-11-06; results copies at
  repo/results/plan-08-eviction-devlog-1/ in the same tree).

## Lesson (the narration filter, measured)

A working solo dev's devlog is evidence of **outcomes, not
method** — and this is measurable, not impressionistic.
Across an 88.8-minute episode, recoverable narration totals
≈ 5.6 minutes (≈ 6%): a spoken intro (premise, roadmap,
scope) and a one-minute render review. The remaining ~94%
is sped-up work footage under music, from which the estate
transcription lane recovered no speech (loop census: 79.9%
of 204 transcript segments are repetition loops). The
narration that does exist contains **zero problem
statements**: no failure, no fix, no scope call is narrated
anywhere. And at review time the dev cannot reconstruct his
own ~50 minutes of lighting/compositor iteration: "I don't
remember what I did, but I think I added more point lights
near her face" — said one minute after doing it, about a
rig the screen shows to be spot lights, with his render
count ("four or five") corrected by his own file counter
(test_render_005).

Portable rules:
1. **Process knowledge does not survive in devlog format.**
   If a programme needs its method transferable — to a
   second agent, a future self, a study programme — the
   decisions must be recorded contemporaneously, in writing,
   at the decision points. Retrospective narration will
   contain intent (before) and judgement (after), never
   method (during).
2. **A devlog's narration timestamps map its author's
   idle moments, not its work.** Narration appears exactly
   where hands are stopped (before starting; while renders
   display). Any study of devlogs should budget its
   extraction accordingly: premise and verdicts from the
   audio, method only from the screen, and problems from
   neither.
3. The counterfactual is the estate's own overhead, priced:
   written briefs, gate records, and provenance-first
   numbers are what it costs for "what did we do and why"
   to have an answer other than this dev's honest shrug.

## Friction log (D-1064 — yes, three items)

1. **rule34video `get_file` 403 gate is UA+Referer, not
   cookies.** The 1080p token URL returned 403 (15 B) from
   both egresses, with and without the page load's cookie
   jar; adding the browser User-Agent **and** the watch
   page as Referer cured it instantly (206 via CDN 302).
   Cost: ~10 minutes of probing across two egresses. The
   next agent should send UA+Referer on the first attempt;
   prior manifests emphasise the cookie jar, which was not
   the operative pair here. (Sandbox page fetch also failed
   outright this run with the site's own 503 database
   error; primo egress served the page.)
2. **Stitch verify can FAIL on loop overshoot alone.** The
   stitcher's verify rule (last segment end ≤ duration)
   failed (5350.92 vs 5329.984) purely because whisper
   stamps repetition loops in exact 30.00 s blocks that
   run past the media end. The transcripts are still valid
   records — every substantive segment ends in-media — but
   the next agent should expect this failure mode on
   music-heavy sources and check *which class* of segment
   overshoots before doubting the stitch.
3. **Sheet-scale frame reads mislead on versions and
   small text.** At contact-sheet scale I initially read
   "Blender 3.2.0 LTS" and missed the characters' names,
   file paths, and light types entirely; the native frames
   (5.2.0 LTS; E:\Eviction\geo\…; Spot lights) reversed
   two of those reads. For devlog/process studies, pull
   native frames at structure-bearing timestamps *before*
   drafting the observation, not after.
