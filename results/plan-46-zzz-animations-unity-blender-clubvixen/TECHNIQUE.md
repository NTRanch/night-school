# Plan 46 — Pass 2 Technique Sheet (Distillation)

Source: TheClubVixen, "How To Import Zenless Zone Zero Animations
Into Unity3D" (YouTube so6jjN1lbgM, 25:39). Study run: 2026-11-24,
fathom route. **Confidence: VERIFIED** (full transcript; ARP retarget
frames agree). The fullest pipeline in the set: extract a character's
game animations, retarget them onto a high-quality model, export to
Unity. Blender 5.2.0 LTS, Auto-Rig Pro Remap. Admitted: extraction +
retarget craft. Timestamps from the transcript; name-level details
are single-transcriber ASR (treat codenames as PARTIAL).

- **T1 — Build the game-specific extractor (00:00:30–00:02:00).**
  AnimeStudio's **ACL branch** — the ZZZ-specific fork — built from
  source in VS Code: **Release** configuration (not Debug), .NET
  9.0, Build Solution. The game-specific branch is slower than the
  generic build but correct for this game.
  → **Adopt** as bookkeeping for the reference pipeline: the ZZZ
  animation route needs the ACL (game-specific) fork, Release build.
- **T2 — CAP map + Asset Map, rebuilt per update (00:02:15).** Build
  both maps from the game's
  `ZenlessZoneZero_Data/StreamingAssets/Blocks` folder. **After
  every game update, rebuild the maps** or new content silently
  won't appear. Also launch the game itself once, so assets and
  shaders that download on demand exist locally. (Files involved
  are large: the demo character ≈ 562 MB with maps; some ≈ 2.6 GB.)
  → **Adopt as a standing census rule**: any game-side census is
  valid only against maps built from the current game version;
  stale maps silently omit new content.
- **T3 — Animation is name-bound to its model (00:03:36).** Clips
  bind by name: an outfit variant whose bone naming differs will
  not animate. Relatedly, do **not** Shift+Add when assembling an
  embedded-FBX export set — it breaks the linkage.
  → **Adopt** as a census rule: clips marry models by name — a
  variant with renamed bones is a *different* animation target.
  Record bone-name identity before assuming transfer.
- **T4 — Census by Name + Type (00:04:30).** In the asset browser:
  **AnimationClip** = the animation file, **Animator** = the rigged
  model. Characters follow `Avatar_Female_Size##_<Name>` naming,
  and in-game codenames differ from display names — community
  character-ID lists map them. Select by name + type, then
  Shift-collect *all* of a character's clips.
  → **Adopt**: AnimationClip vs Animator type discipline +
  codename↔display-name mapping tables are census prerequisites
  (cf. Plan 47 T5).
- **T5 — Export Animator + selected Animation Clips (00:07:38).**
  Select from an Animator (clicking a clip decompresses it),
  Shift-select everything, right-click → **Export Animator +
  selected Animation Clips**. If the export comes out
  distorted/bindpose-wrong, export each candidate animator and keep
  the one that looks right — duplicates of the same name are
  partial/full variants, and the exporter cycles to the first
  compatible one (the "UI" variant often looks best).
  → **Adopt** as procedure for the reference pipeline; "export each
  candidate, keep the one that looks right" matches the estate's
  verify-don't-trust posture.
- **T6 — The LOD trap (00:09:36).** The game-side export defaults to
  **LOD3 — the lowest detail** (fingers come out coarse), though all
  animation is present. The high-quality model must be sourced
  separately (a HoyoToon-linked character download site) and the
  animations married to it — which is what the retarget half of the
  video exists for.
  → **Adopt as a census rule**: verify LOD before any study use of a
  game-side export. A LOD3 model silently degrades finger/face
  census — the same failure class as the estate's past census
  corrections.
- **T7 — Zero the target's root offset before retargeting
  (00:12:30).** Import the raw animated export and the HQ model with
  identical settings. HQ downloads can float: his example sits at
  Location Z **0.021249** — set it to **0** and confirm in Edit-Mode
  rest pose that the two armatures coincide exactly before any
  remapping.
  → **Adopt as an intake check**: root offsets on imported reference
  models are zeroed and verified before any measurement. A 21 mm
  float would poison proportion tables (the C1 instrument
  discipline).
- **T8 — Census the curves before retargeting (00:13:30).** Dope
  Sheet → Action Editor, per-bone view: read which bones actually
  carry motion. The remap list is built from evidence, not from the
  full skeleton.
  → **Adopt**: the retarget table is built from the curve census,
  not the full skeleton.
- **T9 — Remap discipline (00:14:40–00:15:39; frame-verified).**
  Auto-Rig Pro Remap, source = raw armature, target = HQ armature.
  **Pelvis must be set as root** (at least one root is required).
  **Props need "Location Local" enabled** — the gun (Prop 1)
  otherwise lands translated away from the hand; the same applies
  to magazine/bullet sub-props. **Prune non-bones** from the mapping
  list (FX Root, Skin Root, R Foot Root Fix, GunPoint). Repair
  missing mappings by name fragment. **Save the mapping as a
  preset** — it is reused across the character's other skins.
  → **Adopt the discipline wholesale** into the estate's own
  retarget table work — it speaks directly to the import
  programme's current dominant error (the retarget stage). The tool
  is **not** adopted (see Conflicts).
- **T10 — Never Auto-Scale same-size models (00:18:58).** Auto-Scale
  between a source and target of the same size corrupts the
  translations. Leave it off.
  → **Adopt as a retarget rule**: same-size source/target → no
  auto-scale; translations corrupt otherwise.
- **T11 — Prove one clip, then batch (00:14:40, 00:20:30).** Leave
  Multiple Source Animations **off**; retarget a single clip and
  verify it end-to-end (gun seated in the hand; unmapped parts
  visibly lag until given Location Local). Only then enable
  **Multiple Source Animations → Retarget** and batch the set.
  Delete the old hierarchy, export FBX with animations; Unity
  import preserves textures and fidelity.
  → **Adopt (corroboration)** of the standing estate batch rule (one
  item first, batch after proof) — here with a concrete proof
  image: the prop seated in the hand.

## Conflicts — flagged, not silently adopted

- **Auto-Rig Pro.** A paid third-party addon; the estate's
  rig-tools RE study already priced ARP and dropped the purchase
  (2026-11-24). The remap *discipline* is adopted into the estate's
  own retarget table; the tool is **not bought** and is never a
  curriculum recommendation.
- **Extracted game models/animations.** Tier A: study, measurement
  and reference only — never shipped. The video's end goal (game
  animations exported to FBX and reused in Unity) is not an estate
  output route; shipped animation is code (D-1397 scene specs).
- **Version drift.** The video runs Blender 5.2.0 LTS; the estate
  pins Blender 5.3 (official build for IK-carrying files).
