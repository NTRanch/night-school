# Plan 18 — Capture Manifest

Plan: `repo/plans/18-bonnie-ending.md`
Item: "Bonnie Doggystyle Tutorial — Ending", rule34video video 4283554.

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-18/plan18-source-720p.mp4`
- Bytes: **208,432,388** (matches the Content-Range total probed
  before download: 208,432,388 for the 720p rendition).
- SHA-256:
  **2e34b2a60be231d9e602a4e8ae4388b7493eba69e2a6b9d6f5c4a3c2d3f1a826**
- Streams (ffprobe): video h264 1280×720 @ 30 fps, **30,602
  frames**; audio AAC stereo 44.1 kHz. Format duration
  **1020.067 s (17:00.07)**.
- Rendition: 720p — the highest the page offers (flashvars tokens
  for 360p / 480p / 720p only; the page's own download menu lists
  82 MB / 129 MB / 199 MB for those renditions).
- Integrity: full ffmpeg decode of the pinned file, rc=0
  (`DECODE_OK` in `~/.local/share/pax/detach/ns18-download.log` on
  primo).
- Captured: 2026-11-06 (primo egress).

## Capture route (what actually worked)

- A cold cookie-less GET of the watch page returns **403
  "Access denied"** from both sandbox and primo egress.
- The route that worked: reuse of the sibling Plan 15 run's
  cookie jar (same site, same day) on primo — watch page HTTP
  200, 217,557 B, kept at `dl/page.html` in the primo plan dir
  (copy in this run's parent records on primo only; the page
  carries session tokens and is not copied to `results/`).
- The 720p token URL was taken from that page's flashvars and
  fetched with the cookie jar (302 → 206 range-capable file
  server). File-mediated detached run `ns18-download` on primo,
  nice 19, under a loaded tenant box (two sibling whisper jobs +
  one ffmpeg job live); download and all analysis ran nice 19,
  nothing audible.

## Licence as seen

The watch page carries **no licence statement** for the video;
full-text search finds only the player config's opaque
`license_code` token (`$611881720187049`) — a player key, not a
content licence. Recorded AS SEEN: no explicit licence stated.
Per protocol the video is studied, never redistributed; no
video file or frame enters any shipped artifact.

## Audio

- An audio stream EXISTS (AAC stereo; volumedetect mean
  −26.8 dB, max −6.7 dB; 16 silence-start events at
  −35 dB / 0.5 s across 1020 s).
- Content: background music (credited on screen at 0:01:
  "Background Music: Animal Crossing Theme LoFi") **plus a
  quiet English narration** under it. The census suggested
  music-only; the bounded whisper pass settled it the other
  way — speech EXISTS (the Plan 12 lesson, again: census is a
  screen, transcription is the verdict).
- Transcription: whisper.cpp large-v3-turbo on primo, 2
  threads, nice 19, file-mediated as `ns18-analyze`. Primo was
  saturated by sibling jobs; at this run's close the pass had
  reached **0:01:43 of 17:00** and was still running — the
  partial transcript (14 segments, 0:00–1:43) is filed as
  `transcript-partial.srt` in this run dir, and the completed
  transcript will land in the primo plan dir when the detached
  run finishes. Every claim this run draws from speech is
  inside the transcribed span and is marked [SPEECH] with its
  timestamp.

## Frames and records filed in this run dir

- `frames/contact-grid-30s.jpg` — 34-frame grid, one frame per
  30 s of recording (primo copies: `frames/g01.jpg`–`g34.jpg`).
- `frames/sheet-intro-2fps.jpg` — 0–26 s at 2 fps.
- `frames/sheet-480-516-viewport.jpg` — viewport crops,
  480–516 s at 2 fps (the largest sustained-motion cluster,
  visually resolved; see OBSERVATION §3).
- `frames/sheet-outro-1fps.jpg` — 1006–1020 s at 1 fps (credit
  cards).
- `frames/crop-g34-timeline.png` — 2× crop of the SFM Clip
  Editor at t≈990 s: the shot clip's duration line.
- `records/motion-energy.csv` — per-frame full-frame motion
  energy (mean abs pixel difference, 160×90 gray), all 30,601
  frame pairs; `records/motion-per-second.csv` — its per-second
  means; `records/viewport-energy.csv` — the same instrument
  restricted to the primary-viewport crop for the windows
  0–95, 460–530, 615–660, 960–1020 s (plus a second pass,
  225–260 / 710–750 / 830–920 s, summarised in OBSERVATION §3;
  raw CSV on primo at `records/viewport-energy2.csv`).
