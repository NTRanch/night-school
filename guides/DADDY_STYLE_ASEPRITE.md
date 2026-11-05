# Daddy Style Aseprite — full guide

> This is the Ranch's house style guide for Aseprite, adapted for adult game
> production — pixel-art sprites, animation loops, and sprite-sheet pipelines
> for explicit scenes — and published as part of Night School.
> Every rule, gate, and number below is the rule the Ranch actually runs:
> the framing is adult production, the engineering is unchanged.

Version basis: **Aseprite 1.3.18.6**: Arch package `aseprite 1.3.18.6-1`,
binary `/usr/bin/aseprite`. The package version was read from the pacman
local database (`/var/lib/pacman/local/aseprite-1.3.18.6-1/desc`) on
2026-11-02. The version string `1.3.18.6-dev` that the binary prints was
**re-verified by run on 2026-11-02**: `--version` exited 0 and `--help`
was re-captured under an isolated throwaway `HOME`/`XDG_CONFIG_HOME`
(logs `version.txt` / `help.txt` in the verification scratch; see
`VERIFY-aseprite.md` in the verification workdir). Scripting API
level: **41**, confirmed by run on 2026-11-02 (`app.apiVersion` printed
41 by the uuid probe; also the version-guard table in
`aseprite-scripting-api.md`).

This guide holds the full reasoning and is the operational core for
Ranch Aseprite work; when a shorter summary disagrees with it, this
guide wins. The flag and API tables live in
`aseprite-cli.md` and `aseprite-scripting-api.md`.

## Evidence legend

The same legend is used in every file of this package. The order below
carries meaning (strongest evidence first), so it is not alphabetical.

- **B**: present in the full `aseprite --help` output captured from
  `/usr/bin/aseprite` 1.3.18.6-dev on 2026-10-15 (prior Ranch pass),
  and **re-verified by run on 2026-11-02**: `--help` was re-captured and
  diffed against the flag table in `aseprite-cli.md` (exact match; the
  only table entry absent from `--help` is `--noinapp`, marked **D**).
  Where a claim was also exercised by a run on 2026-11-02, the text says
  so inline ("run-verified 2026-11-02").
- **S**: statically verified on 2026-11-02 by reading a file installed by
  the `aseprite 1.3.18.6-1` package, or the pacman database entry for it.
  Nothing was executed. The file is named at each use.
- **D**: stated in the official docs (CLI page read 2026-09-27, API pages
  and changes log 2026-09-27 / 2026-10-15). Not confirmed by **B** or
  **S**.
- **U**: UNVERIFIED. No source settles it. A **U** claim never carries
  load in a pipeline without a probe run first.

**Execution claims in this guide were exercised by run on 2026-11-02.**
The golden suite (12 cases) and the probe sets (20 + 5 items) ran against
the installed binary under isolation; per-item outcomes, suite per-case
results, and the evidence logs they rest on are recorded in
`VERIFY-aseprite.md`. Claims a run settled are marked run-verified
2026-11-02 at their point of use. Claims no run could settle stay marked
**U** in the closing UNVERIFIED register, each with its reason. One
earlier claim was proved **FALSE** by run and is corrected in place, not
footnoted: CLI palette export via `--save-as <out>.gpl` (see the census
Palette export row and the Converters / Golden tests sections).

## Agent use

ELI5: Aseprite has no remote control the Ranch trusts. Agents drive it the
way a shell script would: they build a command line, run it headless, and
check what comes out. On the Ranch that means batch-exporting a heroine's
idle loop, or packing the sprite sheet for an explicit scene, is a command
line and a verified file — never a clicking session. They never drive it
by clicking.

### Broker and connector reality

Every item below was checked against the source material for this guide
(2026-11-02):

- **The Ranch's editor sprite module** (`games/aseprite` in the Ranch's
  editor setup) is an editor-native surface, which makes it an Owner
  tool. It is not an agent API. See "The Ranch's editor sprite module".
- **No custom Aseprite connector exists.** The connector list checked
  for this guide names connectors for Blender and for Unity. For
  Aseprite it records only the installed binary.
- **No MCP server or Ranch broker fronts Aseprite.** None is declared in
  the source material for this guide, and this guide proposes none.
- **The Ranch's other tools** front other engines (Unreal Engine 5.8's
  built-in MCP server, for one) and nothing else. Their GUI observation,
  grounding, and verified-action tools have no Aseprite target.
- **Live-editor brokers** on the Ranch broker live game editors: Unity
  first, Godot later. Aseprite is not in their scope.

Aseprite's own scripting API lists `WebSocket` (**D**, member list not
verified here). A script that opens a socket so an outside agent can drive
the editor would be an **unauthenticated localhost bridge**. The Ranch
rejects that pattern (Ranch lesson, learned 2026-10-19).
Do not build one.

### Capture and verification discipline

