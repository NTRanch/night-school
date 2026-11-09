# Plan 19 — Capture Manifest

Plan: `repo/plans/19-bonnie-tutorial-part-2.md`
Item: "Bonnie Doggystyle Tutorial — Part 2", rule34video
video 4283538.

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-19/plan19-source-720p.mp4`
- Bytes: **312,996,455** (matches the Content-Range total
  probed before download: 312,996,455 for the 720p
  rendition; 360p/480p tokens also exist on the page).
- SHA-256:
  **4f52d73ae1059066ce1c86c7b8273974fdf448a55c5b75f52739a55687b26f92**
- Streams (ffprobe): video h264 1280×720 @ 30 fps, **35,311
  frames**; audio AAC stereo 44.1 kHz. Format duration
  **1177.033 s (19:37.03)** — matches the watch page's
  JSON-LD duration PT0H19M37S exactly. **Plan erratum:**
  the plan states 1:34:19 (5,659 s); page and file both say
  1,177 s. The plan overstates the artefact ~4.8×. Errata
  filed to the LOCAL plan copy only.
- Packet-span check (Plan 05 lesson): first video pts
  0.000, last video pts 1176.967 + 0.033 frame duration =
  1177.000 ≈ format duration 1177.033 (audio tail) — no
  truncated-rendition gap. Frame-count check: 35,311 / 30
  fps = 1177.03 s. Consistent.
- Decode verification: full ffmpeg decode to null, exit 0,
  zero error bytes (primo detach `ns19-analyze.log`:
  `decode_rc=0 errbytes=0`).
- Captured: 2026-11-06 (primo egress). Sandbox egress
  returned 503 on the watch page; primo won, as in
  Plans 15/18.
- Rendition: **720p — the highest the page offers**
  (flashvars tokens for 360p / 480p / 720p only).

## Capture route (what actually worked)

- Route per Plan 18's precedent: the sibling Plan 15 run's
  cookie jar, reused on primo — watch page HTTP 200,
  219,008 B, kept at `dl/page.html` in the primo plan dir
  (the page carries session tokens; it is not copied to
  `results/`).
- The 720p token URL was taken from that page's flashvars.
  Single-stream ranged probe: ≈6.80 MB/s. Download ran as
  8 parallel ranged segments on primo (detach
  `ns19-download`, nice 19); **every segment size-verified**
  (7 × 39,124,557 B + 1 × 39,124,556 B) before
  numeric-order concatenation; concatenated bytes equal
  the probed total exactly; sha256 above.

## Licence as seen

The watch page carries **no licence statement** for the
video; full-text search finds only the player config's
opaque `license_code` token (`$611881720187049`) — a player
key, not a content licence. Recorded AS SEEN: no explicit
licence stated. Per protocol the video is studied, never
redistributed; no video file or frame enters any shipped
artifact.

## Audio

- An audio stream EXISTS (AAC stereo; volumedetect mean
  −30.4 dB, max −10.7 dB; 32 silence-start events at
  −35 dB / 0.5 s across 1177 s).
- Content: quiet English narration (present from 0:00 in
  the transcribed slices — e.g. the map-entity / lighting
  guidance at 0:39–1:06) — speech under the session, the
  Plan 18 pattern (census is a screen; transcription is
  the verdict).
- Transcription: whisper.cpp large-v3-turbo on primo,
  single pass (1177 s < the 3,600 s lane cap — no chunking;
  chunk map: "single pass"), 16 kHz mono WAV, nice 19,
  `-t 2`, file-mediated as `ns19-whisper`. Primo was
  saturated by sibling whisper jobs (11 whisper-cli
  processes live at check); the full pass was still
  running at this run's close (read span at filing:
  0:00–2:00, 15 segments, filed in this run dir as
  `transcript-partial.txt`), and three targeted slices
  (0–150 s, 460–580 s, 1080–1177 s; `ns19-slices`) were
  queued on the same lane and were still in flight at
  filing. Every claim this run draws from speech is
  inside the read span and marked [SPEECH]; tier
  single-transcriber UNCONFIRMED throughout. The
  completed full transcript lands in the primo plan dir
  when the detached run finishes.

## Frames and records filed in this run dir

- `frames/g01.jpg`–`g20.jpg` + `g-tail.jpg` — 60 s grid
  (primo copies in `frames/` of the primo plan dir).
- `frames/grid30/` — 30 s grid, 40 stills (12 pulled to
  this run dir; full set on primo).
- `frames/grid30-sheet.jpg` (primo) — contact sheet.
- `frames/targeted/` — timeline crops at 105/225/495 s
  (the shot-duration reads) + frames at the energy peaks
  and phase transitions (200–220, 470–580, 840–870,
  1160–1172).
- `frames/sheets/` — 2 fps sheets resolving the only two
  sustained-motion candidate windows (267–282, 388–404),
  the early still (92–110), and the tail (1150–1177).
- `records/motion-per-second.csv` — per-second full-frame
  motion energy (mean abs pixel difference, 160×90 gray),
  all 35,311 frames → 1,178 s rows.
- `records/viewport-per-second.csv` — the same instrument
  restricted to the primary-viewport crop (696×432 @
  360,56 → 174×108).
- `records/scene-cuts-04.txt` — scene-cut detector at
  threshold 0.4: **empty — zero hard cuts** in the file.
