from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("vellum-lensed")
        label = QLabel("Crafting Tree Browser — set DataForge path to begin")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
