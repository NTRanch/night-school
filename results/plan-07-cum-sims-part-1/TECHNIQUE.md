# Plan 07 — Pass 2 Technique Sheet (GATED)

- **Source draft:** Azoth, `PASS2-AZOTH-DRAFT.md` (primo `~/grok-reports/night-school-plan07-distillation.md`, 28,848 B)
- **Evidence of record:** `OBSERVATION.md` — sha256 `e11656413dcba751d0801f1d777b4c5912a665a7d157724e739da783e6e4a60c`, 366 lines. The draft cites this exact hash; verified identical to the run-dir copy at gating time.
- **Gate (coordinator, 2026-11-06): PASS — all 20 entries (T-01…T-20) verified line-by-line against OBSERVATION.md.** Every numeric value in the sheet was re-matched against the observation's §2/§4 tables, Physical-tab record, Vellum f11/f12/f14/f15 record, and f10 Blender transforms: particle-separation table (0.1/0.45/0.13/1.43/1.3/0.151), viscosity drags (1.68263/1.51632/0.05632), Density 1000→718, meshing table (0.75→0.3→0.44 voxel; 2.933 influence; erosion 0.8; adaptivity 0.005), Vellum grain set (0.1 size, 10000 points, mass 0.1, 0.5→3.95 viscosity, 0.001→0.13 surface tension) — zero discrepancies found. Counts check: Adopt 8 · Adapt 8 · Reject 4 as declared.
- **UNREADABLEs honoured:** all five OBSERVATION §7 items carried unfilled (surface-tension field, substeps, scattering expression, Vellum friction, cache sizes/times); "scale intact" stays UNVERIFIED; the unit question stays UNANSWERED. The four binding findings (Chapter-1-only, 2 m sphere scale fake, partial collision, scale-intact unverified) are carried at the head of the sheet and inside the affected entries.
- **Gate notes:** (1) DOCUMENTATION contrasts (SideFX docs via the distill-prep) are fenced and labelled, and carry no video values — accepted as fenced contrast only; they are not evidence about the video. (2) Two draft additions beyond the observation's own registers (jitter-after-increase as unsettled; a "not in video" list) are honest fences, retained.
- **Coordinator answers to the draft's QUESTIONS FOR PAX** (recorded 2026-11-06):
  1. Spoken surface-tension "10" may seed the Pass 3 rebuild as a *spoken-only starting value*, never as a pane-verified preset value; the rebuild's sensitivity strip is where it earns or loses standing.
  2. **The estate has no Houdini** (checked primo and sandbox, 2026-11-06; Blender 5.2.3 LTS is the primo pin). The T-02 Source Smoke workaround is therefore moot for the estate route and is recorded as a 19.5.435-specific finding. Pass 3 route = the plan's own fallback: "the estate's available FLIP route" — Blender Mantaflow FLIP, with every parameter mapping and every unmappable parameter recorded as a route deviation, and Houdini-side verification of the sheet's Houdini claims marked UNTESTABLE-IN-ROUTE rather than reproduced/refuted.
  3. Unit discipline: the rebuild stays faithful at the video's metre scale; a centimetre retune is a Pass 4 adaptation question, not a Pass 3 invention (T-20 stands).
  4. Body collision and directed emission are NOT to be invented in Pass 3; Plan 06 (Part 2) is the curriculum's scheduled source.
  5. T-17: preview-only for Vellum grain meshing is accepted.
  6. Import-side checks in Pass 3 use the estate Blender pin (5.2.3 LTS), not the video's 3.3.9.

---

## Binding findings (carry into every entry; do not soften)

1. **Foundations only (Chapter 1).** The observation states the video is Chapter 1 of a two-chapter tutorial: SFW generic demo (two icospheres + ground plane). Chapter 2 (forces, directing fluid, anatomical application) is a different video and is **not** in this record. Entries below are technique claims about FLIP/Vellum **mechanics**, not about an applied anatomical scene. (OBSERVATION.md §"What this video actually is"; SHOULD-BE-SEEN close.)

2. **"Small-scale" look is faked.** The FLIP source sphere measures **Dimensions X 1.9 m, Y 2 m, Z 2 m** at **Location X −0 m, Y 7 m, Z 6 m**, scale 1.000 (f10). Scene units are never named; metres are Blender default. The droplet/strand look is produced with **surface tension + viscosity** on that 2-metre blob, not by modelling at centimetre scale. **Unit/scale question = UNANSWERED by the source.** Any entry that depends on absolute physical scale is flagged. (OBSERVATION.md §3; SHOULD-BE-SEEN "Small-scale — CONTRADICTED".)

