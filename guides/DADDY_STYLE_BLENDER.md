# Daddy Style Blender — full guide

> Daddy Style is Nice Thoughts Ranch's house style for Blender,
> adapted for adult game production and published as part of
> Night School, the Ranch's public study programme.

Blender, driven the Ranch's way: headless first, scripts over clicking,
every claim tied to evidence, and the machine's two Blender builds treated
as the different tools they measurably are. Plain version first: Blender
is the Ranch's mesh-and-rig workshop — the place heroines are rigged
for adult scenes, soft-body and jiggle setups are weighted, fluid
simulations for explicit shots are baked, and finished bodies are
censused, converted, and rendered without a human at the mouse. It is
not a game engine and not a Torogao build target; it makes and inspects
the 3D assets that the sprite-to-3D factory carries and Torogao
references by id.

Version basis: **Blender 5.2.3 LTS**, commit `e13b728c6880`, in two
builds on the Ranch workstation — the Arch system build (`/usr/bin/blender`, package
`blender 17:5.2.3-5`, embedded Python 3.14.8) and the official tarball
staged at `~/blender-official/blender-5.2.3-linux-x64/`
(embedded Python 3.13.13; the tarball's SHA-256,
`78486c018b4443efe5e75ab54c290ed8c15abafd249b862c2c9ce2530a918eec`,
matches the `blender-5.2.3.sha256` list staged beside it). Both version
claims, both Python versions, the shared commit hash, and the tarball
hash are **R** (verified by run, 2026-11-02, this leg).

## Evidence legend

In strength order:

- **R** — verified by run on the Ranch workstation, 2026-11-02 (this leg's probes;
 per-probe record in `REPORT-blender.md`).
- **S** — static read of an installed file, 2026-11-02 (this leg, or
 Leg 0's reads recorded in the Ranch's facial-rigging notes / `VERIFY-facial.md`).
- **H** — the binary's own `--help` text, captured 2026-11-02.
- **A** — agent-worker draft claim, taken with attribution, not re-verified.
- **U** — UNVERIFIED. Named as such; do not build on it.

Where a claim came from the Ranch's agent workers and this leg verified
it, the text says "agent workers claimed; verified **R**" — the full
agent-worker ledger is in `REPORT-blender.md`.

## Agent use

### Broker and connector reality

- **`custom.blender` is the agent route.** It is a connector, not an
 MCP server: three headless operations over SSH to the Ranch workstation — GLB census
 (no Blender process; parses the file), `.blend` census (Blender,
 autoexec off), embedded-image extraction from GLBs, and single-frame
 renders. It reads and renders; it does not edit, save, or convert
 (connector doc, **S**).
