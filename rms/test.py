from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton)
from PyQt5.QtCore import (QRect, Qt)
from PyQt5.QtCore import Qt

from login import Login
from appname import AppName

from classes2.db import DB

class Test(QMainWindow):

    def __init__(self):
        super().__init__()

        self.db = DB()

        self.initUI()

    def initUI(self):
        t1 = AppName("")
        t1.setMaximumWidth(600)
        t1.setGeometry(100, 0, 600, 160)

        t2 = Login()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(t2)
        layout.addWidget(t1)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

        self.resize(800, 1000)
        self.setWindowTitle("Test")

        self.show()