# Aseprite CLI reference

> Part of Night School: the Ranch's CLI reference for Aseprite, companion
> to `DADDY_STYLE_ASEPRITE.md`. It covers the headless routes the Ranch's
> adult-game sprite pipelines actually use — sheet exports, frame
> sequences, and palette work — with every flag's evidence level attached.

Version basis: **Aseprite 1.3.18.6** (Arch package `aseprite 1.3.18.6-1`,
binary `/usr/bin/aseprite`). The package version was read from
`/var/lib/pacman/local/aseprite-1.3.18.6-1/desc` on 2026-11-02. The binary
prints `1.3.18.6-dev`: captured 2026-10-15 and **re-verified by run on
2026-11-02** (`--version` exit 0, `--help` re-captured under an isolated
throwaway `HOME`/`XDG_CONFIG_HOME`; see `VERIFY-aseprite.md` in the
verification workdir).

Evidence legend (the **Src** column), identical across this package:

- **B**: present in the full `aseprite --help` output captured from
  `/usr/bin/aseprite` 1.3.18.6-dev on 2026-10-15 (prior Ranch pass),
  and **re-verified by run on 2026-11-02**: `--help` was re-captured and
  every flag row below was diffed against it (exact match; the only
  table entry absent from `--help` is `--noinapp`, marked **D**). Where
  a row's behaviour was also exercised by a run on 2026-11-02, the row
  says so inline ("run-verified 2026-11-02").
- **S**: statically verified 2026-11-02 from a file installed by the
  package (named at use). Nothing executed.
- **D**: stated on <https://www.aseprite.org/docs/cli/> (full page read
  2026-09-27) and absent from the 2026-10-15 `--help` capture.
- **U**: UNVERIFIED. Neither source settles it.

Census legend (the **Class** column), per this guide's census:

- **CLI-NATIVE**: a flag does the whole job.
- **GUI-ONLY**: no terminal route.
- **SCRIPTABLE-HEADLESS**: needs a Lua script under `-b`.

A **[no-automation]** mark means the flag is terminal-reachable but
interactive or unsettled, so it is banned from pipelines.

## Argv safety rules

- **Absolute paths only.** This guards against a relative filename that
  starts with `-` being parsed as a flag. Aseprite does **not** honour
  `--` as an end-of-options marker (run-verified 2026-11-02: in
  `-b -- <file> --save-as <out>`, `--` is treated as a filename —
  stdout `File not found: "--"` — the export still runs, and the exit
  code is still 0), so never rely on it.
- **Argv arrays** (one element per argument), never shell strings. The
  Ranch's editor setup writes them in Lua. The shapes are the same from
  Rust or Python.
- **No secrets in argv**, ever. No Aseprite operation needs one.

## Canonical argv shapes

Alphabetical by purpose. All of these shapes were exercised by run on
2026-11-02 (golden suite and probes; see `VERIFY-aseprite.md`).

```lua
-- Introspection: list tags (prints one per line)
{ bin, '-b', '--list-tags', sprite_path }

-- PNG frame sequence (numbered output)
{ bin, '-b', sprite_path, '--save-as', '/abs/out/frame001.png' }

-- Script with parameters (every --script-param precedes --script)
{ bin, '-b',
  '--script-param', 'output=' .. out_path,
  '--script-param', 'frames=' .. tostring(n),
  '--script', script_path }

-- Sheet JSON to stdout for verification (bounded: see RUN_STDOUT_BYTES_MAX)
{ bin, '-b', sprite_path, '--sheet', sheet_png, '--data', '',
  '--format', 'json-array' }

-- Single tag to GIF (selection option precedes the input)
{ bin, '-b', '--tag', 'Walk', sprite_path, '--save-as', '/abs/out/walk.gif' }

-- Sprite sheet + metadata (json-array matches the Ranch editor module's importer)
{ bin, '-b', sprite_path, '--sheet', sheet_png, '--data', meta_json,
  '--format', 'json-array', '--sheet-type', 'packed' }

-- Version probe (10 s, 4 KiB stdout cap)
{ bin, '--version' }
```

