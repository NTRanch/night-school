# Plan 07 — How to Make 3D Porn Cum Simulation, Part 1: Houdini FLIP Fluid to Blender

- **Source:** https://rule34video.com/video/3213819/how-to-make-3d-porn-cum-simulation-from-houdini-to-blender-part-1-flip-fluid-ve/
- **Video ID:** 3213819 · **Creator:** Mushen (sponsored by Anime Nyan) · **Duration:** 1:07:48 · **Views at intake:** 18,282 · **Licence:** stated CC0 on the video page (see Plan 06 note) · **Also covers:** Vellum, not only FLIP — observation list extended accordingly
- **Lane:** NSFW-primary in subject / SFW translation: FLIP simulation and cross-DCC cache discipline are general fluid craft
- **Estate targets:** Torogao fluid systems, Blender pipeline work, any future fluid effect (water, drink, rain) in either lane
- **Status:** PLANNED — run before Plan 06 (Part 2)

## Why this video

FLIP is the industry-standard fluid solver and the estate has no
fluid-simulation practice at all: every fluid in current work is faked
or shader-only. A complete Houdini→Blender FLIP walkthrough — emitter
setup, solver settings, meshing, cache export, Blender import — is the
foundation course, and its numbers are the kind that take weeks to
converge on alone.

## SHOULD-BE-SEEN (written before viewing)

A Houdini FLIP setup tuned for a small-scale, viscous, short-duration
emission (very different from the water tanks FLIP defaults assume):
particle separation, viscosity, surface tension, collision geometry
handling, meshing settings, and an Alembic (or equivalent) cache
handed to Blender with scale intact.

## Timed observation focus

- Emitter: geometry, emission timing, initial velocity, and how the
  source is animated.
- Solver numbers, copied exactly: particle separation, grid scale,
  viscosity, surface tension, substeps, collision settings.
- Scale decisions: scene units and real-world size assumptions — the
  single largest small-fluid failure source.
- Meshing: particle-to-mesh settings, smoothing, droplet/blur
  handling.
- Export: format, frame range, cache size, naming; import scale and
  orientation fixes in Blender.
- Iteration: what the creator re-sims vs adjusts downstream, and the
  sim-time cost of their settings.

## Distillation targets

1. **Small-scale FLIP recipe** — the solver numbers as a named
   starting preset. Question: how far are they from FLIP defaults,
   and does each deviation have a stated reason?
2. **Scale discipline** — the unit choices that make small fluids
   behave. Question: is it documented in the video or only visible
   in the setup?
3. **Cache contract** — the Houdini→Blender handoff format and its
   failure modes. Question: does the same contract serve a
   Houdini→estate-engine handoff?

## Clean-room rebuild spec

- Rebuild the sim from the technique sheet: Houdini (or the estate's
  available FLIP route) at the distilled preset, cache exported and
  imported into Blender, rendered evidence frames at emission peak.
- Parameter sensitivity strip: three sims varying the single most
  load-bearing setting ±, so the preset arrives with its tolerances
  known, not just its values.

## Application

- **NSFW application:** the preset and cache contract feed Plan 06's
  integration rebuild.
- **SFW translation:** the same preset class, re-tuned for water-like
  viscosity, is the starting point for any SFW fluid (fountains,
  drinks, weather) — the study records both tunings' deltas.

## Gate

PASS = rebuilt sim matches the video's result class (coherence,
strand/droplet behaviour, settle) at the evidence frames, and the
sensitivity strip is recorded. FAIL on scale or meshing returns to
Pass 2 with the frame evidence.

## Deliverables

- `results/plan-07-cum-sims-part-1/` — technique sheet, FLIP preset,
  sensitivity strip, cache contract note.
