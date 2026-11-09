# Plan 40 — Pass 2 Technique (Anime Nyan, "Basics — Lighting and Color Grading")

Evidence base: OBSERVATION.md (screen reads, frame-cited) + PASS3-REBUILD.md
(measurements). Speech tier UNCONFIRMED; no technique below rests on
narration. Creator's own provenance, stated in his description and
visible on his screen: lighting practice is his own; the grade is
assembled from Polyfjord's EXR workflow, Sobotka's filmic-resolve, and
Waqas Qazi's teal-and-orange method — credited, not concealed.

## 1. The method in one pass

1. Append a pre-built set as its own collection; pose the character.
2. **Zero the world** (HDRI loaded, strength 0.000), **hide the set**,
   and light the character alone from a pure silhouette, one lamp at a
   time, against the live rendered pane.
3. Build a **distributed micro-rig**: ~10 small close lamps (Areas incl.
   a strip, narrow Spots, Points; largest read 25.7 W), coloured at the
   lamp where wanted (a pink key-class Area), placed by eye, deleted and
   replaced freely. A plane rides in the light path as a flag.
4. Reunite the set; fix interior light by making blocking set geometry
   **ray-transparent (Light Path → Transparent BSDF)** rather than by
   moving lamps; finish the camera with real DoF (f/2.4 @ 121 cm).
