# Plan 37 — Capture Manifest

Plan: `repo/plans/37-how-to-draw-sexy.md` — "How to Draw Sexy",
rule34video 3285544. **TRIAGE micro-plan run** (18 s source):
Pass 0 intake + full-span observation; classification JOKE
(see INTAKE.md / OBSERVATION.md). Gate = the 18 seconds fully
accounted for in the record.

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-37/plan37-source-1080p.mp4`
- Bytes: **3,416,637**
- SHA-256:
  **5f59de0307491bced44dd9c31e162a5b3a9865cae07c5924449cd863c2d5d7d0**
  (identical on the sandbox download and the primo copy —
  verified by sha256sum on both machines)
- Streams (ffprobe, `records/ffprobe.json`): video h264
  1920×1080 @ 60 fps, 1,087 frames, duration 18.117 s;
  audio AAC stereo, 48 kHz, duration 18.181 s. Format
  duration **18.181 s** — the page states PT0H0M18S (18 s)
  and the plan states 0:18. **Plan duration VERIFIED**
  (the 0.181 s is container/stream duration, recorded not
  smoothed).
- Rendition: 1080p — the highest the page offers (flashvars
  tokens exist for 360p/480p/720p/1080p). Total size
  established before download by a Content-Range probe:
  bytes 0-1023 of 3,416,637, matching the finished file
  exactly.
- Integrity: full ffmpeg decode of the pinned file, rc=0,
  **0 error bytes** (`dl/decode-errors.txt`, empty).
- Captured: 2026-11-06.

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/02/06/07
  route), terminal egress ONLY (curl with a per-egress
  cookie jar; no browser text-fetch was used — the Plan 25
  attempt-1 failure mode was avoided by construction).
- Watch page fetched on BOTH egresses, HTTP 200, **224,172 B
  on each** (sandbox copy saved as `dl/page.html` in this run
  dir; primo copy at primo `plan-37/dl/page-primo.html`).
- File download: **sandbox egress won** — single-stream GET
  of the 1080p token URL with the sandbox cookie jar,
  HTTP 200, 3,416,637 B in 3.20 s, size equal to the
  Content-Range total. (Contrast Plan 16, where sandbox got
  0 bytes from primo-fetched tokens: here page and file were
  both fetched on the same sandbox egress, and the tokens
  carried.) The verified file was copied to the primo
  canonical path over the primo SSH route and re-hashed
  there (identical, above).
- yt-dlp was not attempted (prior plans proved it fails on
  this host class).
- Primo tenant check before any primo work (2026-11-06
  ~20:45 PST): primo heavily loaded by sibling plan workers
  (~8 concurrent whisper-cli transcriptions, load ~27,
  ComfyUI on GPU). This run stayed light by design: one page
  fetch, one 3.4 MB copy, and one nice-19 whisper pass over
  18 s of audio (see Transcription). Nothing was played
  aloud (audio silence rule).

## Licence

- Page-stated licence, verified firsthand: **none stated.**
  Full-text search of the saved watch page (`dl/page.html`)
  for "license" / "licence" / "creative commons" / "CC0"
  finds only the player config's opaque `license_code` token
  (`$611881720187049`) — a player key, not a content licence.
  Recorded exactly as seen. Study-only posture: studied,
  never redistributed — no video file or frame enters any
  shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06, saved as `dl/page.html`)

- Title (as seen): "How to draw sexy" · video_id 3285544
- JSON-LD: description **"Haha u learnt nothing"**;
  uploadDate **2024-02-09**; duration PT0H0M18S; views
  **88,237**, likes **157** (counts of their moment).
- Categories (page): **Tutorials, 2D, Blender**
- Tags (page, flashvars, complete): sexy girl, animation,
  background music.
- `video_models`: **"Telepurte"** — the creator of record.
  "Uploaded by" pill: **69inch** (member 1086709). The plan's
  creator field was blank ("category listing shows none");
  recorded as seen: creator **Telepurte**, uploader 69inch.

## Transcription (single-pass lane)

- whisper-cli (whisper.cpp, OpenChatCut bundled on primo),
  model ggml-large-v3-turbo, primo CPU, nice-19, 2 threads;
  16 kHz mono WAV (`records/audio-16k.wav`); **single pass**
  (18.181 s, far under the 3,600 s cap).
- Result (`transcript.txt` / `.srt` / `.json` in this run
  dir): ONE segment spanning 0.00–18.08 s whose entire text
  is **"*outro music*"** — the transcriber's music tag, not
  speech. There is **no speech and no lyric** in the item.
- Corroboration: ffmpeg silencedetect (−35 dB, 0.5 s) finds
  **zero** silence events across the file — continuous
  audio; volumedetect mean −17.4 dB / max −1.2 dB; page tag
  "background music". Audio of record: **background music
  throughout, no narration**. The screen governs (protocol);
  nothing in the audio qualifies any visual finding.
- Whisper total time 114,642 ms per its own timings block —
  for 18 s of audio; the wall cost is primo contention from
  sibling workers' transcription jobs, recorded in the
  friction log (BLOCH-CANDIDATE.md).

## Analysis artifacts (all numbers in this run's documents trace to these)

In this run dir:

- `records/ffprobe.json` — full stream/format probe of the
  pinned file.
- `records/scene-cuts-clean.txt` — hard cuts at scene
  threshold 0.4: one cut (15.167 s). `records/scene-cuts-012.txt`
  — threshold 0.12 scan: cuts at 2.617 / 13.417 / 15.167 s.
  (Most transitions in this item are animated redraws and
  mostly-white card changes that fall below scene thresholds;
  segment boundaries in OBSERVATION.md are anchored jointly
  by these cuts and the dense frame grid, ±0.3 s.)
- `frames/f_001.jpg` … `f_036.jpg` — 36 stills at 2 fps
  (every 0.5 s), native 1920×1080, covering the whole span.
- `frames/sec/s_00.jpg` … `s_17.jpg` — 18 per-second stills,
  native 1920×1080 (the second-by-second evidence base).
- `frames/contact-sheet-1s.jpg` — 6×3 tile sheet of the
  per-second stills.
- Total sampled stills: **54**, the whole observation base.
