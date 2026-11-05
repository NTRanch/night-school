# Daddy Style — Unreal Engine

> This is the Ranch's house style guide for Unreal Engine, adapted for adult game production — high-end adult scenes and cinematics, explicit character work, and render pipelines you can trust. It is part of Night School, the Ranch's public study programme.

Full guide for the Ranch's Unreal work. This guide is the operational core and carries the reasoning, the census, and the registers in one place; if a shorter summary elsewhere disagrees with this file, this file wins.

Why Unreal, and why this much discipline around it: the Ranch builds adult games where the selling surface is the character — a face that holds up in close-up, a body whose morph targets behave exactly as authored, a cinematic that renders the same way every time it is queued. Unreal Engine 5.8 gives us the fidelity for that work, and it also gives us a project format that executes code the moment it is opened. Both facts shape everything below. The style is plain first, then mechanism-deep: say what a rule does for the work, then show exactly how it works.

Version basis: **Unreal Engine 5.8.0 source build** at `/opt/Unreal` on the Ranch workstation (**S**: `Engine/Build/Build.version` — Major 5, Minor 8, Patch 0, Branch `UE5`). Drafts by the Ranch's agent workers rest on the upstream 5.8 documentation set and report **5.8.4** as the latest upstream hotfix (forum post dated 2026-10-20 — **A/D**). Epic publishes no per-hotfix docs, so the 5.8 pages apply across 5.8.x; this guide rests on the **installed 5.8.0** wherever a claim is load-bearing and names 5.8.4 only as the reported latest from the Ranch's agent workers. Evidence marks: **R** run-verified on the Ranch workstation 2026-11-02 · **S** static read of an installed file 2026-11-02 · **D** official documentation as cited by the Ranch's agent workers (their staged docs tree no longer exists on the Ranch workstation; the citations cannot be re-read there) · **A** draft claim by the Ranch's agent workers, with attribution · **U** UNVERIFIED. Sections are alphabetical wherever content allows; the workflow runs are sequential by meaning.

## CLI census

On the Ranch, headless comes first. An adult scene, a character import, or a Movie Render Queue pass that can only be produced by clicking through the Editor GUI cannot be gated, repeated, or handed to an agent worker — so every operation below is classified by whether a machine can do it without a human in the viewport. Classes: **CLI-NATIVE** (a binary/flag does it directly), **SCRIPTABLE-HEADLESS** (`UnrealEditor-Cmd` commandlet or `-run=pythonscript`), **GUI-ONLY** (honest negative — no headless route; the Ranch's editor broker or the Owner's hands). Rows alphabetical.

