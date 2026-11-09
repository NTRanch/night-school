# Plan 25 — Capture Manifest — ATTEMPT 3 (terminal egress, final)

Plan: `repo/plans/25-cat-vid.md` — "Cat Vid", rule34video 3663988.
**TRIAGE re-run, outcome: SOURCE-NOT-FOUND** (brief branch b,
Plan 29/30 pattern). The item's watch page returns a
byte-identical 404 shell on both egresses whenever the origin
answers, while a known-good control video page on the same
egress at the same moment returns 200. Attempts 1–2 records
(MANIFEST.md, MANIFEST-2.md and the appended sections in
INTAKE.md / OBSERVATION.md / PASS4-APPLICATION.md) stand
unedited; attempt-3 sections are appended to those files
under clear headings, and this file is the attempt-3 manifest.

## Route discipline (per brief)

- Terminal egress ONLY. `browser.open` / `browser.search`
  were not used for this domain at any point in attempt 3
  (the attempt-1 browser route is policy-blocked for this
  domain and was not retried).
- Both sanctioned egresses exercised: sandbox `curl` and
  primo `curl` via `~/workspace/bin/primo-ssh`, each with its
  own warmed cookie jar (homepage hit first) and a browser
  user agent — the same route class as attempts 2 and
  Plans 01–24/29/30.
- Bounded probe window per brief: 1 initial probe set +
  4 confirmation rounds per egress at 45 s spacing
  (2026-11-07 05:32:19–05:34:56 UTC = 2026-11-06
  21:32–21:35 PST). No detached loops were needed; all
  fetches were foreground and short.

## Pinned capture

- Canonical primo path: `~/.local/share/pax/night-school/plan-25/`
  — **no file captured, no media copied** (there is nothing
  to capture: the source page does not exist at the origin).
  Primo's `dl3/` holds only this attempt's probe bodies and
  cookie jar.
- Bytes / SHA-256 / streams (ffprobe): **not established** —
  no download occurred or is possible. Nothing is smoothed
  or promoted.
- Duration: plan states **2:59 (179 s)** — still **NOT
  verified** (no page, no file, and now no prospect of
  either). Plan-stated only, permanently.

## Control probe (per brief step 1) — 2026-11-07 05:32 UTC

Control video: Plan 14's 4293878
(`https://rule34video.com/video/4293878/futa-tutor-futa-black-date-ep-1-2/`),
which returned 200 / 259,287 B in the Plans 29/30 probes.
All numbers trace to `records3/probe-sandbox.log` and
`records3/probe-primo.log`; bodies in `records3/`.

| Egress | URL | Status | Bytes | SHA-256 |
|---|---|---|---|---|
| sandbox | homepage `/` | 200 | 206,004 | 3cb5288cf0502256aa9cbfb55f358a6cd22ab43a7764d60409ad46049b7c947f |
| sandbox | control 4293878 | 200 | 259,287 | f08f0156d4eb032a0971f33879600f038c9582ce0eb38d456fca8ab5aba260bd |
| primo | homepage `/` | 503 | 93 | a990dd3f8fdc4d794e5f60fa46d481524f868ab6193b90a41c12afc3439e754e |
| primo | control 4293878 | 503 | 93 | a990dd3f8fdc4d794e5f60fa46d481524f868ab6193b90a41c12afc3439e754e |

- The sandbox control body carries its correct page title,
  `<title>Futa Tutor & Futa Black Date Ep-1,2</title>`
  (grep of `records3/control-video-sandbox.html`) — the
  control is the right item, served in full, at exactly the
  Plans 29/30 byte size (259,287 B).
- The 503 body (93 B, both primo probes) is verbatim the
  attempt-2 database-failure body: `[FATAL]: can't connect
  to database defined in /admin/include/setup_db.php:
  Connection refused` (confirmed from
  `records3/confirm-target-3663988-sandbox-r1.html`).

## Target probe (per brief step 2) — all attempt-3 fetches

