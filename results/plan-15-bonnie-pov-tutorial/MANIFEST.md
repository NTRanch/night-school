# Plan 15 — Capture Manifest

Plan: `repo/plans/15-bonnie-pov-tutorial.md`
Item: "Bonnie Doggystyle Pov Tutorial Video" — uploader
Malikai Polk / model Hstudios, rule34video video 4297714.

## Pinned capture

- Canonical file (primo): `~/.local/share/pax/night-school/plan-15/plan15-source-720p.mp4`
- Bytes: **1,223,491,951**
- SHA-256: **9c7124c81444a4d77b6750b21ec873976d9695e30ead88f30115c87ab196c039**
- Streams (ffprobe at download, primo detach log `ns15-dl.log`):
  video h264 1280×720, 30 fps, 149,740 frames; audio AAC.
  Format duration **4991.333 s (1:23:11)** — matches the watch
  page's JSON-LD duration PT1H23M11S exactly. **Plan erratum:**
  the plan states 1:21:00 (4,860 s); the page and the file both
  say 4,991 s. Errata filed to the LOCAL plan copy only.
- Packet-span check (Plan 05 lesson): first video pts 0.000,
  last video pts 4991.267 + 0.033 frame duration = 4991.300 ≈
  format duration 4991.333 — no truncated-rendition gap.
  Frame-count check: 149,740 / 30 fps = 4991.3 s. Consistent.
- Decode verification: full ffmpeg decode to null, exit 0, no
  error output (primo detach `ns15-decode.done` = 0).
- Captured: 2026-11-06 (primo local ~18:56–19:10 PST).
- Rendition: **720p — the highest the page offers.** The
  flashvars token set for this video is 360p / 480p / 720p
  only; no 1080p token exists (page probed firsthand).

## Capture route (what actually worked)

- Watch page: sandbox egress **403** ("Access denied.", 15 B);
  primo egress **200** (216,358 B page, cookie jar saved at
  primo `plan-15/dl/`). Primo won the page.
- Rendition sizes established by cookie-jar ranged probes on
  primo (302 → `us-cdn09-prem.boomio-cdn.com`): 360p
  488,415,501 B; 480p 744,835,222 B; 720p **1,223,491,951 B**.
- Speed probe (primo, single stream, 20 MiB ranged GET):
  952,972 B/s average. Download ran as 8 parallel ranged
  segments on primo (detach `ns15-dl`), aggregate ≈1.46 MB/s;
  **every segment size-verified** before numeric-order
  concatenation; concatenated bytes equal the probed total
  exactly; sha256 above.
- yt-dlp was not attempted (prior plans proved it fails on
  this host class).

## Licence

- Page-stated licence: **none**. The watch page states no
  content licence (only the player config's opaque
  `license_code` token `$611881720187049`). Posture per
  protocol: study only, never redistribute; the capture stays
  on primo + this run dir.

## Page metadata of record (watch page fetched 2026-11-06 on primo, saved as `dl/page.html` in the primo plan dir)

- Title: "Bonnie Doggystyle Pov Tutorial Video"
- video_id 4297714; uploader **Malikai Polk** (member 1242729);
  `video_models`: **Hstudios**; uploadDate **2026-03-21**
  (JSON-LD); duration PT1H23M11S; views 6,655, likes 20 at
  capture load (counts move; of their moment).
- Categories (flashvars): 3D, Five Nights at Freddy's,
  Tutorials. Tags (flashvars, complete): `bonnie (fnaf)`,
  `doggystyle position`, `pov`.

## Transcription (chunked lane, per skill)

- whisper-cli (whisper.cpp 1.9.2), model ggml-large-v3-turbo,
  primo CPU; 16 kHz mono WAV chunked at 3,300 s into **2
  chunks** (map: `chunk-map.txt` in the primo plan dir).
  Launched at nice 19, `-t 2`, beside two foreign whisper jobs
  (Plans 11/13) that held the heavy slot — see the friction
  log in BLOCH-CANDIDATE.md.
- **Status at close-out: PARTIAL — see OBSERVATION.md §1
  for the exact covered spans (≈393 s of 4,991 s, 7.9%,
  chosen at the decisive segments) and the staged stitch
  (`dl/stitch.py`) + loop census (not run on a partial
  record).** Programme-wide whisper contention throttled
  all jobs to ~0.1× realtime; the full transcription
  continues detached on primo (`ns15-whisper`). Tier:
  single-transcriber, UNCONFIRMED; the screen governs.

## Analysis artifacts (numbers in this run's documents trace to these)

- `records/scene-cuts.txt` (primo plan dir + copy here): 7
  hard cuts at threshold 0.4 — clusters at 1513.6–1520.3 s
  (desktop break: YouTube/Patreon) and 3269.3/3273.3 s
  (Audacity/VEGAS switch). The SFM spans are otherwise
  continuous screen recordings.
- `frames/` — 42 grid stills at 120 s spacing (native
  1280×720) + `frames/grid30/` 166 stills at 30 s spacing +
  targeted sets (`cuts1/`, `cuts2/`, `open/`, `tail/`) +
  native crops. Contact sheets: `frames/contact-sheet-grid.jpg`,
  `frames/grid30-sheet{1,2,3}.jpg`.