3. **Parameter pane governs.** Where narration rounds or contradicts the screen, **screen values only** are cited. Known disagreements: radius-scale worked example (speech 1.13/0.26 vs screen Particle Radius Scale **1.2**, Particle Separation **0.13**); separation speech "0.15" vs screen **0.151**; Vellum "increase friction" with no friction field framed; Density field **718** at 24:50 with no spoken announcement. (OBSERVATION.md §6.)

4. **Collision handling is partial.** Seen: DOP Ground Plane (infinite) + Merge/affector set to **Mutual** (19:35–21:08). **No shaped/body collider** appears. This sheet does **not** distill a body-collision technique the video does not contain. (OBSERVATION.md SHOULD-BE-SEEN "Collision geometry handling — PARTIALLY SEEN".)

---

## Technique sheet

Entries are ordered roughly by the observation's focus list (§1–§5), then Vellum, then workflow conventions. Verdict = **Adopt** (use as taught for Torogao foundations), **Adapt** (use with named change), or **Reject** (do not use for the stated purpose).

### T-01 — Single-shot FLIP fill from SOP Path (static sphere, gravity only)
**Verdict: Adopt**

- **(a) Settings (screen / observation):** FLIP Object Initial Data (f17): Input Type `Surface SOP`; Initial Configuration `Grid`; Jitter Seed 0; **Jitter Scale 0.1**; Use Object Transform on. SOP Path pointed at imported sphere via backtick `opinputpath` expression ("..", input 0) replacing default `../particlefluidobject/defaultfluid` (15:52–16:27). **No initial velocity** set anywhere. Source geometry: Blender icosphere `FlipSourceGeo`, Dimensions **X 1.9 m, Y 2 m, Z 2 m**, Location **X −0 m, Y 7 m, Z 6 m**, rotation 0°, scale **1.000** (f10).
- **(b) Mechanism:** One-time particle fill from surface SOP; fluid falls under gravity with no emitter velocity.
- **(c) Estate (Torogao):** Useful as a cold-start / pour-test preset for FLIP mechanics before continuous emission or directed streams (Chapter 2 territory — not in this video).
- **Scale flag:** Depends on the unanswered unit question if treated as "small-scale anatomy"; treat as metre-demo mechanics only.

### T-02 — Continuous emission via Volume Source + Points from Volume
**Verdict: Adapt**

- **(a) Settings:** SOP Path on FLIP Object emptied. **Volume Source** DOP sources a **Points from Volume** SOP from the same sphere; point separation bound to FLIP Object particle separation by copy-parameter → paste-relative-reference (29:56–31:05; f06: volumesource2 → flipsolver1). Workarounds stated and required: source mode **Source Smoke** (Source FLIP "does not work here", 31:43–31:54); auto-added source operations cleared; Source Particles group left empty (32:35–33:02).
- **(b) Mechanism:** Continuous particle injection from a volume-sampled point cloud wired into the FLIP solver, with particle separation kept in lockstep with the FLIP Object.
- **(c) Estate (Torogao):** Continuous stream foundation for Torogao emitters — but only as mechanics; aiming/forces are Chapter 2 (absent).
- **(d) Adapt — what changes and why:** Keep the Source Smoke workaround and empty Source Particles group until estate Houdini build is verified to accept Source FLIP (observation: Source FLIP failed in **19.5.435**). Do **not** invent a body-shaped emitter; video uses the same sphere. Bind separation by relative reference as shown.

### T-03 — Emission timing by Volume Source Activation keyframes
**Verdict: Adopt**

- **(a) Settings:** Volume Source **Activation** parameter (1/0) keyframed (Alt+click) to cut the stream at a chosen frame (35:18–36:08). Source geometry itself is **never animated**.
- **(b) Mechanism:** Binary on/off of the source DOP controls duration; motion of the emitter mesh is not required for timing.
- **(c) Estate (Torogao):** Preferred cutoff method for short bursts without animating emitter transforms — matches "short-duration emission" partially seen in SHOULD-BE-SEEN.

### T-04 — Reseeding usually off; jitter up to break grid
**Verdict: Adopt**

