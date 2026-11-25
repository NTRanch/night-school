# Plan 49 — Sakuya Hypnosis App → Oral Performance (6393073)

- **Source:** https://rule34video.com/video/6393073/
- **Video ID:** 6393073 · **Creator:** Dr.Misteroku / taka84 · **Duration:** 1:27
- **Lane:** NSFW-primary / SFW translation: none — performance grammar for the estate's adult scene work
- **Estate targets:** Torogao scene-spec authoring (the beat table is written in authoring terms), Prima's hypnosis-grammar line — third shelf, the favourites performance studies
- **Status:** PLANNED
- **Status after run:** EXECUTED through Pass 2 on 2026-11-24 (favourites follow-on wave; dossier of record in the extraction audit) — Passes 3–4 open; the three-layer eye state machine and the gaze phase-lock landed as Prima programme inputs

## Why this video

The set's most complete single performance, extracted *for animating
with Torogao*: a full beat table (expression components, body keys,
timing), a measured stroke cycle (≈2.0 s, descent faster than rise),
and two headline devices — an eye state built as three independent
layers (emissive hue, emissive intensity, pattern swap) with trigger,
transition and lock as three distinct timed events, and gaze
phase-locked to the stroke cycle (eye contact at the top of each
stroke, hair curtaining the face at the bottom). It also names its
own gaps honestly: the standing→kneeling descent is elided by a
black cut, and no release exists — both are spec work.

## Intake notes (2026-11-24)

Fail-closed screen PASS on coding (sole character tag: Sakuya
Izayoi, Touhou — adult-coded by role and by the Owner-supplied
character profile, est. mid-20s; no death/gore/snuff tags, full arc
in scope). Method: ffprobe census, contact sheets at 3 s and 1.5 s,
fine strips at 0.25 s / 0.5 s, 15 full-resolution beat frames.
Reference only (Tier A): measurements, beat descriptions, transfer
analysis — never copied motion data.

## SHOULD-BE-SEEN (written before viewing)

A POV induction-and-performance piece whose state change is carried
by the eyes in separable layers, and whose performance phase times
its eye contact to the work cycle instead of holding it constant.

## Timed observation focus

- The flash: what changes first — light or face — and the lag.
- Eye layers: hue, intensity, pattern — when each moves.
- The pant cycle; the tremor window and where it stops.
- Stroke cycle period, dwell distribution across phases.
- Gaze vs stroke phase; hair secondary lag; hand brace behaviour.
- The joins: what the edit elides.

## Distillation targets

1. **Three-layer eye state** — hue / intensity / pattern as
   independent parameters; trigger, transition and lock as separate
   timed events. Question: the shape of a Torogao iris spec?
2. **Gaze phase-lock** — contact at stroke tops only. Question: a
   spec device (`gaze_target` gated by stroke phase)?
3. **Tempo map** — cycle → deep dwell → shallow finish at near-equal
   periods. Question: dwell distribution, not period, as the tempo
   variable?
4. **Gaps as spec work** — the elided descent; the missing release.

Findings: `results/plan-49-sakuya-hypnosis-oral-performance/TECHNIQUE.md`.

## Clean-room rebuild spec

Pass 3 (open): the beat table is authored as a Torogao scene spec
inside the Prima programme — three-layer iris state machine,
phase-locked gaze, the authored descent and release the source
withholds — with MMD staging (POV camera, focus-pull, overlays, the
phone prop) explicitly *not* transferred as keys.

## Application

- **NSFW application:** Torogao scene authoring; Prima's mb-01/02/03
  missing-beats specs (descent, consolidation, release).
- **SFW translation:** none.

## Gate

Pass 4 (open) is discharged in the Prima programme's verdict packs:
the eye state readable at full blur (the source's own proof), gaze
contact landing on stroke tops, and the authored descent judged as a
performed beat — the source's cut is not available to the rebuild.

## Deliverables

- `results/plan-49-sakuya-hypnosis-oral-performance/` — technique sheet (landed 2026-11-24), rebuild record and gate result when Passes 3–4 run.