5. Render **dark and cheap**: Cycles 0.0100/**128**, OptiX denoise,
   single-layer OpenEXR (RGBA, Float Full, DWAA), character-only and
   combined plates.
6. **Grade in DaVinci Resolve** (YRGB, Rec.709 (Scene) timeline): a
   saved Filmic/Qazi PowerGrade for look development; a compact
   delivery chain (base encode → denoise → contrast → colour → base →
   vignette/sharpen); deliver PNG + .drx, versioned.

## 2. House look decomposition — taste or missing settings?

The delivered look (OBSERVATION §2, g0001): low-key warm/cool split —
warm practical glow behind, cool blue-purple subject light, teal
shadow side, deep blacks, soft background. Decomposition against the
evidence:

**What the Blender settings explain (the render half).** The subject's
cool sculptural read, the warm/cool separation, and the deep-black
floor are all in the plate: a zeroed world, a distributed cool-white +
pink micro-rig on the subject, and the set's own warm practicals. The
rebuild reproduces this half from settings alone (PASS3: variant plate
structure is measurably his — no dominant key, backdrop absolute energy
unchanged at 0.03378 mean lum, subject lit entirely by the small rig).

**What the Blender settings do NOT explain (the missing half).** The
plate that leaves Blender is *drastically* dark — his own EXR sits
near-black in Resolve's viewer (OBSERVATION §5.1), and the rebuild's
variant plate measures **4.8× darker** than the template's
(mean lum 0.1272 vs 0.6101, probe EXR Combined, PASS3). The delivered
brightness, the filmic rolloff, the teal/orange split-toning, the glow
and the grain **are not in the Blender file at all** — they are a
Resolve node structure he carries as a saved PowerGrade + .drx files.
Anyone reproducing "his look" from the .blend alone is missing half
the pipeline, and it is the half that does the exposure.

**The taste residue.** On top of the saved structure: per-image
primaries nudges of ±0.07 class (two wheel reads, OBSERVATION §5.3),
which saved gallery still he auditions first (§5.5), and every lamp
placement (no transform is ever typed). These are real but small —
they season a look whose body is structural.

**Verdict: MISSING SETTINGS first, taste second.** The house look is
a *two-application system*: distributed micro-light plate (settings,
reproducible) + saved Resolve grade (settings, but stored in another
tool and never enumerated node-by-node on screen — U5/U7) + a thin
taste layer. The rebuild's grade translation is the test of how much
of the second half is structure vs taste: see PASS3 §beauty
(raw-vs-graded deltas) for the measured recovery.

## 3. Grading contract — the minimal chain that survives across scenes

His contract is a **stored structure, not stored values**. What
survives across scenes (evidenced by the PowerGrade's reuse, the
gallery stills library, and .drx versioning) is the *order of
operations*:

**Encode → Filmic blend → tonal trims (highlights, printer lights,
primaries) → teal/orange split → look + look-adjust → finish (glow,
grain)** — with the delivery form compressing the same ideas to
**encode → denoise → contrast → colour → base contrast →
vignette/sharpen**.

Translated to estate terms (the form Pass 3 built and measured): work
on the scene-referred plate; (1) a filmic S-curve with a lifted toe
does the exposure the render refused to do; (2) a split-tone pass
(lift toward teal, gain toward warm) sets the warm/cool axis;
(3) a gentle contrast S re-seats blacks after the lift; (4) threshold
bloom for practical glow; (5) vignette + sharpen as the terminal
pair; denoise is a *chain stage*, budgeted from the start (his render
pair assumes it). Per-scene survival rule: **the structure is fixed;
only wheel-class nudges (±0.1) move.** A grade that needs new nodes
per scene is, in his practice, a new saved still — the library grows,
the contract doesn't change.

## 4. Triangulation rows vs Plans 02 / 11 / 13 / 17

Format per the established table discipline; every row evidenced in
OBSERVATION.md (§) or PASS3-REBUILD.md.

| # | Topic | 02 | 11/13 | 17 | 40 (this voice) | Row |
|---|---|---|---|---|---|---|
| T-40-1 | Where the look is finished | Blender render (exposure −1.8 estate fill) | Blender compositor (pass algebra) | Blender render + global comp grade | **DaVinci Resolve, external** | **DIFFERENT-PHILOSOPHY** (§5) — a third position vs 17's bake-in-render and 11/13's fix-in-comp: *fix-in-Resolve*; the renderer is a capture device |
| T-40-2 | World / background light | World 0.000, no HDRI; emissive backdrop | (inherits 02) | Emissive dome + authored gradient world | HDRI **loaded but 0.000**; real set + practicals | **AGREE in effect with 02** (zero world contribution), **CONFLICT in mechanism** with 17 (no dome/gradient) (§3.1) |
| T-40-3 | Key light scale | 1000 W rect area | (inherits) | 50 W areas (fills) | **8.8–25.7 W total class; largest lamp 25.7 W** | **CONFLICT** with 02's kilowatt doctrine; extends 17's low-power direction by another ~2–40× (§3.3) |
| T-40-4 | Light structure | One dominant key (measured 75.6%) + fill + accents | per-group proof of 02's split | two-point + accents | **Distributed: no source >27.1%** (PASS3 shares: Fill 27.1 / Points 17.0 / Strip 13.7 / Key 12.3 / SpotKey 3.3 / SpotRim 0.07) | **CONFLICT** — a flat micro-source field, not a hierarchy (§3, PASS3) |
| T-40-5 | Rim/back light | Spot 55°/0.150, backdrop-sampled magenta, **measures 0 (dead, behind wall)** | dead-rim finding | Point rims 1000→250 W | White narrow spots (14.2°/0.732) placed behind subject in open space; **measures 0.000663 share — live but faint** | **CONFLICT** with 02 on geometry and colour; **AGREE** with 11's implicit lesson (occlusion is the risk) by designing it out (§3.4, PASS3) |
| T-40-6 | Rim colour source | sampled from backdrop (HSV) | — | neutral | **white at the lamp**; colour from a pink Area accent + the grade | **CONFLICT** with 02 (§3.3, TQ-5) |
| T-40-7 | Render pair | 0.0100 / 4096 | (inherits; comp-side) | 0.0300 / 512 production | **0.0100 / 128** + OptiX + Resolve NR | **AGREE** with 02 on threshold (0.0100 is now a two-voice constant); **CONFLICT** on ceiling (32× lower) — ceiling is per-creator ceremony, threshold is the shared constant (§4) |
| T-40-8 | EXR codec | n/a (PNG stills) | **ZIP** (estate, DWAA rejected for dark gradients) | DWAA | **DWAA (lossy), Float Full, single-layer** | **AGREE** with 17; estate ZIP ruling stands against both (11) — note his plates are exactly the dark-gradient case 11 warned about (§4) |
| T-40-9 | Denoise strategy | OIDN in render (estate choice) | comp-side Denoise node | render denoise | **Two-stage: OptiX in render + NR in Resolve** (spatial 5.0/5.0, temporal 11.6/11.6) | **SINGLE** — no other voice budgets denoise across two applications (§4, §5.3) |
| T-40-10 | Depth of field | deep focus (post DoF rejected in 02's study) | — | — | **Real render DoF f/2.4 @ 121 cm** | **CONFLICT** with 02 (§3.5) |
| T-40-11 | Character/set separation | backdrop cyclorama, one scene | — | one scene | **Character lit alone (set collection hidden), separate character-only EXR** | **SINGLE** — separability as a first-class workflow step (§3.1, §4) |
| T-40-12 | Set-light conflict fix | n/a | — | — | **Light Path → Transparent BSDF** on blocking set material | **SINGLE** — a ray-visibility fix no other voice teaches (§3.5) |
| T-40-13 | Grade values discipline | fixed template numbers | pass algebra, exact | per-scene retune of a fixed chain | **Fixed node structure, wheel nudges ±0.07–0.1, saved as PowerGrade/.drx/stills** | **AGREE** with 17's philosophy (fixed chain, per-scene trim), different host (§5) |
| T-40-14 | Aspect / format | 1080×1920 portrait | (inherits) | 720×1280 delivery | **3840×2160 @75% landscape** | **SINGLE** for this corpus pair (his subject is a wide thumbnail composition) (§4) |

Tallies: AGREE 2 (T-40-2 partial-effect, T-40-13) · CONFLICT 6
(T-40-2 mechanism counted once — conflict rows: T-40-3, 4, 5, 6, 7
ceiling, 10) · SINGLE 4 (T-40-9, 11, 12, 14) ·
DIFFERENT-PHILOSOPHY 1 (T-40-1). (T-40-2 and T-40-7 are split rows —
agreement on the constant/effect, conflict on the mechanism/ceiling;
counted in both columns' notes, once each in the tally as
AGREE-with-conflict-mechanism.)

## 5. Adopt / Adapt / Reject (estate reading; decisions land in P4)

- **Adopt** — character/set separability as a build step (light the
  subject against nothing, reunite after): it is also the structural
  vaccine against the Plan 11 dead-rim class (T-40-5/11).
- **Adopt** — Light Path → Transparent BSDF for set geometry that
  eats light (T-40-12): a named, reusable fix.
- **Adapt** — the render pair economics: 0.0100 threshold is
  corroborated; the 128 ceiling only works because a second denoise
  stage is budgeted downstream. Estate adaptation: keep the estate
  pair for keeper stills; the *principle* (threshold constant,
  ceiling negotiable against a named downstream denoise) is the
  transferable part (T-40-7/9).
- **Adapt** — the grading contract (§3) as a compositor chain: Pass 3
  built it in Blender nodes (FilmicBlend → TealOrange → Contrast →
  Glow → Vignette → Sharpen). The Resolve host is not estate
  tooling; the *structure* is host-portable.
- **Reject** — DWAA for estate EXR interchange (standing Plan 11
  ruling; his use does not reopen it) (T-40-8).
- **Reject** — kilowatt key doctrine is *not* thereby refuted: 02's
  key works on its own stage (75.6% share, delivered stills). What
  40 refutes is its *necessity*: a delivered look exists at 1/40th
  the lamp power when the grade carries exposure (T-40-3/4).
