import sys
from PySide6.QtGui import QWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Hydra")
    window.resize(200, 50)

    label = QLabel(text="Cut off one head . . .")
    layout = QVBoxLayout()
    layout.addWidget(label)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
