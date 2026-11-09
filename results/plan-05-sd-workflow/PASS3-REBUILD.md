# Plan 05 — Pass 3: A/B Rebuild (Prima, their loop vs estate loop)

Status: COMPLETE (generation + repair + census, 2026-11-06). Agent census read;
keeper judgements are Owner eye items (PASS4). No Owner PASS declared.

## Budget (fixed before generating)

12 seeds per loop, SAME seed list 51001–51012, one plate per seed.
Subject: Prima. Identity reference (Loop E only, per its recipe): FACE-CLOSE
anchor SHA `aeabe6c3…e31` (see INTAKE). Driver: `gen_ab.py`; job files
`AB/jobs-e.json`, `AB/jobs-t.json` (generator `make_jobs.py`); per-plate
provenance JSON beside every PNG in `AB/`.

## Loop E — estate recipe of record, unchanged

Solo-sheets Loop E verbatim (keeper-chain.json + workflow record): WAI
Illustrious v170 (SHA `f116b0c7…3f0bd04`), euler_ancestral/normal, 30 steps,
CFG 6.0, 1024×1280, BUILD prompt + negative verbatim, IP-Adapter PLUS 0.28,
ControlNet Union openpose 0.5 on pose_build (SHA `1357c842…`). No repair pass
(estate discipline: plates stand as generated; deterministic repair is a
separate gated step, not part of this loop's census).

## Loop T — their loop structure on the estate checkpoint

Pass order from the sheet: txt2img (their grammar + defaults) → hires ×1.8 →
curation → face inpaint at their anime denoise.
- Prompt (their grammar: subject + plain descriptors, no quality head):
  "Prima, nude, solo, 1girl, adult woman, silver hair, long wavy hair, red
  eyes, heart-shaped pupils, medium breasts, sitting on a couch, looking at
  viewer"
- Negative verbatim: "bad-hands-5, bad-artist, EasyNegative"
- euler_ancestral/normal, 20 steps, CFG 7.0, 768×768 base, clip skip 2,
  hires ×1.8 (model-mode 4x-AnimeSharp, 15 steps, denoise 0.4) → 1382×1382.
- No IP-Adapter, no ControlNet (his loop has neither).
- Repair pass (`repair.py`): face-zone inpaint per his settings — only-masked
  crop at 1024², DPM++ 2S ancestral + Karras, 20 steps, CFG 7, denoise 0.5
  (his anime value), seed = plate seed, region prompt "face, high quality"
  (the prompt form his own failure taught), feathered paste-back.

### Substitutions (each forced, each recorded)

1. Character LoRA (ElinaliseV6 role) → descriptive tags. No Prima LoRA exists
   in the estate stack; downloads barred. Loop T therefore tests text-only
   identity, which is also the honest control for TECHNIQUE 1.2.
2. SwinIR_4x → 4x-AnimeSharp.pth (estate upscale model present on primo).
3. Embedding vectors (bad-hands-5/EasyNegative/bad-artist) → their NAMES as
   negative text (no such embeddings in the estate stack). Loop T measures
   the names' text effect, not the vectors; TECHNIQUE 1.1's verdict is
   written to survive this.
4. A1111 inpaint (only-masked, padding 32, blur 4) → ComfyUI crop-inpaint
   equivalent (mask bbox + 64 px pad ≈ padding 32 at 2× crop scale, VAE
   inpaint grow 6 ≈ blur, feathered composite).
5. His checkpoint stack → WAI v170 (mandated: estate checkpoints only).

## Determinism (tasked check)

- Loop T seed 51001 re-run: BYTE-IDENTICAL (SHA `71575809…` both runs).
- Loop E seed 51001: run 2 == run 3 BYTE-IDENTICAL (SHA `5ec1d968…`);
  run 1 (the cold first job on the fresh server process) differs — MAD 1.9074,
  NCC 0.992405, 78.7 % of pixels differ slightly, composition identical.
  Settings records identical across all three runs. Cause class:
  first-inference kernel/autotune selection in a fresh process; steady state
  is byte-deterministic. Same magnitude family as the estate's own Prong 0
  cross-build jitter (MAD ≤ 1.9). Loop T's first job ran second overall
  (server already warm), which is why its "first" run was already steady-state.
  Practical rule recorded for future rounds: discard or re-run the first job
  after a ComfyUI restart before treating outputs as of record.

## Timing (from per-plate records)

Loop E ≈ 14–38 s/plate (38 s = the cold first job). Loop T ≈ 14–20 s/plate
incl. hires, + ≈ 10.5 s/plate repair. Neither loop is time-bound at this
budget; the difference is passes, not minutes.

## Census (agent read, TG language verbatim; sheets cen-E-*, cen-T-*,
cen-TR-* + full plates in AB/)