- **No editor broker for Blender.** The Ranch's editor broker fronts Unreal Engine only.
 There is no brokered GUI route for Blender, and none is proposed by
 this leg (MCP recommendations are Leg 6's document).
- **The official Blender Lab MCP is a consumed upstream, never a
 Ranch server.** It is not merged into `custom.blender`.
 The Ranch's agent workers read its add-on as an unauthenticated localhost TCP socket
 (port 9876) that `exec`s received code, and ruled it GUI-lab only
 (**A** — their staged copy at `~/.local/share/blender-mcp` no longer
 exists on the Ranch workstation, so the code read could not be repeated; see the
 UNVERIFIED register). Independently, the Ranch workstation has an AUR package
 `blender-mcp-git r250.5a3618f-1` installed (`/usr/bin/mcp-for-blender`,
 a different, third-party codebase): its bundled add-on also defaults
 to `localhost` port 9876 and also runs received code with
 `exec(code, namespace)` (**S**:
 `/usr/lib/python3.14/site-packages/blender_mcp/bundled/addon.py`,
 host/port at line 1206, `exec` at line 2296). Two codebases, same
 rejected pattern: an unauthenticated localhost socket that executes
 code is not an agent route, whoever ships it. Agent use: none.
 Owner-supervised GUI lab use on a throwaway `.blend`, port closed
 afterwards, is the Owner's call, not an agent's.
- **The live-editor broker programme:** its named backends are Unity
 first, Godot later. It has no Blender tools
 (**A**, agent-worker fleet read; not re-grepped this leg).

### Capture and verification discipline

Every agent Blender run leaves a run record with: binary path and
`--version` first line, build (Arch or official), script SHA-256, argv,
input SHA-256, output SHA-256s, exit code, and the sentinel check.
A render or census without the record is not evidence. GUI work, when
the Owner authorises it at all, is verified headlessly afterwards
(census + comparison); screenshots are not the record. There is no op
log for Blender (that is the Ranch's editor broker's Unreal surface); the run record is
the substitute, appended to the task report.

### Deterministic routes over GUI

For every operation class in the CLI census, the SCRIPTABLE-HEADLESS or
CLI-NATIVE route is the agent route. GUI-ONLY classes (hand modelling,
sculpting, weight painting by hand, node-graph authoring by eye) are
handed to the Owner by name. An agent never substitutes clicking for a
missing script route; it writes the script or reports the gap.

## CLI census

On the Ranch's pipelines this census is what stands between a studied
adult game's extracted bodies and a shipped scene: census first, convert
second, render last, and never trust a file you have not counted. Classes:
**CLI-NATIVE** (a flag or command does it), **SCRIPTABLE-
HEADLESS** (a `bpy` script under the canonical argv does it),
**GUI-ONLY** (honest negative — no headless route). All rows rest on
5.2.3; evidence per row. Canonical argv and flag detail:
`blender-cli.md` (alongside this guide).

| Operation class | Class | Terminal route | Evidence |
| --------------- | ----- | -------------- | -------- |
| Add-on enable (incl. Rigify) | SCRIPTABLE-HEADLESS | Script: `addon_utils.enable(...)`; the `--addons` flag route fails for Rigify | R |
| Animation playback | GUI-ONLY | The `-a` player mode exists (H) but is a viewer, not a pipeline step; Ranch playback checks are renders + census | H |
| Armature / rig construction | SCRIPTABLE-HEADLESS | Script: edit bones in Edit Mode, pose bones in Pose Mode; see Facial rigging | R (probes), S |
| Asset census (`.blend`) | SCRIPTABLE-HEADLESS | Connector `blend-census`, or census script under canonical argv | R |
| Asset census (GLB) | CLI-NATIVE (connector) | Connector `glb-census` parses the GLB without Blender | S (connector doc) |
| Autoexec control | CLI-NATIVE | `-Y` always; `-y` never | R |
| Batch rendering (frame range) | CLI-NATIVE | `-b <file> -o <path> -s <a> -e <b> -a`, settings before `-a` | H; single-frame R |
| Extension management | CLI-NATIVE | `blender --command extension <sub>`, offline + staging only | R |
| FBX export | SCRIPTABLE-HEADLESS | Script: `bpy.ops.export_scene.fbx` | Operator R; behaviour U |
| FBX import | SCRIPTABLE-HEADLESS | Script: `bpy.ops.wm.fbx_import` (new) or `bpy.ops.import_scene.fbx` | Operators R; behaviour U |
| glTF export | SCRIPTABLE-HEADLESS | Script: `bpy.ops.export_scene.gltf` | R (byte-stable probe) |
| glTF import | SCRIPTABLE-HEADLESS | Script: `bpy.ops.import_scene.gltf` | R (round trip) |
| Hand modelling / sculpting | GUI-ONLY | None. Hand work; agents script or hand the task to the Owner | — |
| IK / constraint evaluation | SCRIPTABLE-HEADLESS | Script + depsgraph evaluation — **official build only** (Arch segfaults) | R |
| Image extraction from GLB | CLI-NATIVE (connector) | Connector `glb-census` side output | S (connector doc) |
| Keyframe / action authoring | SCRIPTABLE-HEADLESS | Script: `keyframe_insert`, action/slot APIs | Practice R (probe keyframing is the Ranch's editor setup's route, S); this leg U |
| Material / shader authoring | SCRIPTABLE-HEADLESS (mechanical) / GUI-ONLY (by eye) | Script for named, parametric node setups; visual authoring is the Owner's | — |
| Mesh editing (parametric) | SCRIPTABLE-HEADLESS | Script: `bpy.data` / `bmesh` | R (probes build meshes) |
| Node-graph authoring (geometry/shader/compositor) | GUI-ONLY by eye; SCRIPTABLE-HEADLESS for named graphs | Script can build graphs; judging them is visual | U (no probe) |
| Physics / simulation bake | SCRIPTABLE-HEADLESS | Script: set frame range + rate, bake to a scratch copy, compare caches | A (agent-worker depth notes); no probe this leg |
| Preferences / keymap editing | GUI-ONLY | None for agents; `--factory-startup` exists precisely to ignore them | H |
| Rigify rig generation | SCRIPTABLE-HEADLESS | Script route above — **official build only** (Arch segfaults) | R |
| Script execution | CLI-NATIVE | `-P <script>` / `--python-expr` under the canonical argv | R |
| Shape-key authoring (numeric) | SCRIPTABLE-HEADLESS | Script: `shape_key_add`, delta edits, drivers | R (probe), S |
| Single-frame render | CLI-NATIVE | `-b <file> -o <prefix> -f <n>`; connector `render-frame` | R |
| Skinning / weight assignment (numeric) | SCRIPTABLE-HEADLESS | Script: vertex groups, weight ops | A (agent-worker rigging probes, Ranch note); not re-run |
| UV editing by eye | GUI-ONLY | None | — |
| Version / help | CLI-NATIVE | `--version`, `--help`, `-E help`, `-c help` | R |
| Video sequence editing | GUI-ONLY for Ranch purposes | No Ranch route; not a Blender job in this programme | — |
| Weight painting by hand | GUI-ONLY | None. The numeric route above is the agent substitute | — |

## Editor-setup surface

The Ranch's editor setup's `lua/games/blender/` module (11 files: actions, batch,
character, commands, config, export, health, init, render, sprites,
versions) is the Ranch's in-editor Blender driver (**S**, read
2026-11-02). Findings, alphabetical; the editor setup was not edited — these are
proposals for the Ranch:

