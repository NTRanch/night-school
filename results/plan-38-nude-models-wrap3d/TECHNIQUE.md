# Plan 38 — Pass 2 Technique Sheet: Template-Wrap Conforming (R3DS Wrap)

Distilled from Pass 1 (OBSERVATION.md; claim numbers C-n
there). Tool of record in the source: R3DS Wrap 2021.11.3.
**DEVIATION (declared up front): Wrap3D does not exist in
the estate** (probe: primo + sandbox — no binary, no install,
no licence; Wine exists on primo but carries no Wrap3D).
The Pass 3 rebuild therefore reproduces the pipeline with
the estate stack (Blender 5.2.3 LTS: Shrinkwrap Project +
Surface Deform + Data Transfer) and the estate anchor set
(SIX-GIRL-STANDARD §6). The contract, the grammar, and the
lie-zone map below are tool-neutral; values that exist only
inside Wrap are marked UNTESTABLE-IN-ROUTE and are never
faked in the rebuild.

## 1. THE WRAP CONTRACT — precondition checklist

Each item states the precondition, the failure it predicts
when skipped, and its Pass 3 validation route. (Validation
outcomes are recorded in PASS3-REBUILD.md; an item whose
skipped failure does not reproduce is STRUCK there, with
evidence — it is not kept on faith.)

| # | Precondition | Predicted failure if skipped | Evidence in source |
|---|---|---|---|
| W-1 | Both meshes cross the tool boundary under an explicit interchange contract: modifiers applied, vertex order kept, normals + UVs + material groups written, one scale/axis convention (OBJ: Selection Only, Apply Modifiers, Keep Vertex Order, −Z fwd / Y up, scale 1.00). | Group/UV loss downstream; point indices silently rebind. | Export dialog read in full at 32:30; narration V-1 repeats "apply modifiers… keep vertex order" as instruction. |
| W-2 | Template and target are pre-aligned in scale and pose BEFORE the wrap tool; the wrap tool applies identity transforms only. | The solver spends its budget on rigid mismatch; landmark error everywhere, worst at extremities. | Both LoadGeom editors: Translation/Rotation 0, Scale 1 (37:30, 40:00). Alignment corrections happen Blender-side (110:00 rotation) — never in Wrap. |
| W-3 | The template carries NAMED polygroups/materials for every anatomical region (Face, Lips, Teeth, Ears, EyeSocket, Mouth, Pupils, Cornea, Irises, Sclera, EyeMoisture, Torso, Arms, Legs, nails…). | Subsets can only be hand-lassoed → inconsistent exclusions between runs and operators. | The 17-group list read from the − Material dropdown (50:00/55:00); groups survive the round trip as Blender material slots (97:30). |
| W-4 | Subsets on BOTH sides exclude anatomy with no correspondence on the other side (eyeball parts, teeth, mouth interior, eye moisture) BEFORE solving. | The solver drags surface verts into cavities; socket/mouth lies (C-7) get worse and less local. | Two SelectPolygons→Subset chains, one per side (graph, 35:00); cleanup still needed at eyes/mouth even WITH subsets (100:00–105:00) — the map in §3 prices what remains. |
| W-5 | The correspondence point set must MATCH the current geometry pair. A set authored against other geometry is cleared, never reused. | Silent misbinding: points anchored to triangles of a different mesh deform the wrap toward a stranger's face. | 57:30: 127 stale points + "Points does not match geometry" warning → Clear All → restart from 5. The single most quotable failure in the video — and it is a *process* failure, caught by the tool's own guard. |
| W-6 | Correspondence is placed FEATURE-ORDERED (grammar, §2) at a density matched to feature complexity — ~69 pairs for a human head — in a surface-anchored format (Point on Triangle), with symmetry used for paired organs. | Under-anchored features drift (ears/eyes); vertex-anchored points break across topology differences. | Count ladder 5→20→42/43→52→69 with the order read from the viewports; format + symmetry fields read from the panel (60:00–80:00). |
| W-7 | The solve runs at a multi-resolution schedule, not a single projection: subdivision levels with ICP alignment passes and an optimizing refine whose sampling tightens coarse→fine (Wrap values: Subdiv 3, ICP 5, Opt 20, Sampling 5 → 0.2 — tool-specific, UNTESTABLE-IN-ROUTE as numbers). | A single nearest-surface projection folds at concavities and bridges across lips/eyes (the naive-shrinkwrap failure). | Parameter panel read at 82:30; ONE compute sufficed (no re-wrap in 3:20:54). |
| W-8 | The raw wrap is NEVER edited directly. All hand cleanup lives in a separate correction layer (Blender shape key "Correction"); the raw result stays as Basis. | Cleanup becomes unauditable and unrepeatable; the next wrap destroys the fixes. | Basis + Correction keys at 95:00; every cleanup frame (95:00–105:00) is Edit Mode ON the Correction key. |
| W-9 | Texture transfer is a SEPARATE pass in UV space, after geometry settles: target texture → template UVs, with border extrapolation; the template's UVs must therefore exist and be sane before this pass (UVs are a TEXTURE-pass precondition, not a wrap precondition). | Baking textures before cleanup bakes the lies in; missing UVs make the pass impossible, silently if unexamined. | Second Wrap graph at 135:00: TransferTexture → ExtrapolateImage → SetTexture → SaveImage (PNG, Q80). |
| W-10 | The conformed result integrates into the host as a BLEND (shape key on the host body), not as a mesh swap. | Rig, weights, and the host's other morphs are lost; every downstream asset (eyes, lashes, hair) must be re-fit by hand. | Host key stack: "GBF Wrapped Feng" = 1.000 among the anatomical keys (108:00); eyes/lashes then fit to the blended result (115:00–125:00). |

