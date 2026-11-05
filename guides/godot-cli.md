# Godot CLI reference

> **Night School — Daddy Style: Godot CLI reference.** This is the Ranch's house reference for driving Godot from the terminal, adapted for adult game production — headless imports, checks, and exports for adult visual novels and adult game builds. Part of Night School, the Ranch's public study programme.

Version basis: **Godot 4.7.2.stable** (Arch package `godot 4.7.2-2`,
binary `/usr/bin/godot`, 182,015,704 bytes). `--version` prints
`4.7.2.stable.arch_linux.ed1daf0bf` and exits 0 (run-verified 2026-11-02).
`--help` was captured from the installed binary on 2026-11-02 (log
`help.txt` in the leg's scratch tree, `scratch-godot/logs/` in the
engine-daddy-guides workdir): 129 lines, **95 unique long flags**. Every
flag row in the table below is in that capture, and the table and the
capture were diffed by flag name (exact match).

Evidence legend (the **Src** column), identical across this package:

- **B**: present in the `--help` capture from `/usr/bin/godot`
  4.7.2.stable on 2026-11-02.
- **R**: run-verified on 2026-11-02 by a bounded headless probe on a
  scratch copy (probe logs in `scratch-godot/logs/`).
- **S**: statically verified on 2026-11-02 by reading an installed or
  generated file (named at use). Nothing executed.
- **D**: stated in official Godot documentation or a Ranch staged
  source (named at use). Not confirmed by **B**, **R**, or **S**.
- **U**: UNVERIFIED. No source settles it.

Census legend (the **Class** column), per the brief:

- **CLI-NATIVE**: a flag does the whole job.
- **GUI-ONLY**: no terminal route.
- **SCRIPTABLE-HEADLESS**: needs a GDScript run with `--headless
  --script`.

A **[no-automation]** mark means the flag is terminal-reachable but
interactive, unsafe, or crash-prone on this build, so it is banned from
pipelines.

Build-availability letters from `--help` (**B**): **R** = all builds
(editor, debug and release templates); **D** = editor + debug templates;
**X** = editor builds and templates built with
`disable_path_overrides=false`; **E** = editor builds only. This binary
is an editor build, so every flag below exists here; an exported
project's template binary accepts only its letters.

## Argv safety rules

- **Absolute paths for `--path`, export outputs, and `--log-file`.**
  `--path` to a missing directory aborts with exit 1 (**R**:
  `Invalid project path specified: "…", aborting.` printed to stdout).
- **Argv arrays** (one element per argument), never shell strings.
- **No secrets in argv.** `--remote-fs-password <password>` puts a
  password on the command line, where any local process list shows it.
  It is **[no-automation]** in this Ranch.
- **User arguments go after `--` (or `++`)** and are read back with
  `OS.get_cmdline_user_args()` (**B**). Engine arguments after `--` are
  not parsed as engine flags.
- **Unknown flags do not fail fast.** Run-verified 2026-11-02:
  `godot --headless --definitely-not-a-flag` printed the engine header
  and kept running until the 15 s `timeout` killed it (exit 124). A
  pipeline that mistypes a flag therefore hangs, not errors — one more
  reason every run carries a deadline and a sentinel (see the exit
  contract).

## Canonical argv shapes

Alphabetical by purpose. Shapes marked **R** were exercised by run on
2026-11-02 (probe logs in `scratch-godot/logs/`).

```bash
# API dump for GDExtension bindings (writes extension_api.json in cwd) [R]
godot --headless --dump-extension-api

# Check one script for parse errors, run nothing [R]
godot --headless --path /abs/proj --check-only --script res://scripts/tool.gd

# Documentation dump (target directory must already exist) [R]
godot --headless --doctool /abs/existing/dir

# Export a data pack only (no template needed) [R]
godot --headless --path /abs/proj --export-pack "Linux/X11" /abs/out/game.pck

# Export a runnable build (needs export templates installed) [R: fails
# on the Ranch workstation today, templates absent — see "Export reality on the Ranch workstation"]
godot --headless --path /abs/proj --export-release "Linux/X11" /abs/out/game.x86_64

# Import pass: scan the project, import new/changed assets, quit [R]
godot --headless --path /abs/proj --import

# Run the project's main scene headless, bounded by the script's quit [R]
godot --headless --path /abs/proj

# Run an exported pack standalone [R]
godot --headless --main-pack /abs/out/game.pck

# Run a SceneTree tool script; require its OK sentinel [R]
godot --headless --path /abs/proj --script res://scripts/tool.gd

# Version probe (10 s, 4 KiB stdout cap) [R]
godot --version
```

## Exit-code and output contract

