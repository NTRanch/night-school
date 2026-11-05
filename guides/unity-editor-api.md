# Unity Editor and runtime API reference (Ranch subset)

> This reference is part of the Ranch's house style for Unity,
> adapted for adult game production. It is part of Night School,
> the Ranch's public study programme.

Version basis: **Unity Editor 6000.6.6f1**. Signatures and
existence are read from the installed Editor's XML API docs
under `~/Unity/Hub/Editor/6000.6.6f1/Editor/Data/Managed/
UnityEngine/` — evidence **S** with file:line at each table.
Behavioural claims carry **R** (run, 2026-11-02, via
`VERIFY-facial-runs.md` Probe 3 unless another run is named),
**D** (citations by the Ranch's agent workers of the 6000.6
manual / ScriptReference, marked [A]), or **U**. This file is
the Ranch subset — the APIs
the guides, converters, and gates actually use — not a census
of the whole API. For facial mechanisms in depth, see the Ranch's
facial-rigging notes; this file cross-references them and does
not duplicate their treatment.

## Animation and rigging

| API | Evidence | Notes |
|---|---|---|
| `Animator.GetBoneTransform(HumanBodyBones)` | **S** AnimationModule.xml:3839 | Humanoid bone access. |
| `Animator.SetLookAtPosition(Vector3)` | **S** AnimationModule.xml:4351-4357 | "Sets the look at position for a character during animations." Applied in the IK pass: a layer's `iKPass` triggers `OnAnimatorIK` (**S**, UnityEditor.CoreModule.xml:1428). |
| `Animator.SetLookAtWeight(weight, bodyWeight, headWeight, eyesWeight, clampWeight)` | **S** AnimationModule.xml:4387-4406 | Every weight is 0–1; `eyesWeight` "determines how much the eyes are involved". The head/eye split is the gaze-coupling contract. |
| `HumanBodyBones` (`LeftEye`, `RightEye`, `Jaw`) | **S** AnimationModule.xml:5389-5424 (existence); values **R** Probe 3 | `LeftEye` = 21, `RightEye` = 22, `Jaw` = 23, read in-Editor by the supplementary probe. |
| `LookAtConstraint` | **S** AnimationModule.xml:2339-2343 | "Constrains the orientation of a GameObject based on the position of one or more sources." |
| `RotationConstraint` (`GetSource`, `SetSources`, …) | **S** AnimationModule.xml:3000-3029 | Couples rotation only — e.g. lid bones following eye bones without scripting. |
| `SkinQuality` (`Bone1`, `Bone2`, `Bone4`, `Auto`) | **S** CoreModule.xml:57132-57156 | The importer's default influence cap is 4 bones (**D** [A]); exports over the cap lose weights at import [A]. |

