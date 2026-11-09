# Plan 22 — Blender Tutorial: Shrinkwrap Sleeve

- **Source:** https://rule34video.com/video/3881849/tutorial-shrinkwarp-sleeve-blender/
- **Video ID:** 3881849 · **Duration:** 2:31 · **Creator:** (category listing shows none — record at intake)
- **Lane:** Lane-neutral technique (clothing fit) / examples may be adult, method is not
- **Estate targets:** Outfit fitting across the model fleet — factory fitting, Torogao/Strobe wardrobe work
- **Status:** PLANNED

## Why this video

Two minutes on one modifier: shrinkwrap-fitting a sleeve to an arm. Clothing fit is a standing estate cost (fitted outfits on parametric bodies, Yui's rope-as-outfit register, every wardrobe variant). A tight micro-tutorial on exactly that joint is high value per minute.

## SHOULD-BE-SEEN (written before viewing)

A single-technique demo: sleeve mesh, shrinkwrap modifier settings, the fix for the usual failures (offset, pinching at the joint, projection direction).

## Timed observation focus

- Modifier stack and every setting value.
- Target/offset choices and the failure each prevents.
- Any vertex-group limiting (where the wrap applies).

## Distillation targets

1. **Fit recipe** — settings as a named preset. Question: does it survive a bent joint (the sleeve case is literally the hard case) or only a straight arm?

## Clean-room rebuild spec

Apply the preset to one estate outfit piece over a posed (bent) joint; deformation checked at three joint angles.

## Application

- **NSFW application:** Wardrobe fitting for the cast fleets.
- **SFW translation:** Identical — clothing fit is rating-blind; SFW character work adopts the preset unchanged.

## Gate

PASS = clean fit at all three angles with no hand repair. Pinch or slide at the bend is recorded with the angle, not smoothed over.

## Deliverables

- `results/plan-22-shrinkwrap-sleeve/` — technique sheet, rebuild record, gate result.

## Errata (added by the Plan 22 execution run, 2026-11-06, local copy only)

- **Duration is 12:27, not 2:31** (page JSON-LD PT0H12M27S;
  probed file 746.602 s — runs/plan-22/MANIFEST.md). The
  "single-modifier micro-tutorial" framing is also wrong:
  the stack is Shrinkwrap + Surface Deform + Solidify.
- **Creator: KenFurFox** (watch page, "Uploaded by").
- **Premise:** the "sleeve" is a responsive tube over an
  armature-animated shaft asset, not a garment sleeve on an
  arm; no bent joint is demonstrated. The technique and the
  plan's rebuild/gate were executed as written; gate result
  FAIL at the bent angles (see results/plan-22-shrinkwrap-sleeve/).
