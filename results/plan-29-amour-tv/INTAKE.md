# Plan 29 — Intake (Pass 0) + Triage — CAPTURE-BLOCKED / SOURCE-NOT-FOUND

Plan: `repo/plans/29-amour-tv.md` — "Amour TV" (rule34video
3637868). This plan is a **triage**: identification +
disposition, plus a packaging-grammar note if the item is
packaged content. This run could not reach identification —
not because the route failed, but because **the origin no
longer serves the artefact at the plan's URL** (evidence in
MANIFEST.md). The gap is recorded honestly instead of filled.

## Identification: **NOT ESTABLISHED**

Artefact class (show episode / tool demo / studio tour /
content / other), segment structure, and framing device are
all **unknown from this run**. No watch page exists to read
and no frame was sampled, so no classification claim is
made in any direction — not even "pure content", which is a
finding about an artefact this run never saw.

### Evidence actually in hand

| # | Evidence | Source artifact |
|---|---|---|
| 1 | The plan describes the item only as a channel-style name on the Tutorials shelf: title "Amour TV", ID 3637868, stated duration 14:51, no creator in the category listing. Its SHOULD-BE-SEEN is explicitly deferred: "Unknown until intake writes it." | `repo/plans/29-amour-tv.md` (read at run start) |
| 2 | The origin serves an application-level **404 Not Found** (384 B XHTML body, JS redirect to `/404.php`) for this video ID from **both** terminal egresses, byte-identically (SHA-256 `fd562038072a7a48…`), across repeated attempts — including the slug-less `/video/3637868/` form. Interleaved 503s are the origin's known database flakiness and also struck the control once. | `records/route-log.txt`; `dl/target-404-sandbox.html` |
| 3 | The routes are proven healthy by a same-egress, same-method **control**: video 4293878 fetched 200 / 259,287 B with its correct title from the sandbox *and* from primo; homepage and site search also fetch 200. The failure is target-specific, not route-, egress-, or policy-shaped. | `dl/control-4293878-sandbox.html`; MANIFEST.md §Capture route |
| 4 | The site's own "amour tv" search (200, first page) does not list ID 3637868, though a sibling "Amour TV『W.T.Dinner』" (3623811) is live. Consistent with the target having been removed/renamed; not proof of which, and not an identification of the target. | `dl/search-amour-tv-sandbox.html` |

There are no "2–3 strongest evidence points" *for an
identification*, because there is no identification. The
four points above are the strongest evidence for the
run's actual finding: **source-not-found at origin**.

## SHOULD-BE-SEEN

Per the plan, deferred to intake; intake could not write
one, because writing it requires the artefact. No
expectation was formed and none was tested. In particular,
the plan's motivating guesses (show episode? tool demo?
studio tour?) remain exactly that — guesses, untested.

## Tutorial-marker question

**Not run.** If instruction had been found, the brief
requires stopping and reporting TUTORIAL-FOUND; there was
nothing to inspect for markers. A checklist over zero
frames would be a fabricated result, so none is reported,
not even as "0 of N".

## Packaging-grammar question

**Not reachable.** Segments, framing device, and runtime
discipline can only be measured on a captured file. The
application question (borrowings for verdict packs,
devlogs, trailers) is therefore answered in
PASS4-APPLICATION.md in its only honest form: no borrowing
is claimed, because no format was observed.

## Licence as seen

**Not seen** (no page). See MANIFEST.md.

## Audio posture

No media obtained; nothing played, transcribed, or
inspected. No transcription was attempted: there is no
speech, and the census-is-a-screen discipline would in any
case only have licensed a bounded slice had a file existed.
Audio silence rule satisfied trivially.