Every automated run also sets `HOME` and `XDG_CONFIG_HOME` to a throwaway
directory. The reasons are in `DADDY_STYLE_ASEPRITE.md` → Daddy Style
treatment → Isolation.

## Exit-code and output contract

- **A zero exit is necessary but not sufficient.** Every script run prints
  a final success sentinel (`OK <output>`), and the runner requires it. A
  zero exit with no sentinel is a failure. The sentinel rule stays as
  defence in depth, but the underlying question is settled: an uncaught
  Lua `error()` under `-b` **does** exit non-zero on 1.3.18.6
  (run-verified 2026-11-02: exit 255, the error text on **stdout**, and
  execution stops at the error). Zero exits can still lie — a truncated
  input and a refused `.gpl` save both exit 0 (see the full guide's
  golden-test results) — so output verification is not optional.
- **Any non-zero exit is a failure**, as is Lua error text on stderr,
  even if output files exist. When wrapped in coreutils `timeout`, exit
  `124` means the run was killed at its deadline.
- **`--sheet` overwrites its target.** Never point it at a file you need
  to keep unless that overwrite is the intent.
- **Verify outputs after a zero exit**, before reporting success: every
  expected output exists and, where the job defines them, has the right
  dimensions or sheet metadata.

## Flag table (alphabetical)

Order-sensitive flags are marked **[pre-input]**. They apply to the
**next sprite opened on the command line**, so they go **before** the
`.aseprite` input. `--scale` is the reverse: it affects sprites opened
**before** it. `--script-param` goes before `--script`.