All items **R** on 2026-11-02 unless marked otherwise.

- **A zero exit is necessary but not sufficient.** A SceneTree script
  that reaches `quit(0)` exits 0; the runner still requires the script's
  `OK <job>` sentinel on stdout and verifies every promised output.
- **Exit codes propagate exactly.** `SceneTree.quit(3)` in a `--script`
  run exited 3; `get_tree().quit(7)` in a main-scene `_ready()` exited
  7 — including when the scene ran from an exported pack via
  `--main-pack`.
- **Parse errors exit 1.** A syntax-broken script under `--check-only`
  and under `--script` both exited 1, with
  `SCRIPT ERROR: Parse Error: …` on **stderr**.
- **A missing script exits 1** (`Attempt to open script '…' resulted in
  error 'File not found'`, stderr).
- **A missing project directory exits 1** (message on stdout).
- **Runtime errors in a SceneTree `_init()` do NOT exit.** The error
  prints to stderr (`SCRIPT ERROR: Invalid call. …`), the function
  aborts before `quit()` runs, and the engine keeps idling until killed
  — exit 124 came from `timeout`, not from Godot. This is the single
  most important exit-code fact in this reference: **a headless script
  that errors can hang forever.** Mitigations, in order: deadlines on
  every run; structure tool scripts so `quit()` is reached on every
  path (`MainLoop._process` returning `true`, or a deferred quit); and
  treat any `SCRIPT ERROR` on stderr as failure regardless of exit.
- **Export without `export_presets.cfg` exits 1**, with
  `ERROR: This project doesn't have an 'export_presets.cfg' file at its
  root.` on stderr.
- **Export of a runnable build without templates exits 1**, naming the
  expected template paths on stderr (see "Export reality on the Ranch workstation").
  `--export-pack` with the same preset exits 0: a data pack needs no
  template.
- **Crashes are exits too.** Headless `--write-movie` crashed with
  signal 11 on this build (shell-reported exit 134 through the crash
  handler / `timeout` core-dump path) and left a 0-byte movie file.
  Any exit ≥ 128, or a core-dump line on stderr, is a crash failure.
- **Stderr is part of the verdict.** Successful probes still printed
  leak warnings on stderr at exit in dummy-rendering contexts
  (`ObjectDB instances were leaked at exit`, RID allocation leaks).
  The Ranch rule: `SCRIPT ERROR` or `ERROR:` lines fail the run;
  leak *warnings* after a completed sentinel are recorded, not fatal —
  but they are recorded, never silently dropped.

## Export reality on the Ranch workstation

Run-verified 2026-11-02, on the scratch project with a hand-written
`Linux/X11` preset:

| Route | Result |
| ----- | ------ |
| `--export-release "Linux/X11" <out>` | Exit 1. `No export template found at the expected path: /home/owner/.local/share/godot/export_templates/4.7.2.stable/linux_debug.x86_64` (and the `linux_release.x86_64` twin) |
| `--export-pack "Linux/X11" <out>.pck` | Exit 0. Wrote a 13,212-byte PCK (SHA-256 in `REPORT-godot.md`); the pack stores imported artifacts (`.ctex`, `.sample`) and **compiled** scripts (`.gdc`), not `.gd` sources |
| `--headless --main-pack <out>.pck` | Exit 7 — the pack's main scene ran headless and its `quit(7)` propagated |

