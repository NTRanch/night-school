# Godot GDScript / engine API reference (headless surface)

> **Night School — Daddy Style: Godot GDScript / engine API reference.** This is the Ranch's house reference for the headless GDScript surface, adapted for adult game production — scene, animation, and blend-shape work for adult characters in visual novels and adult game builds. Part of Night School, the Ranch's public study programme.

Version basis: **Godot 4.7.2.stable** (`/usr/bin/godot`, Arch package
`godot 4.7.2-2`). Two inventories were taken on 2026-11-02:

- The **extension API dump** (`godot --headless --dump-extension-api`,
  run-verified): `extension_api.json`, 6,965,061 bytes, header
  `version_full_name = "Godot Engine v4.7.2.stable.arch_linux"`,
  **1,036 classes** (**S**: the dump read back by script).
- The **runtime class list** (`ClassDB.get_class_list()`, run-verified
  by the census probe): a `PackedStringArray` of **1,054 classes** in a
  headless project run. The 18-class difference from the dump is
  recorded, not explained (**U**: which classes account for it was not
  diffed).

Evidence legend (the **Src** column), identical across this package:
**B** = in the 2026-11-02 `--help` capture; **R** = run-verified
2026-11-02 by a bounded headless probe on a scratch copy (logs in
`scratch-godot/logs/` in the engine-daddy-guides workdir); **S** =
statically verified 2026-11-02 from an installed or generated file
(named at use); **D** = official documentation or Ranch staged source,
not run here; **U** = UNVERIFIED.

Scope: this file covers the API surface the Ranch's headless work
actually touches — tool scripts, scene/resource construction, animation
and blend shapes, skeletons, packs, and project files. It is not a
general GDScript tutorial. Language-level style (typing, contracts,
bounds) lives in the sibling `daddy-style-gdscript` skill; this file is
the engine-API companion to it.

## Animation

| Member | Notes | Src |
| ------ | ----- | --- |
| `Animation.add_track(Animation.TYPE_BLEND_SHAPE)` → track index | Track type constant's value printed as `4` by the probe | R |
| `Animation.add_track(Animation.TYPE_VALUE)` | The route that drove a blend shape in probes (below) | R |
| `Animation.blend_shape_track_interpolate(track, time)` | Returned exactly `1.0` at t = 0.25 for keys (0.0 → 0.0, 0.25 → 1.0). Pure resource evaluation: no scene tree needed | R |
| `Animation.length` | Settable; set to the last key time in probes | R |
| `Animation.track_insert_key(track, time, value)` | Keys inserted and counted (`track_get_key_count` = 2) | R |
| `Animation.track_set_path(track, NodePath)` | Blend-shape property form: `NodePath("Face:blend_shapes/eyeBlinkLeft")` — the part after `:` is **one** subname (`NodePath` subnames split on `:`, verified by a parse probe: the slash form yields subname count 1, the colon form 2, and neither is the property form the mixer wants — the property string itself contains the slash) | R |
| `AnimationLibrary.add_animation(name, anim)` | Library built in code and handed to a player | R |
| `AnimationMixer` | Base class of `AnimationPlayer`/`AnimationTree`; exists in the runtime class list | R (existence) |
| `AnimationNodeStateMachine`, `AnimationNodeBlendSpace1D/2D`, `AnimationNodeBlendTree` | Exist in the runtime class list and the API dump. Building a state machine in code and playing transitions headless was **not** probed | R (existence); U (behaviour) |
| `AnimationPlayer.add_animation_library("", lib)` | Empty-string library is the default library | R |
| `AnimationPlayer.advance(delta)` | Manual advance without waiting for frames. With a **TYPE_VALUE** track on `Face:blend_shapes/eyeBlinkLeft`, `advance(0.25)` set the blend value to exactly `1.0` | R |
| `AnimationPlayer.play(name)` | Started playback in probes | R |
| `AnimationPlayer` + `TYPE_BLEND_SHAPE` track | **Did not drive the value in any code-built probe** (three variants; the mixer reported `blend shape track points to a non-existing name: 'blend_shapes/eyeBlinkLeft'` in `animation_mixer.cpp`). Editor-authored scenes were not probed, so this is a probe finding, not an engine verdict — see the UNVERIFIED register | R (probe outcome); U (engine behaviour) |
| `AnimationTree` | Exists (runtime list + dump). Headless state-machine playback **U** | R (existence); U |