- **Argv builders are pure and list-shaped.** `character.lua`'s
 `build_argv` returns `{ bin, '-b', [blend], '--python', script }`
 and validates its inputs (non-empty, no NUL) before building
 (**S**, `character.lua` lines 213–240). Paths travel as argv
 entries, never interpolated into generated code (module's own
 stated contract).
- **No safety flags anywhere.** A grep of the whole module finds zero
 occurrences of `-Y`, `--factory-startup`, `--offline-mode`, or
 `--python-exit-code` (**S**). The Ranch's agent workers claimed the same of an earlier
 read; verified **S** this leg. Consequence: editor-driven runs
 inherit the user's preferences and startup file, a Python exception
 in a generated script exits 0, and a studied `.blend` opened through
 the editor setup relies on Blender's CLI untrusted-by-default behaviour alone.
 Proposal: one shared argv builder emitting the canonical argv
 (below), with the binary as a config value.
- **Binary config exists.** `config.lua` carries a managed install
 root (`~/workspace/tools/blender`) and a `bin` override field on
 the character options (**S**). Proposal: pin the official 5.2.3
 build for rigging-class jobs per the Binary choice rule.

## Facial rigging cross-reference

Blender facial mechanics are specified once, in the Ranch's facial-rigging notes
(Leg 0, same workdir), and this guide does not duplicate them. What
lives there, by its own anchors: the ARKit-52 channel mapping (shape
keys by name; the glTF exporter parameters), blink construction
(relative keys, `slider_min`/`slider_max` overshoot room, the Rigify
bone blink), bone-based facial rigs (Rigify `face.skin_eye`), eye and
eyelid mechanics (the surface-clamped lid — the structural answer to
the Owner's "eyelids above the eyes" defect), gaze implementation
(Damped Track, lid follow (0.2, 0.7) with corner falloff), and the
shape-key API table. Read it before any facial work in Blender.

This leg adds three verified data to Leg 0's record:

- **Damped Track does not crash the Arch build.** A one-bone armature
 with a `DAMPED_TRACK` constraint to an Empty, depsgraph-evaluated,
 exits 0 on both builds (**R**). Leg 0 left this **U**; the Arch
 crash class is narrower than "constraints": it bites IK evaluation
 and Rigify generation (below), not Damped Track alone.
- **Leg 0's Rigify caveat is confirmed with the Ranch's agent workers' exact numbers.**
 Official build, `addon_utils` route: metarig 159 bones, generated
 rig `rig` with 706 bones, 160 `DEF-` (**R**). Arch build: segfault
 139 (**R**). The Ranch's agent workers claimed; verified **R**.
- **The Prima avatar rig v2 takes are not a reference.** Owner ruling
 2026-11-02 08:49 PST: the approval was an accidental tap; his
 verdict stands as "still wrong". Nothing in this guide is derived
 from, compared against, or calibrated to v2.

## Owner use

### Plain-language opening

You mostly will not open Blender's window. You will give the
command line a file — say, a heroine's scene ready for a jiggle-physics
bake or a night's batch render of an explicit cut — and a small Python
script, Blender will do the work with no interface at all, and it will
print one line saying it finished. Three habits keep that safe and
honest. First, `-Y`: never
let a file run code just because you opened it — a `.blend` can carry
scripts. Second, know which Blender you are running: the Ranch workstation has two
builds of the same version, and one of them crashes on rigging work
(below). Third, never trust "it exited fine" — Blender exits 0 even
when the script failed, unless you pass the flag that makes failures
loud.

### Mechanism, in full depth

Arguments execute strictly in the order given (**H**, **R**): the
file loads when its argument is reached, settings apply when theirs
is, and `-f 1` renders the moment it is parsed — which is why the
output path must be set before it. `--python-exit-code 1` converts a
Python exception into exit 1; without it the same failure exits 0
(**R**: measured 0 without, 1 with, 7 when 7 was requested).
Everything after `--` is passed untouched to your script in
`sys.argv`. A segfault exits 139 and writes `blender.crash.txt` to
`$TMPDIR`. Headless work runs under `timeout`, with `-noaudio`
(audio is never part of a gate), `--offline-mode`, and
`--factory-startup` so your personal startup file and preferences
cannot change the result. The connector pins
`VK_ICD_FILENAMES` to the NVIDIA ICD so GPU work never enumerates the
Intel iGPU.

**The two builds.** Same version, same commit (`e13b728c6880`), and
measurably different behaviour (**R**): the Arch build (system Python
3.14.8, branch `makepkg (modified)`) segfaults when a script evaluates
an IK constraint against a real target, and when Rigify generates a
rig; the official build (bundled Python 3.13.13) passes both, with
Rigify producing exactly the expected rig (706 bones, 160 deform).
A symbolised trace (2026-11-02, Arch debuginfod + addr2line) places
the fault in an Eigen aligned packet load inside
`ColPivHouseholderQR` preconditioning for `JacobiSVD`, called by the
legacy IK solver's `IK_QJacobian::Invert` during a depsgraph TBB
task. TBB is the execution context, not the fault, and no Python
frames appear in the faulting stack. Why the Arch build reaches a bad
load there while the official build passes is still not isolated
(**U**). The rule is operational, not causal:
**rigging-class headless work (IK, Rigify, anything that evaluates
constraints into a gate) runs on the official binary, pinned by path;
census, export, and Workbench renders are verified on both.** Which
binary a run used is part of its record. Replacing the system package
is your call, not an agent's.

### First commands, with the check for each

```bash
# 1. Which Blender, which build. Expect: Blender 5.2.3 LTS, and the
# build branch line tells you which build you have.
/usr/bin/blender --version
~/blender-official/blender-5.2.3-linux-x64/blender --version

# 2. Census a .blend without trusting it (autoexec off, no UI).
# Check: exit=0 and an "OK" line in the log.
timeout --kill-after=10s 120s /usr/bin/blender -b -Y --factory-startup \
 --offline-mode -noaudio --python-exit-code 1 \
 --python ~/scratch/blend_census.py -- /abs/path/scene.blend \
 > ~/scratch/census.log 2>&1; echo "exit=$?"

# 3. Render one frame. Output BEFORE -f, always.
# Check: exit=0 and out_0001.png exists with a fresh timestamp.
timeout --kill-after=10s 300s /usr/bin/blender -b -Y --factory-startup \
 --offline-mode -noaudio /abs/path/scene.blend \
 -o ~/scratch/out_ -f 1; echo "exit=$?"

# 4. Or use the connector (census, image extraction, one frame):
python3 ~/workspace/custom-connectors/custom.blender/bin/blender_tools.py version
python3 ~/workspace/custom-connectors/custom.blender/bin/blender_tools.py blend-census /abs/path/scene.blend
python3 ~/workspace/custom-connectors/custom.blender/bin/blender_tools.py glb-census /abs/path/model.glb
```

(The connector commands are the connector doc's own routes, **S**;
`version` is its documented health check.)

### Desk techniques (interactive only)

Two repertoire techniques from the four-video review (T-7).
Both are **interactive-only**: they depend on the viewport,
the pointer and a hand on the sculpt brush, so they are desk
repertoire for the Owner's own sessions and stay **out of every
headless gate** — no gate may require them, simulate them, or
treat them as run. The mechanisms are **PROVEN-BY-VIDEO**
(demonstrated in the source dossier); Ranch desk verification is
owed, not done — see the proof line at the end.

**Face Project snapping with Project Individual Elements — drape
a flat shape onto a curved body.** The job: place a flat piece
authored in 2D (a brow strip, a collar strap, a tattoo decal)
onto a curved surface — a face, a breast, a hip — so it follows
the surface in one gesture instead of vertex by vertex.
In Edit Mode, set the snap target to Face Project and enable
**Project Individual Elements** in the snapping options. Select
the strip, move it toward the body, and each element projects
individually along the view onto the target surface, so the flat
shape lands draped over the curvature. Two disciplines: the
projection follows the current view, so frame the surface square-on
before the move; and the result is a placement, not a weld —
check the strip's distance off the surface afterwards and shrink
or offset it deliberately rather than trusting the drape.

**Face Sets by loose parts, with auto-masking — isolate
disconnected pieces while sculpting.** The job: sculpt one
disconnected piece (a breast, a tail, a horn, a hand-held prop)
without the brush dragging its neighbours. In Sculpt Mode, initialise face
sets from the mesh's loose parts (Face Sets → Init Face Sets →
By Loose Parts) so every disconnected piece becomes its own face
set in one command. Then enable **Face Sets auto-masking** so
brush strokes affect only the active face set; the **Boundary**
variant of auto-masking confines the stroke at the face-set
boundary itself, which is the setting that keeps falloff from
bleeding across the seam between pieces. Face sets are sculpt
isolation, not mesh structure: they cost the model nothing and
can be reinitialised whenever the piece layout changes.

