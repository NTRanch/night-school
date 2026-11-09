# Plan 34 — Capture Manifest

Plan: `repo/plans/34-witch-poses-timelapse.md` — "Timelapse:
Making Some Witch Poses" (rule34video 3360585), creator
**shadowyartsdirty**.

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-34/plan34-source-720p.mp4`
- Bytes: **261,605,970**
- SHA-256: **7eabbadfe6612446b3f69942dc0005c31a77b419991b1bf316ceed8b550b268f**
- Streams (ffprobe): video h264 1282×720 @60 fps (54,264
  frames), audio AAC 48 kHz stereo; format duration
  **904.400 s (15:04.4)**.
- Duration verdict: the plan's stated **15:04 VERIFIES**
  against the file (page JSON-LD PT0H15M04S = 904 s; the
  0.4 s tail is container rounding, recorded not smoothed).
  This corpus's durations are unreliable in general; this
  one is exact.
- Rendition: 720p — the highest the page offers (flashvars
  tokens exist for 360p/480p/720p). Total size established
  before download by a Content-Range probe:
  bytes 0-0/261605970.
- Decode verification: full ffmpeg null decode rc=0, no
  error output. Packet span (video): first pts 0.000000,
  last pts 904.366667 — full span, no truncation.
- Captured: 2026-11-06.

## Capture route (what actually worked)

- Binding route honoured: terminal egress only, cookie jar
  per egress; the browser text-fetch route was never used
  for this domain.
- Sandbox egress: first watch-page GET returned the
  origin's known DB-fatal 503 (93 B, SHA-256
  a990dd3f8fdc4d79… — the same body Plan 29 dossiered);
  retries through the flakiness succeeded: 200, page saved
  locally as `dl/page-sandbox.html` (SHA-256
  4207a4f8bbbadbe5f50248d94758fab7da4cd947d378fd5c0ab737cab8a03b2b).
- Primo egress: watch page 200, 233,770 B on the first try
  (`dl/page-primo.html` on primo, SHA-256
  aa7306ef5e5b39df41388d030330ccf197676297baf9722120c13951b4f3815c),
  same title. No 404 occurred on either egress, so Plan
  29's control discipline was not needed.
- Download: primo detach `ns34-dl` (.done reads 0), 8
  parallel ranged segments of 32,700,747 B (last
  32,700,741 B); segments 3 and 5 needed one retry each
  after short reads (29,451,472 B and 31,548,624 B); every
  segment size-verified before concatenation in numeric
  order. Segments deleted at task end (intermediates).

## Licence as seen

- Page-stated licence: **none stated.** Full-text search of
  the watch page for licence terms finds only the player
  config's opaque `license_code` token (same posture as
  Plan 02). Recorded exactly as seen. Study-only posture:
  studied, never redistributed — no video file, transcript,
  or frame enters any shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06)

- Title: "Timelapse making some witch poses Patreon
  timelapse"
- video_id 3360585; creator **shadowyartsdirty** (member
  1244159; description: "Video by shadowyartsdirty";
  tooltip on the saved preset in-video also reads "Author:
  shadowyartsdirty"); uploadDate 2024-03-30; duration
  PT0H15M04S.
- Description: "A timelapse video where I make some sexy
  witch poses, the full video is on my patreon
  https://www.patreon.com/shadowyartsdirty" (link not
  followed).

## Transcription (bounded-slice verification)

- Audio census first: AAC track is LOUD (volumedetect
  mean −10.4 dB, max 0.0 dB) — silence could not be
  assumed, and "music only" could not be recorded from
  the census (census-is-a-screen discipline).
- Bounded whisper slices: 3 × 30 s at t=60/450/840
  (whisper-cli, ggml-large-v3-turbo, primo CPU, nice 19,
  detach `ns34-whisper`, .done reads 0; slices ran behind
  a saturated sibling whisper queue — slice files on primo
  at `audio-slices/slice-{60,450,840}.txt`).
  - t=60: "Thank you." (single fragment over music)
  - t=450: song lyrics ("With someone else's mind / He
    moves and touches like a treat … I just wanna kiss
    you, baby / Tough decision … We'll be right back.")
  - t=840: song lyrics, a different passage ("I'ma do my
    thing … My third eye … so divine")
- **Verdict: NO COMMENTARY.** The audio is music with
  vocals throughout the sampled span; the artist never
  speaks. The plan's SHOULD-BE-SEEN ("commentary absent")
  is confirmed by evidence, not by the census. Audio as
  files only; nothing was played aloud.

## Primo tenancy

- At run start primo carried ~7–13 sibling whisper-cli
  jobs (load ≈ 27–34 on 16 threads, ~14 GiB available).
  This run's heavy stages were niced (10–19), detached
  with the `ns34-` prefix, and run one at a time; Blender
  Workbench work is probe-scale and short.
