# Plan 36 — Capture Manifest

Plan: `repo/plans/36-dildo-drone-daz.md` — "How to Use Dildo
Drone Asset for Daz Studio", rule34video video 3352555,
creator **shadowyartsdirty** (as seen, below).

## Source-integrity probe (run FIRST, per brief)

Bounded control-vs-target probe, terminal egress only
(shell curl, per-egress cookie jars; the browser text-fetch
route was never used for this domain):

- **Control** = Plan 14's video 4293878
  (`/video/4293878/futa-tutor-futa-black-date-ep-1-2/`):
  - Sandbox: **200, 259,287 B**, correct title ("Futa Tutor
    & Futa Black Date Ep-1,2") — `dl/control-sandbox.html`,
    SHA-256 `fab3f93782b53d35…` (page hashes move with
    per-load tokens; size + title are the stable facts).
  - Primo: **200, 259,287 B**, correct title, first try.
  - Matches the brief's known control (200 / 259,287 B) exactly.
- **Target** = video 3352555 (slugged URL from the plan):
  - Sandbox: try 1 = 503 (93 B DB-fatal body, the origin's
    known flakiness), **try 2 = 200, 222,295 B, correct
    title** ("How to use Dildo Drone asset for Daz Studio",
    saved as `dl/target-sandbox.html`, SHA-256
    `848aad96be17ec80…`), try 3 = 503. Record:
    `records/route-log-sandbox.txt` (the on-disk log is the
    evidence of record — see BLOCH-CANDIDATE.md on the
    contradictory background-handoff text).
  - Primo: **200, 222,295 B**, correct title, first try
    (primo `dl/page-primo.html`, SHA-256 `c4b8fcb4d331219a…`;
    size identical to sandbox, hash differs by per-load
    tokens, as expected).
  - Slug-less variant `/video/3352555/` (sandbox): 404,
    384 B, SHA-256 `fd562038072a7a48…` — the origin's
    standard 404 shell. This is a property of the slug-less
    form, **not** of the target: the slugged target serves
    200 on both egresses.
- **Verdict: SOURCE FOUND.** The Plan 29/30/25
  SOURCE-NOT-FOUND close does **not** apply: the target does
  not 404 — it serves, control-proven, on two independent
  egresses. The run proceeded to full capture.

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-36/plan36-source-720p.mp4`
- Bytes: **67,884,878** (established before download by a
  Content-Range probe on primo: `bytes 0-0/67884878` for
  the 720p rendition; the concatenated file equals it
  exactly).
- SHA-256: **72b62b81fcb71954fa08de94c2649cf2faae4b1fe7c358066d4dc00545c007b3**
- Streams (ffprobe, primo `records/ffprobe.txt`): video
  h264 High 1282×720 @ 60 fps, 15,950 frames, 1,828,807 b/s;
  audio AAC LC 48 kHz stereo, 203,646 b/s. Format duration
  **265.833 s (4:25.83)**.
- Duration verdict: the plan's stated **4:26 VERIFIES** —
  page JSON-LD `PT0H4M26S` (266 s) and the file's 265.833 s
  agree to container rounding (0.167 s). This corpus's
  durations are unreliable in general; this one is exact.
- Rendition: **720p — the highest the page offers**
  (flashvars tokens exist for 360p / 480p / 720p, plus a
  bare `3352555.mp4` token that answered 200 without a
  Content-Range and was not taken; the named 720p rendition
  is the pinned one).
- Decode verification: full ffmpeg decode to null, rc=0,
  zero error output (primo detach `ns36-dl.log`).
- Captured: 2026-11-06 (primo local ~21:38–21:39 PST).
  Download: primo detach `ns36-dl` (.done reads 0), 4
  parallel ranged segments (16,971,219 B ×3 +
  16,971,221 B), every segment size-verified on first try
  before numeric-order concatenation.

## Licence as seen

- Page-stated licence: **none stated.** Full-text search of
  the watch page finds only the player config's opaque
  `license_code` token (`$611881720187049`) — a player key,
  not a content licence (same posture as Plans 01/14/15/34).
  Recorded exactly as seen. Study-only posture per
  protocol: studied, never redistributed — no video file,
  transcript, or frame enters any shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06,
sandbox + primo, saved as `dl/target-sandbox.html` in this
run dir and `dl/page-primo.html` on primo)

- Title: "How to use Dildo Drone asset for Daz Studio"
- video_id 3352555; creator **shadowyartsdirty** —
  JSON-LD description: "The video was made and recorded by
  shadowyartsdirty"; flashvars `video_models`:
  `Shadowyartsdirty`; member ID 1244159 (the same creator
  as Plan 34). The plan's creator field was blank
  ("category listing shows none"); recorded as seen here.
- uploadDate **2024-03-24** (JSON-LD); duration PT0H4M26S;
  views **10,210**, likes **25** at capture load (counts
  move; of their moment).
- Categories (flashvars): `3D, Tutorials`. Tags (flashvars,
  complete): `drone, dildo, dildo machine, sound`.
- Description (JSON-LD, excerpt): the maker combined a
  drone and a dildo into one asset and recorded this
  tutorial on using it. (Full text in the saved page;
  paraphrased here, not shipped.)

## Transcription

- Single whisper pass (266 s « 3,600 s cap, per the chunked
  skill §3: under-cap media takes the single-pass lane):
  whisper-cli (whisper.cpp 1.9.2), model
  ggml-large-v3-turbo, primo CPU, nice 19, detach
  `ns36-media`. Record + census: see OBSERVATION.md §1.
  Tier: single-transcriber, UNCONFIRMED; the screen governs.

## Primo tenancy

- At run start: load ≈ 10.4–15.4 on 16 threads, ~24 GiB
  available (programme-wide sibling work live). This run's
  heavy stages are serialized under the `ns36-` detach
  prefix, one at a time, niced where CPU-bound. Nothing was
  played aloud (audio silence rule); audio handled as
  files/metrics only.
