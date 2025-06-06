from core.ocr import extract_text

if __name__ == "__main__": # Executes only when run directly [not invoked]
    text = extract_text("data/Picture1.png")
    print(text)
