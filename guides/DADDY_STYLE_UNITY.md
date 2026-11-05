# Daddy Style Unity — full guide

> This is the Ranch's house style guide for Unity, adapted for
> adult game production on the Ranch's pipelines. It is part of
> Night School, the Ranch's public study programme.

Version basis: **unity CLI 1.0.0-beta.13** (`~/.local/bin/unity`) and
**Unity Editor 6000.6.6f1** (the build target), both on the Ranch workstation.
Editor 7000.0.0a10 is installed alongside; it is a 7.0 alpha, is not
a build target, and no route in this guide targets it. Where a
section rests on a different version, the section says so.

Plain version, for the Ranch's work: this is how adult games
get built in Unity here — character-customization systems,
blendshape facial rigs that have to hold an expression through
an adult scene, imported bodies and outfits, and player builds
that ship explicit content. The discipline is boring on
purpose. The content is not, but a build that cannot be
reproduced, a census that cannot be trusted, or a facial rig
whose weights were never measured will fail exactly when a
scene depends on it.

This guide holds the full reasoning. It is the operational
core as well, and when a shorter Ranch summary disagrees with
it, this guide wins. The
command tables live in `unity-cli.md` and the API tables in
`unity-editor-api.md`. Facial mechanisms live in the Ranch's
facial-rigging notes and are cross-referenced, never duplicated.

## Evidence legend

The order below carries meaning (strongest evidence first), so it
is not alphabetical.

- **R**: verified by run on the Ranch workstation on 2026-11-02. The command is
  named at the point of use. Editor batchmode runs credited to
  **R** via `VERIFY-facial-runs.md` Probe 3 ran on 2026-11-02
  against a scratch copy and were judged by logs and output files.
- **S**: statically verified on 2026-11-02 by reading an installed
  file (the Editor's XML API docs, a project file, a package
  manifest, the live editor-setup tree). The file is named at each use.
- **D**: stated in official documentation. Two sub-cases, named
  where it matters: (a) text shipped inside the installed CLI
  itself, read via `unity skill show` / `--help` on 2026-11-02 —
  documentation, but documentation of exactly the installed
  version; (b) verbatim citations of the 6000.6 offline manual /
  ScriptReference by the Ranch's agent workers, taken from
  their drafts. The staged docs tree kept by the Ranch's agent
  workers no longer exists on the Ranch workstation (checked
  2026-11-02), so sub-case (b)
  citations cannot be re-read against the staged copy; they stay
  **D** with **[A]** attribution and never carry a gate alone.
- **A**: a draft claim by the Ranch's agent workers
  (`un-guide.md` / `un-depth.md`,
  2026-10-27), kept with attribution. **A** is provenance, not
  evidence: an **[A]** claim is only as strong as the **R**/**S**/
  **D** mark beside it.
- **U**: UNVERIFIED. No source available to this leg settles it.
  A **U** claim never carries load in a pipeline without a probe
  run first. Every **U** in this guide is gathered in the closing
  UNVERIFIED register with its reason.

**Execution status.** The CLI surface of this guide was exercised
by run on 2026-11-02 (version, editors, projects, env, license,
status, pipeline list, build target list, exit-code probes, the
commands manifest). Editor batchmode behaviour rests on the facial
leg's Probe 3 runs (three invocations, PASS) plus Ranch-measured
Track B failures F1–F5 (2026-10-19). No new Editor run was launched
by this leg: the Ranch workstation good-neighbour rules and the already-landed
Probe 3 evidence made a duplicate heavy run poor value. Claims no
run settles are marked **U** in place.

## Agent use

Plain version: agents drive Unity the way a build server would —
the `unity` CLI for everything outside a project, and short,
bounded Editor batchmode runs for everything inside one. They do
not click the Editor, and the Ranch has no broker route for
Unity: work goes through the `unity` CLI, Editor batchmode,
and the Ranch's Unity connector. On the Ranch, agent work
serves adult builds the way a build server's work would on any
other title: censuses of characters, bodies, outfits, and
scenes; bounded builds; and bounded test runs — never a hand
clicking through an explicit scene to see whether it worked.

### Broker and connector reality

Every item below was checked on 2026-11-02:

