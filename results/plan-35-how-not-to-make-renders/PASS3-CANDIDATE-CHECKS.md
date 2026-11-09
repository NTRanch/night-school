# Plan 35 — Pass 3: Candidate Gate Checks + Exercise Record

Per the plan's rebuild spec there is **no scene rebuild**: Pass 3
derives candidate gate checks and exercises them against real
estate artifacts. Provenance (TECHNIQUE.md §1): the video yielded
**zero** defect classes, so every check below is sourced to the
plan's pre-viewing SHOULD-BE-SEEN categories instantiated by
estate-evidenced defect classes — **source: Plan 35 (plan
categories) + estate taxonomy entry** (TECHNIQUE.md §3). No check
is sourced to the video's content, because there is no such
content to source.

## 1. The candidate checklist (v0, for gated adoption)

| ID | Defect (taxonomy entry) | Detection method | Scope condition |
|---|---|---|---|
| NS35-C01 | Flat/unlit figure read (L-2) | Visual at viewing size: no directional shading on figure | All render classes |
| NS35-C02 | Skin-block wash — unshaded salmon/tan blocks or gradient wash on skin (L-1) | Visual at viewing size + native crop of limbs | Shaded-register artifacts |
| NS35-C03 | Garment/appearance spec violation — specified colour, construction, or hair colour wrong (M-1, F-1 hair) | Visual against the artifact's written spec | Spec-bearing artifacts |
| NS35-C04 | Print error — print/glyph present where spec says none, or specified print migrated off its garment (M-2) | Visual against spec. **Spec-relative:** specified body text/tattoos are not fires | Spec-bearing artifacts |
| NS35-C05 | Invented motif/accessory — floating hearts, invented crown/headpiece, unlisted props (M-3) | Visual census of the whole frame | All |
| NS35-C06 | Background leak — tiled/giant faces, floating heads, hair-mass blobs, anchor elements in ground (C-1) | Visual; checked FIRST (TG gate order) | Plain-ground-spec artifacts |
| NS35-C07 | Framing crop — head/feet cropped, figure incomplete (C-2) | Visual/measurable | **Only where full-body-in-frame is specified** (see prune evidence §3) |
| NS35-C08 | Non-neutral stance where neutral is specified (A-2) | Visual against benchmark stance line | Neutral-stance-spec artifacts only |
| NS35-C09 | Hand defect — merged, hidden, claw-like, or not five-fingered (A-1) | Visual + native hand crop at ≥2× | Hands-visible-spec artifacts |
| NS35-C10 | Face/identity defect — void eyes, missing pupils, wrong eye colour (F-1) | Visual + face-gate measurement where applicable | All |
| NS35-C11 | Proportion/register break vs cast spec (A-3) | Visual; segment ratios as support | Cast-spec artifacts |

## 2. Exercise pools

- **Keepers (known-good), 10:** D-802 kink stylesheet stills —
  `~/workspace/strobe-kink-stylesheet-20261103/stills/still-{vivienne,kaisa,valentina,maren,katya,cordelia,sadie,yuna,zuzana,manon}.png`
  (Owner-adopted keepers, D-802; REPORT.md in that directory).
- **Rulable-with-defects (middle), 3:** TG4-P1, TG4-Y2, TG4-A1 —
  `~/workspace/full-rigs-20261103/keeper-art-reanchor/round-tg4/candidates/`
  (verdicts per round-tg4/REPORT-TG4.md; fires here are EXPECTED
  where the round census named the same defect — concordance,
  not prune evidence).
- **Known-bad, 7:** TG4-Y1 (FAIL), TG3-Y1 (FAIL), TG2-Y1, TG2-Y2,
  TG2-A2, TG2-A3, TG2-A4 (all FAIL in their rounds) — candidates/
  dirs of round-tg4, round-tg3, round-tg2.
- Reads are this agent's reads of contact sheets built from the
  final artifacts (`gate-exercise/sheet-*.jpg` in this run dir),
  cross-checked against the rounds' own censuses. The Owner's
  eye remains the verdict of record.

## 3. Exercise record (fire = defect present; — = no fire; N/A = scope condition excludes the artifact)

### Keepers — D-802 stills (any fire here is prune evidence)

