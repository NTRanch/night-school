# Bloch candidate — Night School Plan 25 (attempts 1–2)

- origin_lane: ntranch
- content_label: nsfw
- source: Night School Plan 25 triage, attempts 1–2, 2026-11-06
  (`~/workspace/night-school-20261105/runs/plan-25/` —
  MANIFEST.md §Capture route [attempt 1];
  MANIFEST-2.md §Capture route [attempt 2];
  `records2/page-loop-primo.log`, `records2/page-loop-sandbox.log`)

## Lesson (a browser-fetch block is not a capture block)

A policy block on the browser text-fetch tool for a domain
says something about **that route only** — it is not a
finding that the domain cannot be captured, and it must
never be recorded as a global capture block. Proven both
ways by this plan:

- **Attempt 1** fetched the rule34video watch page via the
  browser text-fetch tool, hit the domain policy block, and
  treated it as terminal: no other route was tried, and the
  plan closed CAPTURE-BLOCKED on a route error.
- **Attempt 2** used the programme's established route of
  record — terminal egress (`curl` with a warmed cookie jar
  from the sandbox and/or via primo-ssh) — and both egresses
  reached the origin immediately and received real origin
  HTTP answers (homepage 200; watch-page 404/503 bodies).
  Every prior executed plan (01–24) captured this domain the
  same way; Plan 04's MANIFEST already recorded the identical
  browser block routed via primo terminal.

**Transferable rule:** for this domain (and by extension any
domain with an established capture route), a brief names the
route of record, a worker uses it first, and a block on any
*other* route is reported as a per-route fact — never as the
run's outcome. A capture-blocked verdict requires the route
of record itself to have failed, with per-route evidence.

**Second, separable fact (not the lesson, its context):** the
terminal route can still honestly fail — attempt 2's failure
was an origin video-page outage (homepage intermittent
200/503; video pages alternating a 384 B 404 shell and a
93 B 503 database body, degrading to timeouts, never a 200), also recorded by Plan 24 the same
night. Outage ≠ block: the proportionate response is
detached retry loops on both egresses with the per-route
evidence logged, and the plan stays open rather than closed
on the merits.

## D-1064 friction log

- What cost time: attempt 1 as a whole — a full triage run
  spent reaching a verdict ("blocked") that a route check
  would have dissolved in one command. The fix is brief-side
  (name the route of record; attempt 2's brief did, and the
  route worked instantly) and worker-side (a tool block is
  scoped to the tool until the sanctioned route is tried).
- Workaround forced in attempt 2, worth keeping: when the
  origin alternates 404-shell/503-DB on the video route with
  only an intermittently healthy homepage,
  do not hand-retry — launch file-mediated detached loops on
  BOTH egresses (45 s interval, ~60 attempts) and read the
  outcome from the `.done`/log files. Artefacts:
  `runs/plan-25/records2/fetch-page-loop.sh` (the loop script),
  `records2/page-loop-primo.log` (60 attempts, complete),
  `records2/page-loop-sandbox.log` (59 attempt lines logged;
  the attempt-60 outcome line is absent from the log — a
  logging gap recorded in MANIFEST-2.md, not filled).
- One guess avoided, recorded for the next run: a homepage
  200 does NOT certify the video route. Health-check both the
  homepage and a known-good video page before budgeting a run
  against this origin.

---

## Attempt 3 addendum (2026-11-06) — the flapping-origin discrimination problem

Birth metadata unchanged (origin_lane=ntranch,
content_label=nsfw — see header). Attempt 3 closed Plan 25
as SOURCE-NOT-FOUND; the transferable friction is *how*
that verdict was reachable at all.

**The trap:** attempt 3's origin was neither up nor down —
it flapped at the database layer, returning the 93 B
`[FATAL]: can't connect to database` 503 body at random to
the homepage, a known-good control video page, and the
target alike (control: 4× 503 in 10 fetches; target: 3×
503 in 10). A target-only probe in such a window reads
exactly like attempt 2's total outage and invites either
another 120-attempt loop or a false CAPTURE-BLOCKED. The
attempt-2 lesson ("outage ≠ block; loop both egresses")
is necessary but not sufficient here: looping the *target*
cannot distinguish "origin down" from "item gone" when
the origin fails stochastically.

**What resolved it:** same-egress, same-round **control
pairs**. Fetch the target and a known-good control video
page back-to-back on each egress, and judge only the
rounds where the origin answered. In 5 clean pairs the
control returned 200 / 259,287 B while the target
returned the byte-identical 404 shell — a discrimination
no volume of target-only retries could have produced.
Rule for the next flapping-origin triage: interleave
control and target per round, count only answered rounds,
and let ~5 clean pairs decide; cap total fetches (this
verdict took 22 fetches in ~3.5 minutes, vs attempt 2's
120+ in ~69 minutes for no verdict).

**Silent workaround, recorded:** none beyond the above —
no route substitution, no browser fetch (policy-blocked
route stayed untouched), no sampling ahead of the
bar-class screen (the screen stayed unrun for want of
metadata; absence closed the question instead). One
near-miss worth naming: primo's *initial* probe returned
503 for both homepage and control while its target
returned the real 404 — read alone, that egress would
have suggested "origin down on primo"; only the paired
confirmation rounds corrected it. Per-egress first probes
are not verdicts either.

## D-1064 friction log (attempt 3)

- What cost time: nothing material — the control-first
  order in the brief made the verdict cheap. The residual
  cost is inherited: two prior attempts (~a full run and
  ~69 min of loops) were spent before the control-pair
  question was posed. The fix is procedural (adopted
  above): control-pair probing is step 1, not a fallback.
- Guess avoided: the 503 flap could have been smoothed
  into "origin still degraded" (branch c). It was not:
  with the control serving 200 in the majority of
  attempt-3 fetches, branch (c) was affirmatively excluded
  by counts, and the 404-shell hash (fd562038…) was
  matched byte-for-byte against attempt 2's shell before
  the SOURCE-NOT-FOUND call.

## Per-edit attribution rows (attempt 3)

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| Probe design | Control probe (homepage + known-good 4293878) run *before* target, both egresses | First sandbox probe set already discriminated: control 200 / 259,287 B vs target 404-identical, in <4 s | adopt |
| Probe design | Confirmation rounds interleave control+target per egress (4 rounds, 45 s spacing) | 5 clean control-200/target-404 pairs across both egresses; flap rounds identifiable as flap (both-503 or control-200/target-503) instead of contaminating the verdict | adopt |
| Verdict rule | Branch chosen by answered-round pairs, not by raw target tally (7× 404 vs 3× 503 alone is ambiguous under flap) | SOURCE-NOT-FOUND rests on pair evidence; the 3 target 503s attributed to the DB flap also seen on control/homepage | adopt |
| Egress reading | Primo initial probe (control 503, target 404) NOT read as a verdict | Later primo rounds 1–2 gave clean pairs (control 200, target 404); the initial 503 pair would have mislabelled the egress as down | confounded (single-probe reading vs later rounds — the correction came from the rounds, but which primo fetch was "typical" is not separable from flap timing) |
