#!/usr/bin/env bash
# Descarga los subtítulos de un video de YouTube y los convierte en texto con marcas de tiempo.
# Uso: youtube_transcript.sh "<url>" [carpeta_salida]
set -euo pipefail
URL="${1:?Falta la URL del video}"
OUT="${2:-./transcripcion}"
mkdir -p "$OUT"
command -v yt-dlp >/dev/null 2>&1 || pip install -q yt-dlp
yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "es.*,en.*" --sub-format vtt \
  --print "%(title)s | %(channel)s | %(duration_string)s" --no-simulate -o "$OUT/video.%(ext)s" "$URL" || {
  echo "No se pudo descargar. Si el error es 403 / Tunnel connection failed / ENOTFOUND, la red bloquea YouTube:" >&2
  echo "pide al usuario el texto de 'Mostrar transcripción' o que permita www.youtube.com en la red del entorno." >&2
  exit 2; }
VTT=$(ls "$OUT"/*.vtt 2>/dev/null | head -1)
[ -n "$VTT" ] || { echo "El video no tiene subtítulos." >&2; exit 3; }
# VTT -> "m:ss texto", sin duplicados (los automáticos repiten líneas)
python3 - "$VTT" "$OUT/transcripcion.txt" <<'PY'
import re,sys
src,dst=sys.argv[1],sys.argv[2];out=[];last=None;t=None
for line in open(src,encoding='utf-8'):
    line=line.strip()
    m=re.match(r'(\d+):(\d+):(\d+)\.\d+ -->',line) or re.match(r'(\d+):(\d+)\.\d+ -->',line)
    if m:
        g=[int(x) for x in m.groups()];s=g[0]*3600+g[1]*60+g[2] if len(g)==3 else g[0]*60+g[1];t=f"{s//60}:{s%60:02d}";continue
    if not line or line.startswith(('WEBVTT','Kind:','Language:')) or t is None: continue
    txt=re.sub(r'<[^>]+>','',line).strip()
    if txt and txt!=last: out.append(f"{t} {txt}");last=txt
open(dst,'w',encoding='utf-8').write('\n'.join(out)+'\n')
print(f"{len(out)} líneas → {dst}")
PY
