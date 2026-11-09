# Plan 07 — Pass 3 Clean-Room Rebuild Record

- **Date:** 2026-11-06 · **Route (ruled, not relitigated):** Blender 5.2.3 LTS
  Mantaflow FLIP on primo — the estate has no Houdini (verified primo +
  sandbox 2026-11-06); the plan's own "estate's available FLIP route" fallback.
- **Only source used:** gated `TECHNIQUE.md` (this run dir). The source video
  and transcript stayed **closed** for the whole pass. Gaps found in the sheet
  are recorded in §7 with a dated addendum appended to `TECHNIQUE.md`.
- **Build host:** primo (`/usr/bin/blender`, Blender 5.2.3 LTS, hash
  e13b728c6880). All runs file-mediated via primo `~/.local/share/pax/detach/`
  (names `ns07-*`); completion read from `.done` files and run records, never
  from background handoffs. One heavy job at a time; Blender ran alone
  (standing tenants: Android emulator, ComfyUI :8191 — neither is a build/sim
  job; ≥30 GiB RAM available throughout, `free -g` probes in detach logs).

## 1. The build

Scripted, seeded, headless, re-runnable:

- Script: `rebuild/scripts/ns07_sim.py` — final sha256
  `2d74f5418cf602f4dee6cccaff1510827d3610e9c2d5359724825549b45a16aa`
  (primo copy verified identical). Render/stats: `rebuild/scripts/ns07_render.py`
  sha256 `47a565022c7a17cde5c42bd3a0c6ba6079c7b0a4daf09632c418d91fea39b099`.
  Pixel-hash: `rebuild/scripts/ns07_pixelhash.py` sha256
  `40fc0728f41174128da0eb98e04157096b46a05ee80877dc01c061b18ba410c6`.
  Alembic export: `rebuild/scripts/ns07_abc.py` sha256
  `d2f42c7604231467ed0510d90a4d965a64b26e89c348acb080c3da3f11d4b751`.
- Exact command (per variant):
  `blender -b -Y --factory-startup --python ns07_sim.py -- <variant> <outdir> <frames_end> <visc_base> <visc_exp> <surface_tension> <resolution> <cutoff> [single]`
  Main: `mainA2 <out> 250 5.632 2 10.0 50 90`.
- Scene (faithful to sheet f10): UV-sphere source `FlipSourceGeo`, Ø 2 m at
  (0, 0, 6) m; ground plane `GroundPlaneGeo` at z = 0 (effector, COLLISION);
  domain 4.6 × 4.6 × 7.6 m centred (0, 0, 3.8); 24 fps (source never states
  fps — estate assumption, recorded); seed 7 (`random.seed`; Mantaflow exposes
  no solver seed — see determinism, §5).
- Emission: INFLOW from the sphere volume, `use_inflow` keyframed on at
  frame 1, off at frame 91 (cutoff 90 — sheet T-03 analogue; the sheet gives
  no cutoff frame number, 90 is an estate choice, recorded).
- Runs of record (bake seconds from each `run_record.json`, in
  `rebuild/records/`): mainA2 **54.5 s** / 250 f · mainB2 **54.21 s** / 250 f ·
  sens_lo2 **34.72 s** / 160 f · sens_hi2 **37.04 s** / 160 f · single2
  **19.59 s** / 90 f. Superseded v1 runs (see §7 trap): mainA 89.66 s,
  mainB 80.46 s, sens_lo 41.56 s — retained as trap evidence only.

## 2. Parameter-mapping table (sheet → Mantaflow)

24 distilled settings considered: **15 mapped, 9 UNMAPPABLE-IN-ROUTE**.

