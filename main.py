import sys
import random

from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent

app = QtWidgets.QApplication(sys.argv)
width = app.primaryScreen().size().width()
height = app.primaryScreen().size().height()
windows = []


class Hydra(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text = QtWidgets.QLabel("Cut off one head . . .")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)

    def closeEvent(self, _e: QCloseEvent):
        create_window()
        create_window()


def create_window():
    window = Hydra()
    window.move(random.randint(0, width), random.randint(0, height))
    window.show()
    windows.append(window)


create_window()
sys.exit(app.exec())