Aseprite has no op log, so the **run record** stands in for it. Every
agent-initiated run appends one record to the task's report. Fields,
alphabetical:

| Field | Content |
| ----- | ------- |
| `argv` | The exact argv array, one element per argument |
| `aseprite_version` | Parsed from the probe for this session (never assumed) |
| `converter` | Converter name and version (see "Daddy Style treatment") |
| `exit_code` | The process exit code, plus `124` from `timeout` when killed |
| `inputs` | Path and SHA-256 of every input file |
| `isolation_dir` | The throwaway `HOME` / `XDG_CONFIG_HOME` used |
| `outputs` | Path, SHA-256, and (for images) decoded dimensions of every output |
| `sentinel` | The `OK <path>` line found on stdout, or `absent` |
| `stderr_excerpt` | The first 2 KiB of stderr |
| `timeout_s` | The deadline that applied |

A run counts as successful only when all of these hold: the exit code is
`0`, the sentinel is present for script runs, and every promised output
exists with the promised shape.

### Deterministic routes over GUI

The order of preference carries meaning:

1. A **CLI-NATIVE** flag route (`aseprite-cli.md`).
2. A **SCRIPTABLE-HEADLESS** route: a Lua script under `-b`, using the
   object API (`Sprite`, `Image`, `Cel`) rather than `app.command` or
   `app.useTool`, because both depend on editor state.
3. **GUI-ONLY** work goes to the Owner, named plainly in the hand-off
   ("this needs the Aseprite GUI: <operation>"). It is never clicked
   through by an agent. If the Owner explicitly authorizes an agent to
   drive the GUI, that authorization covers that task only. The result is
   still verified headlessly: export the saved file with `-b` and compare.
   Screenshots are not the record.

## CLI census

ELI5: for every kind of job — exporting a character's animation loop,
packing a sheet for an adult scene, converting a palette for a new outfit
variant — this section says whether you can do it from the terminal with
one flag, whether you need a small script, or whether you must open the
window.

Classes:

- **CLI-NATIVE**: one or more flags do the whole job.
- **GUI-ONLY**: no terminal route exists. This is an honest negative.
- **SCRIPTABLE-HEADLESS**: needs a Lua script run with `-b --script`.

Exit-code behaviour (all classes):

- **Run-verified 2026-11-02**: an uncaught Lua `error()` under `-b`
  exits 255, the error text goes to **stdout**, and execution stops at
  the error. Script runs still require the success sentinel line as
  defence in depth.
- **Run-verified 2026-11-02**: a zero exit can still lie. A truncated
  input and a refused `.gpl` save both exit 0 (see "Golden tests"), so
  output verification is not optional.
- **Ranch rule**: a zero exit with missing outputs is a failure.
- **Ranch rule**: when wrapped in coreutils `timeout`, exit `124` means
  the run was killed for exceeding its deadline. It is always a failure.

Bounded-work rules for all classes are in "Daddy Style treatment → Bounds".

