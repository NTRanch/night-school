# Plan 30 — Capture Manifest

Plan: `repo/plans/30-wl-scene-import.md` — "WL Scene Import",
rule34video 3621064. **Micro-plan run, CAPTURE-BLOCKED /
SOURCE-NOT-FOUND outcome** (see INTAKE.md). Both binding
terminal egresses were honestly tried; the routes work —
the target itself returns the origin's application-level
404. No artefact was captured, so no operation, contract,
or failure mode is claimed for the clip.

## Pinned capture

- Canonical primo path intended:
  `~/.local/share/pax/night-school/plan-30/` — the directory
  exists (dl/ + records/ from the route probes); **no media
  file captured, nothing pinned.**
- Bytes: **not established** — no download occurred.
- SHA-256: **not established** — no file to hash.
- Streams (ffprobe): **not established** — no file to probe.
- Decode / packet-span verification: **not applicable.**
- Duration: plan states **0:29 (29 s)** — **NOT verified**.
  No watch page and no file exist in this run to verify it
  against. Recorded as plan-stated only. Real duration:
  **unknown**. (Cautionary context: the same-title sibling
  3569655's page states PT0H0M14S — 14 s — for a different
  artefact; it says nothing about this one's length.)

## Capture route (what actually happened, per route)

Binding route honoured throughout: terminal egress only
(shell curl), cookie jar per egress, page and file to be
fetched from the same egress. The browser text-fetch /
search route was never used for this domain. All tries are
in `records/route-log.txt`.

### Sandbox egress (2026-11-07 04:29–04:31 UTC)

- Watch-page GETs of
  `https://rule34video.com/video/3621064/wl-scene-import/`:
  **3× 404, 384 B** — the origin's XHTML "404 Not Found"
  body with JS redirect to `/404.php`, SHA-256
  `fd562038072a7a486e6fb98e7bf223ca494aef557c0d610ae30fe5774c9ee2ae`
  (`dl/target-sandbox.html`). This body is byte-identical
  to Plan 29's target-404 body.
- Slug-less variant `/video/3621064/`: 503 once, then
  **2× the same 404 body** (`dl/target-noslug-sandbox.html`).
- **Control (same egress, same jar, same method):** Plan
  14's video 4293878 fetched **200, 259,287 B** with its
  correct title ("Futa Tutor & Futa Black Date Ep-1,2")
  after one interleaved 503 (`dl/control-sandbox.html`,
  SHA-256 `6d6ff6a4800ebecf…`). Route healthy; 404 is
  target-specific.
- Site search `/search/wl-scene-import/` fetched 200
  (216,028 B saved copy, SHA-256 `55bcde3bc9c7de21…`;
  `dl/search-wl-scene-import-sandbox.html`): ID **3621064
  does not appear** on the results page (grep count 0).

### Primo egress (via ~/workspace/bin/primo-ssh, 2026-11-06 20:30 PST)

- Same target URL: **2× 404, 384 B, SHA-256 prefix
  `fd562038072a7a48`** — byte-identical to the sandbox body
  — plus one interleaved **503, 93 B** DB-fatal body
  (SHA-256 prefix `a990dd3f8fdc4d79`, the origin's known
  noise class; it also struck the control and the search).
  Slug-less variant returned the 503 on its single try.
- **Control (same egress):** video 4293878 fetched **200,
  259,287 B**, correct title, twice. Primo route healthy.
- Primo tenant check before the probes: load ≈ 30–35 on
  16 threads, 49/62 GiB RAM used (sibling jobs live). This
  run launched **no primo batch** — single curl probes
  only — and no detached `ns30-` run. Nothing was played
  aloud; no media existed to play.
- Record-keeping note: primo's on-disk `dl/target-primo.html`
  was overwritten by the final 503 retry (93 B on disk at
  close). The primo 404s are evidenced by the contemporaneous
  per-try hashes in `records/route-log.txt` and by the
  byte-identical sandbox body preserved in this run's dl/.

### Conclusion of the route evidence

This is Plan 29's outcome repeated on a second target, with
the same control discipline: the origin answers for the
site, for a sibling video, and for search, and answers
**404 Not Found for video 3621064 itself**, byte-identically
from two independent egresses. The artefact appears removed,
renamed, or otherwise no longer served at the plan's URL as
of 2026-11-06; the plan was written 2026-11-05 from a
category listing, so the listing may have been stale at
writing, or the item was withdrawn in the interval. This
run cannot distinguish those two, and does not try.

## Licence as seen

**Not seen** — the watch page does not exist to be read.
No licence claim is made. Default study-only posture per
protocol would apply to any future capture. (The sibling
3569655's page likewise states no content licence in its
JSON-LD; not a claim about the target.)

## Metadata of record

Target (plan file only, NOT firsthand watch-page data):

- URL (plan): https://rule34video.com/video/3621064/wl-scene-import/
- Video ID (plan): 3621064 · Title (plan): "WL Scene Import"
- Duration (plan): 0:29 — **not verified** (above).
- Creator (plan): "(category listing shows none — record at
  intake)" — **not recorded at intake; page not fetched.**
- Tags / categories / uploader / description / upload date /
  views / likes: **none seen in this run for the target.**

Sibling lead (different artefact, recorded as a lead only —
see INTAKE.md): ID 3569655, "WL Scene Import (Secret Recipe
Tutorial)", watch page fetched 200 from the sandbox
(`dl/sibling-3569655-sandbox.html`, 222,009 B, SHA-256
`7a7c1d293816c696…`); JSON-LD as seen: uploadDate 2024-10-20,
duration PT0H0M14S, views 9,657, likes 8; description invites
top supporters to a "secret recipe" on a Patreon page naming
the handle `absurdcookie`. Uploader field: no explicit
uploader name extracted; the page links member ID 423887.

## Analysis artifacts

- `records/route-log.txt` — timed per-try route log, both
  egresses, with body hashes, search/sibling tries, and the
  primo tenant check.
- `dl/target-sandbox.html` — the origin 404 body as served
  (384 B, SHA-256 `fd562038072a7a48…`).
- `dl/control-sandbox.html` — healthy-route control page
  (259,287 B).
- `dl/search-wl-scene-import-sandbox.html` — site search
  page for "wl scene import" (target ID absent).
- `dl/sibling-3569655-sandbox.html` — the same-title
  sibling's watch page (a lead, not the target).
- Primo `~/.local/share/pax/night-school/plan-30/dl/` —
  primo-side probe originals.
- `frames/` — README only; no frame exists in this run.
