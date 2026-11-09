# Plan 11 — Capture Manifest

Plan: `repo/plans/11-porn-in-blender-light-aovs.md`
Item: "How to make Porn in Blender - Light AOVs" —
divinitystudiox (Divinity Studio), rule34video video 4316378.

## Pinned capture

- Canonical file (primo): `~/.local/share/pax/night-school/plan-11/plan11-source-720p.mp4`
- Bytes: **310,708,360**
- SHA-256: **0b4592fa085c066643c3da0e536b102af2878ed62299f1b327f979f2b57bbd61**
- Streams (ffprobe): video h264 1280×720, audio AAC; format
  duration 1,154.944 s — the watch page states PT0H19M15S
  (1,155 s); the 0.056 s difference is container rounding,
  recorded not smoothed.
- **Packet-span check (the Plan 05 lesson):** last video
  packet pts **1154.90 s** against the 1,154.944 s format
  duration — the served object is complete, NOT truncated.
  Decode verified: full-frame decodes at t = 60/300/600/900/
  1140 s each produced 0 error bytes (`decode-<t>.err` files
  beside the media on primo, all empty).
- Rendition: 720p — the highest the page offers (flashvars
  tokens exist for 360p/480p/720p only; **no 1080p rendition
  exists for this video**). Total size established before
  download by a Content-Range probe: 310,708,360 bytes.
- Captured: 2026-11-06.

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/02/04/06/07
  route). Token GET used the same page load's cookie jar
  after a homepage warm-up hit, on both egresses.
- Egress probes (2026-11-06, on the real file, ranged GETs):
  - primo, single stream: 4,194,304 B in 14.38 s ≈ **0.29 MB/s**.
  - sandbox, single stream: 4,194,304 B completed inside its
    probe window (≈0.3 MB/s class; the sandbox probe command
    backgrounded mid-run, so its exact wall time was not
    captured — recorded as a class, not a number).
  - **Winner: primo** (canonical home; per-connection
    throttling on this host makes parallelism the lever).
- Winning download: primo detach `ns11-dl`, `.done` file
  reads 0. 8 segments of 38,838,545 B (last 38,838,545 B —
  total divides evenly at this segment count: 8 × 38,838,545
  = 310,708,360); every segment size-verified before
  concatenation in numeric order (segmap: `dl/segmap.txt`
  on primo); wall time 18:43:16 → 18:51:43 PST ≈ 0.61 MB/s
  aggregate. Assembled size equals the probed total exactly.

## Licence

- Page-stated licence, verified firsthand at intake: **none
  stated.** Full-text search of the watch page (saved as
  `dl/page-sandbox.html` in this run dir; `page.html` on
  primo) for "license" / "licence" / "creative commons" /
  "CC0" finds no licence statement for this video (sole hit:
  the player config's opaque `license_code` token). Recorded
  exactly as seen. Study-only posture: the tutorial is
  studied, never redistributed — no video file, transcript,
  or frame enters any shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06)

- Title: "How to make Porn in Blender - Light AOVs";
  video_id 4316378; uploader **divinitystudiox** (member
  4570966, "Uploaded by" pill); uploadDate 2026-04-03
  (JSON-LD); duration PT0H19M15S; views **15,937** and
  likes **88** at capture load.
- Categories (flashvars): "3D, Tutorials, Final Fantasy
  vii, Blender"; tags "big breasts, sound"; video_models
  empty.
- Description names the mechanism **"Light Groups"** and
  links a YouTube mirror and the creator's Patreon /
  SubscribeStar (divinitystudio / divinity-studio).

## Transcription (chunked lane, per skill)

- Single chunk (1,154.944 s < the 3,600 s single-pass cap —
  no chunking): whisper-cli (whisper.cpp 1.9.2, OpenChatCut
  bundle on primo), model ggml-large-v3-turbo, primo CPU,
  16 kHz mono WAV extracted from the pinned file
  (`audio.wav`, 36,958,286 B). Run niced at 4 threads
  alongside two other lanes' whisper jobs (parallel-wave
  contention, recorded in PASS3-REBUILD.md's run record).
- Stitch verify (single chunk — span check in place of a
  stitch): 242 segments, first at 00:00:00,000, last ends
  00:19:13,680 against 1,154.944 s of media — narration
  covers the file to within the outro.
- loop_census: rule=normalized-segment-v1
  threshold_repeats=>8 segments=242 loop_segments=0
  loop_share=0.0% recoverable_segments=242
  recoverable_share=100.0% loop_phrases=0.
- Detach `ns11-tr` rc 0; wall time ~65 min at nice 10 /
  4 threads under parallel-wave contention (load 19–35).
  Transcript files: `transcript.srt` (15,332 B),
  `transcript.txt` (6,728 B), `transcript.json`
  (46,202 B) in this run dir; originals pinned with the
  media on primo.
- Tier: single-transcriber, **UNCONFIRMED**. The study is
  screen-governed — every setting in OBSERVATION.md is
  tagged [SCREEN]; narration appears only in the
  OBSERVATION addendum.

## Deliverables in this run dir

INTAKE.md · MANIFEST.md · OBSERVATION.md · TECHNIQUE.md ·
PASS3-REBUILD.md · PASS4-APPLICATION.md · BLOCH-CANDIDATE.md ·
transcript.srt/.txt · frames/ (39 grid + 4 targeted natives
+ 5 native-res crops + contact grid) · rebuild/
(build_aov_variant.py, probe_render.py, relight.py,
exr_to_png.py, template copies + AOV variant blends +
fingerprints/parameters, passes EXR, base comp + three
relight EXRs/PNGs, measurements JSON).
Copies: `repo/results/plan-11-porn-in-blender-light-aovs/`
(LOCAL only).