| Operation class | Class | Terminal route | Evidence |
| --------------- | ----- | -------------- | -------- |
| Animation playback / onion skin / live preview | GUI-ONLY | None. `PlayAnimation` / `PlayPreviewAnimation` are editor commands bound to keys. The headless equivalent is to export GIF or PNG frames and view them elsewhere | S (`gui.xml` lines 130–132) |
| Color-mode conversion | CLI-NATIVE | `--color-mode <mode>` with `--dithering-algorithm`, `--dithering-matrix` | B |
| Crop / trim | CLI-NATIVE | `--crop x,y,w,h`; `--trim`, `--trim-sprite`, `--trim-by-grid` | B |
| Desktop thumbnails | CLI-NATIVE | `aseprite-thumbnailer <input> <output> [size]` (positional; freedesktop convention `%i %o %s`). Run-verified 2026-11-02: PNG output, exit 0, and a json-hash sheet dump of the input printed to stdout; `size` is a cap, not an upscale (the 8×8 fixture at size 128 stayed 8×8). For desktop previews only; pipelines use `aseprite -b --save-as` | S (`/usr/share/thumbnailers/aseprite.thumbnailer`); run-verified 2026-11-02 |
| Extension install / enable / disable | GUI-ONLY | Done through the Options dialog. Installing by copying files is **U** and banned (extensions are executable Lua) | S (dialog set in `widgets/`); U (file route) |
| File-format conversion (PNG, GIF, WebP, …) | CLI-NATIVE | `-b <in> --save-as <out>`. The extension picks the format | B; S (MIME list in the `.desktop` file) |
| Filters (Hue/Saturation, Outline, Replace Color, Convolution Matrix, Color Curve) | SCRIPTABLE-HEADLESS | `app.command.<Name>{ ui=false, … }`. Command names are **S**. Batch behaviour is run-verified 2026-11-02 for `HueSaturation` (with `ui=false`; see `aseprite-scripting-api.md` for the four batch-verified commands); batch behaviour and parameters for the other filter commands remain **U**. A deterministic alternative is a pixel loop with `Image:pixels()` | S (`gui.xml` lines 63–68); run-verified 2026-11-02 (`HueSaturation` only) |
| Frame / layer / slice / tag selection | CLI-NATIVE | `--frame-range`, `--layer`, `--ignore-layer`, `--all-layers`, `--slice`, `--tag` **before** the input | B |
| Hand painting / interactive tools | GUI-ONLY | None for hand work. `app.useTool{…}` is scriptable but depends on editor state, so use `Image` pixel writes instead | D |
| Introspection (layers, tags, slices) | CLI-NATIVE | `--list-layers`, `--list-layer-hierarchy`, `--list-tags`, `--list-slices` | B |
| Keyboard shortcuts / Preferences | GUI-ONLY | Done in dialogs. The backing file `~/.config/aseprite/aseprite.ini` is Owner-curated text and is never edited by automation | S (`widgets/keyboard_shortcuts.xml`, `widgets/options.xml`; ini header read 2026-11-02) |
| Layer / tag / slice / grid splitting | CLI-NATIVE | `--split-layers`, `--split-tags`, `--split-slices`, `--split-grid` **before** the input | B |
| Licence, update check, crash report, news | GUI-ONLY | None, and not needed for automation | S (`widgets/enter_license.xml`, `aseprite_update.xml`, `send_crash.xml`) |
| Palette apply | CLI-NATIVE | `--palette <file>` | B |
| Palette export (`.gpl`) | SCRIPTABLE-HEADLESS | Lua route only: `Palette:saveAs` inside a `-b --script` run (run-verified 2026-11-02: a real GIMP Palette file was written). The CLI route is **FALSE**: `-b <in> --save-as <out>.gpl` writes nothing, prints `Aseprite can't save … file ("gpl")` to stdout, and still exits 0 (run-verified 2026-11-02). The Ranch editor module's established `--save-as` shape for `.gpl` therefore does not work on this binary; do not use it | Run-verified 2026-11-02 (CLI route FALSE; Lua route verified); S (the editor module's `actions.lua` lines 65–91, for that shape only) |
| Pixel editing (keying, recolour, generated art) | SCRIPTABLE-HEADLESS | `-b [--script-param k=v]… --script s.lua`, with the object API | B (flags); D (API) |
| Scaling | CLI-NATIVE | `--scale <factor>` (it acts on sprites opened **before** it); `--shrink-to w,h`. Fractional factors are run-verified 2026-11-02: on an 8×8 sprite, `0.5` → 4×4, `1.5` → 12×12, and `2` → 16×16 | B; run-verified 2026-11-02 |
| Script debugging | GUI-ONLY | The script debugger window. Headless, debugging is `print` to stdout | S (`widgets/debugger.xml`) |
| Sprite creation from scratch | SCRIPTABLE-HEADLESS | `Sprite(w, h [, colorMode])`, then `saveAs` inside a `-b` script | D |
| Sprite-sheet export | CLI-NATIVE | `--sheet`, `--data`, `--format`, `--sheet-type`, padding, trim, and extrude flags | B; S (`widgets/export_sprite_sheet.xml` mirrors the same options) |
| Sprite-sheet import (sheet → frames) | SCRIPTABLE-HEADLESS | Preferred: a Lua slice loop with `Image(other, rect)`. `app.command.ImportSpriteSheet` exists (**S**) but its batch behaviour is **U** | S; D |
| Tag groups (timeline, v1.3.18) | GUI-ONLY | No Lua field is documented, so this is presentation state only | D |
| Tileset export | CLI-NATIVE | `--export-tileset` (v1.3-beta21+) | B |
| Undo-history inspection | SCRIPTABLE-HEADLESS | `sprite.undoHistory` (1.3.15+). Rarely meaningful under `-b` | D |
| Version probe | CLI-NATIVE | `aseprite --version` | B |

Exact flag spellings, order sensitivity, and per-flag evidence are in
`aseprite-cli.md`.

## The Ranch's editor sprite module

These items were read from the Ranch's editor setup, in its live
`~/.config/nvim/lua/games/aseprite/` module tree, on 2026-11-02,
read-only. They are use-only evidence. The proposals go to the Ranch's
maintainers, and nothing here edits that editor setup.

### Findings against the prior guide (alphabetical)

- **Binary lookup confirmed.** The order is env `ASEPRITE_BIN`, then
  `NVIM_ASEPRITE_BIN`, then PATH candidates `aseprite`, `Aseprite`
  (`config.lua` lines 594–602; `util.lua` lines 19–29). If the override
  path is not executable, the editor setup warns and falls back to PATH.
