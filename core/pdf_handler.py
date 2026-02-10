import fitz
from pdf2image import convert_from_path
from core.ocr import extract_text

def extract_text_from_pdf(pdf_path):
    text = ''

    #----- Try Else -----
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()

    if text.strip():
        return text

images = convert_from_path(pdf_path)
for img in images:
    text += extract_text(img)

return text

# ----- Fallback -----
images = convert_from_path(pdf_path)
for img in images:
    text += extract_text(img)

return text
