# Plan 12 — Capture Manifest

Plan: `repo/plans/12-waifufactory-devlog-1.md`
Item: "WaifuFactory — Game Character Design [DevLog #1]",
rule34video video 4313470.

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-12/plan12-source-1080p.mp4`
- Bytes: **53,749,645**
- SHA-256:
  **1230744b77308a6d43c1c3863a5596202554550345de534740914b20a408a090**
- Streams (ffprobe): video h264 1920×1080 @ 60 fps, duration
  94.167 s; audio AAC stereo 44.1 kHz, duration 94.203 s.
  Format duration 94.203 s — the watch page states PT0H1M34S
  (94 s); container values recorded as probed, not smoothed.
- Rendition: 1080p — the highest the page offers (flashvars
  tokens for 360p/480p/720p/1080p). Total size established
  before download completed by a Content-Range probe:
  53,749,645 bytes, matching the finished file exactly.
- Integrity: full ffmpeg decode of the pinned file, rc=0, no
  errors. (The curl transfer itself exited 18 — early close
  after the final byte; the size match against Content-Range
  plus the clean full decode are the integrity evidence, not
  the curl exit code.)
- Captured: 2026-11-06 (sandbox egress). The primo pin's hash
  was verified against the sandbox copy byte-for-byte after
  transfer (identical, above; file-mediated copy `ns12-copy`,
  done rc=0). The manifest of record is this file in the run
  dir; the primo media dir holds the media + the transcript
  outputs.

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/02/06/07
  route). Watch page fetched on the sandbox egress with a
  cookie jar (HTTP 200, 226,588 B, kept at `dl/watch-sandbox.html`);
  the 1080p token URL was taken from that page's flashvars and
  the file fetched with a cookie-jar GET following the 302
  redirect. Primo egress was not needed — the file is small
  and the sandbox route landed first try; no HEAD-403 detour
  occurred.
- Licence as seen: the watch page carries no licence statement
  for the video; the page's own terms posture is the site's
  standard upload terms. Recorded AS SEEN: no explicit licence
  (no CC or other grant) is stated on the page. Per protocol
  the video is studied, never redistributed; no video file,
  transcript, or frame enters any shipped artifact.

## Audio

- An audio stream EXISTS (AAC stereo, mean volume −15.9 dB,
  max −0.1 dB). Silence census: exactly 1 silence-start event
  at −35 dB / 0.5 s across 94.2 s — a continuous bed, no
  narration-shaped pauses.
- Speech check: whisper.cpp large-v3-turbo run on primo
  (nice −n 19, 2 threads, file-mediated as `ns12-whisper`,
  done rc=0) against `audio.wav` in the primo plan dir.
  **Verdict: speech EXISTS** — a quiet English voiceover
  under the music bed (11 segments, 0:00–1:34). Transcript:
  `transcript.txt` in this run dir + the primo plan dir.
  The silence census above did NOT predict this; see
  INTAKE.md's audio verdict for the correction.

## Frames

- `frames/f001.jpg`–`f047.jpg`: dense extraction at 2 s
  intervals (fps=1/2), 1920×1080, from the pinned file.
- `dl/contact1.jpg`: 6×8 tile contact sheet of the same 47
  frames (agent viewing aid).
- Frame timestamps: frame N covers ≈ (N−1)·2 s to N·2 s.
