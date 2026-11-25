# Plan 57 — Technique Sheet (from the RECIPE of record, 2026-10-30)

Source: Danbooru post 5447477, "Raiden x Yae — Animation"
(vicineko, kitsuneecchi; voice kassioppia), 137.47 s. Extraction:
fathom RE of record, `~/workspace/fathom-re-5447477-20261030/`
(RECIPE.md, motion records, manifest) — this sheet distils it; the
RECIPE remains the document of record. Owner-supplied emulation
target 2026-10-30; screened under the Danbooru video carve-out
(108 tags, PASS); byte-exact download (44,183,337 B, sha256
32d97a1e…b0893). Tier I law: technique and pattern level only.

## What was measured (observed)

- **Container.** H.264, 1280×720, **30 fps**, 4,124 frames,
  137.47 s; AAC 44.1 kHz stereo.
- **Every frame is new.** 4,098 of 4,124 frames are unique
  drawings (99.4%). No holds, no frame reuse, no stepped cycles —
  the motion is fully interpolated 3D, rendered at 30 fps.
  Perceptual clustering finds **34 clusters** — the framing
  families the unique frames fall into.
- **It is not a loop.** File-level loop class: *segment library*;
  loop seam ratio **22.2**. The file is an edited scene.
- **Shot structure.** 24 measured cut points → 25 shots of
  3.5–19.4 s, median ≈ 5 s. The **longest shot is the last**:
  118.1–137.5 s (19.4 s), one sustained face-to-face framing.
- **Cycles live inside shots.** Motion periods of 10 / 15 / 20
  frames (**0.33 / 0.50 / 0.67 s**) — the rocking-cycle band. (The
  2-frame period on other segments is render cadence, not a motion
  claim.)
- **Audio.** 158 events: voice-short 63, impact 58, silence 21,
  voice-sustained 16. ≈60 events/min; median inter-onset **0.8 s**;
  audio active 45.6% of runtime; envelope periodicity **1.35 s**
  (r = 0.40, resolved). Overall RMS 0.137 — a modest, voice-forward
  mix.
- **Contact is the default state.** In the final shot, the contact
  zone is active for **564 of 581 frames (97%)** in 7 runs — the
  figures are in continuous near-contact interaction for the whole
  19.4 s, including a hand rising to the partner's face. Activity:
  right figure 2.64 vs left figure 2.08 mean — the receiving figure
  is the more expressive one; the after-phase is face-led.
- **Palette families:** deep plum shadows `#540e46` / `#600c31`;
  hot magenta-red mids `#b31348` / `#a91447`; warm rose skin
  highlights `#ec8584` / `#da6869`. Twilight magenta environment,
  red foliage accent, warm skin — high chroma separation between
  world and bodies.

## Editorial phases (asserted, provenance recorded)

| Phase | Time | Content |
|---|---|---|
| act-oral-focus | 0.0–36.7 s | Oral focus; one partner reclining |
| act-varied-framings | 36.8–99.2 s | Varied positions and framings, sustained contact |
| act-climax | 99.3–118.0 s | Climax region (72–86% through the runtime) |
| surface-after-phase | 118.1–137.5 s | Single held shot; face-to-face exchange, flick, gaze |

Also asserted from viewing: expressions evolve through intermediate
positions (no snapping); the rhythm pauses for a facial reaction or
a hand repositioning, then resumes — it is performed, not
metronomic.

## What cannot be established from the file

Exact rig topology, blendshape list, or whether hair/ear lag is
physics-simulated or hand-keyed (the lag itself is observed).
Voice↔motion synchronisation at file level by this method (no
global visual period recovered): sync is asserted from viewing, not
measured. Fine face metrics: the face-track activity region
saturates at analysis width on this content. Render settings beyond
what the tags assert (Blender, cel shading).

## Codification (Pass 3/4 equivalents — landed 2026-10-30)

- **Handfast translation** — the recipe rebuilt in the jam form
  (Rust), committed in handfast/docs/ (494f126).
- **Torogao-main translation** — the recipe rebuilt for Torogao,
  with acceptance metrics: contact-zone ≥95%, climax band 72–86%
  (`TOROGAO-RECIPE-5447477.md` in the torogao P0 tree).
- Media + excerpts deleted post-verification per D-248;
  manifest/records/strips retained. Local video copy: **not held**
  (by policy, not by loss).

**Status: extracted ✓, distilled ✓, codified ✓ (two consumer
translations).** The audit of record marks this the set's one
fully-closed extraction.
