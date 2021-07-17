import sys
import random

from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent

app = QtWidgets.QApplication(sys.argv)
width = app.primaryScreen().size().width()
height = app.primaryScreen().size().height()
windows = []


class Head(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.text = QtWidgets.QLabel("Cut off one head . . .")
        self.text.setStyleSheet("color: white;")
        self.layout.addWidget(self.text)

        self.setWindowTitle("Hydra")
        self.setStyleSheet("background-color: black;")
        self.setFixedSize(200, 50)
        self.move(random.randint(0, width), random.randint(0, height))

        self.show()

    def closeEvent(self, _e: QCloseEvent):
        message = QtWidgets.QMessageBox()
        message.setText("Two more shall take its place!")
        message.setStyleSheet("background-color: red;")
        message.exec()

        create_window()
        create_window()
        windows.remove(self)


def create_window():
    window = Head()
    windows.append(window)


create_window()
sys.exit(app.exec())
