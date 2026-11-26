# Daddy Style HLSL — full guide

> This is the Ranch's house style guide for HLSL and ShaderLab
> in adult Unity work, adapted for adult game production on the
> Ranch's pipelines. It is part of Night School, the Ranch's
> public study programme.

Version basis: **Unity Editor 6000.6.6f1** (the build target,
per the Daddy Style Unity guide) with the **Universal Render
Pipeline** for all new content (Owner ruling 2026-10-19: no
surface shaders, URP for new content — carried in the Unity
guide and binding here). ShaderLab and HLSL in this guide mean
URP ShaderLab (`.shader` files with `HLSLPROGRAM` blocks) and
Shader Graph custom-function HLSL where named. Where a section
rests on a different version, the section says so.

Plain version, for the Ranch's work: this is how shaders get
read, censored, and authored for adult Unity titles here —
censusing the shaders of studied adult games without running
them, building mosaic censors that satisfy a release target's
rules as a build-time fact rather than a runtime hope, and
authoring skin, wetness, fluid, and face-state shaders for the
Ranch's own explicit scenes. The discipline is boring on
purpose. A censor that can be toggled off by a patch, a skin
shader whose wetness layer nobody bounded, or a census that
copied shader code out of a held game will fail exactly when
it matters — in a shipped build, or at the lane-law fence.

This guide holds the full reasoning. It is the operational
core as well, and when a shorter Ranch summary disagrees with
it, this guide wins. General URP shader discipline — pass
structure, SRP Batcher compatibility, keyword hygiene, the
compile gates themselves — lives in the Tiger Style HLSL
guide (`local-tiger-style-hlsl`, references
`TIGER_STYLE_HLSL.md`) and is cross-referenced, never
duplicated. Editor and CLI driving lives in
`DADDY_STYLE_UNITY.md`. This guide carries only what adult
work adds: the studied-game shader census, the censor
contract, and the skin / fluid / face-state authoring rules.

## Evidence legend

The order below carries meaning (strongest evidence first),
so it is not alphabetical. The legend is the Unity guide's,
unchanged, because the two guides are read together.

- **R**: verified by run on the Ranch workstation. The command
  or run is named at the point of use.
- **S**: statically verified by reading an installed file or a
  landed census record. The file or record is named at each
  use.
- **D**: stated in official documentation (Unity's manual /
  ScriptReference for the installed Editor, or the URP package
  documentation for the version a project carries).
- **A**: a draft claim by the Ranch's agent workers, kept with
  attribution. **A** is provenance, not evidence: an **[A]**
  claim is only as strong as the **R**/**S**/**D** mark beside
  it.
- **U**: UNVERIFIED. No source available to this guide settles
  it. A **U** claim never carries load in a pipeline without a
  probe run first. Every **U** in this guide is gathered in
  the closing UNVERIFIED register with its reason.

**Execution status.** No shader census of a held game has run
under this guide yet: the Live3D Editor/Maker census is landed
estate evidence (**S**: estate census records, 2026-11-25 —
Unity Mono build, 135 managed assemblies), and the shader
census this guide specifies is its named follow-on. Rules that
restate estate law (lane law, Tier A, OE-1b, the per-push and
build contracts) are marked as Ranch rules and carry no
evidence letter; they bind because the Owner ruled them, not
because a run proved them. Claims no run settles are marked
**U** in place.

## Agent use

Plain version: agents read held games' shaders the way the
estate reads every held game — files only, never execution —
and they author the Ranch's own shaders as checked-in code
under compile gates. An agent does not open a held game in a
player, does not attach a mod loader or injector to one, and
does not paste a held game's shader source into a Ranch
project, a report, or a prompt. Census output is measurement:
names, properties, keyword sets, and recorded behaviour of the
*model* (how skin is lit, how the censor is built), written as
estate-original specs. The moment a task needs the held game
running to answer its question, the answer is "unmeasured
under static scope" and the task stops there.

On the authoring side, agents write ShaderLab/HLSL as text,
compile it through the Editor batchmode route the Tiger HLSL
guide names, and judge the result by the shader-compiler log,
the variant census, and golden frames — never by "it looked
right in the Scene view once."

## Bounds

Named limits. Every route in this guide respects them; a
route that needs more names the reason in the run record.