| Flag | Class | Effect | Src |
| ---- | ----- | ------ | --- |
| `--all-layers` | CLI-NATIVE | Export all layers, including hidden ones **[pre-input]** | B |
| `-b`, `--batch` | CLI-NATIVE | Batch (headless) mode: no UI. Required for automation. Release notes say batch runs stopped saving the preferences file (`aseprite.ini`) in v1.3.18 (**D**). Isolation is still required; do not rely on that change | B |
| `--border-padding <n>` | CLI-NATIVE | Padding around the sheet border | B |
| `--color-mode <mode>` | CLI-NATIVE | Convert colour mode (e.g. `indexed`, `rgb`, `grayscale`) | B |
| `--crop <x,y,w,h>` | CLI-NATIVE | Crop rectangle | B |
| `--data <json>` | CLI-NATIVE | Sprite-sheet metadata JSON. `--data ""` writes the JSON to stdout | B |
| `--debug` | CLI-NATIVE | Debug output | B |
| `--dithering-algorithm <algo>` | CLI-NATIVE | Dithering algorithm for colour conversion | B |
| `--dithering-matrix <matrix>` | CLI-NATIVE | Dithering matrix for colour conversion | B |
| `--export-tileset` | CLI-NATIVE | Export tileset (v1.3-beta21+) | B |
| `--extrude` | CLI-NATIVE | Extrude edge pixels (bleed for tiling) | B |
| `--filename-format <fmt>` | CLI-NATIVE | Output filename template (placeholders below) | B |
| `--format json-array` \| `json-hash` | CLI-NATIVE | Metadata layout: an array, or a hash keyed by name | B |
| `--frame-range <from,to>` | CLI-NATIVE | Export a frame range **[pre-input]** | B |
| `--frame-tag <name>` | CLI-NATIVE | Alias of `--tag` **[pre-input]** | B |
| `--help` | CLI-NATIVE | Print help | B |
| `--ignore-empty` | CLI-NATIVE | Skip empty cels/frames | B |
| `--ignore-layer <pattern>` | CLI-NATIVE | Exclude matching layers **[pre-input]** | B |
| `--import-layer` | CLI-NATIVE | Alias of `--layer` (**B**: `--help` groups them on one line). Run-verified 2026-11-02: selecting layer `fg` with each flag produced byte-identical decoded output; there are no distinct semantics | B |
| `--inner-padding <n>` | CLI-NATIVE | Padding inside each sprite | B |
| `--layer <name>` | CLI-NATIVE | Select which layer(s) to export **[pre-input]** | B |
| `--list-layer-hierarchy` | CLI-NATIVE | Print the layer tree | B |
| `--list-layers` | CLI-NATIVE | Print layer names | B |
| `--list-slices` | CLI-NATIVE | Print slices | B |
| `--list-tags` | CLI-NATIVE | Print frame tags | B |
| `--merge-duplicates` | CLI-NATIVE | Merge duplicate frames | B |
| `--noinapp` | CLI-NATIVE **[no-automation]** | Do not run as an in-app process. Absent from the 1.3.18.6 `--help`, so do not use it without re-probing | D |
| `--oneframe` | CLI-NATIVE | `--help` says "Load just the first frame" (**B**). Its exact semantics remain **U**: on 2026-11-02 no tested batch route observed the one-frame load — with the flag before or after the input, `--save-as` still wrote both frames, sheet JSON still listed 2 frames, and a script still saw `#app.sprite.frames == 2`. Do not let a pipeline depend on it without a new probe | B |
| `-p`, `--preview` | CLI-NATIVE **[no-automation]** | Dry run (run-verified 2026-11-02): prints the planned actions (`- Open file …`, `- Save file …`) to stdout, writes no files, exit 0. Banned from pipelines because it produces no output, not because its behaviour is unknown | B |
| `--palette <file>` | CLI-NATIVE | Use the given palette file for conversion | B |
| `--play-subtags` | CLI-NATIVE | Play subtags and repeats when saving the frames of an animated sprite | B |
| `--power-of-two-size` | CLI-NATIVE | Power-of-two sheet size (added in v1.3.18). The installed export dialog has the same option (**S**: `widgets/export_sprite_sheet.xml` line 43) | B |
| `--save-as <file>` | CLI-NATIVE | Convert/save to another file. `frame001.png` yields a numbered PNG sequence | B |
| `--scale <factor>` | CLI-NATIVE | Scale sprites opened **before** the option. Fractional factors work (run-verified 2026-11-02: on an 8×8 sprite, `0.5` → 4×4, `1.5` → 12×12, `2` → 16×16). The Ranch editor module's fractional default (see the main guide's editor-module section) rests on verified behaviour | B |
| `--script <file>` | SCRIPTABLE-HEADLESS | Run a Lua script (with `-b` for automation) | B |
| `--script-param name=value` | SCRIPTABLE-HEADLESS | Parameter for the script. It arrives as a string in `app.params`. Place **before** `--script` | B |
| `--shape-padding <n>` | CLI-NATIVE | Padding between packed shapes | B |
| `--sheet <png>` | CLI-NATIVE | Pack and save the sprite-sheet PNG. **Overwrites the output file** | B |
| `--sheet-columns <n>` | CLI-NATIVE | Fixed column count | B |
| `--sheet-height <n>` | CLI-NATIVE | Fixed sheet height | B |
| `--sheet-pack` | CLI-NATIVE | Pack tightly (same as `--sheet-type packed`) | B |
| `--sheet-rows <n>` | CLI-NATIVE | Fixed row count | B |
| `--sheet-type columns` \| `horizontal` \| `packed` \| `rows` \| `vertical` | CLI-NATIVE | Sheet layout | B |
| `--sheet-width <n>` | CLI-NATIVE | Fixed sheet width | B |
| `--shell` | CLI-NATIVE **[no-automation]** | Interactive console/scripting shell. Never use in automation | B |
| `--shrink-to <width,height>` | CLI-NATIVE | Shrink each sprite that is larger than width,height | B |
| `--slice <name>` | CLI-NATIVE | Export only the given slice **[pre-input]** | B |
| `--split-grid` | CLI-NATIVE | Split by grid (v1.3-beta21+) **[pre-input]** | B |
| `--split-layers` | CLI-NATIVE | One file per layer **[pre-input]** | B |
| `--split-slices` | CLI-NATIVE | One file per slice **[pre-input]** | B |
| `--split-tags` | CLI-NATIVE | One file per tag **[pre-input]** | B |
| `--tag <name>` | CLI-NATIVE | Export only the given frame tag **[pre-input]** | B |
| `--tagname-format <fmt>` | CLI-NATIVE | Tag name template | B |
| `--trim` | CLI-NATIVE | Trim transparent borders per frame | B |
| `--trim-by-grid` | CLI-NATIVE | Trim by grid cells | B |
| `--trim-sprite` | CLI-NATIVE | Trim the whole sprite | B |
| `-v`, `--verbose` | CLI-NATIVE | Verbose output | B |
| `--version` | CLI-NATIVE | Print version (binary probe) | B |

