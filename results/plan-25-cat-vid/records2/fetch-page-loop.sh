#!/bin/bash
# ns25 page-fetch retry loop: watch page only (no file download).
# Usage: fetch-page-loop.sh <workdir> <cookiejar> <outpage>
set -uo pipefail
WD="$1"; JAR="$2"; OUT="$3"
cd "$WD" || exit 1
UA="Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
URL="https://rule34video.com/video/3663988/cat-vid/"
for i in $(seq 1 60); do
  curl -s -o /dev/null -c "$JAR" -A "$UA" "https://rule34video.com/" --max-time 30
  code=$(curl -s -w "%{http_code}" -b "$JAR" -c "$JAR" -A "$UA" -o "$OUT.tmp" "$URL" --max-time 60)
  sz=$(stat -c %s "$OUT.tmp" 2>/dev/null || echo 0)
  echo "$(date -Is) attempt=$i http=$code bytes=$sz"
  if [ "$code" = "200" ] && [ "$sz" -gt 10000 ]; then
    mv "$OUT.tmp" "$OUT"
    echo "PAGE_OK $(date -Is) bytes=$sz"
    exit 0
  fi
  sleep 45
done
echo "PAGE_FAILED after 60 attempts $(date -Is)"
exit 1