| # | Sheet value ( TECHNIQUE.md ) | Mantaflow control | Deviation note |
|---|---|---|---|
| 1 | Particle Separation **0.151** (T-06) | `resolution_max` 50 → cell 7.6/50 = **0.152 m** | +0.7% coarser; closest integer resolution |
| 2 | Grid Scale (voxel scale, T-06) | same `resolution_max` | Not an independent knob in Mantaflow — merged with #1 |
| 3 | Particle Radius Scale **1.43** (last pane read, sourcing setup) | `particle_radius` 1.43 | Factor-of-cell vs factor-of-separation — near analogue, not identical definition |
| 4 | FLIP viscosity end-state **0.05632**, solver Enable Viscosity on (T-07) | `use_viscosity` on + **`viscosity_value` 0.05632** | Value-exact. **API trap:** `viscosity_base`/`viscosity_exponent` are inert legacy props in 5.2 — see §7 |
| 5 | Surface tension spoken-only **"10"** (T-08) | `surface_tension` 10.0 | Value transfer only: Mantaflow's is a dimensionless solver coefficient, not Houdini's physical strength. Tested as a starting value per coordinator ruling, not a verified preset |
| 6 | Velocity Transfer `FLIP (Splashy)` (T-07) | `simulation_method` FLIP + `flip_ratio` 0.97 | Splashy is the high-FLIP-ratio end of the same dial — analogue |
| 7 | Jitter Scale **0.1** (T-01/T-04) | `particle_randomness` 0.1 | Analogue (spawn jitter vs initial-lattice jitter) |
| 8 | Volume Source + Points from Volume from sphere (T-02) | Flow object `INFLOW` on the sphere mesh | Mantaflow has no separate points-from-volume stage; sampling is internal. Source Smoke workaround is Houdini-19.5.435-specific — moot in route |
| 9 | Activation keyframes cut stream (T-03) | `use_inflow` keyframes (on 1–90, off 91) | Direct analogue |
| 10 | DOP Ground Plane + Mutual affector (T-11) | Plane effector, type COLLISION | No affector graph exists in Mantaflow; collision is structural once the effector is in the domain |
| 11 | Meshing Influence Scale **2.933** (T-12) | `mesh_particle_radius` 2.933 | Same role (surface kernel radius, in cell units) |
| 12 | Frame range **250** (T-13) | cache/render frames 1–250 | fps unstated in source; 24 fps assumed |
| 13 | Alembic ROP, meshed fluid only (T-13) | `wm.alembic_export` of the domain's evaluated mesh | Direct analogue; see Pass 4 contract |
| 14 | Naming before export: `FlipSourceGeo`, `GroundPlaneGeo` (T-14) | Same object names in the build | Carried verbatim |
| 15 | Points-from-Volume density (T-02) | `particle_number` 2 (solver default class) | Loose analogue only |
| 16 | Meshing Voxel Scale **0.3** (T-12) | **UNMAPPABLE-IN-ROUTE** | Mantaflow mesh is generated at grid resolution; no independent mesh voxel size exists |
| 17 | Meshing Droplet Scale **1**, Erosion **0.8**, Adaptivity **0.005**, Isovalue **0**, Union Compressed (T-12) | **UNMAPPABLE-IN-ROUTE** | No equivalents in the IMPROVED mesh generator |
| 18 | Density **1000** (and silent **718**) (T-09) | **UNMAPPABLE-IN-ROUTE** | Mantaflow liquid density is not an exposed control |
| 19 | Bounce **0** / Friction **0** / Bounce Forward **1** (T-09) | **UNMAPPABLE-IN-ROUTE** as pane values | Effector friction exists under a different model; left at default and recorded, not silently mapped |
| 20 | Substeps (T-08 register: UNREADABLE) | — (estate choice: adaptive timesteps, min 1 / max 4, CFL 4.0) | Not a mapping: the source has no value to map |
| 21 | Reseeding usually-off (T-04) | **UNMAPPABLE-IN-ROUTE** | No reseeding control exists in Mantaflow |
| 22 | Frame-driven scattering/viscosity expression (T-05) | **UNMAPPABLE-IN-ROUTE** | Expression UNREADABLE in source; sheet verdict Reject |
| 23 | Collision Separation **0.2**, disabled (T-06) | not mapped | Was disabled in the source; nothing to carry |
| 24 | Vellum grain set, all values (T-16/T-17) | **UNMAPPABLE-IN-ROUTE** | Blender route has no Vellum grain solver; nothing in this build stands in for it |

Houdini-specific claims behind rows 16–24 are scored UNTESTABLE-IN-ROUTE in
§3 — never "reproduced" by assertion.

## 3. Claims test list (from OBSERVATION.md §2/§4 + SHOULD-BE-SEEN check)

Scored: **REPRODUCED 9 · REFUTED 2 · UNTESTABLE-IN-ROUTE 9** (20 claims).
Evidence files: `rebuild/records/*-render_stats.json` (mesh verts / island
count / min-z per frame), `rebuild/frames/*.png`.

