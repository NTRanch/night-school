# Aseprite scripting API reference

> Part of Night School: the Ranch's scripting-API reference for Aseprite,
> companion to `DADDY_STYLE_ASEPRITE.md`. It covers the Lua surface used
> to build, key, recolour, and export character sprites and animation
> loops for the Ranch's adult games — batch mode only, with version
> guards stated for every feature.

Version basis: **Aseprite 1.3.18.6** (package `aseprite 1.3.18.6-1`, read
from `/var/lib/pacman/local/aseprite-1.3.18.6-1/desc` on 2026-11-02);
scripting API level **41** per the version-guard table below. Evidence
legend (**B** / **S** / **D** / **U**) as defined in `aseprite-cli.md`.

All members verified against <https://www.aseprite.org/api/> on 2026-09-27
(**D**). Source pages: `app`, `cel`, `dialog`, `image`, `pixelcolor`,
`sprite`, `tag`, plus the API changes log at
<https://aseprite.com/api/Changes>. **Exercised members (run-verified
2026-11-02):** the golden suite and probe scripts ran against the
installed binary and exercised, alphabetically: `app.apiVersion` (printed
41), `app.command.FlattenLayers`, `app.command.GotoFrame`,
`app.command.HueSaturation`, `app.command.SaveFileCopyAs` (each with
`ui=false`; see the Commands section), `app.open`, `app.params`,
`app.pixelColor.rgba`, `app.sprite` (read and assignment), `app.transaction`,
`Cel.image` (setter), `Cel.frameNumber`, `Cel.layer`, `ColorMode.RGB`,
`Image` (constructor), `Image:drawPixel`, `json.decode`, `Layer.name`,
`Layer.uuid`, `Palette:saveAs`, `Point`, `Rectangle`, `Sprite`
(constructor), `Sprite.cels`, `Sprite.colorMode`, `Sprite.frames`,
`Sprite.layers`, `Sprite.newCel`, `Sprite.newFrame`, `Sprite.newLayer`,
`Sprite.newSlice`, `Sprite.newTag`, `Sprite.palettes`, and
`Sprite.saveCopyAs`. Those members and the exact uses named here are
run-verified; **every other member in this file remains D only** — listed
from the docs, not exercised. Command names in "Commands verified against
the installed registry" are **S**: checked on 2026-11-02 against the
installed `/usr/share/aseprite/data/gui.xml` (lines 22–136); four of them
are additionally batch-verified by run (see the Commands section).
Members not listed here are unverified — check the official page for the
installed version before using them.

Lua runtime: Aseprite embeds Lua 5.3 libraries (base, coroutine, debug,
math, OS facilities, string, table, utf-8). `os.exit` and `os.tmpname`
are **not** available; `io.open` and `os.execute` **may ask the user for
permission** in interactive use — keep them to the minimum a batch job
names. The permission prompt is a real installed dialog:
`/usr/share/aseprite/data/widgets/script_access.xml` defines the window
with *allow* / *stop script* buttons and "don't show for this access /
for this script" checkboxes (**S**, read 2026-11-02). **Script-access
behaviour under `-b` is settled by run on 2026-11-02:** no dialog
appears, and both `io.open` (read of a runner-created file, 8 bytes) and
`os.execute("true")` succeeded for `--script` runs with exit 0. An
uncaught `error()` under `-b` exits 255 with the error text on stdout,
and `--script` stdout is streamed on this Linux install (a first `print`
arrived ~0.01 s after start, well before the script finished). A note
from the suite scripts (run-verified 2026-11-02): `json.decode` returns
userdata, not a plain table; it supports field access, `#` length,
indexing, and `pairs`, and numbers decode as floats, so geometry and
indices need coercion (`math.floor`).

## `app` namespace

Active objects (all can be `nil` when nothing is active), alphabetical:
`app.cel`, `app.frame`, `app.image`, `app.layer`, `app.sprite`, `app.tag`.

Properties, alphabetical:

- `app.apiVersion` → integer scripting-API version (`nil` on the very
  first scripting builds; see the version-guard table)
