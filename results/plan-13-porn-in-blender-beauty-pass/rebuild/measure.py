# NS13 measurement gate — compare EXR outputs pixel by pixel.
# Usage: python3 measure.py <dirA> [dirB]
#   Within dirA: compares beauty_image vs recreated (MATCH, raw),
#   beauty_image vs recreated_denoised, noisy_image vs recreated,
#   recreated_denoised vs variant (MODIFY), recreated vs variant.
#   If dirB given: decoded-pixel hash equality of recreated / variant /
#   recreated_denoised between dirA and dirB (determinism).
# EXR files written by Blender's compositor File Output carry a frame
# number suffix (0001) — resolved by glob.
import glob, hashlib, json, os, sys
import numpy as np
import OpenEXR

def find(d, base):
    hits = sorted(glob.glob(os.path.join(d, base + "*.exr")))
    hits = [h for h in hits if "multilayer" not in h]
    return hits[0] if hits else None

def read_rgba(path):
    # Channels are read in the file's own pixel type (header-declared).
    # NOTE: an earlier version passed OpenEXR.FLOAT (invalid in OpenEXR 3.5)
    # and silently substituted ones on failure — producing identical hashes
    # for every file. That defect was caught by the identical-hash smell and
    # this reader now fails loudly instead of fabricating data.
    f = OpenEXR.InputFile(path)
    hdr = f.header()
    dw = hdr['dataWindow']
    w = dw.max.x - dw.min.x + 1
    h = dw.max.y - dw.min.y + 1
    chans = []
    for c in ('R', 'G', 'B', 'A'):
        if c == 'A' and 'A' not in hdr['channels']:
            chans.append(np.ones((h, w), dtype=np.float32))
            continue
        tname = str(hdr['channels'][c].type)
        dt = {'HALF': np.float16, 'FLOAT': np.float32, 'UINT': np.uint32}[tname]
        buf = f.channel(c)
        chans.append(np.frombuffer(buf, dtype=dt).reshape(h, w).astype(np.float32))
    return np.stack(chans, axis=-1), hdr

def decoded_hash(arr):
    return hashlib.sha256(np.ascontiguousarray(arr, dtype=np.float32).tobytes()).hexdigest()

def compare(name, a, b, tols=(1e-6, 1e-4, 1.0 / 255.0)):
    d = np.abs(a[..., :3] - b[..., :3])
    per_pixel_max = d.max(axis=-1)
    out = {"pair": name,
           "mean_abs_diff": float(d.mean()),
           "max_abs_diff": float(d.max()),
           "rms_diff": float(np.sqrt((d ** 2).mean())),
           "hash_a": decoded_hash(a), "hash_b": decoded_hash(b),
           "hash_equal": decoded_hash(a) == decoded_hash(b)}
    for t in tols:
        out[f"pct_pixels_beyond_{t:g}"] = float((per_pixel_max > t).mean() * 100.0)
    return out

def main():
    dA = sys.argv[1]
    dB = sys.argv[2] if len(sys.argv) > 2 else None
    files = {}
    for base in ("beauty_image", "noisy_image", "recreated", "recreated_denoised", "variant"):
        p = find(dA, base)
        if p:
            files[base] = read_rgba(p)[0]
            print(f"{base}: {p} shape={files[base].shape} decoded_sha256={decoded_hash(files[base])}")
        else:
            print(f"{base}: MISSING in {dA}")
    results = []
    pairs = [("MATCH recreated vs renderer beauty (Image)", "recreated", "beauty_image"),
             ("MATCH recreated vs Noisy Image", "recreated", "noisy_image"),
             ("denoised recreation vs renderer beauty (Image)", "recreated_denoised", "beauty_image"),
             ("MODIFY variant vs recreated_denoised", "variant", "recreated_denoised"),
             ("MODIFY variant vs recreated (raw)", "variant", "recreated")]
    for label, x, y in pairs:
        if x in files and y in files:
            r = compare(label, files[x], files[y])
            results.append(r)
            print(json.dumps(r, indent=1))
    if dB:
        det = {}
        for base in ("recreated", "recreated_denoised", "variant"):
            pB = find(dB, base)
            if pB and base in files:
                arrB = read_rgba(pB)[0]
                det[base] = {"hash_runA": decoded_hash(files[base]),
                             "hash_runB": decoded_hash(arrB),
                             "equal": decoded_hash(files[base]) == decoded_hash(arrB)}
                print("DETERMINISM", base, det[base])
        results.append({"determinism": det})
    with open(os.path.join(dA, "measurements.json"), "w") as f:
        json.dump(results, f, indent=1)

main()
