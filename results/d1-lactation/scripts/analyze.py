#!/usr/bin/env python3
# analyze.py - assemble the lactation gate table from primo-copied artifacts
# under results/ (the local results tree mirrors primo out/). Every number
# in GATE-RECORD.md traces to the JSON/txt files read here.
import json, os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "results"
CLIPS = ["alma_m100_drip", "alma_m100_stream", "alma_m100_spray",
         "alma_m150_stream", "prima_m100_stream", "prima_m100_drip",
         "prima_m150_stream"]
GATED = {"alma_m100_drip": [12, 24, 36], "prima_m100_drip": [12, 24, 36]}

def gated(cid):
    return GATED.get(cid, [14, 20, 28])

def load(p):
    with open(p) as fh:
        return json.load(fh)

def pixelhashes(p):
    out = {}
    if not os.path.exists(p):
        return out
    txt = open(p).read()
    i = txt.find("PIXELHASH_JSON ")
    if i >= 0:
        obj, _ = json.JSONDecoder().raw_decode(txt[i + 15:])
        for k, v in obj.items():
            out[k] = v["pixel_sha256"]
    return out

report = {"clips": {}, "sens": {}, "appl": {}}
for cid in CLIPS:
    g = gated(cid)
    entry = {}
    for t in ("A", "B"):
        d = os.path.join(ROOT, "clips", cid + "_" + t)
        rec = load(os.path.join(d, "run_record.json"))
        meas = load(os.path.join(d, "measurements.json"))["frames"]
        entry[t] = {"rec": rec, "meas": meas}
        entry.setdefault("interior_gated", {})[t] = \
            {str(f): meas[str(f)]["interior"] for f in g}
        entry.setdefault("interior_max_loop", {})[t] = \
            max(r["interior"] for r in meas.values())
        entry.setdefault("counts", {})[t] = \
            {f: r["particles"] for f, r in meas.items()}
    entry["counts_identical"] = entry["counts"]["A"] == entry["counts"]["B"]
    pa = os.path.join(ROOT, "clips", cid + "_A", "pixelhash_gated.txt")
    ha = pixelhashes(pa if os.path.exists(pa) else os.path.join(ROOT, "clips", cid + "_A", "pixelhash.txt"))
    hb = pixelhashes(os.path.join(ROOT, "clips", cid + "_B", "pixelhash.txt"))
    entry["pixel_gated"] = {
        f: {"A": ha.get("full_frame_%04d.png" % f),
            "B": hb.get("full_frame_%04d.png" % f),
            "equal": ha.get("full_frame_%04d.png" % f) is not None and
                     ha.get("full_frame_%04d.png" % f) ==
                     hb.get("full_frame_%04d.png" % f)}
        for f in g[:2]}
    for t in ("A", "B"):
        mh = os.path.join(ROOT, "clips", cid + "_" + t, "meshhash.txt")
        entry.setdefault("meshhash", {})[t] = \
            open(mh).read().strip() if os.path.exists(mh) else None
    entry["meshhash_equal"] = \
        entry["meshhash"]["A"] is not None and \
        entry["meshhash"]["A"].split()[1] == entry["meshhash"]["B"].split()[1]
    abc = os.path.join(ROOT, "clips", cid + "_A", "abc.sha256")
    entry["abc_sha256"] = open(abc).read().strip() if os.path.exists(abc) else None
    report["clips"][cid] = entry

for tag in ("lo", "hi"):
    d = os.path.join(ROOT, "sens_" + tag)
    if os.path.exists(d):
        report["sens"][tag] = {
            "rec": load(os.path.join(d, "run_record.json")),
            "meas": load(os.path.join(d, "measurements.json"))["frames"]}
for girl in ("yui", "sloane", "lux", "piper"):
    d = os.path.join(ROOT, "appl_" + girl)
    if os.path.exists(d):
        report["appl"][girl] = {
            "rec": load(os.path.join(d, "run_record.json")),
            "meas": load(os.path.join(d, "measurements.json"))["frames"]}

with open(os.path.join(ROOT, "gate-table.json"), "w") as fh:
    json.dump(report, fh, indent=2, default=str)
print("gate-table written:", len(report["clips"]), "clips,",
      len(report["sens"]), "sens,", len(report["appl"]), "appl")
for cid, e in report["clips"].items():
    print(cid, "counts_identical=", e["counts_identical"],
          "interior_gated A=", e["interior_gated"]["A"],
          "loop_max A=", e["interior_max_loop"]["A"],
          "pixel=", {f: v["equal"] for f, v in e["pixel_gated"].items()},
          "mesh_eq=", e["meshhash_equal"])
