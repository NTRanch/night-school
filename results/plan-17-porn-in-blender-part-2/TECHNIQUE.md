# Plan 17 — Pass 2 Technique Sheet (Distillation):
# FINISHING CONVERGENCE

Source: `OBSERVATION.md` (Pass 1). Comparison sources:
Plan 02 TECHNIQUE.md (LANDED, gated — firm); Plan 11
TECHNIQUE.md (present at this run's P2 check —
**LANDED-SOURCE**); Plan 13 (TECHNIQUE.md **not** landed
at this run's P2 check — its OBSERVATION.md landed during
this run and rows were built PROVISIONAL on it; **at
delivery, Plan 13's TECHNIQUE.md landed and all six rows
were reconciled against it — every row holds; see the
reconciliation note at the end**). Plan 16 (Part 1) had
not landed beyond INTAKE/MANIFEST at P2; at delivery its
OBSERVATION.md has landed and confirms the join
(OBSERVATION §10): Part 1 is the setup-and-pose session
for the **same Domina file** (`Domina_1.0.1`), so Part
1's steps precede this run's F-17-01…18 unchanged.
Estate context: Blender 5.2.3 (source video: Blender
5.0.1), Plan 02 NS02 template + Plan 11 NS11
Light-Groups variant.

## The headline finding

**The integrated workflow contradicts the deep-dives.**
Divinity Studio's own specialist videos teach
decomposition: Plan 11 relights per light-group in comp;
Plan 13 rebuilds the beauty from component passes so
every decision survives the render. Part 2 — the same
creator finishing a real delivery — does neither. It
relights *interactively* (viewport renders, lamps moved
and halved by eye), renders **once** at a deliberately
cheap sampling pair, and comps a **global grade on the
combined image**. Its only pass algebra double-counts
Volume Direct + Emission at 0.492 as an atmosphere
effect. Stated precisely:

> **Part 2's philosophy is bake-it-in-the-render,
> grade-the-combined; Plans 11/13's philosophy is
> decompose-it-so-comp-can-re-decide. The creator owns
> both and chooses the first for production.**

## Comparison table — vs Plan 11 (Light Groups) [LANDED-SOURCE]

| Row | Topic | Plan 17 (Part 2) evidence | Plan 11 evidence | Verdict |
|---|---|---|---|---|
| C-11-A | Light groups in production | Pass list terminates at Noisy Image; **no Combined_\<group\> outputs exist** (OBS §6, t3150) | The whole video: one group per lamp, beauty = Σ groups + Emission + Volume (C-11-1/2) | **DIFFERENT-PHILOSOPHY** |
| C-11-B | Ungrouped energy (Emission / Volume) | Emission (dome + rings) and Volume Direct are enabled, inspected solo, and used in comp (OBS §6, §8) | Group-pure sum is a figure on black; Emission + Volume Direct must be added back (C-11-2) | **AGREE** — both creators' scenes prove ungrouped energy is real image content, not garnish |
| C-11-C | Denoise placement | Render-time denoise ON; Denoising Data passes OFF; no comp Denoise node appears (OBS §6–§8) | Denoise is the terminal *comp* stage, guided by Denoising Albedo/Normal, so a relight never re-renders denoise (C-11-4) | **DIFFERENT-PHILOSOPHY** (placement of the same stage: renderer vs compositor) |
| C-11-D | Glare | Glare Bloom then Glare Streaks applied to the **summed, graded master** (OBS §8.4) | Glare groups on the **rim branch before the sum**, so bloom belongs to one lamp's light (TECHNIQUE Target 2, op 4) | **AGREE** on mechanism (glare as a comp stage); **DIFFERENT** in placement (branch vs master) — counted AGREE with the placement difference named |
| C-11-E | HSV node | HSV as a *global grade*: Saturation 1.025 on the combined image (OBS §8.3) | HSV Value as a *per-group gain* (rim ×2.000), Hue as per-group retint (C-11-3) | **CONFIRMATION** — same node grammar, different job: the node is the creator's universal adjuster |
| C-11-F | Pass persistence | Output configured: OpenEXR RGBA Float (Full) **DWAA (lossy)**, path /tmp (OBS §8) | Nothing saved on screen; workflow is session-resident (OBS UNREADABLE 2); estate filled the gap with multilayer EXR 32-bit **ZIP** | **AGREE** that persistence matters (17 configures it, 11 omits it); **conflict in codec**: DWAA spends its error in the dark gradients the estate contract chose ZIP to protect — estate keeps ZIP (see PASS3, U-8) |
| C-11-G | Lamp grammar | Five lamps, role-named `fill_lgt_01/02, key_lgt, rim_lgt(.001)`; fills read 50 W / 6500 K (OBS §5) | Four lamps, same role names; fill_lgt_01 read 50 W / 6500 K / radius 0.5 m (C-11-1) | **CONFIRMATION** — same standing scene family, same fill values, across two characters (Tifa → Domina) |
| C-11-H | Environment | Starfield **dome geometry**, emissive in effect (OBS §3) | Emissive **photo plane** backdrop, Emission Strength 1.000 (OBS §3:00) | **AGREE** — emissive environment geometry is the backdrop mechanism in both; geometry (dome vs plane) is scene dressing |