- **(a) Settings:** Particle Motion → Reseeding discussed (34:04–34:45); creator **usually disables** it ("I get better results without it"). Jitter increased to break grid pattern (33:37–33:50). As-created Jitter Scale **0.1** (f17); later increase magnitude UNREADABLE as a single settled screen value beyond the as-created figure.
- **(b) Mechanism:** Reseeding can refill/reshape the particle field in ways that fight a deliberate stream breakup; raising jitter randomizes the initial lattice.
- **(c) Estate (Torogao):** Default Torogao FLIP preset: reseeding off unless a specific fill-hole need appears; start jitter at **0.1** and raise only while watching the pane.

### T-05 — Frame-driven expression for time-varying scatter / viscosity ramp
**Verdict: Reject (as a copyable recipe) — expression UNREADABLE**

- **(a) Settings:** Scattering varied over time by a frame-driven expression (38:08–38:30). Exact expression **UNREADABLE** (OBSERVATION.md §7 item 3): whisper fragments only; reading as `$F * 0.01` would be inference. Same frame-parameter trick noted for ramping viscosity so fluid "stops over time" (40:28–40:48) — **no numeric ramp endpoints on screen**.
- **(b) Mechanism (qualitative only):** Drive a parameter from frame number so scatter or viscosity evolves during the shot.
- **(c) Estate (Torogao):** Idea is useful; **do not copy a fabricated expression**. Re-author under estate naming once a readable expression is captured or written from first principles.
- **(d) N/A (Reject):** No Adapt path until expression is readable or rewritten.

### T-06 — FLIP Object resolution triad (Particle Separation / Radius Scale / Grid Scale)
**Verdict: Adapt**

- **(a) Settings (screen table, OBSERVATION.md §2):**

  | When | Particle Separation | Particle Radius Scale | Grid Scale | Frame |
  |---|---|---|---|---|
  | As created, 15:20 | 0.1 | 1.2 | 2 | f17 |
  | Experiments, 24:50 | 0.45 | 1.2 | 2 | f03 |
  | Experiments, 25:22 | 0.13 | 1.2 | 2 | f04 |
  | Experiments, 25:58 | 0.13 | 1.43 | 2 | f05 |
  | Sourcing setup, 30:12 | 0.13 | 1.43 | 1.3 | f06 |
  | Settled (meshing read-back), 48:50 | **0.151** | — | — | f09 + crop |

  Collision Separation **0.2**, disabled (f17/f03). Closed Boundaries all off (f03). Creator's explanation (24:40–26:20): particle separation = point distance / resolution (cost rises as it falls); particle radius scale × particle separation = collision radius; grid scale = voxel scale (lower = better resolution, much higher cost). Spoken worked example does **not** match screen (§6 disagreement 1) — **screen governs**.
- **(b) Mechanism:** Separation sets particle spacing; radius scale sets collision size relative to separation; grid scale sets pressure/velocity voxel size relative to separation.
- **(c) Estate (Torogao):** Use the **settled Particle Separation 0.151** (f09) as the Chapter-1 reference point for meshing-matched sims, not the spoken "0.15".
- **(d) Adapt — what changes and why:** Retune separation/radius/grid for Torogao emitter size; **do not** treat 0.151 as physically "small-scale" (see Binding finding 2 — unit question UNANSWERED). Prefer screen values over any spoken arithmetic. Radius Scale / Grid Scale at the settled meshing moment are **not** re-read on f09 (table shows "—"); if estate needs them, re-read live rather than inventing from earlier experiment rows.
- **DOCUMENTATION contrast (not video):** SideFX Houdini 22.0 liquids.html states Particle Separation is in scene units (= metres in dynamics) and gives `0.1` as a **unit example** (10 cm), not as this video's value — `~/grok-reports/night-school-plan07-distill-prep.md` Target 1. Numeric UI defaults for Radius Scale / Grid Scale remain UNVERIFIED in that prep.

### T-07 — Enable Viscosity on FLIP Solver; keep object viscosity low
**Verdict: Adapt**

