import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QMessageBox, QVBoxLayout
)

class MessageBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox Demo")
        self.setFixedSize(500, 400)

        button = QPushButton("Show Message Box")
        button.clicked.connect(self.show_message)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

    def show_message(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Welcome to PyQt5")
        msg.setText(
            "Congratulations! You have successfully displayed a QMessageBox."
        )

        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setEscapeButton(QMessageBox.Cancel)

        msg.exec_()

app = QApplication(sys.argv)
window = MessageBoxDemo()
window.show()
sys.exit(app.exec_())
