# Plan 29 — Structural Observation

## Observation base: **NONE**

The triage method calls for structural sampling (grid
~1/30 s plus boundary-targeted frames plus stream facts)
sufficient to identify the artefact and, if packaged, its
segment structure. **No sampling was performed**, because
no artefact was captured: the origin returns 404 for video
3637868 on both terminal egresses while a same-route
control succeeds (MANIFEST.md, INTAKE.md).

Accordingly this file records, deliberately:

- Stream facts: **none** (no ffprobe — no file).
- Frame grid: **none** (`frames/README.md` states this in
  the grid's place; no image in this run depicts the source).
- Segment table: **none** — no openings, recurring
  furniture, segment boundaries, or runtime proportions
  were observed, and none are reconstructed from the
  plan's stated 14:51, which is itself unverified.
- Framing device: **not observed.**
- Runtime discipline / format clock: **not measurable.**

## What was observed instead (route-level, not artefact-level)

- The origin's failure taxonomy, measured this run:
  (a) application 404 body, 384 B, SHA-256
  `fd562038072a7a486e6fb98e7bf223ca494aef557c0d610ae30fe5774c9ee2ae`,
  served for the target ID from both egresses;
  (b) database-fatal 503 body, 93 B, SHA-256 prefix
  `a990dd3f8fdc4d79`, served intermittently for target
  *and* control alike — origin noise, distinguishable from
  (a) by body and hash. A triage that retries through (b)
  and reads (a) as its answer will not mistake flakiness
  for absence, or absence for flakiness.
- The site search surface remains live for the name
  "amour tv" and lists a sibling instalment (3623811,
  "Amour TV『W.T.Dinner』") but not the target — recorded
  in INTAKE.md as a lead for any re-run, not as structure.

## What a re-run owes this plan

In order: (1) re-probe the target URL on both egresses —
if it has returned, proceed with the original triage
(page Pass 0 as seen; capture with size + SHA-256 pinned;
decode + packet-span verification; ~1/30 s grid +
boundary frames; segment table; borrowings verdict);
(2) if it is still 404, check whether the sibling
3623811 or the maker's listing explains the withdrawal
(renamed/re-uploaded IDs are common on this host) — but a
*different* ID is a different artefact and must not be
silently substituted for 3637868; substitution would need
a brief amendment, not an agent decision.
