# Plan 03 — Capture Manifest

Plan: `repo/plans/03-testing-patterns.md` — "Testing Patterns",
Virt-A-Mate clip by TdotONY, rule34video 3300899. Re-scoped at
intake to a reference-only scene analysis (no rebuild).

## Pinned capture

- Canonical file (primo):
  `~/.local/share/pax/night-school/plan-03/plan03-source-1080p.mp4`
- Bytes: **33,005,485**
- SHA-256: **3d0cb623f2b8245c3d86a6ca1cd516c5d92c7e44fae15c85b5dae777108ec3be**
  (identical on the sandbox download and the primo copy —
  verified by sha256sum on both machines)
- Streams (ffprobe, both machines agree): **one video stream
  only** — h264, 1920×1080, 60 fps, 4,963 frames, format
  duration 82.716667 s. **No audio stream exists.** The page
  tag "no sound" is confirmed at the stream level; per the run
  brief, transcription was skipped entirely (nothing to
  transcribe; nothing manufactured). Nothing was played aloud.
- Page-stated duration PT0H1M23S (83 s) vs file 82.716667 s:
  0.283 s container/rendition difference, recorded not smoothed.
- Rendition: 1080p — the highest the page offers (flashvars
  tokens exist for 360p/480p/720p/1080p).
- Captured: 2026-11-06.

## Capture route (what actually worked)

- Route class: watch-page token URLs (the Plan 01/06/07/35
  route). Both egresses fetched the watch page fine (200,
  217,971 B, identical).
- **Primo file download FAILED**: the primo detached run
  (ns03-dl) returned a 0-byte file; a foreground header probe
  showed the file host answering **HTTP 403 (ddos-guard)** to
  primo for the 1080p `get_file` URL. The token used had been
  minted by the *sandbox* page load — the working hypothesis
  (recorded as such, not proven): `v-acctoken` URLs are bound
  to the egress/session that loaded the watch page. Prior
  plans fetched page + file on the same egress and never hit
  this.
- **Sandbox egress won**: same token URL, HTTP 200,
  33,005,485 B in ~22 s. The verified file was then copied to
  the primo canonical path over the primo SSH route and
  re-hashed there (identical, above).
- yt-dlp was not attempted (prior plans proved it fails on
  this host class).

## Licence

- Page-stated licence, verified firsthand: **none stated.**
  Full-text search of the saved watch page (`dl/page.html`)
  for "license" / "licence" / "creative commons" / "CC0"
  finds only the player config's opaque `license_code` token
  (`$611881720187049`) — a player key, not a content licence.
  Recorded exactly as seen. Study-only posture: studied,
  never redistributed — no video file or frame enters any
  shipped artifact.

## Page metadata of record (watch page fetched 2026-11-06, saved as `dl/page.html` + primo `dl/page.html`)

- Title: "Testing patterns" · video_id 3300899
- JSON-LD: name "testing patterns", **description "" (empty —
  absent, as the plan's intake stated)**, uploadDate
  2024-02-18, duration PT0H1M23S, views 5,324, likes 14
  (plan intake recorded 5,317 views — counts move).
- Categories: Virt-A-Mate, Tutorials · Tags: blowjob,
  deepthroat, no sound · `video_models`: "Unknown Artist"
  (creator TdotONY is the plan's attribution; the page names
  no model).

## Analysis artifacts (all numbers in the run's documents trace to these)

Primo `~/.local/share/pax/night-school/plan-03/records/`,
copies in this run dir's `records/`:

- `adj-mad.csv` / `adj-mad.npy` — adjacent-frame mean absolute
  difference, all 4,962 frame pairs, decoded at 480×270 grey
  (script `analyze.py`).
- `region-mad.npy` — adjacent MAD on a 4×4 tile grid.
- `slider-fills.json` — depth/bias/speed slider fill fractions
  at 10 Hz from native-resolution panel crops (script
  `pass2b.py`; boxes verified visually against grid frames).
- `head-template-track.csv` + `segment-periods.json` —
  template-matched head position every frame (match score
  median 0.936, min 0.798) and per-segment cycle periods from
  track autocorrelation (script `pass3.py`).
  `head-trajectory.csv` (an earlier hair-blob centroid track)
  is superseded by the template track — the blob track mixed
  the moving target marker into the blob; kept for provenance,
  not cited.
- `ui-static.json` — UI/background region MAD vs frame 0
  (script `pass2.py`).
- `cycle-variation.json` — cycle-corresponding vs control-lag
  frame MAD by region in the three stable segments
  (script `pass4.py`).
- The whole-clip lag scan in `analyze.py` was killed after
  ~20 min without completing (3571 lags over full-frame
  signatures was undersized for the box's shared load); the
  per-segment template-track autocorrelation answers the same
  question and is the record of record. `adj-mad` and
  `region-mad` outputs from that script survive and are cited.

## Frames

- 83 grid stills at 1 s spacing (t = 0…82 s), native
  1920×1080 (`frames/grid_001…083.png`) + a 10-wide contact
  sheet (`frames/contact-1s.jpg`).
- 5 targeted native frames (`frames/targeted/`): freeze start
  (f213) / freeze end (f446), S4 forward extreme (f1548),
  S4 back extreme (f1939), S8 back extreme (f4401).

## Cleanup

- Deleted at task end: the sandbox duplicate media file in
  `dl/` (hash pinned above; canonical copy on primo), the
  0-byte primo download remnant (overwritten by the verified
  copy), primo probe leftovers. Kept: page HTML + cookies +
  all analysis scripts (`analyze.py`, `pass2.py`, `pass2b.py`,
  `pass3.py`, `pass4.py` on primo beside the media), records,
  frames, and all run documents.
