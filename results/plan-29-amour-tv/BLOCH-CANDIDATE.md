# BLOCH Candidate — Plan 29 (Night School)

- origin_lane: ntranch
- content_label: nsfw
- Candidate: **Same-egress control probing before declaring
  CAPTURE-BLOCKED.** When a target watch-page fetch fails,
  fetch one known-good sibling video (same host, recent
  successful plan's ID) on the *same* egress, cookie jar,
  and method before writing the disposition. Control
  succeeds + target fails with the origin's application
  404 ⇒ target absence (re-run only if URL returns / brief
  amends). Control also fails ⇒ route/egress problem
  (different re-run instruction). Hash the failure bodies:
  this host's intermittent DB-fatal 503 (93 B) hits targets
  and controls alike and must be retried through, while its
  application 404 (384 B) is the target-specific answer.

## Friction log (D-1064)

- What cost time: ~15 min of retries across two egresses
  before the control fetch was run; until then, target 404s
  and DB 503s were interleaved and indistinguishable from
  a Plan 25-style route block, which carries the opposite
  disposition.
- What forced a guess: nothing in the run after the
  control; before it, every disposition on the table
  (route-blocked vs source-gone) fit the same evidence.
- Workaround the next agent would also hit: any future
  rule34video triage that opens with a failing target will
  face the same interleave; the control + body-hash pair
  is the disambiguator.
- Also encountered, recorded as known-defect corroboration
  only: one detached/background exec handoff reported a
  successful 200 capture (293,390 B) that had never
  persisted to disk (the on-disk file remained the 384 B
  404 body). It was caught only because subsequent reads
  went to the file. This restates the estate's standing
  D-567 file-mediated rule; no new claim is made from it.

## Artefact pointers

- `runs/plan-29/MANIFEST.md` §Capture route (this programme,
  night-school-20261105) — per-egress evidence.
- `runs/plan-29/records/route-log.txt` — timed tries, both
  egresses, body SHA-256 prefixes (404 body
  `fd562038072a7a48…`; DB-fatal body `a990dd3f8fdc4d79…`;
  control 200 / 259,287 B on both egresses).
- `runs/plan-29/dl/target-404-sandbox.html` (384 B) and
  `runs/plan-29/dl/control-4293878-sandbox.html`
  (259,287 B) — the paired bodies.
- Contrast case: `runs/plan-25/` — a capture block with
  *no* control run and egresses untried; its disposition
  (route-barred partial) differs from Plan 29's
  (source-not-found) precisely because of the control.

## Per-edit attribution

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| Route diagnosis | Added same-egress control fetch (ID 4293878) after target failures on both egresses | Control 200 / 259,287 B on sandbox AND primo while target returned byte-identical 404 on both — disposition flipped from "route unknown" to "target absent" | adopt |
| Failure taxonomy | Hashed failure bodies instead of trusting HTTP status alone | Two distinct bodies separated cleanly: 384 B app-404 (target-only) vs 93 B DB-503 (target and control) — retries could be scoped to the noise class | adopt |
| Completion checking | Re-read capture target from disk after a background handoff reported success | Handoff's claimed 200 / 293,390 B did not exist on disk; foreground re-run produced the true, repeatable 404 result | confounded (harness defect already dossiered under D-567; the *check* is adoptable, the incident adds no new mechanism) |
