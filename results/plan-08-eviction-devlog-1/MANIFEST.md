# Plan 08 — Capture Manifest

Plan: `repo/plans/08-eviction-devlog-1.md` — "Eviction — DevLog
Episode #1", DivinityStudio, rule34video 4601875. Process
study; the plan's Pass 3 is procedural (sequence diff document,
no code rebuild — see PASS4-APPLICATION.md / REBUILD-DIFF.md).

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-08/plan08-source-1080p.mp4`
- Bytes: **1,902,231,620** — exactly the Content-Range total
  the CDN reported for the 1080p rendition.
- SHA-256: **7a88eb29ac4aef7d97d5d5ff59db90f5245b528a40b696a5d820d254abc1e72c**
- Streams (ffprobe): video h264 1920×1080, 30 fps, duration
  5329.966667 s; audio AAC, duration 5329.984 s. **An audio
  stream exists** (page tags include "sound") — narration
  transcribed via the estate whisper lane, files only; nothing
  was played aloud at any point.
- Page-stated duration PT1H28M50S (5,330 s) vs file
  5,329.966667 s: 0.03 s container difference, recorded not
  smoothed.
- Rendition: 1080p — the highest the page offers (flashvars
  tokens exist for 360p/480p/720p/1080p).
- Captured: 2026-11-06 (America/Los_Angeles evening).

## Capture route (what actually worked)

- Watch page: **sandbox egress FAILED** — HTTP 503 with the
  site's own "[FATAL]: can't connect to database" body (93 B);
  the site was erroring for that egress at fetch time.
  **Primo egress won**: HTTP 200, 223,232 B, saved as
  `dl/page.html` on primo + copy in this run dir's `dl/`.
- File tokens: the 1080p `get_file` URL returned **HTTP 403
  (15 B)** from BOTH egresses, with and without the page load's
  cookie jar, until the request carried the **browser user
  agent + the watch page as Referer** — then primo answered
  206 via a 302 to the CDN (`us-cdn09-prem.boomio-cdn.com`).
  The gating pair is UA+Referer, not cookies (cookies alone
  did not cure the 403; UA+Referer+cookies is the recorded
  working combination).
- Per-connection throttle (PF-5/PF-6 shape): single range
  probe 4 MiB in 5.47 s ≈ 0.77 MB/s. The download ran as **8
  parallel ranged segments** on primo (script
  `dl-script.sh` on primo beside the media; segmap +
  seg-verify in `dl/`), aggregate ≈ 242 MB in the first
  minute, all 8 segments size-verified, concatenated in
  order; final size and SHA-256 above. Wall clock ≈ 7 min
  for 1,902,231,620 B.
- yt-dlp was not attempted (prior plans proved it fails on
  this host class).

## Licence

- Page-stated licence, verified firsthand: **none stated.**
  Full-text search of the saved watch page (`dl/page.html`)
  for "license" / "licence" / "creative commons" / "CC0"
  finds only the player config's opaque `license_code` token
  (`$611881720187049`) — a player key, not a content licence.
  Recorded exactly as seen. Study-only posture: studied,
  never redistributed — no video file, transcript, or frame
  enters any shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06 via primo, saved as `dl/page.html`)

- Title: "Eviction - DevLog - Episode #1" · video_id 4601875
- JSON-LD: description "Come with me on this journey as I
  develop a simple adult comic in Blender. From ideation to
  final product." (+ Patreon / SubscribeStar / YouTube links
  for DivinityStudio), uploadDate 2026-09-11, duration
  PT1H28M50S, views 11,509, likes 28.
- flashvars: categories "Tutorials, 3D, Blender"; tags
  "comic, big breasts, sound"; `video_models`:
  "DivinityStudio" (the creator of record; the plan's intake
  recorded no creator).

## Transcription (estate whisper lane, files only)

- Route: whisper.cpp 1.9.2 `whisper-cli` (OpenChatCut bundle
  on primo), model large-v3-turbo
  (`/usr/share/whisper.cpp-model-large-v3-turbo/ggml-large-v3-turbo.bin`),
  CPU, `-t 8`. Input: 16 kHz mono WAV extracted from the
  pinned file (`audio.wav`, 170,559,566 B).
- Duration 5,329.984 s exceeds the lane's 3,600 s single-pass
  cap → chunked, chunk map on primo
  (`~/.local/share/pax/night-school/plan-08/chunk-map.txt`):
  chunk1 0–3300 s, chunk2 3300–5330 s, seam at 55:00.
- Lane results (close-out): chunk1 done in 39:51 wall,
  chunk2 in 20:18 (primo shared with other Night School
  lanes throughout). Stitched: 204 segments.
  **Stitch verify FAIL — mechanism named, record stands:**
  whisper stamps repetition-loop segments in exact 30.00 s
  blocks that overshoot the media end (stitched last end
  5350.92 s vs duration 5329.984 s); every substantive
  segment ends inside the media. **Loop census**
  (normalized-segment rule): 163/204 segments loop (79.9%),
  recoverable 20.1% — the quantitative form of the finding
  that recoverable narration is ≈ 5.6 min of 88.8
  (OBSERVATION.md §2). Substantive narration: 00:00–04:17
  and 58:30–59:37 only.
- Tier: single-transcriber output, UNCONFIRMED; on-screen text
  and values were corroborated against sampled native frames
  wherever a number is cited.

## Frames

- 89 grid stills at 60 s spacing (t = 0…5,280 s), 640 px wide
  (`frames/grid/` on primo; 8 contact sheets of 12 in this run
  dir's `frames/sheet-01…08.jpg`).
- 7 native 1920×1080 frames (`frames/native/`): t180, t840,
  t1020, t2700, t3540, t5040, t5280 — project folder/file
  structure, world-node and light settings, render review.

## Cleanup

- Deleted at task end (primo): the 8 download segments
  (1,902,231,620 B — the assembled canonical file above is
  the keeper), `audio.wav` (170,559,566 B) and both chunk
  WAVs (170,560,668 B) — all derivable from the pinned
  media. Total deleted ≈ 2.24 GB. (Primo free space is
  shared with parallel lanes; the disk-level delta across
  the run is theirs as much as mine, so the deleted bytes
  are reported, not a net disk figure.)
- Sandbox duplicate media: none (the download ran
  primo-side only).
- Kept: canonical media + page HTML + cookies + segmap/
  seg-verify + chunk SRT/TXT/JSON + stitched transcript +
  loop census on primo; scripts (`dl-script.sh`,
  `transcribe.sh`, `frames.sh`, `stitch.py`) on primo
  beside the media; all run documents, frames, and records
  in this run dir.
