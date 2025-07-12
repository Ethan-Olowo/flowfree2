import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
import ui.theme as theme

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Flow Free 2 - Home")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        title = QLabel("Flow Free 2")
        title.setStyleSheet(theme.titleStyle)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        start_btn = QPushButton("Start")
        timed_btn = QPushButton("Timed")

        layout.addWidget(start_btn)
        layout.addWidget(timed_btn)

        self.setLayout(layout)

        # start_btn.clicked.connect(self.show_menu)
        # timed_btn.clicked.connect(self.show_timed_menu)

