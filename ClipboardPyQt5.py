import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit,
    QPushButton, QVBoxLayout, QHBoxLayout
)

class ClipboardDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clipboard Example")
        self.resize(600, 400)

        # Text edits
        self.text1 = QTextEdit()
        self.text2 = QTextEdit()

        # Buttons
        copy_btn = QPushButton("Copy")
        paste_btn = QPushButton("Paste")

        copy_btn.clicked.connect(self.copy_text)
        paste_btn.clicked.connect(self.paste_text)

        # Button layout
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(copy_btn)
        btn_layout.addWidget(paste_btn)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addLayout(btn_layout)
        layout.addWidget(self.text2)

        self.setLayout(layout)

        # Clipboard
        self.clipboard = QApplication.clipboard()

    def copy_text(self):
        self.clipboard.setText(self.text1.toPlainText())

    def paste_text(self):
        self.text2.setPlainText(self.clipboard.text())

# Run application
app = QApplication(sys.argv)
window = ClipboardDemo()
window.show()
sys.exit(app.exec_())
