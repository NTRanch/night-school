# Daddy Style CUDA — full guide

> Daddy Style is Nice Thoughts Ranch's house style for CUDA,
> adapted for adult game production and published as part of
> Night School, the Ranch's public study programme.

CUDA, driven the Ranch's way: the GPU is where the Ranch's adult work
is *made* — heroines' dialogue registers trained, companion text
tuned, explicit plates and clips generated — and it is the one place
where a routing mistake is not a style error but a fence breach.
Plain version first: every NSFW byte the Ranch puts on a GPU stays on
the Ranch's own hardware. Hosted GPU services are for SFW work; the
moment a corpus, a prompt set, or an adapter carries adult content,
the job runs locally or it does not run. Everything else in this
guide — budgets, corpora, probes, backups — is bookkeeping in service
of that one fact and of the ordinary Tiger discipline underneath it.

This guide covers only what is NSFW-unique. Kernel mechanics —
memory hierarchy, occupancy, warp discipline, nvcc flag hygiene,
the two-GPU environment on the Ranch workstation (RTX 4070 8 GB +
A6000 eGPU, `CUDA_HOME=/opt/cuda`, explicit env in non-interactive
shells), and the half-adversarial kernel test split — live in the
Tiger Style CUDA guide (`local-tiger-style-cuda`) and are not
duplicated here. Read it first; this guide assumes it.

## Evidence legend

In strength order:

- **R** — verified by run on the Ranch workstation (a ruling executed,
  a job record read back, a gate passed).
- **S** — static read: a licence, a provider's terms, a repo record,
  read in full at the cited date.
- **M** — measured house practice: the Ranch's standing discipline,
  stated here as rules, not as claims about any tool.
- **U** — UNVERIFIED. Named as such; do not build on it.

## The hard fence: NSFW GPU work is local only

This section is first because it outranks every other section. A job
that violates it is not a job done badly; it is a defect, full stop,
whoever dispatched it and whatever it produced.

- **Hosted fine-tuning bars NSFW input.** The hosted SFT provider the
  Ranch evaluated for SFW tool-calling work bars adult content in its
  terms (Fireworks ToS §3.3(v) class, **S**, read 2026-11-26): NSFW
  training data may not be uploaded to it at all. The Ranch's ruling
  generalises the shape, not just the vendor: **no NSFW corpus,
  prompt set, or adapter is ever uploaded to a hosted GPU service** —
  fine-tuning, inference, or "just an eval" — unless that service's
  terms have been read, in full, and admit the content, and the
  admission is recorded in the job record (**M**). Default is no.
- **The local stack is therefore the NSFW stack.** NSFW training and
  generation run on the Ranch workstation's own cards, served and
  trained through the local tooling (rose for serving; the estate's
  own training scripts for SFT). A plan whose critical path needs a
  hosted GPU for adult content is rejected at planning, not rescued
  at run time (**M**).
- **SFW work may travel; the boundary is the content, not the job.**
  The same workstation runs SFW fine-tunes on hosted services when
  the terms admit them and the price is right (the Ranch's SFW
  tool-calling tune is the standing example, **R**). What may never
  happen is a mixed job: one upload carrying both SFW and NSFW rows
  "because the pipeline was already built". Pipelines are built per
  lane (see Data handling), and a lane crossing is a defect even when
  every individual row was legal where it landed (**M**).
- **No NSFW data in exhaust.** Crash dumps, profiler traces,
  training logs, and eval transcripts from NSFW jobs stay in
  NTRanch-lane trees. A log that quotes corpus rows is corpus, for
  handling purposes. Nothing in this class is attached to a hosted
  issue, a public gist, or a qompassai-side report (**M**).

## Job classes and GPU budget

The Ranch workstation carries two cards of very different size, and
NSFW job classes are assigned to cards by budget, stated before the
run, not discovered by an out-of-memory kill mid-run (**M**).
Headroom law from the house heavy-compute policy applies throughout:
one heavy job at a time, A6000 preferred, at least 4 of 16 CPU
threads and 16 GiB RAM left free, and a heavy job yields on the
Owner's word (**M**).

