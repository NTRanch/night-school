# Plan 13 — Capture Manifest

Plan: `repo/plans/13-porn-in-blender-beauty-pass.md`
Item: "How to make Porn in Blender - Recreating Beauty Pass" —
Divinity Studio (per the page's own support links; no presenter
named on the page), rule34video video 4307858.

## Pinned capture

- Canonical file (primo): `~/.local/share/pax/night-school/plan-13/plan13-source-720p.mp4`
- Bytes: **503,118,348**
- SHA-256: **e8de0b64de4b4d62251ee207e048e0e2c7c5c92a42b1e933daa2f335b6dc719f**
- Streams (ffprobe): video h264 1280×720 @30 fps, audio AAC;
  format duration 2058.346 s — the watch page states
  PT0H34M18S (2,058 s); the 0.346 s difference is container
  rounding, recorded not smoothed.
- **Packet-span check (Plan 05 lesson): PASS, not truncated.**
  Video packets 61,750 = 2,058.33 s × 30 fps exactly; max video
  pts 2058.300 s; max audio pts 2058.325 s — both streams span
  the full header duration. Decode probes at t = 100 / 600 /
  1200 / 1800 / 2040 s: rc=0, 0 error bytes, frames produced
  at every probe including the final minute.
- Rendition: 720p — the highest the page offers (flashvars
  tokens exist for 360p/480p/720p only; no 1080p rendition
  exists for this video). Total size established before
  download by a Content-Range probe: 503,118,348 bytes.
- Captured: 2026-11-06.

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/02/04/05/06
  route). yt-dlp was not attempted (prior plans proved it
  fails on this host class).
- Egress probes (2026-11-06):
  - sandbox: watch page returns **403 "Access denied"** (15 B)
    through the sandbox egress proxy — sandbox egress is dead
    for this host on this run.
  - primo: watch page intermittently returns **503** with a
    site-side body ("can't connect to database defined in
    /admin/include/setup_db.php: Connection refused") —
    roughly one request in three; retries land **200,
    222,388 B**. The 503 is the site's own backend flapping,
    not an egress block (same URL, same jar, alternating
    200/503 within one minute).
  - primo, single-stream ranged GET on the 720p CDN object:
    8,388,608 B in 9.47 s ≈ **0.89 MB/s**.
  - **Winner: primo** (sandbox unusable), 8 parallel ranged
    segments.
- Winning download: primo detach `ns13-dl`, log ends
  `DOWNLOAD_COMPLETE`. 8 segments of 62,889,794 B (last
  62,889,790 B); every segment size-verified on first attempt
  (no retries needed); concatenation in numeric order
  (`seq 0 7`); assembled size equals the probed total exactly.

## Licence

- Page-stated licence, verified firsthand at intake: **none
  stated.** Full-text search of the watch page (saved on primo
  as `dl/page.html` in the canonical dir) for "license" /
  "licence" / "creative commons" / "CC0" finds no licence
  statement for this video (sole hit: the player config's
  opaque `license_code` token). Recorded exactly as seen.
  Study-only posture: the tutorial is studied, never
  redistributed — no video file, transcript, or frame enters
  any shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06 on primo)

- Title: "How to make Porn in Blender - Recreating Beauty Pass"
- video_id 4307858; `video_models` empty; uploadDate
  2026-03-29; duration PT0H34M18S.
- Description, in full: "Support my Patreon/Subscribestar for
  more tutorials: https://www.patreon.com/divinitystudio
  https://subscribestar.adult/divinity-studio" — the series
  is presented under the **Divinity Studio** name; no personal
  name is stated on the page. (In-video corroboration: the
  presenter's Gmail tab reads divinitystudiox@… and the
  model's file path is `E:\Divinity Studio\chars\Grace\…`.)
- The recording itself is dated by its own taskbar clock:
  3:00 PM, 3/27/2026 at record start (OBS window, t=0:00) —
  recorded 2026-03-27, uploaded 2026-03-29.

## Transcription (chunked lane, per skill)

- Single-chunk lane: 2,058 s is under the 3,600 s cap, so no
  chunking (chunk map: "single pass").
- whisper-cli (whisper.cpp 1.9.2, OpenChatCut bundled on
  primo), model ggml-large-v3-turbo, primo CPU, 8 threads
  (nice 10; the box was shared with the parallel all-hands
  wave), 16 kHz mono WAV extracted from the pinned 720p file.
- Run: detached `ns13-whisper` on primo, rc=0 (`.done`
  read as evidence); whisper total compute 3,230,663 ms;
  wall time stretched by parallel-wave contention (up to
  six whisper jobs sharing the box; load peaked at 27/16).
- Stitch verify: single chunk — 507 segments, first at
  00:00:00, last end **00:34:17.72** (2,057.72 s ≤ the
  media's 2,058.35 s) — full coverage, nothing to stitch.
  Language detected: en.
- Loop census (rule normalized-segment-v1, threshold >8):
  segments=507, loop_segments=13, **loop_share=2.6%**,
  recoverable_segments=494, **recoverable_share=97.4%**,
  loop_phrases=1. The one loop phrase ("…what's going on in
  the middle of the night", ×13) is confined to
  **00:30:31.7–00:30:46.7**, a provably silent stretch of
  Glare tuning (neighbouring real speech at 30:20 and
  31:13 is intact) — a silence hallucination; no spoken
  content is lost to it.
- Files: `transcript.txt` (12,048 B), `transcript.srt`
  (30,192 B), `transcript.json` (94,368 B) — primo
  canonical dir, copied into this run dir byte-size-equal.
- Tier: single-transcriber, **UNCONFIRMED**.
