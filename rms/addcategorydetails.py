from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QDateEdit, QComboBox)
from PyQt5.QtCore import (QRect, Qt, QDate, pyqtSignal)
from PyQt5.QtGui import (QIntValidator)

from classes2.db import DB

import datetime


class AddCategoryDetails(QMainWindow):

    closing = pyqtSignal(int)

    def __init__(self, parent, update, id=None):
        super().__init__(parent)

        self.db = DB()

        self.initUI(update, id)

    def initUI(self, update, id):

        self.setWindowModality(Qt.ApplicationModal)

        frame = QFrame()
        # frame.setStyleSheet("background-color: rgb(30, 45, 66);")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        # frame.setMinimumWidth(430)
        # frame.setFixedHeight(395)
        frame.setStyleSheet("border: none")

        add_employee_button = QLabel(frame)
        add_employee_button.setAlignment(Qt.AlignCenter)
        add_employee_button.setGeometry(QRect(110, 30, 210, 41))
        add_employee_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(30, 45, 66);\n"
                                 "color: rgb(255, 255, 255);")
        add_employee_button.setText("Add Category Details")

        # name = QHBoxLayout()
        # jobtitle = QHBoxLayout()
        # salary = QHBoxLayout()
        # bonus = QHBoxLayout()
        # joindate = QHBoxLayout()

        category_name = QLabel(frame)
        category_name.setText("Category Name")
        category_name.setGeometry(QRect(45, 100, 95, 13))

        self.categorytextbox = QLineEdit(frame)
        self.categorytextbox.setGeometry(QRect(160, 90, 181, 31))
        self.categorytextbox.setFixedWidth(180)

        self.addbutton = QPushButton(frame)
        self.addbutton.setText("Add Category")
        self.addbutton.setGeometry(QRect(160, 300, 151, 31))
        self.addbutton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(30, 45, 66);\n"
                                   "color: rgb(255, 255, 255);")
        # self.addbutton.clicked.connect(lambda: self.add_button_click("tables"))

        if update == 'add':
            print("Add")
            print(id)
            self.addbutton.setText("Add Category")
            self.addbutton.clicked.connect(lambda: self.add_button_click("category"))
        else:
            print("Update")
            print(id)
            self.addbutton.setText("Update Category")
            self.addbutton.clicked.connect(lambda: self.update_button_click("category", id))

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(frame)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

        # self.setLayout(layout)

        self.setWindowTitle("Add Category Details")
        self.resize(430, 395)
        self.show()

        self.center()

    def center(self):
        '''centers the window on the screen'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def update_button_click(self, where, id):
        if where == "category":
            print("Tables Finally here")

            category_name = self.categorytextbox.text()

            if category_name != "":

                query = "update category set `category_name`=%s" \
                        "where id=%s;"
                values = (category_name, id)

                result = self.db.execute(query, values)

                self.closeEvent = self.message()

    def add_button_click(self, where):
        if where == "category":
            print("Category Finally here")

            category_name = self.categorytextbox.text()

            if category_name != "":

                query = "insert into category (`category_name`)" \
                        "values (%s);"
                values = (category_name,)

                result = self.db.execute(query, values)

                self.closeEvent = self.message()

    def message(self):
        self.closing.emit(1)
        self.close()

    # def closeEvent(self, event):
    #     print("Closed")
    #     self.closing.emit()
    #     # self.parent.update()