Humanoid contract (**D** [A], from the depth draft by the
Ranch's agent workers): each
humanoid model uses the Humanoid animation type with a
configured Avatar; configuration requires a T-stance / T-pose;
Generic animations do not use Avatars and need a named root
bone. Gates use a checked-in Avatar (Copy From Other Avatar),
never per-import auto-mapping [A, Ranch rule].

## Asset database and build (Editor API)

| API | Evidence | Notes |
|---|---|---|
| `AssetDatabase.FindAssets(string)` (+ folder overload) | **S** UnityEditor.CoreModule.xml:3509, :3519 | Result order is **not** guaranteed (**D** [A]) — sort by GUID or path before use. The facial census sorts by path. |
| `AssetDatabase.GUIDToAssetPath(string)` / `(GUID)` | **S** UnityEditor.CoreModule.xml:3937, :3946 | The GUID ↔ path bridge the meta audit relies on. |
| `AssetDatabase.LoadAllAssetsAtPath(string)` | **R** Probe 3 (exercised by `FaceCensus.Run`) | How the census reaches every `Mesh` sub-asset at a path. |
| `BuildPipeline.BuildPlayer(BuildPlayerOptions)` (+ profile overload) | **S** UnityEditor.CoreModule.xml:10124-10149 | The raw-route build entry. The profile overload is the Unity 6 form; the scene-array overload is marked for replacement in its own doc text. |
| `BuildPipeline.BuildAssetBundles(...)` | **S** UnityEditor.CoreModule.xml:10071-10094 | Bundle builds, for completeness of the build family. |
| `BuildPipeline.CleanBuildCache()` | **S** UnityEditor.CoreModule.xml:10154 | Gate builds are clean builds (**D** [A]: incremental builds can cache-poison; release/troubleshooting builds are clean). |
| `EditorApplication.Exit(int)` | **S** UnityEditor.CoreModule.xml:14407 | The explicit-exit half of the executeMethod failure contract (**D** [A] for the contract itself). |
| `ModelImporter.importBlendShapes` / `importBlendShapeNormals` / `importBlendShapeDeformPercent` | **S** UnityEditor.CoreModule.xml:36368-36383 | Blendshape import switches. Normals additionally require FBX smoothing groups [A]. |

Project facts these APIs operate on (**S**, read 2026-11-02):
`ProjectSettings/ProjectVersion.txt` carries
`m_EditorVersion` (Track B: `6000.6.6f1`); every asset's `.meta`
carries `fileFormatVersion: 2` and a 32-hex `guid:`; package
state lives in `Packages/manifest.json` (+ lock file).

## Blendshapes (facial subset)

Settled in the Ranch's facial-rigging notes; restated here only as an index
with its evidence, per the leg instruction to build on the
facial leg's findings and cite them.

| API / fact | Evidence | Notes |
|---|---|---|
| 0–100 weight convention | **R** Probe 3 | Frames added at weights 50 and 100 read back verbatim via `GetBlendShapeFrameWeight`; `SetBlendShapeWeight` / `GetBlendShapeWeight` round-tripped 0 / 50 / 100. The installed XML doc itself does **not** state the range (**S** read of the member). |
| `Mesh.AddBlendShapeFrame(name, frameWeight, deltas…)` | **S** CoreModule.xml:26549; **R** Probe 3 | Two frames under one name: `blendShapeCount` = 1, frame count = 2. |
| `Mesh.blendShapeCount` | **S** CoreModule.xml:57123 (member neighbourhood) | Count of blendshape *names*, not frames. |
| `Mesh.GetBlendShapeName(index)` | **S** CoreModule.xml:26743; **R** Probe 3 (twice: supplementary probe + the census itself) | The census's core call. |
| `SkinnedMeshRenderer.SetBlendShapeWeight(int, float)` | **S** CoreModule.xml:57119-57125 | Doc text says only "The weight for this BlendShape" — the range is the **R** row above. |
| `blendShape.<name>` animation-clip property path | **U** | The string appears in no installed XML doc read (facial leg). Settling it needs a clip-authoring run no probe performed. |
| 3D lid blendshape construction; UV-offset gaze | **U** | General practice claims with no first-party installed source (facial leg). |

## Packages bundled in the Editor distribution

Static census (**S**): the `.tgz` bundles under
`~/Unity/Hub/Editor/6000.6.6f1/Editor/Data/Resources/
PackageManager/Editor/`, read 2026-11-02 (facial leg + this
leg). "Bundled" means *installable from the distribution* —
presence in a project's `Packages/manifest.json` is a separate
fact, checked per project by `unity-package-census@1`.

| Package bundle | Version | In the flagship adult game's Track B manifest? |
|---|---|---|
| `com.unity.2d.animation` | 16.0.1 | No (**S**) — its Sprite Swap (Sprite Library) documentation is the verified 2D blink-swap route (facial leg). |
| `com.unity.formats.fbx` | 5.1.6 | No (**S**, this leg's listing) — the FBX Exporter package (round-trip export); import is built in. |
| `com.unity.scriptablebuildpipeline` | 3.0.3 | No (**S**, this leg's listing). |
| `com.unity.testtools.codecoverage` | 1.3.0 | No (**S**, this leg's listing) — the package `unity test --coverage` requires. |
| `com.unity.xr.arfoundation` | 6.6.2 | No (**S**) — carries `ARFace`, `ARFaceManager`, `XRFaceBlendShape` (facial leg). ARKit faces arrive through this package or as conventionally named blendshapes; the Editor itself has no built-in ARKit face table (facial leg). |

Also verified by listing: the BuiltInPackages tree carries
`com.unity.animation.rigging`, `com.unity.cinemachine`,
`com.unity.entities`, and the 2D feature packages (**S**).
Unity's primary model format is FBX (**D** [A]); `.blend` direct
import shells out to an installed Blender, so Ranch projects
never commit `.blend` into `Assets/` [A, Ranch rule]. No
first-party glTF/USD importer page was found in the 6000.6
manual by the Ranch's agent workers — treat glTF/USD import
as package-only
(**U** as a documented claim, [A] as the search report).

## Play mode, domain reload, and rendering (Ranch rules)

- **Enter Play Mode default = Reload Scene only** (**D**
  [A]): the scripting domain is not reloaded by default, so
  static variables keep their values and static events keep
  their subscribers between Play sessions (**D** [A]). The
  full-reload behaviour is opt-in via Enter Play Mode options
  (**D** [A]). Ranch rule: reset statics with
  `[RuntimeInitializeOnLoadMethod(SubsystemRegistration)]` or
  assert fresh state; a Play-mode pass without this is not
  evidence.
- **Render pipelines** (**D** [A] + Ranch ruling): the
  Built-In Render Pipeline is deprecated (supported, with bug
  fixes, through the Unity 6.7 LTS lifecycle); URP does not
  support surface shaders. Ranch ruling 2026-10-19: new
  content is URP-only, custom shader for the cel look, F2
  control capture on the built-in project precedes the Track B
  migration (staged note, **S**). Track B's manifest still has
  no render-pipeline package (**S**, 2026-11-02).
- **Deterministic builds, first-party shape** (**D** [A]):
  identical output requires identical source, assets, and
  settings; the commonest cause of divergence is mismatched
  environments (Editor version, toolchains, float behaviour);
  lightmap rebakes diverge even with identical lighting, so
  gates do not rebake per build; `-consistencyCheck` is the
  importer determinism check. Ranch addition: `git config
  core.autocrlf false` is set **per-repo**, never `--global`
  [A, boundary rule].

## Sprites and masks (2D subset)

| API | Evidence | Notes |
|---|---|---|
| `SpriteMask` (`alphaCutoff`, `frontSortingOrder` / `backSortingOrder`, `isCustomRangeActive`) | **S** SpriteMaskModule.xml:7-41 (facial leg) | Masks Sprites and Particles; the sorting range is the aperture's membership rule. |
| `SpriteRenderer.maskInteraction` | **S** CoreModule.xml:58169-58173 (facial leg) | "Specifies how the sprite interacts with the masks." |
| `SpriteMaskInteraction` {`None`, `VisibleInsideMask`, `VisibleOutsideMask`} | **S** CoreModule.xml:58021-58041 (facial leg) | The aperture membership enum. |
| `SpriteRenderer.sprite` | **S** CoreModule.xml:58179-58183 (facial leg) | A single property, "The Sprite to render" — one renderer, one sprite at a time: the single-slot basis for hard swaps. |

## Time, physics, and capture

| API | Evidence | Notes |
|---|---|---|
| `Physics.Simulate(float)` | **S** PhysicsModule.xml:3799 | Manual stepping when simulation mode is Script — the deterministic-gate route (**D** [A] for the best-practice framing). |
| `Physics.simulationMode` | **S** PhysicsModule.xml:3288 | Controls when simulation executes. The Ranch's agent workers also cite Enhanced Determinism and per-scene physics for stronger guarantees (**D** [A]); "true determinism with PhysX has other challenges" (**D** [A]) — cross-machine bit-identity is never promised. |
| `Random.InitState(int)` | **D** [A] | "Initializes the random number generator state with a seed." The seeded-RNG half of the determinism gate set. |
| `ScreenCapture.CaptureScreenshot(path)` | **D** [A] | The simple capture route; gate captures prefer an explicit `RenderTexture` + `ReadPixels` (Track B pattern) so size and colour handling are named. |
| `Time.captureFramerate` | **S** CoreModule.xml:61477 | Setting it also sets `captureDeltaTime` to the inverse (**D** [A]); 0 = real time in both (**D** [A]). |
| `Time.fixedDeltaTime` | **S** CoreModule.xml:61487 | "A value of 0.01 means each fixed time step is one hundredth of a second" (**D** [A]) — and "in practice the interval between fixed updates isn't fixed" (**D** [A]). |

## UNVERIFIED in this file

Alphabetical; each is also in the full guide's register.

- `blendShape.<name>` clip property path — needs a
  clip-authoring run.
- Editor (raw argv) exit-code table beyond code 1 — partially
  documented only.
- glTF/USD first-party import — no manual page found [A];
  package-only until a package is named and probed.
- Pipeline package APIs (`CliCommand` authoring, command list
  contents) — no instance was reachable to enumerate (**R**:
  zero instances); the CLI's bundled text describes the shape
  (**D**) but no Ranch workstation project carries the package (**S** for
  Track B).
