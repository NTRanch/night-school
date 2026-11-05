# Plan 24 — Tentacle Monster WIP 3

- **Source:** https://rule34video.com/video/3666838/tentacle-monster-wip-3/
- **Video ID:** 3666838 · **Duration:** 1:48 · **Creator:** (category listing shows none — record at intake)
- **Lane:** NSFW-adjacent (creature work) / SFW translation: curve-driven appendage animation is general
- **Estate targets:** Creature/appendage rigging — Torogao creature work, any curve-driven limb or tail in SFW work
- **Status:** PLANNED

## Why this video

A 1:48 work-in-progress clip of a tentacle creature: not a tutorial, but WIP artefacts show rig state honestly. Tentacles are the hard case of curve-driven appendages (spline IK, sine layering, tip control) — the same rig problem as tails, hair masses, and rope systems the estate already fights.

## SHOULD-BE-SEEN (written before viewing)

A rig demonstration: appendages moving under their control system, likely with the control rig visible or inferable.

## Timed observation focus

- Appendage control structure, as inferable: bone chains vs spline IK vs simulation.
- Motion layering: base wave + directed motion + tip behaviour.
- Interaction: does anything get touched/held, and how is that registered?

## Distillation targets

1. **Appendage control grammar** — how directed intent and idle wave combine. Question: which layer does the animator touch?

## Clean-room rebuild spec

Reference-plus: if the control structure is inferable with confidence, a minimal estate test rig (one appendage, the inferred layering) is built and compared. If not inferable, the plan closes as reference-only with that stated.

## Application

- **NSFW application:** Creature and rope-system direction for Torogao.
- **SFW translation:** Curve-appendage layering serves tails/hair/ropes in SFW character work identically.

## Gate

PASS = control grammar stated with evidence or the reference-only closure recorded. Guessing a rig from pixels and presenting it as fact is a fail.

## Deliverables

- `results/plan-24-tentacle-monster-wip-3/` — technique sheet, rebuild record, gate result.