- **Fractional `--scale` in live use — now verified.** The Aseprite
  import path passes `--scale` formatted with `%.3f` (`import.lua` lines
  343–347), and `scale_via_cli = true` is the default (`config.lua` line
  591). The binary's handling of fractional factors was **U**; it is now
  run-verified 2026-11-02 (on an 8×8 sprite, `0.5` → 4×4, `1.5` → 12×12,
  `2` → 16×16). That module's default therefore rests on verified behaviour,
  and the earlier probe proposal is closed. No change to that module is
  proposed on this point.
- **Import bounds corrected.** The prior guide said "64 files / 16 MB /
  120 s" for the ImageMagick fallback. The live code has three different
  limits. `BATCH_FILES_MAX = 64` caps batch imports on either path.
  `INPUT_MEGAPIXELS_MAX = 16` (megapixels, not megabytes) applies on the
  **Aseprite** path. `MAGICK_TIMEOUT_MS = 120000` is the timeout for both
  paths (`import.lua` lines 27–31, 331, 349).
- **Known gaps from the prior guide are fixed in the live tree.** The
  generated keying script now asserts on a nil sprite (no `app.alert`),
  gates `spr.colorMode == ColorMode.RGB`, wraps edits in `app.transaction`,
  and prints an `OK` line (`import.lua` lines 76–108). Two gaps remain.
  First, the runner checks only `result.code`, never the sentinel
  (`import.lua` lines 349–355). Second, the sentinel is `OK background
  stripped` rather than `OK <output path>`.
- **No isolation.** The editor module's exports and script runs use the Owner's real
  `HOME`, so they load the curated `~/.config/aseprite/aseprite.ini` and
  any user extensions. Proposal: run headless actions under a throwaway
  `HOME` / `XDG_CONFIG_HOME`, as described in "Daddy Style treatment →
  Isolation".

### What the editor module wires today (alphabetical by action id)

`batch_import`, `describe_environment`, `export_gif`, `export_palette`,
`export_png_sequence`, `export_sheet_type_preset`, `export_sprite_sheet`,
`import_art`, `new_sprite`, `open_in_editor`, `run_script`,
`sprite_prompt`, `sync_palette_to_user_config` (`actions.lua` lines
141–222). `new_sprite` and `open_in_editor` launch the GUI detached. They
are Owner actions.

## Owner use

### Plain-language opening

Aseprite is a paint program for pixel art, but underneath it is also a
command-line tool. When you add `-b` ("batch"), no window opens. Aseprite
reads your file, does what the flags say, writes the result, and exits.
You can do almost everything an export dialog does that way. That matters
on the Ranch because the drawing is the small part of shipping an adult
game: after a heroine's expressions, outfits, and scene frames are painted,
they still have to be keyed, packed, timed, and exported the same way every
time. You only need the window for drawing by hand, watching an animation
play, and changing preferences.

### Mechanism, in full depth

- **Arguments are processed left to right, and they are stateful.** A
  selection flag such as `--tag Walk` sets state that applies to the
  **next** file opened, so it goes before the file. `--scale` applies to
  files **already** opened, so it goes after the file. `--script-param`
  values must exist before `--script` runs, so they go before it. Wrong
  order does not error. It silently does something else. This is the most
  common Aseprite CLI bug.
- **Batch mode has no UI.** In batch mode `app.isUIAvailable` is false and
  `Dialog()` returns `nil` (**D**). A script that tries to show a dialog
  either fails or does nothing.
- **Exit codes.** The shell variable `$?` holds the last command's exit
  code. `0` is the success claim, but you still check the output files,
  because a program can exit `0` having written nothing useful.
- **Your preferences file is curated.** `~/.config/aseprite/aseprite.ini`
  is the Ranch-authored config. Its own header says Aseprite may
  rewrite it when preferences change or on exit. Headless experiments
  therefore run against a throwaway copy of `HOME`, so a pipeline can
  never disturb your real settings.

### First commands, with the check for each

These blocks rest on **B/S/D** facts, and the routes they show were
exercised by run on 2026-11-02 (golden suite and probes; see
`VERIFY-aseprite.md` and the evidence legend).

```bash
# 1. Which binary, which version.
command -v aseprite        # expect: /usr/bin/aseprite        (S, 2026-11-02)
aseprite --version         # expect a line naming 1.3.18.6    (B; re-verified 2026-11-02)
echo $?                    # expect: 0
```

```bash
# 2. A throwaway home, so experiments never touch ~/.config/aseprite.
ASE_SANDBOX="$(mktemp -d)"
mkdir -p "$ASE_SANDBOX/config"
ase() {
  HOME="$ASE_SANDBOX" XDG_CONFIG_HOME="$ASE_SANDBOX/config" \
    timeout 120 aseprite -b "$@"
}
# Check: after any ase run, your real config file is unchanged.
sha256sum ~/.config/aseprite/aseprite.ini   # note it now, compare after
```