**Proof owed.** There is no formal test. Proof is one
supervised desk task using each technique; the named occasion is
the collar-and-brow placement on the T-5 heroine build (Face Project drape for
the collar strap and brow strip, loose-parts face sets for isolating the pieces
being sculpted). Until that task runs, both notes are repertoire
on video evidence — **U** for Ranch desk use, recorded as owed
here rather than implied done.

## RE alignment

### Graphics-enhancement pass

The brief requires the graphics-enhancement pass convention to
be stated wherever asset pipelines are described. Its text is not in
any staged source available to this leg (the Aseprite leg recorded
the same gap). **U**: the obligation is recorded at both asset
pipelines below (converters, sprite-to-3D factory seam); the convention itself is
not invented here.

### Static RE only

The Ranch does not reverse-engineer Blender, and does not
reverse-engineer games *with* Blender by executing anything — the
studied titles on the Ranch's shelves are adult games, and the posture
below applies to their assets exactly as written. Blender
is a content tool, not a game runtime: no pilot class in the Phase 1
tranche (Ren'Py, RPG Maker MV, Unity IL2CPP, Unity Mono, Godot,
GameMaker, Electron) is a Blender game (**S**, `PHASE1-REPORT.md` —
Blender does not appear in it). The RE posture that applies here is
the file posture: a `.blend` from any studied source is executable
content — census it headless with `-Y`, on a copy, and never open it
in the GUI or with `-y`. Blender's own sources are a study target of
a different kind: Rigify's shipped Python (`face.skin_eye` and
friends) is read statically to learn mechanisms, exactly as Leg 0
did. Nothing is executed to learn it.

