# Plan 02 — Pass 2 Technique Sheet (Distillation)

Source: `OBSERVATION.md` (Pass 1). Every Pass 1 claim is
distilled below or judged not-a-technique with a reason.
UNREADABLEs from OBSERVATION §8 are carried with their
dependencies marked. Estate context: Blender 5.2.3 (source
video: Blender 4.0 — version drift recorded at C-02-8),
Prima's conformed rig (54-bone Mixamo armature, flat
Principled materials), scripted/headless discipline.

## Target 1 — The lighting rig as a named reproducible setup

**The rig is a ROLE SYSTEM, not a preset.** The artist builds
it per shot, aloud, in role order, against a live camera
render, starting from a black silhouette. Named estate form —
**NS02 "Neon Backdrop" rig**:

| Role | Type (as built) | Values (Pass 1 evidence) | Mechanism |
|---|---|---|---|
| Environment | Curved photo backdrop mesh, emissive | Image Color → Emission Color; Alpha → Emission Strength + Alpha; World strength 0.000; NO HDRI | The backdrop is the light field AND the background; the subject starts unlit (silhouette) and is carved out of it with lamps |
| Key | Area, Rectangle | 0.6 m × 1 m, ≈1000 W (1005.4 W read mid-tune), pale blue-white, Cast Shadow ✓ | A tall softbox portrait key; rectangle matched to a standing figure |
| Rim | Spot (object misnamed "Area.002") | 55°, Blend 0.150, ≈1000 W (1007.9 W), magenta HSV 0.817/0.932/1.000 | Rim colour SAMPLED FROM the backdrop's dominant neon (pink) so subject and ground share one palette |
| Fill | Area, oversized | "scale it up super large so it doesn't affect it that much" — size/power UNREADABLE (carried) | A very large area source: intensity per unit area drops, giving shadow-lift without a second shadow direction |
| Accents | Points ×4 | White, 5 W (10 W seen mid-tune), Radius 0 m, Cast Shadow ✓ | Small hard accents (face/prop glints); cheap in Cycles |

