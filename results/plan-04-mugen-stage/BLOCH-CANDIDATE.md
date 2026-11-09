# Bloch candidate — Night School Plan 04 (MUGEN stage creation)

- origin_lane: ntranch
- content_label: nsfw
- Evidence: `~/workspace/night-school-20261105/runs/plan-04/`
  (OBSERVATION.md, TECHNIQUE.md, PASS3-REBUILD.md,
  PASS4-APPLICATION.md, stage/)

## Candidate lessons

1. **Layer grammar (five treatments).** A scene element earns
   its own layer only if it needs a treatment a composited
   plate cannot give it: different motion (delta/velocity),
   animation, draw side of the actor plane (layerno), blend
   (addalpha), or coverage by tiling. Everything else is baked
   into one plate. Declaration order = draw order. Verified by
   a two-renderer rebuild whose per-layer displacements agreed
   to 0.0 px (MUGEN delta model vs estate depth-plane model,
   z = f·(1/delta − 1)).

2. **Parallax calibration is rule-bound, not formula-bound.**
   Pin the floor's delta (1,1 at scene scale; it is the
   anti-slide anchor), rank other layers monotonically by
   depth, and treat delta as width-invariant: stage-width
   changes break *coverage and anchors*, never the factors.
   A studied build stated this doctrine and then shipped every
   delta at 1,1 because its depth was composited — when
   distilling a practitioner's method, record practice and
   doctrine separately; the gap between them is itself a
   finding (DG1 in OBSERVATION.md).

3. **Ambient budget.** One animated system, at the furthest
   layer, on a slow loop (studied instance: 8 frames × 10
   ticks + one 50-tick hold = 120 ticks, 0.18–0.35% of layer
   pixels changing per beat in the rebuild's measurement).
   Motion at the actors' depth reads as busy; motion at the
   back reads as alive. Engine motion (velocity+tile) is the
   budget valve before frame animation is spent.

4. **Capture route (this host, rule34video).** HEAD requests
   to the token `get_file` URL return 403 on both egresses;
   GET with the same page load's cookie jar (after a homepage
   warm-up hit) returns the 302 to the CDN and works. Tokens
   are egress-bound — each egress must fetch its own page.
   Sandbox egress failed to resolve the redirect at all;
   primo sustained 9.2 MB/s single-stream. (Extends the
   Plan 01/02 capture notes.)

5. **Whisper over music/game audio.** A 4,127 s streamed build
   with music + game audio and no narration produced only
   hallucination loops ("Thank you." / "Bye." / "Fight!") at
   30 s spacing through the processed span — the screen-first
   observation design (frames carry every claim) is what made
   the study completable. For stream VODs, budget a
   no-narration outcome and design observation to not depend
   on the transcript.
