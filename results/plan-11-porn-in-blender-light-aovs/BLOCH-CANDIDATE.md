# Bloch candidate — Night School Plan 11 (Light Groups / "Light AOVs")

- **origin_lane:** ntranch
- **content_label:** nsfw
- **Evidence pointers:** `runs/plan-11/OBSERVATION.md`,
  `TECHNIQUE.md`, `PASS3-REBUILD.md`, `PASS4-APPLICATION.md`,
  `rebuild/relight-probe-measurements.json` (probe numbers),
  `rebuild/relight-measurements.json` (full-EXR numbers),
  primo media pin `~/.local/share/pax/night-school/plan-11/`
  (MANIFEST.md: capture 0b4592fa…).

## Candidate lessons

### L1 — A light-group split is a lamp audit: a summed beauty can hide a dead lamp forever
In the Plan 02 NS02 template, the Rim_Spot (1000 W, 55°)
stands at (1.6, 1.5, 2.1) — behind the backdrop cyclorama
wall (y = +1.3) it is meant to rim against — and is fully
occluded by that mesh: its light-group pass is identically
zero (mean 0, max 0, 0/518,400 nonzero pixels, both
variants). Every summed render looked fine, and a Pass 4
review credited "rim-side edge light" that was actually
the backdrop's emission gradient. **Lesson:** any estate
lighting template should ship with a per-group (or
per-lamp solo) energy census — a lamp whose pass is zero
is a defect no beauty render can reveal. Proposed gate:
nonzero-energy assertion per named light role in template
fingerprint runs.
- Artefact: `runs/plan-11/rebuild/passes-probe-nswfw.exr`
  (+ `-sfw`), measurement in PASS3-REBUILD.md §"The dead rim".

### L2 — The relight identity is Σ groups + only the energy that belongs to no group
Beauty = Σ Combined_<group> holds exactly (probe mean
|diff| 1.47e-07) **when every emissive/volumetric source
is grouped**. The source video's scene needs + Emission
+ Volume Direct because its backdrop and fog are
ungrouped; the estate variant groups its backdrop, and
adding Emission then *double-counts* (measured overshoot
mean 0.750 vs 0.704). **Lesson:** state the remainder
rule with the grouping rule, never as a fixed pass list:
remainder = energy whose source is in no group. A fixed
"always add Emission" recipe silently corrupts grouped
scenes.
- Artefact: `runs/plan-11/rebuild/relight.py` (base =
  group sum; Emission as diagnostic), measurements in
  `relight-probe-measurements.json`.

### L3 — Blender 5.2 compositor/API drift is a probe-first surface (5.0 → 5.2)
Four breaking changes were found by census probes, not
documentation: `scene.node_tree` → `compositing_node_group`;
Composite → NodeGroupOutput and MixRGB → ShaderNodeMixRGB;
render-format `OPEN_EXR_MULTILAYER` removed (multilayer
EXR now written by the compositor File Output node via
`file_output_items.new('RGBA', …)`, as a **multi-part**
EXR); ViewLayer denoising-data passes no longer exposed
(5.0.1's guided comp Denoise has no build-time equivalent).
**Lesson:** on this estate's Blender, any compositor
script from an older tutorial must be probed node-type by
node-type before it is trusted; budget the census as part
of the rebuild, and record drift at the claim.
- Artefact: probe scripts `/tmp/ns11-census*.py` on primo
  (ephemeral) + the applied findings in
  `runs/plan-11/rebuild/build_aov_variant.py` comments and
  PASS3-REBUILD.md §"Version drift".

## Friction log (D-1064 — silent workarounds logged even in successful runs)

| # | Friction | Workaround applied | Cost |
|---|---|---|---|
| F1 | Sandbox background-exec completion handoff interleaved into a primo-ssh result | Ignored per D-567; all state read from files/detach `.done` | ~0 (rule exists) |
| F2 | `scene.node_tree` AttributeError on 5.2.3 | Census probe (ns11-census2) → `compositing_node_group` | 1 probe run |
| F3 | `CompositorNodeComposite` / `CompositorNodeMixRGB` undefined | Census probe (ns11-census3) → NodeGroupOutput / ShaderNodeMixRGB | 1 probe run |
| F4 | Hand-made compositor group renders black (no interface output socket) | Interface-socket assertion added to exr_to_png.py | 1 failed conversion round (4 black PNGs, md5-identical — the identical-md5 was the tell) |
| F5 | Render-format enum rejects OPEN_EXR_MULTILAYER | Censuses 5–10 located the File Output node route + items API | 6 probe runs, ~15 min |
| F6 | EXR read as single-part showed only Combined (4 channels in a 51.7 MB file — the size was the tell) | Multi-part read via `OpenEXR.File` parts | 3 probe snippets |
| F7 | OpenEXR 3.5 write API: `OpenEXR.Channel(PixelType)` invalid | Switched to Imath.Channel/Imath.PixelType | 1 failed relight run |
| F8 | Relative render filepath fails to save from a blend-less Blender | Absolute paths everywhere in the conversion lane | 1 failed conversion round |
| F9 | Full-render detach launched ~2 s before its `-P` script finished uploading (operator error by this agent) | Verified from the detach log that Blender read the blend and the script landed before exec; no relaunch needed — logged because it was luck, not discipline | 0, flagged |
| F10 | Primo parallel-wave contention (load 19–28; four whisper jobs + tenants) | Niced every heavy stage; probe-first ordering so the full render was the only long pole; SFW full render honestly not run | Wall-clock stretch on transcript + render |
| F11 | The comp-beauty File Output (PNG) node wrote no file during the probe render while its EXR sibling wrote correctly | Not chased: the scene render output itself is the comp beauty. Recorded as an open minor — the passes node (the contract) is proven | 0 |
| F12 | Artifact pull-down: a background-exec handoff reported the tar transfer "failed, exit 1" while the tar was in fact still streaming (verified alive on disk), and a later handoff reported an rsync "completed, exit 0" while its temp file was still growing; running the tar and rsync concurrently into one directory left the 204 MB EXR short (147.9 MB) | Killed the duplicate transfer, deleted partials, re-pulled the EXR as a single verified rsync; all other files size-verified against primo | ~20 min of transfer churn; lesson: one transfer at a time, completion read from file size + hash only (D-567 applied to file transfer, not just job control) |

## Per-edit attribution (rebuild changes vs the Plan 02 template copy)

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| Scene lights | Light groups added (8) + per-object assignment | RL gains Combined_<group> ×8; beauty identity holds at 1.47e-07 | works as the sheet claims |
| Backdrop object | Assigned to its own group `Backdrop` (his scene: ungrouped) | Backdrop energy (5.5% share) becomes gainable; Emission leaves the required sum | adapt — improvement, measured |
| Renderer denoise | ON (Plan 02) → OFF (variant) | Passes carry raw sampler output; sum still matches Combined exactly; comp tree owns denoise | works (sheet C-11-4) |
| Render output | PNG still → multilayer EXR (File Output node) + PNG comp render | 10-part EXR; passes persist beyond the session (his workflow's missing contract) | works |
| Compositor | None (Plan 02) → gain/tint per group → Add chain → Denoise | Unmodified tree reproduces the comp beauty; gains are the relight controls | works |
| Rim_Spot | **unchanged** (variant copies, never repairs) | Its group pass measures identically zero | **confounded** — the relight evidence cannot separate "technique fine, lamp dead" from any rim-specific technique claim; the rim branch of the grammar is untested by this input and is recorded as such |
| Exposure / view settings | unchanged (−1.8, AgX default) | Relight PNGs judge in the template's own pipeline | works |