### Loop E (12 plates, as generated)

- CLEAN 6/12 — E-02, E-03, E-06, E-07, E-08, E-12
- RULABLE-WITH-DEFECTS 6/12 — E-01 (hand merged with held vibrator), E-04
  (minor nipple asymmetry), E-05 (raised-hand fingers merged at knuckle),
  E-09 (navel rendered as concentric ring), E-10 (support hand fist-merged;
  oversized prop), E-11 (prop duplicated on both thighs; mild face drift)
- FAIL 0/12
- Keeper-candidate rate (CLEAN + RULABLE): 12/12. Clean rate: 6/12 (50 %).

### Loop T (12 plates, pre-repair)

- CLEAN 0/12. RULABLE-WITH-DEFECTS 12/12. FAIL 0/12.
- Every plate carries the hands/arms class (fusion into thighs/seat/shadow,
  arms lost behind body or out of frame, elongated fingers): 12/12.
  Named per plate in the working census (T-01 forearm–thigh fusion worst;
  T-03/T-09 least — distinct fingers on the visible hand).

### Loop T post-repair (TR-01…12, face inpaint denoise 0.5)

- Class counts UNCHANGED: CLEAN 0/12, RULABLE 12/12, FAIL 0/12. Faces
  marginally smoother; no seam or identity drift introduced at census scale;
  T-08's mild face drift persists (structural, not surface). The repair pass
  does not touch the loop's dominant defect class (hands/arms), because his
  mask target is the face — the same targeting his video shows.

### Defect-class table (plates affected / 12)

| class | Loop E | Loop T pre | Loop T post |
|---|---|---|---|
| hands/arms (fusion, loss, malformed) | 3 (mild) | 12 | 12 |
| faces (drift/defect) | 1 (mild) | 1 (mild) | 1 (mild) |
| breasts/nipples (asymmetry, placement) | 1 (minor) | 5 | 5 |
| text | 0 | 0 | 0 |
| artifacts (prop duplication, body-detail) | 2 | 0 | 0 |
| composition (subject-dominance breaks) | 0 | 2 | 2 |

### Curation cross-check (his rule applied to both loops)

His observed rule — carry ~1 of a 12-batch forward (~8 %) — applied by the
agent reader: Loop T's carry-forward is T-03 (least-defective), 1/12, matching
his observed rate almost exactly. Loop E under the same single-carry rule
would still carry 1/12 by construction, but it holds 6 CLEAN plates in
reserve; the loops differ in what the batch leaves behind, not in the carry
count.

## Claims verification (from OBSERVATION §9)

- C3 (20 steps enough at his defaults): on the estate checkpoint his step
  count produced coherent plates 12/12 — VERIFIED for coherence; the deficit
  is defect density, not coherence.
- C9/C10 (inpaint repairs faces at 0.35–0.5): VERIFIED mechanically (pass
  runs, faces stable, no drift at 0.5) — and shown to be a face-only tool:
  it cannot clear a hands-class census.
- C11 (upscale before inpaint): followed in Loop T's order by construction;
  no contrary evidence.
- C2 (LoRA 0.5 too weak / 0.8 right): NOT testable (substitution 1) —
  remains UNVERIFIED.
- C1, C4–C8, C12–C14: observational only; see TECHNIQUE/PASS4.

## Files

AB/ holds: 12 E plates + 12 T plates + 12 TR plates, each with a provenance
JSON (loop, seed, sampler, steps, CFG, sizes, checkpoint SHA, prompt,
negative, pass history, output SHA-256); determinism evidence
(E-01 .first/.run2 files + T-01 .first); contact sheets sheet-E/T/TR and
census sheets cen-E-1..4, cen-T-1..3, cen-TR-1..3.
