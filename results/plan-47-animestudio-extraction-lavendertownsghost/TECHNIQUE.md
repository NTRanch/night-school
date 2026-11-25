# Plan 47 — Pass 2 Technique Sheet (Distillation)

Source: LavenderTownsGhost, "AnimeStudio Setup and Model Extraction
Tutorial" (YouTube cLzMA0YEGhQ, 16:18). Study run: 2026-11-24,
fathom route. **Confidence: VERIFIED** (full transcript; intake
frames agree). Genshin-side extraction plus a Blender
intake-cleanup routine. Blender 4.4.3 in the video. Admitted:
extraction census + import hygiene. Timestamps from the transcript.

- **T1 — Game profile before maps (00:01:15).** Options → Select
  Game → Game Type "Hoyo Game" → title → Live version, confirm —
  the tool's whole file grammar follows from this profile.
  → **Adopt** as bookkeeping for the community extraction route
  (cross-checks against the estate's fathom/bundle-reader routes,
  which stay primary).
- **T2 — Scale Factor 100 (00:02:15).** Export Options → **Scale
  Factor = 100**, so Unity-scale models land at a Blender-workable
  size on export instead of needing per-import rescaling.
  → **Adopt** as the community-route export convention when that
  route is used.
- **T3 — Map build and the CAB gotcha (00:02:52–00:05:30).** Name
  the map set; Map Type = **MessagePack**; **Build Both**; point at
  `<Game> Data/StreamingAssets/AssetBundles/Blocks` (≈24,000 blocks
  for Genshin; ≈1 h of processing on his machine). The gotcha he
  flags twice: the **CAB map always saves into the tool's own
  `maps/` folder**, whatever destination the Asset Map (.map) was
  given — load each map from where it actually is.
  → **Adopt** as tool bookkeeping; record it in the route notes so
  the next census doesn't lose an hour to it.
- **T4 — Filter by Type to cut noise (00:07:30).** In the Asset
  Browser's type selector, deselect **AnimationClip** when hunting
  models (and the reverse when hunting animation) — the result set
  shrinks by orders of magnitude.
  → **Adopt** as census ergonomics, general.
- **T5 — The naming grammar (00:08:00–00:09:40).** Playable
  characters: `Avatar_<Body>_<Weapon>_<Name>` — Body classes:
  **Boy** (short male), **Girl** (short female), **Lady** (tall
  female), **Loli** (child girl), **Male** (tall male). Outfit
  variants: `<Name>Costume<Variant>`; a **TT** suffix marks the
  censorship-changed skins. Internal names ≠ display names (Amber
  is stored as "Ambor"; Jean's stored name likewise differs — ASR
  renders it unclearly, the codename point stands). A file path
  becomes a search string by replacing slashes with underscores. A
  community file index ("Anime Extraction Project") documents the
  grammar per game version.
  → **Adopt as census grammar** for the Genshin-side reference set;
  the ZZZ-side equivalent is Plan 46 T4's
  `Avatar_Female_Size##_<Name>`. Variant enumeration (costumes, TT)
  is how a character's full model family is found.
- **T6 — Pick the real container, not the helpers (00:09:40).** The
  wanted Animator is the one whose hierarchy contains **Trigger** +
  the character's own name + **Dummy**. Avoid entries named
  **Edit**, **Ragdoll** or **Mannequin** — helper variants, not the
  playable model.
  → **Adopt as a census rule**: helper rigs are a wrong-census trap
  — same class as the estate's "shared material fools naive census"
  correction. Assert container identity before counting anything.
- **T7 — Export Models/Objects (00:10:30).** Export → Models
  Objects → Export Selected → an FBX plus its texture set.
  → Procedure of record for the community route.
- **T8 — Material repair on intake (00:11:38–00:11:54).** In the
  Shading workspace, per material: (a) **disconnect the Alpha→Alpha
  link** on the Principled node (kills the broken transparency),
  (b) set the colour image texture's alpha mode to **Channel
  Packed**. Repeat for every material; finish back on the first
  material (hair) so the selection state is sane. Why: Unity FBX
  exports carry packed alpha conventions that Blender's default
  node wiring misreads — the model looks black/funky until the
  alpha path is fixed.
  → **Adopt as a named intake-cleanup step** for Unity-FBX
  reference imports — after re-verification on the pinned Blender
  5.3 build (see Conflicts).
- **T9 — Helper hygiene (00:12:30).** The import litters the scene
  with small helper/dot objects; hide them all so they can't be
  mis-selected during any later modelling.
  → **Adopt** as intake hygiene (helpers must not be mis-selected
  or miscounted as geometry).
- **T10 — Effect meshes, eye stars, and the duplicate eye shell
  (00:13:14).** Hide the **Effect** mesh (a spurious "dress"
  volume) and **EyeStar**. Some characters carry a **duplicated
  mesh shell over the eyes**: select Face_Eye → Edit Mode →
  face-select → hover a face and press **L** (Select Linked) →
  Delete Faces. The face reads correctly only once the duplicate
  shell is gone.
  → **Adopt as a named import-defect class**: imported references
  can carry a duplicated eye shell. Prima's eye census on any
  imported reference should assert exactly one shell per eye.
- **T11 — Save the cleaned intake (00:14:30).** Save the .blend with
  the texture fixes and hides applied, so the cleanup is performed
  exactly once per model.
  → **Adapt (corroboration)** — the estate already saves intake
  states.

## Conflicts — flagged, not silently adopted

- **Version drift.** The video runs Blender 4.4.3; the estate pins
  Blender 5.3 (official build for IK-carrying files, per the
  two-build rule) and mmd_tools 4.5.14. Every adopted mechanism must
  be re-verified on the pinned build before it becomes a checklist
  item — T8's node operations in particular; UI paths do not
  transfer verbatim.
- **Extracted game models** are Tier A: study, measurement and
  reference only — never shipped.
