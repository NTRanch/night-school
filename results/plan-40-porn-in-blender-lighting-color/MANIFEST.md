# Plan 40 — Capture Manifest

Plan: `repo/plans/40-porn-in-blender-lighting-color.md` — "How to Make Porn in
Blender: Basics — Lighting and Color Grading", rule34video.com video ID
**3213694**. Worker run 2026-11-06 (PST). LOCAL only; nothing pushed.

## Capture outcome (pinned artifact of record)

| Field | Value | Source artifact |
|---|---|---|
| Canonical media | primo `~/.local/share/pax/night-school/plan-40/plan40-source-1080p.mp4` | `ns40-dl.log` (primo detach dir) |
| Rendition | 1080p (`3213694_1080p.mp4`) | watch-page flashvars, `dl/page.html` |
| Bytes | **2,898,146,377** | script byte-count check `concat bytes=2898146377 want=2898146377`, `ns40-dl.log`; ffprobe `size=2898146377`, `ffprobe.txt` |
| SHA-256 | **0b3eebddcba33a6755a5ed7cf90a89a2285f8dde412f285c937706a7bf4bab35** | sha256sum line, `ns40-dl.log` |
| Streams | h264 1920×1080 + AAC | `ffprobe.txt` |
| Verified duration | **6884.033 s = 1:54:44.03** | `ffprobe.txt` |
| Packet span | first pts 0.000000, last 6883.989333, **735,731 packets** — full span, no truncation | `span.txt`, `packets.csv` |
| Full decode | **0 error bytes** (`decode_err_bytes=0`); spot decodes at 60/1800/3600/5400/6800 s all 0 errors | `span.txt`, `decode.err`, `spot-*.err` (all 0 B) |
| Egress | primo only (16 parallel ranged segments, per-segment size verify, up to 3 tries; concat in numeric order). Sandbox egress rejected: ~133 KB/s single-stream probe | `dl.sh`, `ns40-dl.log` (segment lines: 10 OK try 1; segs 0,7,8,10,12 OK try 2; seg14 OK try 3) |
| Download window | launched 2026-11-06T21:05:41-08:00, complete 21:57:35-08:00 (wave contention) | `ns40-dl.log` |

Duration verdict: plan states 1:54:44; page JSON-LD states PT1H54M44S
(6,884 s); ffprobe reads 6884.033 s. **All three agree — Plan 40 is a
duration exception** (joins Plans 34/37). No duration errata.

## Route lessons (capture mechanics)

- Watch page fetch is flaky at the origin: sandbox first fetch 403 (15 B
  "Access denied."); primo attempts interleaved 503 (93 B DB-fatal body) —
  the Plan 29 transient-noise family. Retry with a per-egress cookie jar
  converged: 200, 224,624 B on both egresses (`dl/page-sandbox.html`,
  primo `dl/page.html` / `page2.html`).
- **Rendition `get_file` URLs are egress/session-bound AND require a
  `Referer` header (the watch-page URL).** Without Referer: 403 on both
  egresses. With `-b <jar> -e <watch URL>` on primo: 302 → CDN → 206
  Content-Range. (Plan 20's manifest recorded the jar half; the Referer
  half is new — see BLOCH-CANDIDATE.md.)
- Renditions offered: 360p / 480p / 720p (1,968,048,753 B) / 1080p
  (2,898,146,377 B), probed via Content-Range on primo.
- No SOURCE-NOT-FOUND condition arose: page and CDN demonstrably serve
  this target; the 403/503 bodies were transient origin noise, never a
  target-404 with a succeeding control.

## Source metadata AS SEEN (watch page, fetched 2026-11-06, both egresses)

- Title: "How to Make Porn In Blender: Basics - Lighting and Color Grading"
- **Creator / uploader: Anime Nyan** (member 807029; "Uploaded by" pill;
  `video_models: 'Anime Nyan'`; JSON-LD description is first-person by the
  maker — creator and presenter are the same voice; sibling Plan 41 is
  the same "Basics" series).