## 2. CORRESPONDENCE GRAMMAR

Correspondence is authored, not sprayed. The placement
sequence is a fixed rhetorical order over the face: **anchor
the nose first** (5 pairs: tip + nostril wings — the face's
most rigid, least ambiguous structure), **then the mouth**
(lip ring + corners + chin, to ~20), **then the eyes with
mirror symmetry switched on** (rings around both sockets,
to ~43), **then the ears** (to ~52), **then a sparse fill**
(jaw line, neck, forehead, to ~69) that exists to keep the
solver honest in the regions between features, not to add
detail. Three rules make it teachable: (1) every pair is
placed on the TEMPLATE first and matched on the target in
the same order (the tool counts both sides; a 42/43 split
mid-placement is normal and closes); (2) symmetry is a
placement accelerator for paired organs, toggled for the
eyes/ears pass and off elsewhere — asymmetric features
(nose deviation, mouth) are placed unmirrored; (3) points
are surface-anchored (Point on Triangle), so the set is a
statement about ANATOMY ("this point of the ala") that
survives the two meshes having different topologies —
which is the entire premise of wrapping a quad template
onto a triangulated game mesh. Density follows FEATURE
COMPLEXITY, not surface area: the whole torso gets zero
pairs because the template body is already the destination
body; the face gets 69 because the face is what is being
re-targeted.

## 3. CLEANUP MAP — the lie zones

| Zone | What the wrap does there | Pre-emptable by preparation? | Evidence |
|---|---|---|---|
| Ears | Worst lie in the video: the wrapped ear is a tangled dark patch at 95:00 — the solver collapses the ear's folded concavities. | **INHERENT** (mitigable): ear points were placed (W-6) and ears still tangled; concavity folding is a solver property. Cleanup: hand work in Correction. | 75:00 ear points; 95:00 tangled ear. |
| Eye sockets | Socket verts mis-seated; the cavity pulls rim verts inward. Needed material-select + micro-move repair (µm-class moves). | **PARTLY PRE-EMPTABLE**: W-4 subsets kept eyeball parts out, yet the socket still lied → the residue is inherent; without subsets it would be worse (Pass 3 prices the difference). | 100:00–102:30 repair sequence. |
| Mouth interior | Collapsed dark cavity — the mouth bag has no true correspondence on a closed-lip template. | **INHERENT**: no preparation gives the interior a counterpart; it is rebuilt/inspected by hand. | 105:00 closeup; the pre-export mouth inspection at 20:00–24:00 shows the creator knew this zone was special before wrapping. |
| Neck blend seam | The wrapped head meets the unwrapped neck/shoulder: a visible step, repaired with proportional-edit smoothing (Smooth falloff, 0.0923 m radius) inside Correction. | **PRE-EMPTABLE in degree, INHERENT in kind**: subset boundary placement (W-4) chooses WHERE the seam sits; a seam exists wherever a partial wrap ends. Subset the whole head+neck and the seam moves to the shoulders; it never vanishes. | 95:00 neck work, header numbers read. |
| Scalp / hairline | No cleanup seen; the scalp was outside the retarget (hair covers it). | **PRE-EMPTED by scoping**: the subset + the hair asset make the zone a non-problem. The estate analog: scope the wrap to what the next asset covers. | Hair restored at 192:00 with no scalp work anywhere in 3:20:54. |
| Hands / fingers, body joints | **No lies, no cleanup** — because the template BODY was the destination body (zero correspondence pairs below the neck). | n/a — the absence is itself the lesson: a wrap only lies where it actually re-targets. Plan expectation (d) priced hands/joints as lie zones; on this evidence they are lie zones only when the body is the target. | 108:00 shape-key integration; no body cleanup frames exist. |
| Lips | Parted-lip shape transferred with the mouth ring of points; red-lip material reads correctly at 84:00 with no dedicated cleanup pass. | **PRE-EMPTED by grammar**: the lip ring is placed second (W-6) — early, dense anchoring is what keeps lips honest. | 65:00 lip ring; 84:00 result. |