### Torogao: what is adopted, adapted, improved

The unified engine map names **no Blender row** (**S**:
the Torogao unified engine map (Ranch-internal) read in full; the word does not
appear). Blender enters Torogao's world through the map's §5 sprite-to-3D factory
seam: *the sprite-to-3D factory owns meshes/rigs/textures; Torogao references them by id
and never embeds them in game records*, and character records convert
out GLB-first. Within that seam:

- **Adopted (mechanisms, via Leg 0):** the channel separation Blender's
 reference eye rig proves — aperture (lid position on the eyeball
 surface) ≠ gaze (eye rotation) ≠ iris scale (a deliberate, separate
 channel) — as Torogao rig parameters; the corner-falloff lid follow
 weights (0.2, 0.7) and `1 − (θ/θc)²` falloff; sampling-safe closed
 holds in blink curves (`export_frame_step` discipline on the
 Blender side). Full treatment: the Ranch's facial-rigging notes → "Blender — RE
 study and Torogao adoption".
- **Adapted:** Rigify's rig *shape* (metarig → generated rig, `DEF-`
 deform set, no runtime dependence on the generator) as the pattern
 for the sprite-to-3D factory's rig records: a rig is data with a deform set and a rest
 pose, generatable and hashable, not an editor session. The 2D side
 fakes the eyeball surface with an arc path and a clip mask — the
 analogy is stated, not hidden (Leg 0).
