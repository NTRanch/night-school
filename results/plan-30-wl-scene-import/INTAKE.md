# Plan 30 — Intake (Pass 0) — CAPTURE-BLOCKED / SOURCE-NOT-FOUND

Plan: `repo/plans/30-wl-scene-import.md` — "WL Scene
Import" (rule34video 3621064), micro-plan. The deliverable
was the IMPORT CONTRACT note: the operation, its
preconditions/dependencies, its failure mode, with the
stated 29 seconds fully accounted for. **None of that is
accountable in this run**, because the origin no longer
serves the artefact at the plan's URL (evidence in
MANIFEST.md). The gap is recorded instead of filled; per
the plan's own gate, "if the clip shows less, the record
says so" — here the clip shows nothing, and the record
says exactly that.

## SHOULD-BE-SEEN (from the plan, written before viewing)

"One operation, start to finish: file in, scene loaded,
the one thing to check." — **Not tested.** No operation
was observed; no step list, setting, or end-check exists
in this run.

## Numbered claims / evidence actually in hand

| # | Claim | Provenance |
|---|---|---|
| C1 | The origin serves an application-level **404 Not Found** (384 B XHTML body, JS redirect to `/404.php`, SHA-256 `fd562038072a7a48…`) for video 3621064, slugged and slug-less, from **both** terminal egresses, across repeated attempts. Interleaved 503s are the origin's DB-fatal body (93 B, `a990dd3f8fdc4d79…`), which also struck control and search fetches. | `records/route-log.txt`; `dl/target-sandbox.html` |
| C2 | Both routes are healthy: same-egress, same-jar, same-method **control** video 4293878 fetched **200 / 259,287 B** with its correct title from the sandbox and from primo. The failure is target-specific, not route-, egress-, or policy-shaped. | `dl/control-sandbox.html`; MANIFEST.md §Capture route |
| C3 | The plan's stated duration **0:29 is NOT verified** — no watch page and no file exist for this ID. Duration of record: plan-stated only; real duration unknown. | MANIFEST.md §Pinned capture |
| C4 | The site's own search for "wl scene import" (200) does **not** list ID 3621064. Its top hit is a **different** ID, 3569655, "WL Scene Import (Secret Recipe Tutorial)". A different ID is a different artefact and was **not substituted** for the target. | `dl/search-wl-scene-import-sandbox.html` |
| C5 | **"WL" identification: UNRESOLVED.** The target artefact that could settle it (page metadata + on-screen evidence) does not exist in this run. See the leads below — leads, not an identification. | This file, §WL leads |
| C6 | The operation, its step list, every setting, the import contract, and the missing-dependency failure mode are all **NOT OBSERVED** — not "absent from the clip", but unobservable because there is no clip. | OBSERVATION.md; TECHNIQUE.md |

## WL leads (contextual, NOT an identification of the target)

1. The search page for "wl scene import" also lists other
   items carrying a "WL - " title prefix (e.g. 3103443
   "WL - Max Scrof Minigame", 3091819 "WL - Byron (Kral) x
   Maya and Max") — consistent with **WL being a maker /
   series mark** used as a title prefix across multiple
   uploads, rather than a file format. (`dl/search-wl-scene-import-sandbox.html`)
2. The same-title sibling 3569655 (2024-10-20, 14 s per its
   JSON-LD) describes itself as a supporters-only teaser
   whose "secret recipe" lives on a Patreon page naming
   the handle `absurdcookie` — consistent with WL being
   that maker's project/series name, with "scene import"
   being a technique the maker withholds as a paid recipe.
   (`dl/sibling-3569655-sandbox.html`)
3. Nothing in either lead mentions Virt-A-Mate, a scene
   file format, or any host application. The plan's "likely
   Virt-A-Mate" framing and its "format or author mark"
   question therefore remain **open**: the author-mark
   reading has weak circumstantial support; the VaM reading
   has none from this run. Recorded answer: **UNRESOLVED**.

## Licence as seen

**Not seen** (no page for the target). See MANIFEST.md.

## Audio posture

No media obtained; nothing played, transcribed, or
inspected. The bounded-whisper step was not run — there
is no file to slice, and the census-is-a-screen discipline
licenses nothing on an absent artefact. Audio silence rule
satisfied trivially. UNREADABLE count: not applicable —
zero frames, zero audio, zero UI text from the target
(the only UI text read this run is the origin's 404 body
and the control/search/sibling pages, all fully legible).
