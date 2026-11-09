# ADDENDA — Plan 39 run-dir addenda (TECHNIQUE.md untouched)

Dated notes from the 2026-11-06 remainder run (bake-determinism
experiment + loop layering). These supplement TECHNIQUE.md; the
sheet itself is not edited (coordinator rule).

## A-1 (2026-11-06) — Video cloth parameters → Blender 5.2.3 RNA mapping

Verified against the 5.2.3 cloth settings RNA on primo
(`work/probe39.py`, `work/prop_probe.py`):

- "Pressure scale 10,000" = `ClothSettings.pressure_factor`
  (RNA name literally "Pressure Scale", ambient pressure in
  kPa). The companion value "Pressure" is
  `uniform_pressure_force`, "in units of Pressure Scale"; the
  source gives no separate value for it (OPEN stands).
- "Fluid density 1,000" has **no counterpart property** in the
  5.2.3 cloth settings (full property list checked). It is
  carried as an unmapped source value; the fallback variant in
  BAKE-DETERMINISM.md §4 applied the source's "lower it to 1"
  instruction to the pressure scale, the only pressure-side
  scalar the estate build exposes.
- "Gravity / force-field multiplier 0.5" = the Effector Weights
  panel at the bottom of the cloth settings:
  `settings.effector_weights.gravity = 0.5`. (Not
  `settings.gravity`, which is the gravity vector.)
- "Pin group" = `settings.vertex_group_mass`; "Quality Steps"
  = `settings.quality` (default 5 in 5.2.3; the source's OPEN
  stands, the experiment states the value it used).
- Point-cache disk files are **off by default**
  (`point_cache.use_disk_cache = False`); a bake-determinism
  experiment must enable disk cache and name the caches, or
  there are no cache files to compare.

## A-2 (2026-11-06) — Baked-cache replay discipline

From BAKE-DETERMINISM.md §6 (R-1/R-2), recorded here because it
governs any future use of the §5.3 route:

- Toggling a cloth modifier (visibility or enable) in a process
  that has a baked scene open **frees the bake** — in-process
  A/B measurements against a toggled state silently read the
  un-simulated follow (0.0 mm), and on disk the cache files are
  deleted (96 → 10 observed).
- Sanctioned measurement form: build the reference (no-cloth)
  scene separately, replay each scene in its own fresh process,
  step frames sequentially, never touch a modifier.
