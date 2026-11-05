# Daddy Style Godot — full guide

> **Night School — Daddy Style: Godot.** This is the Ranch's house style guide for Godot, adapted for adult game production — adult visual novels and adult game builds, their dialogue and scene systems, and the sprite and blend-shape work behind their characters. Part of Night School, the Ranch's public study programme.

Version basis: **Godot 4.7.2.stable**: Arch package `godot 4.7.2-2`,
binary `/usr/bin/godot` (182,015,704 bytes). The version was confirmed
by run on 2026-11-02: `--version` prints
`4.7.2.stable.arch_linux.ed1daf0bf` and exits 0, and a headless census
script printed `Engine.get_version_info()["string"]` as
`4.7.2-stable (arch_linux)`. Every section of this guide rests on that
version unless it names another source. This guide is written from
scratch: no prior Godot guide text survives in the Ranch, and none was
used.

This guide holds the full reasoning. The companion operational summary is the operational
core, and when the two disagree, this guide wins. The flag table lives
in `godot-cli.md`; the headless API surface lives in
`godot-gdscript-api.md`.

On the Ranch, Godot work means adult work: adult visual novels and
adult game builds whose dialogue trees, scene graphs, and character
presentation have to survive the same engineering discipline as any
other build. A branching explicit scene is, mechanically, a scene
like any other — nodes, resources, animation tracks, and imported
assets — and it gets no exemption from the rules below. Plain first,
then the mechanism: that is how every section here is written, and it
is how the Ranch expects adult projects to be built.

## Evidence legend

The same legend is used in every file of this package. The order below
carries meaning (strongest evidence first), so it is not alphabetical.

