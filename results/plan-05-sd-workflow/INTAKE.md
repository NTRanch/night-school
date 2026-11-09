# Plan 05 — Intake (Pass 0)

Plan: `repo/plans/05-stable-diffusion-nsfw-art-harry-heck.md`
Item: "Using Stable Diffusion to Create AI NSFW Art" —
Harry Heck, rule34video video 3257364.

## Source as seen (watch page fetched 2026-11-06, primo egress)

- URL: https://rule34video.com/video/3257364/using-stable-diffusion-to-create-ai-nsfw-art-harry-heck/
- Video ID: 3257364
- Page title: "Using Stable Diffusion to create AI NSFW Art - Harry Heck"
- Creator: **Harry Heck** (tutorial author). Poster: **Anime Nyan** —
  the page description reads: "Here is a comprehensive tutorial by
  Harry Heck on how to create NSFW AI Art with Stable Diffusion.
  Thank you for Harry Heck for giving permission to post this
  tutorial." (matches the plan's "posted by Anime Nyan with
  permission").
- Upload date (JSON-LD): 2024-01-21
- Duration (JSON-LD): PT1H18M51S = **4,731 s** — matches the plan's
  1:18:51 exactly. (Captured-file duration pinned in MANIFEST.md.)
- Views at capture: **66,982** (JSON-LD WatchAction count); the
  plan's intake recorded 66,968 on 2026-11-05 — view counts move;
  both numbers are of their moment.
- Renditions offered: 360p / 480p / 720p / 1080p (player config).
  Capture takes 1080p, the highest offered.

## Licence as seen

- **None stated.** Full search of the fetched watch page for
  licence text finds only the player config's opaque
  `license_code` token — no licence statement, no Creative
  Commons mark. Posture per protocol: study only, never
  redistribute; no video file, transcript, or frame enters any
  shipped artifact.

## SHOULD-BE-SEEN (verbatim from the plan, written before viewing)

> A complete generation workflow: model/checkpoint choice, prompt
> construction, negative prompt habits, sampler and step settings,
> resolution strategy, img2img/inpaint use, upscaling, and the
> curation ratio — how many generations per keeper, and what the
> artist does with the rejects.

## Estate ground truth for the A/B (verified from records)

- Estate recipe of record (solo-sheets / D-555/D-802 lane,
  `~/workspace/cast-solo-sheets-20261104/keeper-chain.json` +
  workflow JSONs): checkpoint `waiIllustriousSDXL_v170.safetensors`
  SHA-256 `f116b0c78ff441467b0cdc8f1936e1ed18ea31e9997c7b132b1b8db533f0bd04`,
  sampler `euler_ancestral`, scheduler `normal`, 30 steps, CFG 6.0,
  1024×1280, IP-Adapter PLUS (weight 0.28 for Prima) + ControlNet
  Union openpose 0.5 where the round uses them, ComfyUI own
  instance, A6000.
- Note (recorded, not smoothed): the TG4 keeper round itself ran
  the torogao-gen native stack at 28 steps / CFG 5.5 / 832×1344 /
  DPM++ 2M Karras (`round-tg4/REPORT-TG4.md`). The A/B's Loop E
  uses the **ComfyUI solo-sheets recipe** named in the tasking,
  since Pass 3 runs on primo ComfyUI; the TG4 numbers are context,
  not the Loop E recipe.
- Census language of record: **CLEAN / RULABLE-WITH-DEFECTS /
  FAIL** with named defects (TG-round usage) — reused verbatim
  for the A/B census.
- Subject: **Prima**; identity reference both loops =
  `full-rigs-20261103/keeper-art-reanchor/prima/anchors/FACE-CLOSE-prima.png`
  SHA-256 `aeabe6c3ecbe5a25adbadb4f47cdb73d2325792da350bf6f7a5ffad50ee72e31`
  (the same gated face-close anchor the solo sheets used).
