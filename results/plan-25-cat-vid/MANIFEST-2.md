# Plan 25 — Capture Manifest — ATTEMPT 2 (terminal egress)

Plan: `repo/plans/25-cat-vid.md` — "Cat Vid", rule34video 3663988.
**TRIAGE re-run, CAPTURE-BLOCKED / PARTIAL outcome** — this time
with the programme's route of record used throughout, and a
different cause: an origin outage, not a route error. Attempt
1's record (MANIFEST.md, INTAKE.md, OBSERVATION.md,
PASS4-APPLICATION.md) stands unedited above/beside this file;
attempt-2 sections are appended to those files under clear
headings.

## Route discipline (per brief)

- Terminal egress ONLY. `browser.open` / `browser.search`
  were not used for this domain at any point in attempt 2.
- Both sanctioned egresses were exercised for real: sandbox
  `curl` and primo `curl` via `~/workspace/bin/primo-ssh`,
  each with its own warmed cookie jar (homepage hit first to
  set ddos-guard cookies) and a browser user agent — the
  Plan 01/03/04/06/07/14 route class (watch-page fetch →
  flashvars tokens → ranged file GET). The run never reached
  the token stage: no watch page was ever served.

## Pinned capture

- Canonical primo path: `~/.local/share/pax/night-school/plan-25/`
  — **no file captured, no media copied.** The directory's
  `dl2/` holds only this attempt's fetch-loop artifacts
  (script, cookie jar, failure bodies).
- Bytes / SHA-256 / streams (ffprobe): **not established** —
  no download occurred, so there is nothing to pin, hash, or
  probe. Nothing is smoothed or promoted.
- Duration: plan states **2:59 (179 s)** — still **NOT
  verified** (no page, no file). Plan-stated only.

## Capture route — per-egress evidence (all numbers trace to
`records2/page-loop-primo.log`, `records2/page-loop-sandbox.log`,
and the closing-probe bodies in `records2/`)

### Sandbox egress

- Foreground, 2026-11-06 ~20:20 PST: homepage **HTTP 200,
  206,198 B**. Watch page **HTTP 503, 93 B** — body verbatim:
  `[FATAL]: can't connect to database defined in
  /admin/include/setup_db.php: Connection refused`.
  A short foreground retry batch then left a **404 shell
  (384 B)** as the saved page body (`dl2/page-sandbox.html`,
  04:22 UTC) — the origin was already alternating.
- Detached retry loop `ns25-page-sandbox` (file-mediated,
  D-567; script `records2/fetch-page-loop.sh`): 45 s interval,
  ran 2026-11-07 04:21:39–05:29:24 UTC (20:21–21:29 PST),
  exit rc=1, `PAGE_FAILED`. **59 attempt lines are logged:
  28× HTTP 404 (384 B shell), 11× HTTP 503 (93 B DB body),
  20× HTTP 000 (curl 60 s timeout — the origin degraded from
  refusing to hanging late in the window).** The loop's own
  completion line reports 60 attempts; the attempt-60 outcome
  line is absent from the log. That gap is recorded, not
  filled — no outcome is claimed for it.
- Closing probe, 21:29 PST: homepage now also **503 (93 B)**;
  watch page **404 (384 B shell)** (`records2/probe-close-sandbox.html`).

### Primo egress

- Foreground, 2026-11-06 ~20:21 PST: homepage **HTTP 503,
  93 B** (the outage intermittently reached the homepage too;
  primo's homepage returned 200 at the closing probe below);
  watch page **HTTP 503, 93 B** (same FATAL DB body).
- Detached retry loop `ns25-page` (primo detach dir
  `~/.local/share/pax/detach/`, `.done` file rc=1): **60
  attempts, all logged: 38× HTTP 404 (384 B shell), 22× HTTP
  503 (93 B DB body), zero successes**, 20:21:41–21:07:50 PST,
  ending `PAGE_FAILED`.
- Closing probe, 21:29 PST: homepage **HTTP 200 (206,004 B)**;
  watch page **404 (384 B shell)** (`records2/probe-close-primo.html`).

### Reading of the evidence

The terminal route **works** — both egresses reached the
origin and received real origin HTTP answers throughout.
What failed is the origin's video-page service: for the whole
attempt-2 window (20:20–21:29 PST) the watch-page route
alternated a generic 404 shell (384 B, Apache-style body with
a `/404.php` redirect script) and a 503 carrying the origin's
own database-connection failure, while the homepage was
intermittent — 200 at the sandbox foreground probe (window
start) and the primo closing probe, but the same 503 body at
the primo foreground batch and the sandbox closing probe.
The video route, by contrast, never returned 200 once. Plan 24's intake recorded the
identical alternation (404 shell / 503 DB body, homepage 200)
for a different video (3666838) earlier the same night — this
is an origin-wide degraded window, not an item-specific
deletion and not an egress fault. No per-item conclusion is
drawn from it.

## Primo tenant check

Run before the batch, 2026-11-06 ~20:20 PST: primo heavily
loaded with tenant whisper-cli transcriptions (several jobs;
load average ≈44) with ~11 GiB RAM available. This run is
network/ffmpeg-light (page fetches only; no download, no
transcription batch was ever started), and ran beside the
tenants per the good-neighbour rules. Nothing was played
aloud at any point (audio silence rule — trivially satisfied:
no media was obtained).

## Licence

- Page-stated licence: **not seen** — the page was never
  served. No licence claim is made. Default study-only
  posture per protocol would apply to any future capture.

## Metadata of record

Unchanged from attempt 1: the plan file only
(`repo/plans/25-cat-vid.md`) — URL, ID 3663988, title
"Cat Vid", stated duration 2:59, no creator in the category
listing. **No firsthand page metadata exists from either
attempt**: no tags, categories, description, uploader, or
upload date has ever been seen for this item. Consequently
the bar-class metadata screen (see INTAKE.md attempt-2
section) could not be performed, and no frame sampling was
attempted — the screen gates sampling by design.