Target: `https://rule34video.com/video/3663988/cat-vid/`.
Logs: `records3/probe-{sandbox,primo}.log`,
`records3/confirm-{sandbox,primo}.log`; bodies in `records3/`.

| Fetch set | Target results | Control results (same rounds) |
|---|---|---|
| sandbox initial (05:32:19Z) | 404 / 384 B / fd562038… | home 200; control 200 / 259,287 B |
| sandbox rounds 1–4 | 503, 503, 404, 404 | 503, 200, 200, 200 (200s all 259,287 B) |
| primo initial (05:32:25Z) | 404 / 384 B / fd562038… | home 503; control 503 (93 B DB body) |
| primo rounds 1–4 | 404, 404, 503, 404 | 200, 200, 503, 503 (200s all 259,287 B) |

Totals: target fetched 10× (5 per egress) → **404 ×7, every
one byte-identical** (384 B, SHA-256
`fd562038072a7a486e6fb98e7bf223ca494aef557c0d610ae30fe5774c9ee2ae`
— the same 404 shell family recorded in attempt 2, an
Apache-style "Not Found" body with a `/404.php` redirect
script), 503 ×3 (the DB-flap body above). Control fetched
10× → 200 ×6 (always 259,287 B), 503 ×4.

**Discriminating pairs** (same egress, same round, origin
answering): sandbox initial, sandbox rounds 3 and 4, primo
rounds 1 and 2 — **5 pairs, control 200 / target 404
byte-identical in every pair.** (Sandbox round 2 is the one
mixed round: control 200, target 503 — the flap hit the
target fetch only.)

## Branch determination: (b) SOURCE-NOT-FOUND

- This is **not** attempt 2's outage repeated (branch c):
  in attempt 2 the video route never returned 200 once in
  120+ attempts; in attempt 3 the control video page
  returned 200 in 6 of 10 fetches spread across both
  egresses and the whole window. The origin is intermittently
  flapping at its database layer (the 503s above, hitting
  homepage, control, and target alike), but it demonstrably
  serves video pages — just not this one.
- Whenever the origin answers the target at all, the answer
  is the byte-identical 404 shell. That is the Plan 29/30
  SOURCE-NOT-FOUND signature: same-egress, same-moment
  control 200 vs target consistent 404. The item
  (ID 3663988) is absent at the origin — removed or never
  present under this ID/URL; which of those, the evidence
  cannot distinguish and this record does not guess.
- Consequences per brief branch (b): identification
  **outstanding** (nothing was ever served to identify);
  **no disposition on the merits** (not CLOSE, not
  CLOSE-BAR-CLASS, not proceed-as-technique); census line
  **unchanged** — an absent source is not a mis-shelving
  instance. See PASS4-APPLICATION.md attempt-3 section.
- Bar-class screen: **could not be performed, and is now
  permanently moot for this source** — no metadata was ever
  served in any attempt, and no content exists at the origin
  to sample. The boundary was neither encountered nor ruled
  out; it is recorded as unexaminable, not as passed.
  No frame sampling was attempted in attempt 3.

## Primo tenant check

Run before the probes, 2026-11-06 ~21:32 PST: primo loaded
with tenant whisper-cli transcriptions (several jobs, load
average ≈12–18), ~22 GiB RAM available. This attempt was
page fetches only (10 target + 10 control + 2 homepage,
≤259,287 B each) and ran beside the tenants per the
good-neighbour rules. Nothing was played aloud at any point
(audio silence rule — trivially satisfied: no media exists).

## Licence

- Page-stated licence: **not seen** — the page does not
  exist. No licence claim is made.

## Metadata of record

Unchanged across all three attempts: the plan file only
(`repo/plans/25-cat-vid.md`) — URL, ID 3663988, title
"Cat Vid", stated duration 2:59, no creator in the category
listing. **No firsthand page metadata exists from any
attempt**: no tags, categories, description, uploader, or
upload date has ever been seen for this item, and — the
source being absent — none ever will be from this URL.