```bash
# 3. Look inside a sprite without changing it (absolute paths always).
ase --list-layers "$PWD/hero.aseprite"   # check: layer names, exit 0
ase --list-tags   "$PWD/hero.aseprite"   # check: tag names, exit 0
```

```bash
# 4. Export a sprite sheet plus its JSON description.
OUT="$(mktemp -d)"
ase "$PWD/hero.aseprite" --sheet "$OUT/hero.png" --data "$OUT/hero.json" \
    --format json-array --sheet-type packed
echo $?                       # check: 0
file "$OUT/hero.png"          # check: "PNG image data, W x H, ..."
jq 'keys' "$OUT/hero.json"    # check: the top-level keys are "frames"
                              # and "meta" (run-verified 2026-11-02)
```

```bash
# 5. Run a script with parameters, and require its success line.
ase --script-param input="$PWD/hero.aseprite" \
    --script-param output="$OUT/hero-keyed.aseprite" \
    --script "$PWD/key.lua" | tee "$OUT/run.log"
grep -qxF "OK $OUT/hero-keyed.aseprite" "$OUT/run.log" && echo PASS || echo FAIL
```

```bash
# 6. Is this file really an .aseprite file? Read 2 bytes; execute nothing.
od -An -j4 -N2 -tx1 "$PWD/hero.aseprite"   # expect: e0 a5
# (S: the installed MIME rule matches little-endian 0xA5E0 at offset 4,
#  /usr/share/mime/packages/aseprite.xml)
```

When a block's check fails, stop. Read stderr first, then check argument
order, then check the evidence legend for whether the flag was ever
verified.

## RE alignment

ELI5: when the Ranch studies other people's adult games, it only looks,
and never runs them. Aseprite is one of the magnifying glasses for their
2D art: how a sprite is layered, how a loop is timed, how a palette holds
a character together across explicit scenes. It is not a game engine the
programme studies, and the art it looks at never becomes ours.

### Graphics-enhancement pass

House convention binds this guide to state the Ranch's
graphics-enhancement pass convention wherever asset pipelines are
described. **The text of that convention is not among the source material
for this guide**, and no source document defines it. This guide therefore
records the obligation and does not state the convention's content, which
is **U**. Two asset pipelines here must carry it once the Owner supplies
the ruling text: the converter set in "Daddy Style treatment →
Converters" and the sprite-to-3D factory seam below. Inventing a
convention would violate the "never filled in from memory or inference"
standard.

### Static RE only

Game-RE programme law is that nothing is executed. For Aseprite:

- **Extracted assets are untrusted input.** Opening a PNG or `.aseprite`
  file in Aseprite does not run the game, but it feeds untrusted bytes to
  a large C++ parser. Open only **copies** taken out of
  `<study-extraction-dir>/<slug>/`, never the extraction originals.
  Use batch mode with isolation, a timeout, and an output directory
  outside the extraction tree.
- **Identification without opening.** Census `.ase` / `.aseprite` files
  with the 2-byte magic check (Owner use, step 6), not by opening them in
  Aseprite. Whether a `.aseprite` file can carry executable content stays
  **U**, with this reason: a chunk census of the generated fixture on
  2026-11-02 (verified by source read of its bytes) found only data
  chunk kinds — layer (`0x2004`), cel (`0x2005`), tags (`0x2018`), slice
  (`0x2022`), and header/colour-profile chunks — and no source document
  describes any executable chunk kind. That settles the generated file
  only, not arbitrary files. Treat every `.aseprite` file as data, under
  the untrusted-input rule.
- **Never run what a game ships.** A studied game may ship Aseprite Lua
  scripts or extensions. These are executable code, and a custom-format
  extension (v1.3.18-beta2+, **D**) runs **on file open**. They are never
  installed, never run, and never placed under any `HOME` that Aseprite
  reads. They may be read as text, statically.
- **Provenance at birth.** Any record derived from a study (a census JSON,
  a measured frame-timing table) carries the study slug, its STUDY.md
  section, `content_label: nsfw`, and origin, per the study intake shape
  and lane law used on the Ranch. Attribution names the studio only.

### Torogao: what is adopted, adapted, improved

Status, stated plainly: **the Torogao unified engine map
names no Aseprite row.** Aseprite is not one of the seven engine classes.
It has no pilot, no GAP-ANALYSIS row, and no importer. Nothing below is a
ruling. Each item is a candidate that can reach Torogao only through the
engine map's intake shape (capability, measured behaviour, classification,
one layer, anchor or missing primitive, parity gate, a measurable
"better", provenance).

Under the unification rule in the Torogao engine map, Torogao is the
singular build engine. Aseprite is a study target and a desktop tool only. Its file format, its
sheet JSON, and its Lua runtime **never** become a Torogao format,
runtime, or export target.