- **B**: present in the full `godot --help` output captured from
  `/usr/bin/godot` 4.7.2.stable on 2026-11-02 (129 lines, 95 unique
  long flags; log `help.txt` in the leg's scratch tree).
- **R**: run-verified on 2026-11-02 by a bounded headless probe on a
  scratch copy of a project, under `timeout`, with logs kept in
  `scratch-godot/logs/` in this workdir. Probe outcomes, including the
  failures, are itemized in `REPORT-godot.md`.
- **S**: statically verified on 2026-11-02 by reading an installed file,
  a generated file, or a staged Ranch source. The file is named at
  each use. Nothing was executed for an **S** claim.
- **D**: stated in official Godot documentation or in a Ranch staged
  source named at use. Not confirmed by **B**, **R**, or **S**.
- **U**: UNVERIFIED. No source settles it. A **U** claim never carries
  load in a pipeline without a probe run first.

**Execution status.** The probes behind the **R** marks were small and
bounded by design: one scratch project, a handful of SceneTree tool
scripts, one PNG and one WAV fixture, one hand-written export preset.
They settle CLI behaviour, exit codes, the import and pack routes, and
the code-level animation/blend/skeleton primitives. They do not settle
editor behaviour, GUI behaviour, runnable exports (impossible on the Ranch workstation
today — no export templates), XR, or rendering quality. Those stay
**D** or **U**, named as such.

## Agent use

Plain-language version: Godot has no remote control the Ranch trusts,
but it barely needs one — almost everything an agent must do with Godot
is a terminal command or a small GDScript program run headless:
importing a new character sprite sheet for an adult visual novel,
parse-checking the dialogue script that drives an explicit scene, or
packing a build for playtesting. Agents drive Godot the way a shell
script would, check what comes out, and never click in the editor.

### Broker and connector reality

Every item below was checked against this leg's staged sources and the
installed machine on 2026-11-02:

- **No custom Godot connector exists.** The brief's connector list
  names `custom.blender` and `custom.unity`. For Godot it records only
  the installed binary.
- **No MCP server or Ranch broker fronts Godot today.** None is
  declared in the brief, and this guide proposes none. MCP
  recommendations are a separate deliverable (a later leg).
- **The Ranch's Unreal editor broker** fronts Unreal Engine 5.8's built-in MCP server and
  nothing else. Its `gui.observe` / `gui.ground` / `gui.act_verified`
  tools have no Godot target. There is **no editor broker for Godot** — this
  section exists to say so plainly, per the leg spec.
- **The Ranch's live game-editor broker** is the Ranch's editor-broker MCP:
  Unity backend first, **Godot later** (brief, idea-register anchors).
  Until that broker's Godot backend lands and is gated, agents use the
  deterministic CLI/GDScript routes in this guide. A future Godot backend
  changes the transport, not the contracts: the same
  census classes, bounds, and verification discipline apply.
- **The editor's own LSP/DAP servers are not an agent API.** Godot's
  editor can serve GDScript LSP (`--lsp-port`) and DAP (`--dap-port`)
  (both **B**). The Ranch's editor setup already wires both for the Owner (see "Editor setup surface"). No agent session against them was run in this leg; their
  live-session behaviour is **U**.

### Capture and verification discipline

Godot has no op log, so the **run record** stands in for it. Every
agent-initiated run appends one record to the task's report. Fields,
alphabetical:

| Field | Content |
| ----- | ------- |
| `argv` | The exact argv array, one element per argument |
| `converter` | Converter name and version, when a converter ran (see "Daddy Style treatment") |
| `exit_code` | The process exit code, plus `124` from `timeout` when killed |
| `godot_version` | Parsed from this session's `--version` probe (never assumed) |
| `inputs` | Path and SHA-256 of every input file |
| `outputs` | Path, SHA-256, and shape (scene census, image dimensions) of every output |
| `project` | Absolute `--path` used |
| `sentinel` | The `OK <job>` line found on stdout, or `absent` |
| `stderr_excerpt` | The first 2 KiB of stderr |
| `timeout_s` | The deadline that applied |

A run counts as successful only when all of these hold: the exit code
is 0, the sentinel is present for script runs, no `SCRIPT ERROR` or
`ERROR:` line appears on stderr, and every promised output exists with
the promised shape. The stderr clause is load-bearing in Godot: a
runtime error in a SceneTree script's `_init()` prints `SCRIPT ERROR`
and then **hangs** rather than exiting (**R** — see the exit contract
in `godot-cli.md`), so a run can also "succeed" by being killed at its
deadline with the error sitting unread in the log. The record is what
prevents that from passing as success.

### Deterministic routes over GUI

The order of preference carries meaning:

1. A **CLI-NATIVE** flag route (`godot-cli.md`): `--import`,
   `--export-pack`, `--check-only`, the dumps.
2. A **SCRIPTABLE-HEADLESS** route: a GDScript tool script under
   `--headless --script`, using the resource/object API
   (`PackedScene`, `ResourceSaver`, `ArrayMesh`, `PCKPacker`) rather
   than editor state.
3. **GUI-ONLY** work goes to the Owner, named plainly in the hand-off
   ("this needs the Godot editor: <operation>"). It is never clicked
   through by an agent. If the Owner explicitly authorizes an agent to
   drive the GUI for a task, that authorization covers that task only,
   and the result is still verified headlessly: import the saved
   project, census its scenes, compare. Screenshots are not the
   record.

## CLI census

Plain-language version: for every kind of job, this section says
whether you can do it from the terminal with one flag, whether you
need a small script, or whether you must open the editor window —
importing the sprites, backgrounds, and voice lines an adult visual
novel ships with, building the layered character a scene presents,
or packing the build a playtester will run.

Classes:

- **CLI-NATIVE**: one or more flags do the whole job.
- **GUI-ONLY**: no terminal route exists. This is an honest negative.
- **SCRIPTABLE-HEADLESS**: needs a GDScript script run with
  `--headless --script`.

Exit-code behaviour for all classes is in `godot-cli.md` ("Exit-code
and output contract"). The headlines: parse errors exit 1; export
failures exit 1; script `quit(n)` propagates `n` exactly; runtime
errors in a SceneTree `_init()` hang until the deadline; headless
`--write-movie` crashes on this build. Bounded-work rules for all
classes are in "Daddy Style treatment → Bounds".

| Operation class | Class | Terminal route | Evidence |
| --------------- | ----- | -------------- | -------- |
| Animation authoring (curves, tracks, state machines by hand) | GUI-ONLY | None. The Animation editor panels are the authoring surface. Code construction of `Animation`/`AnimationLibrary` resources is the headless alternative (next row) | D |
| Animation construction and evaluation in code | SCRIPTABLE-HEADLESS | `--headless --script`: build `Animation` resources, add tracks/keys, evaluate with `blend_shape_track_interpolate`, or play through `AnimationPlayer.advance()` with a TYPE_VALUE track | R |
| Asset import (textures, audio, models) | CLI-NATIVE | `--headless --path <proj> --import`. Writes `<asset>.<ext>.import` sidecars and `.godot/imported/<name>-<32 hex>.<artifact>` | R (PNG → `CompressedTexture2D` `.ctex`; WAV → `AudioStreamWAV` `.sample`) |
| Blend-shape / morph authoring on a mesh | SCRIPTABLE-HEADLESS | Register names with `ArrayMesh.add_blend_shape`, supply one blend array per name to `add_surface_from_arrays`, drive values via `MeshInstance3D` | R |
| C# solution build | CLI-NATIVE | `--build-solutions` (implies `--editor`). The Ranch workstation binary is the standard build; .NET support in it is **U** (no C# project was probed) | B; U |
| Documentation dump (engine API XML) | CLI-NATIVE | `--headless --doctool <existing dir>`. A nonexistent target directory exits 1 | R (6.8 MB dump) |
| Editor session (scene editing, node placement by hand, inspector work) | GUI-ONLY | None, by definition. Everything the Ranch needs from an editing session must be re-expressible as a script or it is Owner work | — |
| Export: data pack (`.pck`/`.zip`) | CLI-NATIVE | `--export-pack <preset> <path>` with `export_presets.cfg`. Needs **no** export templates | R (exit 0; pack runs standalone via `--main-pack`) |
| Export: patch pack | CLI-NATIVE | `--export-patch <preset> <path>` + `--patches`. Behaviour **U** on the Ranch workstation | B; U |
| Export: runnable build (debug/release) | CLI-NATIVE | `--export-release` / `--export-debug <preset> <path>`. Requires installed export templates; the Ranch workstation has none, so the verified behaviour is the exit-1 template error | R (failure); U (success) |
| Extension API dump (bindings JSON) | CLI-NATIVE | `--headless --dump-extension-api` in the target cwd (6,965,061 bytes here; 1,036 classes) | R; S |
| Face tracking (XR) | GUI-ONLY | No terminal route. `XRFaceTracker` exists in the API dump but needs an XR runtime and a tracking device; none exists on the Ranch workstation | S (existence); U (behaviour) |
| GDExtension interface dump | CLI-NATIVE | `--dump-gdextension-interface` / `--dump-gdextension-interface-json` | B |
| GDScript documentation dump | CLI-NATIVE | `--doctool` with `--gdscript-docs <path>` / `--gdextension-docs` | B |
| Godot 3.x → 4.x project conversion | CLI-NATIVE [no-automation] | `--convert-3to4` rewrites a project **in place**; `--validate-conversion-3to4` reports only. Run the converter on a copy only | B; U (behaviour) |
| Headless game/scene run (smoke test) | CLI-NATIVE | `--headless --path <proj>` (main scene) or `--scene <path>`; bound it with the scene's own `quit()` or `--quit-after <n>` | R (main scene; exit 7 propagated) |
| Movie / frame-sequence capture | GUI-ONLY on this build | `--write-movie` is CLI-NATIVE in `--help` but **crashes headless** on 4.7.2 (`godot-cli.md` settles the negative). With a real display it is **U** | B; R (crash); U |
| Pack authoring (project files → `.pck`) | SCRIPTABLE-HEADLESS | `PCKPacker` in a tool script: `pck_start` / `add_file` / `flush`. Header magic `GDPC`, format version 4 | R |
| Pack inspection (`.pck` census) | SCRIPTABLE-HEADLESS | The Ranch route is the reverse-engineering tooling's `inspect_godot_pck` (see "RE alignment"); a script can read the header (`GDPC` + version) itself | R (header); S (reverse-engineering tooling route, PHASE1) |
| Performance benchmark | CLI-NATIVE | `--benchmark` / `--benchmark-file <abs path>` (JSON) | B |
| Profiling / GPU debug views | GUI-ONLY | `--profiling`, `--gpu-profile`, `--debug-collisions` etc. exist (**B**) but their output is an interactive debugging surface; no pipeline consumes it | B |
| Project creation from scratch | SCRIPTABLE-HEADLESS | Write `project.godot` (a `ConfigFile`-shaped text file) + scenes from a tool script or a text template. There is no `godot --create-project` flag in `--help` | B (absence); R (hand-written project ran) |
| Project manager | GUI-ONLY | `--project-manager` is a window. Nothing an agent needs lives there | B |
| Scene construction / census / edit | SCRIPTABLE-HEADLESS | `--headless --script`: build node trees, `PackedScene.pack`, `ResourceSaver.save`; or load with `ResourceLoader` and census children/properties | R |
| Script parse check (CI gate) | CLI-NATIVE | `--headless --path <proj> --check-only --script <script>`. Exit 0 clean, 1 on parse error | R |
| Scripted tool run (any project transform) | SCRIPTABLE-HEADLESS | `--headless --path <proj> --script res://scripts/<tool>.gd`, structured per "Daddy Style treatment → Tool-script contract" | R |
| Skeleton / IK setup | SCRIPTABLE-HEADLESS | Bones by code: `Skeleton3D.add_bone` / `set_bone_parent` (verified). IK solving (`SkeletonIK3D`) exists but is **U** headless | R (bones); U (IK) |
| UID and import-cache maintenance | CLI-NATIVE | A side effect of `--import` and of any editor pass: writes `.godot/uid_cache.bin` and per-script `.gd.uid` sidecars | R |
| Visual / screenshot verification | GUI-ONLY | Headless rendering is the **dummy** driver: it produces no image and crashes Movie Maker. Visual gates need a real display driver (**U** here) or another engine's render | B; R |

Exact flag spellings, order notes, and per-flag evidence are in
`godot-cli.md`. The verified API members behind the scriptable rows
are in `godot-gdscript-api.md`.

## Editor setup surface

Read from the live tree `~/.config/nvim/` on 2026-11-02, read-only
(**S**; file names from `ls`, ports from the files). Proposals go to
the Ranch's lane; nothing here edits the Ranch's editor setup.

- **DAP:** `lua/dap/godot.lua` — connects to the Godot editor's debug
  adapter over TCP, `DEFAULT_DAP_PORT = 6006`, matching the editor's
  `network/debug_adapter/remote_port` setting (file comment, lines
  12–23, 61).
- **Formatter:** `lua/formatters/gdformat.lua` catalogues `gdformat`.
  The binary is **not installed** on the Ranch workstation (**S**: `command -v
  gdformat` empty), so the format gate is honestly absent until the
  godot-gdscript-toolkit is installed.
- **Linter:** `lua/linters/gdlint.lua` and
  `lua/linters/gdscript-linter.lua` catalogue `gdlint`. The binary is
  likewise not installed; the lint gate is absent on the same terms.
- **LSP:** `lsp/gdscript_ls.lua` — the Godot editor's built-in
  language server, reached on port 6005 (file line 11). The Ranch
  gate that *is* available today is therefore the engine's own:
  `godot --headless --check-only --script` (**R**), which editor-driven
  work should treat as the floor, with LSP diagnostics added whenever
  an editor with the LSP port is actually running.

## Facial and rigging

This section folds in the Ranch's facial-rigging notes (Leg 0), which measured
Blender, Unity, and Unreal against the Ranch's facial-performance
defects. Godot was not a Leg 0 engine. The findings below state
Godot's own surface at the same depth and cross-reference the Leg 0
mechanisms instead of duplicating them.

This is where an adult character either reads as a person or falls
apart on screen. In a visual novel the face carries the dialogue: a
blink that never fully closes, a gaze that drifts off the player, or
a mouth shape that misses its line will be stared at for minutes at
a time, including through the explicit scenes the character was
built for. The discipline below is therefore not cosmetic polish —
it is the difference between a character who holds a scene and one
who breaks it. **Prima avatar rig v2 is not
an approved reference** (Owner correction, 2026-11-02 08:49 PST;
verdict "still wrong"); nothing here cites or uses it.

### ARKit-52 mapping

Godot ships **no facial framework and no channel-name standard**. The
strings `eyeBlinkLeft`, `eyeLookDownLeft`, `jawOpen`, and `ARKit`
occur zero times in the dumped extension API (**S**:
`extension_api.json`, 1,036 classes). Blend shapes are free-form
`StringName`s on `ArrayMesh`. Consequences:

- Any ARKit-52 discipline (the channel list in the facial-rigging notes'
  mapping tables) reaches a Godot project only as an **Ranch naming
  convention**: author the 52 names (or the project's subset) exactly,
  and lint the mesh — every expected name present, no extras — in a
  tool script (`get_blend_shape_count` / `get_blend_shape_name` are
  **R**-verified, so the lint is a verified route).
- There is no engine remapping layer to lean on (no equivalent of
  Unreal's ARKit curve names or Unity's `blendShape.<name>` clip
  paths). A name typo is a silent no-op at the value level unless the
  lint catches it — the facial-rigging notes' "name identity" discipline
  applies with no engine backstop.

### Blink construction

A blink is blend-shape weight over time: one shape per eye (or one
shared shape), 0 → 1 → 0, with a fully closed hold. Godot-verified
mechanics:

- Shapes are registered on the mesh (`add_blend_shape`, **R**) and
  valued on the instance (`set_blend_shape_value`, **R**), by index;
  the name-addressed dynamic property is `blend_shapes/<name>` (**R**).
- Driving: a TYPE_VALUE animation track on that property through
  `AnimationPlayer.advance()` reached exactly 1.0 at the keyed time
  (**R**). Offline evaluation of a blend-shape track
  (`blend_shape_track_interpolate`) also returned exactly 1.0 (**R**).
- The editor-canonical TYPE_BLEND_SHAPE track did **not** drive the
  value in code-built probes (mixer name-resolution error, three
  variants) — **U** for editor-authored scenes; see
  `godot-gdscript-api.md`.
- Timing discipline (closed hold ≥ 1 frame at target fps, overshoot,
  curved in-betweens) is construction discipline from the Ranch's facial-rigging notes
  ("Blink construction", "Sampling-safe closed hold"); Godot's
  animation curve editor is where the Owner authors it (GUI), and the
  values are checkable headless by interpolation probes like the ones
  above.

### Bone-based facial rigs

- `Skeleton3D` bones are fully code-buildable: `add_bone`,
  `set_bone_parent`, name/parent read-back all **R**. A jaw bone, eye
  bones, and lid bones are ordinary bones; nothing facial is special.
- `BoneAttachment3D` (exists, **R**) pins a node to a bone — the node
  form of the facial-rigging notes' "Eye-anchored lid": parent the lid's
  attachment under the eye bone's chain and the lid cannot detach from
  the eye without a rig edit a lint can catch.
- `SkeletonIK3D` and the `SkeletonModifier3D` stack (including
  `SpringBoneSimulator3D` for secondary motion) exist (**R**) but
  their evaluation was not probed headless (**U**). A facial rig that
  depends on them is gated on a probe before it carries load.

### Eye and eyelid mechanics

- **Layering.** Godot gives no structural guarantee about the eye
  stack (sclera, iris, lid). In 2D it is draw order / `CanvasItem`
  z-index; in 3D it is mesh and transparency discipline. That makes
  layering a *tuning* property in Godot unless the project builds the
  structural forms from the Ranch's facial-rigging notes: single-source eye,
  aperture-by-occlusion via a mask/clip, an eye-anchored lid. The
  plausibility gates (layer order, singularity, state possibility)
  apply unchanged and are checked on real renders — never on dummy
  rendering (**R**: it cannot even record a movie).
- **Lid travel.** A lid is a blend shape, a bone, or a 2D part; all
  three are driven by the same animation machinery verified above.
  Lid under-travel (defect class iii in the Ranch's facial-rigging notes) is measured
  the same way: at blink = 1, visible iris must be 0 — a render gate,
  not a numeric one.

### Gaze implementation

- The primitive is aiming: `Transform3D.looking_at` (**R**: from
  `(0,0,2)` toward the origin, `basis.z` = `(0,0,1)` — Godot nodes
  look down their −Z, so the eye node's −Z is its gaze direction).
  `Node3D.look_at` is the in-tree form (**D**).
- Two-bone eye aiming via `SkeletonIK3D` is **U** headless.
- Iris-in-socket gaze (translate the iris inside a fixed aperture, the
  2D pattern in the Ranch's facial-rigging notes) has no first-party Godot feature;
  in a 2D project it is authored as a clipped iris part — project
  discipline, **D** as a pattern, **U** as an engine feature (absence
  from the API dump, **S**).

### Morph channels (Godot name: blend shapes)

- Storage: names and target shapes on `ArrayMesh`; one blend array
  per name per surface, enforced by the engine with an error, not a
  silent drop (**R**).
- Modes: `BLEND_SHAPE_MODE_NORMALIZED` (set in probes, **R**) vs
  `RELATIVE` (semantics **D**). The mode is a mesh property; a
  converter that rebuilds a mesh must carry it explicitly.
- Values: per-instance float array addressed by index, mirrored by
  the `blend_shapes/<name>` property (**R**). Values are **not**
  clamped by `set_blend_shape_value` in any way a probe tested beyond
  0.75/1.0 (**U** for out-of-range behaviour).

## Owner use

### Plain-language opening

Godot is a game engine with a window, but underneath it is also a
command-line tool. With `--headless`, no window opens and no sound
plays: Godot reads your project, does what the flags or a small script
say, writes the result, and exits. For a Ranch adult project — say an
adult visual novel gaining a new character, a rewritten dialogue
branch, or a re-blocked scene — most of the daily churn is exactly
this kind of work. You can import assets, check
scripts for errors, build scenes, export a data pack, and run your
game as a smoke test that way. You need the window for drawing scenes
by hand, authoring animation curves, and playing the game yourself.

### Mechanism, in full depth

- **A project is a folder.** `project.godot` at its root is the
  marker; `--path <dir>` points Godot at it. The file itself is a
  text file in the same section/key shape as a `ConfigFile` save
  (**R**), so you can read and diff it like any config.
- **Headless means dummy drivers.** `--headless` selects the
  `headless` display driver and the `Dummy` audio driver (**B**, **R**).
  Nothing renders to a screen and no audio device is opened. That is
  why headless runs are safe on a workstation in use — and why they
  can never be visual evidence.
- **Scripts are programs.** A GDScript file whose class extends
  `SceneTree` (or `MainLoop`) can be run directly with `--script`.
  Its `quit(n)` becomes the process exit code, exactly (**R**: 0, 3,
  and 7 observed). The Ranch's tool scripts print an `OK <job>` line
  when they finish, because of the next point.
- **Errors do not always stop the process.** A syntax error is
  refused before anything runs (exit 1, **R**). But a *runtime* error
  inside a tool script's opening function prints `SCRIPT ERROR`,
  abandons that function — and the engine keeps running with nothing
  to do (**R**). From the terminal that looks like a hang. Every
  example below therefore runs under `timeout`, and a run that hits
  its deadline is a failed run, whatever it was doing.
- **Importing is a separate step.** Source assets (PNG, WAV) are not
  used directly; an import pass converts them into `.godot/imported/`
  artifacts and writes a small `.import` text file beside each source
  naming the conversion (**R**). If a game behaves as if an asset is
  missing, the `.import` file and one `--import` run are the first
  things to check. A zero-byte source file imports as an error, not
  an asset (a probe WAV from the Ranch's agent workers was 0 bytes; its import log shows the
  failure — see `REPORT-godot.md`).
- **Exports come in two kinds.** A *data pack* (`.pck`) is just the
  project's data, packed; it needs no extra downloads and the Ranch workstation can
  make one today (**R**). A *runnable export* (an actual game binary)
  additionally needs Godot's **export templates**, which are a
  separate download and are **not installed on the Ranch workstation** (**S**, **R**):
  the export stops with an error naming the missing template files.
  Installing them is your call, from the editor's Manage Export
  Templates dialog or the official release page.

### First commands, with the check for each

All commands are bounded and silent (headless = dummy audio). They
rest on **B/R** facts verified 2026-11-02. Read them as a worked pass
over one adult visual-novel project: version, look, import, check,
smoke-run, pack.

```bash
# 1. Which binary, which version.
command -v godot           # expect: /usr/bin/godot            (S)
godot --version            # expect: 4.7.2.stable.arch_linux…  (R)
echo $?                    # expect: 0
```

```bash
# 2. Look at a project without opening it: the marker file is text.
cat /abs/proj/project.godot          # sections like [application]
grep -n 'run/main_scene' /abs/proj/project.godot   # the entry scene
```

```bash
# 3. Import pass (converts new/changed assets; safe to re-run).
timeout 120 godot --headless --path /abs/proj --import
echo $?                              # expect: 0                 (R)
ls /abs/proj/.godot/imported/        # expect: one artifact per asset
cat /abs/proj/assets/red.png.import  # the conversion record, as text (R)
```

```bash
# 4. Parse-check one script (the CI gate; runs nothing).
timeout 30 godot --headless --path /abs/proj \
  --check-only --script res://scripts/tool.gd
echo $?                    # expect: 0; a syntax error gives 1  (R)
```

```bash
# 5. Smoke-run the game headless; the scene must quit itself,
#    or bound it with --quit-after <frames>.
timeout 60 godot --headless --path /abs/proj --quit-after 120
echo $?                    # the game's own quit code           (R: 7 in probes)
```

```bash
# 6. Export a data pack (works today) and run it back.
timeout 120 godot --headless --path /abs/proj \
  --export-pack "Linux/X11" /abs/out/game.pck
echo $?                                                # expect: 0  (R)
timeout 30 godot --headless --main-pack /abs/out/game.pck --quit-after 2
echo $?                    # the packed game runs standalone        (R)
```

```bash
# 7. What a runnable export needs (expected to fail on the Ranch workstation today).
timeout 120 godot --headless --path /abs/proj \
  --export-release "Linux/X11" /abs/out/game.x86_64
# expect: exit 1, stderr names …/export_templates/4.7.2.stable/
# linux_debug.x86_64 and linux_release.x86_64 as not found        (R)
```

When a check fails, stop. Read stderr first (that is where `SCRIPT
ERROR` and export errors live), then check the deadline (a 124 is a
hang, most often a script error that never reached its `quit()`),
then check the evidence legend for whether the route was ever
verified on this version.

## RE alignment

Plain-language version: when the Ranch studies other people's Godot
games — most of them adult games, whose scene graphs, schedules, and
layered-character systems are the Ranch's study material — it only
looks, and never runs them. Godot games are unusually
easy to look at: their data ships in a `.pck` file whose contents a
census tool can list and verify without executing a line of the game.
That census is measurement for a study. Nothing studied becomes ours.

### Graphics-enhancement pass

The brief binds this guide to state the graphics-enhancement
pass convention wherever asset pipelines are described. **The text of
that convention is not among this leg's staged sources** (a search of the whole
engine-daddy-guides workdir finds it only as a mention in the brief
and the Aseprite leg's records). This guide therefore records the
obligation and does not state the convention's content, which is
**U**. The asset pipelines here that must carry it once the Ranch supplies
the ruling text: the converter set in "Daddy Style treatment →
Converters" and the sprite-to-3D factory seam below. Inventing a convention would
violate the "never filled in from memory or inference" standard.

### Static RE only

Game-RE programme law is that nothing is executed. For Godot:

- **The pack is data.** A `.pck` begins with the magic `GDPC` and a
  u32 pack-format version (4 on this build, **R** — the same version
  the Phase 1 pilot's directory parse handled, **S**: PHASE1-REPORT).
  Listing, extracting, hashing, and parsing its directory are static
  operations on bytes. Running the pack (`--main-pack`) is execution:
  it is a route for **Ranch** projects only, never for a studied
  game's pack.
- **Extracted assets are untrusted input.** Work on copies taken out
  of `~/.local/share/ntranch-game-re/<slug>/`, never the originals.
  A studied game's GDScript ships in exports as compiled `.gdc`
  (observed in this leg's own export pack, **R**) and as zstd-framed
  token streams in the pilot (**S**: PHASE1-REPORT). Token/string
  extraction is static reading; loading a studied `.gdc` or `.tscn`
  into a running Godot is not — a scene can carry scripts, and
  scripts are code.
- **Provenance at birth.** Any record derived from a study carries
  the pilot slug, its STUDY.md section, `content_label: nsfw`, and
  origin, per the unified map §3 intake shape and lane law.
  Attribution names the studio only.

### The Godot pilot: MODIFICATION_APP

From the staged sources (**S**: the Phase 1 pilot report (Ranch-internal) and
the Torogao unified engine map (Ranch-internal), read in full for this leg):

- **Route.** The reverse-engineering tooling's `inspect_godot_pck` was the primary tool:
  exhaustive extraction, **18,828 / 18,828 entries MD5-verified**,
  plus direct tooling (PCK directory parse, zstd `.gdc` token
  strings, JSON tables). Completeness: **full, importer-grade**.
- **Ruling.** **build the Godot importer.** The unified map's
  §7 Q1 records the ruling and its oracle: importer output on
  MODIFICATION_APP must reproduce the §G5 paper map — clock,
  schedules, the 39-node path graph, and the save shape — as Torogao
  records.
- **The build shape.** An imported path-graph project: StoryFlow's
  39 scene nodes with Path/Time/ReqFlag/Minigame fields, a 4-slot
  clock, a TP economy, and a visual-state delta table driving the
  layered doll.
- **The one disagreement.** The §G5 paper map claimed
  "attempt-count conditions"; the pilot did **not** find them in
  this build (6 of 7 claims agreed exactly). Recorded here because a
  guide that repeats only the agreements would misstate the
  evidence.
- **Tooling gap named by the pilot.** The reverse-engineering tooling's PCK inspection is
  proven; the script layer needs the **`.gdc` token/string
  extractor** (zstd-framed GDScript bytecode; the hand route was
  proven in the pilot) as its complement (PHASE1 cross-pilot table,
  torogao-cli/MCP group).

### Torogao: what is adopted, adapted, improved

Under the unification rule (map §1), Torogao is the singular build
engine. Godot is a study target and a desktop tool only. Its
scene format, its GDScript runtime, and its pack format **never**
become a Torogao format, runtime, or export target. What crosses is
capability, through the map's §3 intake shape (capability, measured
behaviour, classification, one layer, anchor or missing primitive,
parity gate, a measurable "better", provenance).

| Capability (from the pilot) | Measured behaviour (PHASE1 / map) | Torogao layer | Concrete "better" claim |
| --------------------------- | --------------------------------- | ------------- | ----------------------- |
| Path-graph scene flow as data | StoryFlow.json ships the graph as data: 39 nodes with Path/Time/ReqFlag/Minigame fields | torogao-cli + MCP (the importer) | The importer emits ordinary AUTH-G scene/trigger records, validated and simulated deterministically (hash chain ×3), instead of a runtime that interprets a proprietary graph at play time |
| Visual-state delta table driving a layered character | The pilot's build shape names it as the doll's driver | torogao-format / engine (rig seam) | State changes are authored records evaluated under the determinism contract, with the face-first readout discipline — not deltas baked into scene files |
| Clock + economy as project data | 4-slot clock, TP economy, schedules — all in the §G5 paper map, verified 6/7 against the build | torogao-runtime | Named stats and clock records the dead-state lint can see, instead of fields whose wiring only the original's scripts know |

The PCK container itself is a study format: the reverse-engineering tooling censuses it,
Torogao never reads it at build time. The importer consumes the reverse-engineering tooling's
census output and the study, per the map §4 doctrine — never the
source game's assets, scripts, or dialogue as build input.

### Seams

- **The Ranch's audio lane** owns audio. A studied game's audio census is
  measurement; Ranch audio reaches a Godot-shaped study only as
  reference, and Torogao binds audio by id (map §5).
- **The Ranch's reverse-engineering tooling** owns measurement: `inspect_godot_pck` and the future
  `.gdc` token extractor are on the reverse-engineering tooling's side. Their output is the
  importer's and the studies' input; the reverse-engineering tooling never emits Torogao
  projects.
- **The sprite-to-3D factory** owns textures, meshes, and rigs (map §5). Ranch-original
  assets reach Torogao through the sprite-to-3D factory by id. The graphics-enhancement obligation
  above applies to any asset pipeline described here, including this
  seam.

## Daddy Style treatment

Priority order, always: **Safety > Performance > Developer Experience.**

For adult builds this order is not abstract. Safety is the player,
the workstation, and the studied material staying inside their
bounds; performance is a scene that holds its frame rate when a
layered character, a dialogue system, and a background are all live
at once; developer experience is the tooling that lets a small Ranch
team ship that scene without hand-waving. When the three pull apart,
they resolve in that order.

### Bounds

These are Ranch policy, not Godot limits. Every run carries named
limits with units. Alphabetical:

| Name | Value | Reason |
| ---- | ----- | ------ |
| `CHECK_TIMEOUT_S` | 30 s | A parse check is CPU-only; longer means something is wrong |
| `EXPORT_TIMEOUT_S` | 300 s | Exports do a full import + pack; longer only with a named reason in the run record |
| `IMPORT_TIMEOUT_S` | 120 s | The scratch project's import finished in seconds; big projects justify their own number in the record |
| `PACK_FILES_MAX` | 4096 files | `PCKPacker` jobs name their file list; an unbounded walk of a tree is not a pack spec |
| `PROBE_STDOUT_BYTES_MAX` | 4 KiB | `--version` is one line; the census probes are a few dozen lines |
| `PROBE_TIMEOUT_S` | 10 s | Prior-family probe bound for `--version`-class calls |
| `RUN_STDERR_BYTES_MAX` | 64 KiB | Captured whole, then truncated to 2 KiB for the run record |
| `RUN_STDOUT_BYTES_MAX` | 1 MiB | Scene censuses beyond this go to a file, not stdout |
| `SCRIPT_TIMEOUT_S` | 30 s | Tool scripts are bounded transforms; the rterr hang (**R**) is what this bound exists for |
| `UID_SIDECAR_REVIEW` | every new `.gd.uid` | First-import sidecars are reviewed and committed deliberately, never swept in silently |

### Contracts

Every run answers these questions before it starts. Alphabetical:

- **Bounds**: the deadline and byte caps above, always including a
  `timeout` wrapper — Godot will not reliably kill itself (**R**).
- **Failure behaviour**: a non-zero exit, a missing sentinel, a
  `SCRIPT ERROR` or `ERROR:` line on stderr, a missing or misshapen
  output, or a timeout. Each is a failure, reported with the run
  record. Partial outputs are deleted or quarantined.
- **Inputs accepted**: an absolute `--path` to a directory containing
  `project.godot`; script paths in `res://` form that exist;
  `export_presets.cfg` present before any export flag is used.
- **Inputs rejected**: relative project paths; a `--script` path that
  does not exist (exit 1, **R**, but reject it before the run, not
  through it); an output path equal to any input path; any studied
  game's pack, scene, or script as an input to a *run* (static census
  only — see "RE alignment").
- **Owner of cleanup**: the runner owns its scratch project copies
  and removes them; the `.godot/` cache inside a *working* project is
  the project's own and is never deleted by a pipeline.
- **Trust boundary**: every project is code. A `project.godot` plus
  its scripts is an executable program; opening an untrusted project
  in the editor or running it headless executes its GDScript and any
  GDExtension it carries. Untrusted projects are censused statically,
  never opened. (This is the Godot form of the Ranch's `.blend`
  discipline.)

### Converters

CODE-FIRST doctrine: the code form is canonical, and Godot's forms
are derived. Every conversion is a **named, versioned converter**.
Its version bumps whenever its argv, its normalization, or the pinned
Godot version changes. Converters, alphabetical:

| Converter | Direction | Fixed route | Normalization before comparison |
| --------- | --------- | ----------- | ------------------------------- |
| `gdcensus@1` | project → census JSON | `--headless --script` census tool: walk scenes via `ResourceLoader`, list scripts, autoloads, import sidecars | Lines as data in emitted order; the record serialized with sorted keys. `.godot/` cache contents are excluded (they are derived state) |
| `gd2pck@1` | project → data pack | `--headless --export-pack <preset> <out>.pck` | Compare the pack's **file census** (paths + per-file SHA-256 after extraction by a static reader), never the pack bytes: pack byte-stability across runs is **U** |
| `spec2scene@1` | code spec (JSON/RON) → `.tscn` | `--headless --script` builder tool: construct the tree, `PackedScene.pack`, `ResourceSaver.save` | Parse the saved text scene and compare the node/property record with **`unique_id` attributes stripped** — they are random per save (**R**: the only differing lines in a two-run diff). Then load and instantiate, and compare the live tree |
| `spec2cfg@1` | code spec → `project.godot` / ConfigFile text | `ConfigFile.set_value` in spec order, `ConfigFile.save` | Byte comparison is the gate: two saves of the same value set **in the same order** were byte-identical (**R**). Insertion order is part of the spec, because the writer preserves it (**R**) |

**Deterministic IDs.** Scene and resource files carry two ID kinds,
and they behave differently (**R**):

- **Script/resource UIDs** (`uid://…` in `.gd.uid` sidecars and
  `.import` files): assigned once at first scan, then stable. They
  may be used as IDs **after** the first import has been reviewed
  and the sidecars committed.
- **Node `unique_id` values in text scenes**: random per save. Never
  an ID. Strip before hashing, always.
- Converter output IDs are content addresses (SHA-256 over the
  normalized record), as elsewhere in the Ranch.

**Pinning.** Each converter version pins Godot `4.7.2`. When pacman
upgrades Godot, the goldens are regenerated **and reviewed**, and the
converter version bumps. A silent pass across an upgrade is not
trusted — 4.7's own `--help` shows how much surface moves between
versions (a 95-flag table).

### Golden tests

The test set is half validation and half adversarial. Every case runs
on a scratch copy under the bounds above. **The cases below are the
suite design; the probe runs of 2026-11-02 exercised the behaviours
most of them assert** (per-case mapping in `REPORT-godot.md`). Cases
not yet run as a packaged suite are marked as designed-not-run there,
not silently claimed.

Adversarial (6), alphabetical:

1. `adv-dash-path`: a project path or script path beginning with `-`.
   The runner rejects it before exec (argv safety); Godot is never
   invoked.
2. `adv-hang-script`: a tool script whose `_init()` raises a runtime
   error before `quit()`. Expected: the deadline kills it (exit 124),
   the run is reported failed, and stderr's `SCRIPT ERROR` is in the
   record. **This behaviour is R-verified** (the `rterr` probe).
3. `adv-missing-preset`: an export run in a project with no
   `export_presets.cfg`. Expected exit 1 with the named error.
   **R-verified.**
4. `adv-missing-template`: a runnable export with a preset but no
   templates. Expected exit 1 naming both template paths.
   **R-verified** on the Ranch workstation (it is the Ranch workstation's standing state).
5. `adv-output-equals-input`: a converter whose output path equals
   its input project path. The runner refuses; the input tree's
   hashes are unchanged.
6. `adv-zero-byte-asset`: a 0-byte WAV/PNG in the assets. The import
   pass must surface it as an error in the record, not as a silent
   skip. (The Ranch agent workers' probe log is the evidence this failure is quiet:
   their 0-byte WAV produced an import ERROR and a stub `.import`.)

Validation (6), alphabetical:

1. `val-census`: `gdcensus@1` on the fixture project reproduces the
   golden census (classes present, physics tick rate, main scene).
2. `val-check-only`: a clean script exits 0 under `--check-only`; a
   syntax-broken twin exits 1. **R-verified as probes.**
3. `val-config-roundtrip`: `spec2cfg@1` output is byte-identical
   across two runs and parses back to the spec's values.
   **R-verified as a probe.**
4. `val-import`: `--import` on the fixture assets produces the
   `.import` sidecars and the imported artifacts with the expected
   types (`texture` → `CompressedTexture2D`, `wav` →
   `AudioStreamWAV`). **R-verified as a probe.**
5. `val-pack-runs`: `gd2pck@1`'s pack runs standalone under
   `--main-pack` and the main scene's quit code propagates.
   **R-verified as a probe (exit 7).**
6. `val-scene-roundtrip`: `spec2scene@1` then load + instantiate
   reproduces the spec's tree (names, types, properties) after
   `unique_id` normalization. **R-verified as a probe.**

The fixture project is generated from a checked-in spec by the
converters themselves, never hand-made: a minimal `project.godot`,
one main scene, one tool script, one PNG, one WAV.

### Isolation

Godot has no per-run HOME isolation story like a config-dir tool:
runs write into the project's own `.godot/` directory and the user
editor settings (`~/.config/godot/`, which holds per-version
`editor_settings-4.7.tres` files, **S**). The Ranch rules are
therefore about *which project* a run touches:

- **Pipelines run on scratch copies.** A transform run never points
  `--path` at a live project tree; it copies the project, runs, and
  the copy is the output. (All probes in this leg ran that way.)
- **The editor settings are the Owner's.** Automation never passes a
  bare `--editor`, `--project-manager`, or `--import` against a
  project the Owner is editing, because editor passes write settings
  and caches.
- **Caches are honest state.** `.godot/` inside a working project is
  regenerable, but a pipeline that deletes it to "clean up" forces a
  full reimport on the Owner's next open. Runners clean only their
  own scratch trees.

### No hidden behaviour

- **First scan writes files.** Any editor-shaped pass (`--import`,
  an export, a `--script` run in a fresh checkout) creates `.godot/`,
  `uid_cache.bin`, and per-script `.gd.uid` sidecars (**R**). A
  "read-only look" at a project is therefore never read-only; take
  the copy first.
- **Exports compile scripts.** An exported pack stores `.gdc`
  bytecode, not `.gd` source (**R**, from the pack census log). A
  pack is not a source artifact and cannot be diffed as one.
- **Import names are hashes.** Imported artifacts are named
  `<file>-<32 hex>.<ext>` in `.godot/imported/` (**R**). What the hex
  is a hash *of* was not established in this leg (**U**); pipelines
  refer to artifacts through their `.import` files, never by
  reconstructing the name.
- **Sentinels over silence.** Every tool script prints `OK <job>` as
  its last act before `quit(0)`. A run that ends any other way —
  including a clean-looking exit after a `SCRIPT ERROR` — is a
  failure (see the exit contract).
- **`--write-movie` is not a capture route.** It crashes headless on
  this build (**R**). Nothing in a pipeline may list it as a step.

### Tool-script contract (headless GDScript)

Every script run via `--headless --script` satisfies all of these
(alphabetical). Language style itself is the `daddy-style-gdscript`
skill's territory; this is the run contract on top of it.

1. **Bounded work.** Loops over files, nodes, or pack entries carry
   named maxima (see Bounds). A script that walks a tree walks a
   tree it has counted first.
2. **Deterministic output.** Print results in a sorted or spec order.
   `ConfigFile` and scene saves preserve the order you build in
   (**R**); randomness (`unique_id`) is normalized at comparison
   time, never "seeded away" by assumption.
3. **Every path quits.** Structure the script so `quit(code)` is
   reached on success *and* on handled failure. The verified trap:
   an error in `_init()` skips everything after it and the process
   idles (**R**). Prefer the `MainLoop._process` staged shape (do
   work on a later iteration, return `true` to quit) or a single
   `_init` that validates first and calls `quit(1)` itself on bad
   input.
4. **Failure is a code and a line.** On bad input the script prints
   `FAIL <reason>` to stderr (via `printerr`) and quits non-zero
   itself. It never relies on an engine error to fail the run — the
   engine may not exit at all.
5. **Inputs through argv, validated.** User args after `--` arrive
   via `OS.get_cmdline_user_args()` (**B**). Validate count and shape
   at the top; a missing argument is `FAIL`, exit 1.
6. **No editor state.** Tool scripts run with
   `Engine.is_editor_hint() == false` (**R**). Code that needs the
   editor (`EditorScript`, `@tool` behaviours) is a different,
   Owner-supervised class and is **U** as an automation route.
7. **Output paths are parameters.** A tool script never hardcodes an
   output inside the project it reads; the runner passes the output
   path and checks it differs from every input.
8. **Static typing on the tool surface.** The census probe's
   `PackedStringArray` lesson (**R**): 4.7's API return types are
   exact, and a typed-variable mismatch is a runtime error, with the
   hang that follows. Type the variables, and let `--check-only`
   catch what it can before the run.
9. **Success is a sentinel.** The last print before `quit(0)` is
   `OK <job>`. The runner greps for it; absence is failure.

## UNVERIFIED register

Alphabetical. Each item is marked **U** at its point of use as well,
with its reason. Everything the 2026-11-02 probes settled has been
removed from this register and is marked **R** at its point of use;
the per-item record is in `REPORT-godot.md`.

- `AnimationPlayer` driving a TYPE_BLEND_SHAPE track in an
  editor-authored scene. Three code-built probe variants failed at
  the mixer's blend-shape name resolution; no editor-authored scene
  was probed, so the editor route is untested, not condemned.
- `AnimationTree` / state-machine playback headless. Classes verified
  to exist; no transition was played.
- `--export-debug`, `--export-patch`, and
  `--install-android-build-template` behaviour, and any successful
  runnable export. No export templates exist on the Ranch workstation.
- `--lsp-port` / `--dap-port` live client sessions. Flags are **B**;
  the editor setup's wiring is **S**; no session was opened.
- `--validate-conversion-3to4` and `--validate-extension-api`
  behaviour. In `--help` (**B**); never run.
- `--write-movie` under a real (non-dummy) display driver. The
  headless crash is settled; the real-driver route is untested.
- C# / .NET in the Ranch workstation binary. No C# project was probed;
  `--build-solutions` is **B** only.
- Exit code of a runtime error inside a running scene (a node
  `_ready()` error). The SceneTree `_init` hang is **R**; the scene
  case was not probed.
- Imported-artifact name hash input (the 32-hex suffix in
  `.godot/imported/`). Observed in every import; its input was not
  established.
- Out-of-range blend-shape values (below 0 or above 1) and
  skinned-morph evaluation order. Not probed.
- Pack (`.pck`) byte-stability across identical export runs. The
  census comparison is the gate precisely because this is open.
- `SkeletonIK3D` solving, `SpringBoneSimulator3D` simulation, and
  `XRFaceTracker` / `XRFaceModifier3D` behaviour. Existence is **R/S**;
  no probe could exercise them headless (and no XR device exists on
  the Ranch workstation).
- The 18-class difference between the runtime class list (1,054,
  **R**) and the extension API dump (1,036 classes, **S**). Counted,
  not diffed.
