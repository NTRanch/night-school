# Plan 14 — Capture Manifest

Plan: `repo/plans/14-futa-tutor-black-date.md` — "Futa Tutor &
Futa Black Date Ep-1,2", rule34video 4293878. **TRIAGE run**:
Pass 0 intake + sparse structural sampling only, per the plan's
own gate (classification recorded with evidence; the plan closes
at intake on a content classification — see INTAKE.md).

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-14/plan14-source-1080p.mp4`
- Bytes: **420,351,622**
- SHA-256: **33442c015c559ce46e752559861bfcf8dab5414109acc2e0f6f915b5c92ad0e8**
  (identical on the sandbox download and the primo copy —
  verified by sha256sum on both machines)
- Streams (ffprobe, `records/ffprobe.json`): video h264
  1920×1080, 60 fps, 42,988 frames, 4,517,333 bit/s; audio AAC
  stereo, 48 kHz, 163,546 bit/s, language tag `eng` on both
  streams. Format duration **716.480 s (11:56.48)** — the page
  states PT0H11M56S (716 s); the 0.48 s is container duration,
  recorded not smoothed. Handler strings as seen:
  "Mainconcept Video / MP4 Sound Media Handler"; muxed with
  Lavf62.3.100, video encoded Lavc62.11.100 libx264.
- Rendition: 1080p — the highest the page offers (flashvars
  tokens exist for 360p/480p/720p/1080p). Total size established
  before download by a Content-Range probe: bytes 0-1023 of
  420,351,622.
- Captured: 2026-11-06.

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/03/06/07/35
  route). Watch page fetched on the sandbox egress (HTTP 200,
  259,266 B, saved as `dl/page.html` in this run dir and at
  primo `plan-14/dl/page.html`).
- **Sandbox egress won the file**: 8 parallel ranged segments
  (detach `ns14-dl`, `.done` file reads rc=0), every segment
  size-verified before concatenation; concatenated bytes equal
  the probed total exactly; ~80 s wall. The verified file was
  then copied to the primo canonical path over the primo SSH
  route (~7 min for 420 MB through the tunnel proxy) and
  re-hashed there (identical, above).
- yt-dlp was not attempted (prior plans proved it fails on
  this host class).
- Primo tenant check before the batch (2026-11-06 ~18:41 PST):
  two whisper-cli transcriptions (Plans 08/10) and ComfyUI
  :8191 live; this run is network/ffmpeg-light and ran beside
  them. Nothing was played aloud at any point — audio was
  inspected as stream facts only (audio silence rule).

## Licence

- Page-stated licence, verified firsthand: **none stated.**
  Full-text search of the saved watch page (`dl/page.html`)
  for "license" / "licence" / "creative commons" / "CC0" finds
  only the player config's opaque `license_code` token
  (`$611881720187049`) — a player key, not a content licence.
  Recorded exactly as seen. Study-only posture: studied, never
  redistributed — no video file or frame enters any shipped
  artifact.

## Page metadata of record (watch page fetched 2026-11-06, saved as `dl/page.html`)

- Title: "Futa Tutor & Futa Black Date Ep-1,2" · video_id 4293878
- JSON-LD: description "Story by-Aneyasha's comic" +
  SubscribeStar promotion for **ntrgasm** ("MAKING BBC-NTR &
  FUTA-NTR Films … ALL CHARACTERS ARE 18+ AND CONTAINS NTR
  THEMES"); uploadDate **2026-03-25**; duration PT0H11M56S;
  views **62,368**, likes **132** (counts move; of their moment).
- Categories (page): **3D, Hentai, iwara, Tutorials** — the
  Tutorials placement is the shelf under census.
- Tags (page, flashvars, complete): futanari, futanari is
  bigger, futanari penetrating, futanari on male, futadom,
  futanari masturbation, futanari dominates male, futanari pov,
  submissive, captions, big breasts, big penis, big thighs,
  big black cock, big white cock, big cleavage, big areola,
  student, girlfriend, stealth sex, toilet, sound, sound
  effects, voice acted, voice acting, blacked, black cock,
  black skin, cum leaking, cumshot, porn with plot, moaning in
  pleasure, doggystyle position, missionary position. Every tag
  is a content tag; no tag names a tool, a technique, or
  instruction.
- `video_models`: "NTRgasm, WILDNTR". "Uploaded by" pill:
  **NTRgasm** (member 2907565). The plan's creator field was
  blank ("category listing shows none"); recorded as seen:
  uploader/creator brand **NTRgasm**, story credited in the
  description to **Aneyasha's comic**.

## Analysis artifacts (all numbers in this run's documents trace to these)

In this run dir:

- `records/ffprobe.json` — full stream/format probe of the
  pinned file.
- `records/scene-cuts-clean.txt` — 37 hard-cut timestamps from
  an ffmpeg scene scan at threshold 0.4 over the whole file
  (the raw log's showinfo header lines were stripped; the
  clean file is the record cited).
- `frames/grid_*.jpg` — 25 stills at 30 s spacing
  (t = 0…690 s plus t = 715 s), native 1920×1080, assembled as
  `frames/contact-sheet-30s.jpg`.
- `frames/boundary/` + `frames/boundary-sheet.jpg` — 13 stills
  at t = 335…390 s around the inter-episode cards.
- `frames/ep2open/` + `frames/ep2open-sheet.jpg` — 16 stills
  at t = 356…464 s covering Episode 2's opening structure.
- `frames/tail/` + `frames/tail-sheet.jpg` — 7 stills at
  t = 680…716 s covering the closing segment and end card.
- Total sampled stills: **61**, the whole observation base.
  Sampling is structural only, per the triage brief — no
  scene-by-scene content viewing was done or is recorded.
