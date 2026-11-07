#!/usr/bin/env python3
"""Convierte la página publicada como Artifact (sin <html>/<head>/<body>) en un index.html completo para GitHub/Vercel.
Uso: python3 build_index.py pagina_artifact.html repo/index.html "Descripción corta"
Todo lo que está antes del primer elemento visible (<canvas class="bgdeco"…>, o si no hay, <header>) va al <head>."""
import sys

RESET = ('<style>[hidden]{display:none!important}img{max-width:100%}'
         ':root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>\n')

def main(src, dst, desc=""):
    s = open(src, encoding="utf-8").read()
    cut = s.find('<canvas class="bgdeco"')
    if cut < 0:
        cut = s.find("<header")
    if cut < 0:
        sys.exit("No encontré dónde empieza el contenido visible (<canvas class=\"bgdeco\"> o <header>).")
    head, body = s[:cut], s[cut:]
    meta = f'<meta name="description" content="{desc}">\n' if desc else ""
    doc = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
           '<meta name="theme-color" content="#05070B">\n' + meta + RESET + head +
           '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
    open(dst, "w", encoding="utf-8").write(doc)
    print(f"index.html listo → {dst}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(*sys.argv[1:4])
