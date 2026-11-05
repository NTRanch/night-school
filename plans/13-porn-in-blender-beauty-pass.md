# Plan 13 — How to Make Porn in Blender — Recreating Beauty Pass

- **Source:** https://rule34video.com/video/4307858/how-to-make-porn-in-blender-recreating-beauty-pass/
- **Video ID:** 4307858 · **Duration:** 34:18 · **Creator:** (category listing shows none — record at intake)
- **Lane:** NSFW-primary in examples / SFW translation: beauty-pass compositing is universal
- **Estate targets:** Plan 02/Plan 11 render lane, keeper still finishing
- **Status:** PLANNED

## Why this video

The companion to Plan 11: rebuilding a beauty pass from components is the compositing half of modern render finishing — denoise control, pass recombination, and grade-on-top. Together 11+13 cover the estate's whole post-render surface.

## SHOULD-BE-SEEN (written before viewing)

The artist decomposes and recreates a beauty pass in the compositor: which passes feed it, in what math, and what the recreation buys over the renderer's own output (control of noise, fireflies, and per-component grade).

## Timed observation focus

- Pass list and recombination math, node by node.
- Denoise strategy: where it happens, what it costs in detail.
- Differences the artist demonstrates between renderer beauty and recreated beauty.

## Distillation targets

1. **Recombination recipe** — the exact pass math. Question: does it reproduce the renderer beauty bit-for-bit before modification (the honesty check of any recreation)?
2. **Control surface** — what becomes adjustable that wasn't.

## Clean-room rebuild spec

Extend the Plan 11 template variant: recreation must first match the renderer beauty (measured), then produce one graded variant the renderer alone could not.

## Application

- **NSFW application:** Keeper still finishing: grade variants per render for verdict packs.
- **SFW translation:** Shared with the SFW render lane unchanged.

## Gate

PASS = match-then-modify both demonstrated with measurements. A recreation that cannot match the original is recorded as an approximation, not adopted silently.

## Deliverables

- `results/plan-13-porn-in-blender-beauty-pass/` — technique sheet, rebuild record, gate result.
