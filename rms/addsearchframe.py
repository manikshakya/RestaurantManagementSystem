from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton)
from PyQt5.QtCore import (QRect, Qt)
from PyQt5.QtCore import Qt

class AddSearchFrame(QFrame):

    def __init__(self, addButton):
        super().__init__()

        self.initUI(addButton)

    def initUI(self, addButton):

        frame = QFrame()
        # frame.setStyleSheet("background-color: rgb(30, 45, 66);")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setMinimumWidth(960)
        frame.setFixedHeight(80)
        frame.setStyleSheet("border: none")

        self.add_button = QPushButton(frame)
        self.add_button.setGeometry(QRect(20, 10, 180, 41))
        self.add_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(30, 45, 66);\n"
                                 "color: rgb(255, 255, 255);")

        if addButton == "employees":
            self.add_button.setText("Add Employee")
        elif addButton == "reservations":
            self.add_button.setText("Add Reservations")
        elif addButton == "category":
            self.add_button.setText("Add Category")
        elif addButton == "tables":
            self.add_button.setText("Add Table")
        elif addButton == "stocks":
            self.add_button.setText("Add Stocks")
        elif addButton == "menu":
            self.add_button.setText("Add Menu Item")
        elif addButton == "bill":
            self.add_button.setText("Add Bill")

        self.add_button.setMinimumWidth(180)
        self.add_button.setMinimumHeight(40)
        # self.add_button.clicked.connect(lambda: self.findClick(addButton))

        self.search_box = QLineEdit(frame)
        self.search_box.setGeometry(QRect(230, 10, 560, 41))
        self.search_box.setMinimumWidth(540)
        self.search_box.setMinimumHeight(40)

        self.search_button = QPushButton(frame)
        self.search_button.setGeometry(QRect(810, 10, 130, 41))
        self.search_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(30, 45, 66);\n"
                                 "color: rgb(255, 255, 255);")
        self.search_button.setText("Search")
        self.search_button.setMinimumWidth(130)
        self.search_button.setMinimumHeight(40)

        layout = QHBoxLayout()
        layout.addWidget(frame)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)

    # I don't think we need this.
    def findClick(self, where):
        if where == "employees":
            print("Employee Button Clicked from inside")
            return "Employee Button Clicked"
            # view = AddEmployeeDetails(self)
            # view.show()
        elif where == "stocks":
            print("Stock Button Clicked")
        elif where == "reservation":
            print("Stock Button Clicked")