| Candidate | What Aseprite shows | Torogao anchor (from the map) | Concrete "better" claim |
| --------- | ------------------- | ----------------------------- | ----------------------- |
| Atlas packing model | Sheet layouts (`packed`, `rows`, `columns`, `horizontal`, `vertical`), border/shape/inner padding, trim, extrude, and power-of-two sizing as explicit, named parameters (**B**; mirrored in the installed export dialog, **S**) | torogao-cli toolbox `atlas` command (per the Torogao engine map) | Torogao's atlas record is byte-stable serialized (torogao-format "byte-stable serialization"). Aseprite makes no upstream byte-stability promise, but on the pinned binary two identical runs produced byte-equal sheet PNG and sheet JSON on 2026-11-02 (run-verified; a version-pinned observation, not a promise across versions) |
| Frame-timing model | Per-frame durations; tags with direction (`FORWARD`, `PING_PONG`, `PING_PONG_REVERSE`, `REVERSE`) and `repeats` (**D**) | Picture-track presentation class: per-frame timing, transitions, overlay compositing | Timing becomes authored records evaluated under the determinism contract (hash chain ×3, §G3.2). It is not editor state |
| Layer/visual-state structure as data | Layers, cels, and z-index as an explicit stack (**D**) | Visual-state delta table (Modification App GAP row, torogao-format table) | Only a measured pilot can carry this row. Aseprite supplies vocabulary, not evidence |

What never crosses: pixels, sprites, or palettes from a studied game. The engine map's
doctrine is that no importer reads a source game's assets into a
Torogao project.

### Seams

- **The Ranch's reverse-engineering tooling** owns measurement. A
  frame/tag/layer census produced with Aseprite's `--list-*` flags or
  sheet JSON is measurement input to a
  study, filed under the study. It is not a Torogao record.
- **The sprite-to-3D factory** owns textures, meshes, and rigs.
  Ranch-original pixel art made in Aseprite — a character's base sprite,
  her outfit variants, the frames of a scene — reaches Torogao **only**
  through the sprite-to-3D factory and is referenced by id. That factory
  ingests 2D sprites, so Aseprite exports are a natural input there.
  That hand-off is an asset pipeline, and the graphics-enhancement
  obligation above applies to it.

## Daddy Style treatment

Priority order, always: **Safety > Performance > Developer Experience.**

### Bounds

These are Ranch policy, not Aseprite limits. Every run carries named
limits with units. Alphabetical:

| Name | Value | Reason |
| ---- | ----- | ------ |
| `BATCH_FILES_MAX` | 64 files | Matches the Ranch editor module's live import cap (`import.lua` line 27) |
| `EXPORT_TIMEOUT_S` | 120 s | Prior-guide default for exports. Longer only with a named reason in the run record |
| `INPUT_MEGAPIXELS_MAX` | 16 MP | Matches the Ranch editor module's live Aseprite-path cap (`import.lua` line 30) |
| `PROBE_STDOUT_BYTES_MAX` | 4 KiB | The `--version` output is one line. Anything larger is wrong |
| `PROBE_TIMEOUT_S` | 10 s | Prior-guide probe bound |
| `RUN_STDERR_BYTES_MAX` | 64 KiB | Captured, then truncated to 2 KiB for the run record |
| `RUN_STDOUT_BYTES_MAX` | 1 MiB | If sheet JSON could exceed it, write `--data` to a file instead of `--data ""` |

### Contracts

Every run answers these questions before it starts. Alphabetical:

- **Bounds**: the deadline and the byte caps above.
- **Failure behaviour**: a non-zero exit, a missing sentinel, a missing or
  misshapen output, or a timeout. Each is a failure, and each is reported
  with the run record. Partial outputs are deleted or quarantined. They
  are never left looking like success.
- **Inputs accepted**: an absolute path to an existing file with an
  allowed extension. For `.aseprite`/`.ase`, the magic also checks out.
  The file is within the pixel cap.
- **Inputs rejected**: relative paths, and paths beginning with `-`.
  Aseprite does **not** honour `--` as an end-of-options marker
  (run-verified 2026-11-02: it is treated as a filename), so a leading
  dash could be parsed as a flag. Also rejected: missing files, an output path
  equal to any input path, and an output that already exists unless
  overwrite is the declared intent (`--sheet` overwrites, **B**).
- **Owner of cleanup**: the runner owns its temp script and isolation
  directory, and removes both whether the run succeeds or fails.
- **Trust boundary**: every input file is untrusted, studied-game assets
  doubly so (see "RE alignment").

### Converters

CODE-FIRST doctrine: the code form is canonical, and Aseprite's forms are
derived. Every conversion is a **named, versioned converter**. Its version
bumps whenever its argv, its normalization, or the pinned Aseprite version
changes. Converters, alphabetical:

