from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QDateEdit, QComboBox)
from PyQt5.QtCore import (QRect, Qt, pyqtSignal)
from PyQt5.QtCore import (Qt, QDate)
from PyQt5.QtGui import (QIntValidator)

from classes2.db import DB

class AddTableDetails(QMainWindow):

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
        add_employee_button.setText("Add Table Details")

        tablenolabel = QLabel(frame)
        tablenolabel.setText("Table No.")
        tablenolabel.setGeometry(QRect(80, 170, 60, 13))

        self.tablenotextbox = QLineEdit(frame)
        self.tablenotextbox.setGeometry(QRect(170, 160, 181, 31))
        self.tablenotextbox.setFixedWidth(180)

        coverlabel = QLabel(frame)
        coverlabel.setText("Cover")
        coverlabel.setGeometry(QRect(80, 220, 47, 13))

        self.covertextbox = QLineEdit(frame)
        self.covertextbox.setGeometry(QRect(170, 210, 181, 31))
        self.covertextbox.setFixedWidth(180)
        self.covertextbox.setValidator(QIntValidator())

        self.addbutton = QPushButton(frame)
        self.addbutton.setGeometry(QRect(160, 300, 111, 31))
        self.addbutton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(30, 45, 66);\n"
                                   "color: rgb(255, 255, 255);")
        # self.addbutton.clicked.connect(lambda: self.add_button_click("tables"))

        if update == 'add':
            print("Add")
            print(id)
            self.addbutton.setText("Add Table")
            self.addbutton.clicked.connect(lambda: self.add_button_click("tables"))
        else:
            print("Update")
            print(id)
            self.addbutton.setText("Update Table")
            self.addbutton.clicked.connect(lambda: self.update_button_click("tables", id))

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(frame)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

        # self.setLayout(layout)

        self.setWindowTitle("Add Table Details")
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
        if where == "tables":
            print("Tables Finally here")

            table_number = self.tablenotextbox.text()
            covers = self.covertextbox.text()

            print(type(table_number))
            print(type(covers))

            print(table_number)
            print(covers)

            if table_number != "" and covers != "":

                query = "update tables set `table_number`=%s, `covers`=%s" \
                        "where id=%s;"
                values = (table_number, covers, id)

                result = self.db.execute(query, values)

                self.closeEvent = self.message()

    def add_button_click(self, where):
        if where == "tables":
            print("Tables Finally here")

            table_number = self.tablenotextbox.text()
            covers = self.covertextbox.text()

            print(type(table_number))
            print(type(covers))

            print(table_number)
            print(covers)

            if table_number != "" and covers != "":

                query = "insert into tables (`table_number`, `covers`)" \
                        "values (%s, %s);"
                values = (table_number, covers)

                result = self.db.execute(query, values)

                self.closeEvent = self.message()

    def message(self):
        self.closing.emit(1)
        self.close()