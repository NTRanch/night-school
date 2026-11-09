# Plan 20 — Capture Manifest

Plan: `repo/plans/20-bonnie-tutorial.md`
Item: "Bonnie DoggyStyle Tutorial", rule34video video 4283510.
Series: Plans 15 / 18 / 19 / 20 — one 2021-03-19 SFM sitting
(`tutorial.dmx`), four published instalments. This instalment is
the sitting's FIRST segment (taskbar 11:26 AM → ~11:39 AM on
19/03/2021, immediately before Plan 19's 11:40 AM start).

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-20/plan20-source-720p.mp4`
- Bytes: **176,893,139** (matches the Content-Range total probed
  before download: 176,893,139 for the 720p rendition; 360p/480p
  tokens also exist on the page).
- SHA-256:
  **984e206fc28111a70ecb4976100fcea78bd1e573ddc9d73a310bcf4213fa553b**
  (identical on the sandbox assembly and on primo after transfer).
- Streams (ffprobe): video h264 1280×720 @ 30 fps, **21,732
  frames**; audio AAC stereo 44.1 kHz. Format duration
  **724.400 s (12:04.40)** — matches the watch page's JSON-LD
  duration PT0H12M04S (724 s). **Plan erratum (fourth duration
  error in this series):** the plan states **51:08 (3,068 s)**;
  the page and the file both say 724 s. The plan overstates the
  artefact ~4.24×. Errata filed to the LOCAL plan copy only.
- Packet-span check (Plan 05 lesson): first video pts 0.000,
  last video pts 724.333 + 0.033 frame duration = 724.367 ≈
  format duration 724.400 (audio tail) — no truncated-rendition
  gap. Frame-count check: 21,732 / 30 fps = 724.4 s. Consistent.
- Decode verification: full ffmpeg decode to null, exit 0, zero
  error bytes (primo `records/decode.log`: `decode_rc=0
  errbytes=0`).
- Captured: 2026-11-06. Rendition: **720p — the highest the page
  offers** (flashvars tokens for 360p / 480p / 720p only;
  `video_alt_url2_hd: '1'`).

## Capture route (what actually worked)

- Egress probe, both routes: the watch page fetched **200 from
  the sandbox** (218,916 B) while primo returned **503** (93 B —
  the origin's DB-error body). Reverse of Plans 15/19 (primo won
  there). The page was therefore fetched on the sandbox.
- The `get_file` rendition URLs are **session-bound**: tokens
  issued to the sandbox page fetch returned 403 from BOTH
  egresses when used without the matching cookie jar, and 403
  from primo even with Plan 15's sibling jar. With a fresh
  cookie jar saved by the same sandbox fetch, the 720p URL
  answered 302 → 206 with the full Content-Range.
- Download ran as 8 parallel ranged segments **on the sandbox**
  (every segment size-verified: 7 × 22,116,643 B + 1 ×
  22,116,638 B) before numeric-order concatenation;
  concatenated bytes equal the probed total exactly; the file
  was then transferred to the primo canonical path and its
  SHA-256 re-verified there (identical).
- yt-dlp was not attempted (prior plans proved it fails on
  this host class).

## Licence as seen

The watch page carries **no licence statement** for the video;
full-text search finds only the player config's opaque
`license_code` token (`$611881720187049`) — a player key, not a
content licence. Recorded AS SEEN: no explicit licence stated.
Per protocol the video is studied, never redistributed; no
video file or frame enters any shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06 on
the sandbox, saved as `dl/page-sandbox.html` in the primo plan
dir; the page carries session tokens and is not copied to
`results/`)

- Title: "Bonnie DoggyStyle Tutorial"
- video_id 4283510; uploader **Malikai Polk** (member 1242729 —
  the token payload and the page's author meta agree; same
  uploader as Plans 15/18/19); `video_models`: **Hstudios**;
  uploadDate **2026-03-10** (JSON-LD); duration PT0H12M04S;
  views 4,807; likes 20 at capture load (counts move; of their
  moment).
- Categories (flashvars): 3D, Five Nights at Freddy's,
  Tutorials. Tags (flashvars, complete): `doggystyle position`,
  `pov`, `bonnie (fnaf)`, `sound`.

## Transcription (chunked lane, per skill)

- whisper.cpp 1.9.2 (`whisper-cli`), model ggml-large-v3-turbo,
  primo CPU; 16 kHz mono WAV extracted from the canonical
  capture (`audio.wav`). 724 s < the 3,600 s single-pass cap —
  chunk map: "single pass".
- Contention at launch: ~11 sibling whisper jobs programme-wide
  (load ≈ 30 on 16 threads). Per the brief's slice-ladder
  provision, three targeted slices were transcribed FIRST on
  the same lane (nice 19, `-t 1`, detach `ns20-slices`):
  A = 0–150 s, B = 280–450 s (rig-setup span), C = 560–724 s
  (tail). The full pass runs behind them on the same detached
  chain (`ns20-whisper`, `-t 2`). Coverage is recorded honestly
  in OBSERVATION.md §1; the census runs only if the full
  transcript completes.
- Tier: single-transcriber, UNCONFIRMED; the screen governs.

## Analysis artifacts (numbers in this run's documents trace
to these)

- `records/ffprobe.txt`, `records/packet-span.txt`,
  `records/decode.log` (primo plan dir + copies in this run's
  `records/` where pulled).
- `frames/` — 24 grid stills @30 s (640 px) + 12 grid stills
  @60 s (native 1280×720) in this run dir; full sets on primo.
