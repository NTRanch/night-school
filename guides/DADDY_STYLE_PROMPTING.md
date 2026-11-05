# Daddy Style Prompting — full guide

> Daddy Style is Nice Thoughts Ranch's house style for image-generation
> prompting, adapted for adult game production and published as part of
> Night School, the Ranch's public study programme.

Prompting, done the Ranch's way: a prompt is a contract, not a wish.
Every generation the Ranch keeps is reproducible from a written record —
model, seed, sampler, full positive and negative text, LoRA stack — and
every prompt that reaches a pipeline is built from named, ordered parts
that can be reviewed, diffed, and gated like any other code. Plain
version first: the Ranch generates explicit character art, scene plates,
and reference stills for its games. A prompt nobody can re-run is a
rumour, a keeper nobody can reproduce is an accident, and an accident is
not an asset. This guide turns one public source article's worked
examples into the house discipline: what a prompt's parts are, in what
order they go, how weighting and negative registers are handled per
model family, and what gets recorded before an image is allowed to be
called a keeper.

## Source and evidence

The technique base for this guide is a single public article:
BetterWaifu's prompt gallery for Stable Diffusion, Pony, Illustrious,
and FLUX models (full citation under Sources). The article is an
example gallery, not a textbook: roughly fifteen worked generations,
each printed with its full WebUI metadata block, grouped by model
family, wrapped in a short introduction. It states almost no principles
in prose. Everything teachable in it lives in the common structure of
its examples — and in its mistakes, which are also instructive: two of
its Illustrious examples print one seed in the prose settings and a
different seed in the pasted metadata block, and one prints "Steps:
200" in prose where its own metadata says 20. A reader who copies the
prose gets a different image than the one shown. That discrepancy is
the whole argument of this guide in miniature: **the record is what the
generator actually consumed, never what an article, a chat message, or
a filename says it consumed.**

Evidence legend for this guide:

- **A** — from the source article: a claim it makes in prose, or a
 pattern present across its worked examples. One source, not
 independently verified; treated as a lead, not a fact.
- **M** — measured house practice: the Ranch's standing generation
 discipline (keeper gates, provenance records, barred registers),
 stated here as rules, not as claims about any model.
- **U** — UNVERIFIED. Named as such; do not build on it.

Where the article's practice and house practice disagree, the house
rule wins and the disagreement is recorded in the UNVERIFIED register
at the end, not smoothed over.

## The prompt is a contract

A production prompt at the Ranch has five properties, all **M**:

1. **It is written before the run.** A prompt assembled by editing a
 result's metadata after the fact is a description, not a contract.
2. **It names its model family.** Prompt text is a dialect; the same
 words are different instructions on different base models (see
 Model-family dialects). A prompt without a named family is
 incomplete.
3. **It is ordered.** Slots come in a fixed order (see Anatomy). Two
 prompts with the same tags in different orders are different
 contracts and are diffed as such.
4. **It is bounded.** Token count, LoRA stack size, and emphasis
 weights all have house maxima (see Bounds). A prompt that needs to
 exceed a bound is a design problem, not a longer prompt.
5. **It ships with its record.** Positive text, negative text, model
 name and hash, seed, sampler, steps, CFG, size, and the LoRA stack
 with versions and weights — recorded from the generator's own
 output at run time. No record, no keeper.

## Anatomy of a prompt

Across the article's examples, in every family, the positive prompt is
built from the same ordered slots (**A** as a pattern; adopted as
house structure, **M**):

| # | Slot | What goes there |
| - | ---- | --------------- |
| 1 | Register prefix | The family-mandated quality/score tokens (family-specific; see dialects) |
| 2 | Count and subjects | `1girl`, `1boy`, `2girls`, `solo` — how many bodies, of what kind |
| 3 | Act and pose | The act, position, and contact: what the bodies are doing |
| 4 | Body and appearance | Build, hair, face, the physical description of each subject |
| 5 | Expression and state | Face and arousal state: expression tags, sweat, flush, gaze direction |
| 6 | Dress and undress | Clothing, its state (worn, opened, removed, displaced), footwear, accessories |
| 7 | Setting and light | Place, time, lighting, camera framing |
| 8 | Style and artist | Medium and style tokens, artist names where the family uses them |
| 9 | LoRA stack | `<lora:name:weight>` entries, in load order (see LoRA stacks) |

