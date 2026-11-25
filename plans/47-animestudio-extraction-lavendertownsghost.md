# Plan 47 — AnimeStudio Setup and Model Extraction Tutorial

- **Source:** https://www.youtube.com/watch?v=cLzMA0YEGhQ
- **Video ID:** cLzMA0YEGhQ · **Creator:** LavenderTownsGhost · **Duration:** 16:18
- **Lane:** SFW-primary (YouTube pipeline study) / NSFW application: none direct — this plan serves the reference/census pipeline's intake hygiene
- **Estate targets:** The reference/census pipeline (extraction census + import hygiene) — second shelf, YouTube track
- **Status:** PLANNED
- **Status after run:** EXECUTED through Pass 2 on 2026-11-24 (fathom study run, Owner-supplied set) — Passes 3–4 open; census rules landed as reference-pipeline standing rules

## Why this video

The census-grammar companion to Plan 46: where Plan 46 retargets,
this one finds things. It teaches the Genshin-side extraction route
end to end — game profile, map build (with the CAB gotcha flagged
twice), type filtering, the `Avatar_<Body>_<Weapon>_<Name>` naming
grammar with costume/TT variants and codenames, how to pick the real
container (Trigger + Dummy) over the helper rigs (Edit, Ragdoll,
Mannequin) — and then a Blender intake-cleanup routine whose last
item is a named import-defect class the estate adopts outright:
imported references can carry a duplicated mesh shell over the eyes,
and an eye census on any imported reference should assert exactly
one shell per eye.

## Intake notes (2026-11-24)

Owner-supplied YouTube set, fathom route. Full transcript recovered
(346/346 segments; only an `[en]` audio track exists). **Confidence:
VERIFIED** (full transcript; intake frames agree). Blender 4.4.3 on
screen; the estate pins 5.3 — the material-repair step is adopted
subject to re-verification on the pinned build (see the technique
sheet's conflicts).

## SHOULD-BE-SEEN (written before viewing)

A complete community-route extraction: tool setup, map building,
finding one playable character among ~24,000 asset blocks by grammar
rather than by scrolling, exporting it, and cleaning the import
until the face reads correctly.

## Timed observation focus

- Profile and export settings: game type, scale factor, map types.
- Map build: destinations — where each map file actually lands.
- Search discipline: type filters, the naming grammar, variant and
  codename handling.
- Container selection: what distinguishes the playable Animator from
  the helpers.
- Intake cleanup: material fixes (exact node operations), helper
  hygiene, the eye-shell defect and its removal.

## Distillation targets

1. **Naming grammar** — `Avatar_<Body>_<Weapon>_<Name>`, Body
   classes, Costume/TT variants, codenames ≠ display names.
   Question: census grammar for the Genshin-side reference set?
2. **Container identity** — Trigger + Dummy, never Edit / Ragdoll /
   Mannequin. Question: a standing census rule (assert identity
   before counting anything)?
3. **Material repair on intake** — disconnect Alpha→Alpha, Channel
   Packed. Question: adopted as a named step, after re-verification
   on Blender 5.3?
4. **Duplicate eye shell** — Question: a named import-defect class
   with an assertion in the eye census?

Findings: `results/plan-47-animestudio-extraction-lavendertownsghost/TECHNIQUE.md`
— 11 techniques (T7 is the export step; the sheet follows the study's
numbering), each marked Adopt / Adapt / Reject with the reason.

## Clean-room rebuild spec

Pass 3 (open): the adopted census rules are written into the
reference pipeline's intake checklist and exercised on the next
community-route census — container identity asserted, eye-shell
count asserted, material repair applied and re-verified on the
pinned Blender 5.3 build. The estate's fathom/bundle-reader routes
stay primary; this route is the cross-check.

## Application

- **NSFW application:** none direct; the census grammar keeps the
  reference set the Prima programme measures against honest.
- **SFW translation:** extraction census + import hygiene are
  general estate reference-pipeline practice.

## Gate

Pass 4 (open): the intake checklist carrying these rules is used on
a live census and the run record filed here; a census that counts a
helper rig or a duplicated eye shell has failed the gate it now
carries.

## Deliverables

- `results/plan-47-animestudio-extraction-lavendertownsghost/` — technique sheet (landed 2026-11-24), intake-checklist record when Passes 3–4 run.
