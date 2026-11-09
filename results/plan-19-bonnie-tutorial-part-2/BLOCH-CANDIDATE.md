# Bloch candidate — Plan 19 run

- origin_lane: ntranch
- content_label: nsfw
- origin: Night School Plan 19 execution run, 2026-11-06
  (artefact: rule34video 4283538, an NSFW-lane study source)

## Lesson

**A sustained single-act scene stays alive by rotating
the WORK, not the content: variation by channel-family
passes inside an unmoving frame.** The Bonnie series'
middle sitting (1177 s over a 20 s shot) varies nothing
about its destination — one shot, one act, one tableau,
zero cuts — and sustains itself entirely by rotating
which channel family is under work (flex → pelvis → feet
→ fingers → feet again), applying each pass across the
whole span, reviewing only at endpoints and by camera
flight, and pulsing finishing effort (a 1024-sample
refinement still) mid-session and at the close. The
invariants are half the grammar: cast, set, blocking,
layout, and playhead discipline never change in 84 sampled
stills. Estate form: this is exactly the shape D-1072's
C3 seeded variation mechanises (per-cycle bounded jitter
over eligible channels; contact/hand/identity channels
exempt) — the human author's rotation and the estate's
seeded rotation are the same rule at two levels of
automation, which is the mapping Plan 20's 60-second
aliveness test now gates.

Evidence pointers:
- `runs/plan-19/TECHNIQUE.md` §2 (rules V-1…V-8 with
  triggers and evidence), §4 (invariants)
- `runs/plan-19/OBSERVATION.md` §3 (23-event log, class
  tallies, 11.7 events/10 min), §4 (no-playback finding)
- `runs/plan-19/PASS3-REBUILD.md` §2 (grammar→mechanism
  mapping), §3 (aliveness criteria traced to Plan 01 /
  D-1072 measurements)
- Artefact: primo
  `~/.local/share/pax/night-school/plan-19/plan19-source-720p.mp4`,
  312,996,455 B, sha256
  4f52d73ae1059066ce1c86c7b8273974fdf448a55c5b75f52739a55687b26f92,
  revision = capture of 2026-11-06 (plan file
  `repo/plans/19-bonnie-tutorial-part-2.md`, local copy
  with errata appended this run).

## Secondary lesson (corroborating, not the candidate)

Series plan-file data failed a third time, in the opposite
direction: Plan 19's stated 1:34:19 overstates the real
1177 s artefact ~4.8× (Plan 18 understated ~28×; Plan 15
was off by 131 s). The intake rule proposed in Plan 18's
candidate (JSON-LD + ffprobe replace plan numbers in the
first hour; ≥2× discrepancy triggers a re-scope note)
would have caught all three. This run followed it and
re-scoped to the session world the brief pre-authorised.

## Friction report (D-1064 format)

- **What cost time / forced a guess / forced a workaround:**
  (1) Primo contention: 11 whisper-cli processes live
  (sibling plans' jobs) with load average ~30 on 16
  threads; this run's single-pass transcription crawled
  to ~1:38 of 1177 s inside the run window. Workaround
  (silent, in a successful run): three targeted slices
  were queued on the same lane AND the speech claims were
  restricted to the spans actually read (full-pass log
  0:00–1:38, which contained the load-bearing narration —
  the 20 s decision — by luck of ordering, not by
  design). (2) The timeline's 60.000 read at 105 s
  initially contradicted the series' 20.000 s record;
  resolving it cost a targeted-crop round before the
  transcript independently confirmed it as a narrated
  mid-session decision.
- **Per-edit attribution rows:**

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| Observation sampling (brief: grid ≤120 s) | 30 s grid (40 stills) + 19 targeted + 4 sheets = 84 stills | Caught the ≤225 s length change and the 86 s refinement phase; a 120 s grid lands ~10 points and misses both events' bounds | adopt census-then-focus as the session-world default |
| Transcription (skill lane, single pass) | Slices queued in parallel under contention; claims bounded to read spans | Speech evidence sufficient for C-02/C-03/V-8; slices B/C and the full pass still in flight at filing | **confounded** — contention vs lane throughput cannot be separated from this run's data; the bounding discipline, not the workaround, is the transferable part |
| Event counting | Counting rule stated before counting (OBSERVATION §3) | 23 events as a defensible lower bound instead of an impressionistic tally | adopt |

- **Artefact pointers for embodied lessons:** the grammar
  lives in `runs/plan-19/TECHNIQUE.md` (this run's
  revision, 2026-11-06); the test it feeds lives in
  `runs/plan-19/PASS3-REBUILD.md` §3; the mechanism it
  maps to lives in `runs/d1072-pattern-candidates/
  CANDIDATES-RECORD.md` (C3), revision = D-1072 landing,
  2026-11-06.
