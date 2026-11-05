# Daddy Style — the Ranch's engine guides

Daddy Style is the house style of Nice Thoughts Ranch: a safety-first
engineering standard — explicit contracts, bounded work, no hidden
behaviour — written for adult game production. It is the same discipline
the Ranch applies to everything it builds, with its examples, lead-ins,
and worked cases drawn from the work this studio actually does: rigging
characters for adult scenes, soft-body and fluid setups, explicit-scene
render pipelines, adult visual novels, and sprite work for adult games.
The rules do not soften because the content is explicit; a scene that
cannot pass its gates does not ship, whatever it depicts.

## The five guides

Each engine has a main guide plus its command-line and scripting
references. The main guide carries the rules; the references carry the
exact flags, calls, and tables those rules cite.

- **[DADDY_STYLE_BLENDER.md](DADDY_STYLE_BLENDER.md)** — Blender driven
  headlessly and through bpy: census, conversion, renders, and rigging
  gates for character work, with the two-build rule and exit-code
  honesty. References: [blender-cli.md](blender-cli.md),
  [bpy-scripting-api.md](bpy-scripting-api.md).
- **[DADDY_STYLE_GODOT.md](DADDY_STYLE_GODOT.md)** — Godot projects and
  GDScript held to a contract: headless imports, exports, and tool
  scripts with exact exit-code discipline and deterministic conversion.
  References: [godot-cli.md](godot-cli.md),
  [godot-gdscript-api.md](godot-gdscript-api.md).
- **[DADDY_STYLE_UNITY.md](DADDY_STYLE_UNITY.md)** — Unity through its
  CLI and Editor batchmode: deterministic asset GUIDs, the batchmode
  shutdown-crash discipline, and blendshape discipline for facial rigs.
  References: [unity-cli.md](unity-cli.md),
  [unity-editor-api.md](unity-editor-api.md).
- **[DADDY_STYLE_UNREAL.md](DADDY_STYLE_UNREAL.md)** — Unreal Engine 5.8
  on scratch projects only: commandlets, Editor Python, morph-target
  discipline, and packaging judged by logs and outputs, never by exit
  code alone. References: [unreal-cli.md](unreal-cli.md),
  [unreal-python-api.md](unreal-python-api.md).
- **[DADDY_STYLE_ASEPRITE.md](DADDY_STYLE_ASEPRITE.md)** — Aseprite from
  the CLI and Lua: headless batch exports, sprite-sheet pipelines, and
  scripted pixel work with named deterministic converters.
  References: [aseprite-cli.md](aseprite-cli.md),
  [aseprite-scripting-api.md](aseprite-scripting-api.md).

## How the guides relate to the study plans

The study plans in [../plans/](../plans/) are how techniques arrive:
each plan observes a tutorial, distils what it teaches, and rebuilds it
clean-room before the technique counts as proven. These guides are the
house rules the rebuilt techniques get built under — the contracts,
bounds, and gates a technique has to satisfy before it joins a Ranch
pipeline. Plans produce candidate techniques; Daddy Style decides
whether the result is built well enough to keep.
