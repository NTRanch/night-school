# Blender CLI reference — flags, commands, exit behaviour

> Daddy Style reference: the Ranch's house CLI discipline for Blender,
> adapted for adult game production and published as part of
> Night School, the Ranch's public study programme.
> Companion to `DADDY_STYLE_BLENDER.md` (alongside this file).

Version basis: **Blender 5.2.3 LTS**, two builds on the Ranch workstation, same commit
`e13b728c6880`:

| Build | Path | `--version` build line | Embedded Python |
| ----- | ---- | ---------------------- | --------------- |
| Arch (system) | `/usr/bin/blender` | built 2026-10-26, branch `makepkg (modified)` | 3.14.8 |
| Official (staged tarball) | `~/blender-official/blender-5.2.3-linux-x64/blender` | built 2026-10-22, branch `blender-v5.2-release` | 3.13.13 |

Evidence marks: **R** = verified by run on the Ranch workstation, 2026-11-02 (this leg;
probe logs kept in the leg scratch, cited in `REPORT-blender.md`).
**H** = the binary's own `--help` text, captured 2026-11-02 from the Arch
build; the official build's flag set is identical (diff of extracted flag
lists: no differences, **R**). **S** = static read of an installed file.
**U** = UNVERIFIED.

The two builds are **not interchangeable**: the Arch build segfaults on
IK evaluation and on Rigify generation where the official build passes
(**R**; see the full guide → Daddy Style treatment → Binary choice).
Every flag below exists in both builds; behaviour differences are noted
per entry.

## Argument order (read this first)

Arguments are executed in the order they are given (**H**, and **R**):
setting the render output *after* `-f 1` renders the frame to the old
output path (the factory default wrote `/tmp/0001.png`) and still exits
0. Loading a `.blend` overwrites render settings set before it. The
canonical order is: `-b`, safety flags, the `.blend` file, settings,
script, render actions last. An unrecognised `--argument` is treated as
a filename to load and errors (**R**: `--render-engine` →
`unknown argument, loading as file: --render-engine`, exit 1) — a typo'd
flag is a failed run, never a silent no-op, but only if you check the
exit code and the log.

## Commands (`blender -c <command>`, implies `--background`) (**H**, list **R**)

| Command | Purpose | Evidence |
| ------- | ------- | -------- |
| `asset_listing` | List assets | H |
| `extension` | Manage extension repositories and packages (subcommands below) | H, R |
| `maketx` | Convert images to `.tx` (OpenImageIO) | H |

`extension` subcommands (alphabetical; from `blender --command extension
--help`, **R**, exit 0): `build`, `install`, `install-file`, `list`,
`remove`, `repo-add`, `repo-list`, `repo-remove`, `server-generate`,
`sync`, `update`, `validate`. Ranch rule: run extension commands only
with `--offline-mode`, in staging, against a throwaway user directory;
`sync`/`update`/`install` reach the network by design.

## Exit-code behaviour (**R** unless noted)

| Situation | Exit | Note |
| --------- | ---- | ---- |
| `--help`, `--version` | 0 | Both builds |
| Python exception, no `--python-exit-code` | **0** | The zero-exit lie: a failed script looks successful |
| Python exception, `--python-exit-code 1` | 1 | Any value in [0..255] is honoured (7 tested → 7) |
| Segfault (Arch build: IK evaluation, Rigify generation) | 139 | 128 + SIGSEGV; a crash file is written (`Writing: /tmp/blender.crash.txt` on the probe runs) |
| Unknown `--argument` | 1 | Treated as a file to load; error report printed |
| Killed by `timeout` | 124 | The runner's timeout, not Blender's code |

Contract: exit 0 is necessary, not sufficient. A run passes only when
the exit code is 0 **and** the script's `OK <name>` sentinel is present
**and** every expected output exists. Buffered stdout is lost when the
process segfaults (**R**: the Arch Rigify run printed nothing before
dying), so sentinels are evidence only on clean exits, and scripts
`flush=True` on progress lines that count.

## Flags (alphabetical by long flag)

Only flags with an automation, safety, determinism, or census use are
listed; the full 525-line `--help` capture is the authority for the rest
(window, debug, and GPU flags are **H** there). Short forms are given
where they exist.

