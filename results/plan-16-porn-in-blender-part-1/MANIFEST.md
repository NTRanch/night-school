# Plan 16 — Capture Manifest

Plan: `repo/plans/16-porn-in-blender-part-1.md`
Item: "How to Make Porn in Blender (Part 1)", rule34video
video 4274245, creator Divinity Studio (via page description
links; page creator field blank — see INTAKE.md).

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-16/plan16-source-720p.mp4`
- Bytes: **432,178,972**
- SHA-256:
  **fd0277d2f95106cee7b4d198123319ca96eae0b2594e6dca685bd7e61b6f8e6b**
- Streams (ffprobe): video h264 1280×720 @ 30 fps, duration
  1668.067 s; audio AAC, duration 1668.074 s. Format duration
  **1668.074 s (27:48.07)** — matches the watch page's
  PT0H27M48S exactly.
- **Plan erratum:** the plan states duration 1:14:03
  (4,443 s). That is wrong by ~2.7× (see INTAKE.md). The
  task brief's chunking arithmetic (~4,443 s → 2 chunks)
  falls with it: at 1,668 s the media is UNDER the 3,600 s
  single-pass cap, so the chunked lane runs as a single
  pass (chunk map: one chunk, 0–1668.074 s).
- Rendition: **720p — the highest the page offers**
  (flashvars tokens exist for 360p/480p/720p only; no 1080p
  exists for this video). Total size established before
  download by a Content-Range probe: 432,178,972 bytes,
  matching the finished file exactly. An unsuffixed
  `4274245.mp4` token URL answered ranged probes with
  HTTP 200 and no Content-Range (range not honoured), so it
  could not be segment-verified and was not used.
- Integrity: full ffmpeg decode of the pinned file, rc=0,
  **0 error bytes** (primo detach `ns16-prep`, log on primo);
  decode spot-frames at t=800 and t=1600 also rc=0 during
  the download run (`ns16-dl`).
- Captured: 2026-11-06 (primo egress).

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/02/06/07
  route). Watch page fetched on BOTH egresses with a cookie
  jar (HTTP 200, 226,006 B; the sandbox's first attempt hit
  a transient site DB error, HTTP 503, and succeeded on
  retry; the primo copy is the page of record, kept at
  primo `plan-16/dl/watch-primo.html`).
- Egress probes (2026-11-06; numbers from the probe
  commands' own output):
  - primo, single-stream ranged 2 MiB from the 720p token
    URL: 2,097,152 B in 7.64 s ≈ **274,558 B/s**.
  - sandbox, ranged 2 MiB from the same (primo-fetched)
    token URL: **0 bytes** — the sandbox cookie/token set
    does not carry to the file host; primo-fetched tokens
    are not portable across egresses.
  - **Winner: primo, 16 parallel ranged segments** (the
    Plan 02-proven shape).
- Winning download: primo detach `ns16-dl`, `.done` reads 0.
  16 segments of 27,011,186 B (last 27,011,182 B); every
  segment size-verified on first attempt (no retries);
  segment byte sum 432,178,972 = Content-Range total;
  concatenation in numeric order (`seq 0 15` — the Plan 02
  glob-order lesson applied).
- Licence as seen: the watch page carries **no licence
  statement** for the video (full-text search: the sole
  "license" hit is the player config's opaque `license_code`
  token, as in Plan 02). Recorded AS SEEN: no explicit
  licence (no CC or other grant) is stated on the page. Per
  protocol the video is studied, never redistributed; no
  video file, transcript, or frame enters any shipped
  artifact.

## Audio

- An audio stream EXISTS (AAC; WAV extract mean volume
  −24.4 dB, max 0.0 dB). Silence census (screen only):
  172 silence-start events at −35 dB / 0.5 s across
  1,668 s — narration-shaped pauses, consistent with a
  narrated tutorial (page tag "sound"). Per the Plan 12
  lesson, the census is a screen, not a verdict; the
  transcription below is the verdict.

## Transcription (single-pass lane, per skill)

- whisper-cli (whisper.cpp 1.9.2, OpenChatCut bundled on
  primo), model ggml-large-v3-turbo, primo CPU. Media is
  1,668.074 s — UNDER the 3,600 s cap, so the lane runs
  single-pass (chunk map: one chunk, 0–1668.074 s). A first
  run at 2 threads, nice 19, was killed at 294 s of decoded
  audio for pace under wave contention (five concurrent
  whisper jobs; load average peaked ~40) and restarted at
  8 threads, nice 0 — the shipped transcript is the second
  run alone (primo detach `ns16-whisper2`, `.done` reads 0;
  the killed run's partial log is `ns16-whisper.log`,
  retained on primo as the friction evidence).
- Outputs (primo plan dir + this run dir): `transcript.txt`
  (11,878 B), `transcript.srt` (21,994 B), `transcript.json`
  (58,152 B).
- Stitch verify: 284 segments; last in-range end
  1667.36 s ≤ 1668.074 s — PASS with one flagged terminal
  segment ("Thank you.", ends 1668.36 s, +0.286 s over).
- Loop census (`loop-census.txt` in this run dir; rule
  normalized-segment-v1): `segments=284 loop_segments=15
  loop_share=5.3% recoverable_segments=269
  recoverable_share=94.7% loop_phrases=1`. The single loop
  phrase is "I'm not going to be exact" (hands passage).
- Tier: single-transcriber, **UNCONFIRMED**.

## Frames

- `frames/` (run dir): 14 grid frames every 120 s from t=0
  (g001–g014), 1280×720, from the pinned file.
- `frames60/` (run dir): 14 targeted frames at
  t = 60, 180, …, 1620 s.
- Canonical copies in the primo plan dir (`frames/`,
  `frames60/`).
