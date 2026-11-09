# Plan 30 — Technique / Import Contract Note (Pass 2)

**No import contract for the WL artefact exists in this
run, and none is fabricated.** The plan's sole distillation
target was the import contract of the operation shown in
video 3621064 — what the file carries, what the host must
already have, and the failure mode when a dependency is
missing. The artefact was never captured — the origin
404s its ID on both terminal egresses (MANIFEST.md) — so:

- The operation / step list: **NOT OBSERVED.**
- What the imported file carries (scene data; embedded vs
  referenced assets): **NOT OBSERVED.**
- Host preconditions (application, version, plugins,
  packages): **NOT OBSERVED.**
- Missing-dependency failure mode: **NOT OBSERVED** —
  not shown, not stated, not inferred. In particular, no
  Virt-A-Mate behaviour is asserted anywhere in this run:
  the plan's "likely Virt-A-Mate" framing was a guess at
  intake and remains one (INTAKE.md C5).

This file is the closure note the brief allows in place of
a contract note, plus the two items the run *can* honestly
file with the VaM/scene reference material: the dependency-
class comparison (estate side only) and the format-neutral
dependency-contract paragraph that is this plan's SFW
translation. Both are derived from estate records, not
from the missing clip, and are labelled as such.

## Dependency-class comparison (the plan's question)

The plan asks whether a scene import's dependency surprise
is the same class as the estate's own scene records.
**Verdict for the WL artefact: INDETERMINATE — its side of
the comparison was never observed.** The estate side, from
the run records, is documented and is *not* a surprise
class by construction: the D-1 demonstrator's clip records
(`repo/results/d1-demonstrator/clips/*.clip.json`, format
`torogao-motion-clip/1`) carry their dependency **inside
the record itself** — a named skeleton definition
(`skeleton.def`, e.g. `prima-rig/1`) plus its SHA-256 —
and their provenance/retarget blocks repeat the authoring
skeleton's def + hash, so a consumer can verify the exact
dependency, byte-for-byte, before or at import, and a
mismatch is a detectable hash inequality rather than a
silent wrong-scene load; the demonstrator gate in turn
checks `clips_eq` / clip-sha256 sets across twin builds.
Whether WL/VaM-style scene files declare their dependencies
that way, embed them, or leave them to be discovered by
failure is precisely what the missing 29 s would have
shown; this run has no evidence on it and claims none.

## SFW translation — the format-neutral dependency contract

(Written from the estate's own record practice, above;
lane-neutral and safe to carry to any scene/clip format.)

A scene record is importable without surprise iff its
contract states, in the record or its manifest: (1) the
format name and version; (2) every external dependency by
name **and** content hash (skeletons/rigs, packages,
plugins, referenced assets), distinguishing embedded
payload from referenced payload; (3) the host preconditions
(application + minimum version + required extensions);
(4) the failure behaviour on a missing or mismatched
dependency — fail-closed with the dependency named, never
a partial silent load. A record that omits (2) has not
eliminated the dependency; it has converted it into a
surprise at import time. Verification is a pre-import hash
check, not a post-import inspection.

## Clean-room rebuild (Pass 3)

None — per the plan itself ("P3: none — the contract note
is the artefact"), and doubly so on a blocked capture:
there is no observed operation to rebuild.