- **(a) Settings:** FLIP Solver `flipsolver1` Viscosity sub-tab (21:50, f13): **Enable Viscosity on**; Solve Viscosity with Adaptivity off; Viscosity by Attribute off; Mix Method `Copy`. FLIP Object Physical tab Viscosity dragged live: **1.68263** (21:35, f01), **1.51632** (22:15, f16), **0.05632** (22:58, f02) — lowered because "even a little viscosity here will be pretty viscous" (22:34–22:40). Later zeroed/disabled for a comparison run (26:32–27:05). Volume Motion (f13): Velocity Transfer `FLIP (Splashy)`, Force Scale **1**, Velocity Smoothing **0.1**, Smooth Surface on, Update Surface `Advect`, Update Velocity `Advect`.
- **(b) Mechanism:** Viscosity is a separate solver toggle from the object field; with Enable on, small object viscosity already reads as thick at this demo scale.
- **(c) Estate (Torogao):** Always verify **Enable Viscosity** on the solver when dialling object viscosity; start near **0.05632** (f02) and raise only while watching behaviour — not from docs "thick fluid ~1000" guidance without a live re-tune (**DOCUMENTATION** tip in flipobject.html / flipviscosity.html per distill-prep; not used as video value).
- **(d) Adapt — what changes and why:** Splashy velocity transfer is default-class and fine for foundations; Torogao gel/cum look will need viscosity re-tuned to estate emitter scale (unit question UNANSWERED — flag). Do not assume the mid-drag values 1.68 / 1.52 are targets.

### T-08 — Surface tension for droplet/strand cohesion (FLIP)
**Verdict: Adapt — magnitude UNREADABLE on screen**

- **(a) Settings:** Surface tension enabled on the solver alongside viscosity (21:57). Strength **spoken only: "surface tension that is 10"** (22:54). Surface Tension sub-tab **never opened** in any sampled frame — on-screen value **UNREADABLE** (OBSERVATION.md §7 item 1). Viscous, droplet-forming behaviour SEEN with spoken "10" producing coherent droplet and strands / "clear lines" (36:12–36:27).
- **(b) Mechanism:** Surface tension pulls the free surface toward coherent blobs and thin strands; combined with viscosity it fakes a small-scale look on a metre-sized source.
- **(c) Estate (Torogao):** Adopt the **enable + pair with viscosity** practice for cohesive emission; treat magnitude **10 as spoken-only**, not pane-verified.
- **(d) Adapt — what changes and why:** Re-measure Surface Tension on a live Houdini **19.5.x / estate** pane before locking a Torogao preset. **Scale flag:** this is the primary fake-small-scale lever (Binding finding 2); do not claim centimetre-scale physics.
- **Substeps:** never opened, never mentioned — **UNREADABLE** (§7 item 2). Do not invent substep counts for this technique.

### T-09 — Physical tab friction / bounce / density (screen record)
**Verdict: Adapt (density caution) / partial**

- **(a) Settings (f01 + crop, f16, f02):** Bounce **0** · Bounce Forward **1** · Friction **0** · Dynamic Friction Scale **1** · Temperature **0** · **Density 1000** early; at 24:50 Density field reads **718** (f03 + crop; unannounced; narration only: "we can also change our friction or density" at 24:00).
- **(b) Mechanism:** Density scales inertial response; bounce/friction govern ground interaction for the FLIP object.
- **(c) Estate (Torogao):** Prefer **Density 1000** as the stable early-frame reading unless a deliberate density experiment is logged; treat **718** as an observed mid-session screen state without spoken target.
- **(d) Adapt:** If Torogao needs non-water density, set it explicitly and record the pane value — do not inherit the silent 718 drift.

### T-10 — Tight FLIP volume limits (domain discipline)
**Verdict: Adopt**

- **(a) Settings:** Qualitative practice only — FLIP volume limits scaled tight around expected fluid path; "keep your volume as low as possible… the smaller this boundary, the faster simulation is" (16:40–17:39); Visualize Volume Limits then disabled (17:51–18:01). **No numeric domain extents on screen.**
- **(b) Mechanism:** Every voxel in the FLIP domain is paid for; unused volume wastes memory and time.
- **(c) Estate (Torogao):** Always shrink domain to the expected path after emitter placement; visualization off once checked.

### T-11 — Ground collision via DOP Ground Plane + Mutual affector
**Verdict: Adopt** — ground plane only; **NOT** a body-collider recipe

