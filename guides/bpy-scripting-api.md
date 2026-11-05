# bpy scripting API — the Ranch's verified surface

> Daddy Style reference: the Ranch's verified `bpy` surface for
> Blender, adapted for adult game production and published as part of
> Night School, the Ranch's public study programme.
> Companion to `DADDY_STYLE_BLENDER.md` (alongside this file).

Version basis: **Blender 5.2.3 LTS** (both Ranch workstation builds; embedded Python
3.14.8 Arch / 3.13.13 official). Evidence marks: **R** = verified by run
on the Ranch workstation, 2026-11-02 (this leg). **S** = static read of an installed
file, 2026-11-02 (this leg, or Leg 0's reads in
the Ranch's facial-rigging notes/`VERIFY-facial.md`, cited by path). **A** = agent-worker
draft claim, not re-verified. **U** = UNVERIFIED.

This file covers only the surface the Ranch's routes actually use:
census, conversion, rendering, rigging gates. The full API is the
installed Python tree at `/usr/share/blender/5.2/scripts/` plus the
binary itself — introspect, do not guess:

```python
names = [op for mod in dir(bpy.ops) for op in dir(getattr(bpy.ops, mod))]
```

## Add-on enabling — the route that works (**R**)

`--addons rigify` fails on both builds (`KeyError: key "rigify" not
found`). The working headless route is inside the script:

```python
import addon_utils
addon_utils.enable("rigify", default_set=True, persistent=False)
ok, loaded = addon_utils.check("rigify") # (True, True) after enable, R
```

On the official build, generation then succeeds end to end:
`bpy.ops.object.armature_human_metarig_add` (159-bone human metarig),
`bpy.ops.object.mode_set(mode='POSE')`,
`bpy.ops.pose.rigify_generate` → rig named `rig`, **706 bones, 160
`DEF-` deform bones** (**R**). On the Arch build the same script
segfaults (139) during generation (**R**). The metarig operator is
`bpy.ops.object.armature_human_metarig_add`; there is no
`bpy.ops.armature.metarig_add` in 5.2 (**R**, operator census).

## Census surface (**R**)

Everything the connector's census does is plain data access:

- `bpy.data.objects`, `bpy.data.meshes`, `bpy.data.armatures`,
 `bpy.data.materials`, `bpy.data.images` — iterate and count; sort by
 `.name` for deterministic output.
- `ob.data.shape_keys.key_blocks` — shape-key census; per key:
 `name`, `slider_min`, `slider_max`, `vertex_group`, `relative_key`,
 and peak delta from `kb.data[i].co` against the relative key (**R**,
 this leg's glTF round trip and Leg 0 Probe 1: 28 morph targets in a
 GLB arrived as 28 shape keys).
- `ob.data.bones` / `arm.pose.bones` — bone counts; deform set =
 names starting `DEF-` on a Rigify rig (**R**).
- Actions and frame ranges: `bpy.data.actions` (**S**, connector doc
 notes slotted-action curve counts can read −1 on 5.2; frame ranges
 read correctly).

## Import / export operators (**R**, introspected on the official build)

| Operator | Route | Note |
| -------- | ----- | ---- |
| `bpy.ops.export_scene.fbx` | FBX export | The add-on exporter; the Ranch's agent workers' "legacy add-on" framing is **A** for its manual wording, the operator's existence is **R** |
| `bpy.ops.export_scene.gltf` | glTF/GLB export | Keyword form used by this leg's probe: `export_format='GLB'`, `use_selection=True` (**R**) |
| `bpy.ops.import_scene.fbx` | FBX import | Present alongside the new importer (below) |
| `bpy.ops.import_scene.gltf` | glTF/GLB import | **R** (round trip; also Leg 0 Probe 1) |
| `bpy.ops.wm.alembic_export` / `bpy.ops.wm.alembic_import` | Alembic | Existence **R**; behaviour **U** |
| `bpy.ops.wm.fbx_import` | FBX import (5.2's new importer) | Existence **R**; behaviour **U** |
| `bpy.ops.wm.obj_export` / `bpy.ops.wm.obj_import` | Wavefront OBJ | Existence **R**; behaviour **U** |
| `bpy.ops.wm.ply_export` / `bpy.ops.wm.ply_import` | PLY | Existence **R**; behaviour **U** |
| `bpy.ops.wm.stl_export` / `bpy.ops.wm.stl_import` | STL | Existence **R**; behaviour **U** |
| `bpy.ops.wm.usd_export` / `bpy.ops.wm.usd_import` | USD | Existence **R**; behaviour **U** |
| `bpy.ops.wm.save_as_mainfile` / `bpy.ops.wm.read_factory_settings` | Save / reset | **R** (save probe, census scripts) |

glTF exporter parameters relevant to faces (**S**, Leg 0 reads of
`/usr/share/blender/5.2/scripts/addons_core/io_scene_gltf2/__init__.py`):
`export_apply` (default False; its own description warns it prevents
exporting shape keys — never set it on a face export),
`export_frame_step` (default 1, range 1–120), `export_morph` (True),
`export_morph_animation` (True), `export_morph_normal` (True),
`export_morph_reset_sk_data` (True), `export_morph_tangent` (False),
`export_optimize_animation_size` (True), `export_try_sparse_sk` (True).
Full treatment: the Ranch's facial-rigging notes → "Blender — ARKit-52 channel
mapping".

## Determinism facts (**R**)

- GLB export of the probe scene (cube + one shape key) is
 **byte-identical** across two exports in one run, across runs, and
 across the two builds (one SHA-256 for all four files). Scope: this
 trivial scene, pinned builds. Larger scenes: **U**.
- `.blend` save is byte-identical across two saves **within** one build
 and **differs across builds** (86 538 vs 86 553 bytes, different
 hashes, same script and scene). Never promise cross-build `.blend`
 byte equality; compare `.blend` outputs by census, not by hash.
- Pose/rest hashes as a gate (the Ranch's agent workers' `rig_probe.py` RIG_GATE idea):
 **U** — not re-run this leg; the Arch crash makes any hash gate
 build-specific until it is.

## Gotchas that bind Ranch scripts

- **Do not hold RNA references across mutations or mode switches.**
 Re-resolve by name after any operator or mode change. The Ranch's agent workers cite the
 API docs verbatim for this (**A** as citation; the rule itself is
 standard and this leg's probes follow it). Edit bones exist only in
 Edit Mode; pose bones only in Pose Mode (**R**, probe scripts switch
 modes explicitly).
- **faulthandler first.** Every probe in this leg starts with
 `import faulthandler; faulthandler.enable`. On a segfault the crash
 file lands in `$TMPDIR` (`blender.crash.txt`); stdout buffered before
 the crash is lost, so print progress with `flush=True`.
- **Handlers** (`bpy.app.handlers`) are freed when a new file loads
 unless registered with the `@persistent` decorator (**A**, the Ranch's agent workers'
 API citation; not re-run). A multi-file gate script re-registers or
 goes without.
- **Operators use the context.** Prefer `bpy.data`/`bmesh` APIs; when an
 operator is unavoidable (import/export, Rigify), set the active
 object/selection explicitly first and check the returned set
 (`{'FINISHED'}`) (**A** as doctrine; this leg's probes set
 `view_layer.objects.active` before every operator, **R** as practice).
- **Threads.** No background threads in Ranch scripts; parallelism is
 one Blender process per job, bounded by the runner (**A** doctrine,
 adopted).
- **Timers do not run the show headless.** A timer registered with
 `first_interval=0.1` in a `-b` script did not fire during a 0.6 s
 `time.sleep` (**R**). Do not build headless logic on
 `bpy.app.timers`; behaviour under a manually pumped event loop is
 **U**.

## Modules sampled from the Ranch's agent workers' annex (**R**)

The Ranch's agent workers' `bl-annex.md` (4 787 lines) is an index of documentation pages,
not a set of tool claims; it was sampled, not absorbed. Sample check:
`import aud, blf, bmesh, bpy_extras, freestyle, gpu, idprop, mathutils`
all succeed headless on the Arch build. The annex's underlying doc
bundle (`~/.local/share/daddy-style/engine-docs/`) no longer exists on
the Ranch workstation, so its `[bl:…]` line citations cannot be re-checked — treat
every annex-derived statement as **A** until re-derived from the
installed tree.

## Shape keys and facial API

Covered once, in the Ranch's facial-rigging notes (Leg 0), and cross-referenced from
the full guide — not duplicated here: shape-key fields
(`properties_data_mesh.py` reads), the Rigify `face.skin_eye` mechanism
(`skin_eye.py` reads), blink construction, gaze. This leg adds one
datum: the shape-key census fields above round-trip through GLB
(**R**).

## UNVERIFIED in this file

- Alembic / OBJ / PLY / STL / USD operator behaviour (existence only).
- FBX export parameters and round-trip fidelity (no FBX probe ran).
- Handler persistence and operator-context doctrine (agent-worker citations,
 doc bundle lost).
- Pose-hash gate comparability, within or across builds.
