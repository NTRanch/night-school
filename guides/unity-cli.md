# Unity CLI and Editor command-line reference

> This reference is part of the Ranch's house style for Unity,
> adapted for adult game production. It is part of Night School,
> the Ranch's public study programme.

Version basis: **unity CLI 1.0.0-beta.13** at `~/.local/bin/unity`
and **Unity Editor 6000.6.6f1** at
`~/Unity/Hub/Editor/6000.6.6f1/Editor/Unity`, both on the Ranch workstation.
Everything in the CLI tables was read from the installed CLI on
2026-11-02 (`--help` output, `commands --json`, `skill show`) —
evidence **R** for existence and help text, **D** where the
meaning comes from the CLI's own bundled skill text. Editor argv
rows rest on citations by the Ranch's agent workers of the
6000.6 manual (**D** [A]) plus Ranch-measured runs, and say
so per row.

## Evidence marks

**R** run on the Ranch workstation 2026-11-02 · **S** static read of an installed
file · **D** documentation (installed CLI's bundled text, or
manual citations by the Ranch's agent workers where marked
[A]) · **U** UNVERIFIED.

## The two surfaces, kept separate

Unity has **two** command-line surfaces with **two different
exit-code contracts**. Conflating them is the classic error this
package exists to prevent.

1. **The `unity` CLI** (beta.13): a .NET tool that manages
   Editors, projects, builds, and tests, and can drive a running
   Editor through the Pipeline package. Its exit codes are
   documented, machine-readable, and verified below.
2. **The Editor binary** in batchmode: the heavyweight route for
   in-project work (`-executeMethod`). Its exit codes are
   partially documented (1 = failure, per citations by the
   Ranch's agent workers) and
   its shutdown path can crash after successful work. Judge it
   by logs and outputs, never by exit code alone.

## CLI global options

Alphabetical (from `unity --help`, **R**). Every command also
accepts these unless its help says otherwise.

| Option | Meaning |
|---|---|
| `--color <mode>` | Coloured output: `auto`, `always`, `never`. |
| `--format <format>` | Output format: `human`, `json`, `tsv`, `ndjson`, `github` (env `UNITY_FORMAT`). |
| `--json` | Shorthand for `--format json`. |
| `--log-proxy` | Log outbound requests to `proxy-request.json` for this run (env `UNITY_LOG_PROXY`). |
| `--no-banner` | Suppress the startup banner (env `UNITY_NO_BANNER`). |
| `--no-color` | Shorthand for `--color never`. |
| `--no-log-proxy` | Opt out of proxy logging for this run. |
| `--no-pager` | Disable the pager for long output (env `UNITY_NO_PAGER`). |
| `--non-interactive` | Disable interactive prompts (env `UNITY_NON_INTERACTIVE`). Always set in pipelines. |
| `--proxy <url>` | HTTP / HTTPS / SOCKS / PAC proxy URL (env `UNITY_PROXY`). |
| `--proxy-disable` | Ignore all proxy sources for this invocation. |
| `--quiet` | Suppress informational output (env `UNITY_QUIET`). |
| `--verbose` | Full error details including stack traces (also a per-command flag on some verbs). |
| `-V`, `--version` | Print the CLI version (`1.0.0-beta.13`, **R**). |

Machine-consumption rules (**D**, `unity skill show`): failures
still write a complete document to stdout; branch on `success`
and `errors[0].code`, never on `data` (usually `null` on
failure, not always) and never on stderr, which carries only
human diagnostics. Only `json` / `ndjson` fully bypass the
pager; human listings page through a pager on a TTY.

## CLI exit codes

From the installed CLI's bundled skill text (**D**,
`unity skill show`, beta.13), with this leg's run checks noted.
This table is the CLI's contract — it says nothing about raw
Editor batchmode exits.