- **(a) Settings:** DOP Ground Plane (infinite) plus Merge/affector; collision works only after affector relationship set to **Mutual** (19:35–21:08). Collision Separation **0.2**, disabled on FLIP Object (f17/f03). **No shaped/body collider** in the video.
- **(b) Mechanism:** Mutual affector couples the FLIP object and the ground plane so particles interact with the infinite plane.
- **(c) Estate (Torogao):** Use for floor/catcher planes in foundation tests.
- **Explicit non-claim:** Do **not** distill Torogao body/mesh collider setup from this video — absent (Binding finding 4). Body collision waits for a source that shows it (likely Chapter 2 or another plan).

### T-12 — Particle Fluid Surface meshing (FLIP)
**Verdict: Adapt**

- **(a) Settings (OBSERVATION.md §4 table):**

  | When | Particle Separation | Voxel Scale | Influence Scale | Droplet Scale | Frame |
  |---|---|---|---|---|---|
  | First pass, 44:35 | `ch("../dopnet1/flipobject1/particlesep")` | 0.75 | 3 | 1 | f07 |
  | Detail pass, 47:16 | (same reference) | **0.3** | 2.933 | 1 | f08 |
  | Final check, 48:50 | **0.151** (literal; reference replaced) | 0.44 | 2.933 | 1 | f09 |

  Constants across f07–f09: Method `Average Position`; Union Compressed Fluid Surface **on**; Erosion Scale **0.8**; Output Convert To `Surface Polygon Soup`; Isovalue **0**; Adaptivity **0.005**. Stated practice (45:02–45:23): usually tweak influence scale, voxel, and droplet scale. Verdict at sep **0.151**: mesh "may not be really detailed when you zoom into it, but… from far [it] is pretty fine" (48:27–49:24); meshing "quite fast" once sim cached (48:03).
- **(b) Mechanism:** Converts FLIP particles to a polygon-soup surface; voxel/influence/droplet scales trade detail vs smoothness; referencing `particlesep` keeps mesh resolution tied to sim until deliberately frozen.
- **(c) Estate (Torogao):** Start from detail-pass **Voxel Scale 0.3**, **Influence Scale 2.933**, **Droplet Scale 1**, then freeze separation to the sim's settled value when caching final mesh.
- **(d) Adapt — what changes and why:** Final check replaced the channel reference with literal **0.151** (f09) — estate should decide reference-vs-literal explicitly so meshing does not silently desync if sim separation changes. Close-up Torogao hero shots will need tighter separation than 0.151 (creator already notes zoom detail is limited).

### T-13 — Cache pipeline: Fluid Compress before File Cache; then mesh cache; Alembic out
**Verdict: Adopt**

- **(a) Settings:** SOP order (f07–f09): DOP Import → File Cache (particles) → Particle Fluid Surface → File Cache (mesh). Particle cache pattern: **`dopOutput_SFWSetup.filecache1_v1.$F4.bgeo.sc`**. Fluid Compress **before** File Cache — "mainly to save us some space… good practice" (43:34–43:56). Folder practice: DOP output → `sim/`; File Cache → `simcache`. **Alembic ROP** writes the **meshed** fluid ("not volume") (49:31–50:48); Blender timeline Start **1**, End **250** (f10); narration "250 frames" (50:35). Cache sizes and sim wall-clock times: **UNREADABLE** (§7 item 5).
- **(b) Mechanism:** Disk-cache particles so parameter changes do not force full upstream recompute; compress to shrink storage; mesh from cached particles; export mesh Alembic for Blender.
- **(c) Estate (Torogao):** Standard Houdini→Blender surface handoff for Torogao FLIP: `.bgeo.sc` particle/mesh caches + Alembic mesh ROP; frame-range contract explicit (lesson used **250**).
- **DOCUMENTATION contrast (not video):** File Cache default type `.bgeo.sc` — SideFX Houdini 22.0 filecache.html (distill-prep Target 3). Alembic: do not put `$F` in Alembic archive filename (alembic.html) — lesson used `$F4` on the **File Cache** `.bgeo.sc` pattern, which is a different node/format.

### T-14 — Naming / Convert / Null conventions for Blender↔Houdini round trip
**Verdict: Adopt**

