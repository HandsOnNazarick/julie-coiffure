"""Render JULIE_GUIDE.md → printable A4 PDF for client delivery."""
from pathlib import Path

# Load our actual script from skill location, run on the Julie guide
import importlib.util
skill_script = Path(r"C:\Users\alaza\AppData\Local\hermes\skills\printable-pdf-from-markdown\scripts\md_to_pdf.py")
spec = importlib.util.spec_from_file_location("md_to_pdf", skill_script)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

ROOT = Path(r"C:\Users\alaza\projects\julie-coiffure")
md_path = ROOT / "JULIE_GUIDE.md"
pdf_path = ROOT / "JULIE_GUIDE.pdf"

mod.render_md_to_pdf(md_path, pdf_path)
print(f"Généré: {pdf_path}")

import fitz
doc = fitz.open(str(pdf_path))
print(f"Pages: {doc.page_count}")
pix = doc[0].get_pixmap(dpi=110)
preview = ROOT / "_preview.png"
pix.save(str(preview))
print(f"Preview page 1: {preview}")
