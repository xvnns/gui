import sys
import random

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QFont


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('3 Digit Number Generator')
        self.setGeometry(600, 800, 400, 200)

        self.btn = QPushButton(self)
        self.btn.move(150, 100)
        self.btn.setText("Generate new!")
        self.btn.adjustSize()
        self.btn.clicked.connect(self.randint_to_text)

        self.msg = QLabel(self)
        self.msg.move(120, 60)
        self.msg.setFont(QFont('Arial', 12))
        self.randint_to_text()

    def randint_to_text(self):
        self.msg.setText("Random integer: %s" % random.randint(100, 1000))
        self.msg.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())