| Job class | Card | VRAM budget | Notes |
| --------- | ---- | ----------- | ----- |
| NSFW SFT (27B-class base, adapter tune) | A6000 (48 GB) | Weights (4-bit) ≈ 14–16 GB + adapter/optimizer/activations; plan ≤ 40 GB total | The ruled programme's class; never attempted on the 4070 |
| NSFW inference / register probes (quantised 27B) | A6000 | ≈ 16–20 GB | Probe batches sized to leave the card shareable afterwards |
| Image generation (wai pipeline) | 4070 (8 GB) or A6000 | ≤ 7 GB on the 4070, offload stated in the record | Tight on the 4070 by design; see Generation compute |
| Video / img2video passes | A6000 | Job-named; measured per pipeline | The 4070 route exists only for the pipelines already proven on it (**R**, per-pipeline records) |
| Kernel development / small tests | Either | ≤ 4 GB | Small-scale correctness first, per the Tiger guide; scale is a separate run |

Numbers in the budget column are planning figures (**M**), stated so
a job can be refused on paper. A run that exceeds its stated budget
is stopped and re-planned, not allowed to swap, thrash, or quietly
spill to the other card (**M**).

## Local NSFW SFT discipline

The Ranch's NSFW SFT programme is a ruled, standing programme
(**R**, Owner ruling 2026-11-26): a local adapter tune on the
Qwen3.6-27B base already in the rose store, over three estate-authored
corpora — mesmer/Sirena dialogue, the Strobe story corpus, and
torogao companion/session text. This section is that programme's
discipline, written so any NSFW tune follows it, not only the first.

### Corpus provenance

- **Every row traces to an authored source.** Each training row
  carries its source: the authored file, the heroine and register it
  was written for, and the authoring lane. A row whose source cannot
  be named does not enter the corpus. There is no "found text" in an
  NSFW corpus — no scraped dialogue, no lifted lines from studied
  games, no held-reference material of any kind (see Tier A, below)
  (**M**).
- **The corpus is frozen and hashed before training.** The exact
  train/eval files are hashed (SHA-256 recorded in the job record)
  before the run starts, and the eval split is disjoint from train by
  construction, not by sampling luck. A corpus that changes mid-
  programme is a new corpus with a new hash and a new version; runs
  cite the hash they consumed (**M**). This is the D-1397 pattern —
  frozen, hashed, deterministic inputs — applied to datasets.
- **Registers are authored separately and stay labelled.** Sirena's
  three registers (Host / Trainer / Subject) are separate corpus
  sections with separate provenance, because the adapter's job is
  precisely to keep them apart on cue. A corpus that blends registers
  into one undifferentiated "adult dialogue" pool trains exactly the
  register bleed the programme exists to prevent (**M**).
- **All characters in every corpus are adults.** Authored corpora
  describe the Ranch's own cast — adult heroines, identity-locked at
  intake — and no row introduces a character whose adult status is
  ambiguous. This is the prompting guide's barred register applied to
  training data: it gates at authoring, not at the trainer (**M**).

### Third-party material: the D-1461 gate