**The verified blend-shape animation routes, in preference order:**
(1) a `TYPE_VALUE` track on the dynamic property
`blend_shapes/<name>` of the `MeshInstance3D` (run-verified end to
end); (2) `Animation.blend_shape_track_interpolate` for offline
evaluation of a blend-shape track without a player (run-verified);
(3) direct `set_blend_shape_value` for tooling that computes values
itself (run-verified). A `TYPE_BLEND_SHAPE` track through
`AnimationPlayer` is the editor's canonical route and may well work in
editor-authored scenes — it is **U** until an editor-authored probe
settles it, and no pipeline may depend on it before then.

## ClassDB and Engine introspection

| Member | Notes | Src |
| ------ | ----- | --- |
| `ClassDB.class_exists(name)` | Probed for 16 class names; results in "Facial and rigging surface" and the census log | R |
| `ClassDB.class_has_method("ArrayMesh", "add_blend_shape")` | `true`; same for `MeshInstance3D.set_blend_shape_value` | R |
| `ClassDB.get_class_list()` | Returns **`PackedStringArray`** in 4.7.2 (1,054 entries headless). Assigning it to `Array[StringName]` is a runtime type error — the census probe's first version did exactly that, errored, and hung (see the exit contract in `godot-cli.md`) | R |
| `Engine.get_version_info()` | Dictionary; `["string"]` = `4.7.2-stable (arch_linux)`, plus `major`/`minor`/`patch`/`status` fields (7/2/stable probed) | R |
| `Engine.is_editor_hint()` | `false` in a headless project run | R |
| `OS.get_executable_path()` | `/usr/bin/godot` in probes | R |
| `OS.get_name()` | `Linux` | R |
| `OS.get_cmdline_user_args()` | The documented reader for args after `--`/`++` | B |

## Files, packs, and project data

