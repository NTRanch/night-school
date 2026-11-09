# Plan 07 — Pass 4 Application and Gate

- **Date:** 2026-11-06 · **Benchmark:** `rebuild/EXPECTED-VS-SEEN.md`, written
  2026-11-06 ~02:04 PST — after the Pass 3 bakes launched (02:02:38 PST) and
  **before** any main-run frame was inspected, per estate gate discipline.
- All numbers below trace to artifacts named inline (records in
  `rebuild/records/`, frames in `rebuild/frames/`).

## 1. NSFW application — preset + cache contract for Plan 06

Deliverables (in `rebuild/`, copied to the repo results dir):

- **Preset:** `preset-torogao-flip-viscous-ch1.json` — the distilled
  Mantaflow preset (domain, flow, scene, Houdini reference values, known
  limits). Parses as JSON (verified `python3 -m json.tool`). Every value
  traces to TECHNIQUE.md via the mapping table in PASS3-REBUILD.md §2, or
  to a recorded route deviation there (notably `viscosity_value` — the
  preset carries the API warning in `_viscosity_api_note`).
- **Cache contract:** `CACHE-CONTRACT.md` — two-tier estate translation of
  T-13/T-14: Mantaflow working cache per variant directory (renders/exports
  read cache; parameter change = new variant + new bake), and the Alembic
  mesh-only handoff (`ns07_<variant>_fluidmesh.abc`, digit-suffix
  iteration, source naming discipline carried verbatim). Contract evidence:
  main export 476,974,171 bytes / 120 frames, sha256
  `f8a2f8a29c26b94b00d6611962fce2e5890ec27b04a2d55d5104360aa0302604`
  (primo `~/.local/share/pax/ns07/runs/mainA2/`), reimport-verified in
  metres (PASS3 C-16).
- **Scope honesty (from the sheet, carried into the preset's
  `known_limits`):** foundations only — no body collider, no directed
  emission, no anatomical application. Those are Chapter 2 / Plan 06
  sources, and this preset does not pretend to them. Surface tension 10
  remains a spoken-only starting value that survived one in-route test,
  not a verified constant.

## 2. SFW translation — water-like re-tune

Deliverable: `preset-estate-flip-water-ch1.json` (parses as JSON, verified).
Same preset class — identical domain discipline, emitter geometry,
cutoff method, cache contract — re-tuned for water-like viscosity.

| Setting | NSFW preset (viscous class) | SFW water preset | Why |
|---|---|---|---|
| `viscosity_value` (ν) | 0.05632 m²/s | **1.0 × 10⁻⁶ m²/s** (base 1.0 / exp 6) | Water's kinematic viscosity; the sheet's whole point is that the viscous class is a deliberate deviation from water behaviour |
| `surface_tension` | 10.0 | **1.0** | Cohesion should barely bind at SFW scales (splashes, fountains, drinks break up freely); 10.0 is the fake-small-scale lever and would read as gel |
| `particle_radius` | 1.43 | **1.0** | The 1.43 was the source's tuned collision plumpness for the viscous look; water starts from the neutral solver value |
| `mesh_particle_radius` | 2.933 | **2.0** | The 2.933 influence was tuned to merge viscous strands smoothly; water surfaces start from the Mantaflow default-class radius |
| Everything else (resolution 50 / cell 0.152 m, flip_ratio 0.97, cutoffs, cache contract, naming) | — | **unchanged** | The transferable craft is the discipline (scale, domain, cache, naming), not the fluid numbers |

The SFW preset is a *starting point by construction* (the plan's own
wording): it was not separately baked in this run, and it does not claim
a gate. Its first use re-runs the Pass 3 harness with the delta applied.

## 3. Gate — expected vs seen (agent reads; Owner's eye is the verdict of record)

Benchmark items from `rebuild/EXPECTED-VS-SEEN.md`:

| # | Item | Agent read | Evidence |
|---|---|---|---|
| 1 | Coherent column, 1 island while emission on | **PASS** | Islands = 1 at f20/45/90; `frames/mainA2_frame_0045_emission-peak.png` |
| 2 | Impact + pooling, min-z ≈ 0 within one cell, no splash class | **PASS** | min-z 0.119 m ≤ cell 0.152 m from f45 on; pooling foot in f45 frame; no detached splash islands at any sampled frame |
| 3 | Cutoff → necking, droplet islands > 1, volume stops growing | **FAIL** (partial) | Volume stops growing ✓ (verts peak 17,552 @f90, decline after). Droplet separation ✗ — islands stay 1 (PASS3 C-02 REFUTED). The benchmark's droplet expectation is not met in this configuration |
| 4 | Settle by f250: 1 island, min-z ≈ 0, verts stable vs f180 | **PASS** with recorded deviation | Islands 1, min-z 0.119; verts 12,504 (f180) → 13,894 (f250) — the rise is pool spreading, and the pool is domain-filling by then (PASS3 §6 deviation). "Settled pool" yes; "free pool" no |
| 5 | Sensitivity direction: ×0.1 thinner/more breakup, ×10 thicker/less | **PASS** | f90 verts 20,050 / 17,552 / 13,618 monotone in ν; frames `sens_lo2_frame_0090…` / `sens_hi2_frame_0090…` read in the expected directions |
| 6 | Determinism: identical decoded-pixel hashes A vs B, all frames | **PASS** | 8/8 identical (PASS3 §5 table) |
| 7 | Preset artifacts exist, parse, trace to sheet/deviations | **PASS** | Both JSONs verified with `json.tool`; traceability via PASS3 §2 |
| 8 | Alembic handoff exists, non-trivial | **PASS** | 476,974,171 bytes, sha256 recorded, reimport bbox in metres |

**Gate summary (agent read): 7 PASS / 1 FAIL (item 3, droplet separation).**
Per the plan's gate, a FAIL on behaviour returns the item to Pass 2/3 with
frame evidence — the C-02 row in PASS3-REBUILD.md is that record. The
preset is **not** blocked by item 3 for Plan 06's foundation use (emission,
pooling, cache discipline all gated), but Plan 06 must not cite this run
as evidence for droplet/strand separation; that behaviour is an open
item (candidate levers: longer post-cutoff fall, smaller emitter, surface
tension re-test — none run here, none invented).

## 4. Eye items queued for the Owner (verdict of record — not agent-scored)

1. **E-1 Droplet/strand class:** does the f45/f90 column + f110 mound read
   as the video's viscous class to your eye, despite the missing detached
   droplets (C-02)?
2. **E-2 Settle read:** f250's domain-filling slab — acceptable as
   "settled" for foundation purposes, or does the preset need the
   wider-domain/shorter-emission variant before Plan 06 consumes it?
3. **E-3 Surface quality at viewing size:** mesh smoothness in the f45
   frame (the sheet's own caveat: at separation 0.151 the mesh "may not be
   really detailed when you zoom into it") — is Workbench-flat evidence
   enough, or do you want a Cycles beauty render of one frame?
4. **E-4 Sensitivity direction by eye:** sens_lo2 vs main vs sens_hi2 at
   f90 — does the thickness ordering read as strongly in frames as it
   does in the vert counts?

## 5. Lesson filing

- Bloch candidate: `BLOCH-CANDIDATE-PLAN07-PASS34.md` (this run dir),
  origin_lane=ntranch, content_label=nsfw — the viscosity-API trap and
  the decoded-pixel determinism gate are the cross-cutting lessons.
- Repo results copy: `repo/results/plan-07-cum-sims-part-1/` (technique
  sheet copy, both presets, cache contract, sensitivity + gate records).
  Local only; no pushes.
