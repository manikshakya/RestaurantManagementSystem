from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton)
from PyQt5.QtCore import (QRect, Qt)
from PyQt5.QtCore import Qt

class Footer(QFrame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        frame2 = QFrame(self)
        # frame2.setGeometry(QRect(0, 700, 800, 160))
        frame2.setStyleSheet("background-color: rgb(30, 45, 66);")
        frame2.setFrameShape(QFrame.StyledPanel)
        frame2.setFrameShadow(QFrame.Raised)
        # frame.setObjectName("frame")
        # frame2.setFixedWidth(self.width())
        frame2.setMinimumWidth(800)
        frame2.setFixedHeight(50)

        layout = QVBoxLayout()
        layout.addWidget(frame2)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)
        # self.resize(800, 50)