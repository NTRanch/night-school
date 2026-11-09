# Plan 25 — Capture Manifest

Plan: `repo/plans/25-cat-vid.md` — "Cat Vid", rule34video 3663988.
**TRIAGE run, CAPTURE-BLOCKED / PARTIAL outcome** (see INTAKE.md).

## Pinned capture

- Canonical primo path intended:
  `~/.local/share/pax/night-school/plan-25/` — **no file captured,
  nothing copied to primo.**
- Bytes: **not established** — no download occurred.
- SHA-256: **not established** — no file to hash.
- Streams (ffprobe): **not established** — no file to probe.
- Duration: plan states **2:59 (179 s)** — **NOT verified** against
  a captured file or a fetched page in this run. Recorded as
  plan-stated only, not smoothed and not promoted to verified.

## Capture route (what actually happened)

- One attempt was made to fetch the watch page text via the
  text-fetch tool on 2026-11-06 ~20:18 PST. It failed with a
  policy block on the domain (`browser.open`:
  "Domain rule34video.com is blocked by policy", service
  status 200, no source HTTP status returned).
- On that failure the runtime instructed: do not repeat the
  request, including with changed arguments or through another
  tool or endpoint, and do not bypass an access/policy denial.
  That instruction was obeyed: **no second fetch, no cookie-jar
  GET, no primo-egress attempt, no sandbox-egress curl, and no
  alternate endpoint was tried for this source in this run.**
- Consequently the task's CAPTURE-BLOCKED protocol applies in
  its page-metadata-only form, except that even page metadata
  could not be fetched firsthand in this run: the only
  metadata of record is the plan file itself (below).
- Primo tenant check: not run as a batch prerequisite, because
  no primo batch was started. No detached `ns25-` run was
  launched. Nothing was played aloud at any point (audio
  silence rule — trivially satisfied: no media was obtained).

## Licence

- Page-stated licence: **not seen** — the page was not fetched.
  No licence claim is made. Default study-only posture per
  protocol would apply to any future capture: studied, never
  redistributed.

## Metadata of record (plan file only, NOT firsthand page data)

Source: `repo/plans/25-cat-vid.md`, read at run start.

- URL (plan): https://rule34video.com/video/3663988/cat-vid/
- Video ID (plan): 3663988
- Title (plan): "Cat Vid"
- Duration (plan): 2:59
- Creator (plan): "(category listing shows none — record at
  intake)" — **not recorded at intake; page not fetched.**
- Tags / categories / uploader / description / upload date /
  views / likes: **none seen in this run.**

No other metadata is asserted. Any number above traces to the
plan file, which is the sole artifact for this run's metadata.