| Operation class | Class | Exact route |
|---|---|---|
| Automation tests (framework) | SCRIPTABLE-HEADLESS | `UnrealEditor-Cmd <proj> -ExecCmds="Automation RunTests <filter>; Quit" -TestExit="Automation Test Queue Empty" -nullrhi -unattended -abslog=<log>` (**D** [A] shape; the staged page for the CLI invocation was missing in the workers' set, so the exact invocation stays **U** — see register) |
| Build / compile project code | CLI-NATIVE | `RunUAT.sh BuildCookRun -build …` or `Engine/Build/BatchFiles/RunUBT.sh` (**D** [A]); per-flag semantics **U** |
| Cook content | SCRIPTABLE-HEADLESS | `UnrealEditor-Cmd <proj> -run=cook -targetplatform=<Plat>` (**D** [A]); legacy platform names on the doc page are **U** for 5.8 — confirm against the installed build before relying on one |
| Editor Python (censuses, imports, edits) | SCRIPTABLE-HEADLESS | `UnrealEditor-Cmd <proj> -run=pythonscript -script=<file> -nullrhi -unattended -stdout -abslog=<log>` (**R**: facial Probe 4 PASS; this leg's probes PASS — see `unreal-cli.md`). The commandlet does not automatically load levels (**D** [A]) |
| Gauntlet tests | SCRIPTABLE-HEADLESS | UAT Gauntlet (**D** [A]); the doc's own `MaxDuration` example arithmetic disagrees with its comment — the unit is **U**; set bounds explicitly |
| MCP server start (downstream) | CLI-NATIVE | `-ModelContextProtocolPort=N` overrides the port; console `ModelContextProtocol.StartServer [port]`; config `bAutoStartServer` default false (**S**, the broker surface record §2). The Ranch's agent workers also cite a `-ModelContextProtocolStartServer` startup flag (**D** [A]) |
| Movie Render Queue renders | SCRIPTABLE-HEADLESS | MRQ commandlet route (**D** [A]); the exact headless MRQ CLI flags are **U** in the workers' staged pages |
| Package (build + cook + stage + pak) | CLI-NATIVE | `RunUAT.sh BuildCookRun -project=<proj> -noP4 -platform=<Plat> -cook -build -stage -pak -archive -archivedirectory=<out>` (**D** [A] pipeline shape; the Ranch's editor setup invokes the same command — **S**, `games/unreal/actions.lua` `package_project`) |
| Plugin packaging | CLI-NATIVE | `RunUAT.sh BuildPlugin` (**S**: the Ranch's editor setup `package_plugin` action) |
| Project files generation | CLI-NATIVE | `GenerateProjectFiles.sh <proj>` (**S**: engine tree + the Ranch's editor setup action) |
| Resave / world-partition builders | SCRIPTABLE-HEADLESS | Builder commandlets, e.g. resave with `-ActorClass=` filters (**D** [A]) |
| Blueprint graph authoring (visual) | GUI-ONLY | No headless authoring route. Downstream MCP exposes `write_graph_dsl` (execute-class, default-deny via the Ranch's editor broker). Named plainly: visual Blueprint editing is GUI work |
| Control Rig graph authoring | GUI-ONLY | Rig graphs are asset data edited in the Editor; no verified headless route (**U** for any scripted path) |
| Level / viewport composition | GUI-ONLY | Placing and framing in the viewport is GUI work; actor transforms are scriptable via Python once a level is loaded, but composition judgement is the Owner's eye (the visual gate: state what SHOULD be seen, compare seen vs should) |
| Material graph authoring (visual) | GUI-ONLY | Node-graph editing is GUI work; material *parameters* are scriptable |
| MetaHuman assembly | GUI-ONLY | MetaHuman Creator/assembly is GUI + content-side; internals **U** (facial register) |
| Niagara authoring (visual) | GUI-ONLY | Emitter/module graphs are GUI work |

Bounded-work rules for every headless route: outer wall-clock `timeout` wrapper (no Unreal route in this census carries a trustworthy internal bound); single-process cooks for gates (multi-process cook can report false success — **D** [A]); `-nullrhi` whenever nothing renders; `-abslog` always, because the log is the evidence.

## Determinism and converters (CODE-FIRST)

Adult content pipelines live or die on repeatability. When a character's morph set, a scene's lighting, or a rendered cinematic changes between runs for no authored reason, there is no gate — only vibes. So conversion between the code form and Unreal's form must be specified and deterministic: named, versioned converters, golden tests, deterministic IDs where the format has them. The converter set this guide names (alphabetical; each is a specification, and the golden suite below is its gate — the suite as a suite was **not run** by this leg and is stated as a specification):

- **uasset-census v1** — Editor Python census (assets → canonical JSON/TSV: path, class, GUID, morph/property facts). Rests on the **R**-verified pythonscript route (facial Probe 4 shape). This is how the Ranch proves a character asset actually carries the morph targets an explicit scene depends on, instead of discovering a missing target at render time.
- **fbx-to-uasset v1** — FBX import with a pinned import-data record (`bImportMorphTargets` explicit — **S**, `FbxSkeletalMeshImportData.h:89-91`); re-import of the same FBX with the same record must yield the same asset census.
- **uasset-to-gltf v1** — export for the sprite-to-3D factory / Torogao consumption; the census, not the binary, is the equivalence record where byte-determinism does not hold.
- **Deterministic GUIDs:** a converter never accepts a fresh random package GUID per run; the GUID is derived from the canonical asset path under a named seed rule and recorded in the census, so two runs over the same inputs produce the same census bytes.
- **Simulation determinism:** no documentation guarantees bit-identical simulation (**D** [A]). Fixed timestep and manual substepping are inputs; the claim a build may make is only the measured one (same inputs → same recorded outputs across N runs on the named machine), never an asserted one.

Golden suite (half validation / half adversarial, per the Ranch's test split): validation — census of a known skeletal mesh returns its morph list verbatim; FBX re-import reproduces the census; package of the scratch template stages the declared outputs; pythonscript success sentinel present. Adversarial — a raising script must exit non-zero and leave no success sentinel (**R** this leg); a project carrying an `init_unreal.py` must be refused by preflight, never opened; a cook with a deliberately broken asset must fail the log-and-outputs gate even if the exit code is 0; an unclassified downstream MCP tool must be refused by the Ranch's editor broker's class table.

## Editor wiring (the stub's three items, resolved)

The Ranch works editor-first, so the guide records honestly what the Ranch's editor setup can and cannot do with Unreal. The surviving fragment of a lost first-set package (an Unreal engine report stub drafted by the Ranch's agent workers) named three UNVERIFIED items about the editor setup's `games/unreal` module. All three are resolved by static read this leg (**S**, the editor config's `lua/games/unreal/` + `lua/dap/unreal.lua`):

1. **UAT BuildCookRun with no timeout — CONFIRMED as stated.** `grep -rn timeout` over all six `games/unreal/*.lua` files returns no hits; `package_project` and `cook_only` invoke `RunUAT BuildCookRun …` / `-cook` through the shared `output.run_with_progress` with no wall-clock bound. (The module's engine-*bootstrap* action does bound itself — `ENGINE_BOOTSTRAP_TIMEOUT_MS` via `run_bounded` — which makes the packaging path's missing bound a plain inconsistency.) Rule: until the editor lane adds a bound, every caller wraps UAT in an outer `timeout`. This is a finding for the editor lane; this leg changed nothing in the live config.
2. **GUI editor path only — CONFIRMED.** `config.lua:52-59`: `editor_binary()` returns the GUI `UnrealEditor` on every platform (Linux line 59: `Engine/Binaries/Linux/UnrealEditor`). The module contains no `UnrealEditor-Cmd`, `-run=pythonscript`, `-nullrhi`, or `-unattended` route (re-verification by the Ranch's agent workers, corroborated by this leg's reads). The headless routes in this guide are therefore terminal routes, not editor routes.
3. **DAP lldb/gdb editor-native — CONFIRMED, keep.** `lua/dap/unreal.lua` defines adapters `lldb` (default) and `gdb` (`UnrealDapAdapter 'lldb'|'gdb'`, :68-69, :93), resolving `lldb-dap` / `gdb` executables (:577-607). Native debugging of the Editor is editor-native tooling, correctly kept as-is.

## Facial cross-reference

For adult work the face is the product. A heroine's expression set — the morph targets that carry arousal, reaction, and character in close-up — is authored and measured against the Ranch's facial-rigging notes, never improvised per scene. Built on the Ranch's facial-rigging notes (Unreal Engine section, nine subsections) and `VERIFY-facial.md`; cited, never re-derived. Settled there: the morph census API and its 63-name result (**R** Probe 4); `UMorphTarget` (**S** `MorphTarget.h:227`); `SetMorphTarget` signature (**S** `SkeletalMeshComponent.h:1347`); curve→morph **name matching** (**S** `AnimCurveTypes.h:32`, `AnimInstanceProxy.cpp:3597-3625`, `SkeletalMeshComponent.cpp:3383-3405`); `bImportMorphTargets` (**S** `FbxSkeletalMeshImportData.h:89-91`); `UPoseAsset` (**S** `PoseAsset.h:311-315`); the ARKit 52-channel count. Carried **U** from there, honestly: Control Rig lid constraints and Control Rig → morph driving (rig-graph content is asset data, not headers); render-level singularity (needs a render probe); eye-material translucency sort (production eye materials are content-side, none ship in the tree read); MetaHuman internals (binary DNA payloads); the MetaHuman ARKit mapping pose asset; Live Link Face app details (external iOS app). The Prima avatar rig v2 takes are **not** Owner-approved (corrected 2026-11-02 08:49 PST) and are cited nowhere here as a reference.

## RE alignment

The Ranch studies shipped games to learn how their scenes, characters, and cinematics were built, then rebuilds those techniques cleanly for its own adult productions. Study law: **static RE only — nothing executed.** For Unreal that law bites harder than for any other engine in this programme, because of the auto-run contract (below): a studied game's project, and any extracted Editor content, is never opened in the Editor. The study surface is files: `.uasset` / `.umap` bytes read statically, cooked-content listings, string and class censuses taken without loading the project.

What Torogao (the singular build engine) adopts, adapts, or improves from Unreal, per the Ranch's unified engine map — Unreal is the map's **eighth engine class** (the census row-41 line): animation (AnimBP/state-machine layering, curve-driven morphs by name, pose assets), asset pipeline (Interchange-style importer records; the pinned-import-record discipline above), build pipeline (UAT's staged build/cook/stage/pak separation, adopted as *stage separation with per-stage gates*, not as UAT itself), MCP/editor brokering (the Ranch's editor broker's class-table + decide() pattern is the Ranch's reference broker shape), and rendering (MRQ-style offline render queues as the model for deterministic gate renders — the same discipline the Ranch uses when an adult cinematic has to come out of Movie Render Queue identical on every pass). Source engines are study targets only; nothing here makes Unreal a build dependency of Torogao.

Where an asset pipeline is described, the **graphics-enhancement pass convention** applies as an obligation: enhancement is a named, separate pass over studied assets, never silently folded into extraction. (As in the Aseprite and Unity legs, the convention text itself is not staged anywhere this leg could read; it is recorded as an obligation, not invented.)

## Daddy Style treatment

Safety > performance > developer experience; explicit contracts; bounded work; no hidden behaviour. In an adult pipeline these are not abstractions: safety is refusing to execute an untrusted project that ships with a scene you want to study; bounded work is a render queue that cannot run away overnight; no hidden behaviour is a character import that changes nothing the census did not declare.

- **Auto-run contract (first-class).** Project Python/startup scripts auto-run on project load: `init_unreal.py` and plugin `Content/Python/` scripts execute when the Editor opens the project (engine-plugin side **R**-corroborated, facial Probe 4; project-level **A**). Therefore: project content is executable; studied projects are never opened; Ranch projects are opened headless only from preflighted scratch copies; the preflight (no `init_unreal.py`, no unvetted plugin Python) is part of the run record, not a courtesy.
- **Bounded work.** Every Editor/UAT invocation carries an outer wall-clock bound set by the caller; batch sizes (assets per census run, maps per cook) are named in the run record; Gauntlet's own duration setting is set explicitly because its documented unit is **U**.
- **Explicit contracts.** A headless run's contract is: named project copy, named script, named log, named outputs, named sentinel. A run missing any element is not a gate run.
- **No hidden behaviour.** No auto-start MCP server in Ranch projects (`bAutoStartServer` stays false outside a lab session); no `unity`-style client-config writers — the Epic client-config generator writes `.mcp.json`-class files and is treated as a live-tree change needing the Owner's approval; deterministic alternatives are preferred over GUI state wherever they exist.
- **Exit-code discipline.** See this guide's census and CLI companion: log + outputs + hashes gate; the exit code is supporting evidence only. RunUAT BuildCookRun in particular is judged by its log and its staged outputs, never by its exit code alone — a clean exit with a thin archive is a failed package.

## USE — agents via the Ranch's editor broker / GUI

Agent workers do not drive the Unreal Editor GUI directly. They go through the Ranch's editor broker, and the broker's contract is the whole point: it is the only agent GUI route for Unreal, it observes before it acts, and anything that can execute code is denied by default.

The broker is deployed on the Ranch workstation as a local broker binary with a broker config file (0600) (**S**): a born-modern rmcp broker fronting UE 5.8's built-in MCP server at `http://127.0.0.1:8123/mcp` (downstream timeout 30 s), token auth at the broker (agent + operator token digests in the config — values never read into this guide), acquisition enabled with a quarantine dir, and an append-only op log in the broker's local share directory. Lab-only.

The downstream reality the broker fronts (**S**, the broker surface record): Epic's MCP is an in-Editor plugin (Experimental, `EnabledByDefault: false`) hosting a Streamable-HTTP server inside the Editor process — it exists only while an Editor with the plugin enabled runs; the broker does not start the Editor. The plugin has **no auth of its own** and speaks legacy protocol eras only (2025-11-25 and older); the broker bridges eras and adds the token + decide() layer. Default Epic port is 8000; the Ranch's lab runs on **8123** from project config. With tool search enabled (default), `tools/list` returns 3 meta-tools and all real tools are reached through `call_tool`; downstream tool lookup is case-insensitive, so the broker matches its class table case-insensitively and dispatches canonical casing. The full-catalog lab census measured **52 toolsets / 830 tools**, classified **395 read / 409 write / 26 execute / 0 unclassified**; registration is not atomic (toolsets can appear minutes after the server answers), so the broker rebuilds its surface per downstream session.

The GUI ladder, and what each rung may do:

- `gui.observe` (read) — broker frame + geometry, window identity, blank-frame verdict. Observation changes nothing.
- `gui.ground` (read) — a natural-language target → bounding box + derived centre point. Grounding changes nothing.
- `gui.act_verified` (actuate) — act, then verify against the expected post-state; anchored/full-frame checks, strategy-changing retries, window pinning. This is the only GUI write path, and it is verified by construction.
- Execute-class downstream tools (code execution, arbitrary file write, Python tool scripts, PIE sessions that run project logic) are **default-deny via decide()** and are not reachable through the GUI ladder at all.
- The broker op-log tool reads back the append-only op log — the log is the record of GUI work, exactly as the run record is the record of headless work. `code.feedback` (read) closes the loop with the Ranch's diagnostics tooling (editor diagnostics, lint, and format verdicts); it has no write path.

Capture/verification discipline for GUI work (the visual gate): state what SHOULD be seen before acting, capture from the final surface at a size a person actually views, compare seen vs should per item. A screenshot without the expected-vs-seen statement is not evidence — for adult scene work that means naming the expected framing, character state, and morph/expression state before the capture, not admiring whatever came out. This leg launched no Editor GUI and acquired nothing, per its bounds; the ladder above is verified against the deployed binary/config and the surface record, and a live ladder run stays a lab-session act, not a guide claim.

## USE — the Owner

Plain version first: Unreal on the Ranch workstation is a source build you drive from the terminal. You almost never need to open the Editor GUI to get Ranch work done — censuses of a character's morph targets, imports of a new heroine model, cooks, packages, and queued renders for adult cinematics all run headless — and you should treat any Unreal project you did not write the way you treat an unknown binary, because opening it runs its Python.

Mechanism level:

1. **Know your version.** `cat /opt/Unreal/Engine/Build/Build.version` → 5.8.0. A project's `.uproject` names its `EngineAssociation`; a mismatch means the project wants a different engine than the one installed.
2. **Copy before you open.** Make a scratch copy (`.uproject` + `Config/` + needed `Content/`), then check it: `find <scratch> -name init_unreal.py` must return nothing you did not write, and plugin `Content/Python/` folders get the same look. Only then may the Editor touch it.
3. **Run the census route.** The `UnrealEditor-Cmd … -run=pythonscript` command in `unreal-cli.md`. Verify three things: exit 0, the log line `Python script executed successfully`, and your script's own sentinel/output file. Any one missing = the run did not do what you asked, whatever the others say.
4. **Package through UAT**, judging by the log and the staged tree under the archive directory — a 0 exit with a thin archive is a failed package (multi-process cook's false success is the documented shape of this trap; gate cooks run single-process).
5. **GUI work is broker work** (agents) or your own hands. There is no third route on the Ranch, and no route at all that involves opening a studied game's project.

## UNVERIFIED register

Alphabetical; each item names the missing evidence. An honest register is part of the style: a claim the Ranch cannot yet prove — about a render flag, a rig path, or a cook behaviour an adult production is about to depend on — sits here in the open instead of hardening into folklore.

- Automation-test CLI invocation (exact `-ExecCmds` form) — the staged doc page was missing from the workers' set.
- Control Rig → morph driving and lid constraints — facial register; rig graphs are asset data.
- Graphics-enhancement pass convention text — not staged anywhere readable; recorded as an obligation only.
- Downstream toolset read-only classification per shipped toolset — the docs do not classify them (per the Ranch's agent workers); the Ranch's editor broker's class table is the operative classification instead.
- Eye-material translucency sort; render-level singularity — facial register; need content-side materials / a render probe.
- Gauntlet `MaxDuration` unit — the doc example contradicts itself.
- Headless MRQ CLI flags — UNVERIFIED in the workers' staged pages.
- Legacy cook platform names for 5.8 — doc page predates 5.8 naming; confirm per build.
- Live Link Face app details; MetaHuman ARKit mapping pose asset; MetaHuman internals — facial register.
- Multi-process cook false-success fix status in 5.8 — the cited page says UE 5.4.
- Offscreen (`-nullrhi`-off) render behaviour on the Ranch workstation — this leg ran `-nullrhi` only; no render probe.
- Project-level `init_unreal.py` auto-run as a *run* — the engine-plugin side is **R**-corroborated (Probe 4); the project-level claim rests on **A** + the preflight discipline it justifies either way.
- Simulation bit-determinism — no doc guarantees it; measured claims only.
- UAT BuildCookRun per-flag semantics and the full UAT / commandlet exit-code tables — the workers' register; this leg measured only the pythonscript success/failure pair.
