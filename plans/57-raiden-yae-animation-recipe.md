# Plan 57 — Raiden x Yae — Animation (5447477)

- **Source:** https://danbooru.donmai.us/posts/5447477
- **Video ID:** 5447477 (Danbooru post) · **Creator:** vicineko, kitsuneecchi (voice: kassioppia) · **Duration:** 2:17
- **Lane:** NSFW-primary / SFW translation: none — production-recipe study for the estate's adult animation work
- **Estate targets:** Handfast (jam translation, landed), Torogao main (3D translation, landed) — third shelf, the favourites performance studies
- **Status:** PLANNED
- **Status after run:** EXECUTED — full fathom RE + RECIPE complete 2026-10-30 (Owner directive 2026-10-30 21:43 PT); distilled ✓; codified ✓ in two consumer translations (Handfast, Torogao main). The shelf's one fully-closed item: its Pass 3/4 equivalents are the two translations and their acceptance metrics

## Why this video

The set's proof that the extraction pipeline terminates in shipped
grammar: a complete fathom reverse-engineering of a 137-second
animation into a production recipe — measured (4,124 frames, 34
perceptual clusters, 24 measured cuts, an audio event census),
annotated into four editorial phases, and rebuilt twice: once as a
Handfast translation (committed in that repo) and once as a Torogao
translation with acceptance metrics (contact-zone ≥95%, climax band
72–86%). It was an Owner-supplied emulation target, grouped by the
Owner with the favourites studies; its source is a Danbooru post,
not rule34video, and the record says so rather than smoothing it
over.

## Intake notes (2026-10-30)

Owner directive 2026-10-30 21:43 PT ("use fathom to reverse
engineer how to create that for handfast and for torogao").
Screened under the Danbooru video carve-out (108 tags, PASS);
downloaded byte-exact (44,183,337 B, sha256 32d97a1e…b0893).
Extraction: fathom-anim-re motion record (schema
fathom-motion-record/3, phase-annotated /4) + an ensemble (contact)
pass on the final shot. Media + excerpts deleted post-verification
per D-248; manifest/records/strips retained — the local video copy
is **not held**, by policy, not by loss. Tier I law throughout:
technique and pattern level only; no characters, designs, or
assets cross into estate work.

## SHOULD-BE-SEEN (written before viewing)

A fully-interpolated 3D animation (no holds, no frame reuse) built
as a segment library rather than a loop, whose longest shot is its
last — a sustained face-to-face after-phase in continuous
near-contact.

## Timed observation focus

- Frame uniqueness and cluster structure (is anything held or
  reused?).
- Cut points and shot-length distribution; where the longest shot
  sits.
- Cycle periods inside shots (the rocking-cycle band).
- Audio event census against the motion record.
- Contact: is it the default state or an event? Activity balance
  between the figures.

## Distillation targets

1. **The measured recipe** — shot structure, cycle band, phase
   boundaries, contact statistics. Question: what does a
   production recipe look like when every number is measured, not
   asserted?
2. **The after-phase** — the receiving figure as the more
   expressive one; the phase face-led. Question: a staging rule
   for post-peak scenes?
3. **The unmeasurables** — rig topology, sync at file level, fine
   face metrics. Question: named as unestablishable, in the record,
   rather than filled in?

Findings: `results/plan-57-raiden-yae-animation-recipe/TECHNIQUE.md`.

## Clean-room rebuild spec

EXECUTED as the two translations (2026-10-30): the Handfast
translation (Rust, jam form — committed in handfast/docs/) and the
Torogao-main translation (contact-zone ≥95% acceptance metric,
climax band 72–86%) — both built from the recipe alone, per Tier I
law.

## Application

- **NSFW application:** Handfast and Torogao main, as above.
- **SFW translation:** none.

## Gate

The translations carry their own acceptance metrics (above); the
extraction itself was verified per the recipe's verification
section (byte-exact download, manifest, ensemble pass). No further
gate is open on this plan; it stands in the curriculum as the
worked example of the full pipeline.

## Deliverables

- `results/plan-57-raiden-yae-animation-recipe/` — technique sheet (landed 2026-11-25, distilled from the 2026-10-30 RECIPE of record), pointing at the extraction tree and the two translations.