No third-party fine-tune, adapter, or merge is used on benchmark
evidence alone (**M**, standing rule D-1461). Before any external
adapter touches an NSFW job: a provenance check (who trained it, on
what, under what licence) and a behavioural probe (the Verification
section's probe set) both pass and are recorded. An adapter that
fails either is not "used carefully"; it is not used.

### Adapters are candidates until gated

- **Candidate labelling.** A finished training run produces a
  *candidate* adapter. It is labelled candidate in its record, its
  directory name, and its backup (below) until the Verification
  gates pass. Nothing serves a candidate to a game, a companion
  session, or another training stage (**M**).
- **The job record is the adapter's identity.** Base model and hash,
  corpus hash, hyperparameters, seed, wall-clock, card used, final
  loss — recorded at run time from the trainer's own output. An
  adapter whose record is lost is downgraded to scratch, however good
  its samples look: it cannot be re-run, audited, or trusted in a
  series (the prompting guide's keeper rule, applied to weights)
  (**M**).
- **Backup is gated, immediate, and private.** On completion, a
  candidate adapter is backed up to a **gated** Hugging Face repo
  under the Ranch's NFAA posture — access-controlled, never public,
  never a dataset sweep (**R** as programme ruling; **M** as
  discipline). This is the generated-media backup rule (finished
  media uploaded immediately, labelled candidate) applied to weights,
  with the NSFW tightening: where finished SFW media may go to a
  public dataset with attribution, an NSFW adapter goes only to a
  gated repo, and its corpus never goes to HF at all (**M**). If the
  upload route is unavailable at completion time, the adapter is
  staged locally with a manifest and an UPLOAD-PENDING flag, and the
  pending backup is swept at the next opportunity — the flag, not
  memory, carries the obligation (**M**).

## Generation compute

- **One generator.** Image generation for SFW and NSFW alike runs on
  the Ranch's single pinned generator (wai, per standing rule
  D-1525, **R**); the second model (iris) is demoted to face/eye
  unify only and never generates bodies or redraws hands or device
  regions. CUDA work respects the split: kernels, schedulers, and
  pipeline patches are maintained for the one generator's route, and
  a job that routes generation through the demoted model is a defect
  caught at review, not a variant (**M**).
- **Generation is local for NSFW, by the fence.** Hosted image/video
  generation for adult plates follows the same rule as training:
  terms read in full and admitting the content, recorded, or it runs
  on the Ranch's cards (**M**).
- **Budgets are per pipeline, proven per card.** The 8 GB 4070 route
  is real but narrow: it serves the pipelines already proven on it,
  at their proven settings. Raising resolution, batch, or frame count
  on the small card is a new proving run with its own record, not a
  flag change in an old one. The A6000 is the default for anything
  unproven (**M**).
- **Determinism where the medium allows it.** Seeds, sampler,
  scheduler, and step counts are recorded per generation job exactly
  as the prompting guide requires per image; batch jobs record the
  seed schedule, not just the first seed. A keeper that cannot be
  re-run from its record is reference material, not an asset (**M**).

## Data handling and the lane law

GPU work touches whatever its kernels touch, so the lane law is
stated here in its CUDA form. The law itself is the bloch lane law
(**S**, standing estate rule): sharing is governed by *content
label*, not origin.

- **NSFW-pure material never crosses to qompassai.** No NSFW corpus,
  adapter, generation output, or derivative statistic (a loss curve
  is fine; a quoted sample is material) enters a qompassai repo,
  registry, dataset, or report. SFW lessons learned on NSFW jobs may
  flow the other way only when genuinely SFW and re-labelled as such
  by a gated act, never by the job that learned them (**M**).
- **The ache carve-outs are named, not implied.** The Ranch's haptics
  server (ache) is adult-adjacent infrastructure with hard fences of
  its own: it is never listed in the ai.qompass registry, never
  published on qompass.ai, and never routed to lanes that do not take
  adult work. CUDA jobs do not soften these fences by accident —
  there is no "the training box already had the data" exception
  (**M**).
- **Tier A held material is study-only, and study is not training.**
  Held references (studied games, extracted media, census corpora)
  are measurement and reference material. They are never training
  rows, never fine-tune input, never generation conditioning for a
  shipped asset, and they never leave their held trees. A CUDA job
  whose dataloader can reach a held tree is misconfigured by
  construction; corpus paths are allowlisted per job, and the
  allowlist is in the job record (**M**).
- **Corpora live in NTRanch-lane trees only.** NSFW datasets,
  adapters, and their records are stored under NTRanch-lane paths on
  the Ranch workstation. They are not mirrored into shared scratch,
  not synced to SFW trees "for backup", and not left in `/tmp` after
  a run. The gated-HF backup above is the only off-workstation copy
  (**M**).

## Verification

An NSFW adapter is gated on behaviour, measured, with the numbers
cited from run artefacts (the house provenance-first rule: every
number in a gate report cites its run, **M**). Three probe families,
all run locally, all on a fixed probe set versioned with the corpus:

- **Register and voice checks.** Per heroine, the probe set carries
  canon-anchored prompts for each register the corpus taught (for
  Sirena: Host, Trainer, Subject), and the gate checks that the
  adapter answers in the cued register, in the heroine's canon voice,
  without bleeding a neighbouring register's markers. The check is
  expected-vs-seen against a written canon statement per heroine —
  the same shape as the visual keeper gate — not a reviewer's vibe
  (**M**).
- **Refusal-drift measurement.** The base model and the candidate
  adapter are run over the same fixed in-scope probe set (adult,
  in-canon requests) and the same out-of-scope set (anything barred:
  minors, non-consent with real persons, the estate's closed
  taxonomy). The gate reports both rates as numbers: in-scope refusal
  rate must not rise materially over base (that is drift, and it
  means the tune damaged the tool for its ruled purpose), and
  out-of-scope refusal must not fall (that is the fence, and it is
  not negotiable). Both are measurements from a named run, reported
  with the probe-set version — stated honestly as measurements with a
  sample size, never as vibes and never as a guarantee about inputs
  outside the probe set (**M**).
- **Regression floor.** The adapter must not lose the base model's
  ordinary competence on a small SFW control set (the programme's
  tools and dialogue still have to work). A tune that buys register
  fidelity with general damage is a failed tune with good samples
  (**M**).

A candidate that passes all three is promoted by a recorded act;
the record names the probe artefacts. A candidate that fails is
kept, labelled with its failure, or deleted — it is never quietly
re-probed until it passes on a friendlier set (**M**).

## Daddy Style treatment

Safety > performance > developer experience, in that order, applied
to the one compute class where the safety question is not "does it
crash" but "where did the data go". Adult production is exactly
where that discipline pays: a night's SFT run is long, unattended,
and worthless — worse, a liability — if its corpus crossed a lane,
its adapter backed up to a public repo, or its gate was a vibe.

### Bounds

Named limits, with units, for every Ranch NSFW CUDA run:

| Limit | Value | Why |
| ----- | ----- | ------- |
| `HEAVY_JOBS_MAX` | 1 at a time on the workstation | House heavy-compute law; a second heavy job is a scheduling act, not an accident of two queues |
| `SFT_VRAM_BUDGET_GB` | ≤ 40 GB on the A6000 for the 27B adapter class | Leaves the card's remainder and the machine's headroom intact; overruns stop and re-plan |
| `GEN_4070_VRAM_GB` | ≤ 7 GB for generation on the 4070 | The proven pipelines' envelope; beyond it is a new proving run |
| `CORPUS_ROWS_UNTRACED_MAX` | 0 | Every row traces to an authored source; one untraced row fails the corpus, not the row |
| `PROBE_SET` | Fixed and versioned per programme | Drift and register numbers are comparable only against a frozen set |
| `BACKUP_LAG` | Adapter backed up (or UPLOAD-PENDING flagged) before the run is reported done | A finished adapter existing in exactly one place is an unfinished job |

### Contracts

- **The fence is a pre-flight check, not a post-hoc apology.** Every
  NSFW job record names its execution venue (local card, by name)
  before it runs. A record that names a hosted venue for NSFW input
  fails review before any GPU time is spent.
- **Corpus paths are allowlisted per job.** The dataloader's world is
  the allowlist in the job record; held trees and cross-lane trees
  are unreachable by construction, not by care.
- **Frozen inputs, cited hashes.** Corpus hash, base-model hash, and
  probe-set version are in the record before the run; the adapter
  that comes out cites all three.
- **Candidate until gated.** Labelling is part of the artefact: a
  directory, repo, or manifest that omits the candidate label before
  the promotion act is a defect in the artefact.
- **No hidden behaviour:** no telemetry, sample upload, or
  "anonymous usage" path leaves the workstation from any NSFW job's
  tooling; a tool that cannot run fully offline does not run on NSFW
  jobs at all.

### Golden tests

Half validation, half adversarial, per the standing split. Specified
here; running them is programme work, and this guide claims no run
beyond the rulings cited above.

Validation cases:

- `val-corpus-trace` — a random sample of corpus rows, each traced
  to its authored source file and register label without a miss.
- `val-freeze-hash` — re-hashing the corpus at gate time reproduces
  the hash in the job record (the run trained on what the record
  says it trained on).
- `val-register-probe` — the candidate adapter answers the per-heroine
  probe set in the cued registers, per the Verification section.
- `val-backup-gated` — the candidate's HF backup exists, is gated
  (unauthenticated read refused), and its hash matches the local
  adapter.

Adversarial cases:

- `adv-hosted-upload` — a job script pointed at a hosted fine-tune
  endpoint with an NSFW corpus path must fail the pre-flight venue
  check before any network call is made.
- `adv-held-tree-reach` — a dataloader configured outside its
  allowlist (a held-reference path) must fail loudly at startup,
  not skip, not sample-around.
- `adv-public-backup` — a backup script aimed at a public repo or a
  public dataset must fail the backup gate; gated-or-flagged are the
  only passing outcomes.
- `adv-drift-vibe` — a gate report quoting refusal or register
  quality without probe-run artefacts must fail review on its face:
  numbers without a run are not numbers.
- `adv-mixed-lane-job` — a single upload or corpus file containing
  both SFW-lane and NSFW-lane rows must fail the lane check, even
  when each row is legal in its own lane.

## UNVERIFIED register

Alphabetical. Each item is marked **U** at its point of use as well.

- A6000/4070 VRAM figures for future job classes (video pipelines,
  larger bases) beyond the pipelines already proven per card —
  planning figures until a proving run records them.
- Behavioural-probe sample sizes sufficient to bound refusal drift
  tightly (the probe method is house discipline; its statistical
  power per programme is measured per run, not asserted here).
- Hosted providers beyond the one evaluated whose terms might admit
  NSFW fine-tuning (none has been read and admitted; the fence's
  default stands until one is).
- Third-party NSFW adapters' provenance claims generally (each is a
  D-1461 case of its own; no general verdict exists).
