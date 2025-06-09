from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QFileDialog, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QRect
import sys
from core.ocr import extract_text

class NoteAnalyzerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Note Analyzer")
        self.setWindowIcon(QIcon('ui\\icon.png'))
        self.setGeometry(100, 100, 800, 600)

        # Drag and Drop
        self.setAcceptDrops(True)

        #Main Layout
        layout = QVBoxLayout()

        # Button-Upload
        self.upload_btn = QPushButton("Upload Image")
        self.upload_btn.setGeometry(QRect(20, 20, 80, 80)) #not working need to check
        self.upload_btn.clicked.connect(self.load_image)
        layout.addWidget(self.upload_btn)

        # Hover - Drag-and-drop
        self.drop_label = QLabel("(Or)\n⬇️Drag & Drop an image here", self)
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.drop_label.setStyleSheet("border: 2px dashed gray; padding: 20px; font-size: 16px;")
        layout.addWidget(self.drop_label)

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

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith((".png", ".jpg", ".jpeg")):
                self.process_image(file_path)

    def process_image(self, file_path):
        text = extract_text(file_path)
        self.output_box.setText(text)
            
def run_app():
    app = QApplication(sys.argv)
    window = NoteAnalyzerApp()
    window.show()
    sys.exit(app.exec_())

