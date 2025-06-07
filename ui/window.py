from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QFileDialog, QVBoxLayout, QWidget
import sys
from core.ocr import extract_text

class NoteAnalyzerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Note Analyzer")
        self.setGeometry(100, 100, 800, 600)

        #Main Layout
        layout = QVBoxLayout()

        # Button-Upload
        self.upload_btn = QPushButton("Upload Image")
        self.upload_btn.clicked.connect(self.load_image)
        layout.addWidget(self.upload_btn)

        # Output-Text_Result
        self.output_box = QTextEdit()
        layout.addWidget(self.output_box)

        # Container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image","","Image Files (*.png *.jpg *.jpeg)")
        if file_path:
            text = extract_text(file_path)
            self.output_box.setText(text)
            
def run_app():
    app = QApplication(sys.argv)
    window = NoteAnalyzerApp()
    window.show()
    sys.exit(app.exec_())

