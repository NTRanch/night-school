# Plan 05 — Capture Manifest

Plan: `repo/plans/05-stable-diffusion-nsfw-art-harry-heck.md`
Item: "Using Stable Diffusion to Create AI NSFW Art" —
Harry Heck, rule34video video 3257364.

## Pinned captures (primo `~/.local/share/pax/night-school/plan-05/`)

| Rendition | Bytes | SHA-256 | Video span | Role |
|---|---|---|---|---|
| 1080p `plan05-source-1080p.mp4` | 879,676,586 | `3ed1bbe4631b61425dd05822d501dea1ff9485852b2c615ab18c8c64ae433d41` | **packets end 2,679.02 s** (see defect note) | native-res frames, 0–2,679 s only |
| 720p `plan05-source-720p.mp4` | 880,142,013 | `28833aa42769dfcce45294290f66385d6c80d83d30b9b2587759d439baebd090` | **full: max video pts 4,730.77 s** | canonical video for the full span; second-half native frames |
| 360p `plan05-source-360p.mp4` | 427,528,659 | `e6c0cb5047bff93fdafe2f1846ac7a306e5477e2ce60be5d191cf1e5da045d97` | **full: max video pts 4,730.77 s** | canonical complete video; audio of record |

- Streams (1080p ffprobe): video h264 1920×1080 @60fps + AAC;
  header duration 4,730.78 s — the page states PT1H18M51S
  (4,731 s); the 0.22 s difference is container rounding.
- **Rendition defect (measured, not assumed):** the 1080p object
  the CDN serves is truncated in BOTH streams at 2,679.02 s
  (160,741 video packets present vs the header's claimed
  283,847 frames; AAC decode stops at the same point with
  "partial file" at offset 0x346ecf79) while its metadata claims
  the full 4,730.78 s. Assembled size equals the CDN's probed
  Content-Range total exactly and every segment size-verified,
  so the defect is in the served object, not in this capture.
  The 360p object is complete (video packets to 4,730.77 s),
  which is how the defect was isolated. Recorded as a capture
  finding: a size+hash pin alone would have certified a
  defective file; the packet-span check caught it. (The first
  decode-verify pass — frame decode at 6 timestamps reporting
  0 error bytes — was vacuous past 2,679 s: ffmpeg decoded
  nothing and errored silently. The verify that counts is the
  packet span + per-timestamp frame-production check.)
- Captured: 2026-11-06. A duplicate pin lives beside the media
  at primo `~/.local/share/pax/night-school/plan-05/MANIFEST.md`
  (written at close).

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/02/04/06/07
  route), terminal egress on primo.
- **HEAD trap confirmed again:** HEAD on the token `get_file`
  URL returned **403**; GET with the same page load's cookie
  jar (after a homepage warm-up hit) returns the 302 to the
  CDN (`us-cdn15-prem.boomio-cdn.com`) and works. Tokens are
  egress-bound.
- Egress probes (2026-11-06, on the real file):
  - primo, single-stream ranged GET on the CDN at 16:30:
    8,388,608 B in 0.9 s ≈ **9.31 MB/s**. Rate decayed over the
    session: parallel-segment aggregate ≈1.5 MB/s during the
    1080p download; a fresh-token probe at ~17:47 measured
    **0.22 MB/s** single-stream; three 720p segments stalled
    outright and were completed only after killing the stuck
    curls and re-probing with a fresh page load's token
    (re-probe-on-decay, per the binding lesson).
  - sandbox: page fetch works with its own warmed jar and the
    redirect resolves, but the CDN ranged download produced
    **no file in >300 s** — sandbox egress failed on the file
    itself (same outcome as Plan 04).
  - **Winner: primo**, all renditions.
- Downloads: 8 parallel ranged segments per rendition
  (detach `ns05-dl` / `ns05-dl360` / `ns05-dl720` +
  `ns05-fin720` finisher, `.done` = 0), every segment
  size-verified before concatenation in numeric order
  (maps: `dl/segmap*.txt`, `dl/seg-verify*.txt` on primo).

