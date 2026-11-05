# Unreal Python / API reference (UE 5.8.0)

> Companion reference for the Ranch's house style guide for Unreal Engine, adapted for adult game production — the morph-target and pose APIs behind the Ranch's character and facial work. Part of Night School.

Companion to `DADDY_STYLE_UNREAL.md`. All facial items are settled in the Ranch's facial-rigging notes / `VERIFY-facial.md` and cited, never re-derived. Marks as in `unreal-cli.md`. Entries alphabetical.

| API | Shape / fact | Evidence |
|---|---|---|
| `unreal.MorphTarget` (`UMorphTarget`) | Class exists; 63 `MorphTarget` objects on the KiteBoy head in Probe 4 | **R** Probe 4; **S** `Engine/Source/Runtime/Engine/Classes/Animation/MorphTarget.h:227` |
| `unreal.PoseAsset` (`UPoseAsset`) | "Pose Asset that can be blended by weight of curves" | **S** `Animation/PoseAsset.h:311-315`; **R** this leg (attribute present) |
| `USkeletalMeshComponent::SetMorphTarget` | `void SetMorphTarget(FName MorphTargetName, float Value, bool bRemoveZeroWeight=true)`; Python: `set_morph_target` (with `clear_morph_targets`, `disable_morph_target`, `get_morph_target`) | **S** `SkeletalMeshComponent.h:1347`; **R** Probe 4 (existence/signature; live in-game call not probed) |
| `SkeletalMesh.get_all_morph_target_names` | Verbatim census returned 63 morph names on each of two skeletal meshes | **R** Probe 4 |
| Anim curve → morph matching | Curves of type `MorphTargetCurve` collected by name into `TMap<FName, float>`, applied to the component | **S** `AnimCurveTypes.h:32`; `AnimInstanceProxy.cpp:3597-3625`; `SkeletalMeshComponent.cpp:3383-3405` |
| `UFbxSkeletalMeshImportData.bImportMorphTargets` | "True to import morph target meshes from the FBX file" — the morph import gate | **S** `FbxSkeletalMeshImportData.h:89-91` |
| ARKit face channels | 52 channels (the ARKit-52 set) | **S** facial leg |
| Control Rig → morph / lid paths | No path found in source reads; rig graphs are asset data | **U** (facial register) |
| MetaHuman facial internals | DNA payloads are binary content | **U** (facial register) |

## Census script shape (Probe 4, cited)

The facial leg's `ue_morph_census.py` — load each skeletal mesh asset in the scratch project, call `get_all_morph_target_names()`, emit the names — is the canonical census shape for `uasset-census v1` (full guide). Run it only via the route in `unreal-cli.md`, only on a preflighted scratch copy.