- Upload date 2023-12-23; views 56,894; likes 213 (at capture load).
- Categories: Bleach, Tutorials, Blender. Tags: none.
- **Licence AS SEEN: the JSON-LD description states verbatim "This video
  is under the creative commons zero license." → CC0 as seen.** (Differs
  from Plans 02/11/13/17: no licence stated.) Study-only posture kept for
  run artifacts regardless.
- Description credits: Polyfjord's EXR tutorial; Waqas Qazi's "Teal and
  Orange" DaVinci Resolve grading tutorial; chapters by vadimbanshee405;
  a Google Drive link to "the finished Blender file for thumbnail, power
  grades and this youtube video in 1080p" (recorded, NOT followed).
- Chapter list (page's own map — cross-check only; the screen governs and
  deviates from it, see OBSERVATION §1): Introduction 0:00 · Download
  Locations/Characters 1:55 · Download Add-ons 3:37 · Install Add-ons
  4:54 · Add-ons in Work 5:52 · Start Work With Character 6:28 ·
  Increase Performance 7:57 · PureRef 9:03 · Character Pose 10:19 · Fix
  Hand Bug 12:46 · Work with Face 22:08 · How to Add Environment 29:35 ·
  Append Another Character 30:52 · Move Whole Environment 37:00 ·
  Camera 39:50 · **Light Start 46:20** · Fix Texture Bug 48:26 · Layer
  Visibility Off 56:34 · **Light Again 59:27** · **Interior Light Fix
  1:16:39** · **Render Settings 1:24:50** · **DaVinci Resolve Start
  1:27:00** · **Color Tutorial for DaVinci Resolve 1:32:19** · end
  1:54:44.

## Derived artifacts (primo, `~/.local/share/pax/night-school/plan-40/`)

- `audio.wav` — 16 kHz mono, 220,288,398 B (transcription source).
- `frames/grid/` — 57 frames, one per 120 s, 640 px wide.
- `frames/native/` — 77 frames, one per 60 s from t=2280 s, 1920×1080
  (frame t(n) at 2280+(n−1)×60 s).
- `frames/target/` — 9 targeted single frames (x2790/x3300/x4200/x4700/
  x5050/x5120/x5560/x6050/x6500).
- `frames/contact-grid.jpg` — tile contact sheet.
- Local copies of all frames: `runs/plan-40/frames/`.

## Transcription (chunked-transcription skill; slice ladder under wave contention)

Lane: whisper-cli 1.9.2, ggml-large-v3-turbo, primo, nice 19, `-t 2`,
`-l en`, via detach `ns40-chain` (serialized behind the download).
Slices (parameter-bearing spans first): E 0–480 s · A 2340–3540 ·
B 3540–4740 · C 4740–5940 · D 5940–6884 (5,264 s of 6,884 s).
Full chunked lane staged behind the slices (chunk1 0–3300, chunk2
3300–6900) with a `finish.sh` stitch+census on completion.
Census: `loop_census.py` (normalized-segment-v1) per slice/chunk when
landed — census lines recorded in OBSERVATION §8 when available.
**Tier: single-transcriber = UNCONFIRMED throughout.** The screen
governs; speech is tagged [SPOKEN] and never outranks a panel read.
**Status at delivery (2026-11-06 ~23:40 PST):** slice E landed +
censused (OBSERVATION §8); slices A–D and both full chunks still in
flight behind the sibling wave; `finish.sh` staged in the primo plan
dir to stitch + census on completion (`SPEECH-ADDENDUM.md`).

## Primo state during capture

Load 14–27 on 16 threads, swap exhausted (23/23 GiB), ~8 sibling
whisper jobs + ComfyUI — the sanctioned conditions for the slice ladder
and for serialized renders (P3 re-checks tenants before launching).
Blender estate pin verified on primo: 5.2.3 LTS (`/usr/bin/blender
--version`).
