# Plan 08 — Pass 3 Rebuild Record (procedural)

Per the plan's clean-room rebuild spec: **no code rebuild**.
The rebuild is this document — the episode's build sequence
written as a plan-shaped document from the technique sheet
alone (video closed), then diffed against one estate
programme plan: the jam **BUILD-PLAN**
(`~/workspace/jam-entries-20261104/BUILD-PLAN.md`, D-941
programme; read in this run). Claims C-1…C-8 from
OBSERVATION.md §3 are verified against the episode record
at the end.

## Part 1 — The episode's build sequence, plan-shaped

**Project:** "Eviction", an adult comic in Blender
(tentatively titled; premise: a tenant who cannot pay rent,
a landlord who takes advantage — adapted from a named
live-action reference scene).
**Producer:** one person (DivinityStudio, "a one man band").
**Stated horizon:** "small scale... probably done within a
week or so"; stated long-term ladder: solo small projects
of increasing complexity toward a team-scale game.
**Episode 1 scope (as executed, from the screen record):**

| # | Step (his order) | Evidence | Exit state |
|---|---|---|---|
| 1 | Audience surfaces and back-catalogue already exist (prior series, tutorials; Patreon/SubscribeStar linked) | OBS §1 Block A | Channel with 115 subscribers and a monetisation link tree predates the project |
| 2 | Premise fixed by reference: play the source scene, state the borrowing | Block A; N1 | Premise sentence exists ("borrow ideas from this") |
| 3 | Character #1 created in DAZ Studio; strand hair fitted there | Block B | Genesis character export-ready |
| 4 | Bridge export to Blender 5.2.0 LTS; import inspected full-body | Block B | Character standing in Blender with rig (Rigify/MHX-class, 294 bones) |
| 5 | Project skeleton: `E:\Eviction\` functional folders; `geo\chars\all.blend`; `geo\scenes\test_NN.blend`; collection taxonomy + role-named lights | Blocks C/G; t840/t5280 | Any scene re-enterable cold |
| 6 | test_01: camera → HDRI world (DTHDR-RuinsB-500, Strength 2.000) → spot rig (face_lgt, overhead_lgt) → fogbox → hair iteration (≥4 colours tried) → compositor grade (Glare → RGB Curves → Color Balance → Lens Distortion) | Blocks C–E | A repeatable look chain in one scene |
| 7 | Numbered test renders exported (≥ test_render_005) and reviewed full-screen, side by side, outside the DCC | Block E; t3540; N2 | One kept "promotional image"; purple hair kept ("this is what I'm going with") |
| 8 | test_02: second scene, studio HDRI (studio_small_08_1k) → primitive set (extruded pyramid wall, cylinder) → volume fog (Scatter 0.050 / Absorption 1.000, Mix 0.500, grid-read) → Blendkit water material grafted → pink spot rig (key_lgt 7500 K, 200 W, 45°) → pose → save | Blocks F–G; t5040/t5280 | Pool-scene render; file saved on camera |

**What the sequence never contains:** a comic page, panel,
lettering, story text, a second built character, an
environment beyond the two test sets, any written plan,
budget, or gate other than the dev's eye at step 7.

## Part 2 — Diff against the jam BUILD-PLAN

The BUILD-PLAN governs two hand-made jam games in 25 days:
written scope ceilings (≤5 states, ≤3 stages, ≤2,500 words),
a milestone ladder with exit tests and dates, provenance
discipline from day one, compliance checklists wired into
the submission milestone, and session budgets sized to the
Owner's work week. Differences, each judged:

| # | Difference | His way | BUILD-PLAN way | Judgement |
|---|---|---|---|---|
| Df-1 | **Unit of planning** | The publishable episode (ends in judged renders) | The dated milestone with an exit test | **ADAPT** (see T-2): episodes for audience-facing work; milestones stay for programme work. Neither replaces the other. |
| Df-2 | **Scope control** | Verbal and retrospective: "small scale... a week or so"; scope discovered by doing | Written ceilings, countable, set before building; "ceilings shrink before milestones move" | **REJECT his way for estate use.** His ceiling is a hope; the plan's is a contract. His episode stayed small — but nothing in his process would have caught it growing. |
| Df-3 | **Provenance / records** | Numbered renders only; parameters and reasons unrecorded ("I don't remember what I did") | Git history as authorship evidence; records as a day-one discipline | **REJECT his way** (T-3). The plan treats the record as part of the artefact; his process proves the counterfactual. |
| Df-4 | **Evaluation** | One judge (himself), full-screen export review, no written benchmark | Expected-vs-seen benchmarks written first; gates; Owner's eye as verdict of record for art | **ADAPT his loop** (T-5): judging the export outside the DCC is genuinely good and cheap; the estate keeps its written benchmark on top. |
| Df-5 | **Sequencing of risk** | Highest-risk unknown (character look) retired first, in disposable test scenes | Skeleton first (window/state switching), mechanic/playable next, content last | **ADOPT his ordering for art-led work.** The BUILD-PLAN's skeleton-first order suits code risk; for a comic (and for the estate's character programmes) look-first is the honest risk order — and the estate already works this way in its character lanes (pilot before fleet). For code-led jam work the plan's order stands. No change to the BUILD-PLAN; the difference is domain, not error. |
| Df-6 | **Assets** | Third-party material grafted mid-build from an in-DCC library; licence not examined on screen | Closed asset lists per jam regime; licence noted in repo; paid/pre-existing rules differ per track and are checked at submission | **REJECT his way** (T-4): not the graft — the unexamined licence. The BUILD-PLAN's closed lists are jam rules, but the estate's own screening rule (licence recorded at intake) is the general form. |
| Df-7 | **Calendar honesty** | "Within a week or so" — no dates, no session count, no work-week constraint visible | Session count derived from the Owner's actual week (9 build evenings); dates anchored to an immovable close | **REJECT his way for estate use.** His estimate is unfalsifiable as stated; the plan's arithmetic is checkable line by line. (Whether he *hit* his week is unknowable from episode 1 — C-2 below.) |
| Df-8 | **Compliance surface** | None visible (no jam, no ruleset; his constraints are platform ToS only) | Two opposite rule regimes kept in separate repos; checklists ticked at submission | **NO EQUIVALENT — recorded, not judged.** His programme has no external rules to comply with; the diff item exists so the absence is named rather than silently mapped onto estate practice. |

## Part 3 — Claims verification (C-1…C-8)

| Claim | Verdict | Basis |
|---|---|---|
| C-1 Whole process documented, concept to final render | **PARTIALLY REPRODUCED** | Concept (premise + reference) and final renders are in the episode; the middle ~94% is documented only as sped-up, un-narrated footage — the process is *shown* but not *documented* in any retrievable sense (T-3/T-7). The letter of the claim (it is all on the video) holds; its substance (a record someone can use) does not. |
| C-2 Small-scale, done "within a week or so" | **UNTESTABLE-IN-ROUTE** | Episode 1 contains no dates and no completion; the estimate can only be judged against later episodes, which are outside this plan. Recorded as an open estimate, not a finding. |
| C-3 Episode 1 = first character in DAZ → Blender | **REPRODUCED** | Screen Blocks B–C show exactly this, in this order (DAZ 05:00–07:00; Blender from 08:00). |
| C-4 Premise borrowed from the reference scene | **REPRODUCED** | Narration states it; screen shows the scene playing (03:00) and the premise matches (tenant/rent/landlord). |
| C-5 Work footage is sped up | **REPRODUCED** | Stated in N1; consistent with all screen evidence (89 min of edited footage covering two full scene builds; no real-time work segment exists in the sampled record). |
| C-6 Look reached by adding lights near/behind the face; purple hair kept; render is "a promotional image" | **REPRODUCED with one correction** | The rig the screen shows is **spot** lights (face_lgt/overhead_lgt), not the narration's "point lights" (OBS §2, disagreement 1); hair settles lavender-purple at 48:00 and is kept in both final renders; the "promotional image" framing is his own at 58:30. |
| C-7 One chars file feeds numbered scene tests under folder discipline | **REPRODUCED (screen)** | `geo\chars\all.blend` + `geo\scenes\test_01/test_02.blend` in title bars (t840, t1020, t5040, t5280). |
| C-8 Library material acceptable inside a hand-built scene | **REPRODUCED as practice; licence leg UNREADABLE** | Blendkit graft shown at 84:00 (t5040); the asset's licence terms never appear on screen — neither granted nor violated in evidence. The estate's objection (T-4) is to the missing record, not to a proven breach. |

Pass 3 closes: the diff document exists, each difference is
judged adopt/adapt/reject with a reason (Df-1…Df-8), and no
technique claim beyond the episode's evidence has been made.
