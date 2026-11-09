# ns07_pixelhash.py - hash DECODED PIXELS of PNGs (never file hashes: Blender
# writes volatile PNG tEXt metadata). Usage:
# blender -b -Y --python ns07_pixelhash.py -- <img1> [img2 ...]  -> prints sha256 per file
import bpy, sys, hashlib, json
argv = sys.argv[sys.argv.index("--") + 1:]
out = {}
for path in argv:
    img = bpy.data.images.load(path)
    px = img.pixels[:]  # floats 0..1, RGBA
    raw = bytearray(len(px))
    for i, v in enumerate(px):
        raw[i] = max(0, min(255, round(v * 255)))
    h = hashlib.sha256(bytes(raw)).hexdigest()
    out[path.split("/")[-1]] = {"size": list(img.size), "pixel_sha256": h}
    bpy.data.images.remove(img)
print("PIXELHASH_JSON " + json.dumps(out, indent=2))
