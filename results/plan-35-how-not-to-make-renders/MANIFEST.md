# Plan 35 — Capture Manifest

Plan: `repo/plans/35-how-not-to-make-renders.md`
Item: "How not to make rule 34 renders in Blender" — recorded by
shadowyartsdirty, uploaded by shadowyartsporn, rule34video
3352570. **Pass 1 refuted the plan's premise** (see
OBSERVATION.md §1): the video is a behind-the-scenes Blender
posing recording set to music, not a failure catalogue.

## Pinned capture

- Canonical file (primo): `~/.local/share/pax/night-school/plan-35/plan35-source-720p.mp4`
- Bytes: **523,120,487**
- SHA-256: **a46e3bea3be1d50f660c00ba5d892d276efa415b2c3a49400fa6fc3cd1990c1e**
- Streams (ffprobe): video h264 1282×720, audio AAC; format
  duration 1228.567 s (20:28.6) — the watch page states
  PT0H20M29S (1,229 s); the 0.43 s difference is container
  rounding, recorded not smoothed.
- Rendition: 720p — the highest the page offers (flashvars
  tokens exist for 360p/480p/720p only; no 1080p exists for
  this video).
- Captured: 2026-11-06. A duplicate pin lives beside the media
  at primo `~/.local/share/pax/night-school/plan-35/MANIFEST.md`.

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/06/07 route).
  Total size established before download by a Content-Range
  probe: 523,120,487 bytes.
- Egress probes (2026-11-06; numbers from the probe commands'
  own output):
  - sandbox, single stream: 9,007,104 B in ~50 s ≈ 180 KB/s.
  - sandbox, 4 parallel ranged: 20,643,840 B in 32 s ≈ 645 KB/s.
  - primo, single stream: 4,284,416 B in 32 s ≈ 134 KB/s.
  - primo, 8 parallel ranged: 30,072,832 B in 30 s ≈ 1.00 MB/s.
  - **Finding: egress quality flipped mid-task** — the sandbox
    8-segment run decayed to ~170–240 KB/s aggregate after its
    probe and was killed at ~90 MB; the primo-native 8-segment
    run sustained ≈1.05 MB/s and won. Per-file-host empirics,
    re-probed at capture time, per the binding lessons.
- Winning download: primo detach `ns35-prdl`, rc=0 (its `.done`
  file reads 0), 12:05:43–12:11:34 PST. Every segment
  size-verified before concatenation; concatenated bytes equal
  the probed total exactly. yt-dlp was not attempted (prior
  plans proved it fails on this host class).

## Licence

- Page-stated licence, verified firsthand at intake: **none
  stated.** Full-text search of the watch page (saved as
  `dl/page.html` in this run dir) for "license" / "licence" /
  "creative commons" / "CC0" finds no licence statement for
  this video. Recorded exactly as seen. Study-only posture:
  the tutorial is studied, never redistributed — no video
  file, transcript, or frame enters any shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06, saved as `dl/page.html`)

- Title: "How not to make rule 34 renders in Blender"
- video_id 3352570; recorded by **shadowyartsdirty** (JSON-LD
  description + `video_models` field); uploaded by
  **shadowyartsporn** (member 1244159); uploadDate 2024-03-24
  (JSON-LD); duration PT0H20M29S; views 47,428 and likes 108 at
  capture load.
- Description: "Recorded by shadowyartsdirty — Behind the
  scenes of a romantic fan fiction comic I am working on
  featuring Gwen and Hellen Wheels in romantic situation"
  [sic] — the description describes the actual video; the
  plan's premise did not (OBSERVATION.md §5).

## Transcription (single-pass lane, per skill)

- whisper-cli (whisper.cpp 1.9.2, OpenChatCut bundled on
  primo), model ggml-large-v3-turbo, primo CPU; 16 kHz mono
  WAV; **single pass** (1,228.567 s < the 3,600 s cap; chunk
  map: "single pass"). Run nice'd at 4 threads under a tenant
  GPU-training job (one-heavy-job discipline); total whisper
  time 1,133,336 ms per its own timings block. The detached
  wrapper's `.done` file was not written (a mid-task relaunch
  artifact, recorded plainly); completion is evidenced by
  whisper's saved outputs + timings block in
  `ns35-transcribe.log` on primo.
- Stitch verify: single chunk, no seam. Last segment ends
  1228.28 s ≤ media duration 1228.567 s — **PASS**.
- Loop census (`loop-census.txt`; rule normalized-segment-v1,
  loop = repeated >8): **1,080 segments, 1,026 loop segments =
  95.0% loop share, recoverable share 5.0% (54 segments),
  3 loop phrases** ("keep me up at night", "and they try to",
  and one further lyric phrase). The audio is music: the
  recoverable 54 segments are song-lyric fragments. There is
  **no narration**; the transcript evidences the audio's
  nature, nothing else.
- Tier: single-transcriber, UNCONFIRMED; the screen governs
  (see OBSERVATION.md).

## Frames

- 31 grid stills at 40 s spacing (t = 5…1205 s), native
  1282×720, primo frames dir; copies in this run dir's
  `frames/` (g01–g31). Targeted native reads: g27 (t=1045,
  the video's only finished render), g31 (t=1205, Blender
  version/path/outliner), g10 (t=365, face close posing).

## Cleanup

- Deleted at task end: the killed sandbox download's partial
  segments (`dl/segments/`, ~90 MB, never hash-verified, never
  canonical), the primo download segments + probe files
  (regenerable from the pinned media / page), and the primo
  WAV intermediate (`work/audio.wav`). Kept: page/cookie/URL
  artifacts and both download scripts in `dl/` (primo copies
  in the primo dl dir), transcripts, frames, and all records.