**Portability question (plan target 1) — ANSWERED: portable
as roles, tuned as values.** Evidence: (a) the artist states
the pipeline is his standing workflow (C-02-10); (b) every
value that matters is DERIVED on the spot — rim hue from the
backdrop, key size from the figure, fill size from "doesn't
affect it that much"; (c) nothing in the rig references the
character (no character-specific lamps, no HDRI to match).
What does NOT port: the backdrop image itself (a specific
free wallpaper) and the exact wattages (tuned by eye against
that backdrop's brightness). The estate template therefore
parameterises roles + derivation rules, with the video's
numbers as defaults — not as constants of nature.

- **Adopt:** silhouette-first build order (backdrop emissive
  + world 0, THEN lamps one at a time in the camera view);
  rim-colour-from-backdrop rule; oversized-weak fill rule.
- **Adapt:** the estate has no licensed neon-street photo;
  the template generates a **procedural neon-gradient backdrop**
  (emission gradient + window-light speckle) on the same curved
  mesh, so the derivation rules still operate (rim hue is
  sampled from the backdrop's dominant colour parameter).
  Wattages become named parameters with the video's values as
  defaults. Object names are made truthful (the source's
  names lie about types — a Spot named "Area.002").
- **Reject:** per-shot mouse-built rigs as the deliverable
  form (the estate's form is the scripted template, Pass 3);
  the 700 mW disk accent (tried mid-session, absent from the
  final rig — session noise, not technique).

## Target 2 — Posing discipline

The artist's pre-render checks, distilled as an ordered
discipline (all [BOTH] unless noted):

1. **Camera before pose.** Format + lens are standing
   defaults (1080×1920, 35 mm); the reference's ANGLE is
   matched first; the pose is built inside that frame.
2. **Never move the model.** Camera moves; rig stays at its
   origin. Demonstrated failure: moving the model broke the
   rig on screen (C-02-2). Estate form: pose bones only;
   the armature OBJECT transform stays identity — checkable
   in the template gate.
3. **Gross → fine order.** Hip/spine/arms → head/gaze →
   expression morphs → fingers LAST, bone by bone.
4. **Contact is the finger check.** Fingers are done when
   they visibly close on the prop; "barely grabbing it" is
   the named failure. The pinky is called out as the awkward
   case (shortest lever).
5. **Fit failure is solved by removal.** Ill-fitting clothing
   is hidden, accessories kept — the shot is not held hostage
   to a garment (C-02-4 context; outfit segment).
6. **Expression is a blend, not a preset:** one dominant
   morph (Angry HD 0.460) + one modifier (half smile), rest 0.
7. **Clay check before the beauty render:** a grey-material
   full-frame render is reviewed for pose+light read before
   the final render (§6 of OBSERVATION).
8. **Simplify discipline:** ON for all interactive work, OFF
   as the explicit pre-render gate (his only on-screen
   caption — the video's single imperative).

- **Adopt:** 1, 2, 3, 4, 7, 8 as written (they are
  rig-agnostic and estate-shaped).
- **Adapt:** 5 → estate form is outfit-variant selection at
  build time (Prima's rig carries clothed/dress variants as
  separate objects; hide-by-variant is the same move, made
  before posing instead of after a failed fit). 6 → Prima's
  face is shape keys, not DAZ morphs; the blend rule ports
  (one dominant key + one modifier), the values don't.
- **Reject:** nothing in the posing discipline itself.
  Judged not-a-technique: the specific Poison pose (a
  deliverable of the video, not a method) and the DAZ/MHX
  panel workflow (estate rigs are Mixamo-bone; the bone-
  collection layer enabling ports as TARGET 2 item 3's
  "enable the layer you are about to pose").

## Target 3 — Render economics

The numbers (OBSERVATION §7) split cleanly:

- **Carries the quality:**
  - Cycles + GPU (the whole look — emissive backdrop, SSS,
    soft area shadows — is path-traced; Eevee is never
    mentioned or shown).
  - **Adaptive sampling: Noise Threshold 0.0100 with Max
    Samples 4096.** The threshold is the working setting;
    4096 is a ceiling the adaptive sampler rarely reaches
    on a still like this. This pair IS the economics: pay
    for samples only where noise demands them.
  - The pre-render Simplify-OFF gate (a wrong render at
    4096 samples costs the full render time; the caption
    exists because he has paid it).
  - Lightroom Lens Blur as the DoF substitute: the render
    is shot effectively deep-focus (no camera DoF settings
    are ever shown) and the bokeh is SYNTHESISED in post
    from an AI depth map (Blur 50 / Boost 50, focus-brushed).
    DoF-by-post is cheaper and re-doable; render-time DoF
    at 4096 samples is neither.
- **Ceremony / inert:**
  - Min Samples 0 and Time Limit 0 (defaults, untouched).
  - Max Bounces 1024 on every lamp (a per-light field he
    never discusses; almost certainly inherited default).
  - Viewport Max Samples 1024 (never reached interactively;
    the viewport Noise Threshold 0.1000 is what he actually
    previews against).
  - Photoshop in the chain (signature only — a branding
    step, not image quality).
- **Not determinable:** Denoise state (UNREADABLE 3) and
  Colour Management (UNREADABLE 4) — carried: the template
  must CHOOSE (denoise ON, OpenImageDenoise, the estate's
  standard posture for stills; view transform = the Blender
  default of the RUNNING version) and must record that these
  are estate choices, not video evidence. Source-Blender-
  version drift (4.0 → 5.2.3: AgX is default in both, but
  lamp power/area behaviour and Principled SSS semantics
  shifted across versions) is recorded at the claim, not
  silently absorbed.

- **Adopt:** the adaptive pair (0.0100 / 4096) as the
  template's render preset; Simplify-OFF as a scripted
  assertion; DoF-in-post as the sanctioned route (estate
  form: Blender compositor defocus on the depth pass, or
  plain deep-focus delivery — the template ships deep-focus
  and NAMES the post step as external, it does not fake
  Lightroom).
- **Adapt:** GPU Compute → the estate runs headless CPU or
  GPU as available; the preset records device as a parameter
  (determinism note: CPU rendering is the reproducible
  route for the decoded-pixel hash, Pass 3).
- **Reject:** 4096 as a fixed sample count divorced from the
  threshold (misreads the mechanism); per-light Max Bounces
  tuning (no evidence it does anything he relies on).

## Claim-by-claim disposition

| Claim | Disposition | Note |
|---|---|---|
| C-02-1 camera-first defaults | Adopt | Template parameter block |
| C-02-2 never move the model | Adopt | Becomes a gate assertion |
| C-02-3 simplify on/off discipline | Adopt | Scripted assertion in template |
| C-02-4 manual posing order + finger contact | Adopt (method) / Adapt (rig) | Mixamo bones, same order |
| C-02-5 emissive backdrop, world 0, no HDRI | Adopt | Procedural backdrop substitution (Adapt) for the photo itself |
| C-02-6 role rig with his values | Adopt as defaults | Values are parameters, not constants |
| C-02-7 skin dials | Adapt | Prima's flat Principled Skin gets SSS weight + roughness mapped from the dials' intent (see Pass 3 mapping) |
| C-02-8 Cycles 0.0100/4096 | Adopt | Version drift 4.0→5.2.3 recorded |
| C-02-9 LR blur + PS signature post | Adapt | Named external post; template delivers deep-focus render + depth pass so the step is possible |
| C-02-10 portability | Adopt as the design premise | Tested directly in Pass 4 (different character, same template) |

Not-a-technique (with reason): the reference site's
usefulness (a sourcing habit, no mechanism); the model's
genital/outfit panel parameters (content settings of one
commercial model, no transferable mechanism); the
"Not Responding" save hangs (tool friction — the transferable
part, incremental versioned saves, is noted in Target 2's
context and adopted as template versioning practice).
