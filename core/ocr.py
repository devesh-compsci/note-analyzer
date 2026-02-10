from PIL import Image
import pytesseract as pytes
from pdf2image import convert_from_path
import os

def extract_text(path):
    ext = os.path.splitext(path)[1].lower()

    # ---------- IMAGE ----------
    if ext in [".png", ".jpg", ".jpeg"]:
        return pytes.image_to_string(Image.open(path))

    # ---------- PDF ----------
    elif ext == ".pdf":
        text = ""
        images = convert_from_path(path)
        for img in images:
            text += pytes.image_to_string(img) + "\n"
        return text

    else:
        raise ValueError("Unsupported file type")