## Licence

- Page-stated licence, verified firsthand at intake: **none
  stated.** The only licence-shaped token on the page is the
  player config's opaque `license_code`. Posture per protocol:
  study only, never redistribute; no video file, transcript,
  or frame enters any shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06)

- Title: "Using Stable Diffusion to create AI NSFW Art -
  Harry Heck"; video_id 3257364; uploadDate 2024-01-21
  (JSON-LD); duration PT1H18M51S; views **66,982** at capture
  (plan intake: 66,968 on 2026-11-05 — counts move).
- Description: "Here is a comprehensive tutorial by Harry Heck
  on how to create NSFW AI Art with Stable Diffusion. Thank
  you for Harry Heck for giving permission to post this
  tutorial." Poster: Anime Nyan (plan + description).

## Transcription (chunked lane, per skill)

- whisper-cli (whisper.cpp **1.9.2**), model
  `/usr/share/whisper.cpp-model-large-v3-turbo/ggml-large-v3-turbo.bin`,
  primo CPU 12 threads; 16 kHz mono WAV chunked at 3,300 s
  into 2 chunks (map: `chunk-map.txt` in this run dir).
- **Audio of record is the 360p file's audio** (complete span).
  The 1080p file's audio truncates at 2,679 s with the video;
  a first transcription from it (536 segments, 0–2,679 s) is
  kept as `transcript-1080p-part1.*` and used only as a
  consistency cross-check for the shared span.
- Stitch verify: 612 + 1,082 = **1,694 segments** (incl. the
  `[SEAM]` marker at 3,300 s), last_end **4,728.92 s ≤
  4,730.78 s — PASS** (stitch.py output, this run).
- Loop census (`loop-census.txt`; rule
  normalized-segment-v1): stitched **1,687 counted
  segments, 178 loop segments = 10.6% loop share,
  recoverable 1,509 segments = 89.4%**. Per chunk: chunk1
  10.5% (64/612), chunk2 10.6% (114/1,074). The largest
  single loop is the chunk-1 hesitation repeat ("I don't
  know which one to add" ×27 while browsing the embedding
  shelf) — counted, not deleted, per the census rule.
- Consistency cross-check: the 1080p-audio transcript
  (536 segments, 0–2,679 s) and the 360p-audio chunk1 agree
  in substance across their shared span (same settings
  narrative, same quoted lines); neither is quoted against
  the other — the 360p stitch is the transcript of record.
- Tier: single-transcriber **UNCONFIRMED**; the study is
  screen-governed — every setting in OBSERVATION.md is tagged
  [SCREEN] / [SPOKEN] / [BOTH].

## Deliverables in this run dir

INTAKE.md · OBSERVATION.md · TECHNIQUE.md · PASS3-REBUILD.md ·
PASS4-APPLICATION.md · BLOCH-CANDIDATE.md · MANIFEST.md ·
transcript.srt/.txt (stitched, 360p audio) · chunk-map.txt ·
loop-census.txt · frames/ (20 grid + 9+9 targeted + native
frames and parameter crops) · AB/ (both loops' plates,
provenance records, census, contact sheets).
Copies: `repo/results/plan-05-sd-workflow/` (LOCAL only).

## Close-out (2026-11-06)

Passes 0–4 complete. A/B: 36 plates + provenance records in AB/
(Loop E 12, Loop T 12, Loop T repaired 12); census in PASS3-REBUILD.md;
gate in PASS4-APPLICATION.md; bloch candidate in BLOCH-CANDIDATE.md.
Loop E CLEAN 6/12, Loop T CLEAN 0/12 (both FAIL 0/12). Determinism:
byte-identical steady-state both loops; Loop E cold-first-run MAD 1.9074
(run1 f41ab9e6… vs steady-state 5ec1d968…, runs 2==3 byte-identical;
Loop T seed 51001 rerun byte-identical 71575809…). Own ComfyUI instance
(:8189) shut down at close-out; primo media masters and ab-out originals
retained under the primo plan-05 dir.
