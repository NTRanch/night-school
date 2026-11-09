# Plan 40 — How to Make Porn in Blender: Basics — Lighting and Color Grading
## (LOCAL COPY WITH ERRATA — the plan of record is unchanged; errata marked [E#])

- **Source:** https://rule34video.com/video/3213694/how-to-make-porn-in-blender-basics-lighting-and-color-grading/
- **Video ID:** 3213694 · **Duration:** 1:54:44 · **Creator:** (category listing shows none — record at intake)
  - **[E1] Creator as seen at intake: Anime Nyan** (uploader, presenter,
    and model credit on the watch page; member 807029). The plan's
    parenthetical is superseded by the intake record (MANIFEST.md).
  - **[E2] Duration CONFIRMED, no erratum:** page JSON-LD PT1H54M44S
    and ffprobe 6884.033 s agree with the plan's 1:54:44 — Plan 40
    joins Plans 34/37 as a duration exception.
  - **[E3] Licence as seen (not in the plan): CC0** — the page's
    JSON-LD description states "This video is under the creative
    commons zero license." Study-only posture kept regardless.
- **Lane:** NSFW-primary in examples / SFW translation: lighting and grading are universal
- **Estate targets:** All render lanes — companion to Plans 02, 11, 13
- **Status:** PLANNED → **EXECUTED 2026-11-06** (this run; gate result in
  the results dir's PASS3-REBUILD.md / PASS4-APPLICATION.md)

## Why this video

Nearly two hours on the two things that most separate amateur renders from keeper renders: light and grade. This creator's "Basics" series (with Plan 41) is a third independent teaching voice for triangulation, and its lighting half goes deeper than any other single source in the curriculum.

- **[E4] Premise scope note (honest, Plan 17-style):** the lighting
  half does not in fact go deeper than every other source — the
  video is a full production walkthrough in which lighting + grading
  occupy roughly the second hour (Light Start at 46:20 of 1:54:44);
  the first ~46 minutes are character/pose/face/camera work. The
  lighting is taught by dissecting and re-tuning a finished example
  scene (two .blend files alternate on screen), not as a
  from-scratch fixtures course. None of this diminishes the yield —
  the render-pair, EXR and Resolve records are the corpus's most
  complete — but the next reader should not expect a lighting-only
  syllabus.

## SHOULD-BE-SEEN (written before viewing)

A basics course treatment: light types and placement for bodies, exposure discipline, then colour grading in render/compositor — with the reasoning shown on examples.

- **[E5] Correction to the SHOULD-BE-SEEN:** the grading is NOT in
  "render/compositor" — it lives entirely in **DaVinci Resolve**
  (external), and there is no in-Blender exposure discipline to
  record: exposure is a grading act in this pipeline (the EXR
  leaves Blender drastically dark by design). INTAKE.md carries the
  pre-registered claims and their falsifiers as written before
  viewing.

## Timed observation focus

- Lighting setups per example: fixtures, values, distances.
- Exposure and colour-management settings (view transform, look) — numerically.
- Grading chain: where it happens (render settings, compositor, external), node by node.
- Comparison rows vs Plans 02/11/13, kept in the running triangulation table.

## Distillation targets

1. **House look decomposition** — what this creator's light+grade produces that settings alone don't explain. Question: taste or missing settings?
2. **Grading contract** — the minimal grade chain that survives across scenes.

## Clean-room rebuild spec

Extend the Plan 02 template with the distilled lighting rig + grade chain as a named variant; one estate still rendered through it and through the current template, judged side by side.

## Application

- **NSFW application:** Keeper stills and scene renders across the games.
- **SFW translation:** Lighting and grade are the SFW render lane's core as well; the variant template is shared.

## Gate

PASS = side-by-side judged with named differences, and the triangulation table updated. Preference without named differences is not a verdict.

## Deliverables

- `results/plan-40-porn-in-blender-lighting-color/` — technique sheet, rebuild record, gate result.