- **(a) Settings / practice:** Blender objects named **before** export: `FlipSourceGeo`, `GroundPlaneGeo`, `VellumSourceGeo` (02:19–03:09). Incoming Alembic loaded as Houdini geometry (**not** Alembic Delay Load primitives), then **Convert** node (07:15–08:12). Separation in Houdini **by name** via Blast (08:54–09:52). Null appended after each separated object (`FLIP_SOURCE_GEO` etc.) because nulls sort to top of reference lists (10:23–12:05). Project folders named from Houdini's perspective ("Blender Import"); file names end in digits (`001`) for iteration (03:11–04:47). **Import fixes: none** — no scale fix, no orientation fix discussed; mesh lands in same Blender scene (§5). "Scale intact" remains **UNVERIFIED** numerically on the Blender side (SHOULD-BE-SEEN).
- **(b) Mechanism:** Stable names survive Alembic unify/split; Convert ensures editable Houdini geo; Nulls make path picks reliable.
- **(c) Estate (Torogao):** Mandatory naming contract for Torogao assets before any FLIP round trip; keep digit-suffix iteration scheme.
- **Scale flag:** Round-trip "just worked" is not a measured scale proof (Binding finding 2 / SHOULD-BE-SEEN).

### T-15 — Shelf "FLIP Fluid from Object" / Vellum Grains one-click
**Verdict: Adapt**

- **(a) Settings:** Particle Fluids → **FLIP Fluid from Object** builds import → fluid compress → file cache → surfacing → surface cache → auto render → particle preview (50:56–52:22; recap 01:06:25–01:07:27). Vellum Grains has equivalent one-click. Creator teaches **manual route first** because shelf hides it.
- **(b) Mechanism:** Shelf macro wires the standard chain; identical end state to manual if defaults accepted.
- **(c) Estate (Torogao):** Allow shelf for speed after operators understand the manual chain (T-01–T-14).
- **(d) Adapt:** Estate training path = manual first, shelf second; never ship a Torogao preset that only exists as an opaque shelf click without the parameter sheet.

### T-16 — Vellum grains as gel / pseudo-pressure fluid (not splashes)
**Verdict: Adapt (gels) / Reject (splashes)**

- **(a) Settings:**
  - `vellumconstraints_grain1` creation (56:00, f14): Method `Sphere Packing`; Type `Fluid`; **Particle Size 0.1**; Isovalue **0**; Min Spheres **1**; **Point Count 10000**; Overlapping **off** (disabled 55:49). Grains are sphere primitives, not points (55:25–55:49).
  - Physical Attributes (58:35, f11): Mass `Set Uniform` **0.1**; Phase **1**; Viscosity, Surface Tension, Attraction Weight, Repulsion Weight all toggle-**off** with greyed value **1** at that moment; Define Pieces `From Connectivity`; Display as Spheres on; Add Sprite Material on.
  - `vellumsolver1` Fluids (59:18, f12): Kernel Radius Scale **4** · **Viscosity 0.5** · SDF Collision Viscosity **0** · Viscosity Solver `Implicit` · Viscosity Tolerance **0.001** · Max Viscosity Iterations **500** · **Surface Tension 0.001**.
  - After tuning (60:35, f15): **Viscosity 3.95**, **Surface Tension 0.13** — raised until particles just stick; more surface tension "makes it explode" (59:41–60:03).
  - Verdict (58:49, 01:03:14–01:03:44): grains need *less* surface tension than FLIP to hold together; much faster (no pressure/air solve); hard to control; **not for splashes** — suited to very viscous, gel-like fluids and pseudo-pressure uses.
  - Vellum "increase friction" speech (60:47): **UNREADABLE** on screen (§7 item 4 / §6 disagreement 4).
