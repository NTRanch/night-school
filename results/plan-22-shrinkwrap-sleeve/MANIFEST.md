# Plan 22 — Capture Manifest

Plan: `repo/plans/22-shrinkwrap-sleeve.md`
Item: "Tutorial: Shrinkwarp Sleeve [Blender]", KenFurFox,
rule34video video 3881849.

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-22/plan22-source-1080p.mp4`
- Bytes: **204,712,460**
- SHA-256:
  **5b10f95fbee4abb186be03a07072e79634d65bc843171ade0516567e681f8644**
  (sandbox capture and primo pin verified byte-identical by
  hash after transfer, 2026-11-06.)
- Streams (ffprobe): video h264 1920×1080 @ 60 fps, duration
  746.600 s; audio AAC stereo 48 kHz, duration 746.602 s;
  plus a tmcd data stream. Format duration **746.602 s
  (12:27)** — matches the watch page's JSON-LD PT0H12M27S.
- Rendition: 1080p — the highest the page offers (flashvars
  tokens for 360p/480p/720p/1080p).
- Integrity: full ffmpeg decode of the pinned file, rc=0,
  zero errors (sandbox, `dl/decode-errors.txt` empty).

## PLAN ERRATUM (confirmed by probe)

The plan states duration **2:31**. The page metadata says
12:27 and the probed file is 746.602 s. **The plan's 2:31 is
wrong**; the file governs. Recorded as a plan erratum in the
local plan copy only (see `repo/plans/22-shrinkwrap-sleeve.md`
errata note added by this run). This also falsifies the
"tiny file / single-modifier micro-tutorial" framing: it is
a 12.5-minute, three-modifier build (Shrinkwrap + Surface
Deform + Solidify).

## Capture route (what actually worked)

- Watch page fetched on the sandbox egress with a cookie jar
  (HTTP 200, 223,476 B, kept at `dl/watch.html`); the 1080p
  token URL was taken from that page's flashvars and fetched
  with a cookie-jar GET following the 302 (HTTP 200,
  204,712,460 B). Primo egress was probed first for the
  fleet-model search (SSH route healthy); the file route that
  landed was the sandbox's, first try; no HEAD-403 detour.
- First plain `scp` attempts failed ("Connection closed" —
  the sandbox's root ssh config lacks the primo route); the
  working transfer used `scp -F /home/hatch/.ssh/config`.
  Hash verified on primo after transfer (above).

## Licence (as seen)

- The watch page states **no licence** for the video itself.
- The subject asset's collection is named on screen "Horse
  Cock – **CC BY NC SA**" — that licence label attaches to
  the third-party asset used in the demo, as seen; it is not
  a licence for the video. Nothing from the demo (no mesh, no
  file) is used in the rebuild; the rebuild is clean-room
  from the distilled settings onto an estate model.
- Posture per protocol: study only, never redistribute; no
  video file or frame enters any shipped artifact.

## Audio

- An audio stream EXISTS (AAC stereo 48 kHz). Silence
  census (sandbox ffmpeg silencedetect, −35 dB / 0.5 s):
  **266 silence-start events** over 746.6 s — narration-
  shaped pauses, unlike a continuous music bed.
- Speech check: whisper.cpp large-v3-turbo on primo
  (nice −n 19, 2 threads, file-mediated as `ns22-whisper`)
  against `audio.wav` in the primo plan dir. **Verdict:
  speech EXISTS** — English narration by the creator across
  the video. Transcript: `transcript.txt` in this run dir is
  PARTIAL (21 segments, 0:00–3:47) — primo was saturated by
  sibling plans' transcription jobs and the ns22 job was
  left running; the completed transcript lands in the primo
  plan dir beside the media. Per the Plan 12 lesson, the census
  scoped the transcription; it did not replace it. (Sibling
  plans' transcription jobs were saturating primo during
  this run; the ns22 job was nice'd behind them and took
  correspondingly long — see BLOCH-CANDIDATE friction log.)

## Frames

- `frames/full/` — 149 frames at 5 s intervals, native
  1920×1080 (0–745 s).
- `frames/view/` — 960 px viewing copies (two extractions;
  the joined set covers 0–550 s; later times read from
  `frames/full/` and `frames/view/vb_*` (460–745 s)).
- `frames/axis/` — 30 frames at 1 s intervals over
  238–268 s (the Shrinkwrap panel setup).
- `frames/crops/` — native-res enlarged crops of every
  settings panel (crop_0041 Solidify, crop_0051/crop_0066
  Shrinkwrap, crop_0056 SurfaceDeform, axis_14/16/18/20).
