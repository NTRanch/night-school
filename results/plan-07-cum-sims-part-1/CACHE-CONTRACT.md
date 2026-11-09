# Plan 07 — Cache Contract (estate route translation)

- Origin: TECHNIQUE.md T-13/T-14 (Houdini→Blender handoff), translated to the
  estate route ruled 2026-11-06: the sim is **native Blender Mantaflow**, so
  the contract has two tiers — the working cache and the handoff export.
- Consumer: Plan 06's integration rebuild, and any estate Blender fluid work.

## Tier 1 — Working cache (Mantaflow, per run)

| Contract item | Estate value |
|---|---|
| Cache root | `<run>/cache/` under the run directory (never `/tmp`) |
| Sub-caches | `data/` (FLIP particles + grids), `mesh/` (surface mesh per frame), `config/`, `particles/` |
| Frame range | Explicit in the run record (`cache_frame_start/end`); Plan 07 main = 1–250 @ 24 fps |
| Naming | Run-scoped directory per variant (`mainA`, `sens_lo`, …); no shared cache dirs between variants |
| Reuse rule | Renders and exports read the cache; a parameter change = a new variant directory + a new bake, never an in-place cache edit |
| Determinism note | Cache file bytes are NOT the gate. The gate is decoded-pixel hashes of renders drawn from the cache (Blender writes volatile PNG metadata; gzip cache headers likewise prove nothing). |

## Tier 2 — Handoff export (Alembic)

| Contract item | Estate value |
|---|---|
| Format | Alembic (`.abc`), mesh only — the surface mesh, never the particle volume (mirrors the source: "Alembic ROP writes the meshed fluid, not volume") |
| Object | `NS07_Domain` evaluated mesh (the fluid surface as displayed) |
| Naming | `ns07_<variant>_fluidmesh.abc` in the variant's run directory |
| Frame range | Stated on export; Plan 07 main evidence export = frames 1–120 |
| Scale statement | Export is in scene metres (Blender Z-up, metric). **"Scale intact" was UNVERIFIED in the source video and stays unverified as a cross-DCC claim**; within the estate route the export is same-scene, so scale is identity by construction, and the .abc bounding box is recorded in PASS3-REBUILD.md as the check that exists. |
| Iteration naming | Digit-suffix iteration per the source convention (T-14): `..._v1`, `..._v2`, never "final/new" suffixes |
| Object naming | Source naming discipline carries over unchanged: `FlipSourceGeo`, `GroundPlaneGeo` named before any export (T-14) |

## Failure modes carried from the source

- Cache invalidation on parameter change is expected behaviour (source
  42:54–43:05); the contract handles it by variant directories, above.
- Do not put a frame token (`$F`-class) in an Alembic archive filename
  (source documentation contrast in T-13) — frame range lives in the run
  record, not the filename.
- Compressible working caches (`.bgeo.sc` in the source; `.gz`/OpenVDB-class
  in Mantaflow) are a storage optimisation, never a contract surface:
  consumers read the Alembic or re-render from the working cache, they do
  not parse working-cache internals.
