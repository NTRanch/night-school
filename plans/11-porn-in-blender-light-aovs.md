# Plan 11 — How to Make Porn in Blender — Light AOVs

- **Source:** https://rule34video.com/video/4316378/how-to-make-porn-in-blender-light-aovs/
- **Video ID:** 4316378 · **Duration:** 19:15 · **Creator:** (category listing shows none — record at intake)
- **Lane:** NSFW-primary in examples / SFW translation: AOV compositing is universal render craft
- **Estate targets:** Keeper stills and renders in both lanes, the Blender still pipeline of Plan 02
- **Status:** PLANNED

## Why this video

Light AOVs (arbitrary output variables) are how a render becomes adjustable after the fact: per-light passes composited instead of re-rendered. The estate's still pipeline re-renders to fix lighting; a working AOV discipline is a direct cost cut and a quality lever for every render lane.

## SHOULD-BE-SEEN (written before viewing)

A focused technique video: AOV setup in Cycles, per-light group passes, and the compositor build that relights the beauty from passes.

## Timed observation focus

- AOV/light-group configuration, exactly as set.
- Compositor node tree in full order.
- What the artist adjusts in comp vs what still forces a re-render.
- File format and colour pipeline for the passes (EXR settings).

## Distillation targets

1. **The pass contract** — which passes, at what precision. Question: minimal set that still relights convincingly?
2. **Comp grammar** — the node operations that replace render iterations.

## Clean-room rebuild spec

Add the distilled AOV setup to the Plan 02 scene template as a versioned variant; relight one existing estate render three ways from passes alone, no re-render.

## Application

- **NSFW application:** Relight passes for keeper stills — lighting variants of one render become cheap enough to offer as verdict-pack options.
- **SFW translation:** Identical adoption in the SFW render lane; the pass contract is shared.

## Gate

PASS = three distinct, credible relights from one render's passes. FAIL = name which adjustment still needed the renderer, and why.

## Deliverables

- `results/plan-11-porn-in-blender-light-aovs/` — technique sheet, rebuild record, gate result.