| Converter | Direction | Fixed route | Normalization before comparison |
| --------- | --------- | ----------- | ------------------------------- |
| `ase-census@1` | `.aseprite` → census JSON | `-b --list-layers <in>`, `-b --list-tags <in>`, `-b --list-slices <in>` (three runs) | Lines trimmed and kept in emitted order (order is data). The record is serialized with sorted keys |
| `ase2frames@1` | `.aseprite` → PNG sequence | `-b <in> --save-as <dir>/frame001.png` | Compare **decoded RGBA + dimensions** per frame as the gate. PNG bytes are supporting evidence only: two identical runs were byte-equal on 2026-11-02 (run-verified, pinned version), but no upstream promise covers other versions |
| `ase2sheet@1` | `.aseprite` → sheet PNG + JSON | `-b <in> --sheet <png> --data <json> --format json-array --sheet-type packed` | Decoded sheet RGBA + dimensions. JSON parsed and re-serialized with sorted keys. The version/path fields dropped before comparison are `meta.version` (`1.3.18.6-dev`) and `meta.image` (the sheet PNG's filename), both settled by run on 2026-11-02: top-level keys are `frames` and `meta`; `meta` always carries `app`, `format`, `image`, `scale`, `size`, and `version`, and `--list-layers` / `--list-tags` / `--list-slices` before the input add `layers`, `frameTags`, and `slices` to `meta`. Sheet PNG and JSON were byte-equal across two identical runs on 2026-11-02 (run-verified, pinned version) |
| `spec2ase@1` | code spec → `.aseprite` | `-b --script-param spec=<json> --script-param output=<out> --script spec2ase.lua` | Round trip: `spec2ase` then `ase2frames` must reproduce the spec's pixels exactly |

**Deterministic IDs.** Converter output IDs are content addresses: the
SHA-256 of `width ‖ height ‖ frame index ‖ decoded RGBA bytes`. Never use
Aseprite's layer `uuid` (exists since 1.3.14, **D**): it is **not** stable
across saves — run-verified 2026-11-02, a `--save-as` resave changed both
fixture layers' uuids (bg and fg). Never use file mtimes or temp paths.
Byte-stability note (run-verified 2026-11-02, pinned version): two
identical runs produced byte-equal frames PNGs, sheet PNG + JSON, and
`.aseprite` output. Decoded-pixel comparison remains the gate, because
that byte equality is an observation about this binary, not an upstream
promise across versions.

**Pinning.** Each converter version pins Aseprite `1.3.18.6`. When pacman
upgrades Aseprite, the goldens are regenerated **and reviewed**, and the
converter version bumps. A silent pass across an upgrade is not trusted.

### Golden tests

The test set is half validation and half adversarial. Every case runs
under isolation with the bounds above. **The suite ran on 2026-11-02:
11/12 PASS** (evidence: `logs/suite-results.json` in the verification
scratch; per-case record in `VERIFY-aseprite.md`). The one FAIL is a
genuine binary finding, not a suite bug — see `adv-corrupt-input` below.

Adversarial (6), alphabetical:

1. `adv-corrupt-input`: **FAIL — binary finding.** A truncated copy of
   the fixture (first 64 bytes) was expected to fail with a non-zero exit
   or missing outputs. Instead the binary exited 0 with no warning on
   stdout or stderr and silently exported two fully transparent 8×8
   frames (`frame001.png`, `frame002.png`). The decoded-pixel comparison
   in `ase2frames@1` rejects those blank frames, which is why the case
   is recorded as a FAIL of the binary expectation, and why no pipeline
   may trust exit 0 alone for truncated or corrupt input.
2. `adv-dash-path`: **PASS.** An input named `-b.aseprite`. The runner
   rejects it before exec (relative path, leading dash). Aseprite is
   never invoked.
3. `adv-hang`: **PASS.** A script containing an infinite loop. `timeout`
   kills it with exit 124, the run is reported as failed, and the temp
   files are removed.
4. `adv-indexed-into-rgb-script`: **PASS.** An indexed-mode fixture into
   a script that requires RGB. The script's colour-mode assert fires
   (exit 255, sentinel absent), and the run fails.
5. `adv-missing-param`: **PASS.** A script run without
   `--script-param output=…`. The param assert fires (exit 255, sentinel
   absent), and no output exists.
6. `adv-output-equals-input`: **PASS.** `output` is the input path. The
   runner and the script both refuse, and the input's SHA-256 is
   unchanged.

Validation (6), alphabetical:

1. `val-census`: **PASS.** `ase-census@1` on the fixture reproduces the
   golden lists: layers `bg`, `fg`; tags `walk`; slices `hero` (all
   three runs exit 0).
2. `val-config-untouched`: **PASS.** After the full suite,
   `~/.config/aseprite/aseprite.ini` has the same SHA-256 as before
   (`e6abf0368ab69fa0…`).
3. `val-frames`: **PASS.** `ase2frames@1` gives 2 files whose decoded
   RGBA matches the goldens.
4. `val-roundtrip`: **PASS.** `spec2ase@1` then `ase2frames@1`
   reproduces the spec's pixels exactly.
5. `val-sheet`: **PASS.** `ase2sheet@1` sheet RGBA and normalized JSON
   match the goldens; top-level keys are `frames` and `meta`, and the
   frame count in the JSON (2) equals the fixture's.
6. `val-tag-only`: **PASS.** `-b --tag walk <in> --save-as …` gives
   exactly the tag's frame count (2; the tag covers both frames).

The fixture itself is produced by `spec2ase@1` from a checked-in spec (two
layers `bg`/`fg`, two frames, one tag `walk`, one slice `hero`). The
fixture is code, never a hand-made binary.

### Isolation

Every automated run sets both `HOME` and `XDG_CONFIG_HOME` to a fresh
throwaway directory. Config resolution is settled by run on 2026-11-02:
Aseprite uses `$XDG_CONFIG_HOME/aseprite` when `XDG_CONFIG_HOME` is set,
and `$HOME/.config/aseprite` otherwise (probes `config-xdg-only` and
`config-home-only` each wrote only under the expected tree). Automation
still sets both, so the route is pinned either way. The isolation buys
three things:

- No user-installed extension (executable Lua) loads into a pipeline.
  This is load-bearing, not theoretical: run-verified 2026-11-02, an
  extension's `contributes.scripts` script executed at startup under
  `-b` — even for `--version` — when the extension was present in the
  config tree.
- Runs are reproducible, because no Owner preference leaks into an export.
- The curated `aseprite.ini` cannot be rewritten by a run. The suite's
  `val-config-untouched` case passed on 2026-11-02: the real
  `~/.config/aseprite/aseprite.ini` SHA-256 was unchanged
  (`e6abf0368ab69fa0…`) after the full suite.

The prior guide's claim that batch runs stop saving preferences since
v1.3.18 (release notes, **D**) is welcome but is not relied on.

### No hidden behaviour

- **Commands that open dialogs.** `app.command.*` always passes `ui=false`
  (1.3.16-beta1+, **D**). Batch behaviour is run-verified 2026-11-02 for
  `FlattenLayers`, `GotoFrame`, `HueSaturation`, and `SaveFileCopyAs`
  (each with `ui=false`); it remains **U** for every other command, so
  prefer the object API.
- **Overwrites are explicit.** `--sheet` overwrites (**B**). `saveAs()`
  retargets the document, so batch outputs use `saveCopyAs()` (**D**).
- **The permission prompt.** `io.open`, `os.execute`, and file-access
  calls can raise the script-access permission dialog in interactive use
  (**D**). That dialog is a real installed window with *allow* / *stop
  script* buttons (**S**: `widgets/script_access.xml`). Under `-b` there
  is no dialog: run-verified 2026-11-02, `io.open` (read) and
  `os.execute("true")` both succeeded for `--script` runs with exit 0.
  Batch scripts still keep file and process access to the minimum the
  job names, because the interactive prompt gives no protection headless.
- **The success sentinel.** Every script ends with `print('OK ' ..
  output)`. A zero exit without it is a failure.

## UNVERIFIED register

Alphabetical. Each item is marked **U** at its point of use as well, with
its reason. Everything the 2026-11-02 runs settled has been removed from
this register and is marked run-verified at its point of use; the
per-item record is in `VERIFY-aseprite.md`.

- `--oneframe` exact semantics. **U** with reason: `--help` says "Load
  just the first frame", but no batch route tested on 2026-11-02 observed
  a one-frame load — with the flag before or after the input, `--save-as`
  still wrote both frames, sheet JSON still listed 2 frames, and a script
  still saw `#app.sprite.frames == 2`. Which route, if any, honours it is
  unknown, so no pipeline may depend on it without a new probe.
- `.aseprite` executable content, if any. **U** with reason: a chunk
  census of the generated fixture (2026-11-02, verified by source read of
  its bytes) found only data chunk kinds, and no source document describes
  any executable chunk kind; that settles the generated file only, not
  arbitrary files.
- `app.command.*` batch behaviour and parameter lists for commands other
  than the four batch-verified on 2026-11-02 (`FlattenLayers`,
  `GotoFrame`, `HueSaturation`, `SaveFileCopyAs`, each with `ui=false`).
  **U** with reason: those four are the only commands a batch run
  exercised; the rest were never run.
- Graphics-enhancement pass convention: the text is not included in
  the source material for this guide. **U** with reason: genuinely not
  included; not invented.
- Script stdout buffering on platforms other than this Linux install.
  **U** with reason: streaming was run-verified here on 2026-11-02 (a
  first `print` arrived ~0.01 s after start), but no other platform was
  tested.
