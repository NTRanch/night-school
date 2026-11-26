# Daddy Style GLSL — full guide

> Daddy Style is Nice Thoughts Ranch's house style for GLSL,
> adapted for adult game production and published as part of
> Night School, the Ranch's public study programme.

GLSL, driven the Ranch's way: compiled offline against a pinned
validator, every state input a named bounded uniform, and no shader
whose look cannot be reproduced from a frozen spec. Plain version
first: GLSL is the Ranch's skin-and-surface language — the place
adult scenes get their subsurface glow, their wet specular layers,
their censor passes, and the visual feedback that answers a haptic
device's state. It is not a general shader textbook. General GLSL
authoring (dialects, compilation units, SPIR-V interchange, style
for non-adult work) is specified once in the Tiger Style GLSL guide
and cross-referenced, never duplicated; this guide carries only the
substance that is unique to adult production, plus the fences that
substance travels under.

Toolchain basis: **glslangValidator 16.6.0** on the Ranch workstation
(`/usr/bin/glslangValidator`; reports GLSL 4.60 and ESSL 3.20),
with `glslc`, `spirv-val`, and `spirv-cross` alongside it; the
`shaderc` command itself is absent (**R**, probed 2026-11-26, this
leg). Target dialects for Ranch work: `#version 460 core` for
desktop GL and Vulkan-via-SPIR-V routes, `#version 320 es` for
GLES/WebGL-adjacent routes. Dialect is part of a shader's contract,
stated in its header, never inferred from the file extension alone.

## Evidence legend

In strength order:

