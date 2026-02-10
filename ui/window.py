from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel,
    QTextEdit, QFileDialog, QVBoxLayout, QWidget, QTabWidget
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from core.summarizer_offline import summarize_text
from core.ocr import extract_text
import logging
import sys

# -------- logging (terminal only) --------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)


class NoteAnalyzerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Note Analyzer")
        self.setWindowIcon(QIcon('ui/icon.png'))
        self.setGeometry(100, 100, 800, 600)

        self.setAcceptDrops(True)

        # Main Layout
        main_layout = QVBoxLayout()
        self.tabs = QTabWidget()

        # ========= TAB 1: OCR =========
        ocr_tab = QWidget()
        ocr_layout = QVBoxLayout()

        self.upload_btn = QPushButton("Upload File")
        self.upload_btn.clicked.connect(self.load_file)
        ocr_layout.addWidget(self.upload_btn)

        self.drop_label = QLabel("(Or)\n⬇️Drag & Drop a file here")
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.drop_label.setStyleSheet("border: 2px dashed gray; padding: 20px;")
        ocr_layout.addWidget(self.drop_label)

        self.output_box = QTextEdit()
        ocr_layout.addWidget(self.output_box)

        ocr_tab.setLayout(ocr_layout)
        self.tabs.addTab(ocr_tab, "OCR")

        # ========= TAB 2: SUMMARY =========
        summary_tab = QWidget()
        summary_layout = QVBoxLayout()

        self.summary_box = QTextEdit()
        self.summary_box.setPlaceholderText("Summary will appear here...")
        summary_layout.addWidget(self.summary_box)

        self.summary_btn = QPushButton("Generate Summary")
        self.summary_btn.clicked.connect(self.generate_summary)
        summary_layout.addWidget(self.summary_btn)

        summary_tab.setLayout(summary_layout)
        self.tabs.addTab(summary_tab, "Summary")

        main_layout.addWidget(self.tabs)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def generate_summary(self):
        text = self.output_box.toPlainText()
        summary = summarize_text(text)
        self.summary_box.setText(summary)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Image Files (*.png *.jpg *.jpeg *.pdf)"
        )
        if file_path:
            logger.info(f"file selected: {file_path}")
            try:
                text = extract_text(file_path)
                self.output_box.setText(text)
                logger.info("Text Extraction succesful")
            except Exception:
                logger.exception("Text Extraction failed")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith((".png", ".jpg", ".jpeg", ".pdf")):
                self.process_image(file_path)

    def process_image(self, file_path):
        text = extract_text(file_path)
        self.output_box.setText(text)


def run_app():
    logger.info("Application Starting...")
    app = QApplication(sys.argv)
    window = NoteAnalyzerApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_app()