| Constant | Value | Meaning |
|---|---|---|
| `HEAVY_JOBS_MAX` | 1 | The Ranch workstation good-neighbour rule: one heavy job at a time; interactive work wins. |
| `TEST_RETRIES_MAX` | 0 | Gates never retry failing tests into a pass. |
| `SHADER_VARIANTS_MAX` | 256 per shader | Compiled-variant budget for one Ranch-authored shader in one build. A shader that needs more splits or moves a branch to a uniform; the census names the count per build. |
| `CENSUS_FILES_MAX` | 10,000 files per census run | Bound for one studied-game shader census pass over a held tree. A larger tree is censused in named slices. |
| `CENSOR_CELL_PX_REF` | 24 px at 1080p reference height | Mosaic cell size for the default censor profile, defined at the reference height and scaled by the rule in the censor section; per-profile overrides are named in the profile, never in code. |
| `CENSOR_CELL_PX_MIN` / `CENSOR_CELL_PX_MAX` | 8 / 96 px (at reference height) | Clamp for any profile's cell size. A profile outside the clamp does not build. |
| `CENSOR_TRANSITION_MIN_MS` | 500 ms | Floor for any censor state transition (fade, wipe, cell-size change). OE-1b bound; see the censor section. |
| `STATE_SLEW_MAX` | 2.0 units/s | Fastest rate any expression/face shader state value may change. Slower is the default; faster needs a named exception in the scene spec. |
| `FLUID_RT_MAX` | 512×512, 30 Hz | Ceiling for any runtime fluid render-texture (resolution and update rate) per character. A design needing more is a new ruling, not a bigger constant. |
| `GOLDEN_FRAME_TOLERANCE` | named per gate | Golden-frame comparisons state their tolerance in the gate record (estate twin-criterion: byte-identity after metadata stripping, or the recorded measured noise floor). No silent tolerance. |

## Studied-game shader census

How the Ranch reads the shaders of a held adult Unity title.
The worked class is the Live3D class: the estate holds the
Live3D Editor (Steam app 1454500) installed on the Ranch
workstation as a study target (**S**: estate Live3D study
records, `~/.local/share/pax/live3d-study/` on the Ranch
workstation; Editor is a Unity Mono build, 135 managed
assemblies censused). The census method below is
title-agnostic; Live3D names appear where the estate's held
copy is the concrete tree the census runs over.

### Ranch rules (apply to every shader census)

- **Static-only; nothing executed.** The held game is never
  run, and no runtime route — mod loader, injector, graphics
  debugger attach, frame capture of a live process — is in
  scope, ever. Census tooling reads files: serialized assets,
  bundles, and managed assemblies as data. This is the Unity
  guide's RE rule applied to the shader layer, and it does not
  soften because shaders feel like "just text."
- **No shader code leaves the held tree.** A census records
  what a shader *is and does* — its name, properties, keyword
  sets, pass structure, and the measured properties of its
  lighting model. It never copies HLSL/GLSL source, compiled
  program text, or decompiled bodies into a Ranch file. Where
  a platform blob is the only form a shader ships in, the
  census records the blob's existence, target, and size, and
  the shader's serialized property/keyword surface — not a
  disassembly. Findings land as estate-original specs; any
  Ranch implementation is written from the spec.
- **Tier A.** A held game is measurement and reference only.
  Nothing measured becomes a shipped asset: no texture, no
  material setting lifted as a value-for-value copy into a
  shipping title, no shader. A measured *property* (a specular
  intensity range, a cell size, a wrap coefficient's order of
  magnitude) may inform an original implementation's spec,
  cited as a measurement.
- **Provenance at birth.** Every census record carries
  origin, `content_label`, and evidence from birth (bloch
  lane law). Adult-game census records are NTRanch-lane
  material: NSFW-pure findings never reach qompassai repos or
  callers, and an unclassified NTRanch-origin record defaults
  to nsfw.
- **All characters adults.** The census covers adult titles
  whose casts are adults. A title whose cast is not
  established as adult is not a study target at all; the
  census does not start. (Estate screening law, applied at
  intake, before any file is read.)
- **Unmeasured stays unmeasured.** A shader behaviour the
  static record cannot settle — a uniform driven by gameplay
  code paths the census cannot trace, a fluid sim's update
  rule — is recorded as unmeasured, permanently, until a
  static route measures it. It is never reconstructed from
  screenshots or feel.

### Where the shaders are

