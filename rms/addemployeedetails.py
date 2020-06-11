from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QDateEdit, QComboBox)
from PyQt5.QtCore import (QRect, Qt, QDate, pyqtSignal)
from PyQt5.QtGui import (QIntValidator)

from classes2.db import DB

import datetime


class AddEmployeeDetails(QMainWindow):

    closing = pyqtSignal(int)

    def __init__(self, parent, update, id=None):
        super().__init__(parent)

        self.parent = parent

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
        add_employee_button.setText("Add Employee Details")

        # name = QHBoxLayout()
        # jobtitle = QHBoxLayout()
        # salary = QHBoxLayout()
        # bonus = QHBoxLayout()
        # joindate = QHBoxLayout()

        namelabel = QLabel(frame)
        namelabel.setText("Name")
        namelabel.setGeometry(QRect(80, 100, 47, 13))

        self.nametextbox = QLineEdit(frame)
        self.nametextbox.setGeometry(QRect(160, 90, 181, 31))
        self.nametextbox.setFixedWidth(180)

        jobtitlelabel = QLabel(frame)
        jobtitlelabel.setText("Job Title")
        jobtitlelabel.setGeometry(QRect(80, 140, 61, 16))

        self.jobtitletextbox = QComboBox(frame)
        self.jobtitletextbox.setGeometry(QRect(160, 130, 181, 31))
        self.jobtitletextbox.setFixedWidth(180)
        self.jobtitletextbox.addItems(["Manager", "Waiter", "Chef", "Security"])

        salarylabel = QLabel(frame)
        salarylabel.setText("Salary")
        salarylabel.setGeometry(QRect(80, 180, 47, 13))

        self.salarytextbox = QLineEdit(frame)
        self.salarytextbox.setGeometry(QRect(160, 170, 181, 31))
        self.salarytextbox.setFixedWidth(180)
        self.salarytextbox.setValidator(QIntValidator())

        # bonuslabel = QLabel(frame)
        # bonuslabel.setText("Bonus")
        # bonuslabel.setGeometry(QRect(80, 220, 47, 13))

        # bonustextbox = QLineEdit(frame)
        # bonustextbox.setGeometry(QRect(160, 210, 181, 31))
        # bonustextbox.setFixedWidth(180)

        joindatelabel = QLabel(frame)
        joindatelabel.setText("Start Date")
        joindatelabel.setGeometry(QRect(80, 260, 71, 16))

        self.joindatetextbox = QDateEdit(frame)
        self.joindatetextbox.setGeometry(QRect(160, 250, 181, 31))
        self.joindatetextbox.setFixedWidth(180)
        self.joindatetextbox.setDate(QDate.currentDate())
        self.joindatetextbox.setMinimumDate(QDate.currentDate())
        self.joindatetextbox.setDisplayFormat("dd-MM-yyyy")

        self.addbutton = QPushButton(frame)
        self.addbutton.setGeometry(QRect(160, 300, 111, 31))
        self.addbutton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(30, 45, 66);\n"
                                   "color: rgb(255, 255, 255);")
        if update == 'add':
            print("Add")
            print(id)
            self.addbutton.setText("Add Employee")
            self.addbutton.clicked.connect(lambda: self.add_button_click("employee"))
        else:
            print("Update")
            print(id)
            self.addbutton.setText("Update Employee")
            self.addbutton.clicked.connect(lambda: self.update_button_click("employee", id))

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(frame)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

        # self.setLayout(layout)

        self.setWindowTitle("Add Employee Details")
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
        if where == "employee":
            print("Employees Finally here")

            print(self.nametextbox.text())
            print(self.jobtitletextbox.currentText())
            print(self.salarytextbox.text())
            print(self.joindatetextbox.text())

            employee_name = self.nametextbox.text()
            job_title = self.jobtitletextbox.currentText()
            salary = self.salarytextbox.text()

            try:
                date = datetime.datetime.strptime(self.joindatetextbox.text(), "%d-%m-%Y")
                joining_date = datetime.datetime.strftime(date, "%Y-%m-%d")
            except:
                ''' Make sure to add an error message. '''
                return

            if employee_name != "" and salary != "":
                query = "update employee set `employee_name`=%s, `job_title`=%s, `salary`=%s, " \
                        "`joining_date`=%s where id=%s"
                values = (employee_name, job_title, salary, joining_date, id)

                result = self.db.execute(query, values)

                self.closeEvent = self.message()

    def add_button_click(self, where):
        if where == "employee":
            print("Employees Finally here")

            print(self.nametextbox.text())
            print(self.jobtitletextbox.currentText())
            print(self.salarytextbox.text())
            print(self.joindatetextbox.text())

            employee_name = self.nametextbox.text()
            job_title = self.jobtitletextbox.currentText()
            salary = self.salarytextbox.text()

            try:
                date = datetime.datetime.strptime(self.joindatetextbox.text(), "%d-%m-%Y")
                joining_date = datetime.datetime.strftime(date, "%Y-%m-%d")
            except:
                ''' Make sure to add an error message. '''
                return

            if employee_name != "" and salary != "":
                query = "insert into employee (`employee_name`, `job_title`,`salary`, `joining_date`)" \
                        "values (%s, %s, %s, %s);"
                values = (employee_name, job_title, salary, joining_date)

                result = self.db.execute(query, values)

                self.closeEvent = self.message()

    def message(self):
        self.closing.emit(1)
        self.close()

    # def closeEvent(self, event):
    #     print("Closed")
    #     self.closing.emit()
    #     # self.parent.update()