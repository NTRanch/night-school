# Plan 03 — Testing Patterns (Virt-A-Mate clip, TdotONY)

- **Source:** https://rule34video.com/video/3300899/testing-patterns/
- **Video ID:** 3300899 · **Creator:** TdotONY · **Duration:** 1:23 · **Views at intake:** 5,317
- **Categories:** Virt-A-Mate, Tutorials · **Tags:** blowjob, deepthroat, no sound
- **Lane:** NSFW-primary / SFW translation: none direct — VaM performance-capture reference only
- **Estate targets:** Virt-A-Mate as a reference implementation for real-time performance, the animation pipeline's reference shelf
- **Status:** PLANNED — re-scoped at intake (see below)

## Intake correction

The title suggested a pattern-testing/QA tutorial. It is not one: this
is a 1:23 Virt-A-Mate performance clip with no description and no
instruction. The plan is re-scoped honestly rather than padded: the
study is a short-form VaM scene analysis — what a competent VaM scene
does with performance looping, camera, and contact in 83 seconds —
filed as reference for the estate's ongoing VaM-as-reference work, the
same posture as the Laplace reference material (video serves as
reference only; nothing is extracted into shipped work).

## SHOULD-BE-SEEN (written before viewing)

A tight looped VaM scene: performance captured or keyed in VaM's
timeline, physics-driven contact and soft-body behaviour doing the
work that keyframes do elsewhere, one camera, no edit points.

## Timed observation focus

- Loop structure: where the cycle seams, what repeats exactly and
  what varies (physics settle is never identical twice — note how
  the clip handles that).
- Contact and physics: which behaviours are VaM's solvers (hair,
  soft-body, collision) vs authored motion.
- Camera: static or moved; what the framing chooses to prove.
- Performance: the acting beats readable at this length — head,
  hands, timing accents.

## Distillation targets

1. **VaM solver inventory** — which visible behaviours belong to
   which VaM system. Question: which of them does the estate's own
   stack have no equivalent for yet? (Feeds the gap map, not a build.)
2. **Short-loop grammar** — how an 83-second loop stays watchable.
   Question: is it variation, accent timing, or camera?

## Clean-room rebuild spec

None — reference-only item. The deliverable is the analysis record,
not a rebuild. If the solver inventory names a gap worth closing, it
leaves this plan as a separate commission candidate.

## Application

- **NSFW application:** reference shelf for Torogao scene direction.
- **SFW translation:** none claimed.

## Gate

PASS = the analysis record separates solver behaviour from authored
motion with timestamps, and any named gap is stated as a question,
not a conclusion.

## Deliverables

- `results/plan-03-testing-patterns/` — scene analysis record only.

## Errata from the executed run (2026-11-06, runs/plan-03/)

The capture contradicts this plan's intake correction in one
respect. The file is not a rendered performance clip: it is a
**screen recording of VaM 1.22.0.1 in Edit Mode** (UI bar,
cursor, and in-scene controls visible throughout) in which
the creator tests **one vamX animation pattern** live —
depth / bias / speed sliders plus a play/stop toggle — over
82.716667 s (file duration; the page's PT0H1M23S stands).
The intake's rejected first reading ("a pattern-testing/QA
item") was closer than the correction that replaced it,
though the clip contains no instruction: no description
(JSON-LD description is empty), no narration, and no audio
stream at all (page tag "no sound" confirmed by ffprobe).
The re-scope's deliverable (solver-vs-authored analysis +
gap questions) was executed as written and stands; only the
characterisation above is corrected. The solvers the
SHOULD-BE-SEEN expected to star (hair, soft-body) are never
exercised; the working solvers are control-follow and IK.
Full record: `results/plan-03-testing-patterns/`.
