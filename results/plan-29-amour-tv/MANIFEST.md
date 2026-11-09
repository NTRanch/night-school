# Plan 29 — Capture Manifest

Plan: `repo/plans/29-amour-tv.md` — "Amour TV", rule34video
3637868. **TRIAGE run, CAPTURE-BLOCKED / SOURCE-NOT-FOUND
outcome** (see INTAKE.md). Both binding terminal egresses were
honestly tried; the routes work — the target itself returns
the origin's application-level 404. No artefact was captured,
so no identification is claimed.

## Pinned capture

- Canonical primo path intended:
  `~/.local/share/pax/night-school/plan-29/` — the directory
  exists (dl/ + records/ from the route probes); **no media
  file captured, nothing pinned.**
- Bytes: **not established** — no download occurred.
- SHA-256: **not established** — no file to hash.
- Streams (ffprobe): **not established** — no file to probe.
- Decode / packet-span verification: **not applicable** —
  no file.
- Duration: plan states **14:51 (891 s)** — **NOT verified**.
  No watch page and no file exist in this run to verify it
  against; the number is recorded as plan-stated only, per
  the brief's warning that this corpus's durations are
  unreliable. Real duration: **unknown**.

## Capture route (what actually happened, per route)

Binding route honoured throughout: terminal egress only
(shell curl), cookie jar per egress, page and file to be
fetched from the same egress. The browser text-fetch /
search route was never used for this domain.

### Sandbox egress

- Watch-page GETs of
  `https://rule34video.com/video/3637868/amour-tv/`:
  repeated attempts 2026-11-06 ~20:25–20:27 PST returned
  either **404, 384 B** — the origin's XHTML "404 Not Found"
  body with a JS redirect to `/404.php`, SHA-256
  `fd562038072a7a486e6fb98e7bf223ca494aef557c0d610ae30fe5774c9ee2ae`
  (`dl/target-404-sandbox.html`, `records/route-log.txt`) —
  or **503, 93 B**, the origin's database-fatal body
  (`[FATAL]: can't connect to database … Connection refused`,
  SHA-256 prefix `a990dd3f8fdc4d79`).
- Slug-less variant `/video/3637868/` also returned the same
  404 body. No-slash variant alternated 404/503 the same way.
- **Control (same egress, same method):** Plan 14's video
  4293878 fetched **200, 259,287 B** with its correct title
  on the first attempt (`dl/control-4293878-sandbox.html`,
  SHA-256 `0a2688a255456bfe72fc72749dd706b003c87cfb4e8ecb869e9764dd027a49b3`);
  the site homepage fetched 200, 206,198 B; the site search
  page for "amour tv" fetched 200, 200,332 B
  (`dl/search-amour-tv-sandbox.html`). The route is healthy;
  the 404 is specific to this video ID.
- The interleaved 503s are origin noise, not route failure:
  a 503 also hit the control once in the final batch
  (`records/route-log.txt`), while the 404 body — served by
  the application while it was up — says the video record
  itself is not found.

### Primo egress (via ~/workspace/bin/primo-ssh)

- Same target URL: repeated attempts returned the **same
  404 body, byte-identical** (384 B, SHA-256 prefix
  `fd562038072a7a48`, identical to the sandbox body), plus
  the same interleaved 503 DB body (primo
  `records/route-log-primo.txt`, copied into this run's
  `records/route-log.txt`). One early primo attempt returned
  403, 15 B ("Access denied.") before the cookie jar was
  established; with the jar, primo converges on the 404.
- **Control (same egress):** video 4293878 fetched **200,
  259,287 B**, correct title — byte-size identical to the
  sandbox control. Primo route is healthy too.
- Primo tenant check before batches (2026-11-06 ~20:25 PST):
  load ≈ 33–37 on 16 threads with ~10 sibling whisper-cli
  jobs plus ComfyUI live. This run launched **no primo
  batch** — only single curl probes — and no detached
  `ns29-` run; nothing heavy was queued behind the wave.
  Nothing was played aloud (audio silence rule, trivially:
  no media was obtained).

### Conclusion of the route evidence

CAPTURE-BLOCKED is declared on the task's own terms — both
terminal egresses honestly fail **for this target** — with
the stronger, control-proven refinement: this is not an
egress or policy failure (Plan 25's situation). The origin
answers for the site, for a sibling video, and for search,
and answers **404 Not Found for video 3637868 itself**,
byte-identically from two independent egresses. The artefact
appears removed, renamed, or otherwise no longer served at
the plan's URL as of 2026-11-06; the plan was written
2026-11-05 from a category listing, so the listing itself
may have been stale at writing, or the item was withdrawn
in the interval. This run cannot distinguish those two, and
does not try.

## Licence as seen

**Not seen** — the watch page does not exist to be read.
No licence claim is made. Default study-only posture per
protocol would apply to any future capture.

## Metadata of record (plan file + search page only, NOT firsthand watch-page data)

- URL (plan): https://rule34video.com/video/3637868/amour-tv/
- Video ID (plan): 3637868 · Title (plan): "Amour TV"
- Duration (plan): 14:51 — **not verified** (above).
- Creator (plan): "(category listing shows none — record at
  intake)" — **not recorded at intake; page not fetched.**
- Tags / categories / uploader / description / upload date /
  views / likes: **none seen in this run.**
- One contextual lead, recorded as a lead and nothing more:
  the site's own search for "amour tv" (fetched 2026-11-06,
  sandbox; `dl/search-amour-tv-sandbox.html`) does **not**
  list ID 3637868 on its first page, but does list a sibling
  item, ID 3623811, "Amour TV『W.T.Dinner』" — suggesting
  "Amour" is a maker/series name with other instalments
  still live. That is evidence about the *name*, not about
  the target artefact, and no identification is built on it.

## Analysis artifacts

- `records/route-log.txt` — timed per-try route log, both
  egresses, with body hashes.
- `dl/target-404-sandbox.html` — the origin 404 body as
  served (384 B).
- `dl/control-4293878-sandbox.html` — the healthy-route
  control page (259,287 B).
- `dl/search-amour-tv-sandbox.html` — site search page for
  "amour tv" (200,332 B); the sibling lead above traces to it.
- Primo `~/.local/share/pax/night-school/plan-29/dl/` +
  `records/route-log-primo.txt` — the primo-side originals.
- `frames/` — README only; no frame exists in this run.