- **`custom.unity` connector** (the Ranch's Unity connector):
  wraps the unity CLI and the Editor
  batchmode pattern. Its helpers list projects and Editors, show
  live Editor state, inspect a `.unitypackage` without importing
  it, and run one named Editor method in batchmode (exporting
  `DISPLAY` / `XDG_RUNTIME_DIR`, echoing the exit code, printing
  the log tail). It deliberately does **not** wrap the CLI
  `command` / `eval` verbs, does not sign in, manage licenses, or
  download store assets.
- **No broker target for Unity.** The Ranch's other broker
  tooling is a born-modern rmcp broker for Unreal Engine 5.8's
  built-in MCP server only. There is no Unity equivalent at
  the Ranch and this guide proposes none; MCP recommendations
  are a separate leg's deliverable.
- **Pipeline package (Unity's own live-Editor surface).** The CLI
  drives a *running* Editor through the project's
  `com.unity.pipeline` package: `unity status`, `unity command`,
  `unity list`, `unity recompile`, and the `unity mcp` stdio
  server all ride it. On the Ranch workstation today it reaches nothing:
  `unity status --json` exits 6 with `STATUS_NO_INSTANCES` and
  `unity pipeline list --json` reports zero instances (**R**),
  and the flagship adult game project's Track B manifest carries
  no pipeline package (**S**). Preconditions for any future use, from the installed
  CLI's own text (**D**, `unity skill show`): Unity 6.0+, the
  package installed in the target project, the Editor in `ready`
  state (an Editor that booted with compile errors sits in Safe
  Mode, where the package never loads), and an explicit
  `--project-path` whenever more than one Editor could answer —
  an Editor open on a sibling checkout answers commands exactly
  like your own.
- **The Ranch's live game-editor broker** is an MCP broker,
  Unity backend first. Its Unity side is verified by source: its
  bridge package (version 0.1.0) connects the Unity Editor to
  the broker MCP server over an authenticated loopback
  WebSocket. Stage U0 spike: read-only `editor_state` and
  `scene_hierarchy` (**S**, the bridge package's manifest). So
  the broker today is read-only observation of a live Editor — the
  honest Unity analogue of the Unreal broker's `gui.observe`,
  with no `act` surface yet. The description by the Ranch's
  agent workers of the broker (rmcp,
  authenticated WS, read-only tools) is corroborated by that
  manifest [A].
- **Unity's in-Editor MCP server is deprecated.** The Ranch's
  agent workers cite the
  CLI documentation: Unity deprecated the MCP server component of
  the in-editor AI assistant package, and the `unity mcp` command
  in the CLI replaces it; CLI tools "drive the Editor directly,
  without MCP in between" (**D** [A]). Consequence: never add the
  deprecated in-Editor server to any declared-server list; the
  CLI's `unity mcp` (a stdio server fronting the Pipeline
  package) is the Unity-provided route, and the broker is the
  Ranch's.

### Capture and verification discipline

The GUI-work discipline, translated to Unity's surfaces:

1. **Observe** — `unity status` / `unity pipeline list` (CLI), or
   the broker's `editor_state` / `scene_hierarchy` (live Editor), or a
   batchmode census. Observation is read-only and cheap; do it
   before any act.
2. **Ground** — name the exact project path, Editor version,
   target, and method before acting. An ungrounded Editor act
   (wrong checkout, wrong version, project already open in the
   GUI) is the Unity form of clicking the wrong window.
3. **Act verified** — the act is a CLI verb or a bounded batchmode
   run; verification is the sentinel + output census, not the
   exit code and not a screenshot. For Play-mode verification the
   installed CLI's own text warns (**D**, `unity skill show`):
   an unfocused Editor can freeze at frame 1 while status still
   reports `playing`, and a screenshot can render a frozen frame
   that looks alive — proof of play is frame advancement and
   console state, not a still.

The **run record** replaces an op log for batchmode work. Every
run appends: CLI version, Editor version, project path (scratch
copy), full argv, log path, each declared output's SHA-256, the
sentinel line, the exit code, and the verdict (PASS / FAIL /
SHUTDOWN-CRASH). A run without a record did not happen.

### Configuration-writing commands are live-tree changes

`unity mcp configure <client>` writes an AI client's MCP
configuration file, and `unity skill install <client>` installs
the CLI's bundled skill into a client (both **R**, `--help` text
read 2026-11-02; the mutation consequence is the agent
workers', **D** [A] and plainly correct from the help text).
On the Ranch workstation those files are
live agent configuration. Neither command runs outside staging
without the Owner's approval. The same caution applies to
`unity setup`, `unity projects import`, and `unity config`
writes: read verbs are free, write verbs are named in the run
record before they run.

## Bounds

Named limits. Every route in this guide respects them; a route
that needs more names the reason in the run record.

| Constant | Value | Meaning |
|---|---|---|
| `CLI_LIGHT_TIMEOUT_S` | 30 s | Bound for light CLI verbs (version, editors, env, license, projects, status). |
| `CLI_OUTPUT_BYTES_MAX` | 1 MiB | Captured stdout per CLI call; use `--format json` + `--quiet` past it. |
| `EDITOR_RUN_TIMEOUT_S` | 900 s | Outer wall-clock bound for a batchmode run (the facial census used 600 s; captures may name 900 s). |
| `EDITOR_KILL_AFTER_S` | 30 s | Grace between TERM and KILL in the outer `timeout` wrapper. |
| `HEAVY_JOBS_MAX` | 1 | The Ranch workstation good-neighbour rule: one heavy job at a time; interactive work wins. |
| `LOG_TAIL_LINES` | 200 | Log tail quoted in a report; the full log is the evidence, kept by path. |
| `TEST_RETRIES_MAX` | 0 | Gates never retry failing tests into a pass (see Testing). |

## CLI census

Every operation class the Ranch needs, marked **CLI-NATIVE**
(a `unity` CLI verb does it), **SCRIPTABLE-HEADLESS** (an Editor
batchmode `-executeMethod` or a checked-in Editor script does it),
or **GUI-ONLY** (no terminal route; honest negative). Rows are
alphabetical. The exact flags live in `unity-cli.md`; the exact
APIs in `unity-editor-api.md`. Version basis for every row:
CLI 1.0.0-beta.13 / Editor 6000.6.6f1.

| Operation class | Class | Terminal route |
|---|---|---|
| Asset census (meshes, blendshapes, materials) | SCRIPTABLE-HEADLESS | Batchmode `-executeMethod` over `AssetDatabase` (the facial census pattern; **R** via Probe 3). |
| Asset Store purchase / download | GUI-ONLY | No CLI verb exists: `unity assets` has inspect / export / import only (**R**, `--help`). Downloads happen in the Editor's Package Manager / My Assets under the Owner's clicks (connector doc). |
| Blendshape / facial census | SCRIPTABLE-HEADLESS | `FaceCensus.Run` pattern from the Ranch's facial-rigging notes (**R**, Probe 3). Cross-reference, do not re-derive. |
| Build (player) | CLI-NATIVE | `unity build --target <T> --output-path <P>` or `--profile <asset>` (**R**, `--help` + `--list-targets`). Raw-Editor fallback: batchmode + `BuildPipeline.BuildPlayer` (**S**, API exists). |
| Build profile creation / listing | CLI-NATIVE | `unity build --create-profile <T>` / `--list-profiles` (**R**, `--help`). Authoring a profile's *contents* is GUI-ONLY (below). |
| Build profile content authoring | GUI-ONLY | Profile assets are edited in the Build Profiles window; no CLI verb authors their settings. |
| Compile-error report (running Editor) | CLI-NATIVE (conditional) | `unity recompile` against a Pipeline-connected Editor (**R**, verb exists). Useless against a Safe-Mode Editor, where the package never loads (**D**). |
| Editor install / uninstall / upgrade | CLI-NATIVE | `unity install` / `uninstall` / `editors upgrade` (**R**, verbs exist). **Out of bounds for pipelines**: installing is an Owner act, never a side effect (`--allow-install` is never passed silently). |
| Editor state (running instances) | CLI-NATIVE | `unity status` / `unity pipeline list` (**R**; both report zero instances on the Ranch workstation today). |
| Editor verification (install integrity) | CLI-NATIVE | `unity editors verify 6000.6.6f1` → `ok: true` (**R**). |
| GameObject / scene editing (live Editor) | CLI-NATIVE (conditional, gated) | `unity command` / `eval` via the Pipeline package — arbitrary code in the Editor; connector-unwrapped, Owner-command-only (see Agent use). Headless alternative: an Editor script in batchmode. |
| GameObject / scene editing (no live Editor) | SCRIPTABLE-HEADLESS | A checked-in Editor script under `-executeMethod` on a scratch copy. |
| Hub project registry (list / add / remove) | CLI-NATIVE | `unity projects list / add / remove` (**R**). Registry membership is never load-bearing: batchmode always takes an explicit path. |
| Humanoid Avatar mapping (auto) | SCRIPTABLE-HEADLESS | Importer settings in a checked-in `.meta` / an `AssetPostprocessor`; the *visual* mapping editor is GUI-ONLY (below). |
| Humanoid Avatar mapping (visual editor) | GUI-ONLY | The Avatar Configuration window (muscle / bone mapping UI) has no terminal route. Gates use a checked-in Avatar (Copy From Other Avatar) instead (**D** [A]). |
| Inspector property editing (arbitrary) | GUI-ONLY | No general CLI verb edits an arbitrary serialized property. The headless substitute is a purpose-written Editor script per property class — a converter, not a click. |
| License list / status | CLI-NATIVE | `unity license list` → Unity Personal + Asset Store, Assigned (**R**). Activation / return are Owner acts. |
| Live Editor command discovery | CLI-NATIVE | `unity command` (bare, lists Pipeline commands) and `unity list` (**R**, verbs exist; no instance to list from today). |
| MCP client configuration | CLI-NATIVE (gated) | `unity mcp configure` — writes client config files; staging only, Owner approval (see Agent use). |
| Package inspection (`.unitypackage`) | CLI-NATIVE | `unity assets inspect <file>` — contents without importing (**R**, verb exists; connector-wrapped). |
| Package manifest census | SCRIPTABLE-HEADLESS | Static read of `Packages/manifest.json` + `packages-lock.json` — no Editor needed at all (`unity-package-census@1`). |
| Play mode (enter / exit / capture) | SCRIPTABLE-HEADLESS | A batchmode driver method that enters Play mode, steps deterministically, captures, and exits (Track B pattern, Ranch-measured). `unity command editor_play` exists for a live Editor (**D**, `unity skill show`) but is gated as above. |
| Play mode (interactive playtesting) | GUI-ONLY | Feel, timing, and input response are judged by a person playing. Headless captures are evidence about frames, not about feel. |
| Prefab authoring (visual) | GUI-ONLY | Prefab Mode's visual editing has no terminal route. Prefab *censuses* and scripted prefab edits are SCRIPTABLE-HEADLESS. |
| Project creation | CLI-NATIVE | `unity projects create` / `projects new` (non-interactive) (**R**, verbs exist). Creation is an Owner act in practice; pipelines consume existing projects. |
| Project integrity check | CLI-NATIVE | `unity projects verify` (**R**; correctly reported "not a project" for a non-project path). |
| Rendering / screenshot capture | SCRIPTABLE-HEADLESS | Batchmode with a GPU device (NVIDIA ICD pinned) + `ScreenCapture` / explicit `RenderTexture` + `ReadPixels` (Track B pattern). `-nographics` cannot render. Reliability on Arch is **U**. |
| Scene view navigation / gizmo work | GUI-ONLY | No terminal route exists, and none is needed: scene state is data, censused headlessly. |
| Script execution (arbitrary C#, live Editor) | CLI-NATIVE (conditional, gated) | `unity command eval` — see GameObject row. Never wrapped, never unattended. |
| Test run (EditMode / PlayMode) | CLI-NATIVE | `unity test --mode <M> --output <xml>` (**R**, `--help`). Raw-Editor route: `-runTests -testPlatform <P> -testResults <xml>` (**D** [A]). |
| Timeline / Animator window authoring | GUI-ONLY | Visual curve and state-machine authoring has no terminal route. The *data* (clips, controllers) is censused and converted headlessly. |
| Version / environment diagnosis | CLI-NATIVE | `unity version`, `unity env`, `unity editors list -i` (**R**). `unity doctor` exists (**R**, `--help`) but its JSON run did not finish inside this leg's probe batch — timing **U**. |

**The honest summary.** Unity is the engine in this programme
where the GUI-only share is largest. Whole authoring surfaces —
Avatar configuration, Build Profile contents, Inspector editing,
Prefab Mode, Timeline / Animator authoring, playtesting — have no
terminal route at all. What the terminal does cover, it covers
well: builds, tests, censuses, imports, project / Editor
management, and package inspection are fully scriptable. The
Ranch's posture follows from that split: Unity is a *build and
measurement* target from the terminal, and an *authoring* target
only through checked-in code (Editor scripts, importer settings,
converters) — never through simulated clicking. For adult
work the split bites hardest in character authoring: faces,
bodies, and customization are authored by a person in the
GUI, and everything the Ranch ships from them is verified
headlessly afterwards.

## Converters and golden tests

Per the CODE-FIRST doctrine: conversion between the code form and
Unity's form is specified and deterministic — named, versioned
converters, golden tests, and deterministic GUIDs where the format
has them. Unity's format *does* have them: the `.meta` GUID (see
Determinism). On an adult title the worked example is a
character: an FBX body with its blendshape face, its textures,
and its `.meta` files either arrive as a named, golden-tested
conversion, or they do not arrive at all.

### Converters

Alphabetical. Each converter pins Editor 6000.6.6f1 and CLI
1.0.0-beta.13; a version bump of either re-gates the set.

- **`unity-asset-census@1`** — project → census TSV/JSON. Route:
  batchmode `-executeMethod` over `AssetDatabase` on a scratch
  copy; output sorted by asset path, then by index within the
  asset. The facial census (`FaceCensus.Run`,
  the Ranch's facial-rigging notes) is this converter's facial
  instance and
  its proof run (**R**, Probe 3 — including its caveat: a project
  with no blendshape-bearing mesh completes with a 0-byte TSV,
  so "non-empty" is a check only when such a mesh is expected).
- **`unity-build@1`** — project + target/profile → player +
  build report. Route: `unity build`. Two explicit modes (build
  vs test) exist because the raw-Editor test argv forbids
  `-quit` while the build argv requires an explicit target
  (**D** [A]) — the CLI wraps both, and the wrapper refuses a
  build with neither `--target` nor `--profile`.
- **`unity-fbx-intake@1`** — FBX (+ textures) → imported project
  assets with checked-in `.meta`. The importer contract answers
  Track B failure F1 structurally: embedded-texture and material
  mapping behaviour is set at import time by the converter
  (extract textures / asset postprocessor writes the atlas
  assignment), never by a post-hoc scene patch (Ranch ruling,
  staged note, **S**). Humanoid intake additionally enforces the
  T-pose / 4-bone-influence contract (**D** [A]; the 4-bone
  default and `SkinQuality` enum are **S**).
- **`unity-meta-audit@1`** — project → GUID report, no Editor
  needed. Static: every asset has a `.meta`, every `.meta` GUID
  is 32-hex and unique, no asset lacks a pair. This is the
  cheapest gate in the set and runs first.
- **`unity-package-census@1`** — project → package report, no
  Editor needed. Static read of `Packages/manifest.json` and
  `packages-lock.json`: package ids and versions, sorted. It is
  how "is the Pipeline package present?" was answered for Track
  B (**S**: it is not).

**Graphics-enhancement pass obligation.** The FBX-intake and asset-census pipelines
are asset pipelines, so the graphics-enhancement pass
convention applies to them — and its text is not staged anywhere
available to this leg (**U**, see the register). The converters
record provenance and hashes so a graphics-enhancement pass can be inserted
without re-specifying them; nothing stronger is claimed.

### Determinism

- **`.meta` GUIDs are the pinned IDs.** Format **S**: each
  `.meta` begins `fileFormatVersion: 2` and a `guid:` line of 32
  hex characters (read from Track B assets). Rules: check
  `.meta` files in; never let an import regenerate a GUID for an
  asset that already has one; assign a new asset's GUID once and
  treat the checked-in `.meta` as the record; audit duplicates
  with `unity-meta-audit@1`.
- **Editor scripts sort their collections.** `FindAssets` /
  `GetFiles` order is not guaranteed; sort by GUID or path before
  assigning serialized fields (**D** [A]).
- **No random or time-based values in asset generation**
  (`Random.value`, `Guid.NewGuid`, `DateTime.Now`) (**D** [A]).
  Where randomness is the subject, seed it (`Random.InitState`,
  cited by the Ranch's agent workers, **D** [A]).
- **Importer determinism check.** The Ranch's agent workers cite
  `-consistencyCheck` as the flag "intended to be used to test
  that importer output is deterministic" (**D** [A]). It is the
  named gate for `unity-fbx-intake@1`; this leg did not run it
  (**U** as a run claim).
- **Physics and time.** Fixed-step simulation is the default
  shape (`Time.fixedDeltaTime`, **S**, CoreModule.xml:61487),
  but citations by the Ranch's agent workers warn the interval
  between fixed updates is not itself fixed, and Maximum Allowed Timestep drops
  simulated time under load (**D** [A]). Deterministic gates
  therefore use Script simulation mode with manual
  `Physics.Simulate(step)` calls (`Physics.simulationMode` and
  `Physics.Simulate(float)` are **S**, PhysicsModule.xml:3288,
  :3799), a constant step, deterministic spawn order, and a
  seeded RNG — and still do not promise cross-machine
  bit-identity, because floating-point behaviour differs between
  architectures (**D** [A]).
- **Capture timing.** `Time.captureFramerate` decouples capture
  from wall clock (property **S**, CoreModule.xml:61477; the
  `captureDeltaTime` coupling is **D** [A]). Gate captures set
  it; they never trust real time.

### Golden tests

Half validation, half adversarial. Fixtures are scratch copies;
every case is judged by sentinel + outputs. The set is
*specified* here; the facial census cases among them have run
(**R**, Probe 3), the rest are designed, not run, and are marked
as such wherever a report cites them.

Validation (alphabetical):

- `val-build-zero-code` — `unity build` for
  `StandaloneLinux64` (a zero-code target per `--list-targets`,
  **R**) produces a player at the named output path.
- `val-census-blendshapes` — the facial census on a project with
  a known blendshape mesh lists exactly its names, sorted
  (**R**, Probe 3 shape).
- `val-census-empty` — the same census on a project with no
  blendshape mesh completes with the sentinel and a 0-byte TSV
  (**R**, Probe 3 caveat) — an empty result is a valid result,
  not an error.
- `val-meta-audit-clean` — a well-formed fixture passes
  `unity-meta-audit@1` with zero findings.
- `val-package-census` — the package census reproduces a
  fixture's manifest exactly, sorted.
- `val-test-editmode` — `unity test --mode EditMode` on a
  fixture with passing tests exits 0 and writes NUnit XML.

Adversarial (alphabetical):

- `adv-bad-cli-verb` — an unknown CLI command exits 2 with
  `INVALID_COMMAND_ARGS` and a complete JSON envelope (**R**,
  run this leg).
- `adv-compile-error-project` — a project with broken C# boots
  the Editor toward Safe Mode; Pipeline verbs cannot connect
  (**D**) and the batchmode census fails by missing sentinel,
  not by a trusted exit code.
- `adv-duplicate-guid` — two `.meta` files sharing a GUID fail
  `unity-meta-audit@1`.
- `adv-locked-project` — batchmode against a project already
  open (lockfile present) fails fast and is reported as a lock,
  not retried blindly (mechanism **D** [A] + Ranch F4).
- `adv-missing-target` — `unity-build@1` with neither target
  nor profile refuses to run.
- `adv-shutdown-crash` — a run whose outputs and sentinel are
  complete but whose Editor dies in shutdown is recorded
  SHUTDOWN-CRASH: neither PASS nor work-FAIL (Ranch F3).
- `adv-static-state-leak` — a Play-mode test that passes only
  because a static survived from the previous session fails the
  reset rule (see Daddy Style treatment).

## Facial cross-reference

All facial mechanisms are settled in the Ranch's facial-rigging
notes (with
`VERIFY-facial.md` and `VERIFY-facial-runs.md` as its evidence
records). This guide does not re-derive them. Those notes
carry the facial rigs this programme depends on, including
the blendshape faces characters use through adult scenes;
this guide only indexes the Unity facts underneath them,
with their settled evidence:

- AR Foundation 6.6.2 (with `ARFace`, `ARFaceManager`,
  `XRFaceBlendShape`) and 2D Animation 16.0.1 ship as installable
  packages in the Editor distribution; neither is in the flagship
  adult game project's manifest (**S**, facial leg).
- Blendshape weights are 0–100 (**R**, Probe 3: frames at 50 and
  100 read back verbatim; `SetBlendShapeWeight` round-tripped
  0 / 50 / 100).
- `HumanBodyBones.LeftEye` = 21, `RightEye` = 22, `Jaw` = 23
  (**R**, Probe 3; enum existence **S**,
  AnimationModule.xml:5389-5424).
- `LookAtConstraint` exists — "Constrains the orientation of a
  GameObject based on the position of one or more sources"
  (**S**, AnimationModule.xml:2339-2343) — alongside
  `RotationConstraint` (**S**) and the Animator look-at weights
  (`SetLookAtWeight` with `eyesWeight`, **S**).
- `Mesh.AddBlendShapeFrame` and `Mesh.GetBlendShapeName` are
  run-verified (**R**, Probe 3; signatures **S**,
  CoreModule.xml:26549, :26743).
- `ModelImporter.importBlendShapes` /
  `importBlendShapeNormals` / `importBlendShapeDeformPercent`
  exist (**S**, UnityEditor.CoreModule.xml:36368-36383);
  blendshape normals need FBX smoothing groups [A].
- `SpriteRenderer.maskInteraction` with
  `SpriteMaskInteraction` {None, VisibleInsideMask,
  VisibleOutsideMask} is the 2D aperture mechanism (**S**); one
  `SpriteRenderer` draws exactly one sprite at a time (**S**) —
  the single-slot basis for hard swaps to painted extremes.

The Prima avatar rig v2 takes are **not** Owner-approved (the
approval signal was an accidental tap, corrected 2026-11-02;
the Owner's verdict stands as "still wrong"). Nothing in this
guide cites or uses them as a reference.


## RE alignment

How the Ranch studies Unity games — studied adult Unity
games included, in both Mono and IL2CPP form — and what
Torogao, the singular build engine, takes from Unity. The
studied games are reverse-engineering material: measured,
never shipped, and never executed. Sources read for this
section: the Ranch's unified engine map and its Phase 1
report.

### Ranch rules (apply to every Unity study)

- **Static RE only; nothing executed.** Studied games are never
  run. Census tooling reads files; it does not load the game.
- **Provenance at birth.** Every study record carries origin,
  `content_label`, and evidence from birth (lane law). Unity
  pilots in Phase 1 are NTRanch-lane material.
- **Spec-level translation only.** The pipeline is a census by
  the Ranch's reverse-engineering tooling → STUDY.md (measured
  facts) → BUILD-BRIEF (spec) → authored
  Torogao records → `project_validate` → `game_simulate`
  evidence. No importer reads a source game's scripts, dialogue,
  or assets into a Torogao project (unified map §4).
- **Unmeasured stays unmeasured.** A dynamic that the census
  cannot reach is recorded as unmeasured, permanently, until a
  route measures it. It is never reconstructed from feel.

### The two Unity classes

Alphabetical:

- **Unity IL2CPP (pilot: Hypnosis Master) — Partial.** Route: a
  hand-built `global-metadata.dat` v29 parser censused 12,261
  types (the reverse-engineering tooling's il2cpp tools are
  Ghidra-targeted, not a census; the provider belongs in the
  Ranch's reverse-engineering tooling). The game's content
  and logic ship in 3,804 **encrypted** hot-update bundles and
  are statically unreachable — a **recorded negative**. Unblock
  would be bundle-key extraction via Ghidra on
  `GameAssembly.dll`, or runtime capture; both are outside
  static scope. Torogao consequence (unified map §4): **no
  importer** — census → study → authored records is the only
  honest route. Parity is two-tier: structural parity
  from type/field measurement; behavioural parity only after a
  dynamic-evidence route runs. The pilot's gauge dynamics are
  unmeasured and no parity gate may pretend otherwise. The
  hot-update channel itself is ruled handoff-owned if ever
  adopted: versioned project revisions via
  the Ranch's game-maker tooling, no runtime loader.
- **Unity Mono (pilot: RJ318915) — Full.** Route: `monodis`
  typedef / field / method census over `Assembly-CSharp.dll` —
  the entire state model from stock tooling in minutes, the
  cheapest route in the Phase 1 tranche. The Mono IL census
  provider belongs in the Ranch's reverse-engineering
  tooling's managed family. Torogao
  consequence (unified map §4): **no importer** either — IL is
  not a data layer, and there is nothing to import *from* that
  a study does not say better. What Torogao takes is primitives
  and patterns, authored from the BUILD-BRIEF.

### What Torogao adopts, adapts, or improves (Unity-derived)

Each item enters through the unified map's intake shape (§3):
measured behaviour cited from the STUDY, one Torogao layer, a
named anchor or missing primitive, a parity gate stated before
the build, and a concrete "better".

- **Face-first progression readout** (RJ318915 GAP #1; Torogao
  app + the rig seam). Measured: the progression state is
  legible on the character's face via `eyeLv0–4` whole-eye
  material swaps plus a slider, UI gauge secondary. Adoption:
  tier → expression-id binding as authored data (unified map §6
  slice 4). Parity gate: the five-step ladder reproduced as
  five governed expression ids bound to five tier bands, with
  the visual gate on rendered frames and hash-chain
  evidence that the binding is state-driven. Facial side: see
  the Ranch's facial-rigging notes — the same swap is the
  cleanest
  construction for extreme eye states (hard swap to painted
  extremes); using it for blinks is adaptation, not measurement.
- **Ledger day-stamps** (RJ318915 GAP #3; format layer).
  Measured: `SaveData` day / conversation counter fields drive
  recency- and cadence-based conditions. Expected adoption: a
  canonical pattern over existing atoms, with a fixture
  (slice 3); a primitive only if the fixture demands it.
- **Performed-prop minigame seam** (RJ318915 GAP #2; app host).
  Measured: a continuous physical-input minigame (pendulum +
  one balance coefficient). Ruled: the host lives in the
  app, continuous input is reduced to one logged aggregate event
  at a tick boundary, and the tick contract is unchanged. The
  prop's simulation never enters the authored records.
- **SpriteMask sorting-range model** (engine-level study, not a
  game). Unity's 2D mask + sorting-range + `maskInteraction`
  model is the clearest 2D precedent for Torogao's clip-plus-
  order primitive (aperture by occlusion; draw-order role lint).
  Settled in the Ranch's facial-rigging notes (**S** there);
  the transfer is
  direct, being 2D in both systems, with Torogao's own verdict
  recorded in the facial leg's Torogao checks (clip masks
  supported, with named limits).

### What Torogao deliberately does not take

- **No Unity importer.** Neither Unity class gets one (above).
  Any future proposal that reads Unity project files or game
  assemblies *into* a Torogao project contradicts the unified
  map and needs a new ruling, not a converter.
- **No IL2CPP behavioural claims from metadata alone.** The
  census gives the stat model, not the behaviour.
- **No Unity runtime, Editor, or asset format inside Torogao.**
  Unity is a study target and a build/measurement tool for
  Ranch projects that still live in Unity (the flagship adult game's Track B);
  Torogao's own projects never depend on it.

## Daddy Style treatment

Safety > performance > developer experience, applied to Unity's
surfaces. Rules are alphabetical by topic; each names its
evidence or its status as a Ranch rule. Applied to adult
production, none of this softens: explicit content raises the
cost of a sloppy asset pipeline; it does not lower the bar
for one.

- **Assets are untrusted input.** A `.unitypackage`, an FBX, or a
  studied game's bundle is inspected before it is imported
  (`unity assets inspect`), imported only into a scratch copy,
  and censused after import. Studied-game material is never
  imported at all (RE boundary).
- **Bounded work.** Every Editor run has an outer wall-clock
  bound, a named output set, and a log; every CLI call has a
  timeout and a capture cap (Bounds table). An unbounded Editor
  run is the known failure mode in the Ranch's editor setup
  (below), not a style choice.
- **Deterministic converters.** Named, versioned, golden-tested,
  GUID-pinned (Converters section). A conversion that cannot
  state its converter version has not happened yet.
- **Explicit contracts.** A batchmode method validates inputs,
  writes declared outputs, logs `OK <name>` last, and exits
  explicitly (the batchmode contract in this guide). A build
  names its target or profile; a test run names its
  platform/mode.
  "Last used configuration" is a hidden default and is banned:
  the Ranch's agent workers cite the manual that an unspecified
  target loads the
  last used configuration (**D** [A]).
- **No hidden behaviour.** No `--allow-install` side effects, no
  registry reliance, no `-password` on argv, no configuration-
  writing CLI verbs outside staging, no deprecated in-Editor
  MCP server in any server list, no test retries masking flakes
  (`unity test --retries` defaults to 0 at the Ranch;
  the Ranch's agent workers' raw-Editor equivalent: `-retry` is banned in gates,
  `-repeat` is the flake-hunting tool, **D** [A]).
- **No surface shaders; URP for new content.** Owner ruling
  2026-10-19 (see the platform floor note in this guide). A cel look
  needs a custom shader on either pipeline; building it on the
  deprecated pipeline builds it twice.
- **Play-mode state is explicit.** Statics are reset on
  subsystem registration or asserted fresh (**D** [A] mechanism,
  Ranch rule). Domain-reload behaviour is a project setting a
  gate can read, never an assumption.
- **Secrets stay off the command line.** Auth goes through
  `unity auth` interactively; Android signing material goes
  through the Owner, never through a script's argv (the CLI's
  own help warns argv leaks into history and CI logs, **R**).
- **Shutdown crashes are a named outcome.** SHUTDOWN-CRASH is
  recorded with its evidence (outputs verified, log read, exit
  code noted) and counted separately in every report. It is
  never silently reclassified as success — and never as a work
  failure either, because that would send the next run debugging
  the wrong thing.

### Editor-setup wiring (games/unity + games/shared)

Read from the live tree on 2026-11-02, read-only. Proposals go
to the Ranch; the editor setup was not edited.

- **Shape.** `~/.config/nvim/lua/games/unity/` holds `actions`,
  `character`, `commands`, `config`, `init`, `util` (1,006 lines
  total, **S**). Its actions already use the Ranch's batchmode
  argv shape: `-batchmode -nographics -quit -projectPath <root>
  -executeMethod <M> -logFile <path>` (**S**, `actions.lua`
  throughout, e.g. the refresh action at :355).
- **The runner gap, verified with line drift.** The Ranch's
  agent workers reported
  "output.lua:424 no-timeout / :430 exit-code-only" [A]. The
  current tree: the file is the *shared* runner,
  `lua/games/shared/output.lua` (462 lines); line 424 is its
  `vim.system(...)` call (**S**), and the completion callback
  branches on `result.code == 0` a few lines later (**S**,
  :430s). The timer in that file is a *progress* timer
  (`start_progress_timer`), not a wall-clock timeout: no
  timeout option reaches `vim.system` (**S**, grep of the
  file). Verdict: the finding by the Ranch's agent workers stands in substance — no
  wall-clock bound, success decided by exit code alone — with
  the path corrected (shared, not unity-local) and the exact
  second line number drifted. Both halves contradict this
  guide's batchmode contract; the fix (outer timeout + sentinel
  check) is the Ranch's to make.
- **GUI launch exists.** `actions.lua:215` starts the Editor
  with `jobstart({ editor, '-projectPath', root })` (**S**) —
  an Owner-surface convenience, not an agent route.

## USE — agents

This is the summary; the full agent surface is "Agent use"
above. The decision order for any Unity task:

1. Is it outside a project (versions, Editors, registry,
   licenses, package inspection)? → `unity` CLI verb.
2. Is it inside a project and deterministic (census, import,
   build, test, capture)? → `unity build` / `unity test`, or a
   batchmode `-executeMethod` converter on a scratch copy.
3. Does it need a *live* Editor's state? → the broker's read-only
   tools if the Editor is broker-connected; else `unity status`
   / Pipeline verbs if the project carries the package; else
   the answer is "not observable headlessly today" — say so.
4. Is it arbitrary live-Editor mutation (`unity command` /
   `eval`)? → Owner's explicit command for that call, scratch
   project, full run record. Otherwise stop.
5. Is it GUI-ONLY per the census? → Hand it to the Owner by
   name, with the headless verification that will check the
   result afterwards.

## USE — the Owner

Plain version: you almost never need to open Unity to check on
it. The CLI tells you which Editors exist, whether your project
is healthy, and what a build or a census produced — and when you
do run the Editor yourself, you run it in a windowless batch
mode that writes a log you can read afterwards.

Mechanism, briefly: a Unity *project* is a folder whose
`ProjectSettings/ProjectVersion.txt` names its Editor version.
The `unity` CLI reads that file and launches the matching
Editor. Batchmode (`-batchmode`) runs that Editor with no
window; `-executeMethod` calls one static C# method and stops;
`-logFile` decides where the evidence goes. The one trap worth
knowing before any command below: an Editor that did its work
can still crash while shutting down, so you always judge a run
by its log and its output files first and its exit code second.

The worked examples below are the Ranch's everyday ones: a
facial census over a character's blendshape face, a headless
player build of an adult project, and a test run.

First commands (each with its check). Run them in order; the
order carries meaning.

**1. Confirm the CLI and the installed Editors.**

```bash
~/.local/bin/unity version --json
~/.local/bin/unity editors list -i --json
```

Check: the first prints `"version": "1.0.0-beta.13"`; the second
lists exactly `6000.6.6f1` and `7000.0.0a10`, each with a
`location`. (Drop the `-i` and the list also shows versions you
could download — that list is a catalogue, not your machine.)

**2. Verify the build-target Editor is intact.**

```bash
~/.local/bin/unity editors verify 6000.6.6f1 --json
```

Check: `"ok": true`. This is a structural check of the install;
it launches nothing.

**3. See what projects Hub knows, and what is running.**

```bash
~/.local/bin/unity projects list --json
~/.local/bin/unity status --json
```

Check: `projects list` is the registry (a convenience — real
work always names a path). `status` today answers with exit
code 6 and `STATUS_NO_INSTANCES`: no Editor with the Pipeline
package is running. That is a normal, healthy answer, and a
good first lesson in reading the envelope (`success: false`
with a named code) instead of fearing it.

**4. Run the facial census on a scratch copy.** (The full
script and its checks live in the Ranch's facial-rigging
notes, Unity —
USE — the Owner; it ran green in Probe 3.) The shape:

```bash
timeout --kill-after=30s 600s \
  ~/Unity/Hub/Editor/6000.6.6f1/Editor/Unity \
  -batchmode -nographics -projectPath /abs/scratch/proj-copy \
  -executeMethod FaceCensus.Run \
  -logFile /abs/scratch/facial/unity.log -quit; echo "exit=$?"
```

Check: `grep -c 'OK face_census' /abs/scratch/facial/unity.log`
is ≥ 1, and the TSV holds one row per blendshape. A non-zero
`exit=` with both present is a shutdown crash, not a failed
census. An empty TSV with the sentinel present means the
project simply has no blendshape-bearing mesh.

**5. Build headlessly through the CLI.**

```bash
~/.local/bin/unity build /abs/scratch/proj-copy \
  --target StandaloneLinux64 --output-path /abs/scratch/build/out
```

Check: the player exists at the output path and the build log
(default `<project>/Logs/build-<target>-<timestamp>.log`) ends
clean. `StandaloneLinux64` is one of the zero-code targets —
most other targets need `--execute-method` or a build profile
(`unity build --list-targets` shows which, and was run for this
guide).

**6. Run tests through the CLI.**

```bash
~/.local/bin/unity test /abs/scratch/proj-copy \
  --mode EditMode --output /abs/scratch/test-results.xml
```

Check: exit 0 and the NUnit XML exists. Exit 8 means the tests
ran and some failed — read the XML; do not re-run hoping, and
never add `--retries` to a gate.

## UNVERIFIED register

Alphabetical. Each item is marked **U** at its point of use;
the reason names the missing evidence.

- `-consistencyCheck` as a run — the agent workers' citation
  establishes
  the flag's documented purpose (**D** [A]); no run in this leg
  or the facial leg executed it.
- Agent-worker U-1…U-7 (carried from their v0.1) — their drafts
  reference a
  register whose items are not enumerated in the surviving
  v0.2 text; they cannot be settled or even restated from what
  survives. Recorded as lost-with-the-draft, not silently
  dropped.
- Batchmode rendering reliability on the Ranch workstation (Arch, pinned
  NVIDIA ICD) — captures are Ranch-measured on Track B, but
  no systematic reliability claim is verified; the platform is
  off Unity's support matrix.
- Graphics-enhancement pass convention — its text is in
  no staged source (the same finding as the Aseprite leg: a
  grep of the whole workdir finds it only in the brief and the
  Aseprite records). Not invented.
- Editor-exit-code table (raw Editor argv, as opposed to CLI
  exit codes) — citations by the Ranch's agent workers give
  code 1 for batch failure
  / executeMethod failure (**D** [A]); a complete Editor code
  table was not verified against an installed source, and the
  shutdown-crash discipline exists precisely because this
  surface is not trustworthy alone.
- Pipeline package presence in a project carrying the broker's
  bridge package (agent-worker
  U-10), as distinct from Track B — settled negatively for
  the flagship adult game's Track B by manifest (**S**: no `com.unity.pipeline`),
  and the broker's own bridge package is not
  Unity's pipeline; whether any other project on the Ranch workstation
  carries
  `com.unity.pipeline` was not censused.
- Pipeline localhost HTTP authentication (agent-worker U-9) — no
  Editor with the package was running to probe (`unity status`
  reports zero instances, **R**), and the staged CLI pages
  the Ranch's agent workers cited no longer exist on the Ranch
  workstation to re-read. Until
  settled: lab-only, scratch projects, no long-lived pipeline.
- SHUTDOWN-CRASH → CLI exit-code mapping (agent-worker U-8) — no run
  connects the two surfaces; CLI code 6 ("command-specific
  failure", **D** + one **R** instance) is a CLI-surface fact,
  not evidence about an Editor crash under the CLI.
- `unity doctor` / `unity changelog` timing and output shape —
  a combined probe batch containing `doctor --json` did not
  finish inside its window; neither verb was re-probed alone.
  Their existence is **R** (`--help`); their behaviour is **U**.
- Unity 6000.6.7f1 release date and "latest supported" status
  (agent-worker claim) — 6000.6.7f1's existence as an available
  release is **R** (`editors list`, `upgradeTo`); its release
  date (2026-10-21 per the Ranch's agent workers) and support status are web
  claims this leg did not re-verify.
- Unity CLI beta.14's changelog claims (the Ranch's agent
  workers, from beta.14
  release notes) — the Ranch workstation runs beta.13 and the self-update
  check now reports beta.15 as latest (**R**); beta.14's
  notes were not read, and nothing in this guide rests on
  them.