- **Improved (Ranch-side, over the source tool):** the determinism
 and safety wrapper Blender itself does not provide — pinned binary
 per job class, canonical argv, exit-code honesty, byte-stability
 facts measured per format (GLB yes for the probe scene, `.blend`
 within-build only), and the crash map (Arch vs official) that a
 naive `blender` invocation would walk into blind.

### Seams

- **The Ranch's reverse-engineering tooling** censuses studied games; Blender assets extracted by any
 route are re-censused by the connector before use.
- **The sprite-to-3D factory** is the owner of everything Blender produces for the
 Ranch: GLB-first conversion, rig import, texture handling.
 Blender is the sprite-to-3D factory's workshop tool, invoked through the connector or
 the canonical argv, never a runtime dependency of a shipped game.
- **Torogao** references the results by id (map §5). It never embeds
 a `.blend`, and no Torogao build step requires Blender to be
 installed on a player's machine.

## Daddy Style treatment

Safety > performance > developer experience, in that order, applied
to a tool whose defaults are "trust the file" and "exit 0 anyway".
Adult production is exactly where that discipline pays: a night's
explicit-scene renders, soft-body bakes, and fluid passes are long,
unattended, and worthless if a single frame silently came from the
wrong binary, the wrong file, or a script that failed at exit 0.

### Binary choice

Named under Owner use (Mechanism) because the Owner runs these
commands too; the rule binds agents identically: rigging-class work
on the official binary pinned by absolute path
(`~/blender-official/blender-5.2.3-linux-x64/blender`,
SHA-256 of the binary `b8b07a190fb25db76aae6de08dbc6c2b3d64e22e82bed6ba90de9545859f3431`,
**R**); all other classes verified per build before a gate trusts
them. A gate report that does not name its binary is incomplete.

### Bounds