- `app.bgColor` / `app.fgColor` → `Color`; `app.bgTile` / `app.fgTile`
  (1.3.9.2+)
- `app.brush`, `app.clipboard`, `app.defaultPalette`, `app.editor`,
  `app.fs`, `app.os` (platform info, 1.3.7+), `app.preferences`,
  `app.theme`, `app.tool`, `app.uiScale`, `app.window`
- `app.isUIAvailable` → `false` in `--batch` mode; guard every UI call
- `app.params` → table of `--script-param name=value` strings
- `app.pixelColor` → low-level pixel helpers (next section)
- `app.sprites` → array of open sprites
- `app.version` → `Version` object (e.g. `Version("1.3.17")`)

Functions, alphabetical:

- `app.alert(msg)`, `app.tip(msg)` (1.3.15+) — UI only, never in batch
- `app.command.<Name>{...}` — run editor commands with named params;
  since 1.3.16-beta1 all commands accept a `ui` param to suppress dialogs
- `app.open(filename)` → `Sprite` or `nil`
- `app.redo()`, `app.refresh()`, `app.undo()`
- `app.transaction([label], fn)` — groups mutations into one undo step;
  **rolls back everything if `fn` errors**
- `app.useTool{...}` — stroke with the active tool (thin editor state in
  batch mode; prefer direct pixel drawing for determinism). Since
  v1.3.18-beta2 it also supports the eyedropper tool; guard that use with
  `app.apiVersion >= 41` (the first stable apiVersion of the 1.3.18 line)
  or a feature check, never assume it on 1.3.17 or earlier
- `json.decode(s)` / `json.encode(t)` — built in since 1.3-rc5

Deprecated aliases — **never use**: `app.activeBrush`, `app.activeCel`,
`app.activeFrame`, `app.activeImage`, `app.activeLayer`,
`app.activeSprite`, `app.activeTag`, `app.activeTool`. Use the short
names.

## `app.pixelColor` (low-level, fast)

Pixels are unsigned ints: grayscale = 16-bit (alpha + gray), indexed =
8-bit palette index, RGBA = 32-bit (8 bits/channel).

- `app.pixelColor.graya(g [, alpha])`, `grayaA(v)`, `grayaV(v)`
- `app.pixelColor.rgba(r, g, b [, alpha])` — alpha defaults to 255 (opaque)
- `app.pixelColor.rgbaA/B/G/R(v)` — channel extractors. **Components are
  NOT premultiplied by alpha.**

Check `sprite.colorMode == ColorMode.RGB` before using the `rgba*`
extractors; on indexed images the int is a palette index.

## Batch-mode script skeleton

```lua
-- params: fuzz=0-255, input=path, key=#rrggbb, output=path
local params = app.params
local input = params.input
assert(type(input) == 'string' and input ~= '', 'missing param: input')
local output = params.output
assert(type(output) == 'string' and output ~= '', 'missing param: output')
assert(output ~= input, 'output must not be the input path')
-- ... validate the rest the same way ...

local spr = app.open(input)
assert(spr ~= nil, 'cannot open: ' .. input)
assert(spr.colorMode == ColorMode.RGB, 'need RGB, got ' .. tostring(spr.colorMode))

app.transaction('daddy-style-aseprite op', function()
  -- mutations here; any error rolls everything back
end)

spr:saveCopyAs(output)  -- never saveAs: keep the input's saved state
print('OK ' .. output)  -- success sentinel: the runner requires this line
```

Assembled from **D** members; the pattern it encodes (params validation,
`app.open`, colour-mode gate, `app.transaction`, `saveCopyAs`, the `OK`
sentinel, and failure via `error()`/`assert()`) is the pattern the suite's
`spec2ase@1` script ran successfully on 2026-11-02. The skeleton itself,
as printed, was not run verbatim.

