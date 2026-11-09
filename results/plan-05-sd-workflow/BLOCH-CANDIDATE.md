# Bloch candidate — Plan 05 (SD workflow control sample)

origin_lane: ntranch
content_label: nsfw
evidence: ~/workspace/night-school-20261105/runs/plan-05/ (MANIFEST.md,
OBSERVATION.md, TECHNIQUE.md, PASS3-REBUILD.md, PASS4-APPLICATION.md,
AB/ plate records)

## Lessons (each with its evidence pointer)

1. **A vendor's newest rendition can be silently truncated at the packet
   layer while byte-exact at the file layer.** The 1080p file matched the
   CDN's Content-Range total exactly (879,676,586 B) yet its streams end at
   2,679 s of a 4,731 s programme. Decode-verify at sparse timestamps PASSED
   vacuously past the truncation. Gate change: verify packet timestamp span
   (ffprobe packet pts max vs container duration) on every capture, not just
   spot decodes. (MANIFEST.md, plan-05 media records.)
2. **A repair pass repairs only its mask target; census class counts are the
   proof.** Face inpaint at the practitioner's own denoise left a
   hands-dominant census completely unchanged (12/12 hands class pre and
   post). Repair order must be mask-follows-census, not habit.
   (PASS3-REBUILD.md defect-class table.)
3. **Cold-first-run nondeterminism in ComfyUI is a process-warmth effect,
   MAD ≈ 1.9, composition-identical; steady state is byte-identical.**
   Discard/re-run the first job after a server restart before treating
   outputs as of record. Same magnitude family as the estate's Prong 0
   cross-build jitter — one phenomenon class, two sightings.
   (PASS3-REBUILD.md determinism section.)
4. **Keep rate without a defect census cannot separate two loops.** Both A/B
   loops scored 12/12 keeper-candidates under CLEAN+RULABLE while their
   CLEAN rates were 6/12 vs 0/12. Any future loop comparison must gate on
   census classes, never on keep rate or keepers/hour. (PASS4-APPLICATION.md.)
5. **Text-only identity on a modern Illustrious-class checkpoint is a real
   baseline, not a strawman** — descriptive tags held the character 12/12
   with 1 mild face drift and no LoRA/IPA/CN. LoRA adoption claims must beat
   this baseline measurably. (PASS3-REBUILD.md, TECHNIQUE 1.2.)

## Friction answer (D-1064 — what cost time / forced a guess / forced a workaround)

- **Script transfer to primo by stdin heredoc silently produced 0-byte files
  twice** (capture downloaders + A/B driver). Workaround that worked every
  time: base64-encode locally, decode on primo, hash/length-check before
  running. Next agent should start there; a primo-ssh file-push helper would
  remove the class.
- **`pkill -f <scriptname>` self-matched the caller's own ssh command line**
  and killed the session (exit 255) — the primo waiter-loop trap's cousin.
  Kill by explicit PID only.
- **WAV chunk splitting with `-c copy` silently produced a 78-byte chunk**
  (keyframe-style packet boundaries in WAV/PCM are not where the cutter
  assumes). Re-encoding the split to pcm_s16le fixed it; stream-copy splits
  of audio should be span-verified like video (lesson 1's family).
- **Egress decay is per-hour, not per-session**: primo single-stream fell
  9.31 MB/s → 0.22 MB/s within the same afternoon; the plan's re-probe rule
  had to be exercised mid-download, with fresh page tokens (tokens are
  egress-bound — a token minted on one egress is dead on the other, and HEAD
  on a token URL 403s even where GET works). No guess was needed, but the
  re-probe cadence (per segment batch, not per download) is worth writing
  into the capture skill.
- **ComfyUI node inventory ≠ A1111 feature names**: the estate instance has
  no ADetailer/FaceDetailer/UltimateSDUpscale nodes; the practitioner's
  repair/upscale steps had to be re-expressed from core nodes (crop-inpaint,
  model-mode upscale). A standing A1111→ComfyUI-core equivalence table would
  save each future control-sample plan the same derivation.