No export templates are installed on the Ranch workstation: the directory
`~/.local/share/godot/export_templates/` does not exist (**S**, `ls`,
2026-11-02). Installing templates is a download and is out of this
guide's scope; until the Owner installs them, **runnable exports are
not possible on the Ranch workstation and data packs are the only export route.**
`--export-debug`, `--export-patch`, and `--install-android-build-template`
share the template dependency and are marked **U** for behaviour until
templates exist (their failure mode is expected to match
`--export-release`'s, but that expectation is not a verification).

## Flag table (alphabetical)

Debugger, display, and run flags that only make sense with a window or
an interactive session are classed CLI-NATIVE **[no-automation]** where
they are terminal-reachable but banned from pipelines.

| Flag | Class | Effect | Src |
| ---- | ----- | ------ | --- |
| `--`, `++` | CLI-NATIVE | Separator: following args are user args (`OS.get_cmdline_user_args()`) | B |
| `--accessibility <mode>` | CLI-NATIVE [no-automation] | Accessibility mode (`auto`/`always`/`disabled`) | B |
| `--accessibility-driver <driver>` | CLI-NATIVE [no-automation] | Accessibility driver (`accesskit`, `dummy`) | B |
| `--accurate-breadcrumbs` | CLI-NATIVE [no-automation] | Force barriers between Vulkan breadcrumbs (GPU debugging) | B |
| `--always-on-top` (`-t`) | CLI-NATIVE [no-automation] | Request an always-on-top window | B |
| `--audio-driver <driver>` | CLI-NATIVE | Audio driver (`PulseAudio`, `ALSA`, `Dummy`). `--headless` selects `Dummy` | B; R (census probe: `Dummy` under `--headless`) |
| `--audio-output-latency <ms>` | CLI-NATIVE | Override audio output latency (default 15 ms) | B |
| `--benchmark` | CLI-NATIVE | Benchmark the run and print timing | B |
| `--benchmark-file <path>` | CLI-NATIVE | Benchmark and save JSON to an absolute path | B |
| `--breakpoints` (`-b`) | CLI-NATIVE [no-automation] | Breakpoint list `source::line,…` for the debugger | B |
| `--build-solutions` | CLI-NATIVE | Build scripting solutions (C#). Implies `--editor`; needs a valid project | B |
| `--check-only` | CLI-NATIVE | With `--script`: parse only, run nothing. Exit 0 clean, 1 on parse error | B; R |
| `--convert-3to4 [max_file_kb] [max_line_size]` | CLI-NATIVE [no-automation] | Convert a Godot 3.x project to 4.x **in place**. Destructive to the source tree: run only on a copy, never in a pipeline against an original | B |
| `--dap-port <port>` | CLI-NATIVE [no-automation] | GDScript Debug Adapter Protocol port (editor) | B |
| `--debug` (`-d`) | CLI-NATIVE [no-automation] | Local stdout debugger | B |
| `--debug-avoidance` | CLI-NATIVE [no-automation] | Show navigation avoidance debug visuals (debug builds) | B |
| `--debug-canvas-item-redraw` | CLI-NATIVE [no-automation] | Highlight canvas-item redraws (debug builds) | B |
| `--debug-collisions` | CLI-NATIVE [no-automation] | Show collision shapes when running (debug builds) | B |
| `--debug-navigation` | CLI-NATIVE [no-automation] | Show navigation polygons (debug builds) | B |
| `--debug-paths` | CLI-NATIVE [no-automation] | Show path lines (debug builds) | B |
| `--debug-server <uri>` | CLI-NATIVE [no-automation] | Start the editor debug server | B |
| `--debug-stringnames` | CLI-NATIVE | Print all `StringName` allocations at quit (debug builds) | B |
| `--delta-smoothing <enable>` | CLI-NATIVE | Enable/disable frame delta smoothing | B |
| `--disable-crash-handler` | CLI-NATIVE | Disable the crash handler where supported | B |
| `--disable-render-loop` | CLI-NATIVE | Render only when called explicitly from script | B |
| `--disable-vsync` | CLI-NATIVE | Force vsync off (does not override driver enforcement) | B |
| `--display-driver <driver>` | CLI-NATIVE | Display driver (`x11`, `wayland`, `headless`) with its rendering drivers | B; R (`headless` → `DisplayServer.get_name() == "headless"`) |
| `--doctool [path]` | CLI-NATIVE | Dump the engine API reference as XML into an **existing** directory. A nonexistent target exits 1 (`Argument supplied to --doctool must be a valid directory path.`) | B; R (6.8 MB dump into a pre-created directory) |
| `--dump-extension-api` | CLI-NATIVE | Write `extension_api.json` (6,965,061 bytes here) into the current directory | B; R |
| `--dump-extension-api-with-docs` | CLI-NATIVE | Same dump with documentation strings | B |
| `--dump-gdextension-interface` | CLI-NATIVE | Write `gdextension_interface.h` into the current directory | B |
| `--dump-gdextension-interface-json` | CLI-NATIVE | Write `gdextension_interface.json` into the current directory | B |
| `--editor` (`-e`) | CLI-NATIVE [no-automation] | Start the editor instead of running the scene. The Ranch's headless editor-shaped routes are `--import`, `--doctool`, and the dumps — not a bare editor launch | B |
| `--editor-pseudolocalization` | CLI-NATIVE [no-automation] | Pseudolocalization for editor/project manager | B |
| `--export-debug <preset> <path>` | CLI-NATIVE | Export a debug build. Template-dependent; behaviour **U** on the Ranch workstation (no templates) | B; U (behaviour) |
| `--export-pack <preset> <path>` | CLI-NATIVE | Export data only; `.pck` or `.zip` by extension. Needs a preset, **not** templates | B; R (exit 0) |
| `--export-patch <preset> <path>` | CLI-NATIVE | Export a patch pack (changed files only); see `--patches` | B; U (behaviour) |
| `--export-release <preset> <path>` | CLI-NATIVE | Export a release build. Needs templates | B; R (exit 1, templates absent) |
| `--extra-gpu-memory-tracking` | CLI-NATIVE [no-automation] | Extra Vulkan memory tracking; `--help` itself warns it may crash some systems | B |
| `--fixed-fps <fps>` | CLI-NATIVE | Force fixed FPS; disables real-time synchronization. Forced by `--write-movie` | B |
| `--frame-delay <ms>` | CLI-NATIVE | Simulate CPU load per frame. Not an FPS limiter | B |
| `--fullscreen` (`-f`) | CLI-NATIVE [no-automation] | Request fullscreen | B |
| `--gdextension-docs` | CLI-NATIVE | With `--doctool`: dump the project's GDExtensions instead of the engine API | B |
| `--gdscript-docs <path>` | CLI-NATIVE | With `--doctool`: generate docs from GDScript inline documentation under `<path>` | B |
| `--generate-spirv-debug-info` | CLI-NATIVE [no-automation] | SPIR-V debug info for RenderDoc (Vulkan) | B |
| `--gpu-abort` | CLI-NATIVE [no-automation] | Abort on graphics API usage errors (debug builds) | B |
| `--gpu-index <device_index>` | CLI-NATIVE | Select GPU (Forward+/Mobile only) | B |
| `--gpu-profile` | CLI-NATIVE [no-automation] | Print a GPU task profile | B |
| `--gpu-validation` | CLI-NATIVE [no-automation] | Enable graphics validation layers | B |
| `--headless` | CLI-NATIVE | `--display-driver headless --audio-driver Dummy`. The Ranch default for every automated run | B; R |
| `--help` (`-h`) | CLI-NATIVE | Print help; exits 0 | B; R |
| `--ignore-error-breaks` | CLI-NATIVE [no-automation] | Debugger: do not break on errors | B |
| `--import` | CLI-NATIVE | Start the editor, import resources, quit. Exit 0 on the scratch project | B; R |
| `--install-android-build-template` | CLI-NATIVE | Install the Android build template (with an export flag) | B; U (behaviour) |
| `--language <locale>` (`-l`) | CLI-NATIVE | Locale (two-letter code) | B |
| `--log-file <file>` | CLI-NATIVE | Write the log to a path (absolute, or relative to the project) instead of the default | B |
| `--lsp-port <port>` | CLI-NATIVE [no-automation] | GDScript Language Server Protocol port (editor). Recommended range 1024–49151. A live LSP session was not exercised; see the UNVERIFIED register in the full guide | B; U (session) |
| `--main-loop <main_loop_name>` | SCRIPTABLE-HEADLESS | Run a `MainLoop` global class instead of the default scene tree | B |
| `--main-pack <file>` | CLI-NATIVE | Load and run a `.pck` pack | B; R (exported pack ran; exit 7 propagated) |
| `--max-fps <fps>` | CLI-NATIVE | Cap FPS (0 = unlimited) | B |
| `--maximized` (`-m`) | CLI-NATIVE [no-automation] | Request a maximized window | B |
| `--no-docbase` | CLI-NATIVE | With `--doctool`: do not dump base types | B |
| `--no-header` | CLI-NATIVE | Suppress the version/rendering header on startup | B |
| `--patches <paths>` | CLI-NATIVE | Comma-separated patch list for `--export-patch` | B |
| `--path <directory>` | CLI-NATIVE | Project directory (must contain `project.godot`). Missing directory exits 1 | B; R |
| `--position <X>,<Y>` | CLI-NATIVE [no-automation] | Request window position | B |
| `--print-fps` | CLI-NATIVE | Print FPS to stdout | B |
| `--profiling` | CLI-NATIVE [no-automation] | Script-debugger profiling | B |
| `--project-manager` (`-p`) | GUI-ONLY | Starts the GUI project manager. No headless equivalent exists or is needed | B |
| `--quiet` | CLI-NATIVE | Silence stdout messages; errors still print | B |
| `--quit` | CLI-NATIVE | Quit after the first iteration | B |
| `--quit-after <int>` | CLI-NATIVE | Quit after N iterations (0 disables). The bound that keeps a scene run finite | B; R (pack run) |
| `--recovery-mode` | CLI-NATIVE [no-automation] | Editor recovery mode (disables tool scripts, plugins, GDExtensions) | B |
| `--remote-debug <uri>` | CLI-NATIVE [no-automation] | Remote debugger endpoint | B |
| `--remote-fs <address>` | CLI-NATIVE [no-automation] | Remote filesystem (debug builds) | B |
| `--remote-fs-password <password>` | CLI-NATIVE [no-automation] | Remote-filesystem password **in argv**. Banned: secrets never ride argv | B |
| `--render-thread <mode>` | CLI-NATIVE | Render thread mode (`safe`, `separate`; `unsafe` deprecated) | B |
| `--rendering-driver <driver>` | CLI-NATIVE | Rendering driver (depends on display driver; `dummy` under headless) | B |
| `--rendering-method <renderer>` | CLI-NATIVE | Renderer name (e.g. `gl_compatibility`, `mobile`, `forward_plus`) | B |
| `--resolution <W>x<H>` | CLI-NATIVE [no-automation] | Request window resolution | B |
| `--scene <path>` | CLI-NATIVE | Start a named scene (path or UID) instead of the main scene | B |
| `--screen <N>` | CLI-NATIVE [no-automation] | Request a screen | B |
| `--script <script>` (`-s`) | SCRIPTABLE-HEADLESS | Run a script (a `SceneTree`/`MainLoop` script standalone, or an `EditorScript` in editor context). Parse errors exit 1; runtime errors in `_init` can hang — see the exit contract | B; R |
| `--single-threaded-scene` | CLI-NATIVE | Force single-threaded scene processing | B |
| `--single-window` | CLI-NATIVE [no-automation] | Single-window mode (no subwindows) | B |
| `--tablet-driver <driver>` | CLI-NATIVE [no-automation] | Pen-tablet driver | B |
| `--text-driver <driver>` | CLI-NATIVE | Text shaping driver | B |
| `--time-scale <scale>` | CLI-NATIVE | Force time scale (1.0 = normal) | B |
| `--validate-conversion-3to4` | CLI-NATIVE | Dry-run report of a 3.x → 4.x conversion (no writes, per `--help`) | B; U (behaviour) |
| `--validate-extension-api <path>` | CLI-NATIVE | Validate an older `extension_api.json` dump for compatibility. `--help` states incompatibilities exit non-zero | B; U (behaviour) |
| `--verbose` (`-v`) | CLI-NATIVE | Verbose stdout | B |
| `--version` | CLI-NATIVE | Print the version string; exits 0 | B; R |
| `--wid <window_id>` | CLI-NATIVE [no-automation] | Parent to an existing window | B |
| `--windowed` (`-w`) | CLI-NATIVE [no-automation] | Request windowed mode | B |
| `--write-movie <file>` | CLI-NATIVE [no-automation] | Movie Maker: write `.avi`/`.png` frames. **Crashes headless on this build** — see below | B; R (crash) |
| `--xr-mode <mode>` | CLI-NATIVE [no-automation] | XR mode (`default`, `off`, `on`) | B |

## The `--write-movie` crash (a settled negative)

Two independent headless runs crashed the same way: the Ranch agent workers' probe
(`movie.log`, Godot 4.7.2, project with no scene) and this leg's probe
(`movie_main`, the scratch project's real main scene, `--quit-after 3`).
Both printed `Movie Maker mode enabled, recording movie in …`, then
`ERROR: Parameter "t" is null. at: texture_2d_get
(./servers/rendering/dummy/storage/texture_storage.h:110)`, then a
signal-11 crash dump in `Image::get_size()` / `OS_LinuxBSD::run()`,
leaving a 0-byte `.avi`. Conclusion for this build: **Movie Maker under
`--headless` (dummy rendering) is broken; do not use it in a pipeline.**
Movie writing with a real display driver was not tested (no display in
the probe environment) and is **U**. Frame capture routes that work
headless are scripted viewport captures under a non-dummy driver —
also **U** here; the Ranch's visual gates use other engines' renders.

## What the help does not say (UNVERIFIED register)

Alphabetical. Each item is also marked **U** at its point of use in the
full guide.

- `--export-debug`, `--export-patch`, `--install-android-build-template`
  behaviour. No export templates exist on the Ranch workstation, so no successful
  runnable export has ever run here; only `--export-release`'s failure
  mode and `--export-pack`'s success are verified.
- `--lsp-port` / `--dap-port` live sessions. The flags are in `--help`
  (**B**); no client session was opened against them in this leg.
- `--validate-conversion-3to4` and `--validate-extension-api` behaviour.
  In `--help` (**B**); never run (no 3.x project, no older API dump in
  the scratch tree).
- `--write-movie` under a real display driver. Crashed under the dummy
  driver (settled, above); the real-driver route is untested.
- Exit code of a runtime error in a node script during a scene run.
  The SceneTree-`_init` hang is verified (**R**); a `_ready()` runtime
  error's exit behaviour was not probed.
