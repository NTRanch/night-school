# Plan 17 — Capture Manifest

Plan: `repo/plans/17-porn-in-blender-part-2.md`
Item: "How to make Porn in Blender (Part 2)" — Divinity
Studio (uploader divinitystudiox), rule34video video 4282602.

## Pinned capture

- Canonical file (primo): `~/.local/share/pax/night-school/plan-17/plan17-source-720p.mp4`
- Bytes: **916,337,092**
- SHA-256: **6501528046641b23f9b1593c000e2203c434515a0b8d6a871d5b16bc7422da72**
- Streams (ffprobe): video h264 1280×720, audio AAC; format
  duration **3669.845 s (1:01:09.8)** — the watch page states
  PT1H1M10S (3,670 s); the plan states 1:19:12 (4,752 s).
  **The plan's duration is wrong** (errata, Δ 1,082 s); page
  and file agree. The acquired file governs.
- Rendition: 720p — the highest the page offers (flashvars
  tokens exist for 360p/480p/720p only; no 1080p exists for
  this video). Total size established before download by a
  Content-Range probe: 916,337,092 bytes (both egresses
  probed; the value is identical from sandbox and primo).

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/02/06/07/
  11/35 route). yt-dlp was not attempted (prior plans proved
  it fails on this host class).
- Egress probes (2026-11-06; numbers from the probe
  commands' own output, single-stream 4 MiB ranged sample):
  - sandbox: 4,194,304 B at ≈980 KB/s (curl `speed_download`
    980,399 B/s).
  - primo: 4,194,304 B at ≈858 KB/s (curl `speed_download`
    858,388 B/s).
  - Single-stream speeds are comparable; prior plans proved
    primo's parallel ranged download scales while the
    sandbox proxy collapses under parallel load (Plan 02
    manifest), so the download ran on primo with 8 parallel
    ranged segments. Sustained aggregate measured from
    segment-dir growth: ~249 MB in the first ~30 s, decaying
    under wave contention; total wall time 19:03:26→19:05:08
    PST (102 s for the segment phase per the detach log
    timestamps; the log's start/done lines are the artifact).
- Winning download: primo detach `ns17-dl`, `.done` file
  reads 0. 8 segments of 114,542,137 B (last 114,542,136 B);
  every segment size-verified before concatenation (all 8
  OK on attempt 1 per `ns17-dl.log`); concatenation in
  numeric order (`seq 0 7`, the Plan 02 lesson — never glob
  order) produced the pinned file; concat byte count exact
  (916,337,092 = want).
- Decode + span verification (Plan 05 truncated-rendition
  lesson):
  - Packet span (ffprobe, all packets): first pts −0.021 s,
    last pts 3669.824 s, 282,120 packets — the packet span
    covers the full stated duration; no truncation.
  - Spot decodes at t = 60 / 900 / 1800 / 2700 / 3600 s:
    0 error bytes each (ffmpeg `-v error`, per-timestamp
    `.err` files in the primo canonical dir).
  - Full-file decode to null: error log 0 bytes
    (primo detach `ns17-decode.log`). Clean.

## Licence

- Page-stated licence, verified firsthand at intake: **none
  stated.** Full-text search of the watch page (saved as
  `dl/page-sandbox.html` in this run dir and `page.html` on
  primo) for "license" / "licence" / "creative commons" /
  "CC0" finds no licence statement for this video (sole hit:
  the player config's opaque `license_code` token). Recorded
  exactly as seen. Study-only posture: the tutorial is
  studied, never redistributed — no video file, transcript,
  or frame enters any shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06, saved as `dl/page-sandbox.html`)

- Title: "How to make Porn in Blender (Part 2)"
- video_id 4282602; uploader **divinitystudiox**; series
  presented as **Divinity Studio** (page JSON-LD description:
  Patreon/SubscribeStar links for divinitystudio /
  divinity-studio, plus a "Tutorial in PDF Format" Mega
  link); `video_models` empty; uploadDate 2026-03-15 (the
  same date as Part 1, Plan 16's video 4274245);
  duration PT1H1M10S; views 45,866 and likes 124 at capture
  load; categories "Tutorials, 3D, Overwatch, Blender";
  tags "domina (overwatch), thigh highs, big breasts, sound".

## Transcription (chunked lane, per skill)

- whisper-cli (whisper.cpp 1.9.2, OpenChatCut bundled on
  primo), model ggml-large-v3-turbo, primo CPU. WAV 16 kHz
  mono (117,435,278 B audio.wav on primo) chunked at
  3,300 s into 2 chunks (map: `chunk-map.txt` in this run
  dir): chunk1 0–3300 s, chunk2 3300–3669.845 s. The media
  is over the lane's 3,600 s single-pass cap by 69.845 s,
  so the chunked lane is mandatory, not optional.
- Run state: **RUNNING (detached) at this run's delivery.**
  Primo is oversubscribed by the parallel wave (five
  concurrent whispers + a Blender rebuild; swap exhausted,
  load 21–28 on 16 threads — `top` snapshots in the run's
  working notes). This run's job: primo detach
  `ns17-tr2` (script `transcribe2.sh`, whisper-cli -t 8,
  nice 10; PID 133395 at last check), chunk1 then chunk2
  sequentially. A first -t 4 attempt was restarted at
  -t 8 (friction log, BLOCH-CANDIDATE.md items 2/5).
  Flushed segments at delivery reach ≈2:48 of chunk1
  (log `ns17-tr2.log` on primo). Post-processing is
  staged on primo as one command —
  `~/.local/share/pax/night-school/plan-17/finish.sh`
  (runs `stitch.py` → stitch verify, then
  `loop_census.py --manifest`) — to be executed when
  `ns17-tr2.done` lands; its outputs (`transcript.srt`,
  `transcript.txt`, `stitch-verify.txt`,
  `loop-census.txt`) complete this manifest's census
  fields. Tier: single-transcriber, **UNCONFIRMED**.
  The screen governs throughout OBSERVATION.md; the only
  narration cited anywhere in this run is the flushed
  segments quoted in OBSERVATION's preliminary
  transcript addendum, marked as such.
- Preliminary flushed narration (from `ns17-tr2.log`,
  UNCONFIRMED, in-progress): at 0:17–0:47 the creator
  narrates an opening retune — device switched to CPU,
  viewport sampling reduced to 64 ("this is just a
  viewport render this is not the final render"); at
  ≈2:45 he references a link "in the pdf file" (the
  companion PDF named in the page description) for an
  asset. See OBSERVATION addendum.