Rules that follow from the slot structure:

- **One slot, one job.** Appearance words in the act slot and act words
 in the setting slot are how prompts rot: nobody can tell which part
 produced which effect, so nobody can fix the part that failed.
- **Act before appearance.** In the article's explicit examples the
 act and position are named early, immediately after the subject
 count, and the detail work (hair, clothing state, setting) elaborates
 around a fixed act (**A**). House rule adopts this: the act is the
 load-bearing slot of an explicit plate; it is decided first and
 edited last.
- **Contact is stated, not implied.** For two-body scenes the examples
 that read clearly name the contact explicitly — the position tag plus
 a contact tag — rather than stacking atmosphere words and hoping
 (**A**, from the article's two-body examples, which are also its
 weakest: several lean on a single position tag and produce the
 composition by luck of the seed). House rule: a two-body prompt that
 does not state who touches whom, where, fails review before it is
 run (**M**).
- **Counts are exact.** `1girl` and `1boy 1girl` are different
 contracts. A count slot that disagrees with the act slot (a solo act
 under a two-body count) is a defect, caught at review, not at the
 keeper gate after a night's queue has burned on it (**M**).

## Model-family dialects

The article's central implicit lesson is that there is no portable
prompt (**A**, by construction: it never reuses one prompt across
families). Each family has a register prefix, a grammar, and settings
that travel together. Copying text across families without translation
is the beginner failure this guide exists to prevent.

### Illustrious family (the article's WAI examples)

- Register prefix: a quality block — `masterpiece, best quality,
 newest, absurdres, highres` — opens every Illustrious example in the
 article (**A**).
- Grammar: comma-separated descriptive tags, Danbooru-style, with
 artist names weighted in parentheses at the tail in the style-led
 examples.
- Settings across the family's five examples (**A**): sampler Euler a;
 CFG 5; steps 20–28; size 832×1216 (portrait). The consistency is the
 point: within a family, settings are a constant of the pipeline, not
 a per-image improvisation.
- House note: the article's checkpoint is an older WAI release than
 the one the Ranch's pipeline pins. Its metadata will not reproduce
 bit-exact on a different checkpoint version, and is not expected
 to — the record names the hash precisely so that this is checkable
 rather than discovered (**M**).

### Pony family

- Register prefix: score tokens — `score_9, score_8_up, score_7_up, …`
 in the positive, the low-score tokens (`score_6, score_5, score_4`)
 in the negative (**A**). The article attributes this to the base
 model's training process; that attribution is consistent with the
 base model's own published documentation, and the prefix is treated
 as mandatory for the family, not as decoration.
- Grammar: tags plus natural-language fragments, with explicit numeric
 weights used far more heavily than in the Illustrious examples —
 `(petite body)`, `(small breast:0.7)`, `(pinup girl pose:1.2)` —
 including weights below 1.0 to *suppress* a trait without negating
 it (**A**). Sub-1.0 weighting is the family's precision tool; the
 negative prompt is its blunt one.
- The article claims Pony is unpredictable without a stack of LoRAs
 and works best with several (**A**). Single-source, anecdotal, no
 comparison runs shown: recorded as **U** in the register. House rule
 does not mandate a minimum stack on anyone's say-so; it mandates
 that whatever stack ran is recorded (see LoRA stacks) (**M**).

### SD 1.5 realistic family (Realistic Vision, ChilloutMix, Perfect World, majicMIX)

- Register prefix: photographic quality tokens — `RAW photo`,
 `photorealistic`, `8k`, `best quality` — and, in the negatives,
 named textual-inversion embeddings (`EasyNegative`,
 `ng_deepnegative_v1_75t`, `bad-hands-5` and kin) doing the work that
 later families do with plain tags (**A**).
- Grammar: looser, phrase-like, with heavy parenthesis weighting —
 doubled parentheses for strong emphasis, explicit weights up to
 `(see-through:1.6)`, negative quality weights up to `(worst
 quality:2)` (**A**).
- Settings (**A**): DPM++ 2M Karras or DPM++ SDE Karras samplers
 (never Euler a in this family's examples — the sampler split between
 families is itself a dialect marker); CFG 7 where stated; base size
 512×768 with a high-res pass (2× upscale, denoising 0.5) in the one
 fully-recorded example.