Named limits, with units, for every Ranch Blender run:

| Limit | Value | Why |
| ----- | ----- | --- |
| `BLEND_INPUT_BYTES_MAX` | 512 MiB | Census rejects larger studied files before Blender sees them (house bound, proposed) |
| `FRAMES_PER_RUN_MAX` | 1 024 frames | Longer renders split into per-range runs with separate records |
| `LOG_BYTES_MAX` | 8 MiB captured stdout+stderr per run | Beyond that the run is diagnosed, not trusted |
| `PROBE_STDOUT_BYTES_MAX` | 4 KiB for `--version`/`--help`-class probes | Enough for the outputs; more means something else ran |
| `RUN_TIMEOUT_S` | 120 s census / 300 s single frame / job-named otherwise | `timeout --kill-after=10s` wraps every run |
| `THREADS` | Pinned per job (`-t <n>`), never 0 in a gate | 0 = "all cores" is a different machine each run |

### Contracts

- **Argv is a list, never a shell string.** Absolute paths only;
 reject a path beginning with `-` (an unrecognised argument is
 treated as a file to load, **R** — a leading-dash path is an
 argument-confusion hazard, not a filename).
- **Canonical argv** (order carries meaning, so it is not
 alphabetical): `timeout --kill-after=10s <N>s <BIN> -b [-Y]
 --factory-startup --offline-mode -noaudio -t <k>
 --python-exit-code 1 --log-file <abs> [file.blend] -P <script> --
 <args>`. Render variant: settings (`-E`, `-F`, `-o`) after the file,
 `-f`/`-a` last.
- **Exit contract:** 0 + `OK <name>` sentinel + every expected output
 present + output comparison where a golden exists. 139 is a crash,
 124 is the runner's timeout, and a Python exception without
 `--python-exit-code` is a silent 0 — all three are failures the
 contract exists to catch.
- **Isolation:** runs point `BLENDER_USER_CONFIG` /
 `BLENDER_USER_RESOURCES` at a throwaway directory (env vars, **H**)
 or run under `--factory-startup` with the live preferences treated
 as untrusted input; studied files are opened only as scratch
 copies, and outputs land in a scratch output directory, never next
 to a studied original.
- **No hidden behaviour:** no `-y`, no `--python-text`, no
 `--python-use-system-env` / `--python-use-user-env`, no
 `--online-mode`, no extension `sync`/`update`, no background
 threads or timer-driven logic in scripts, no stored RNA references
 across mutations (see `bpy-scripting-api.md`).