| Artifact | Fires | One-line evidence |
|---|---|---|
| still-vivienne.png | — | Shaded, specified collar/leash kit, plain room ground |
| still-kaisa.png | C07-UNSCOPED only | Figure cropped at hips — a deliberate keeper composition; scoped C07 (full-body spec) = N/A |
| still-valentina.png | — | Back-view keeper; specified handprint mark is scene content, not a motif defect |
| still-maren.png | C07-UNSCOPED only | Bust crop by design; scoped C07 = N/A |
| still-katya.png | — (C04 spec-relative) | "FREE USE" body text is her SPECIFIED marking — spec-blind C04 would false-fire here |
| still-cordelia.png | — (C04 spec-relative) | Womb tattoo is specified (corruption tattoo, D-799) |
| still-sadie.png | — | Full maid outfit as specified; complete figure |
| still-yuna.png | — | Shibari as specified; complete figure |
| still-zuzana.png | — | Chastity kit as specified; complete figure |
| still-manon.png | C07-UNSCOPED only | Waist-up crop by design (and this keeper was later re-rolled under D-828 on garment grounds — a spec change, not a checklist fire); scoped C07 = N/A |

**Keeper result: scoped checklist fires 0 / 10 keepers.**
Unscoped C07 fires 3 / 10 → **PRUNE-CANDIDATE (unscoped form)**;
the scoped form above is the fix, recorded here per the plan's
pruning rule. Spec-blind C04 would fire 2 / 10 (katya, cordelia)
→ C04's spec-relative clause is load-bearing, likewise recorded.

### Rulable-with-defects — TG4 (concordance check)

| Artifact | Fires | Evidence (concords with REPORT-TG4.md census) |
|---|---|---|
| TG4-P1.png | C02 | Salmon patches on both knees (report: same) |
| TG4-Y2.png | C03/C04, C02 | Teal alien-head chest print where spec says no print (report: same); one leg tan-washed (report: same) |
| TG4-A1.png | C02, C08 | Salmon knee patches (report: same); arms splayed wide vs neutral spec (report: same) |

**Middle result: 3 / 3 artifacts fire, every fire concords with
the round's own census. No unexpected fires.**

### Known-bad (any check firing on none of these is unproven)

| Artifact | Fires | Evidence |
|---|---|---|
| TG4-Y1.png | C03 | Shirt WHITE; spec = fitted black tee (round FAIL basis) |
| TG3-Y1.png | C03, C04 | White shirt + chest glyph-text print (letters UNREADABLE at sheet size, OBSERVATION.md §5) |
| TG2-Y1.png | C06, C03, C02 | Background = repeating pattern of the character's own faces; white shirt; knee patches |
| TG2-Y2.png | C03, C02 | Shirt beige/cream (spec black); knee patches |
| TG2-A2.png | C10, C05, C09, C11 | Eyes solid black ovals; floating heart; hands hidden in hair mass; chibi register vs cel cast |
| TG2-A3.png | C10, C03, C11 | Eyes solid black voids; garment is bandeau+apron, not the specified dress; rough register |
| TG2-A4.png | C03, C05 | Cow-print migrated to stockings/sleeves, dress plain; hair brown (honey specified); floating heart |

**Bad-pool result: 7 / 7 artifacts fire ≥1 check; 16 fires total.**

## 4. Per-check outcome

| Check | Fires on bad (of 7) | Fires on middle (of 3) | Fires on keepers (scoped) | Verdict |
|---|---|---|---|---|
| C01 flat/unlit | 0 | 0 | 0 | **UNPROVEN** — no instance in any pool; keep for 3D lanes or drop at adoption |
| C02 skin wash | 2 | 3 | 0 | Proven (fires bad+middle, clean on keepers) |
| C03 garment spec | 5 | 1 | 0 | Proven — the single highest-yield check in the exercise |
| C04 print error | 1 (+1 shared with C03 on TG4-Y2) | 1 | 0 scoped; 2 spec-blind | Proven **only in spec-relative form** |
| C05 invented motif | 2 | 0 | 0 | Proven |
| C06 background leak | 1 | 0 | 0 | Proven (low frequency, gate-first severity) |
| C07 framing crop | 0 | 0 | 0 scoped; **3 unscoped** | **PRUNE-CANDIDATE (unscoped)**; scoped form UNPROVEN on these pools (round-TG originals carried the class) |
| C08 stance | 0 | 1 | 0 (N/A on kink poses) | Weak-proven (middle only) |
| C09 hands | 1 | 0 | 0 | Proven (low frequency) |
| C10 face/identity | 2 | 0 | 0 | Proven |
| C11 proportion/register | 2 | 0 | 0 | Proven |

Totals: **11 candidate checks; 9 proven on this exercise, 1
UNPROVEN (C01), 1 PRUNE-CANDIDATE in its unscoped form (C07,
scoped form retained as unproven), 1 weak-proven (C08).** Zero
scoped fires on 10 / 10 keepers; 16 fires across 7 / 7 bad
exemplars; 5 fires across 3 / 3 rulable plates, all concordant
with the rounds' own censuses.
