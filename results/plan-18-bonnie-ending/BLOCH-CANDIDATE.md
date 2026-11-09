# Bloch candidate — Plan 18 run

- origin_lane: ntranch
- content_label: nsfw
- origin: Night School Plan 18 execution run, 2026-11-06
  (artefact: rule34video 4283554, an NSFW-lane study source)

## Lesson

**Verify a plan's stated duration and artefact type at
intake — from the page's structured metadata AND the captured
file's probe — before designing the observation.** Plan 18
was written and approved as a 36-second finished clip. At
intake the page JSON-LD said PT0H17M00S and the captured file
probed at 1020.067 s: the plan's duration was wrong by ~28×,
and the artefact was a different type entirely (a 17-minute
Source Filmmaker finishing session, not a finished clip).
Every downstream design decision in the brief (frame counts,
sampling density, expected beat structure) was built on the
wrong numbers and had to be re-scoped mid-run.

Evidence pointers:
- `runs/plan-18/INTAKE.md` (premise corrections 1–3, with the
  page and probe numbers side by side)
- `runs/plan-18/MANIFEST.md` (capture record: 208,432,388 B,
  30,602 frames, 1020.067 s)

## Friction report (D-1064 format)

- **What cost time / forced a guess / forced a workaround:**
  the brief's observation design (dense sampling of a 36 s
  clip at 60 fps) was inapplicable on contact with the real
  artefact; the run re-scoped to a census-then-focus design
  (whole-file motion-energy census → cluster resolution →
  timeline reads) that the brief had not contemplated.
- **Component:** Night School plan authoring (the listing →
  plan step), not the execution tooling.
- **Change made in this run:** none to the plan template
  (outside this run's authority); the errata was filed to the
  local copy of Plan 18 only.
- **Observed difference:** with the census-first design, the
  artefact's actual structure (one 20.000 s shot; no playback)
  was established from measurements within the same run —
  the workaround worked, but it was invented on the spot.
- **Verdict:** candidate for a standing intake rule —
  *no plan's duration/type field is trusted past intake;
  JSON-LD + ffprobe numbers replace it in the run's first
  hour, and a ≥2× discrepancy triggers an explicit re-scope
  note in INTAKE.md.* (Corroborating pattern, not a duplicate:
  Plan 15's plan duration was also wrong, by 131 s on
  ~4,900 s; Plan 14 closed at intake on a premise failure.
  Three of the Bonnie-series plans carried premise errors.)