Rules encoded here: input via `app.params` with validation; output path
named and distinct from the input; nil-checked `app.open`; color-mode
gate; mutations in `app.transaction`; `saveCopyAs` not `saveAs`; failure
as a Lua error; success as the final `OK <path>` sentinel line on stdout
(the runner treats a zero exit **without** the sentinel as a failure). No
`app.alert`, no `Dialog`, no `io.open`/`os.execute`.

## `Cel`

A cel is an image at an *xy* position for one layer/frame. Members,
alphabetical:

- `cel.bounds` (read-only `Rectangle`), `cel.position` (settable `Point`)
- `cel.color`, `cel.data` (string), `cel.properties`
- `cel.frame` / `cel.frameNumber` — settable; moves the cel (replacing any
  cel already there). Frame `1` is the first frame, not `0`
- `cel.image` — settable; the preferred replacement (one undoable action)
- `cel.layer`, `cel.sprite` (read-only)
- `cel.opacity` — `0`–`255` (`0` transparent, `255` opaque)
- `cel.zIndex` — `[-32768, 32767]`, default `0` (1.3-rc3+)

## Commands verified against the installed registry

`app.command.<Name>` dispatches to the same command objects the GUI menus
and shortcuts use. The installed `gui.xml` (header: "Copyright (C)
2018-2025 Igara Studio S.A.") binds these names to default shortcuts, so
each name below is confirmed to exist in the 1.3.18.6 install
(alphabetical; the cross-platform `shortcut` attribute in brackets where
bound):

`AdvancedMode` [Ctrl+F], `CanvasSize` [C], `ClearCel`, `CloseAllFiles`
[Ctrl+Shift+W], `CloseFile` [Ctrl+W], `ColorCurve` [Ctrl+M],
`ConvolutionMatrix` [F9], `ExportSpriteSheet` [Ctrl+E], `Flip`
[Shift+H / Shift+V, `target=mask`], `FrameProperties` [P], `GotoFrame`
[Alt+G], `HueSaturation` [Ctrl+U], `ImportSpriteSheet` [Ctrl+I],
`LayerProperties` [Shift+P], `LinkCels`, `NewFile` [Ctrl+N], `NewFrame`
[Alt+N; `content=empty` Alt+B], `NewLayer` [Shift+N], `OpenFile`
[Ctrl+O], `Outline` [Shift+O], `RemoveFrame` [Alt+C], `RepeatLastExport`
[Ctrl+Shift+X], `ReplaceColor` [Shift+R], `ReverseFrames` [Alt+I],
`RunCommand` [Ctrl+Space], `SaveFile` [Ctrl+S], `SaveFileAs`
[Ctrl+Shift+S], `SaveFileCopyAs` [Ctrl+Alt+Shift+S], `SpriteProperties`
[Ctrl+P], `SpriteSize` [Ctrl+Alt+I], `UnlinkCel`.

**Batch-verified by run on 2026-11-02 (4 commands):** `FlattenLayers`,
`GotoFrame` (with `frame=1`), `HueSaturation`, and `SaveFileCopyAs` (with
`filename=<output>`), each called as `app.command.<Name>{ ui=false, … }`
under `-b` inside a `pcall`; all four printed `CMD-OK`, the
`SaveFileCopyAs` output file existed, and flattening left 1 layer
(evidence: `app-command-batch` in `logs/probes-results.json`).

What this does **not** verify: any other command's batch behaviour, or a
full parameter list for any command — the four verifications cover only
the parameter shapes named above. Pass `ui=false` (1.3.16-beta1+) and
treat batch behaviour for every other command as **UNVERIFIED** until a
batch run proves it. Prefer the documented object API (`Sprite`,
`Image`, `Cel`) over `app.command` in batch scripts.

## Custom file formats (extensions, v1.3.18 line)

Since v1.3.18-beta2, extensions can register a plugin API for custom
file formats when loading and saving sprites; v1.3.18-beta3 added
auto-detection of custom formats by file extension, and v1.3.18.4 notes
extensions registering `.psd` as a custom format. The release notes do
not state a dedicated `app.apiVersion` for the beta2 surface, so guard
format plugins by Aseprite version (`app.version >= Version("1.3.18")`)
or by feature-detecting the registration call, and treat
`app.apiVersion >= 41` (v1.3.18.2) as the first stable guard level of
the line. A pipeline that relies on a custom format must fail loudly
when the format is not registered, not fall back to a built-in decoder.
Security consequence: a custom-format extension is **executable code
that runs on file open** — the RE rules in the guide forbid installing
any extension that ships with a studied game.

## `Dialog` (interactive only)

`Dialog()` / `Dialog(title)` / `Dialog{ autofit, notitlebar, onclose,
parent, resizeable (1.3.15+), title }`. **Returns `nil` when
`app.isUIAvailable` is `false`** (since v1.2.35) — never construct one in
batch scripts.

Widgets, alphabetical: `button`, `canvas` (1.3-rc1+), `check`, `color`,
`combobox`, `entry`, `label`, `modify{...}`, `newrow{ always=true }`,
`number`, `radio`, `separator` (1.3.14+), `shades{ mode="pick"|"sort" }`,
`show{ autoscrollbars (1.3-rc7+), bounds, hand (1.3.10+), wait=false }`,
`slider`, `tab`/`endtabs` (1.3-rc7+). Results land in `dlg.data` keyed by
widget `id`. Method chaining is supported.

## `Image`

Constructors: `Image(otherImage)`, `Image(otherImage, rect)`,
`Image(spec)`, `Image(sprite)`, `Image(w, h [, colorMode])`,
`Image{ fromFile=filename }`.

- `image.bytes` length **must equal** `image.rowStride * image.height`;
  `image.bytesPerPixel` since 1.3-rc7.
- `image:drawPixel(x, y, color)` — generates **no undo by itself**;
  docs recommend clone → modify → assign (`cel.image = img`, which is the
  single-undoable-action replacement).
- `Image:pixels([rect])` — iterator yielding pixel objects callable for
  get/set, each with `.x`/`.y`. The documented fast path for bulk work.
- `image:resize(w, h)` methods documented: `bilinear`, `rotsprite`
  (nearest-neighbor not named on the official page — unverified).
- Deprecated/renamed — **never use**: `putImage`, `putPixel`, `putSprite`.
- Methods, alphabetical: `clear([rect [, color]])` (rect variant since
  1.3-rc3), `clone`, `context` (`GraphicsContext`, 1.3.11-beta1+),
  `drawImage`, `drawPixel`, `drawSprite`, `flip` (1.3-rc4+, `FlipType`),
  `getPixel`, `isEmpty`, `isEqual`, `isPlain`, `pixels`, `resize`,
  `saveAs{ filename, palette }`, `shrinkBounds` (1.3-rc1+).
- Standalone `Image` edits generate **no undo info**; images attached to
  cels generate undo for documented operations.

## LibreSprite divergence table

Primary source: <https://github.com/LibreSprite/LibreSprite/blob/v1.3/SCRIPTING.md>
(the `SCRIPTING.md` shipped at the v1.3 tag) and the
[releases page](https://github.com/LibreSprite/LibreSprite/releases)
(v1.0, Nov 2023: JavaScript (V8) and Lua scripting; v1.2 pre-release:
more scripting API functions; v1.3, October 2026). LibreSprite's
scripting API tracks the old GPL-era Aseprite API, **not** Aseprite 1.3.
LibreSprite is **not installed** on the Ranch workstation (`command -v libresprite`
found nothing on 2026-11-02), so nothing in this table is binary-verified.

**Re-verified 2026-10-15 against LibreSprite v1.3.** Every row below
was checked against the v1.3 `SCRIPTING.md` named above. Rows that
still hold are unchanged in substance; rows that changed are updated
in place; the two rows no primary source could settle are marked
**unverified** in the table itself rather than presented as current.
Rows are alphabetical by area.

| Area | Aseprite 1.3 | LibreSprite 1.3 (re-verified 2026-10-15) |
| ---- | ------------ | --------------- |
| Active objects | `app.cel`, `app.frame`, `app.image`, `app.layer`, `app.sprite`, `app.tag` | `app.activeDocument`, `app.activeFrameNumber`, `app.activeImage`, `app.activeLayerNumber`, `app.activeSprite` (the names Aseprite deprecated); v1.3 also documents `app.activeDocument` as a `Document` object, `app.command`, and `app.platform` — none of which changes the divergence |
| API guard | `app.apiVersion` → integer | not documented |
| CLI | full flag set (see `aseprite-cli.md`) | **unverified (2026-10-15):** neither the v1.3 release notes nor the v1.3 scripting document describes a CLI flag set; the earlier third-party source reading (`-b`/`--batch`, `--data`, `--format`, `--list-layers`, `--list-tags`, `--script`, `--sheet` in their `app_options.cpp`) could not be re-verified from a primary source in this pass, and no LibreSprite binary was available to probe. Verify with `libresprite --help` on the real binary before relying on any flag. |
| Commands | `app.command.<Name>{...}` with named params | parameter-less GUI commands exposed as a `command` class / `app.command` object (`NewFrame()`, `SaveFile()`, …), with no parameter table in the v1.3 scripting document |
| Dialogs | `Dialog()` constructor | `app.createDialog()` method |
| Extensions | `package.json` plugin manifests | **unverified (2026-10-15):** the v1.3 scripting document contains no extension, plugin-manifest, or scripts-folder statement, so the earlier third-party report (scripts dropped into a user `scripts` folder) could not be re-verified from a primary source; do not rely on it |
| Image pixels | `Image:pixels()` iterator, `drawPixel`, `flip`, `resize`, `saveAs`, `shrinkBounds` | only `clear(color)`, `getImageData`/`putImageData`, `getPixel`/`putPixel`, `getPNGData` (base64 PNG) |
| pixelColor | `rgba(r,g,b[,a])` (alpha optional) | `rgba(r,g,b,a)` (alpha required per their docs); same `graya`, `grayaA`, `grayaV`, `rgbaA/B/G/R` |
| Script params | `--script-param` → `app.params` | not documented |
| Sprite layers | `sprite.layers` array | `sprite:layer(n)`, 0-indexed from bottom |
| Sprite save | `saveCopyAs()` (saved state untouched) | `saveAs(fileName, asCopy)` |
| Transactions | `app.transaction(label, fn)` | `sprite:commit()` commits the current transaction |
| UI check | `app.isUIAvailable` | not documented |
| Version | `app.version` → `Version` object | `app.version` → **string** |

Practical rule: an Aseprite 1.3 script will not run on LibreSprite 1.3
without porting (active-object names, image iteration, save/transaction
calls all differ). For a dual-target pipeline, feature-detect
(`if app.apiVersion ~= nil then ... else ... end`) rather than sniffing
for LibreSprite, and keep the LibreSprite path to the small documented
subset above.

## `Sprite`

Constructors: `Sprite(otherSprite)`, `Sprite(spec)`,
`Sprite(width, height [, colorMode])`, `Sprite{ fromFile=filename [, oneFrame] }`.

Key properties, alphabetical: `backgroundLayer`, `bounds`, `cels`,
`colorMode`, `data`, `filename`, `frames`, `grid`, `height`, `isModified`,
`isValid` (1.3.16+), `layers`, `palettes`, `pixelRatio`, `properties`,
`selection`, `slices`, `tags`, `tileManagementPlugin`, `tilesets`,
`transparentColor`, `undoHistory` (1.3.15+), `width`.

Methods, alphabetical:

- `sprite:assignColorSpace(cs)`, `sprite:convertColorSpace(cs)`
- `sprite:close()` — closes **without prompting**
- `sprite:crop(x, y, w, h)`, `sprite:resize(w, h)`
- `sprite:deleteCel(cel)`, `sprite:newCel(layer, frame, image [, pos])`
- `sprite:deleteFrame(f)`, `sprite:newEmptyFrame()`,
  `sprite:newFrame([duration])`
- `sprite:deleteLayer(l)`, `sprite:newGroup()`, `sprite:newLayer()`
- `sprite:deleteSlice(s)`, `sprite:newSlice([rect [, name]])`
- `sprite:deleteTag(tag)`, `sprite:newTag(from, to [, name])`
- `sprite:deleteTile(...)`, `sprite:deleteTileset(t)`,
  `sprite:newTile(tileset [, index])`, `sprite:newTileset([w, h])`
- `sprite:flatten()` — same as `app.command.FlattenLayers()`
- `sprite:loadPalette(pal)`, `sprite:setPalette(pal)`
- `sprite:saveAs(filename)` — marks the document **saved**, retargets it
- `sprite:saveCopyAs(filename)` — exports a copy; saved state untouched
  (use for batch outputs)

Events (`sprite.events:on(name, fn)`): `'change'` (`ev.fromUndo` tells
undo/redo apart, since 1.3-rc1), `'filenamechange'`, and since 1.3.14.3
`'layerblendmode'`, `'layername'`, `'layeropacity'`, `'layervisibility'`.

## Static analysis

Aseprite's scripting surface ships **no upstream static analyzer**: no
linter, checker, or analysis command for Lua scripts appears in the
official API reference, the API changes log, the scripting overview, or
the CLI reference. This was verified against the Aseprite documentation
surface at <https://www.aseprite.org/api/>, <https://aseprite.com/api/Changes>,
<https://www.aseprite.org/docs/scripting/>, and
<https://www.aseprite.org/docs/cli/> on 2026-10-15, as far as those
sources go; earlier audit passes found no such source either, because
there is none to find. The Ranch does have a generic Lua syntax check —
`luac -p <script>` — which proves only that the file parses as Lua; it
knows nothing about the Aseprite API and is not an Aseprite analyzer.

What this guide prescribes instead is execution-based validation, which
is the practice the rest of this guide already encodes (sequential —
each step assumes the one before passed):

1. Run every script in batch mode (`-b --script ...`) against a known
   input before it enters a pipeline; a Lua error on stderr, a
   non-zero exit, or a missing `OK` sentinel is a failed gate, even if
   output files exist.
2. Guard every post-minimum API feature with `app.apiVersion` (table
   below) so an old binary fails loudly at the guard, not silently
   mid-script.
3. Keep the Lua-level discipline of the prerequisite `daddy-style-lua`
   guide (contracts, bounded work, no deprecated aliases — the alias ban
   above is this guide's own mechanically checkable rule).
4. Verify the outputs the script claims to produce (existence, and
   dimensions or sheet metadata where the job defines them) after a
   zero exit.

Do not describe any of these steps as "static analysis" in a validation
record; they are a batch-execution gate, and the distinction matters
when a reader goes looking for an analyzer that does not exist.

## `Tag`

Members, alphabetical:

- `tag.aniDir` → `AniDir.FORWARD` / `PING_PONG` / `PING_PONG_REVERSE`
  (last since 1.3-rc1) / `REVERSE`
- `tag.color`, `tag.data` (string), `tag.properties`
- `tag.frames` → count; `tag.name` (settable string)
- `tag.fromFrame` / `tag.toFrame` → `Frame` objects (very old 1.2.10-beta2
  returned frame numbers instead)
- `tag.repeats` → `0` = unspecified (infinite in UI, once on export),
  `n` = plays *n* times (1.3-rc1+)

Timeline tag groups (v1.3.18) are a user-interface organisation feature:
tags can be separated into groups in the timeline. No new Lua field for
tag groups is documented in the API reference or the API changes log as
of 2026-10-15, so scripts must not try to read or set a tag's group —
treat grouping as presentation state owned by the editor.

## Unverified / not covered

Alphabetical:

- `app.command.*` individual command parameter lists — check
  <https://www.aseprite.org/api/> per command (names are verified; see
  "Commands verified against the installed registry").
- `Color`, `ColorSpace`, `Editor`, `Frame`, `GraphicsContext`, `Layer`
  (beyond the exercised `name`/`uuid` basics), `Palette` (beyond the
  exercised `saveAs` and count), `Plugin`, `Range`, `Rectangle`/`Point`/
  `Size` (beyond the exercised constructors), `Selection`, `Slice`,
  `Tile`, `Tileset`, `Timer`, `WebSocket` — consult the official page
  for the installed version before use.
- LibreSprite CLI surface beyond what their docs state; their docs never
  mention batch mode or `--script-param`.
- Nearest-neighbor as a named `Image:resize` method (docs name only
  `bilinear` and `rotsprite`).
- Batch behaviour of `app.command.*` commands other than `FlattenLayers`,
  `GotoFrame`, `HueSaturation`, and `SaveFileCopyAs`, and full parameter
  lists for any command (only the shapes in the Commands section were
  run on 2026-11-02).
- Signatures of members listed above other than the exercised members
  named in the header (those remain **D** only; the exercised members are
  run-verified for the exact uses named there).

## Version-guard table (`app.apiVersion`)

From <https://aseprite.com/api/Changes>. Guard every feature at or below
your minimum supported Aseprite. Rows stay in **version order**, not
alphabetical: the table is read as "everything at or below my guard
level", so chronology is the meaning.

| apiVersion | Aseprite | Notable additions |
| ---------- | -------- | ----------------- |
| nil / 1 | 1.2.10-beta1…beta3 | first scripting builds |
| 18 | 1.2.35 | `Dialog()` returns nil in batch mode |
| 20 | 1.2.40 / 1.3-beta21 | `ExportSpriteSheet` gains `fromTilesets`, `splitGrid` |
| 21 | 1.3-rc1 | `AniDir.PING_PONG_REVERSE`, `Dialog:canvas()`, `GraphicsContext`, `Image.bounds`, `Image:shrinkBounds()`, short names (`app.sprite` etc.) replace `app.activeSprite`, `Sprite.isModified`, `Sprite:newTile()`, `Tag.repeats` |
| 22 | 1.3-rc2 | `app.uiScale`, `GraphicsContext.blendMode`/`opacity` |
| 23 | 1.3-rc3 | `app.editor`, `Cel.zIndex`, `Image:clear(rect, color)`, `require()` |
| 24 | 1.3-rc4 | `FlipType`, `Image:flip()` |
| 25 | 1.3-rc5 | `app.window`, `json.decode`/`json.encode` |
| 26 | 1.3-rc7 | `Dialog:endtabs()`/`tab()`, `Image.bytesPerPixel` |
| 28 | 1.3.7 | `app.os` |
| 29 | 1.3.9.2 | `app.bgTile`/`app.fgTile` |
| 30 | 1.3.10 / 1.3.11-beta1 | `app.editor.scroll`/`zoom`; `Image.context` |
| 32 | 1.3.13 | `app.clipboard`, `beforesitechange` event |
| 33 | 1.3.14 | layer `uuid`, `os.remove()`/`os.rename()` |
| 34 | 1.3.14.3 | sprite layer-property events |
| 35 | 1.3.15 | `app.tip`, Dialog `autofit`/`resizeable`/`sizeHint`, `FlipType.DIAGONAL`, `sprite.undoHistory` |
| 36 | 1.3.15.3 / 1.3.16-beta1 | `ui` param on all commands |
| 38 | 1.3.16 | `Sprite.isValid`; **behavior change:** property changes outside a transaction no longer generate undo steps |
| 38 | 1.3.17-beta1 | Dialog `onresize` |
| 39 | 1.3.17 | security fix: a script can no longer gain file access granted to another script |
| 40 | 1.3.17.1 | `Sprite.hasAssociatedFile` (also the level of the v1.3.18 beta line up to v1.3.18.1; the custom-file-format plugin API and `app.useTool` eyedropper support arrived in v1.3.18-beta2 on this line) |
| 41 | 1.3.18.2 | `Dialog:samerow{}`, `beforesave`/`save` sprite events (apiVersion updated to 41 in v1.3.18.2; v1.3.18 line is current, latest patch v1.3.18.6) |