## Comparison table — vs Plan 13 (Beauty Pass) [RECONCILED AT DELIVERY]

Source status: rows were built PROVISIONAL at P2 from
Plan 13's landed OBSERVATION.md + its plan file's scope;
Plan 13's TECHNIQUE.md landed before this run delivered
and every row was checked against it (reconciliation
note at the end). Verdicts below are the reconciled
verdicts.

| Row | Topic | Plan 17 evidence | Plan 13 evidence (OBSERVATION, landed) | Verdict |
|---|---|---|---|---|
| C-13-A | Production render pair | Retuned to **0.0300 / 512, GPU** (OBS §7) | Render at **0.0300 / 512, GPU**, Min 120 (OBS 7:40) | **AGREE** — the pair is the creator's production standard across both videos (17's Min Samples 0 vs 13's 120 is the only delta) |
| C-13-B | Beauty decomposition | Never decomposed: the grade acts on Combined directly (OBS §8) | Beauty rebuilt from (Direct+Indirect)×Color per component + Volume + Emission, factors 1.000, no clamping (C-13-1/8) | **DIFFERENT-PHILOSOPHY** |
| C-13-C | Role of the Emission pass | Re-added at **0.492 on top of** a Combined that already contains it — a glow boost (OBS §8.2) | Added **raw at unity because the reconstruction is missing it** — omit it and the background vanishes (C-13-5) | **DIFFERENT-PHILOSOPHY** — same pass, opposite algebra: ingredient vs effect |
| C-13-D | Finishing chain grammar | B/C → HSV (Sat 1.025) → Color Balance → Glare Bloom → Glare Streaks → Lens Distortion 0.040 (OBS §8) | RGB Curves → HSV → Glare Bloom add-back → Glare Streaks (High, Thr 1.000, Smooth 0.100) → Lens Distortion 0.060 → Scale 1.5× → Box Sharpen (C-13-7) | **AGREE** — the tail grammar is the same sentence in both videos: grade, bloom, streaks, dispersion; near-identical Streaks values |
| C-13-E | Delivery manufacture | 720p master → **external web AI upscale** (OBS §9) | 720×1280 master → in-Blender **Scale 1.5× + Box Sharpen**, PNG 16-bit (OBS 34:00) | **DIFFERENT-PHILOSOPHY** in route (outsource resolution vs manufacture it in comp), **AGREE** in premise: delivery resolution is made in post, not rendered |
| C-13-F | Denoise count | One denoise run (render-time) (OBS §7) | Two denoise runs: renderer's (reference beauty) + compositor's (recreation) (OBS premise surprise 2) | **DIFFERENT** — 13 pays denoise twice as the price of decomposition; 17 pays once |

## Comparison table — vs Plan 02 (NSFW stills, RamFutaNSFW) [LANDED]