- The family's negatives are the longest in the article and the least
 disciplined: duplicated terms, the same embedding named three times
 in one string, whole anatomy lists pasted per image (**A**, as
 observed practice — explicitly *not* adopted; see Negative-prompt
 registers).

### FLUX family

The article's title promises FLUX coverage; its body contains no FLUX
examples and no FLUX-specific guidance (**A**, by absence — verified
by reading the whole page). FLUX prompting at the Ranch is therefore
**U** as far as this source is concerned: no dialect is specified
here, and none may be cited from this guide. A FLUX section waits for
a source that actually generates with it.

## Weighting and ordering

- **Syntax.** Three emphasis forms appear in the article (**A**):
 bare parenthesis stacking `((nude))`, explicit weights
 `(black shiny nylon stockings:1.5)`, and sub-1.0 suppression weights
 `(small breast:0.7)`. In the common WebUI grammar each parenthesis
 level multiplies a token's weight by roughly 1.1 and an explicit
 `:w` sets it directly; the explicit form is the house form, because
 it is the one a reviewer can read without counting brackets (**M**).
- **House weight bound.** Positive weights stay within 0.5–1.5;
 negative-register weights within 1.0–2.0 (**M**). The article itself
 stays inside these bands almost everywhere — its extremes are
 `(worst quality:2)` in negatives and `(see-through:1.6)` in one
 positive — which is weak evidence the bands are where the models
 remain coherent (**A**/**U**). A prompt that seems to need more is
 telling you the base model does not know the concept; the fix is a
 LoRA or a different model, not a bigger number.
- **Ordering.** Tokens earlier in the prompt are widely believed to
 steer more strongly than later ones. The article neither states nor
 tests this; its examples are consistent with it (register, count,
 and act always precede detail) but consistency is not measurement:
 **U** as a mechanism, adopted as a *convention* — the slot order
 above — because a fixed order makes prompts diffable regardless of
 whether the belief is true (**M**).
- **One variable per run.** When tuning, change one slot, one weight,
 or one LoRA at a time, seed held constant; when seed-shopping, hold
 the prompt constant (**M**). A run that changes three things and
 improves proves nothing and cannot be repeated on purpose.

## Negative-prompt registers

The negative prompt is not one list; it is a stack of named registers,
each with one job (**M** structure, distilled from the article's
examples, **A**). A production negative is assembled from the registers
for its family and scene, not typed fresh and not copied whole from a
stranger's metadata.

| Register | Job | Typical contents (from the article's examples) |
| -------- | --- | ---------------------------------------------- |
| Quality | Suppress the model's low tail | `low quality, worst quality` (weighted), `lowres`, `blurry`, `jpeg artifacts` |
| Anatomy | Suppress structural errors | `bad anatomy, extra digits, fewer digits, fused fingers, missing arms, extra limbs, mutated hands` |
| Artefact | Suppress text and marks | `text, watermark, logo, username, signature` |
| Medium | Pin the intended medium | The *other* mediums: `3d, photo, monochrome` for an anime target; `paintings, sketches, cartoon` for a photo target |
| Scene exclusion | Suppress this scene's specific failure modes | Per-scene: `censored` where censorship is a defect, a second character's traits in a solo plate, clothing that must stay absent |
| Family | The family's mandated negative tokens | Pony's low-score tokens; SD 1.5's negative embeddings |

Rules:

- **Registers are versioned lists, kept once per family.** The
 article's SD 1.5 negatives demonstrate the failure mode: the same
 anatomy terms duplicated two and three times inside a single
 string, drifting per example (**A**). Duplicated terms are not
 stronger; they are unaudited. One canonical anatomy register,
 reviewed like code, beats forty pasted variants (**M**).
- **Never port a register across families untranslated.** Pony's
 score tokens in an Illustrious negative are inert at best; SD 1.5's
 embedding names in a family that lacks those embeddings are pure
 noise tokens competing for the token budget (**M**).
- **Scene exclusions are the only per-image part.** Everything else
 in the negative is family baseline. If a run needs a new baseline
 term, that is a register change — proposed, reviewed, and applied
 to the register, not smuggled into one prompt (**M**).
- **The barred register is not a style choice.** Every Ranch prompt
 describes adults only. Any token that states or implies a minor —
 an under-age number, a school context used as an age cue, a
 youth-weighted tag aimed at a subject — fails the prompt at review,
 before any run, in every family, with no exceptions and no
 weighting tricks around it (**M**). The article's examples include
 age-stated tags at the adult boundary and youth-emphasis weights;
 the Ranch does not import that practice: subjects are stated as
 unambiguous adults or the prompt does not run.

## LoRA stacks

The article leans on LoRAs throughout its SD 1.5 and Pony sections:
likeness LoRAs, anatomy LoRAs, detail LoRAs, at weights from 0.1 to
1.0, stacked up to five deep in the recorded examples (**A**). House
discipline (**M**):

- **Every LoRA in a record is named with version and weight**, in
 load order, exactly as the generator consumed it — the article's
 own metadata does this (its hires example carries a LoRA hash list),
 and it is the only reason its stacks are reproducible at all.
- **Stack bound: five.** Beyond five simultaneous LoRAs, attribution
 of any effect to any member is impractical and the stack is a smell:
 consolidate, or admit the base model is wrong for the job.
- **One job per LoRA.** A LoRA that does two things (a likeness that
 also poses) couples two slots of the contract; prefer single-purpose
 LoRAs so a stack change maps to a slot change.
- **A LoRA is a dependency, with a licence and a provenance.** An
 unrecorded LoRA file of unknown origin in a production stack is the
 same defect as an unrecorded model: the keeper built on it cannot be
 re-run, audited, or trusted.

## Settings contracts

Per family, the settings are part of the dialect and change only by
deliberate pipeline decision (**M**). The article's example settings,
collected (**A**):

| Family | Sampler | CFG | Steps | Base size |
| ------ | ------- | --- | ----- | --------- |
| Illustrious (WAI) | Euler a | 5 | 20–28 | 832×1216 |
| Pony | Euler a | — (not stated) | — (not stated) | — (not stated) |
| SD 1.5 realistic | DPM++ 2M Karras / DPM++ SDE Karras | 7 | up to 50 (one example) | 512×768 + 2× hires |

Two disciplines fall out of the table itself. First, the Pony section
omits CFG, steps, and size for its examples — its records are
incomplete, and its images are therefore not reproducible from the
article; incomplete records are a defect in a source exactly as in a
pipeline (**M**). Second, CFG is family territory, not taste: 5 on the
Illustrious examples, 7 on the realistic ones, and porting a CFG value
across families with the prompt text is the same error as porting the
score tokens (**A** pattern, **M** rule).

## Iteration and keeper gates

Generation is cheap; keepers are expensive. The Ranch's loop (**M**):

1. **Draft in batches, gate on paper.** A prompt contract is reviewed
 (slots in order, registers named, weights in bounds, barred register
 clean) before its first run. Review is cheap; a night of queue time
 spent on an unreviewable prompt is not.
2. **Tune on a fixed seed.** Prompt work happens at one seed until the
 contract is right; only then does seed selection begin. Conflating
 the two searches doubles both.
3. **The keeper gate is expected-vs-seen.** Each production prompt
 carries a one-line statement of what the plate must show — the act,
 the count, the contact, the dress state — and the gate compares the
 image against that statement, not against a vibe. Anatomy-register
 failures (hands, digits, limbs) are named defects with a count, not
 impressions.
4. **A keeper is its record.** The image is filed with the full
 provenance record (contract §5 above). An image whose record is
 lost is downgraded to reference material, however good it looks: it
 cannot be extended, varied, or trusted in a series.
5. **Series consistency is a prompt property.** A character's plates
 across a game come from one versioned prompt family — same register,
 same appearance slot text, same LoRA stack — with per-scene changes
 confined to the act, expression, dress, and setting slots. Drift in
 the appearance slot between plates of one character is a defect in
 the prompt set, caught by diffing the records (**M**).

## Daddy Style treatment

Safety > performance > developer experience, applied to a text format
whose failure mode is silent: a bad prompt does not crash, it produces
a plausible wrong image at full price.

### Bounds

| Limit | Value | Why |
| ----- | ----- | --- |
| `PROMPT_TOKENS_MAX` | 225 tokens per prompt side (positive or negative), per family encoder | Beyond the encoder's effective window, tail tokens are decoration; the slot order exists so the load-bearing text is never in the tail |
| `WEIGHT_POS_MAX` | 1.5 (floor 0.5) | Above this the article's own examples do not go; coherence, not courage, is the constraint |
| `WEIGHT_NEG_MAX` | 2.0 | The article's observed ceiling, in the quality register only |
| `LORA_STACK_MAX` | 5 | Attribution limit for stack effects |
| `REGISTERS_PER_NEGATIVE_MAX` | 6 (the six named registers) | A seventh register is a proposal to amend this guide, not a longer string |

### Contracts

- Prompt text is reviewed, versioned, and diffed like code; a prompt
 change in a production series is a commit with a reason.
- The generator's own metadata is the record of a run. Prose —
 articles, chats, commit messages — may quote it but never substitute
 for it (the article's seed mismatches are the standing example).
- Registers (quality, anatomy, artefact, medium, scene, family,
 barred) are shared, named, and changed by review, never per-run.
- Every subject in every prompt is an unambiguous adult; the barred
 register gates before generation, not after.

### Golden tests

Half validation, half adversarial, per the standing split. Specified
here; running them is pipeline work, and this guide claims no run.

Validation cases:

- `val-reproduce-article` — one article Illustrious example, run from
 its pasted metadata block on the named checkpoint version, matches
 the article's image in composition (validates that a full record
 really is a contract).
- `val-fixed-seed-tune` — one slot changed at a fixed seed changes
 the named aspect and no other (validates the slot structure).
- `val-register-baseline` — the family baseline negative, applied to
 a bare count+act prompt, suppresses the anatomy-register defects
 versus the no-negative control.
- `val-series-consistency` — three plates from one versioned prompt
 family hold the appearance slot constant by record diff.

Adversarial cases:

- `adv-prose-seed` — a record whose prose seed disagrees with its
 metadata seed (the article's own defect) must be caught by recording
 from the generator, never from prose.
- `adv-cross-family-port` — an Illustrious prompt run verbatim on the
 Pony family (and vice versa) must fail review on the register
 prefix, before any GPU time is spent.
- `adv-weight-overflow` — a positive weight above `WEIGHT_POS_MAX`
 must fail review; the correct outcome is a LoRA or model change.
- `adv-barred-token` — a prompt containing an age-ambiguous or
 minor-implying token must fail the barred gate in every family,
 including when the token arrives inside a copied foreign metadata
 block.
- `adv-missing-record` — an image presented as a keeper with an
 incomplete record (the article's Pony omission: no CFG/steps/size)
 is downgraded to reference, automatically.

## UNVERIFIED register

Alphabetical. Each item is marked **U** at its point of use as well.

- Article's claim that Pony is unpredictable without several LoRAs
 (anecdote, no comparison runs shown).
- Article's FLUX coverage (promised in its title, absent from its
 body; no FLUX dialect is specified in this guide).
- Article's seed and step figures in its Illustrious prose settings
 (contradicted by its own pasted metadata in three places; the
 metadata is treated as authoritative, itself unverified against the
 article's images).
- Earlier-tokens-steer-more as a mechanism (adopted as an ordering
 convention for diffability, not as a measured fact).
- Quality/register prefixes (`masterpiece, best quality, …`) as
 causal quality levers on any given checkpoint (they are family
 conventions in the article's examples; their effect size on the
 Ranch's pinned checkpoints is unmeasured).
- The 0.5–1.5 / 2.0 weight bands as model limits (house bounds,
 consistent with the article's range; not measured per checkpoint).

## Sources

- BetterWaifu, "Best AI Prompts for Hentai, NSFW & Porn (Stable
 Diffusion, Pony, Illustrious, FLUX etc.)" —
 https://betterwaifu.com/blog/nsfw-prompts (fetched 2026-11-05; the
 served copy was the site's 2026-08-24 crawl). All technique in this
 guide is distilled from that article's worked examples and stated
 claims, re-expressed in house form; the article's prompt strings are
 its own and are quoted here only as short individual terms (register
 tokens, sampler names, register contents) where a term itself is the
 subject.
- The base-model families' own published documentation (Pony
 Diffusion's score-tag convention) as corroboration for the one
 attribution the article makes that is checkable outside itself.
