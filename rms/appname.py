from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton)
from PyQt5.QtCore import (QRect, Qt)
from PyQt5.QtCore import Qt

class AppName(QFrame):

    def __init__(self, title):
        super().__init__()

        self.initUI(title)

        '''
            Add argument to decide which initUI() to call.
            Create if/else to view different initUI().
        '''


    def initUI(self, title):

        frame = QFrame()
        frame.setStyleSheet("background-color: rgb(30, 45, 66);")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setMinimumWidth(800)
        frame.setFixedHeight(160)

        main_label = QLabel(frame)
        main_label.setGeometry(QRect(300, 60, 233, 57))
        main_label.setStyleSheet("font: 75 28pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 36pt \"MS Shell Dlg 2\";")

        if title == "login":
            main_label.setText("Food Fest")
        elif title == "dashboard":
            main_label.setText("Dashboard")
        elif title == "employees":
            main_label.setText("Employees")
        elif title == "users":
            main_label.setText("Users")
        elif title == "tables":
            main_label.setText("Tables")
        elif title == "reservations":
            main_label.setText("Reservations")
        elif title == "category":
            main_label.setText("Categories")
        elif title == "orders":
            main_label.setText("Orders")
        elif title == "menu":
            main_label.setText("Menu")
        elif title == "settings":
            main_label.setText("Settings")
        elif title == "bills":
            main_label.setText("Bills")

        layout = QVBoxLayout()
        layout.addWidget(frame)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)
        # self.resize(800, 250)