| Claim | Score | Evidence |
|---|---|---|
| C-01 Viscous, coherent, droplet-forming emission class (viscosity + surface tension on a falling stream; SHOULD-BE-SEEN "Viscous, droplet-forming fluid — SEEN") | **REPRODUCED** | Main build: single coherent column frames 20–90 (islands = 1 at all 8 sampled frames), bulbous viscous pooling foot at f45 (`frames/mainA2_frame_0045_emission-peak.png`), no splash breakup. Measured difference in C-02 |
| C-02 Strands separate into detached droplets / "clear lines" after cutoff (36:12–36:27 behaviour) | **REFUTED** (in this route + configuration) | Island count = 1 at f90, f100, f110, f130 — the remnant necks and lands whole; mesh verts decline 17,552 (f90) → 16,152 (f100) → 14,556 (f110) by landing/merging, never by detachment. Plausible cause: post-cutoff fall distance is short at this scale; flagged as a configuration-sensitive result, not a solver-class verdict. Owner eye item |
| C-03 Continuous emission from a volume-sampled source, separation in lockstep (T-02) | **REPRODUCED** (route form) | Inflow emits continuously f1–90; verts grow 6,780 (f20) → 17,552 (f90). Lockstep is structural in Mantaflow (one resolution control) — deviation in table row 2 |
| C-04 Emission timing by Activation keyframes; source geometry never animated (T-03) | **REPRODUCED** | `use_inflow` keyframes only; verts peak exactly at cutoff f90 (17,552) then decline monotonically to 12,504 (f180) |
| C-05 Single-shot fill: static sphere released under gravity, no initial velocity (T-01) | **REPRODUCED** via route translation, with measured differences | `single2` (1-frame inflow window; GEOMETRY init failed — §7): a discrete blob falls, splats to a coherent puddle by f30 (`frames/single2_frame_0030_splat.png`), 1 island throughout, verts stable 4,840–5,330 f30–90. Differences: emitted volume is a partial fill (puddle ≈ ⅓ of the sphere's 4.19 m³ by frame estimate), and first ground contact precedes the free-fall time from 5 m (initial pressure-burst suspected, not proven) |
| C-06 Reseeding off + jitter breaks the grid pattern (T-04) | **UNTESTABLE-IN-ROUTE** | No reseeding control in Mantaflow (row 21); jitter analogue set (row 7) but its grid-breaking effect is not independently measurable in this build |
| C-07 Frame-driven expression ramps scatter/viscosity over time (T-05) | **UNTESTABLE-IN-ROUTE** | Expression UNREADABLE in the source; sheet verdict Reject |
| C-08 Separation = resolution; cost rises steeply as it falls (T-06 mechanism) | **UNTESTABLE-IN-ROUTE** | A Houdini-solver claim; the mapping (row 1) is recorded, no cross-solver cost curve was measured |
| C-09 Viscosity end-state 0.05632: "even a little here will be pretty viscous" at demo scale (T-07) | **REPRODUCED** | At ν = 0.05632 the stream is a thick coherent column (C-01 frames); the sensitivity strip (§4) shows the same knob at ×0.1 / ×10 brackets the behaviour in the expected directions, i.e. 0.05632 sits in the viscous regime in-route too |
| C-10 Surface Tension field = "10" produces the cohesion (T-08) | **UNTESTABLE-IN-ROUTE** | Spoken-only in the source (pane never opened); in-route ST 10.0 was used and the cohesion class reproduced (C-01), but the Houdini field value itself cannot be tested from this route |
| C-11 Substeps behaviour (register item 2) | **UNTESTABLE-IN-ROUTE** | UNREADABLE in source — no value exists to test |
| C-12 Physical-tab density/friction/bounce values (T-09) | **UNTESTABLE-IN-ROUTE** | Rows 18–19: no corresponding exposed controls |
| C-13 Ground-plane collision works — fluid lands and pools, no pass-through (T-11) | **REPRODUCED** | Mesh min-z = 0.119 m at every sampled frame from f45 to f250 (pool resting at mesh-kernel offset above the plane); Alembic reimport independently gives z-min 0.119 at f60/f120 (Pass 4) |
| C-14 Meshing detail pass (voxel 0.3 / influence 2.933 / droplet 1) gives a far-view-fine surface (T-12) | **UNTESTABLE-IN-ROUTE** | Voxel element unmappable (row 16); influence mapped (row 11). Surface quality at viewing size is an Owner eye item, not scored here |
| C-15 Cache pipeline: particles cached → mesh from cache → Alembic mesh out, 250-frame range (T-13) | **REPRODUCED** (route form) | Mantaflow working cache per variant on primo; all renders drawn from cache without re-sim; Alembic export `ns07_mainA2_fluidmesh.abc`, 476,974,171 bytes, sha256 `f8a2f8a29c26b94b00d6611962fce2e5890ec27b04a2d55d5104360aa0302604`, frames 1–120 (primo `~/.local/share/pax/ns07/runs/mainA2/`) |
| C-16 Handoff lands in Blender "with scale intact" | **REPRODUCED-IN-ROUTE** (source claim stays UNVERIFIED) | Same-scene route makes scale identity by construction; measured anyway: Alembic reimport at f60 spans z 0.119–7.088 m, x −1.617–1.750 m — metre scale, Z-up, matching the live scene |
| C-17 Vellum grains: gel/pseudo-pressure class, not for splashes (T-16) | **UNTESTABLE-IN-ROUTE** | No Vellum in the Blender route (row 24) |
| C-18 Vellum meshing at ~½ particle size merges but jitters (T-17) | **UNTESTABLE-IN-ROUTE** | As C-17 |
| C-19 The lesson is "small-scale" modelling (SHOULD-BE-SEEN) | **REFUTED** | By the source's own record (Pass 1/2 binding finding 2: 2 m sphere, metre scene, look faked with physics). The rebuild stays faithfully at metre scale; it does not launder the claim |
| C-20 Estate determinism: seeded, scripted rebuild is reproducible (Pass 3 protocol requirement) | **REPRODUCED** | §5: 8/8 decoded-pixel hashes identical across two separate Blender processes |

## 4. Sensitivity strip — viscosity (the load-bearing mappable setting)

**Why viscosity:** it is the sheet's pane-verified end-state (0.05632, T-07),
the value the creator himself re-drags live three times, and — unlike surface
tension (spoken-only) — it is exactly mappable in-route (`viscosity_value`).
It is the knob that decides whether the emission reads as the viscous class
at all. Variants: ×0.1 (ν = 0.005632), ×1 (main, ν = 0.05632), ×10
(ν = 0.5632); all else identical, 160 frames, cutoff 90.

Mesh surface verts at matched frames (`rebuild/records/sens_*-render_stats.json`
+ mainA2 record):

| Frame | ×0.1 (sens_lo2) | ×1 (mainA2) | ×10 (sens_hi2) |
|---|---|---|---|
| 45 | 15,422 | 11,678 | 11,804 |
| 90 | **20,050** | **17,552** | **13,618** |
| 130 | 14,190 | 13,162 | 13,120 |
| 160 | 13,940 | — (13,894 @250) | 12,966 |

Frame-90 mesh-file hashes are all distinct (mainA2 `191c3598…`, sens_lo2
`b6238cea…`, sens_hi2 `5e79e0b4…` — primo cache files), proving three
genuinely different sims. Behaviour read (frames in `rebuild/frames/`):
×0.1 — thinner stream, pool spreads wider and flatter with an impact crater
at f90; ×1 — coherent column, bulbous foot, moderate spread; ×10 — markedly
thicker column, minimal pool spread at f90, fluid still mostly in the
column. **Direction is monotone and matches the sheet's mechanism at both
ends.** Tolerance statement for the preset: the viscous class holds across
the full ×0.1–×10 bracket in-route, but the *look* (spread, column calibre)
moves materially within it — ν must be held near 0.056 for the sheet's
result class; a ±10× error is visible at a glance.

## 5. Determinism (decoded pixels, never PNG file hashes)

Main build run twice as separate Blender processes (mainA2, mainB2;
identical script, args, and machine). Pixel hashes computed by
`ns07_pixelhash.py` (loads each PNG in Blender, hashes the decoded RGBA
pixel array rounded to 8-bit — PNG file bytes are never hashed, per the
gate rule). Full lists: `rebuild/records/mainA2-pixelhash.txt`,
`rebuild/records/mainB2-pixelhash.txt`.

| Frame | mainA2 = mainB2 pixel sha256 |
|---|---|
| 20 | `30e25b69c7c77d012c84a23a8ef24baf7b1ed4666f2dc50f3127be673ba0a2ed` |
| 45 | `40c21edaceb4bec034d38f6970e92e45aa39cac8e84259b6c251e05aaed98f46` |
| 90 | `d03f02c69e16034736f0174e4b69d61462842fd89d6e3ee877ba45c953b3a331` |
| 100 | `0ed944f5d3b0c1ca80b65bff9c76e244ad8076396f348e29724daf3e9f1560ed` |
| 110 | `f34336dd9b27f1761d755b3dbac09d87f3780ac4966edd21897d4370b9af6bec` |
| 130 | `1721ce9bb36594ce52a76a2139e567989cd94eaf20fdda71ecb227c4bf3902ca` |
| 180 | `8246b1bf24f0190e0963373b50d641afd70180954d6c809aa6b3e5b4cc3f7dd0` |
| 250 | `544cba945849d2c8c6ce7937d00739ba942f2fcfd5ac9b6eac9b8d51a583360f` |

**Verdict: 8/8 frames pixel-identical.** Mantaflow FLIP on this build is
bit-deterministic across processes at these settings (the earlier v1 pair
also matched 6/6). Note the honest limit: determinism is proven for
*this* machine/build/settings class, not as a Mantaflow universal.

## 6. Evidence frames (viewing size, 960×540, from the final artifacts)

- Emission peak: `frames/mainA2_frame_0045_emission-peak.png` (sha256
  `2db4f96c…`) and `frames/mainA2_frame_0090_cutoff.png` (`62ad5198…`).
- Post-cutoff: `frames/mainA2_frame_0110_post-cutoff.png` (`dbae514a…`).
- Settle: `frames/mainA2_frame_0250_settle.png` (`665bb5d0…`).
- Sensitivity at f90: `frames/sens_lo2_frame_0090_visc-x0.1.png`
  (`6415df27…`), `frames/sens_hi2_frame_0090_visc-x10.png` (`0edbb103…`).
- Single-shot splat: `frames/single2_frame_0030_splat.png` (`4481843d…`).

**Recorded deviation visible in the settle frames:** the emitted volume
(90 frames of inflow) overfills the 4.6 × 4.6 m domain — by f250 the pool
fills the whole domain footprint (Alembic reimport: pool x-extent ±2.161 m
vs domain half-width 2.3 m at f120). Late-time behaviour is therefore
domain-boundary-dominated, not a free pool. The source's own domain was
likewise bounded (T-10 practice: tight limits), but the preset in Pass 4
carries this as a stated tolerance: widen the domain or shorten emission
for free-pool work. This does not change any claim score above except
C-02's configuration caveat.

## 7. Sheet gaps found in Pass 3 (video stayed closed; sheet fixed by addendum)

1. **Blender 5.2 viscosity API trap (route knowledge the sheet cannot
   contain, now addended):** the first build series (v1) set
   `viscosity_base`/`viscosity_exponent` — inert legacy props in 5.2. All
   three v1 variants silently ran at the default `viscosity_value` 0.05 and
   produced **byte-identical mesh caches** (fluid_mesh_0090 sha256
   `e2b0ef2d…` in mainA, sens_lo and sens_hi alike) while their OpenVDB data
   files differed — a trap that data-file hashes alone would have missed.
   Caught by mesh-hash comparison + property readback from the saved
   blends. The corrected series sets `viscosity_value` only; readback in
   every v2 run record (`viscosity_readback.value` = 0.05632000043988228
   for main).
2. **Blender 5.2 operator drift:** `fluid.bake_all(use_all=True)` and
   `alembic_export(visible_objects_only=…)` kwargs no longer exist; bake
   operators act on the **active** object's fluid modifier. All three bit
   the first attempts and are fixed in the shipped scripts.
3. **Liquid GEOMETRY flow init produced empty caches** in three
   configurations (surface_distance 0.0 / 1.0, sphere at z 6 / z 3):
   22-byte mesh stubs, 1,367-byte data stubs per frame. The T-01
   single-shot was therefore rebuilt via a 1-frame inflow window (C-05).
   Root cause not proven — recorded as a route finding, not a Blender
   verdict.
4. The sheet itself (Houdini content) needed **no** correction: every value
   the rebuild consumed was present. The gaps were all route-side, which is
   what the addendum to `TECHNIQUE.md` records.
