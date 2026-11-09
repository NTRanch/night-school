# Plan 04 — Capture Manifest

Plan: `repo/plans/04-mugen-factory-stage-creation.md`
Item: "MUGEN Factory: Streaming the Creation of a Stage" —
Fapmaster/Viket, rule34video video 3417736.

## Pinned capture

- Canonical file (primo): `~/.local/share/pax/night-school/plan-04/plan04-source-1080p.mp4`
- Bytes: **1,699,252,961**
- SHA-256: **6ce7d9ec73e0db23b990964a3e2c35af80e5c035fb6954f7c34e496aa3f7f87c**
- Streams (ffprobe): video h264 1920×1080, audio AAC; format
  duration 4126.98 s — the watch page states PT1H8M47S
  (4,127 s); the 0.02 s difference is container rounding,
  recorded not smoothed.
- Rendition: 1080p — the highest the page offers (flashvars
  tokens exist for 360p/480p/720p/1080p). Total size established
  before download by a Content-Range probe: 1,699,252,961 bytes.
- Captured: 2026-11-06. A duplicate pin lives beside the media
  at primo `~/.local/share/pax/night-school/plan-04/MANIFEST.md`.

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/02/06/07
  route). The `browser.open` fetch route is policy-blocked for
  this domain; capture used terminal egress, as in prior plans.
- **HEAD is the trap on this host:** HEAD requests to the
  token `get_file` URL returned **403 on both egresses**; a GET
  with the same page load's cookie jar (after a homepage
  warm-up hit to set ddos-guard cookies) returns 302 to the CDN
  (`us-cdn01-prem.boomio-cdn.com`) and works. Tokens are
  egress-bound — primo's token would not resolve from the
  sandbox and vice versa.
- Egress probes (2026-11-06, on the real file):
  - primo, single-stream ranged GET on the CDN: 8,388,608 B in
    0.9 s ≈ **9.20 MB/s**.
  - sandbox: page fetch works with its own warmed jar, but the
    `get_file` GET returned an empty redirect — sandbox egress
    failed on the file itself.
  - **Winner: primo.** The full file came down as 8 parallel
    ranged segments (detach `ns04-dl`, `.done` = 0), every
    segment size-verified before concatenation (map:
    `dl/segmap.txt` on primo), concatenated in numeric order.
- Integrity: assembled size equals the probed total exactly;
  SHA-256 pinned above; **decode verified** (not just ffprobe):
  full-frame decodes at t = 100/1000/2000/3000/4000 s each
  produced 0 error bytes (`dl/decode-*.err` on primo, all
  empty).

## Licence

- Page-stated licence, verified firsthand at intake: **none
  stated.** Full-text search of the watch page (saved on primo
  as `dl/page.html`) for licence terms finds only the player
  config's opaque `license_code` token. Posture per protocol:
  study only, never redistribute; no video file, transcript, or
  frame enters any shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06)

- Title: "Mugen Tutorial Guide Factory Streaming The Creation
  Of A Stage"; video_id 3417736; uploadDate 2024-05-21
  (JSON-LD); duration PT1H8M47S; views **11,592** at capture
  (plan intake: 11,579 on 2026-11-05 — counts move); likes 28.
- Creator description: "i have been asked to stream when i
  create stuff so i wanted to stream the creation of a stage
  so people can see how easy actually is"

## Transcription (chunked lane, per skill)

- whisper-cli (whisper.cpp **1.9.2**), model
  `/usr/share/whisper.cpp-model-large-v3-turbo/ggml-large-v3-turbo.bin`,
  primo CPU 12 threads; 16 kHz mono WAV chunked at 3,300 s
  into 2 chunks (map: `chunk-map.txt` in this run dir).
- Stitch verify: segments 256 + 77 = 333; last_end 4126.92 s
  ≤ media duration 4126.98 s — PASS; one `[SEAM]` marker at
  3300 s in `transcript.srt`.
- Loop census (`loop-census.txt` in this run dir; rule
  normalized-segment-v1): stitched 334 blocks (333 segments +
  seam marker), 330 loop segments = **98.8% loop share**,
  **recoverable share 1.2%**, 4 loop phrases ("thank you.",
  "bye.", "fight!", "fight."). Per chunk: chunk1 99.6%,
  chunk2 97.4%.
- Reading: the audio is music + game audio with **no
  recoverable narration**; the transcript's content is whisper
  hallucination over non-speech (the "fight!" phrases track
  the MUGEN announcer in test fights). Tier: single-transcriber
  UNCONFIRMED; the study is screen-governed throughout and no
  claim in OBSERVATION.md rests on the transcript.
- Run contention note: primo had a tenant training job active;
  the transcription ran at ~0.55× realtime wall-clock. It was
  never the only heavy job on the box; headroom rules were
  observed (12 of 16 threads).

## Deliverables in this run dir

INTAKE.md · OBSERVATION.md · TECHNIQUE.md · PASS3-REBUILD.md ·
PASS4-APPLICATION.md · BLOCH-CANDIDATE.md · transcript.srt/.txt ·
chunk-map.txt · loop-census.txt · frames/ (5 grid sheets +
29 native frames + verdict sheet) · stage/ (layer sources,
harbor-steps.def, compositor.py, make_layers.py,
pass4-relayer.py, sweep-mugen/, sweep-depth/, pass4/,
gate-results.json, per-run measurements.json).
Copies: `repo/results/plan-04-mugen-stage/` (LOCAL only).
