# Plan 04 — MUGEN Factory: Streaming the Creation of a Stage

- **Source:** https://rule34video.com/video/3417736/mugen-factory-streaming-the-creation-of-a-stage/
- **Video ID:** 3417736 · **Creator:** Fapmaster/Viket · **Duration:** 1:08:47 · **Views at intake:** 11,579 · **Tags:** pixel art
- **Lane:** SFW-primary in substance (stage construction) / NSFW application: scene backgrounds for adult work
- **Estate targets:** Torogao and Strobe scene backgrounds, jam-game stages, the ambient-life and parallax toolkits
- **Status:** PLANNED

## Why this video

MUGEN stages are the purest form of a problem the estate has in every
medium: a layered 2D scene that must read as a place — parallax,
animated background elements, a defined floor plane, and a camera that
moves without breaking the illusion. A full streamed stage build shows
the whole construction, including the boring parts tutorials edit out.

## SHOULD-BE-SEEN (written before viewing)

Stage art sliced into depth layers, a stage definition wiring layers
to parallax factors and animation, bounds set so fighters (and the
camera) stay inside the illusion, and the iteration loop as elements
are added and judged in-engine.

## Timed observation focus

- Layer plan: how many layers, what lives on each, the depth story.
- Parallax factors per layer (the actual delta values) and the
  reasoning when stated.
- Animated elements: frame counts, timing, what gets animation and
  what stays still (the ambient-life budget).
- Floor and bounds: zoffset, boundleft/right, screenleft/right
  equivalents in the stage definition — copied exactly.
- Art sourcing: drawn, ripped, composited — and the cleanup each
  source needs before it layers cleanly.
- In-engine judgement: what the creator checks by playing the stage,
  not by looking at the files.

## Distillation targets

1. **Layer grammar** — the rule set deciding what earns a layer.
   Question: does it map onto Torogao scene composition and the
   estate's parallax work one-to-one, or is fighting-game staging a
   special case?
2. **Parallax calibration** — how factors are chosen and tuned.
   Question: tuned by formula or by eye, and does the result survive
   a different stage width?
3. **Ambient budget** — which background elements move. Question:
   what principle separates "alive" from "busy"?

## Clean-room rebuild spec

- Build one stage from the technique sheet: an estate-authored scene
  (no source art), layered and wired per the distilled grammar,
  running in MUGEN or the estate's own 2D scene runner with matching
  parallax behaviour recorded side by side.

## Application

- **NSFW application:** one Torogao scene background rebuilt to the
  distilled layer grammar.
- **SFW translation:** one jam-game stage/level background on the same
  grammar — this plan's SFW value is primary, not incidental.

## Gate

Camera-sweep evidence: recorded sweep across both stages; PASS = no
layer separation artefacts, bounds hold, ambient motion reads at
playing distance.

## Deliverables

- `results/plan-04-mugen-stage/` — technique sheet, layer grammar,
  rebuilt stage, sweep evidence.

## Errata (from the 2026-11-06 execution run, LOCAL copy only)

- Views at capture (2026-11-06): 11,592 (plan intake recorded
  11,579 on 2026-11-05; counts move, both are of their moment).
- The SHOULD-BE-SEEN expectation of "parallax factors" per
  layer did not materialise: the finished stage ships every
  delta at 1,1, with depth carried by compositing, file order,
  scale, and one layerno=1 ghost. The delta doctrine exists in
  the creator's template comments (floor always 1,1 low-res /
  2,2 high-res; lower delta = further) but is not exercised in
  this build. Full record: runs/plan-04/OBSERVATION.md (DG1).
- "Pixel art" tag: the stage plate is a painted anime
  background, palette-reduced to 8-bit on .sff import.
