# Plan 45 — Pass 2 Technique Sheet (Distillation)

Source: Activemotionpictures, "Zenless Zone Zero Official 3d models"
(YouTube Short, sCxIjAKp8ts, 0:59). Study run: 2026-11-24, fathom
route. **Confidence: VERIFIED** (narration + all 12 frames at 5 s
intervals agree). A compressed pointer, not a lecture: it *states* a
route in TTS narration and shows the end state (Ellen Joe's official
PMX open in Blender, full MMD rig + toon face). Techniques are
recorded as stated/demonstrated.

- **T1 — The official-model source (00:00:05).** Official ZZZ models
  are distributed via a Bilibili page (link in the description):
  pick the character from a slider, blue download button, get a zip.
  → **Adapt (corroboration)** of the estate's ZZZ intake route
  (official PMX models are the grammar corpus's model source).
- **T2 — PMX import via mmd_tools (00:00:17–00:00:35).** The
  unpacked format is **PMX**. Install the PMX tools (mmd_tools,
  UuuNyaa GitHub releases) via Add-ons preferences, then File →
  Import PMX — the model loads "with all of the bones and
  textures."
  → **Adapt (corroboration)** — with the estate pin (mmd_tools
  4.5.14 / Blender 5.3), **not** the Short's versions. See Conflicts.
- **T3 — VMD motion bake (00:00:44).** Pose Mode → Physics →
  **Import Motion** → target a **VMD** motion file → **Bake**: MMD
  motions land on the PMX rig as baked animation.
  → **Adapt** as a *reference-motion intake*: MMD/VMD sources can be
  baked to curves, then treated as reference only under D-1397
  (analysis → scene spec), never shipped as animation.

## Conflicts — flagged, not silently adopted

- **Version drift.** The Short shows mmd_tools v2.10.3 on a Blender
  4.x-era install — older than the estate pin (mmd_tools 4.5.14,
  Blender 5.3). The route is corroborated; the versions are **not
  adopted**.
- **Extracted game models/animations** are Tier A: study,
  measurement and reference only — never shipped.
