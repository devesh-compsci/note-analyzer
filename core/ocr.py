from PIL import Image
import pytesseract as pytes

def extract_text(image_path):
    text = pytes.image_to_string(Image.open(image_path))
    return text