| Member | Notes | Src |
| ------ | ----- | --- |
| `ConfigFile.load(path)` / `save(path)` | Save verified: two saves of one built value set were **byte-identical** (SHA-256 equal). Sections and keys are written in **insertion order**, not sorted (a `zeta` section written first stayed first). Determinism therefore comes from a deterministic authoring order, not from the format | R |
| `ConfigFile.set_value(section, key, value)` | Strings are quoted in the file, ints bare (read back from the generated file) | R; S (file) |
| `FileAccess.open(path, FileAccess.READ)` | Opened a generated `.pck` and read its header | R |
| `FileAccess.get_32()` / `get_buffer(n)` / `get_length()` / `seek(n)` | Read `GDPC` magic and the pack-format version (below) | R |
| `JSON.parse_string(text)` | Ranch-standard JSON intake; validate the resulting Variant's shape before use (per `daddy-style-gdscript`) | D |
| `PCKPacker.add_file(target, source)` | Returned `Error.OK` (0) in the pack probe | R |
| `PCKPacker.flush(verbose)` | Wrote the pack; verbose mode printed one `PCKPacker flush: …` line per file to stdout | R |
| `PCKPacker.pck_start(path)` | Returned 0. The generated file: magic bytes `GDPC`, then a little-endian u32 **pack format version = 4**, total 508 bytes for a one-file pack | R |
| `ProjectSettings.get_setting("physics/common/physics_ticks_per_second")` | `60` in probes (explicit in the scratch `project.godot`; the default is also 60 — the Ranch agent workers' probe project set nothing and its script printed the same route; see `REPORT-godot.md`) | R |
| `ProjectSettings.load_resource_pack(path)` | The runtime route to mount a `.pck` into a running project. Not probed; the standalone route (`--main-pack`) is the verified one | D |
| `ResourceLoader.load(path)` | Loaded a code-saved `.tscn` back as a `PackedScene` | R |
| `ResourceSaver.save(resource, path)` | Saved a `PackedScene` to `res://built.tscn`, returned 0. The saved text scene is **not byte-stable across runs** — see "Scenes and resources" | R |
| `ResourceUID.path_to_uid(path)` | For the code-saved scene it returned the path itself (`res://built.tscn`), i.e. no UID had been assigned to that file. Do not treat the return as always being a `uid://` string | R |

## Meshes and blend shapes (morphs)

Godot's name for the morph channel is **blend shape**. The channels
live on the mesh resource, the values live on the mesh instance, and
the names are free-form strings — there is **no built-in ARKit-52 name
set**: the strings `eyeBlinkLeft`, `eyeLookDownLeft`, `jawOpen`, and
`ARKit` occur **zero times** in the dumped `extension_api.json` (**S**).
Any ARKit-52 discipline in a Godot project is a Ranch naming
convention enforced by lint, never by the engine. This is the Godot
counterpart of the facial-rigging notes' per-engine mapping sections: where
Blender, Unity, and Unreal each ship a facial framework, Godot ships
the raw mechanism and no framework.

| Member | Notes | Src |
| ------ | ----- | --- |
| `ArrayMesh.add_blend_shape(name)` | Register names **before** adding surfaces. Names read back exactly (`get_blend_shape_name(0)` = `eyeBlinkLeft`) | R |
| `ArrayMesh.add_surface_from_arrays(prim, arrays, blend_arrays)` | `blend_arrays` must contain **one full surface-arrays array per registered blend shape**: a count mismatch errors (`Condition "p_blend_shapes.size() != blend_shapes.size()" is true`, `mesh.cpp`) and the surface is not added (`get_surface_count()` stayed 0) | R |
| `ArrayMesh.blend_shape_mode = ArrayMesh.BLEND_SHAPE_MODE_NORMALIZED` | `NORMALIZED` clamps the summed influence model; `RELATIVE` is the other mode (**D** for semantics) | R (set); D |
| `ArrayMesh.get_blend_shape_count()` | `2` for two registered names | R |
| `ArrayMesh.get_surface_count()` | `1` after one correct surface add | R |
| `MeshInstance3D.get_blend_shape_value(i)` / `set_blend_shape_value(i, v)` | Index-addressed values; `0.75` set and read back exactly | R |
| `MeshInstance3D` dynamic property `blend_shapes/<name>` | Appears in `get_property_list()`; `set("blend_shapes/eyeBlinkLeft", 0.5)` then `get_blend_shape_value(0)` = `0.5`. This is the property a `TYPE_VALUE` animation track targets | R |
| `Skeleton3D` skinning + blend shapes together | A skinned mesh carries both; combined evaluation order (skin then morph, per docs) was not probed | D; U (probe) |
| `SurfaceTool` | CPU mesh construction helper; exists in the API dump. Not probed | S (existence) |

## Nodes, scenes, and the tree

| Member | Notes | Src |
| ------ | ----- | --- |
| `MainLoop._process(delta) -> bool` | Return `true` to quit. The staged-frame probe pattern (setup on iteration 1, assert on iteration 2) ran clean and exited 0 — the reliable shape for tool scripts that need nodes inside the tree (the `_init` shape cannot resolve some things; see the full guide) | R |
| `Node._ready()` | Ran headless in the main scene; `get_tree().quit(7)` there exited 7 | R |
| `Node3D.look_at_from_position(pos, target, up)` | Executed in probes; basis checked via `Transform3D.looking_at` (below) after the out-of-tree `global_transform` read proved meaningless (it errored and returned identity) | R (with caveat) |
| `PackedScene.pack(node)` | Returned 0 for a code-built `Node2D` + `Sprite2D` tree with `owner` set on the child | R |
| `PackedScene.instantiate()` | The loaded scene instantiated with names and positions intact (`Hero` at `(12, 34)`) | R |
| `SceneTree.quit(code)` | Exit-code propagation verified for 0, 3, and 7 | R |
| `Transform3D.looking_at(target, up)` | For a transform at `(0,0,2)` looking at the origin, `basis.z` = `(0, 0, 1)` (Godot looks down −Z; the basis Z points back at the viewer). This is the gaze primitive: an eye node's forward is its −Z | R |
| Saved `.tscn` from code | Header `[gd_scene format=3]`; nodes carry a **`unique_id=<int>` that differed between two identical saves** (the only differing lines in a two-run diff). Everything else was byte-stable. A converter must strip or normalize `unique_id` before hashing — see the full guide's converter rules | R; S (file diff) |
| Script `.uid` sidecars | On first scan/import the editor pass wrote one `<script>.gd.uid` file per script containing a single `uid://…` line, plus `.godot/uid_cache.bin`. UIDs are assigned once and then stable; a fresh checkout's first import creates them, so they belong in version control once created (**D** for the VCS advice) | R (creation); S (contents) |

## Servers under `--headless`

| Member | Notes | Src |
| ------ | ----- | --- |
| `AudioServer.get_driver_name()` | `Dummy` under `--headless`. No audio device is touched; the Ranch's audio-silence rule is satisfied structurally by headless runs | R |
| `DisplayServer.get_name()` | `headless` under `--headless` | R |
| Rendering driver | `dummy` under the headless display driver (**B**: `--help` maps `headless` → `dummy`). Dummy rendering is why `--write-movie` crashes and why no visual gate may use a headless Godot render as evidence | B; R (crash) |

## Skeletons, IK, and face tracking

| Member | Notes | Src |
| ------ | ----- | --- |
| `BoneAttachment3D` | Exists (runtime list + dump): a node that follows one bone of a `Skeleton3D`. The Ranch pattern for lid/eye anchoring by construction (the Ranch's facial-rigging notes, "Eye-anchored lid"). Behaviour not probed | R (existence); D |
| `Skeleton3D.add_bone(name)` / `get_bone_count()` / `get_bone_name(i)` | Bones added in code; count and names read back | R |
| `Skeleton3D.set_bone_parent(child, parent)` / `get_bone_parent(i)` | Parent set by index and read back (`eye.L` parented to `root`, index 0) | R |
| `Skeleton3D.set_bone_pose_position(...)` | Pose manipulation API exists per docs; not probed | D |
| `SkeletonIK3D` | Exists: two-bone IK solver node. Solving behaviour headless **U** | R (existence); U |
| `SkeletonModifier3D` | Exists: the 4.x modifier-stack base class (replaces Godot 3's `SkeletonModificationStack3D` pattern in 3D). Evaluation not probed | R (existence); D |
| `SpringBoneSimulator3D` | Exists: spring-bone physics modifier (hair/cloth secondary motion). Not probed | R (existence); U |
| `XRFaceModifier3D` | Exists in the API dump: applies face-tracking weights to blend shapes (**D** for the mechanism). No XR runtime exists on the Ranch workstation, so behaviour is **U** | S (existence); U |
| `XRFaceTracker` | Exists in the API dump (the class the brief's `FaceTracker` guess names — plain `FaceTracker` does **not** exist; `ClassDB.class_exists("FaceTracker")` = `false`). Behaviour **U**: no XR runtime or face-tracking device on the Ranch workstation | S; R (absence) |
| `XRInterface` / `XRPositionalTracker` | Exist (runtime list). No XR session was or could be probed headless | R (existence); U |

## Facial and rigging surface — summary against the Ranch's facial-rigging notes

Cross-reference, not duplication. The Ranch's facial-rigging notes (Leg 0) set the
bar from Blender, Unity, and Unreal; Godot is measured against it here.

- **ARKit-52 mapping.** No engine mapping exists (zero ARKit strings in
  the API dump, **S**). The Ranch route is a name convention on
  `ArrayMesh` blend shapes (`eyeBlinkLeft`, …) plus a lint that every
  name in the Ranch's 52-channel list exists on the face mesh and no
  other does. the facial-rigging notes' mapping tables for the other engines
  are the source of the channel list.
- **Blink construction.** A blink is two blend shapes (left/right) or
  one shared shape, driven 0 → 1 → 0. Verified drive routes are the
  three in "Animation" above. The closed-hold and sampling rules are
  the facial-rigging notes' ("Sampling-safe closed hold"); Godot adds nothing
  and removes nothing.
- **Bone-based facial rigs.** `Skeleton3D` bones are code-buildable
  (verified); a lid bone parented under an eye bone is the
  "Eye-anchored lid" mechanism in bone form, and `BoneAttachment3D` is
  its node form. Neither was load-tested; both are **D**-level patterns
  on **R**-verified primitives.
- **Eye and eyelid layering.** Godot's 2D draw-order and 3D
  transparency sorting are project discipline, not engine guarantees;
  the plausibility gates (singularity, layer order, state possibility)
  from the Ranch's facial-rigging notes apply unchanged, checked on renders made with
  a real display driver — never on dummy rendering (**R**: it crashes
  even Movie Maker).
- **Gaze.** `Transform3D.looking_at` / `Node3D.look_at` aim a node's
  −Z at a target (verified basis). Iris-in-socket gaze (offsetting the
  iris inside a clip) is a 2D-project pattern from the Ranch's facial-rigging notes
  ("Gaze inside the clip"); Godot has no first-party equivalent (**U**
  as an engine feature, by absence from the dump, **S**).

## UNVERIFIED register

Alphabetical. Each item is also marked **U** at its point of use.

- `AnimationPlayer` driving a `TYPE_BLEND_SHAPE` track in an
  editor-authored scene. Code-built probes (three variants) all failed
  at the mixer's name resolution; no editor-authored scene was probed.
- `AnimationTree` / state-machine playback headless. Classes exist;
  no transition was ever played in a probe.
- `SkeletonIK3D` solving, `SpringBoneSimulator3D` simulation, and
  skinned-morph evaluation order. Existence verified; behaviour not.
- The 18-class difference between the runtime class list (1,054) and
  the extension API dump (1,036). Counted, not diffed.
- `XRFaceTracker` / `XRFaceModifier3D` behaviour. No XR runtime or
  tracking device exists on the Ranch workstation.
