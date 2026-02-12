# 🧠 Note Analyzer

A modular, offline-first desktop application for extracting and analyzing academic documents.

Built with Python and PyQt5, this project combines OCR, PDF parsing, and extractive NLP summarization into a structured document analysis tool.

---

## 🚀 Features

### 📄 OCR Support
- Extract text from images (PNG, JPG, JPEG)
- Drag & drop support
- Powered by Tesseract OCR

### 📚 PDF Support
- Direct text extraction for digital PDFs
- Automatic OCR fallback for scanned PDFs

### 🧾 Offline Summarization
- Extractive summarization using:
  - TF-IDF
  - Cosine similarity
  - PageRank-based ranking
- Fully offline
- No API keys required

---

## 🏗 Project Structure

```
note-analyzer/
│
├── main.py
│
├── core/
│   ├── ocr.py
│   ├── summarizer_offline.py
│   └── pdf_handler.py
│
├── ui/
│   └── window.py
│
└── requirements.txt
```

Design goals:
- Separation of UI and processing logic
- Extensible backend (future LLM integration ready)
- Offline-first architecture

---

## ⚙ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/devesh-compsci/note-analyzer.git
cd note-analyzer
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run

```bash
python main.py
```

---

## 📦 Core Dependencies

- PyQt5
- pytesseract
- Pillow
- nltk
- scikit-learn
- networkx
- PyMuPDF (fitz)
- pdf2image

---

## 🧠 Roadmap

Planned upgrades:

- Keyword extraction
- Document classification
- SQLite document storage
- Semantic search (embeddings)
- Hybrid LLM summarization
- Background processing

---

## 🎯 Vision

To evolve into a modular academic document analysis system capable of:

- Structured note summarization  
- Intelligent topic detection  
- Semantic document search  
- Offline knowledge management  

---