| Code | Meaning | Run check (2026-11-02) |
|---|---|---|
| 0 | Success. | `unity version --json` → 0 (**R**). |
| 1 | General error. | — |
| 2 | Bad arguments. | Unknown command → 2, code `INVALID_COMMAND_ARGS` (**R**). |
| 3 | Authentication failure. (`cloud` / `auth` map auth failures here and other operational failures to 6.) | — |
| 4 | Precondition not met (e.g. no license active, floating server not configured). | — |
| 6 | Command-specific failure. | `unity status` with no Pipeline instance → 6, code `STATUS_NO_INSTANCES` (**R**). |
| 7 | Network or transient service failure (cloud automation inventory mappings). | — a draft by the Ranch's agent workers said "retry only 6/7, never 8" [A]; the beta.13 text defines 7 more narrowly, and this guide follows the installed text. |
| 8 | `unity test` only: tests ran and one or more failed. Every other test-run failure stays 6, so CI can retry infrastructure and never retry a failing test. | — |
| 9 | `install` / `install-modules` / `projects require` only: install lock busy under `--no-wait` / `--wait-timeout`. Retry later. | — |
| 130 | Interrupted (SIGINT). | — |
| 143 | Terminated (SIGTERM); emitted by long-running commands that clean up first (currently `unity build`, which scrubs the temporary Android keystore). | — |

The exit-code rows from the Ranch's agent workers [A] (usage /
 auth / operation-failed /
service-unreachable / test-failed, cited from the CLI reference
pages) agree in shape with this table; where their paraphrase and
the installed beta.13 text differ (code 7's scope, the existence
of 4 and 9), the installed text wins and the difference is
recorded in `REPORT-unity.md`.

## CLI commands

The manifest is authoritative and machine-readable:
`unity commands --json` returned **52 top-level commands** on
2026-11-02 (**R**). The table below is alphabetical and covers
the commands the Ranch uses or must consciously avoid; the
manifest, not this table, is the census.

| Command | What it does | Ranch posture |
|---|---|---|
| `analytics` | Manage analytics / telemetry consent. | Read-only curiosity; never changed by a pipeline. |
| `assets` | `.unitypackage` work: `inspect` (list contents, no import), `export`, `import` (batchmode import). (**R**, `--help`) | `inspect` is the intake gate. `import` only into scratch copies. No Asset Store list/download verb exists. |
| `auth` (alias `a`) | Sign in, manage accounts, sign out. | Interactive, Owner only. Never scripted with credentials on argv. |
| `build` | Build a project; spawns the Editor in batchmode and forwards CI flags. | The build route. See `unity build` flags below. |
| `changelog` | Release notes for the installed CLI. | Exists (**R**); behaviour/timing **U** (see register in the full guide). |
| `close` | Close the Editor that has a project open (exits without saving). | Owner-surface; agents do not close the Owner's Editor. |
| `command` (alias `cmd`) | Execute commands on connected (Pipeline) Editors, or list them. Includes `eval` on Editors that expose it. | Arbitrary code in a live Editor. Not connector-wrapped; Owner-command-only. |
| `commands` | List every command/subcommand as a machine-readable manifest. | The census route (**R**: 52 top-level). |
| `doctor` | Diagnostic info about the CLI environment; `--ci` preflight exits non-zero when the environment cannot build/test. | Exists (**R**, `--help`); JSON run **U** this leg. |
| `docs` | Open documentation matched to the project's Editor version. | Human route; opens a browser. Not a pipeline verb. |
| `editor` / `editors` (alias `e`) | Manage Editor installations: `list` (`-i` = installed only), `verify`, `path`, `info`, `add`, `default`, `prune`, `upgrade`, `running`. | `list -i`, `verify`, and `path` are the probe verbs (**R**). Install-family verbs are Owner acts. |
| `env` | Print Hub environment paths and version. | Probe verb (**R**: `editorInstallPath` = `~/Unity/Hub/Editor`; `hubVersion` reports the CLI version string). |
| `install` / `install-modules` / `uninstall` | Install or remove Editors and modules. | Owner acts only. Never a pipeline side effect. |
| `license` | `list` / `status` / `activate` / `return` / `server`. | `list` is a probe verb (**R**: Unity Personal + Asset Store, Assigned). Activation/return are Owner acts. |
| `list` | List tools available on a connected Editor (Pipeline). | Needs a connected instance; none exists on the Ranch workstation today (**R**). |
| `logs` | Read and tail the Hub log file. | Diagnostic route. |
| `mcp` | MCP server + client configuration: bare `unity mcp` starts the stdio server (Pipeline-backed); `configure <client>` writes a client's config file. | `configure` is a live-tree write: staging only, Owner approval. |
| `open` | Open a project with the correct Editor version (`--wait` to block). | Owner-surface (launches the GUI Editor). Agents use batchmode instead. |
| `pipeline` (alias `pipe`) | Pipeline package: `install`, `upgrade`, `list`, `list-versions`, plus Build Automation reads. | `list` is a probe verb (**R**: zero instances). `install` modifies a project: named act, scratch first. |
| `projects` (alias `p`) | Hub registry: `list`, `add`, `remove`, `info`, `create`, `new`, `verify`, `size`, `upgrade`, `export`, `import`, `close`, and more. | `list` / `info` / `verify` are probe verbs (**R**). Registry state never substitutes for an explicit path. |
| `recompile` | Recompile a running Editor's scripts and report errors. | Pipeline-conditional; useless against Safe Mode (**D**). |
| `releases` | List available Unity releases. | Catalogue, not a census (see the Editors warning in `DADDY_STYLE_UNITY.md`). |
| `run` | Run a project in batchmode, forwarding args after `--` to the Editor; `--command` runs a registered Editor command headlessly; `--timeout` bounds it. | The CLI's batchmode wrapper. Honours the same judge-by-output discipline. |
| `self-update` (alias `upgrade`) | Update the CLI; `--check` reports current vs latest without updating. | `--check` is a probe (**R**: beta.13 → latest beta.15). Updating is an install: Owner act. |
| `setup` | Set up coding agents to work with Unity. | Writes agent configuration: staging only, Owner approval. |
| `skill` | `skill show` prints the CLI's bundled agent skill; `skill install <client>` installs it into a client. | `show` is a documentation source (**D**). `install` is a live-tree write: gated as `mcp configure`. |
| `status` | Live state of connected Editors (port, project, version, PID, state). | Probe verb (**R**: zero instances, exit 6). `--until-ready` waits (default 300 s). |
| `templates` | Browse / inspect / create project templates. | Read verbs free; template creation is an authoring act. |
| `test` | Run EditMode/PlayMode tests and write a results report. | The test route. See `unity test` flags below. Exit 8 = tests failed. |
| `version` | Print CLI version and build info as an envelope. | The first probe of any session (**R**). |
| `vcs` | Version control for projects (git, GitLab, GitHub, UVCS). | Ranch projects live in git already; do not let the CLI re-home them. |
| `watch` | Watch a project and re-run a command on file changes. | A daemon-shaped verb: never left running unattended on the Ranch workstation. |

