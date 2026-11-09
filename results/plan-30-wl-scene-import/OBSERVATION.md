# Plan 30 — Timed Observation (Pass 1)

## Observation base: **NONE**

The brief calls for dense observation — frames at ≤1 s
intervals plus targeted native-res crops at every UI step,
over the full stated 29 s. **No observation was performed**,
because no artefact was captured: the origin returns 404
for video 3621064 on both terminal egresses while a
same-route control succeeds (MANIFEST.md, INTAKE.md C1–C2).

Accordingly this file records, deliberately:

- Stream facts: **none** (no ffprobe — no file).
- Frame grid: **none** (`frames/README.md` states this in
  the grid's place; no image in this run depicts the source).
- Timed step log: **none** — 0 of the stated 29 s are
  accounted for by viewing; the 29 s are accounted for
  only as *unverifiable plan-stated duration* (INTAKE.md C3).
  That is the honest form of "fully accounted for" available
  to this run, and it is a shortfall against the plan's
  gate, recorded as such in PASS4-APPLICATION.md.
- UI steps / file dialogs / menu paths / settings:
  **none observed.** No setting value is reported anywhere
  in this run, because none was seen.
- Audio / speech: **none** — no file, no whisper slice run.
- UNREADABLEs: **0 counted, by absence** — there was no
  target artefact text to fail to read (INTAKE.md).

## What was observed instead (route-level, not artefact-level)

- The origin's failure taxonomy, re-measured this run and
  identical to Plan 29's: (a) application 404 body, 384 B,
  SHA-256 `fd562038072a7a486e6fb98e7bf223ca494aef557c0d610ae30fe5774c9ee2ae`,
  target-specific; (b) DB-fatal 503 body, 93 B, SHA-256
  prefix `a990dd3f8fdc4d79`, intermittent across target,
  control, and search alike — noise to retry through, not
  an answer.
- The search surface for the exact title remains live and
  surfaces a same-title sibling under a different ID
  (3569655) — a substitution trap, declined (INTAKE.md C4).

## What a re-run owes this plan

In order: (1) re-probe the target URL on both egresses —
if it has returned, run the original micro-plan in full
(page Pass 0 as seen; capture with size + SHA-256 pinned
at the canonical primo path; decode verification; ≤1 s
frame grid + native-res UI crops; step list; bounded
whisper slice; contract note); (2) if it is still 404,
the sibling 3569655 may explain the *name* WL and the
"secret recipe" framing, but it is a 14 s supporters'
teaser for a withheld recipe — studying it would need a
brief amendment naming it as a new target, and it would
still not be the 29 s import operation this plan names.
