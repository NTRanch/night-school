#!/bin/bash
# run_fixup.sh - post-driver fixups: (1) pixel-determinism renders of the
# A builds at the GATED frames (the driver's A renders used the evidence
# frame list; B used gated - the hash needs the same frames on both),
# (2) close bust-camera renders for A builds, (3) sourcing on/off proof
# (near-emitter particle census) for applicability girls + spot clips.
export OMP_NUM_THREADS=8
cd ~/.local/share/pax/nslac
ST=out/status.log
REND="nice -n 10 blender -b -Y -noaudio --python scripts/nslac_render.py --"
HASH="nice -n 10 blender -b -Y -noaudio --python scripts/nslac_pixelhash.py --"
CLOSE="nice -n 10 blender -b -Y -noaudio --python scripts/nslac_closeup.py --"
SRC="nice -n 10 blender -b -Y -noaudio --python scripts/sourcediag.py --"

fix_clip() {  # $1 clipid $2 gated_csv $3 bust_z
  local id=$1 gated=$2 bz=$3
  $REND out/clips/${id}_A/${id}_A_baked.blend out/clips/${id}_A/renders_gated $gated > out/clips/${id}_A.render_gated.log 2>&1
  $HASH $(for f in ${gated//,/ }; do printf "out/clips/${id}_A/renders_gated/full_frame_%04d.png " $f; done) > out/clips/${id}_A/pixelhash_gated.txt 2>&1
  $CLOSE out/clips/${id}_A/${id}_A_baked.blend out/clips/${id}_A/closeups $gated $bz > out/clips/${id}_A.closeup.log 2>&1
  echo "FIX $id done $(date +%H:%M:%S)" >> $ST
}
fix_clip alma_m100_drip   12,24,36 1.33791
fix_clip alma_m100_stream 14,20,28 1.33791
fix_clip alma_m100_spray  14,20,28 1.33791
fix_clip alma_m150_stream 14,20,28 1.33791
fix_clip prima_m100_stream 14,20,28 1.21294
fix_clip prima_m100_drip  12,24,36 1.21294
fix_clip prima_m150_stream 14,20,28 1.21294

for girl in sloane lux piper; do
  $SRC out/appl_${girl}/appl_${girl}_baked.blend out/appl_${girl}/run_record.json > out/appl_${girl}/sourcediag.log 2>&1
  echo "SRC $girl done" >> $ST
done
$SRC out/clips/alma_m100_stream_A/alma_m100_stream_A_baked.blend out/clips/alma_m100_stream_A/run_record.json > out/clips/alma_m100_stream_A/sourcediag.log 2>&1
echo "FIXUP ALL DONE $(date +%H:%M:%S)" >> $ST
