# Plan 08 — Technique Sheet (Pass 2 Distillation)

Source: OBSERVATION.md (screen record + narration record).
A devlog yields process techniques, not solver techniques;
each item below is a *practice* with its mechanism stated.
Verdicts are the estate split: Adopt / Adapt / Reject, with
the reason. Nothing here is a claim the video did not make
or show (claims list: OBSERVATION.md §3).

## T-1 — Reference-first premise adaptation

- **What:** before building anything, the dev plays a
  finished work in another medium (a live-action scene with
  the same landlord/tenant premise), names what he is
  taking ("my comic will borrow ideas from this... that's
  the basic premise"), and only then starts production.
- **Mechanism:** the reference fixes the *premise and beat
  shape* while leaving every production decision open; it
  is a scope anchor, not a template — nothing from the
  reference's execution (shots, dialogue beyond premise)
  is copied on screen.
- **Estate split: ADOPT** (already estate-shaped — the
  estate's clean-room adaptation discipline and its
  ADAPTATION-MAP practice are this, with paperwork). The
  episode is outside confirmation that the sequence
  reference → premise → build is how a solo dev actually
  starts, not a process imposed on him.

## T-2 — Character-first sequencing, episode as the unit

- **What:** the project's first production episode contains
  exactly one workstream: create character #1 and prove her
  look in two test scenes. No environment beyond test sets,
  no page, no second character as a build target (Claire is
  present in files but the episode's hands work on Julia's
  scenes), no story artefact.
- **Mechanism:** look is the project's highest-risk unknown
  (a comic sells on its cast's faces); retiring it first,
  in throwaway numbered test scenes, means every later page
  inherits a solved character. The test scenes are
  disposable by naming (test_01/test_02) — nothing in them
  has to be defended as final art.
- **Estate split: ADAPT** — the estate already sequences
  pilot-first (one girl, all gates, then the fleet), but it
  sizes pilots by *programme*, not by *publishable episode*.
  His unit is the audience-facing episode: each episode
  must end with something showable (here, two renders
  reviewed side by side). The estate version keeps its
  gates and borrows his unit discipline for outward-facing
  programmes (jam devlogs, Strobe progress posts).

## T-3 — The unrecorded iteration (an anti-technique, measured)

- **What:** ~50 minutes of lighting/compositor iteration
  produced a look the dev himself cannot reconstruct at
  review time, one minute later: "I don't remember what I
  did, but I think I added more point lights near her face."
  He is also unsure of his render count ("four or five")
  where his own file counter knows (test_render_005).
- **Mechanism:** interactive DCC iteration keeps state in
  the scene file but keeps *reasons* nowhere; the .blend
  remembers every value and no decision. Recall decays
  immediately; the work is unrepeatable even by its author.
- **Estate split: REJECT the practice; ADOPT its negation
  as confirmed doctrine.** The estate's provenance-first
  records (D-713), written gate benchmarks, and brief-driven
  builds exist precisely so this sentence is never the
  estate's status report. The episode is the control sample
  the plan asked for: this is what the paperwork buys,
  priced in the dev's own words.

## T-4 — Asset-library grafting inside a hand-built scene

- **What:** at 84:00, mid-build, he opens Blendkit inside
  Blender, searches water, and drops a third-party material
  ("Shimmering Pool Water", by Paco Salas per the asset
  card) onto his water plane. The scene around it — wall,
  floor, lights, character — is his.
- **Mechanism:** the library asset is used at the exact
  point where hand-authoring has the worst cost/quality
  ratio (a water surface shader), and nowhere else; taste
  and labour stay concentrated on the character and light.
- **Estate split: ADAPT** — the mechanism is sound and the
  estate does the same class of thing, but his route shows
  no licence step: the asset card is on screen, its licence
  is never opened. The estate version is the same graft
  with the licence recorded at intake (the estate's asset
  screening discipline). His version, unmodified, is
  rejected on that single point: an unrecorded licence in
  a commercial project is a debt with no due-date warning.

## T-5 — The numbered-render review loop

- **What:** iterate in the DCC → export a numbered render
  (test_render_001…005+) → review the exports full-screen,
  side by side, outside the DCC (Windows Photos) → keep or
  adjust. The episode's only evaluation event is this loop;
  its final minute is nothing but the loop's output.
- **Mechanism:** judging the *export* rather than the
  viewport removes DCC chrome, tone mapping surprises, and
  wishful seeing; numbering makes the sequence auditable
  at a glance. It is a gate with one judge and no written
  benchmark.
- **Estate split: ADAPT** — the estate's verdict-pack
  discipline (D-221/D-629: written SHOULD-BE-SEEN first,
  final-artifact frames, per-item verdicts, Owner's eye as
  verdict of record) is this loop plus the two parts his
  version lacks: the benchmark written *before* the render,
  and the verdict recorded *with* the artefact. His loop
  proves the floor of the practice works; the estate's
  additions are what make it survive T-3's memory decay.

## T-6 — Folder and collection discipline

- **What (screen only, never narrated):** project root
  `E:\Eviction\` with functional top folders (comp, misc,
  renders, tex, uploads, vlog among them); geometry under
  `geo\` split into `chars\all.blend` (all characters in
  one file) and `scenes\test_NN.blend`; inside each scene,
  collections geo > chars / env and cameras / lights / fx;
  lights named by role (face_lgt, key_lgt, overhead_lgt);
  environment pieces named by function (back_wall_geo,
  water_plane_geo, fogbox).
- **Mechanism:** names carry the architecture, so a scene
  can be re-entered cold — by the dev next week, or by a
  viewer pausing the video — without a map. The discipline
  is entirely in naming; it costs nothing at build time.
- **Estate split: ADOPT** — estate-shaped as-is (the
  estate's own scene/collection conventions rhyme). Recorded
  because it is the episode's most competent invisible
  practice: the one part of his process that *would*
  survive his own memory, precisely because it is written
  into the artefacts.

## T-7 — Front-loaded narration (the devlog format finding)

- **What:** narration exists at 00:00–04:17 (premise,
  roadmap, scope) and 58:30–59:37 (verdict on the renders),
  and nowhere else: ≈ 6% of runtime, 79.9% of transcript
  segments are whisper loops over music. The narration sits
  exactly where the dev is *not working* (before hands
  start; while renders display) and vanishes wherever work
  happens.
- **Mechanism:** narrating-while-working is a second job;
  under time pressure it is the first thing dropped, and a
  sped-up work section cannot carry real-time narration
  anyway. What survives is intent (before) and judgement
  (after) — the two things an audience can get nowhere
  else — while method, the thing a study programme wants,
  is what the format structurally omits.
- **Estate split: ADAPT for any estate devlog practice** —
  if the estate publishes devlogs, the transferable rule
  is: record the *decision points* contemporaneously (a
  sentence per scope call, at the time), because the
  retrospective voiceover will not contain them — this
  episode's dev, honest and willing, still could not
  reconstruct his own lighting decisions an hour later.

## The plan's two distillation questions, answered

1. **Sequencing — where does his order differ from the
   estate's, and who is right for which goal?** His order:
   catalogue/audience first (back-catalogue shown first),
   reference, character look, test scenes, review. Estate
   order for the same class of work: canon/design authority
   first, pilot with gates, fleet, verdict packs. The
   difference is not the character-first step (shared) but
   *what a finished unit is*: his is a publishable episode
   ending in judged renders; the estate's is a gate record.
   For audience-building and momentum, his unit is right;
   for reproducibility and multi-agent work, the estate's
   is — his own "I don't remember what I did" is the
   evidence that his unit cannot carry a programme bigger
   than one person's memory.
2. **Narration filter — which estate costs are invisible
   in this format?** All of them, measured: gates (his only
   gate is his eye, unnamed as such), provenance (renders
   numbered, parameters unrecorded, one licence unexamined),
   and polish (visible only because polish *is* the content
   here). A viewer of this devlog can learn that the work
   exists and roughly what it looks like; they cannot learn
   what it cost, what was decided, or how to repeat it.
   That is not a defect of this dev — it is the format's
   physics (T-7), and it prices the estate's written-record
   overhead as the cost of making process transferable.