| Flag | Meaning | Evidence / Ranch note |
| ---- | ------- | ---------------------- |
| `--addons <list>` | Enable add-ons by name | H. **Broken for Rigify on both builds**: `KeyError: key "rigify" not found`, then failure (**R**). Use the `addon_utils` route inside a script instead (see `bpy-scripting-api.md`) |
| `--app-template <name>` | Application template | H |
| `-a`, `--render-anim` | Render the frame range | H. Bounded work: always pair with explicit `-s`/`-e` |
| `-b`, `--background` | Run without UI | H, R (every probe). Background mode disables the audio device by default (H) |
| `-c`, `--command <cmd>` | Run a command (table above); implies `-b` | H, R |
| `--cycles-device <dev>` | Cycles device (`CPU`/`CUDA`/`OPTIX`/…), after `--` | H. U for Ranch gates: no Cycles gate ran this leg |
| `--debug-exit-on-error` | Exit immediately on internal errors | H. An agent-worker manual citation names the same behaviour; not run |
| `--disable-autoexec`, `-Y` | Disable automatic Python execution (drivers, startup scripts) | H (`(default)`), R. Always pass it explicitly; see Autoexec |
| `--disable-crash-handler` | Disable the crash handler | H. Effect on the 139 exit code: **U** |
| `--disable-depsgraph-on-file-load` | Background: do not build/evaluate depsgraphs on load | H. Scripts then fetch `context.evaluated_depsgraph_get` themselves |
| `-E`, `--engine <name>` | Render engine; `-E help` lists engines | H, R: listing on this install is `BLENDER_EEVEE`, `BLENDER_WORKBENCH`. Cycles is selected through its add-on properties, not this listing (observed) |
| `--enable-autoexec`, `-y` | Enable automatic Python execution | H, R. **Banned in Ranch routes.** On a scratch file authored for the probe, `-y` executed a registered text block; nothing else did |
| `--env-system-python <dir>` and siblings | Override bundled resource dirs | H. Isolation route; prefer `BLENDER_USER_*` env vars |
| `-x`, `--use-extension <bool>` | Append the format extension to render output | H |
| `-X`, `--factory-startup` | Skip the user's `startup.blend` | H, R (every probe). Does not skip preferences; pair with isolation (full guide) |
| `-F`, `--render-format <fmt>` | Render format (`PNG`, `JPEG`, `OPEN_EXR`, `FFMPEG`, … per build) | H |
| `-e`, `--frame-end <n>` | End frame | H |
| `-j`, `--frame-jump <n>` | Frame step for `-a` | H |
| `-s`, `--frame-start <n>` | Start frame | H |
| `--log <match>` | Enable log categories | H |
| `--log-file <path>` | Write the log to a file | H. Canonical argv carries it (absolute path) |
| `--log-level <level>` | `fatal`/`error`/`warning`/`info`/`debug`/`trace` | H |
| `-noaudio` | Force the sound system to None | H, R (every probe). Ranch default: no audio, ever (standing rule) |
| `--offline-mode` | Disallow internet access, overriding the preference | H, R (probes). Canonical |
| `--online-mode` | Allow internet access | H. Banned in Ranch routes |
| `-o`, `--render-output <path>` | Render path/name template; `#` = frame digits; no `#` appends `####` | H, R (order probe) |
| `-P`, `--python <file>` | Run a Python script file | H, R (every probe) |
| `--python-console` | Interactive Python console | H. Never in pipelines |
| `--python-exit-code <n>` | Exit code on Python exception, [0..255], 0 disables | H, R (0/1/7 measured) |
| `--python-expr <expr>` | Run an expression as a script | H, R. For one-line settings only; real logic lives in script files |
| `--python-text <name>` | Run a named text block from the loaded file | H. **Banned**: it executes file-supplied code by name |
| `--python-use-system-env` | Let Python see `PYTHONPATH` and user site-packages | H. Banned in gate runs (hermetic Python) |
| `--python-use-user-env` | User site-packages only | H. Banned in gate runs |
| `-q`, `--quiet` | Suppress status printing; warnings/errors still print | H |
| `-f`, `--render-frame <f>` | Render frame(s); `+n`/`-n` relative, comma lists, `a..b` ranges | H, R |
| `-r`, `--register` / `--unregister` | Register/unregister the `.blend` extension (OS-level) | H. Never in pipelines: it changes the user's system |
| `-S`, `--scene <name>` | Active scene for rendering | H |
| `-setaudio <dev>` | Force an audio device | H. Never: `-noaudio` is the Ranch setting |
| `-t`, `--threads <n>` | Threads [1..1024]; 0 = processor count | H, R (render probe used `-t 2`). Gates pin it explicitly |
| `-v`, `--version` | Print version and exit | H, R (both builds, exit 0) |
| `--` | End of options; the rest reaches the script via `sys.argv` | H, R (every probe script parsed its arguments after `--`) |

## Autoexec — what actually executes a `.blend`'s code (**R**)

A `.blend` can carry registered text blocks (Python modules run at load)
and scripted drivers. Probe (scratch file authored by this leg, marker
file as the tripwire), Arch build:

| Load route | Registered text ran? |
| ---------- | -------------------- |
| `blender -b file.blend` (plain CLI load) | No |
| Same, with `-Y` | No |
| Same, with `-y` | **Yes** (marker written) |

So on the command line, loads are untrusted by default on this install,
and `-y` is the single flag that arms file-supplied code. The manual's
"(default)" next to `-Y` in `--help` matches the observation. GUI loads
follow the user's preferences and the per-file trust prompt — **U**
(no GUI run this leg); that is precisely why Ranch routes never open
untrusted files in the GUI. Rules: never pass `-y`; always pass `-Y`
even though it is the default, so the intent survives argv edits; never
use `--python-text` on a studied file.

## Environment variables (**H**)

`BLENDER_USER_CONFIG`, `BLENDER_USER_DATAFILES`,
`BLENDER_USER_EXTENSIONS`, `BLENDER_USER_RESOURCES`,
`BLENDER_USER_SCRIPTS` (isolation: point them at a throwaway directory);
`BLENDER_SYSTEM_DATAFILES`, `BLENDER_SYSTEM_EXTENSIONS`,
`BLENDER_SYSTEM_PYTHON`, `BLENDER_SYSTEM_RESOURCES`,
`BLENDER_SYSTEM_SCRIPTS` (pin the install's own resources);
`BLENDER_OCIO` / `OCIO` (colour management config — record which one a
gate used); `TMPDIR` (crash files and temp data land here); plus the
Ranch's own `VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json`
on the Ranch workstation, so the Intel iGPU is never enumerated (connector rule).

## UNVERIFIED in this file

- `--disable-crash-handler` effect on exit codes.
- Cycles flags (`--cycles-device`, `--cycles-print-stats`) — listed from
 **H** only; no Cycles run this leg.
- GUI-mode flag behaviour (window options) — **H** only; no GUI run.
- Whether preferences can re-enable autoexec for CLI loads in some
 configuration the probes did not cover (the plain-load probe used the
 live user preferences; a `--factory-startup` variant was not run for
 the autoexec matrix).