### `unity build` — load-bearing flags

Alphabetical, from `unity build --help` (**R**). The full flag
set (including the Android signing family) is in the help text;
the signing flags' own warnings state that CLI args may appear
in shell history and CI logs — Ranch rule: they are never used
from a script.

| Flag | Meaning |
|---|---|
| `--allow-install` | Install the project's Editor version if missing. **Never passed silently** (install = Owner act). |
| `--create-profile <target>` | Create a build profile for a target, then exit (Unity 6+). |
| `--editor-path <path>` / `--editor-version <v>` | Override the Editor (default: from `ProjectVersion.txt`). |
| `--execute-method <method>` | Static C# method to invoke; without it the CLI uses the built-in build (profile on Unity 6+). |
| `--list-profiles` | List a project's build profile assets, then exit. |
| `--list-targets` | List every valid `--target` value, then exit (**R**: 23 targets; only `StandaloneLinux64`, `StandaloneOSX`, `StandaloneWindows64` are zero-code — the rest require `--execute-method` or a profile, and `--output-path` is always required). |
| `--log-file <path>` (`-l`) | Log path (default `<project>/Logs/build-<target>-<timestamp>.log`); streams to console unless `--no-tail`. |
| `--output-path <path>` (`-o`) | Build destination. Required. |
| `--profile <profile>` | Build profile asset path or name (Unity 6+); defines the target. |
| `--target <target>` | Build target. Required unless `--profile` is used. |

### `unity test` — load-bearing flags

Alphabetical, from `unity test --help` (**R**).