- **Scripts follow `daddy-style-python`** (the Ranch's Python style guide): explicit
 imports, typed signatures where the API allows, `faulthandler`
 enabled first, bounded loops, one `OK` line on success, failure by
 exception (converted to a real exit code by the argv contract).

### Converters

CODE-FIRST: conversion between the code form and Blender's form is
through named, versioned converters; nothing converts by hand-waving.

| Converter | Direction | Status |
| --------- | --------- | ------ |
| `blend-census@1` | `.blend` → census JSON (objects, bones, shape keys, actions, materials, images) | Exists: the connector's `blend_census.py` route (**S**, connector doc); its output shape is the de facto v1 |
| `blend2glb@1` | `.blend` → GLB via `bpy.ops.export_scene.gltf`, pinned exporter parameters recorded in the run record | Specified; the export half is probe-verified (**R**, byte-stable on the probe scene); the packaged converter is not built |
| `glb-census@1` | GLB → census JSON incl. morph-target counts and embedded-image hashes | Exists: the connector's `glb_census.py` (**S**) |
| `rig-gate@1` | Rig → PASS/FAIL (deform set, weight sums, influence cap, naming symmetry, rest round trip) | Proposal (the Ranch's agent workers' §13.8 lineage, **A**); the Rigify-shape assertions (706/160 class) are probe-verified, the gate script is not built |

Deterministic IDs: GLB node/morph names carry identity; `.blend`
datablock names are the ID space, and a converter records the
name → output-index map in its census. `.blend` bytes are stable
within a build only (**R**), so golden comparisons for `.blend`
outputs are census comparisons; GLB goldens may compare bytes where
the probe scope holds, decoded content everywhere else.

### Golden tests

Half validation, half adversarial, per the standing split. The suite
is specified here; this leg *ran* the probe cases marked **R** as
individual probes (same scripts, same assertions), and the packaged
suite runner is not built — that distinction is stated, not smoothed
over.

Validation cases:

- `val-census-known-scene` — census of a generated fixture returns
 the exact object/bone/key sets (**R** in substance: connector
 census + this leg's probes).
- `val-export-roundtrip` — cube + shape key → GLB → import → keys
 `['Basis', 'Smile']` (**R**).
- `val-ik-pose` — IK chain evaluates to the recorded pose
 (official build) (**R**).
- `val-render-frame` — 32×32 Workbench frame lands at the named
 output path on both builds (**R**).
- `val-rigify-generate` — human metarig → rig with 706 bones / 160
 `DEF-` (official build) (**R**).
- `val-save-stability` — two saves of one scene are byte-identical
 within a build (**R**).

Adversarial cases:

- `adv-arch-ik` — the IK case on the Arch build must be *caught*
 (139, no sentinel), never pass silently (**R**: it crashes; the
 gate's job is to refuse the build for this class).
- `adv-autoexec-armed` — a scratch `.blend` with a registered text
 block must not execute under the canonical argv; it executes only
 under `-y` (**R**).
- `adv-corrupt-blend` — a truncated `.blend` must fail the census
 comparison, whatever the exit code (designed; not run).
- `adv-dash-path` — an input path beginning with `-` is rejected by
 the runner before exec (designed; not run).
- `adv-exception-exit` — a raising script exits 1 under the canonical
 argv and 0 without `--python-exit-code`; the contract keys on the
 former (**R**).
- `adv-late-output` — `-f` before `-o` renders to the default path;
 the output-exists check must fail the run (**R**: the mismatch is
 real and silent, exit 0).

### RE boundary

See RE alignment. One line for the checklist: studied `.blend` files
are untrusted executables — copies only, `-Y` always, census before
any other contact, never the GUI.

## UNVERIFIED register

Alphabetical. Each item is marked **U** at its point of use as well.

- Arch-build segfault root cause (the fault is symbolised to an
 Eigen/JacobiSVD load under the legacy IK Jacobian inversion; the
 Arch-only trigger — build flags, system Eigen/GCC, or a degenerate
 Jacobian state — is not yet isolated).
- The Ranch's agent workers' Blender Lab MCP code read (port, `exec` line, no-auth,
 online-access refusal) — their staged copy no longer exists on the Ranch workstation;
 the pattern is independently confirmed for a different installed
 MCP package, which does not verify their read of the Lab code.
- The Ranch's agent workers' fleet greps beyond the editor setup (other
 Ranch tooling Blender references) — the editor setup re-verified
 **S**; the rest not re-grepped.
- The Ranch's agent workers' manual/API line citations throughout their drafts — the cited
 doc bundle (`~/.local/share/daddy-style/engine-docs/`) is gone from
 the Ranch workstation; citations cannot be re-checked and were not carried as
 evidence, only as leads.
- Cross-build determinism beyond the probe scope (pose hashes, large
 scenes, Cycles output; GLB byte equality was measured on one
 trivial scene only).
- Graphics-enhancement pass convention (text not staged).
- FBX / USD / Alembic / OBJ / PLY / STL operator behaviour beyond
 existence.
- GUI behaviour of every kind, including the autoexec trust prompt
 and preferences defaults (no GUI run this leg).
- Physics/simulation baking routes and Cycles gate settings (the Ranch's agent workers
 depth notes only).
- Skinning/weight-op probe results in the Ranch's agent workers' rigging note (their probe
 scripts are not on the Ranch workstation; the note's §4 summary is **A** here).
- `--disable-crash-handler` effect on the 139 exit code.
- Timers under a manually pumped event loop.