Pre-emptable (in whole or part): eye sockets (part),
neck seam placement, scalp (by scoping), lips (by grammar).
Inherent: ears, mouth interior, the seam's existence.

## 4. Adopt / Adapt / Reject — against estate practice

- **W-1 interchange contract — ADOPT.** The estate already
  exports glTF/OBJ between stages; naming the five switches
  (apply modifiers, keep vertex order, normals, UVs, groups)
  as a checklist costs nothing and kills a class of silent
  rebinding. Mirrors the estate's existing deterministic-
  converter discipline.
- **W-2 pre-alignment — ADOPT.** Already implicit in the
  sprite-to-3D factory (canonical rig space); the video
  prices violating it (identity transforms in-tool).
- **W-3 named polygroups — ADAPT.** Estate bodies carry
  vertex groups + §6 anchors rather than DAZ material
  groups; the transferable rule is "subsets are defined
  from NAMED sets, never from ad-hoc selections."
- **W-4 exclusion subsets — ADOPT.** Directly applicable to
  headhack + factory work: eye/teeth/mouth-interior
  exclusions become named, reusable subset definitions.
- **W-5 point-set/geometry binding — ADOPT, and generalise.**
  Any stored correspondence (anchors, landmarks, UV pins)
  must carry the identity of the geometry it was authored
  against, and tooling must refuse or warn on mismatch —
  the estate's anchors are derived per-girl for exactly this
  reason (SIX-GIRL-STANDARD §6.2 rules, E-1 guard).
- **W-6 grammar — ADAPT.** The estate's §6 anchor set IS a
  correspondence grammar (7 anchors, rule-placed). The
  video's feature-ordered placement + density-by-complexity
  is the same idea at higher density; adopt the ORDER as
  the authoring order for any future denser anchor sets.
- **W-7 multi-resolution solve — ADAPT (mechanism only).**
  Wrap's numbers are UNTESTABLE-IN-ROUTE. The mechanism —
  coarse alignment (ICP-analog: rigid + global fit) then
  tightening local projection — maps onto the estate stack
  as: global fit first, Shrinkwrap Project with subdivision
  levels, then a bound Surface Deform refine. A single
  raw projection is REJECTED as a pipeline (it is the
  known folder).
- **W-8 correction layer — ADOPT verbatim.** Basis =
  machine result, Correction key = human fixes. The estate
  already keeps raw vs conformed separate for Prima
  (canon vs m-scaled); this names the discipline for all
  wrapped/conformed bodies.
- **W-9 texture pass separate — ADOPT.** Matches the
  factory's identity-lock-before-texture order.
- **W-10 blend-don't-swap integration — ADOPT.** The
  estate's Body_Bust_Size shape key is already this
  pattern; the video validates it at production scale.
- **REJECT:** recycling a Wrap project (and its point set)
  across targets without revalidation (the 127-point
  near-miss); Draco-quantized OBJ as an interchange for
  further editing (SaveGeom's Draco params are for
  delivery, the working round trip at 132:00 is plain
  Wavefront OBJ); single-shot trust — the video's own
  workflow spends ~2× the wrap's duration on preparation
  and cleanup, which is the honest price the plan's gate
  should expect.

## 5. Relation to Plan 22's NS22-RESPONSIVE-SLEEVE-FIT

Plan 22's preset (Shrinkwrap Project → Surface Deform →
Solidify) is a LIVE modifier stack: the sleeve re-conforms
every frame, which is why its gate failed on articulation
(interpenetration at the bent elbow). Plan 38's pipeline
is the opposite pole: a BAKE — correspondence-driven,
computed once, frozen into Basis, with human fixes in a
Correction key. They are not competitors: the bake is for
identity transfer between static meshes (this plan), the
live stack is for garments on a moving body (Plan 22).
The shared precondition core is W-2 (pre-alignment) and the
Plan 22 lesson that Surface Deform binding is a GUI-phase
operation with a triangulated target — both carried into
the Pass 3 build. Where Plan 38 adds genuinely new estate
knowledge: W-5 (correspondence/geometry binding), W-8
(correction-layer discipline), and the lie-zone pricing in
§3 (Plan 22 found its lie at the elbow by collision test;
Plan 38 maps the face's lies in advance).