A Unity player build carries shaders in serialized form, not
as loose `.shader` files (**D**, Unity manual: build layout;
**S** for the held Live3D tree's shape per the estate census):

- **Serialized asset files** (`sharedassets*.assets`,
  `level*`, `resources.assets`, and AssetBundle files):
  `Shader` objects are serialized assets in these files. A
  readable Shader object exposes its name, its property table
  (names, types, ranges, defaults), its subshader/pass
  structure, and its keyword names; compiled GPU program blobs
  ride inside per platform (**D**).
- **The render pipeline is a census fact, not an assumption.**
  Record which pipeline the title builds on — built-in render
  pipeline for the Live3D class's generation of titles, URP /
  HDRP where the package manifest or the shader surface says
  so. Skin and censor techniques do not transfer across
  pipelines without re-derivation; the census record names the
  pipeline in its header so a later reader cannot mistake a
  built-in-RP finding for a URP recipe.
- **Managed assemblies** name the *drivers*: the census reads
  `Assembly-CSharp.dll` and companions statically (the Unity
  guide's Mono route) for which code sets which material
  properties at runtime — the material-property call sites are
  how a shader's state contract (which uniforms exist, who
  writes them, at what cadence) gets recorded without running
  anything.

Tooling is the estate's static asset-reading tooling
(AssetRipper-class extraction to a scratch tree, serialized-
file readers, `monodis`-class IL census), driven under the
Unity guide's bounds. Extraction happens on a scratch copy;
the held tree is read-only.

### What to record — the census record

One record per shader, one header per title. Rows are the
minimum; a field the tree cannot answer is written
`unmeasured`, never omitted (an omitted field reads as
"checked, nothing there"; `unmeasured` reads as the truth).

**Title header:** title and build identity; engine version;
render pipeline; where the shaders were found (which files,
which bundles); the census tooling and versions; the
provenance triple (origin, `content_label`, evidence).

**Per shader:**

| Field | What is recorded |
|---|---|
| Identity | Shader name as declared; file/bundle it was found in; subshader count; LOD values. |
| Pass structure | Pass names/tags per subshader (LightMode tags name the pipeline role); which passes are shadow/depth/meta. |
| Property table | Every declared property: name, type, range, default. This is the shader's public contract and the single most valuable census output. |
| Keyword surface | `shader_feature` vs `multi_compile` per keyword set (the distinction decides what stripping can remove — see the censor section); the keyword combinations actually present in shipped blobs, counted. |
| Texture slots | Which properties bind textures; texture dimensions/format where the tree states them; whether a slot is an authored mask (see below) or a colour map. |
| State drivers | Which managed code writes which properties (call-site census), and the value ranges written where the IL states them. |
| Skin model | See below. |
| Censor implementation | See below. |
| Fluid layers | See below. |

**Skin model — what to record.** The census answers, in
order: (1) Is skin a dedicated shader or a general material
with skin-tuned properties? (2) Diffuse model: Lambert, or
wrap lighting (record the wrap term's property name and
default/range — the value is a measurement, the *shape* is
the finding). (3) Subsurface approximation class: none /
gradient-or-thickness tint / view-dependent backlight term /
pre-integrated lookup — class only, plus which mask texture
feeds it if one does. (4) Specular model: single-lobe or
dual-lobe; which mask controls roughness; whether a separate
wetness or sweat term exists and which property drives it.
(5) Whether skin state (arousal tint, sweat) is a shader
input at all, and if so which properties carry it — this is
the studied game's face/body state contract, and it feeds the
authoring section below as a *pattern*, never as copied code.

**Censor implementation — what to record.** Class first,
because the class decides everything downstream:
(a) **material swap** — censored regions wear a mosaic/pattern
material; (b) **post-process** — a fullscreen or masked pass
pixelates a region or the frame; (c) **geometry** — a censor
mesh/occluder; (d) **asset-level** — the shipped textures are
themselves censored, no runtime mechanism at all. Then: the
cell size or pattern scale if the record states it; what
drives the censor region (a mask texture, a second UV set, a
renderer list); whether an uncensored variant of the same
shader ships in the same build (keyword sets answer this —
and the answer is a finding about the *studied* title's
compliance posture, recorded neutrally); and whether the
censor state ever animates.

**Fluid layers — what to record.** Class: scrolling-texture
layer / decal / render-texture simulation / particle-only.
Which render queue and blending the layer uses; which mask
shapes it; whether it writes depth (a frequent studied-game
defect worth recording as a defect); the update cadence if a
driver states one. Fluid in studied titles is usually the
least bounded system in the build; the census says so when
it is.

### Census gates

- The census record's header provenance triple is present
  before any per-shader row is accepted.
- Every row's fields are filled or marked `unmeasured`.
- A second reader re-derives the keyword counts from the
  tree independently; counts that disagree do not average —
  the discrepancy is the record until resolved (estate
  Rule 4: re-derive on the artefact, cross-check against an
  independent derivation).
- No file in the census output contains shader source from
  the held tree. A grep for held-tree shader names is a
  citation; a pasted body is a gate failure and the record is
  withdrawn.

## Censor implementations in URP

The Ranch's own censor work for adult Unity titles that ship
into censored release targets. The contract in one sentence:
**the censor profile of a build is decided at build time,
compiled into the player, and verified in the built player —
a shipped build contains exactly one profile's code path,
and no runtime mechanism can select another.**

### Implementation shape

The Ranch default is a **masked post-process mosaic**:

1. A `ScriptableRendererFeature` renders censor-tagged
   renderers into a mask render texture (tag by layer or by a
   renderer-list override, named in the profile — never by
   name-matching strings at runtime).
2. A mosaic pass, ordered after the scene colour pass it
   samples, pixelates the masked region: each output texel
   samples the centre of its cell, cells aligned to a grid
   anchored at the screen origin. The grid is anchored, not
   free-floating, for a physical reason: a grid that follows
   the camera or the region re-samples every frame, and
   re-sampling a high-contrast region at frame rate is
   shimmer — and shimmer at the wrong frequency is a flicker
   hazard (OE-1b, below), not merely an artefact.
3. Per-object mosaic materials (a mosaic shader worn by the
   region itself) are the named alternative for titles whose
   art direction needs the censor to live in the scene's
   lighting. The choice is per title, recorded in the title's
   shader spec; the contracts below bind both shapes.

Full-screen unmasked mosaic is not a Ranch shape: a censor
that pixelates what it does not need to pixelate is a defect
against the release target's actual requirement, and it
hides mask bugs the gates below exist to catch.

### The cell-size contract

- Cell size is named in the **profile**, in pixels at the
  1080p reference height (`CENSOR_CELL_PX_REF`, clamped by
  `CENSOR_CELL_PX_MIN` / `CENSOR_CELL_PX_MAX`). Code reads the
  profile; code never carries a literal cell size.
- At runtime the cell size scales by
  `renderHeight / 1080`, rounded to a whole number of device
  pixels, so the censor's *visual* density is constant across
  resolutions. A 4K build and a 720p build of one profile show
  the same censor; a census of either proves the other.
- Cell size is a **state**, and state changes obey the
  transition contract below. Nothing in the pass may vary the
  cell size per frame from an unclamped driver (a distance-
  based driver, say, must pass through the profile's clamp
  and the slew bound, and the driver is named in the spec).

### OE-1b binds censor animation

Estate law OE-1b: dynamic-stage transitions must be slower
and flicker-free (epilepsy/seizure risk). The censor is a
dynamic stage element, so:

- Any censor transition — region fade in/out, profile-driven
  cell-size change, mask edge softening change — takes at
  least `CENSOR_TRANSITION_MIN_MS`, eased, never stepped.
- The mosaic may never toggle on/off, invert, or re-grid at
  frame rate or on a repeating cycle. A censor that strobes
  is a safety defect, and it fails the gate regardless of how
  it renders in a still.
- Cell-size changes interpolate the *sampled cell size*
  continuously; they never jump the grid anchor.
- The gate is temporal, not visual: a transition is verified
  from a captured frame sequence with timestamps (transition
  duration and per-frame luminance deltas measured), not from
  two stills. A still pair cannot prove a transition is slow.

### Release-target profiles are a build-time contract

Release targets differ — a JP-target build carries mosaic
censorship; a western-target build of the same title ships
uncensored — and the difference is a **build configuration**,
not a setting:

- A profile is a checked-in asset (a ScriptableObject or the
  title's equivalent) selected by the build definition. The
  build names its profile the way it names its target; an
  unspecified profile is a build error, not a default. (The
  Unity guide's rule applies verbatim: "last used
  configuration" is a hidden default and is banned.)
- The unselected profile's code path **does not ship**.
  Concretely: censor on/off and profile variants are
  `shader_feature`-class branches or separate shaders — never
  `multi_compile` branches that ship every variant — and the
  build's shader-variant stripping is configured and then
  *verified* (below) to have removed the unselected path. A
  runtime toggle that ships both paths is banned twice over:
  it is hidden behaviour, and it makes the build's compliance
  posture one patch away from the other profile — which is
  precisely what the release target's rule exists to prevent.
- The same rule binds data: an uncensored texture set does
  not ride inside a censored build "because the shader hides
  it," and conversely. Profiles partition assets, not just
  code.

### Censor gates

- **Built-player census.** Every censored-profile build is
  censused after the build (the census method above, run over
  the Ranch's own player): the variant census shows the
  unselected profile's keywords absent, and the asset census
  shows the unselected profile's textures absent. The build
  report carries both counts.
- **Golden frames per profile.** Each profile has golden
  frames of its named test scene, judged at judging size:
  mask coverage complete (no uncensored texel inside the
  mask region — checked by sampling, not by eye alone), cell
  size at the profile value at two resolutions (720p and
  2160p captures, scaled-cell equality), and the region
  outside the mask pixel-identical to the uncensored profile's
  frame outside the mask, within the gate's named tolerance.
- **Transition measurement.** The OE-1b gate above: a timed
  capture of each censor transition, duration and flicker
  measured, filed with the build.
- **Adversarial half.** The gate suite includes: a mask
  texture missing or zeroed (the pass must fail closed —
  full-region censor — never fail open); a driver pushing
  cell size outside the clamp (clamped, and the clamp event
  logged); a build attempted with no profile named (build
  error, proven); a variant-stripping sabotage case (stripping
  disabled → the built-player census must catch the
  unselected path's presence and fail the build).

## Skin, wetness, and fluid authoring

Original NSFW Unity work: the Ranch's own characters in the
Ranch's own scenes. Everything in this section is authored
from estate-original specs; where a spec's starting values
came from a studied-game measurement, the spec cites the
census record and the measurement, and the implementation is
written from the spec (Tier A).

Terminology, once, per the estate register: in Unity text the
geometry deformations are **blend shapes** on a
SkinnedMeshRenderer; the surface itself is a **Material**
asset driven by a Shader. This section is about the surface.
Expression *geometry* lives in the facial-rigging notes and
`DADDY_STYLE_UNITY.md`; expression *surface state* lives in
the next section.

### The skin layer stack

A Ranch skin shader is URP, custom ShaderLab (or Shader Graph
with named custom functions where the title's tooling demands
it — the layer contract is identical), and its fragment
lighting is an ordered stack of named layers. A layer not in
the stack does not get added ad hoc in a material; the stack
is the shader's contract, and changing it is a shader change
with a census and golden frames, not a material tweak.

1. **Base diffuse.** Albedo with wrap lighting; the wrap
   coefficient is a named property with a named range, not a
   literal in the code.
2. **Subsurface approximation.** One named class per title —
   thickness-tint or view-dependent backlight — fed by an
   authored thickness mask. Exactly one class: stacking two
   approximations is how skin turns to wax, and the census of
   studied titles shows the held references pick one.
3. **Specular.** Dual-lobe (broad sheen, tight highlight)
   with an authored roughness mask. The specular intensity
   range is a named property range in the spec.
4. **Wetness.** A state layer, not a look: a wetness mask
   (authored: where wetness gathers) times a wetness *state*
   value (runtime: how wet, 0–1, a named property with the
   range in its name or its spec entry). Wetness lowers
   roughness and raises specular response inside the mask,
   and may add a clearcoat-class second highlight. The state
   value is written by exactly one named driver (the scene's
   state system), slew-bounded by `STATE_SLEW_MAX` — wetness
   that pops is a transition defect under the same discipline
   as the censor's.
5. **Sweat.** Beads and sheen as a specular sparkle layer:
   a noise-based glint term inside an authored sweat mask,
   density and glint scale as named properties. Sweat is a
   specular phenomenon in the Ranch model; a sweat *albedo*
   darkening term is a defect (it reads as dirt at judging
   size) unless a title's spec names it deliberately.

Every layer's inputs are properties with ranges; every mask
is a named texture slot with a stated channel packing (which
channel carries thickness, which carries roughness
variation, which carries wetness) written in the shader's
spec, so a texture authored for one character fits the next.

### Fluid decals

Fluids that live on skin or surfaces are **decals**, in one
of two named shapes:

- **URP Decal Renderer Feature projectors** for placement on
  arbitrary geometry, with the projector's render queue,
  layer filter, and draw distance named in the scene spec; or
- **Mesh decals** (a fitted surface patch wearing the fluid
  material) where the surface is known and stable — the
  default on characters, because a projector's box on a
  deforming SkinnedMeshRenderer is a standing artefact risk.

The fluid material's contract: fresnel-weighted alpha
(fluid reads by its specular and its edge, not by a flat
tint); a thickness tint term (thin = near-clear, pooled =
tinted, tint named per fluid in the title's spec); drip
streaks, where a title uses them, as a UV-stretched noise
scroll with a named, bounded scroll speed — a drip is a
state with a rate, never an unbounded time-scrolled texture
whose speed nobody chose. Sorting is contractual: the decal's
render queue and depth-write setting are named in the spec
(fluid decals do not write depth; a fluid that writes depth
z-fights its host surface and the golden frame catches it —
studied titles ship this defect; the Ranch does not adopt
it). Lifetime is a named fade (in and out, each at least the
title's named minimum, and never a pop), driven by the same
single state driver discipline as wetness.

Runtime fluid *simulation* (a render texture the fluid
paints into) is out of the default contract: it enters a
title only with its budget named up front — resolution and
update rate under `FLUID_RT_MAX`, one named owner system,
and a determinism note (a sim that cannot reproduce its
state from the scene spec cannot be golden-tested, and says
so in the spec instead of pretending otherwise).

### Performance bounds for adult scenes

Adult scenes concentrate cost exactly where players look:
two or few characters, close camera, everything else cheap.
The bounds that follow from that shape:

- Per-character material count is named in the title's spec;
  skin, eye, and fluid materials are per-character by design
  (their state is per-character — see the next section), and
  the count is a census number in the build report, not a
  surprise.
- Skin and fluid shaders stay inside `SHADER_VARIANTS_MAX`
  with every keyword justified in the spec; a keyword that
  exists for one scene's sake is a uniform until proven
  otherwise.
- SRP Batcher compatibility is kept for everything except
  the named per-character state materials (which use material
  property blocks — next section), and the exception list is
  the spec's, not the profiler's discovery.

## Face and expression shader support

The surface half of the expression system. Geometry — blend
shapes, whole-eye material swaps of the kind the studied-game
census records (the Unity guide's `eyeLv` finding is the
reference construction) — is specified in the facial-rigging
notes. This section covers what the *shader* owes the
expression state system, and the boundary is strict:
**geometry deforms by blend shapes; surface state changes by
uniforms; neither impersonates the other.** A blush faked by
swapping a whole face texture hides the state from the
system; a pupil shape faked by a blend shape spends geometry
on a shading fact. Both are defects here.

### The state block contract

- Per-character expression surface state travels as **one
  named state block**: a fixed set of properties (tint
  intensities, layer enables-as-values, pupil state) written
  by the title's expression state system and by nothing else.
  One writer, named in the spec — the same single-driver
  discipline as wetness.
- State is applied through **material property blocks**, not
  runtime material instances. A `Material.Instantiate` (or an
  accidental `.material` access that clones) inside a scene
  is a defect: it allocates, it breaks batching silently, and
  it makes the character's true state un-censusable. The
  build census counts materials; a count that grows between
  two runs of one scene is a gate failure.
- Every state value has a named range in the spec and is
  clamped at the writer. The shader trusts the range (it is
  a contract, not a hope) and the adversarial tests attack
  the writer, not the shader (below).
- Every state value is slew-bounded by `STATE_SLEW_MAX`.
  Expression surface state never steps: a blush that snaps on
  in one frame is a transition defect under the OE-1b
  discipline, judged from timed captures like the censor's.

### The named layers

- **Blush / heat tint.** A tint layer inside an authored
  face mask (cheeks, nose bridge, ears where the title's art
  puts it), intensity = state value, tint colour = named
  property. Heat tint on the body reuses the skin stack's
  wetness-era machinery (a tint term inside the body mask),
  driven by the same state block — one state, two surfaces,
  never two drivers disagreeing about one character's state.
- **Tear film.** A specular layer, not a colour layer: tear
  film raises the specular response and adds a clearcoat-
  class highlight inside an authored eye-and-cheek mask,
  intensity = state value. Tear *streaks* (a track down the
  cheek) are a mask variant authored per title, selected by
  state value ranges, not by texture swaps at runtime.
- **Sweat (face).** The skin stack's sweat layer, masked to
  the face: same layer, same properties, face mask. A second,
  face-only sweat implementation is a defect — two sweat
  models on one head disagree at the hairline, at judging
  size, in the golden frame.
- **Eye shader.** The eye is its own small shader with its
  own contract: iris with parallax depth (an offset-sampled
  iris texture or a geometric iris — the title's spec names
  which), a cornea specular term, and **pupil shape as
  shader state**. Pupil-shape effects of the heart-pupil
  class are a named, enumerated state (a `pupil_state`
  property whose values are named in the spec — e.g.
  `ROUND`, `HEART` — with the set closed per title), rendered
  as a signed-distance pupil mask blended in the shader, and
  transitioned under the slew bound like every other state.
  The rules that keep this honest: the state set is closed
  (a new pupil shape is a spec change with golden frames,
  not a texture dropped into a folder); the state is set by
  the expression system as part of the character's expression
  state, never by a scene script reaching into the material;
  and the mechanism is named wherever the effect is judged —
  estate Rule 10: an expression component passes only from
  judged-size stills with its moving mechanism named and
  probe-verified, and a shader state's name is its mechanism.
  Where a title instead uses whole-eye material swaps for
  extreme states (the studied construction), the swap set is
  likewise closed, enumerated in the spec, and driven by the
  same state block; the two constructions never mix on one
  character.

### Expression gates

- Golden frames per expression state at judging size: each
  named state (and each pupil state) rendered on the title's
  reference head, judged whole-image against its spec — the
  visual evaluation doctrine applies (expected-vs-seen,
  crops from the final render at viewing size), and a state
  that only reads at 400% zoom has not passed.
- State-block census: a headless run writes every state value
  the driver can produce and reads them back from the
  property blocks; the set matches the spec's enumeration
  exactly — no orphan values, no unlisted states.
- Adversarial half: out-of-range writes (clamped, logged);
  two writers racing one block (the census's writer list
  makes the second writer a build-time find, and the test
  proves the find fires); a missing face mask texture (tint
  layers fail to *no tint*, never to full-face tint — the
  mask's absence must read as the layer off, and the golden
  frame for the missing-mask case is in the suite).

## Converters, determinism, and golden tests

Per the CODE-FIRST doctrine and D-1397 (shipped animation is
code; compiled artefacts are frozen and hashed), shaders are
build artefacts with the same discipline:

- **Shader compilation is a gate, not a hope.** Every Ranch
  shader compiles through the Editor batchmode route the
  Tiger HLSL guide names, and the compile log is the
  evidence: a shader with warnings is a failing gate until
  each warning is fixed or individually waived in the run
  record with a reason. No shader ships from an interactive
  session's say-so.
- **Variant census per build.** Each build's report carries
  the per-shader compiled-variant count (the number
  `SHADER_VARIANTS_MAX` bounds), derived from the built
  player. A count that changes between two builds of one
  commit is investigated as a determinism failure, not
  shrugged at: variant sets are a function of code and
  stripping configuration, both checked in.
- **Frozen, hashed specs.** A title's shader spec — layer
  stacks, state blocks, profiles, mask packings — is a
  checked-in document; the golden frames cite the spec's
  hash, so a frame can always be traced to the contract it
  judged.
- **Golden frames are the visual gate.** Numeric checks
  (variant counts, cell sizes, transition durations) support
  the verdict; the verdict on how a shader *looks* comes from
  judged frames under the visual evaluation doctrine, with
  an honest FAIL exemplar beside each item where one exists.

## RE alignment

How this guide's census relates to the estate's Unity study
programme (the full treatment is `DADDY_STYLE_UNITY.md`'s RE
alignment section; this is the shader layer of it):

- The pipeline is census → STUDY record (measured facts) →
  BUILD-BRIEF (spec) → authored original implementation.
  No importer reads a studied game's shaders into a Ranch
  project, and no shader finding skips the spec stage: a
  finding that cannot be stated as a spec (a class, a
  property contract, a measured range) has not been
  understood yet, however much source was read.
- Parity claims are two-tier, as in the Unity guide:
  structural parity from the census (the Ranch shader has
  the same layer classes and state contract as the measured
  reference) is claimable from static evidence; behavioural
  parity (it *moves* like the reference) needs rendered
  evidence judged under the visual doctrine — and for held
  references, judged against captured reference frames the
  Owner supplies, since the held game is never run by the
  Ranch.
- What Torogao and lumen take from Unity shader findings
  arrives as specs in their own terminology (estate-neutral
  text uses the register's crosswalk: a Unity blend shape is
  a morph target in glTF terms, a shape key in Blender
  terms). Shader *models* transfer as measured classes;
  shader *code* never transfers at all, to any engine,
  including back into Unity.

## Daddy Style treatment

Safety > performance > developer experience, applied to
HLSL/ShaderLab surfaces. Rules are alphabetical by topic;
each names its evidence or its status as a Ranch rule.

- **Assets are untrusted input.** A studied game's bundle, a
  bought shader package, a downloaded Shader Graph — all are
  inspected and censused before use, and studied-game
  material is never imported at all (RE boundary). A
  third-party shader that enters a Ranch title enters as
  source the Ranch can read, compile-gate, and census; a
  compiled-only shader asset is unmeasured by construction
  and does not ship.
- **Bounded work.** Variant budgets, fluid RT budgets,
  census file bounds, slew bounds (Bounds table). An
  unbounded shader cost — an uncounted keyword set, an
  unbudgeted render texture — is a defect at spec time, not
  a profiler surprise at ship time.
- **Censor is a build fact.** One profile per build,
  unselected paths stripped and the stripping verified in
  the built player, no runtime profile toggles, no
  unselected assets riding along (censor section).
- **Explicit contracts.** Every shader declares its layer
  stack, its property ranges, its mask packings, and its
  state drivers in its spec. A property with no range or a
  state with two writers is a contract violation found by
  census, not a style preference.
- **No hidden behaviour.** No runtime material cloning, no
  time-scrolled effects with unchosen rates, no keyword
  branches keyed off unlogged state, no shader-side random
  that a golden frame cannot reproduce. If a frame cannot be
  re-rendered identically from the spec and the state, the
  effect that breaks it is named and bounded or removed.
- **One writer per state.** Expression, wetness, fluid, and
  censor state each have exactly one named driver system.
  This is the shader form of the estate's single-writer
  discipline, and the censuses exist to prove it holds.
- **Safety outranks look.** OE-1b slew and transition bounds
  bind even when a faster transition would read better in a
  still. A gate that trades a flicker hazard for a prettier
  frame has the priorities inverted and fails review.
- **Studied means studied.** Census findings are cited as
  measurements with provenance; an implementation "inspired
  by" a held game that cannot name its spec is an unadmitted
  copy risk and is treated as one until the spec exists.

## Testing

Half validation, half adversarial, per the estate split.
Validation: compile gates clean; variant census within
budget and stable across rebuilds; golden frames per skin
state, per expression state, per censor profile; transition
durations measured within bounds. Adversarial: missing and
zeroed masks (fail closed for censor, fail dark for tint);
out-of-range and dual-writer state attacks; stripping
sabotage; resolution extremes (720p / 2160p) for the cell
contract; a held-tree census attempted over the file bound
(stops at the bound, names the slice). `TEST_RETRIES_MAX`
is 0: a failing gate is a finding, not a dice roll.

## USE — agents

This is the summary; the full agent surface is "Agent use"
above. The decision order for any HLSL/ShaderLab task:

1. Is it a studied game's shaders? → Static census on a
   scratch copy, record per the census section, stop at
   anything that needs the game running. Nothing ships from
   it; findings become specs.
2. Is it a censor question? → The profile is a build
   definition. Check the built player's census before
   believing any claim about what a build contains.
3. Is it authoring for a Ranch title? → Write against the
   title's shader spec (layer stack, state block, mask
   packing); a need the spec doesn't cover is a spec change
   first, code second.
4. Is it general URP discipline (pass structure, batcher,
   keyword hygiene)? → The Tiger Style HLSL guide governs;
   this guide adds nothing there.
5. Does it need a live Editor or a running held game? → The
   Editor route is the Unity guide's, gated as there. The
   held game route does not exist.

## USE — the Owner

Plain version: you almost never need to open a shader to
check on it. The census tells you what a studied game
actually ships, the build report tells you which censor
profile a player actually contains and how many variants its
shaders compiled to, and the golden frames show you what the
skin, the wetness, and the face states actually look like at
the size they'll be judged.

Mechanism, briefly: a Unity *shader* is a checked-in text
asset that the Editor compiles into per-platform GPU
programs, in variants — one program per keyword combination.
That is why this guide is so strict about keywords and
stripping: what ships is the variant set, and the variant
set is exactly what a build census can count. A censor
profile enforced by variant stripping is enforced by the
*absence* of the other path's programs in the file, which is
a fact you can verify after the build instead of a promise
made before it.

The worked judgements below are the Ranch's everyday ones:
accepting a studied-game census (does the record carry its
provenance, are the unmeasured fields named, is there any
copied code in it — there must be none); accepting a censored
build (does its built-player census show the other profile's
keywords and textures absent, and do its golden frames show
the mask complete at both resolutions); and accepting an
expression state (the judged-size still, with the shader
state that produces it named — a face you cannot trace to a
named state has not been gated, however good it looks).

## UNVERIFIED register

Every **U** in this guide, gathered with its reason. A **U**
claim carries no load until its probe runs.

- **Live3D's own shader surface** — the estate census covers
  the Editor/Maker assemblies; a per-shader census of the
  held Live3D tree under this guide's method has not run
  yet. Every Live3D-specific shader statement in this guide
  is therefore a method statement, not a finding, until that
  census lands.
- **The build-target project's URP package version** — this
  guide is written against URP as the 6000.6.6f1-era package
  line presents it (**D**, URP documentation); the exact
  package version in each Ranch project's manifest was not
  re-censused for this guide, and pass-ordering details that
  differ by URP version must be re-derived per project
  before a censor feature is built on them.
- **Standalone HLSL compilation as a pre-Editor gate** —
  whether a `dxc`-class standalone compile can usefully
  pre-check Ranch ShaderLab HLSL (which is meaningful only
  inside Unity's include environment) is unsettled; the
  Tiger HLSL guide's Editor-batchmode compile gate is the
  route of record until a probe proves a standalone route
  adds signal.
- **Decal projector behaviour on skinned meshes** — stated
  above as an artefact risk on general grounds (**D**, URP
  decal documentation describes the projection model); no
  Ranch run has measured it on a Ranch character, and a title
  that wants projectors on characters owes that probe before
  the choice is made.
- **Studied-title fluid update cadences** — no held title's
  fluid driver cadence has been measured under this guide;
  the census records cadence where IL states it, and the
  field is expected to read `unmeasured` in early records.
