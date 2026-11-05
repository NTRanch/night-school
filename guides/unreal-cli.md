# Unreal CLI reference (UE 5.8.0, the Ranch workstation)

> Companion reference for the Ranch's house style guide for Unreal Engine, adapted for adult game production — the exact headless commands behind the Ranch's character censuses, cooks, packages, and queued renders. Part of Night School.

Companion to `DADDY_STYLE_UNREAL.md`. Marks: **R** run · **S** source · **D** documentation via the Ranch's agent workers · **A** claim by the Ranch's agent workers · **U** UNVERIFIED. Binaries alphabetical; flags alphabetical within each route where content allows.

## Binaries

| Binary | Role | Evidence |
|---|---|---|
| `/opt/Unreal/Engine/Binaries/Linux/UnrealEditor` | GUI Editor — never a headless route; the Ranch's editor setup's `editor_binary()` points here (**S** `config.lua:59`) | **S** |
| `/opt/Unreal/Engine/Binaries/Linux/UnrealEditor-Cmd` | Commandlet / headless Editor binary | **R** (facial Probe 4; this leg) |
| `/opt/Unreal/Engine/Build/BatchFiles/RunUAT.sh` | Unreal Automation Tool (BuildCookRun, BuildPlugin, Gauntlet) | **S/D** |
| `/opt/Unreal/GenerateProjectFiles.sh` | Project-file generation | **S** |

## Exit codes — measured

| Route | Case | Exit | Evidence |
|---|---|---|---|
| `UnrealEditor-Cmd -run=pythonscript` | Script completes | 0 | **R** facial Probe 4 (0, 0 incl. supplementary); **R** this leg's success probe (0) |
| `UnrealEditor-Cmd -run=pythonscript` | Script raises | 255 (non-zero) | **R** this leg's failure probe |
| Commandlets generally / UAT | Full table | — | **U** (the workers' register; gate on log + outputs regardless) |

Log sentinels (success): `Python script executed successfully`; `Success - 0 error(s), 0 warning(s)` (**R**, Probe 4 log).

## Headless Python route (the census route)

```
timeout --kill-after=30s <bound>s \
  /opt/Unreal/Engine/Binaries/Linux/UnrealEditor-Cmd \
  <scratch>/<Proj>.uproject -run=pythonscript \
  -script=<file.py> \
  -nullrhi -unattended -stdout -abslog=<log>
```

- `-abslog=<path>` — the log is the evidence; always set it.
- `-nullrhi` — no rendering hardware interface; required when nothing renders.
- `-run=pythonscript` — the PythonScript commandlet; needs `PythonScriptPlugin` enabled in the project (**R**, Probe 4: the template did not enable it; the scratch copy did).
- `-script=<file>` — file (or code) to execute (**D** [A] form, **R** as used).
- `-stdout` / `-unattended` — full stdout logging; no prompts.
- The commandlet does not automatically load levels (**D** [A]).

## UAT routes

- `RunUAT.sh BuildCookRun -project=<proj> -noP4 -platform=<Plat> -cook -build -stage -pak -archive -archivedirectory=<out>` — the packaging pipeline (**D** [A] shape; **S** the Ranch's editor setup invokes BuildCookRun the same way). Per-flag semantics **U**.
- `RunUAT.sh BuildPlugin …` — plugin packaging (**S**, the Ranch's editor setup).
- Cook-only via the Ranch's editor setup's shape: `BuildCookRun -cook -skipbuild -skipstage` (**S**, `actions.lua` `cook_only`).
- Multi-process cook can report success on failure (**D** [A], page says UE 5.4; 5.8 status **U**) — gate cooks single-process.

## MCP downstream start routes

- `-ModelContextProtocolPort=N` — port override (**S**, the broker surface record §2).
- `ModelContextProtocol.StartServer [port]` / `.StopServer` — Editor console commands, cheat-flagged (**S**).
- `bAutoStartServer` config — default **false** (**S**).
- `-ModelContextProtocolStartServer` — start regardless of the auto-start setting (**D** [A]).
- Ranch lab endpoint: `http://127.0.0.1:8123/mcp` (Epic default port 8000, path `/mcp`) (**S**, the Ranch's editor broker config + the broker surface record).
