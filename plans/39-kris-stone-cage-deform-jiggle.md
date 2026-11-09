
## Erratum — Pass 1 (2026-11-06, Pax pilot run)

The recipe above says "Mesh Deform bind". The source video does
not use Mesh Deform: the cage carries **Cloth** physics and
drives the body through a **Surface Deform** modifier, and the
cage itself follows the armature via Data-Transferred vertex
groups. Full evidence: `runs/plan-39/OBSERVATION.md` (this
repo's run record). The pilot executed the plan as written
(keyed cage + Mesh Deform) as the deterministic estate
adaptation; the video's cloth route and its bake-determinism
question are recorded in `runs/plan-39/TECHNIQUE.md`.
