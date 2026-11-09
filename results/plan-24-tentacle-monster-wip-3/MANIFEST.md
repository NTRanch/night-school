# MANIFEST — Plan 24: Tentacle Monster WIP 3

- **Run date:** 2026-11-06 (PST) · **Outcome: CAPTURE-BLOCKED.**
  The source artefact was never acquired; Passes 1–4 could not be
  performed. No observation numbers, motion measures, or control
  grammar are reported, because none exist — fabricating them is the
  plan's explicit fail condition.
- **Source:** https://rule34video.com/video/3666838/tentacle-monster-wip-3/
  · Video ID 3666838 · Duration per plan 1:48 — **UNVERIFIED**
  (no file was acquired, so no ffprobe exists; the plan figure is
  neither confirmed nor refuted).
- **Creator / licence:** NOT SEEN. The watch page never served, so no
  creator name or licence statement was observed. The plan recorded
  no creator in its category listing; nothing further can be stated.

## What happened (all numbers traced to the artefacts named)

The origin's video pages were down for the entire capture window
(~20:01–22:56 PST, 2026-11-06) while its static/listing pages served
normally:

- Origin failure body (HTTP 503, 93 B), verbatim:
  `[FATAL]: can't connect to database defined in
  /admin/include/setup_db.php: Connection refused`
- Alternate failure: HTTP 404, 384 B shell page.
- Control probes: site homepage HTTP 200, 206,871 B (primo
  `home.html`, 20:01 PST); a *different* video page (plan-23's,
  ID 3881817) returned HTTP 200, 219,300 B exactly once (primo
  `p23.html`, 20:34 PST) and 503 on re-probe minutes later; a
  known-live video page (ID 4716262, from the site's own
  latest-updates listing) returned 503 in the same window. The
  distress is therefore origin-wide on video pages, not specific to
  this run's requests. Whether video 3666838 itself still exists
  cannot be determined from outside: its page never once succeeded.

## Capture attempts (of record)

| Route | Artefact | Attempts | 404 | 503 | Result |
|---|---|---|---|---|---|
| Primo loop 1 (45 s cadence, 50 min) | `dl/capture.log` sha256 `2b5a9ba9…f8` | 67 | 51 | 16 | exhausted |
| Primo loop 2 (25 s cadence, 2 h) | `dl/capture2.log` sha256 `7edbd95c…e0` | 284 | 199 | 85 | exhausted |
| Sandbox loops (detach-run ns24-sbx / ns24-sbx2) | `~/workspace/detach-runs/ns24-sbx*.log` | 32 | 30 | 2 | processes reaped by the sandbox (see BLOCH-CANDIDATE) |
| Manual probes (both hosts, fresh cookie jars, embed/search/ID-only URL forms, Wayback CDX) | session record in INTAKE.md | ~15 | — | — | no snapshot exists (Wayback: `archived_snapshots: {}`) |

Total primo loop attempts against the watch page: **351**, zero full
pages. Capture script of record: `dl/capture.py` sha256
`0214fa02…a4` (cookie-jar GET, parses `video_url`/get_file links,
would pin size + SHA-256 + ffprobe into `capture-info.json` on
success — that file does not exist because no download occurred).

## Standing retry

Loop 3 is RUNNING on primo (started 22:57 PST, 60 s cadence, 6 h
budget → ~04:57 PST): `~/.local/share/pax/night-school/plan-24/dl/`
(`capture3.log`, `capture3.done`). On success it writes
`plan24-source.mp4`, `watch-full.html`, `video-url.txt`, and
`capture-info.json` (size + SHA-256 + ffprobe) into that canonical
dir. A follow-up run should check `capture3.done` / `capture-info.json`
first and, if present, execute Passes 1–4 per the original brief.

## No shipped contamination

No video file, frame, or transcript exists in this run; nothing was
redistributed. Deliverables in this directory are the blocked-state
record only.
