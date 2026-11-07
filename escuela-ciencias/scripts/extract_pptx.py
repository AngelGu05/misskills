#!/usr/bin/env python3
"""Extrae texto, notas e imágenes de un .pptx, diapositiva por diapositiva.
Uso: python3 extract_pptx.py clase.pptx carpeta_salida/
Imprime el texto en orden y guarda las imágenes como slideN_imgK.ext para revisarlas una por una."""
import os, sys
try:
    from pptx import Presentation
except ImportError:
    sys.exit("Falta python-pptx: pip install python-pptx")

def main(path, out):
    os.makedirs(out, exist_ok=True)
    prs = Presentation(path)
    for i, slide in enumerate(prs.slides, 1):
        print(f"--- Diapositiva {i}")
        k = 0
        for sh in slide.shapes:
            if sh.has_text_frame and sh.text_frame.text.strip():
                print(sh.text_frame.text.strip())
            if getattr(sh, "has_table", False) and sh.has_table:
                for row in sh.table.rows:
                    print(" | ".join(c.text.strip() for c in row.cells))
            if sh.shape_type == 13:  # imagen
                k += 1
                img = sh.image
                fn = os.path.join(out, f"slide{i}_img{k}.{img.ext}")
                with open(fn, "wb") as f:
                    f.write(img.blob)
                print(f"[imagen → {fn}]")
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text.strip()
            if notes:
                print("NOTAS:", notes)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
