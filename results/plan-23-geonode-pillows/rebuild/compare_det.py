"""Determinism compare: vertex hashes from measures JSONs +
pixel hashes of the two demo renders (decoded pixels, not bytes).
Usage: blender -b -noaudio -Y --python compare_det.py -- OUTDIR
"""
import bpy
import hashlib
import json
import os
import sys

outdir = sys.argv[sys.argv.index('--') + 1]
ma = json.load(open(os.path.join(outdir, 'measures_demo_A.json')))
mb = json.load(open(os.path.join(outdir, 'measures_demo_B.json')))


def pixel_hash(path):
    img = bpy.data.images.load(path)
    h = hashlib.sha256()
    px = img.pixels[:]
    import array
    arr = array.array('f', px)
    h.update(arr.tobytes())
    return h.hexdigest(), img.size[:]


ha, sa = pixel_hash(os.path.join(outdir, 'demo_A.png'))
hb, sb = pixel_hash(os.path.join(outdir, 'demo_B.png'))
out = dict(vert_hash_A=ma['vert_hash'], vert_hash_B=mb['vert_hash'],
           verts_identical=ma['vert_hash'] == mb['vert_hash'],
           measures_identical={k: ma[k] == mb[k] for k in
                               ('verts', 'faces', 'dent_depth', 'apex_z',
                                'contact_min_z', 'bbox')},
           pixel_hash_A=ha, pixel_hash_B=hb, render_size=list(sa),
           pixels_identical=ha == hb)
with open(os.path.join(outdir, 'determinism.json'), 'w') as f:
    json.dump(out, f, indent=1, sort_keys=True)
print('NS23-DET verts_identical=%s pixels_identical=%s' % (
    out['verts_identical'], out['pixels_identical']))
