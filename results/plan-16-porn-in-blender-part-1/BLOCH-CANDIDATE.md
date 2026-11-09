# Bloch candidate — Plan 16 run

- origin_lane: ntranch
- content_label: nsfw
- origin: Night School Plan 16 study run ("How to Make
  Porn in Blender (Part 1)", rule34video 4274245, Divinity
  Studio), 2026-11-06.
- Artefacts: `runs/plan-16/` (this run's files, this repo
  working tree, uncommitted at filing); canonical media on
  primo `~/.local/share/pax/night-school/plan-16/
  plan16-source-720p.mp4`, SHA-256
  fd0277d2f95106cee7b4d198123319ca96eae0b2594e6dca685bd7e61b6f8e6b.

## Candidate 1 — Plan-stated durations on this shelf are not data

**Lesson:** Plan 16's plan stated the video's duration as
1:14:03. The watch page states 27:48 in three places
(JSON-LD, info tab, player config) and the pinned file
probes at 1668.074 s. Every downstream number derived from
the plan's figure was wrong with it: the brief's chunking
arithmetic (4,443 s → 2 chunks; the real file is UNDER the
single-pass cap), the expected frame-grid density, and the
transcription budget. The same pattern is visible one plan
over: the watch page's related rail lists Part 2 at
1:01:10 while Plan 17's plan states 1:19:12 (unverified —
flagged for Plan 17's intake, not asserted).
**Rule:** at intake, a plan's duration is a claim, not a
fact: verify it against the watch page's own metadata
before any arithmetic (chunks, grids, budgets) is derived
from it, and file the erratum to the plan the moment the
page disagrees.
**Evidence:** runs/plan-16/INTAKE.md (erratum),
runs/plan-16/MANIFEST.md (pinned duration + probe),
repo/plans/16-porn-in-blender-part-1.md (errata stamp,
local copy).

## Candidate 2 — Watch-page file tokens are bound to the fetching egress

**Lesson:** The 720p token URL extracted from a page
fetched on primo returned **0 bytes** when requested from
the sandbox egress with the sandbox's own cookie jar, while
the same URL on primo delivered at 274,558 B/s
single-stream. The token is not a portable URL; it is a
capability issued to the session/egress that fetched the
page. A cross-egress retry loop would have burned the
whole capture window diagnosing a "dead link" that was
never dead.
**Rule:** fetch the watch page and the media from the SAME
egress. If a token URL answers 0 bytes / 403 on a different
egress than the one that fetched the page, re-fetch the
page on the working egress instead of retrying the file.
**Evidence:** runs/plan-16/MANIFEST.md (capture route,
both probes' numbers).

## Candidate 3 — Budget whisper by CPU-seconds per audio-second, not by the uncontended realtime figure

**Lesson:** The chunked-transcription skill quotes
~2.16× realtime for large-v3-turbo on primo CPU. Measured
this run under wave contention (five-plus concurrent
whisper jobs, load average peaking ~40): the model's true
cost is ≈7–9 CPU-seconds per audio-second at estate
settings, independent of thread count — a 2-thread nice-19
run decoded 294 s of audio in ~38 min and was killed; the
restart at 8 threads / nice 0 finished the 1,668 s file in
~50 min of wall time. Thread count buys wall-clock only
when cores are actually spare; nice level decides whether
they are.
**Rule:** before a transcription stage, estimate
wall time as (audio_seconds × ~8 CPU-s) ÷ cores the job
can realistically hold under CURRENT `ps` contention, and
start at the thread count and priority the estimate
assumes — a low-priority "polite" start that must be
killed and restarted costs more than it saves.
**Evidence:** runs/plan-16/MANIFEST.md (transcription
block), primo detach logs `ns16-whisper.log` (killed run)
and `ns16-whisper2.log` (shipped run), runs/plan-16/
OBSERVATION.md (media block).

## D-1064 friction log (this run)

- **Cost time:** ~25 min — primo scripts written via
  heredoc through the `primo-ssh` wrapper arrived mangled
  (the first probe script failed with curl "blank argument"
  errors). Silent workaround caught in-run: write the
  script locally, `scp` it, execute the file — first-try
  success for all four later scripts (dl, prep, frames2,
  whisper2). Next agent: never heredoc a multi-line script
  through primo-ssh; scp is the route.
- **Cost time:** ~50 min — transcription contention
  (Candidate 3): one killed run, two renice escalations
  (19 → 15 → 8 → 0, each measured against the wave's own
  observed priorities: sibling jobs ran at nice 0/5/8/10/19
  simultaneously), one restart at higher thread count.
- **Forced a guess (declined):** the pose's REFERENCE is
  load-bearing in the narration (six-plus mentions) and
  appears in zero of 36 captured frames. Rather than guess
  its medium, it is filed as UNREADABLE 1 in OBSERVATION.md
  and the convergence row (R10) is scored on the method
  (reference-first), which all three creators share,
  not on the artefact.
- **Silent workaround caught:** the plan's own duration
  (Candidate 1) — had it been trusted, the run would have
  chunked a 27-minute file for a 74-minute expectation
  and reported a "truncated capture" that never happened.

## Per-edit attribution rows (plan errata, local copy)

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| repo/plans/16-porn-in-blender-part-1.md, header block | Errata stamp appended: duration of record 27:48 (page JSON-LD + info tab + ffprobe 1668.074 s), creator Divinity Studio, no-1080p note, SHOULD-BE-SEEN scope note | Plan text now carries the verified values beside the original claim, which is preserved for provenance | verified |
| runs/plan-16/INTAKE.md, duration section | Plan figure recorded as erratum with the three page-side sources | Intake and manifest agree byte-for-byte on 1668.074 s / 432,178,972 B / the pinned SHA-256 | verified |
| All other numbers in this run's reports | Traced to artifacts: segment sizes + Content-Range total (ns16-dl.log), decode rc + 0 error bytes (ns16-prep.log), census line (loop-census.txt), transcript segment ends (transcript.srt) | No number in the deliverables lacks a named artifact | verified |
| Any technique claim about Part 2's content | None made — lighting/render/post rows held as PART-2-PENDING on the creator's closing statement alone | The map's open rows are labelled, not filled | confounded (by design — the confirmation run is Plan 17) |
