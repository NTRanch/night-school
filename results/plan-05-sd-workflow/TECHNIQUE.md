# Plan 05 — Pass 2 Distillation (Technique Sheet)

Source: `OBSERVATION.md` (claims C1–C12). Method per the
protocol: mechanism over mimicry; every technique split
Adopt / Adapt / Reject with its evidence. A/B evidence
column is filled from `PASS3-REBUILD.md` at gate time;
verdicts below are the observational verdicts the A/B was
designed to test.

Estate frame for comparison: the keeper-art recipe of
record (solo-sheets lane) — WAI Illustrious v170, euler_
ancestral/normal, 30 steps, CFG 6.0, 1024×1280, IP-Adapter
PLUS identity (0.28) + ControlNet Union openpose 0.5,
per-plate stamped run records, census CLEAN /
RULABLE-WITH-DEFECTS / FAIL, deterministic-repair-first
(pixel/analytic fixes before any re-roll).

Verdicts below are the Pass-2 (observational) rulings. Pass 3 A/B evidence
was collected 2026-11-06; the with-evidence verdicts (two sharpened: 1.2,
3.1; none overturned) are recorded in PASS4-APPLICATION.md, which governs.

## Target 1 — Prompt grammar

**His grammar (own generations):** [trigger/name + plain
subject tags] + [inline LoRA call with tuned weight] +
[negative = embedding names only]. No quality boilerplate,
no anatomy lists, no weighting syntax in his own prompts.

**The other grammar (Civitai samples):** Danbooru tag
strings with "masterpiece, best quality" boilerplate and
weighted negative terms — present in the video as *data he
transplants*, not as his practice (OBSERVATION §5).

Mechanism read: the negative embeddings are doing the work
the estate's long negative does by enumeration — a textual
inversion is a learned "away from this defect cluster"
vector, invoked by name. His three names (bad-hands-5,
bad-artist, EasyNegative) map onto the estate negative's
hand/quality clauses. The estate has no embedding shelf in
its ComfyUI lane records (negative is text-only), so the
mechanism is genuinely absent from the recipe of record,
not merely differently spelled.

| # | Technique | Verdict | Reason / evidence |
|---|---|---|---|
| 1.1 | Negative-as-embedding-stack (named TIs instead of enumerated text) | **Adapt** | Mechanism sound (C5, his locked-seed A/B). Estate version: trial one negative embedding as a named candidate variable in a gated round — the estate negative is otherwise text. Not adopted wholesale: his stack is SD1.5-era TIs; SDXL equivalents differ and must be measured, not assumed. A/B Loop T carries the names as text (weaker form) — its census bounds what the *names alone* do without the vectors. |
| 1.2 | Identity = character LoRA + trigger word, weight tuned by eye (0.5→0.8) | **Adapt** | The estate's identity mechanism is IP-Adapter against a gated anchor — stronger provenance, same *slot* in the grammar (a named identity token whose strength is a tuned scalar). The transferable part is the discipline: identity strength is a first-class named variable with an eye-checked operating point, exactly how the estate treats IPA weight (0.28 Prima). No LoRA enters the estate stack on this evidence. |
| 1.3 | Plain-language subject slot ("you want to see some boobies") over tag strings | **Reject** (for estate recipes) | Works for him because the checkpoint + LoRA carry the specificity (C3/C4 context). Estate prompts are specification documents for a deterministic pipeline (pose, props, staging all enumerated); plain-language prompts under-specify and would break cross-round comparability. Recorded as a real divergence: his grammar optimizes for speed of exploration, ours for reproducibility of a named plate. |
| 1.4 | Quality boilerplate ("masterpiece, best quality") | **Reject** | Absent from his own prompts; present only in transplanted sample data and in *our* estate prompt head. His results without it (C3) are evidence it is not load-bearing on a tuned checkpoint. For the estate it stays only because our recipe records hold it constant — removing it is a candidate variable (see PASS4), not a finding. |
| 1.5 | TI-hash self-check (verify the embeddings fired via the info block) | **Adopt** | Pure provenance discipline, estate-shaped as-is: verify the conditioning actually loaded from the run record, not from the prompt text. The estate already stamps hashes per run; this adds the *check* — a record whose conditioning hashes don't match the recipe is a failed run, not a plate. Zero cost, catches silent no-ops (his mistyped-name catch, OBSERVATION §5). |

## Target 2 — Iteration economics

His loop's time budget, from the event tally + batch
structure (OBSERVATION §6–8): ~35% setup/downloads
(extensions, models, embeddings — one-time, amortized),
~45% generation in batches, ~20% browsing/curation.
Per-image cost on his machine: 1.5–2.5 s at 512–768²
SD 1.5 [SCREEN timings ×2] — an order of magnitude faster
per roll than the estate's SDXL 1024×1280 plates, which is
*why* his economics work: rolls are nearly free, so
curation-after is rational. The estate's rolls are
expensive (bigger model, bigger latent, dual
conditioning), so the estate rationally spends its effort
before the roll (anchors, pose maps, held-constant
recipes) instead of after it.

