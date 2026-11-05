# Plan 05 — Using Stable Diffusion to Create AI NSFW Art (Harry Heck)

- **Source:** https://rule34video.com/video/3257364/using-stable-diffusion-to-create-ai-nsfw-art-harry-heck/
- **Video ID:** 3257364 · **Creator:** Harry Heck (posted by Anime Nyan with permission) · **Duration:** 1:18:51 · **Views at intake:** 66,968
- **Lane:** NSFW-primary / SFW translation: the workflow discipline (not the subject settings) is the same one the SFW image lane runs on
- **Estate targets:** torogao-gen keeper-art rounds, the atelier lane, prompt/seed record discipline
- **Status:** PLANNED

## Why this video

The estate's keeper-art rounds are measured events: recipes are held
constant, one variable moves, provenance is stamped per plate. An
outside practitioner's SD workflow is a control sample — what a
working NSFW artist's generation loop looks like without our
discipline, which parts of it outperform ours, and which of our
rigidities are actually costing quality.

## SHOULD-BE-SEEN (written before viewing)

A complete generation workflow: model/checkpoint choice, prompt
construction, negative prompt habits, sampler and step settings,
resolution strategy, img2img/inpaint use, upscaling, and the curation
ratio — how many generations per keeper, and what the artist does
with the rejects.

## Timed observation focus

- Checkpoint and any LoRA/embedding stack, with versions if shown.
- Prompt structure: ordering, weighting syntax, boilerplate vs
  per-image content; negative prompt contents.
- Sampler, steps, CFG, resolution and any hires-fix settings —
  numerically.
- Iteration behaviour: seeds fixed or rolled, batch sizes, when the
  artist changes the prompt vs the seed vs the settings.
- Fix-up passes: inpaint targets, img2img denoise values, face/hand
  repair strategy.
- Curation: keep rate, and the stated or visible criteria.

## Distillation targets

1. **Prompt grammar** — the reusable structure under the per-image
   content. Question: does it encode anything our recipe records
   don't (character consistency tricks, style anchors)?
2. **Iteration economics** — keepers per hour of generation. Question:
   where does this loop spend time that ours doesn't, and vice versa?
3. **Repair practice** — defect classes the artist fixes in-pass vs
   regenerates. Question: how does their split compare with our
   deterministic-repair-first rule?

## Clean-room rebuild spec

- Reproduce the workflow's *structure* on the estate's own stack
  (torogao-gen or atelier, estate checkpoints only): same pass order,
  same fix-up points, our provenance stamping on every output.
- A/B: one subject generated through their loop structure and through
  the current estate recipe, same seed budget, keep rates recorded.

## Application

- **NSFW application:** findings folded into the next keeper-art
  round's recipe notes as named candidate variables — one at a time,
  never a wholesale recipe swap.
- **SFW translation:** the workflow-structure findings (pass order,
  repair split, curation criteria) apply verbatim to the SFW image
  lane; subject-specific settings do not cross.

## Gate

PASS = the A/B record exists with keep rates and defect census for
both loops, and each distilled technique is marked adopt/adapt/reject
with its evidence. No technique enters a recipe on this plan's say-so
alone — it enters as a candidate variable for a gated round.

## Deliverables

- `results/plan-05-sd-workflow/` — technique sheet, A/B record,
  candidate-variable list.