| Flag | Meaning |
|---|---|
| `--affected` | Run only tests a change can reach (guid impact graph); runs the whole suite when it cannot tell. |
| `--coverage` | Collect code coverage (requires the Code Coverage package in the project). |
| `--filter <pattern>` | Run only tests whose names match. |
| `--mode <mode>` | `EditMode` or `PlayMode`. If omitted, the Editor's default platform runs — always pass it in a gate. |
| `--output <path>` | Results report path (default `test-results.xml`). |
| `--report-format <formats>` | `nunit`, `junit`, or `both` (default `nunit`). NUnit XML is the raw-Editor route's format too (**D** [A]). |
| `--retries <n>` | Re-run failing tests up to *n* extra times; passes-on-retry are reported flaky. Default 0. **Gates keep 0.** |
| `--rerun-failed` | Run only the previous run's failures. A debugging tool, not a gate. |
| `--shard <n/m>` | Run one slice of the suite for parallel CI. |
| `--timeout <seconds>` | Kill the Unity process after this many seconds (env `UNITY_TEST_TIMEOUT`). Always set in a gate. |

### `unity run` — notes

`unity run [project] -- <editor args>` forwards args to the
Editor in batchmode; `--command <name>` instead runs a
registered Editor command headlessly, with args after a second
`--` parsed against the command's schema; `--timeout <seconds>`
bounds the run (env `UNITY_RUN_TIMEOUT`); `-l/--log-file`
relocates the log. The CLI's own help steers player builds to
`unity build` ("it adds build targets and profiles, an output
path, a default log file, Android signing, and build exit
codes") (**R**, help text).

## Editor batchmode argv

The raw route. Binary: the project's Editor,
`~/Unity/Hub/Editor/<version>/Editor/Unity`. Version basis for
the semantics: 6000.6.6f1 manual via citations by the Ranch's
agent workers (**D** [A]) plus Ranch-measured runs (Track B,
2026-10-19; facial
Probe 3, 2026-11-02). Flags alphabetical:

| Flag | Meaning / contract |
|---|---|
| `-batchmode` | Run without the GUI. Fails fast: on failure the Editor "immediately exits with return code 1" (**D** [A]). A project open in the GUI cannot be batch-opened (**D** [A]). |
| `-buildTarget <T>` | Select the build target. Always explicit: unspecified means "the last used configuration" (**D** [A]). |
| `-executeMethod <Class.Method>` | Call a public static method, then (with `-quit`) exit. Failure = throw (exit 1) or `EditorApplication.Exit(non-zero)` (**D** [A]; the API itself is **S**, UnityEditor.CoreModule.xml:14407). |
| `-logFile <path>` | Write the Editor log to this file. Always passed. With `-nographics`, the Ranch's agent workers cite that output logs are turned off in that mode (**D** [A]) — `-logFile` is still the evidence route used by every Ranch run. |
| `-nographics` | No graphics device. Cannot render or capture. Correct for censuses and builds that do not render; wrong for captures. |
| `-projectPath <path>` | The project (a scratch copy, always). |
| `-quit` | Exit after the work. Hazards (**D** [A]): it can quit before in-progress tests complete, it can hang (documented default quit timeout 300 s), and it is **not supported while tests are running** — the test argv differs from the build argv. Every Ranch run wraps it in an outer `timeout`. Facial Probe 3's three runs used `-quit` successfully (**R**). |
| `-runTests` | Run the Test Framework suite (raw route). Always with `-testPlatform` and `-testResults`. |
| `-testPlatform <P>` | The test platform; unspecified defaults to EditMode (**D** [A]). Always explicit in a gate. |
| `-testResults <path>` | NUnit XML results path (**D** [A]). |

Ranch additions to the raw route (rules, not flags): the GPU
pin `VK_ICD_FILENAMES=/usr/share/vulkan/icd.d/nvidia_icd.json`
for any rendering run [A, Ranch rule]; the session environment
`DISPLAY` / `XDG_RUNTIME_DIR` exported explicitly (Ranch-
measured F4: without them the Editor exits 1 silently); a probe
for a stale `Temp/UnityLockfile` before launching (F4); and the
outer wrapper `timeout --kill-after=30s <bound>s …; echo
"exit=$?"` so a shutdown hang is bounded and visible.
