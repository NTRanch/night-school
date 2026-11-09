# Plan 23 — Blender Tutorial: Geonode for Pillows

- **Source:** https://rule34video.com/video/3881817/blender-tutorial-geonode-for-pillow-s/
- **Video ID:** 3881817 · **Duration:** 2:04 · **Creator:** (category listing shows none — record at intake)
- **Lane:** Lane-neutral technique (procedural soft props)
- **Estate targets:** Scene dressing and ambient-life props in both lanes, geometry-nodes practice
- **Status:** PLANNED

## Why this video

Procedural soft props via geometry nodes: a pillow is the canonical soft-body-looking static prop — seamed, plumped, deformable by parameters. The estate dresses many scenes; a parametric pillow is a small, complete geometry-nodes study with a reusable node group as its artefact.

## SHOULD-BE-SEEN (written before viewing)

A geometry-nodes setup that turns a base shape into a pillow: seam pinch, plump falloff, possibly fabric subdivision — parameterised.

## Timed observation focus

- The node group, node by node, with input parameters listed.
- Base-shape requirements.
- What breaks it (scale, resolution, extreme parameters).

## Distillation targets

1. **The node group as asset** — parameter ranges that stay plausible. Question: where are its cliffs?

## Clean-room rebuild spec

Rebuild the node group from the sheet; parameter sweep across its ranges with renders at the corners; the group is committed as an estate asset candidate with its safe ranges documented.

## Application

- **NSFW application:** Scene dressing for Torogao interiors.
- **SFW translation:** Identical — props are props; the SFW scene work takes the same asset.

## Gate

PASS = node group rebuilt, sweep recorded, safe ranges written. A group that only works at its demo settings is a fail.

## Deliverables

- `results/plan-23-geonode-pillows/` — technique sheet, rebuild record, gate result.

## Errata (2026-11-06, from the Plan 23 execution run — local copy only)

- **Duration is 11:46, not 2:04.** Page JSON-LD PT0H11M46S;
  the acquired file probes at 706.048 s (sha256 ade3ef07…,
  MANIFEST in `runs/plan-23/`). The 2:04 figure is wrong by
  ~5.7×.
- **Creator is KenFurFox** (watch-page info block), not
  unlisted.
- **Premise correction:** the video does not construct a
  pillow (no seam pinch, no fabric subdivision). Per the
  creator's own description and the screen, it teaches a
  **Set Position + Geometry Proximity fake-collision
  deformation** ("kissen" group) that makes a subdivided box
  behave like a soft cushion under a sitter. The rebuild,
  sweep, safe ranges, and gate are in
  `results/plan-23-geonode-pillows/`.