- **(b) Mechanism:** Sphere-packed Vellum fluid constraints approximate a viscous continuum without FLIP pressure solve; surface tension/viscosity on the Vellum solver control stickiness vs explosion.
- **(c) Estate (Torogao):** **Adopt/Adapt** for thick gel / slow ooze looks; **Reject** as a splash / strand / clear-line substitute for FLIP (creator's negative verdict).
- **(d) Adapt — what changes and why:** Start from tuned **Viscosity 3.95 / Surface Tension 0.13** (f15), not creation defaults; keep Overlapping off; re-tune per emitter — do not copy FLIP's spoken surface tension **10** onto Vellum (creator: grains need *less*).

### T-17 — Vellum grain meshing via Particle Fluid Surface at ~½ particle size
**Verdict: Reject (for hero mesh) / Adapt (preview only)**

- **(a) Settings:** Same Particle Fluid Surface node "performs visibly worse on grains"; fix: set particle separation to **about half the grain particle size** (particle size **0.1** → ≈**0.05**) so grains merge — cost: "a lot of jittering"; result stays jittery with "alien activity" artefacts even after Fluid Compress + File Cache bake (01:01:19–01:03:44). Exact pane value for the half-size setting not framed as a settled digit beyond the "about half" instruction.
- **(b) Mechanism:** Oversampling the surface kernel relative to grain size merges spheres into one mesh but amplifies positional noise.
- **(c) Estate (Torogao):** Do not use as final Torogao beauty mesh for grain sims.
- **(d) Adapt:** Preview-only or far plates; for hero gel mesh prefer a different meshing path (not shown in this video — do not invent one here).

### T-18 — Vellum Object Allow Caching + opinputpath display wiring (failure recovery)
**Verdict: Adopt**

- **(a) Settings:** Initial Vellum failure: cache errors + duplicated object (56:41–57:27). Fix: re-save/re-cache; ensure **Allow Caching** on for Vellum Object; display geometry via volume object inputs (`opinputpath` 0 = geometry, 1 = constraints).
- **(b) Mechanism:** Caching flag and correct input paths prevent stale/duplicate Vellum displays.
- **(c) Estate (Torogao):** Checklist item whenever a Vellum grain setup misbehaves after first create.

### T-19 — Treating this video as an applied Torogao / anatomical fluid recipe
**Verdict: Reject**

- **(a) Evidence:** Chapter 1 only; applied forces / directing fluid / NSFW systems deferred to Chapter 2 (00:37–00:58; close 01:07:27). Demo scene = two icospheres + plane (01:02). No body collider (Binding finding 4).
- **(b) Mechanism:** N/A — wrong scope.
- **(c) Estate (Torogao):** Use this sheet for **FLIP/Vellum foundations** only. Applied Torogao look-dev waits for Chapter 2 (or another plan) observation.
- **(d) N/A.**

### T-20 — Claiming centimetre-scale / true small-scale modelling from this lesson
**Verdict: Reject**

- **(a) Evidence:** 2 m sphere, 6 m drop height, unscaled metre scene (f10; §3). Small-scale *behaviour* faked with surface tension + viscosity (§3; SHOULD-BE-SEEN CONTRADICTED).
- **(b) Mechanism:** Physics parameters impersonate capillary-scale look at metre size.
- **(c) Estate (Torogao):** If Torogao needs real unit discipline, that decision is **UNANSWERED by this source** — set estate units explicitly and re-tune T-06/T-07/T-08; do not cite this video as proof of centimetre modelling.
- **(d) N/A.**

---

## Counts

| Verdict | Count | IDs |
|---|---|---|
| **Adopt** | 8 | T-01, T-03, T-04, T-10, T-11, T-13, T-14, T-18 |
| **Adapt** | 8 | T-02, T-06, T-07, T-08, T-09, T-12, T-15, T-16 |
| **Reject** | 4 | T-05, T-17, T-19, T-20 |

T-16 is counted under **Adapt** (gels / pseudo-pressure) and carries an embedded **Reject-for-splashes** clause (creator verdict). T-11 is Adopt for infinite ground + Mutual affector only.

**Headline for Pax:** **Adopt 8 · Adapt 8 · Reject 4** (plus T-16 splash-reject clause; T-17 Reject for hero grain mesh).

---

## UNVERIFIED / UNREADABLE register (explicit)

Carried from OBSERVATION.md §7 and SHOULD-BE-SEEN; none filled by inference this pass:

1. **UNREADABLE** — FLIP Solver Surface Tension field on screen (spoken "10" only).
2. **UNREADABLE** — FLIP Solver Substeps (never opened / mentioned).
3. **UNREADABLE** — Exact frame-driven expression for time-varying scattering (~38:14–38:24).
4. **UNREADABLE** — Vellum friction value(s) (speech vs no framed field).
5. **UNREADABLE** — Cache sizes and sim wall-clock times.
6. **UNVERIFIED** — Alembic handoff "scale intact" on Blender side (no numeric check in video).
7. **UNANSWERED** — Scene unit / true small-scale modelling question (§3).
8. **UNREADABLE as settled pane digits** — Jitter Scale after the as-created **0.1** increase; Vellum meshing separation beyond "about half" of **0.1** (≈0.05 instruction).
9. **Not in video** — Shaped/body collider technique; Chapter 2 force/aim techniques; applied anatomical setup.

**DOCUMENTATION-only (not video; for contrast, from distill-prep citations):** Houdini 22.0 FLIP numeric UI defaults for several knobs remain UNVERIFIED in docs HTML; Velocity Transfer default FLIP (Splashy) VERIFIED; Enable Viscosity off by default VERIFIED behavioral; Density 1000 VERIFIED on SOP Container docs; Spatial/Mass Scale default 1 VERIFIED — see `~/grok-reports/night-school-plan07-distill-prep.md`. Video tools were Houdini **19.5.435**, not 22.0.

---

## QUESTIONS FOR PAX

1. May Torogao lock a FLIP Surface Tension preset using the **spoken "10"**, or must Pass 3 wait for a live pane capture on estate Houdini?
2. Estate Houdini build vs observation **19.5.435** — confirm pin before treating Source Smoke workaround (T-02) as still required.
3. For unit discipline (T-20 / Binding finding 2): should Torogao standardize on metre scenes with faked capillary look, or move to real centimetre modelling with Spatial Scale / Hip File Options retune (not taught here)?
4. Is Chapter 2 (or another plan) scheduled as the source for **body collision** and directed emission, so Pass 3 does not invent those techniques?
5. Vellum grain hero meshing (T-17): accept "preview only," or commission a separate meshing source?
6. Blender estate pin vs observation **3.3.9** / distill-prep manual **5.2 LTS** — which governs import-side checks in Pass 3?

---

## Verification note (numeric re-fetch)

Every numeric claim in T-01–T-18 was matched word-for-word against OBSERVATION.md before this file was written (tables in §2 and §4; Physical tab values; Vellum f14/f11/f12/f15; Blender f10 dimensions/location/End 250; cache pattern string). No solver numbers introduced from memory, from Houdini docs-as-video, or from the empty distill-prep evidence tables.

---

## POST-TASK PROCESS CHECK

- Processes/servers started for this task: **none** (ssh/scp, local python/file write only).
- Source video `plan07-source-1080p.mp4`: **not opened, not played, not transcribed**.
- No installs, commits, pushes, service changes, or `~/.config/nvim` edits.
- No unknown binaries; no `--help` on estate tools.
- New file only: `~/grok-reports/night-school-plan07-distillation.md` (+ status backup/update per standing orders).


---

## Gate record addendum (coordinator, 2026-11-06)

This sheet is the Pass 2 deliverable of record for Plan 07. The raw
Azoth draft is preserved beside it as `PASS2-AZOTH-DRAFT.md`.
Pass 3 proceeds from THIS sheet alone (video closed), per protocol.

---

## Pass 3 Addendum (2026-11-06, rebuild agent — route findings; gated content above unchanged)

The Pass 3 clean-room rebuild (Blender 5.2.3 LTS Mantaflow route, per the
coordinator ruling in the gate header) consumed every value it needed from
this sheet — no Houdini-side value was missing. The gaps were all
route-side; they are recorded here so the next route rebuild does not
re-pay them:

1. **Blender 5.2 viscosity API:** set `domain_settings.viscosity_value`
   only. `viscosity_base` / `viscosity_exponent` are inert legacy props —
   a full sensitivity strip was silently flattened to the default 0.05
   before this was caught by mesh-cache hash comparison + readback
   (PASS3-REBUILD.md §7.1).
2. **Blender 5.2 operator drift:** `fluid.bake_all()` takes no `use_all`
   kwarg; bake operators act on the active object's fluid modifier;
   `wm.alembic_export` has no `visible_objects_only` kwarg (§7.2).
3. **Liquid GEOMETRY flow init** produced empty caches in three
   configurations on 5.2.3; the T-01 single-shot was rebuilt via a
   1-frame INFLOW window instead (§7.3, claim C-05).
4. **Route result on T-08's spoken surface tension "10":** used in-route
   as the starting value (per gate ruling Q1); the viscous class
   reproduced at that value (claim C-01), and the value remains
   spoken-only as a *Houdini* preset — the in-route test does not upgrade
   its source status.
5. **New measured deviation not in this sheet:** at the sheet's demo
   scale, 90 frames of continuous emission overfills a 4.6 m-wide domain
   (pool reaches lateral borders by ~f120). Preset consumers should
   widen the domain or shorten emission for free-pool work
   (PASS3-REBUILD.md §6).