`--filename-format` placeholders (alphabetical): `{duration}`,
`{extension}`, `{frame}`, `{frame1}`, `{fullname}`, `{innertag}`,
`{layer}`, `{name}`, `{outertag}`, `{path}`, `{tag}`, `{tagframe}`,
`{title}`, plus padded frame variants. The installed export dialog links
its filename-format and tagname-format fields to
`https://www.aseprite.org/docs/cli/#filename-format` and `#tagname-format`
(**S**: `widgets/export_sprite_sheet.xml` lines 134–142).

**Sheet metadata.** The installed export dialog offers *Meta: layers /
tags / slices* checkboxes on the JSON data output (**S**: same file,
lines 126–129). Settled by run on 2026-11-02: the sheet JSON's top-level
keys are `frames` and `meta`; `meta` always carries `app`, `format`,
`image` (the sheet PNG's filename — the path field), `scale`, `size`,
and `version` (`1.3.18.6-dev` — the version field). Placing
`--list-layers` / `--list-tags` / `--list-slices` before the input adds
`layers`, `frameTags`, and `slices` arrays to `meta`. `--data ""` writes
the same JSON to stdout. A converter may depend on all of this.

## Sibling binary: `aseprite-thumbnailer`

The same package installs it (**S**: `/usr/bin/aseprite-thumbnailer` in
the package file list, and on PATH). The installed entry
`/usr/share/thumbnailers/aseprite.thumbnailer` invokes it as
`aseprite-thumbnailer %i %o %s` (input, output, size: the freedesktop
thumbnailer convention). It covers MIME types including
`image/x-aseprite` (**S**).

Class: CLI-NATIVE. Its interface is settled by run on 2026-11-02: the
arguments are positional — `aseprite-thumbnailer <input> <output> [size]`
(a run with a single argument prints exactly that usage line and exits
0); the output is a PNG (the fixture at size 128 produced its native
8×8, so `size` is a cap, not an upscale); a successful run exits 0 and
prints a json-hash sheet dump of the input to stdout. Use it only for
desktop previews. Pipelines use `aseprite -b --save-as`.

## What the docs do not say (UNVERIFIED register)

Most of this register was settled by run on 2026-11-02 (see
`VERIFY-aseprite.md` for the per-item record). What remains, alphabetical:

- `--oneframe` exact semantics. `--help` says "Load just the first
  frame", but no batch route tested on 2026-11-02 observed a one-frame
  load (see the flag table). Which route, if any, honours it is unknown.
- Whether `--script` output buffering is line-buffered on **all**
  platforms. On this Linux install it is streamed (run-verified
  2026-11-02: a first `print` arrived ~0.01 s after start, well before
  the script finished), but the cross-platform claim stays open. Treat
  long silent runs as unknown progress and rely on the timeout.

Settled here on 2026-11-02, for the record: `--` is **not** an
end-of-options marker (treated as a filename); fractional `--scale`
works; `--list-*` flags **do** add `layers`/`frameTags`/`slices` to
sheet `meta`; an uncaught Lua `error()` under `-b` exits 255;
user-installed extensions **do** initialize under `-b` (a
`contributes.scripts` script ran at startup even for `--version` — the
isolation rule is load-bearing); config resolution is
`$XDG_CONFIG_HOME/aseprite` when `XDG_CONFIG_HOME` is set, else
`$HOME/.config/aseprite` (automation still sets both).