| Row | Topic | Plan 17 evidence | Plan 02 evidence | Verdict |
|---|---|---|---|---|
| C-02-A | Build from black | Dome in → character a silhouette → lamps one at a time against the camera render (OBS §3, §5) | Silhouette-first: backdrop emissive + World 0, then lamps in role order in camera view (Target 1, Adopt) | **AGREE** — third creator-workflow confirmation of the estate's adopted build order |
| C-02-B | Environment doctrine | Emissive dome geometry + **gradient world** (World_OW2); no HDRI anywhere (OBS §3, §5) | Emissive photo backdrop + **World 0.000**; "we don't want to do an HDR" (OBS §5) | **AGREE** on no-HDRI emissive environment; **DIFFERENT** on the world term (authored gradient vs zero) |
| C-02-C | Rim colour | Rims are neutral Points (6500 K family); scene colour comes from emissive props/dome (OBS §5) | Rim hue **sampled from the backdrop's neon** (HSV 0.817/0.932/1.000) so subject and ground share a palette (Target 1) | **DIFFERENT** practice (not philosophy): two ways to bind subject to ground — tint the lamp, or light neutrally over a coloured environment |
| C-02-D | Render economics — what carries quality | Template pair 0.0100/4096 **inherited**, then production render at **0.0300/512**: quality is carried by environment + lighting + comp; samples are bought down once those hold (OBS §2, §7) | The adaptive pair 0.0100/4096 IS the economics; threshold does the work, 4096 is a ceiling (Target 3, Adopt) | **AGREE in principle, CONFLICT in letter** — 17 proves the pair is a *template default to be retuned per delivery*, not a prescription; the estate template should record the pair as defaults with a named retune step (F-17-11), which Plan 02's sheet does not currently say. Named as this run's one correction to a landed sheet — carried into PASS4 as a proposal, not an edit (other plans' files are never modified) |
| C-02-E | Post manufactures what render omits | Lens flaw synthesised in comp (Dispersion 0.040); delivery resolution synthesised by upscale (OBS §8.5, §9) | DoF synthesised in post (Lightroom Lens Blur 50/50 from AI depth); render shot deep-focus (C-02-9) | **AGREE** — the doctrine "render the clean plate, synthesise the optical effect in post" holds across both creators |
| C-02-F | Where finishing lives | Entirely inside Blender's compositor + a web service; no Photoshop/Lightroom appears | Lightroom (Lens Blur) + Photoshop (signature only) (OBS §7) | **DIFFERENT** toolchain, same doctrine as C-02-E |
| C-02-G | Inspect before finishing | Passes solo-inspected in comp before any adjustment (Emission solo, OBS §8.1) | Clay check: grey-material render reviewed before the beauty render (Target 2, item 7) | **CONFIRMATION** — an inspection gate precedes finishing in both workflows; the artifact inspected differs (pass vs clay render) |
| C-02-H | Template discipline | The whole Part 2 workflow runs inside the creator's standing scene family (collections, lamp names, world node World_OW2) — a template *lived in*, never exported (OBS §1, §5) | The estate's form is the *scripted, versioned* template (NS02) rebuilt from the artist's per-shot practice (Pass 3) | **CONFIRMATION** of the premise (a standing template is how quality repeats), **DIFFERENT** in form: his template is a directory of scene files; the estate's is code. The estate keeps its form (determinism doctrine) |

## Row tally (for the gate)

- vs Plan 11 (LANDED-SOURCE): 8 rows — AGREE 4
  (C-11-B, C-11-D, C-11-F-partial counted AGREE,
  C-11-H), DIFFERENT-PHILOSOPHY 2 (C-11-A, C-11-C),
  CONFIRMATION 2 (C-11-E, C-11-G).
- vs Plan 13 (PROVISIONAL at P2, reconciled at
  delivery — all hold): 6 rows — AGREE 2 (C-13-A,
  C-13-D; C-13-E counted DIFFERENT-PHILOSOPHY-route),
  DIFFERENT-PHILOSOPHY 3 (C-13-B, C-13-C, C-13-E),
  DIFFERENT (non-philosophy) 1 (C-13-F).
- vs Plan 02 (LANDED): 8 rows — AGREE 4 (C-02-A,
  C-02-B, C-02-D-principle, C-02-E), DIFFERENT 3
  (C-02-C, C-02-F, C-02-H-form), CONFIRMATION 2
  (C-02-G, C-02-H-premise) — C-02-D and C-02-H each
  carry two verdicts by design and are counted in both
  their classes in the run report.

## Render economics — the cross-plan answer

What carries quality, per the three landed/observed
workflows: (1) the environment (emissive, authored —
02/11/13/17 all agree); (2) role-built lighting tuned
against the live render (02/17); (3) the compositor's
grade+glare tail (13/17, near-identical grammar).
What is ceremony: sample ceilings (4096 inherited,
512 delivered — 17 proves the ceiling is headroom, the
threshold is the working setting, exactly as Plan 02's
sheet says in principle), and any pass that is enabled
but never consumed (11's component sprawl; 17 enables
only what its comp consumes — Depth/AO enabled but
unconsumed in 17's visible tree are the exception,
recorded in OBS §6 without a claim).

## Reconciliation note (Plan 13 rows — closed at delivery)

Rows C-13-A…F (6 rows) were PROVISIONAL at P2 (built on
Plan 13's landed OBSERVATION.md + plan scope). Plan
13's TECHNIQUE.md landed before this run delivered;
reconciliation against its dispositions: **all six rows
hold, no verdict changed.** Specifically: C-13-A —
its Target 2 confirms 512 / 0.0300 / min 120, render
Denoise ON. C-13-B — its Target 1 names the estate form
NS13 "Back-to-Beauty", a complete-sum faithful recipe
(Adopt), with completeness as the failure mode (its
first A/B failed on a missing Volume branch) — the
production-route framing this row assumed is the
sheet's own. C-13-C — its recipe states Emission is
"added raw" and enters the beauty *only* there, the
exact ingredient-role the row contrasts with Part 2's
0.492 effect-add. C-13-D — its Target 3 finishing list
matches (Bloom add-back Medium/0.500; Streaks High,
1.000, 0.100, 4 streaks, Iterations 3, Fade 0.900,
Color Mod 0.250; RGB Curves; dispersion settled 0.060;
Scale 1.5×; Box Sharpen). C-13-E — its output is
720×1280 PNG, 16-bit selected. C-13-F — its Target 2
states the second denoise is the recreation's *cost*,
in the sheet's own words. **PROVISIONAL rows at
delivery: 0.** Plan 16's join is confirmed by its
landed OBSERVATION (same Domina file, setup-and-pose
session); only its TECHNIQUE-level numbering remains
for a future concatenation, per OBSERVATION §10.