| # | Technique | Verdict | Reason / evidence |
|---|---|---|---|
| 2.1 | Batch-of-12 → carry one forward (batch curation at fixed prompt) | **Adapt** | The estate generates one plate per seed per round and censuses all — a batch *is* our round, with the census as the curation. What transfers: his batch is a *single prompt explored across seeds*, judged comparatively in one grid (m3000) before any repair time is spent. Estate rounds already compare across seeds; the adaptation is to make the comparative grid the explicit first gate before repair (we sometimes repair serially). A/B tests the structure directly (12 seeds, one prompt, both loops). |
| 2.2 | Seed locking for single-variable questions; free rolling for exploration (two distinct modes, switched deliberately) | **Adopt** | Already the estate's stated discipline (one variable per round); his loop is independent confirmation from practice, including the recycle-button mechanism (C6). Adopted as corroboration, no change needed — recorded because the control sample *validates* an estate rigidity that could have been costing quality and isn't. |
| 2.3 | Save-all + seed-in-filename + browser curation (no deletion, judgement as a separate pass) | **Adapt** | Estate already keeps all candidates + records; his filename-seed convention is the lightweight version of our stamped records. Adaptation is one-way validation: our heavier record discipline costs little at our roll rate and buys cross-round comparability his filenames can't (settings beyond the seed aren't in the name — he re-opens the info block; we stamp the record). No change; noted as the point where his loop is *under*-tooled relative to ours, deliberately. |
| 2.4 | Generation-data transplant (copy a published sample's full settings + seed to reproduce, then vary) | **Adapt** | Mechanism: a published plate with full provenance is a recipe fossil — reproducing it calibrates the local stack against a known output (C7). Estate version: reproduction runs are *calibration gates* (cf. TG4's byte-identical regression plates), not an art source. Adapted as method; rejected as a source of keeper content (protocol: reference only). |
| 2.5 | Keepers/hour as the loop's headline metric | **Reject** (as a gate metric) | His ≈1 carry-forward per batch at ~2 s/roll implies very high keepers/hour, but "carried forward" ≠ keeper (§8 limit: final judgements off camera), and the metric rewards cheap rolls. Estate gates on census classes per round, not throughput. Recorded so the comparison is explicit: the A/B reports keep rates per loop (comparable), not keepers/hour (not measurable honestly from either side). |

## Target 3 — Repair practice

His split: **regenerate** for composition/identity
failures (re-roll, batch, re-prompt, LoRA weight);
**fix in pass** for local defects — masked inpaint at
moderate denoise (0.5 anime / 0.35 photoreal face) with
the image otherwise untouched, and whole-image inpaint
sketch at 0.75 when the composition itself needs another
chance at the same seed. No face-restore automation, no
pixel-level editing shown.

Estate split (deterministic-repair-first): measurable
pixel defects are repaired deterministically (analytic
fixes, paint-overs) before any generative step; generative
re-rolls are rounds, not repairs.

| # | Technique | Verdict | Reason / evidence |
|---|---|---|---|
| 3.1 | Masked inpaint as the local-defect repair (only-masked, padding 32, original content, DPM++ 2S a Karras 20 steps) | **Adapt** | Mechanism sound: repair locality (only the masked region resamples) + moderate denoise (structure survives, defect resampled). Estate adaptation: inpaint enters as a *named repair pass behind the deterministic pass*, with the mask, denoise and seed stamped — his denoise split (0.35 face / 0.5 body region) is the starting calibration, tested in the A/B repair pass. Not adopted as first-line: our deterministic repairs are reproducible bit-exactly; inpaint is not, so it stays second-line. |
| 3.2 | Denoise level encodes repair depth (0.35 touch-up < 0.5 region repair < 0.75 recomposition) | **Adopt** (as a named scale) | A clean, transferable calibration: one scalar, three named bands, each demonstrated (C10/C11). Adopted as vocabulary for estate repair records regardless of which repair runs. |
| 3.3 | Whole-image variation pass at the winner's seed (inpaint sketch 0.75) as a composition second chance | **Adapt** | Estate analogue: a re-roll *conditioned on the winning plate* rather than from noise — our rounds don't currently do img2img continuations of winners. Candidate variable for a gated round (PASS4), tested structurally in Loop T only insofar as Loop T's plates are standalone; the A/B does not chain a winner (budget held equal), so this verdict rests on observational evidence (C10) alone — flagged. |
| 3.4 | No automated face restore; faces fixed by hand-masked inpaint or not at all | **Adopt** (as corroboration) | Matches the estate's position (no ADetailer in the primo ComfyUI node inventory either — verified at capture: 1,097 nodes, no Detailer class). His practice shows a working workflow without it; the estate's face gates stay measurement-based. |
| 3.5 | Defect-spotting as an explicit first skill ("Where's Waldo" scan before any judgement) | **Adopt** (as corroboration) | The estate's census is this, formalized (named defect classes, per-plate). His version validates the *order*: scan for defects before evaluating appeal — the census already runs that way. No change. |

## Not-a-technique (distilled and dismissed)

- **Civitai Helper / in-app downloads** — tooling
  convenience, not a generation technique; the estate's
  model store is local and pinned by hash, which is the
  stronger form of the same need. No transfer.
- **Cozy Nest theme / UI rearrangement** — ergonomics of
  one operator; no mechanism. No transfer.
- **The joke prompt itself** — a teaching device (a
  constant probe prompt carried across every change, so
  each change's effect reads against a fixed baseline).
  As a *device* it is the same one-variable discipline as
  2.2 wearing a comic mask; counted there, not separately.

## UNREADABLE dependencies

- 1.1's A/B form is weakened by an UNREADABLE-independent
  limit: Loop T carries the embedding *names as text*
  (estate stack has no SD1.5 TI shelf and external
  downloads are barred by the tasking), so the A/B
  measures the names' text effect, not the vectors'.
  The verdict (Adapt, gated trial) is written to survive
  that limit: the trial it recommends is precisely the
  one that would measure the vectors.
- 3.1's mask-target calibration for the anime hero rests
  on OBSERVATION §10 UNREADABLE (3) until the chunk-2
  narration mapping lands; the face target (photoreal)
  is [SCREEN]-certain.
