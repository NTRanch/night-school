# Bloch candidate — Night School Plan 40 (lighting & colour grading)

origin_lane: ntranch
content_label: nsfw
evidence: runs/plan-40/ (this dir) — MANIFEST.md, OBSERVATION.md,
PASS3-REBUILD.md, rebuild/ scripts + measure JSONs; primo canonical
`~/.local/share/pax/night-school/plan-40/` (detach logs ns40-*).

## D-1064 question, answered plainly

Yes — four things cost time or forced workarounds the next agent
will also hit: (1) rule34video rendition URLs need a **Referer
header** in addition to the per-egress cookie jar; (2) Blender
5.2's new compositor is **socket-driven** — three of six grade
stages silently no-opped on property-style API calls and only the
fingerprint readback caught it; (3) the compositor File-Output EXR
**overwrites on every render**, which invalidated a determinism
re-read (the twin file copied aside beforehand is what saved the
claim); (4) primo's wave contention starved a 480 s slice's
transcription for ~50 min, forcing the deliver-in-flight posture.

## Friction log (including silent workarounds in successful runs)

1. **Referer-bound egress.** `get_file` rendition URLs 403 on both
   egresses without `-e <watch-page URL>`, even with a valid
   per-egress jar. Plan 20's manifest recorded the jar half; the
   Referer half is new. Cost: ~4 probe rounds. Workaround (now the
   documented route): jar + Referer + parallel ranged segments on
   primo. Candidate lesson: *session-bound media URLs may bind to
   jar, egress AND Referer — probe all three before concluding a
   rendition is gone.*
2. **Origin noise family.** First fetches returned sandbox 403
   (15 B "Access denied.") and primo 503 (93 B DB-fatal) — the
   Plan 29 flakiness family with a different first byte-pattern.
   Retry-with-jar converged on both egresses (200, 224,624 B).
   Not a SOURCE-NOT-FOUND; the discipline's control test is what
   kept this from being misread either way.
3. **CDN segment cuts.** 16 ranged segments of 181,134,149 B:
   repeated near-complete cuts at ~177–180 MB; seg14 needed 3
   tries. Size-verify + bounded retry absorbed it; concat verified
   by byte count, full decode (0 error bytes) and packet span.
4. **Blender 5.2 compositor is socket-driven (the expensive one).**
   `CompositorNodeColorBalance.correction_method/.lift/.gain`,
   `EllipseMask.mask_type`, `Filter.filter_type`, `Glare.glare_type`
   do not exist; stages failed into try/except notes and the chain
   rendered "successfully" without them. Only the builder's
   fingerprint READBACK (stages + notes printed into JSON) exposed
   the partial chain. Fixes probed live on primo: ColorBalance
   (factor, colour) socket pairs; Glare Type/Threshold/Strength
   sockets; Filter Type enum is 'Box Sharpen' (no plain 'Sharpen');
   EllipseMask Position is a 2-vector. Candidate lesson: *on the
   new compositor, treat every node property as guilty until a
   probe prints its socket list; a grade/render claim requires a
   stage readback, not a clean exit code.*
5. **Vignette semantics differ from the old node.** First working
   vignette (ellipse 0.62, blur 120, gain floor 0.42) produced a
   visible halo ring at beauty scale — caught by LOOKING at the
   render, not by any number. Gentler estate values (0.85 / 240 /
   0.72) are the recorded translation. Candidate lesson: *mask-size
   sockets in the new compositor are not the old node's fractions
   in effect; verify vignettes visually at final scale.*
6. **EXR File-Output overwrites silently.** Every render with
   compositing on rewrites `passes-variant.exr`; beauty renders
   replaced the probe EXR (42,276,636 B → 168,771,590 B), and a
   later measure config read the new file and reported determinism
   False against the probe twin. The claim survived ONLY because
   the twin had been copied aside (`passes-twin1.exr`) before the
   beauties ran. Candidate lesson: *copy measurement EXRs aside
   immediately; never let a measure config point at a live
   File-Output path after further renders.*
7. **Wave contention.** Primo load 10–27, swap 23/23 GiB, ~8
   sibling whisper jobs + sibling Blender renders throughout.
   Consequences absorbed: slice ladder instead of full-first
   transcription; beauty renders at a matched 384-sample pair cap
   instead of each creator's own pair; render wall-times 11–25 min
   vs ~90 s probes. Slice A (1,200 s) was still transcribing ~50
   min after launch at delivery; finish.sh staged (Plan 17
   pattern).
8. **Naive argv pairing bug (own code).** `p3_render.py`'s
   `dict(zip(argv[::2], argv[1::2]))` breaks when a lone flag
   (`--raw`) precedes paired args — the first raw beauty died on a
   KeyError (rc=1) and was relaunched with `--raw` last. Cheap,
   but exactly the class of bug a probe render would not have
   caught (the flag path was beauty-only).
9. **rsync chown noise.** First frame pull warned on ownership;
   `--no-owner --no-group` is the standing fix (already estate
   practice; re-earned here).
10. **Background-exec handoffs ignored per D-567** — all primo
    state in this run was read from `.done`/`.log` files and output
    artifacts; several stale completion notices arrived and were
    disregarded by design.

## Per-edit attribution rows (variant build v1 → v3)

| Component | Change | Observed difference | Verdict |
|---|---|---|---|
| Grade chain (v1) | Property-style API for ColorBalance / EllipseMask / Filter / Glare | Readback notes: 3 stages missing; render still "succeeded"; graded beauty existed but was curves+streaks only | confounded (v1 numbers measured a partial chain; kept, labelled) |
| TealOrange (v2) | Socket-pair colour sets (factor, colour) | Stage present, zero notes; shadows take the teal axis in v3 beauty | works |
| Glow (v2) | Type/Threshold/Strength via sockets | 'Bloom' in readback (was default 'Streaks') | works |
| Vignette (v2) | Mask→Blur→Invert→ColorBalance Factor route | Halo ring at beauty scale (ellipse 0.62 / floor 0.42 too strong) | failed visually, fixed in v3 |
| Vignette (v3) | Ellipse 0.85, blur 240, gain floor 0.72 | Halo gone; gentle corner falloff in probe + beauty | works |
| Sharpen (v3) | Type socket 'Box Sharpen', Factor 0.5 | Stage present; no fringing at beauty scale (v2 full-strength fringed) | works |
| Beauty pair cap | 512 → 384 samples both sides | Matched pair held; wall-time per beauty ~11–25 min under contention vs unbounded | works (documented deviation in PASS3) |

## Artefact pointers

- Variant of record: primo
  `~/.local/share/pax/night-school/plan-40/rebuild/variant/ns40-variant.blend`,
  fingerprint d95fa6e57d455670feaa29e59c049b456f6c5b4c7d301fc3053d92d42181a4c2
  (`fingerprint-variant.json` same dir); builder
  `runs/plan-40/rebuild/p3_build_variant.py` (this run dir).
- Measurements: `measure-probe-out.json` (shares + determinism),
  `measure-v3-out.json` (final plate stats) in the primo rebuild
  dir, mirrored in this run's `rebuild/`.
- Judged triptych: `rebuild/side-by-side.png` (this run dir).