- **R** — verified by run on the Ranch workstation, 2026-11-26
  (this leg's probes; commands under Owner use).
- **S** — static read of an installed file or a Ranch record,
  2026-11-26.
- **H** — the tool's own `--help` / `--version` text, captured
  2026-11-26.
- **A** — agent-worker draft claim, taken with attribution, not
  re-verified.
- **U** — UNVERIFIED. Named as such; do not build on it.

## The fences (read before any shader in this guide)

These bind every section below. They are not per-shader options.

- **Bloch lane law.** NSFW-pure material — shaders, specs, and
  renders whose substance is adult — never reaches qompassai
  surfaces: no qompassai repo, registry record, caller, or dataset
  sweep. SFW shader technique (a wrap-lighting derivation, a
  sorting rule) may flow to the SFW lane only when it is SFW in
  substance, with its origin recorded. Unclassified material
  defaults to NSFW. Reclassification is a gated Owner/Pax act,
  never an author's convenience.
- **Tier A.** Held reference material — studied games, extracted
  media, reference renders — is study-only. It is measured,
  described, and learned from; it is never a shipped asset, never
  a texture source, never training input for a shipped model.
  A studied game's shader may teach a mechanism; its code and its
  art do not ship.
- **Adults only.** Every character depicted or performed in work
  under this guide is an adult. No shader technique in this guide
  is specified for, tuned on, or applied to a character who is or
  appears to be a minor; a cast whose adult status cannot be
  verified does not enter the pipeline at all.
- **Mesmer's closed taxonomy.** Where shader work touches
  interactive adult systems (mesmer, HOTT, Sirena-class work), the
  effect vocabulary is the closed taxonomy of that programme —
  a shader implements named, admitted effects only. There is no
  open-ended "script" uniform, no arbitrary user-supplied effect
  string, and no effect class admitted by analogy.

## Agent use

### Toolchain reality

- **There is no GLSL connector and no editor broker for shaders.**
  The agent route is the command line: `glslangValidator` for the
  compile gate, `spirv-val` for the interchange gate, file hashes
  for the determinism gate. A shader that has not passed all three
  has not been built, whatever an editor's preview showed.
- **The compile gate is honest.** A trivial `#version 460 core`
  fragment shader compiles at exit 0; the same shader with an
  undeclared identifier fails at exit 2 with the error on stderr
  (**R**, this leg). The gate keys on the exit code and an empty
  error stream, never on "it printed something plausible".
- **Compiled output is byte-stable.** The probe shader compiled
  twice through `glslangValidator -V` produced byte-identical
  SPIR-V (SHA-256 `f9e49d33…`, **R**). That is the property the
  determinism contract below stands on; it is re-probed per
  toolchain version, not assumed forever.

### Capture and verification discipline

Every shader build leaves a record: shader source SHA-256, dialect
and stage, validator version line, argv, SPIR-V SHA-256 where
produced, exit codes for compile and validation, and the scene-spec
hash the shader was built for. A rendered frame without its build
record is an anecdote, not evidence. Visual verdicts follow the
estate's visual-evaluation doctrine: a written should-be-seen
statement, frames from the final artefact at judging size, and a
PASS/FAIL per item — numeric proxies (mean colour, histogram
distance) support a verdict, they never carry one.

### Deterministic routes over previews

Editor shader previews (in Blender, Unity, or a web playground)
are authoring aids for the Owner's eye. The agent route is always:
frozen source → offline compile → validated SPIR-V or linked
program → render from the frozen scene spec → compare. An agent
never substitutes "looked right in the preview" for a gate, and
never hand-tweaks a uniform at runtime to make a frame pass; the
spec changes, is re-hashed, and the frame is re-rendered.

## Shader census

The classes of shader work this guide governs, in the order a
frame meets them. Classes: **SPECIFIED** (contract in this guide),
**CROSS-REF** (general authoring in the Tiger Style GLSL guide;
only the adult delta is here), **OWNER-EYE** (parameters exist in
spec, but their values are admitted by the Owner's judgement, not
by an agent's default).

| Shader class | Class | Where specified | Evidence |
| ------------ | ----- | --------------- | -------- |
| Skin (SSS approximation, oil sheen) | SPECIFIED | Daddy Style treatment → Skin | House practice **S**; per-parameter values OWNER-EYE |
| Blush / heat tint (state-driven) | SPECIFIED | Daddy Style treatment → Skin | House practice **S** |
| Wetness / fluid layers & decals | SPECIFIED | Daddy Style treatment → Wetness and fluids | House practice **S** |
| Censor / mosaic pass | SPECIFIED | Daddy Style treatment → Censor | OE-1b law **S** (estate record) |
| Device-reactive feedback | SPECIFIED | Daddy Style treatment → Device-reactive | ache decide() gate **S** (estate record) |
| Toon / cel base shading | CROSS-REF | Tiger Style GLSL guide; torogao-render3d notes | — |
| General vertex/fragment authoring | CROSS-REF | Tiger Style GLSL guide | — |
| Studied-game shader reading | SPECIFIED (posture) | RE alignment | Static-only rule **S** |


## Owner use

### Plain-language opening

You mostly will not read GLSL line by line. You will judge frames:
a heroine's skin under the scene's light, a censor pass over a
release build, the visual calm when a device stops. Three habits
keep that judgement honest. First, every look you approve is a
frozen spec — if a frame cannot be re-rendered byte-for-byte from
its spec, it was never really approved, only glimpsed. Second,
state is a number with a name and a range: "arousal 0.62" is a
contract, "make her look more flushed" is not. Third, the censor
pass is a release contract, not an aesthetic: its cell size and
its transition timing are specified per release target and gated
like code.

### Mechanism, in full depth

A Ranch GLSL shader is a pure function of its spec. Its inputs are
exactly: geometry attributes, textures named in the spec, and a
uniform block whose fields are spec data — every field named,
typed, ranged, and hashed with the scene. There is no other input
channel: no wall-clock time except a spec-supplied time uniform
driven by the deterministic timeline, no randomness except a
spec-seeded hash, no device handle, no network, no file access.
That purity is what makes the estate's animation law (shipped
animation is code: a frozen hashed scene spec through a timeline
compiler to rig/curve/render data, double-rendered identical)
applicable to shaders at all.

Compilation is a separate, earlier act from rendering.
`glslangValidator` compiles each stage offline and, on the SPIR-V
routes, emits the exact bytes the runtime consumes; `spirv-val`
validates those bytes before any renderer sees them. Runtime
shader compilation from source strings inside a shipped build is
not a Ranch route: it moves a build failure to the player's
machine and a determinism question to a driver the Ranch does not
control.

Precision and dialect are contracts, not defaults. Desktop work
states `precision highp float;` equivalents via the dialect's own
rules and never relies on a driver's default precision in ES
routes; a shader that only works because one driver is lenient
about an undeclared precision or an implicit conversion is a
latent failure on the next driver, and the compile gate is run
under the strictest dialect the release targets.

### First commands, with the check for each

```bash
# 1. Which validator. Expect: Glslang Version 16.6.0, GLSL 4.60,
# ESSL 3.20. A different version line re-opens the determinism
# probe (Daddy Style treatment → Determinism) before gates trust it.
glslangValidator --version

# 2. Compile gate for one stage. Check: exit=0 and nothing on
# stderr. Exit 2 with an ERROR block is a failed gate, full stop.
glslangValidator scene/skin.frag; echo "exit=$?"

# 3. SPIR-V route: compile, validate, hash. Check: exit=0 from
# both tools, and the hash is the one recorded in the build record.
glslangValidator -V scene/skin.frag -o build/skin.spv; echo "exit=$?"
spirv-val build/skin.spv; echo "exit=$?"
sha256sum build/skin.spv
```

## RE alignment

### Static RE only

Studied adult games' shaders are read, never executed to be
learned from and never copied into a Ranch build. The route is
the file posture: extract by the census tools of the relevant
engine guide, read the shader source or disassembly statically,
record the *mechanism* (the wrap term, the mask construction, the
sorting choice) in the study record, and re-author the mechanism
clean-room under this guide's contracts. Shader *code* from a
studied title is Tier A material even when it is three lines long.

### Torogao: what is adopted, adapted, improved

- **Adopted:** the frozen-spec discipline itself — a shader's
  state inputs (expression state, arousal state, device state)
  arrive as spec data through the same timeline compiler that
  drives rigs and curves, so a frame's look is a function of the
  same hash as its pose.
- **Adapted:** the face-state system's state vocabulary. The
  deterministic facial-feature specification (lids, gaze, blush,
  sweat, tear channels) names the states; this guide's skin and
  tint shaders consume those names as uniforms rather than
  inventing a parallel, shader-local state language.
- **Improved (Ranch-side, over studied sources):** studied titles
  routinely drive skin and fluid effects from unclamped,
  undocumented uniforms and runtime-tweaked values. The Ranch
  form names every input, bounds it, and hashes it — the same
  effect, made reproducible and gateable.

### Seams

- **Torogao / torogao-render3d** consumes compiled shaders and
  frozen specs by id; GLSL source is a build-time artefact, never
  a runtime input a game record carries.
- **Lumen** routes share the skin and tint contracts where the
  same character records render in 2D-projected pipelines; a
  contract change lands in both or is recorded as a deliberate
  divergence.
- **ache** is the only device seam, and it is one-directional and
  gated: see Device-reactive shaders. No other Ranch system feeds
  a shader's uniforms.

## Daddy Style treatment

Safety > performance > developer experience, in that order,
applied to the one language where a single unclamped uniform can
turn an adult scene into something the studio never approved, and
where a flickering censor pass is not a style bug but a seizure
risk. The contracts below are the guide.

### Bounds

Named limits, with units, for every Ranch GLSL shader. A value
outside its bound is a spec error, caught before rendering —
never clamped silently at runtime, because a silent clamp is a
hidden behaviour and the frame that results was approved by no one.

| Limit | Value | Why |
| ----- | ----- | --- |
| `STATE_UNIFORM_MAX` | Every state uniform in `[0, 1]`, named per field | State is a contract value, not a vibe |
| `BLUSH_TINT_MAX` | Tint contribution ≤ 0.35 of final albedo per channel | Beyond it skin reads as sunburn, not heat (**U** as a perceptual bound; Owner's eye admits per character) |
| `WRAP_ANGLE_MAX` | Wrap-lighting wrap term in `[0, 1]` | The SSS approximation stays an approximation; > 1 is a different, unnamed effect |
| `THICKNESS_MAP_MAX` | Thickness texture values in `[0, 1]`, single channel | Two-channel thickness encodings are a hidden second input |
| `WET_LAYER_MAX` | ≤ 4 transparent fluid/wet layers per surface | Sorting cost and artefacts grow combinatorially past it |
| `MOSAIC_CELL_MIN_PX` | ≥ 8 px per cell at 1080p for any release build | Below it the censor is decorative, not a censor (release contracts may raise it) |
| `CENSOR_TRANSITION_MIN_S` | ≥ 1.0 s for any censor state change | OE-1b: dynamic transitions are slow and flicker-free, absolutely, for censor shimmer most of all |
| `SHADER_LOOP_MAX` | Every loop has a literal or spec-named trip bound | Unbounded loops are unbounded work; drivers disagree on the punishment |
| `UNIFORM_BLOCK_MAX` | ≤ 32 fields per state block | A state block is a contract surface; past 32 it is two contracts pretending to be one |

### Contracts — skin

- **Subsurface approximation is wrap lighting plus thickness,
  nothing more exotic.** Diffuse uses a wrap term
  (`dot(N, L) + wrap) / (1 + wrap)`, clamped) so light bleeds
  around the terminator; a single-channel thickness map modulates
  a back-light transmission term for thin regions (ears, nostrils,
  fingers, labia where the geometry carries them). Full
  profile-based SSS is not a real-time Ranch route; a shader that
  needs it is a render-pipeline decision, escalated, not a shader
  author's improvisation.
- **Specular is two named layers.** A base skin specular
  (roughness from the spec's skin record) and an oil-sheen layer:
  lower roughness, masked by a spec-named sheen mask, scaled by a
  state uniform when the scene's state calls for sweat or oil.
  The layers are added in that order and no third specular term
  appears without a name and a mask.
- **Blush and heat are state, not paint.** Blush/heat tinting is
  driven by an arousal-state uniform that is spec data: named
  (e.g. `u_arousal`), ranged `[0, 1]`, supplied by the scene
  spec's expression/state track — the same track that drives the
  face-state system, so face and skin can never disagree about
  the character's state. The tint is masked by a blush mask
  texture (cheeks, nose bridge, chest, ears as the character
  record names them), applied as a bounded albedo shift plus a
  small roughness decrease. Painting blush into the base albedo
  texture is forbidden: baked state cannot be driven, and an
  undrivable state channel is a broken contract.
- **Skin state is whole-body coherent.** The same state uniform
  feeds face tint, body tint, sheen scale, and the sweat layer's
  opacity. Per-part ad-hoc multipliers are how a character ends
  up flushed in the face and corpse-pale at the neck in the same
  frame; the contract exists to make that frame unrepresentable.

### Contracts — wetness and fluids

- **Wetness is a mask and a specular change, not a darkening
  hack.** A wet region is: albedo darkened by a spec factor,
  roughness lowered to the wet floor named in the spec, and a
  clear specular highlight from the wet layer. Each of the three
  is a named term; a shader that only darkens is a stain shader
  and is named as one.
- **Fluid decals are geometry-honest.** Drip and fluid decals
  render as decal passes or thin geometry with their own material
  record — never as alpha painted into the skin texture (Tier A
  discipline applies in mirror: shipped fluid look is authored,
  parametric, and spec-driven, so it can be re-rendered and
  gated). Animated drips move by a spec-timeline parameter
  (length/phase), not by a time uniform the shader invents.
- **Transparency sorting is a discipline, not a hope.** Wet and
  fluid layers are transparent; transparent layers render in a
  spec-declared order, back to front, with depth-write off and
  depth-test on, and the order is part of the scene spec — two
  layers whose order is "whatever the engine felt like" produce
  a frame that changes between runs, which the determinism
  contract forbids. Interpenetrating fluid layers are resolved
  by the declared order, never by polygon offset accidents.
  `WET_LAYER_MAX` bounds how much of this discipline a single
  surface may ask for.

### Contracts — censor and mosaic

- **Mosaic is a render pass with a cell-size contract.** The
  censor pass pixelates a spec-named screen region (or object
  mask) by sampling the framebuffer at a cell grid; cell size in
  pixels at the render resolution is a named spec value, floored
  by `MOSAIC_CELL_MIN_PX` and stated per release target. A
  mosaic whose cell size is a shader-author default is not a
  censor, it is a suggestion.
- **Release targets are contracts, named before the build.**
  A JP-release build carries the mosaic parameters its release
  channel requires, recorded in the release spec beside the
  build's other contracts; an uncensored build is a different
  release spec, not a uniform flipped at packaging time. Which
  build a frame came from is part of its record.
- **Blur variants obey the same contract.** Gaussian or
  box-blur censors name their radius in the same units discipline
  (pixels at render resolution) and meet the same floor logic:
  the test is whether the censored content is unrecoverable at
  judging size, judged by eye on final frames, not by the radius
  number alone.
- **OE-1b is absolute here.** Censor shimmer, cell-size pulsing,
  animated mosaic noise, and censor on/off transitions are
  dynamic-stage effects: they transition slowly
  (`CENSOR_TRANSITION_MIN_S`) and never flicker, strobe, or
  oscillate at seizure-relevant rates. A censor effect that
  shimmers to look "digital" is a defect, not a style. This is
  the one contract in this guide with no Owner-eye override:
  the Owner's standing OE-1b hold outranks a per-scene ruling.

### Contracts — device-reactive shaders

- **The shader never talks to a device.** Device state reaches
  a shader by exactly one route: ache's `decide()` gate emits a
  bounded state value; the scene system maps that value into a
  named uniform through a spec-declared mapping; the shader
  reads the uniform. There is no device handle, no callback, no
  polling, and no shader-side notion of what hardware exists.
- **The mapping is a contract.** Rate and pattern map to shader
  parameters (pulse frequency of a glow, tint intensity, ripple
  phase) through a mapping table in the spec: input range,
  output range, and curve named. A shader parameter that moves
  "because the device did something" outside a declared mapping
  is hidden behaviour and fails the gate.
- **Stop is a named value with a named look.** The stop state is
  uniform value `0` (or the spec's named stop constant), and its
  rendered meaning is *visual calm*: effects settle to their rest
  state over the OE-1b transition floor. Stop must never read as
  a glitch — no snap to black, no frozen mid-pulse frame, no
  error-pattern flash. A viewer who cannot tell the device
  stopped from the frame alone, except that everything became
  calm, is the contract working.
- **Shader feedback never drives the device.** The route is
  one-directional. A shader may display state; it may not
  request, modulate, or confirm device behaviour. The safety
  properties (master off by default, synchronous stop, no resume
  on reconnect) live in ache and its gate, and no visual layer
  is permitted to weaken, bypass, or paper over them.

### Contracts — determinism

- **State uniforms are spec data.** Arousal state, expression
  state, device state, censor state: all of it lives in the
  scene spec, is hashed with the scene, and reaches the shader
  only as uniform values. Re-rendering the spec reproduces the
  frame; the estate twin criterion applies (byte-identity after
  stripping volatile metadata, with a measured GPU noise floor
  accepted per take when recorded).
- **No hidden inputs.** Time, seed, and state arrive as named
  uniforms from the deterministic timeline. `gl_FragCoord`
  tricks, driver-dependent derivative behaviour, and
  uninitialised-uniform reads are defects the adversarial suite
  exists to catch.
- **The build is frozen with the spec.** A shipped scene records
  its shaders' SPIR-V hashes beside its spec hash; a shader
  change is a spec change, with a new hash and a new gate run —
  never a silent swap under an approved frame.

### Converters

CODE-FIRST: state becomes uniforms through named converters;
nothing is hand-copied from a state track into a shader constant.

| Converter | Direction | Status |
| --------- | --------- | ------ |
| `spec-uniforms@1` | Scene spec state tracks → uniform block values (named, ranged, clamped-by-rejection) | Specified here; implementation is torogao pipeline work |
| `shader-build@1` | GLSL source + dialect → validated SPIR-V + build record (hashes, versions, exit codes) | Exists in substance: the `glslangValidator` + `spirv-val` route above (**R** for the probe shader); the packaged converter is pipeline work |
| `device-map@1` | ache `decide()` output → shader uniform values via the spec's mapping table | Specified here; bounded by the ache gate's outputs only |

### Golden tests

Half validation, half adversarial, per the standing split. The
suite is specified here; the probe cases marked **R** ran as
individual probes this leg, and the packaged suite runner is
pipeline work — that distinction is stated, not smoothed over.

Validation cases:

- `val-compile-clean` — every shipped shader compiles at exit 0
  with an empty error stream, per dialect (**R** in substance:
  probe shader, this leg).
- `val-spirv-stable` — compiling one shader twice yields
  byte-identical SPIR-V (**R**: probe shader, SHA-256 `f9e49d33…`
  both runs).
- `val-state-coherence` — one spec state value drives face tint,
  body tint, and sheen in a single frame; the frame matches its
  should-be-seen statement at judging size (designed; Owner-eye
  gate).
- `val-censor-floor` — a release build's mosaic at its spec cell
  size renders the censored content unrecoverable at judging
  size (designed; Owner-eye gate).
- `val-stop-calm` — device state driven to stop settles every
  reactive parameter to rest within the transition contract,
  with no snap or flash (designed).

Adversarial cases:

- `adv-undeclared-ident` — a shader with an undeclared identifier
  fails the compile gate at exit 2, never passes on a warning
  (**R**: probe shader, this leg).
- `adv-state-overrange` — a spec carrying a state value outside
  `[0, 1]` is rejected by `spec-uniforms@1` before rendering,
  not clamped into a plausible frame (designed).
- `adv-censor-flicker` — a censor transition authored under
  `CENSOR_TRANSITION_MIN_S` fails the spec gate even if every
  individual frame is beautiful (designed).
- `adv-layer-reorder` — swapping two declared transparent layers
  must change the frame hash and fail comparison against the
  golden; an order-independent result means the layers were
  never really ordered (designed).
- `adv-device-direct` — a shader source containing any device,
  network, or file identifier fails the build on sight; the
  uniform route is the only route (designed).

### RE boundary

See RE alignment. One line for the checklist: studied shader code
is Tier A — read the mechanism, re-author it clean-room, ship
nothing of theirs.

## UNVERIFIED register

Alphabetical. Each item is marked **U** at its point of use as
well.

- `BLUSH_TINT_MAX` as a perceptual bound (0.35) — a house starting
  value; per-character admission is the Owner's eye, and no
  measured skin-tint study backs the number yet.
- Cross-driver SPIR-V determinism beyond the probe scope (the
  byte-stability probe is one trivial fragment shader on one
  validator version; large production shaders and ES routes are
  unprobed).
- JP-release mosaic parameters per channel — the contract form is
  specified; the numeric requirements are per-release-channel
  facts to be recorded in each release spec, not asserted here.
- Runtime behaviour of the device-reactive mapping under ache's
  live S4 conditions (Owner-present sessions) — specified here,
  not yet exercised end-to-end.
- Studied-game shader mechanisms cited in study records but not
  yet re-authored under this guide (each carries its own record;
  none is adopted by being mentioned).
