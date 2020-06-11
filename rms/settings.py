from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QTableWidget, QTableWidgetItem,
                             QCheckBox, QComboBox)
from PyQt5.QtCore import (QRect, Qt, pyqtSignal)
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import (QIntValidator)

from appname import AppName
# from sidebar import Sidebar
from footer import Footer
import sidebar

from addsearchframe import AddSearchFrame

from addemployeedetails import AddEmployeeDetails

from classes2.db import DB

import dashboard

class Settings(QMainWindow):


    def __init__(self, parent):
        super().__init__(parent)

        self.db = DB()

        self.initUI()

    def initUI(self):

        in_class = "settings"

        self.sidebar = sidebar.Sidebar(self)
        self.sidebar.window.connect(self.getvalue)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)

        header = AppName(in_class)
        footer = Footer()

        change_passwordbtn = QPushButton("Change Password")
        change_passwordbtn.setStyleSheet("background-color: rgb(30, 45, 66);\n"
                                               "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                               "color: rgb(255, 255, 255);")
        change_passwordbtn.setFixedWidth(170)
        change_passwordbtn.setFixedHeight(40)
        change_passwordbtn.clicked.connect(self.change_password)

        add_userbtn = QPushButton("Add User")
        add_userbtn.setStyleSheet("background-color: rgb(30, 45, 66);\n"
                               "font: 75 12pt \"MS Shell Dlg 2\";\n"
                               "color: rgb(255, 255, 255);")
        add_userbtn.setFixedWidth(170)
        add_userbtn.setFixedHeight(40)
        add_userbtn.clicked.connect(self.add_user)

        edit_restaurant_label = QLabel("Edit Restaurant Information")
        edit_restaurant_label.setStyleSheet("color: rgb(30, 45, 66);\n"
                                    "font: 75 20pt \"MS Shell Dlg 2\";")

        restaurantlabel = QLabel()
        restaurantlabel.setText("Name")
        restaurantlabel.setGeometry(QRect(80, 100, 47, 13))
        restaurantlabel.setFixedWidth(190)
        restaurantlabel.setFixedHeight(40)
        restaurantlabel.setStyleSheet(
            "color: rgb(30, 45, 66);\n"
            'font: 75 18pt "MS Shell Dlg 2";')


        self.restauranttextbox = QLineEdit()
        self.restauranttextbox.setGeometry(QRect(160, 90, 181, 31))
        self.restauranttextbox.setFixedWidth(280)
        self.restauranttextbox.setFixedHeight(40)

        addresslabel = QLabel()
        addresslabel.setText("Job Title")
        addresslabel.setGeometry(QRect(80, 140, 61, 16))
        addresslabel.setFixedWidth(190)
        addresslabel.setFixedHeight(40)
        addresslabel.setStyleSheet(
            "color: rgb(30, 45, 66);\n"
            'font: 75 18pt "MS Shell Dlg 2";')

        self.addresstextbox = QLineEdit()
        self.addresstextbox.setGeometry(QRect(160, 130, 181, 31))
        self.addresstextbox.setFixedWidth(280)
        self.addresstextbox.setFixedHeight(40)

        contact = QLabel()
        contact.setText("Salary")
        contact.setGeometry(QRect(80, 180, 47, 13))
        contact.setFixedWidth(190)
        contact.setFixedHeight(40)
        contact.setStyleSheet(
            "color: rgb(30, 45, 66);\n"
            'font: 75 18pt "MS Shell Dlg 2";')

        self.contacttextbox = QLineEdit()
        self.contacttextbox.setGeometry(QRect(160, 170, 181, 31))
        self.contacttextbox.setFixedWidth(280)
        self.contacttextbox.setFixedHeight(40)
        self.contacttextbox.setValidator(QIntValidator())

        update_btn = QPushButton("Update")
        update_btn.setGeometry(QRect(370, 500, 131, 41))
        update_btn.setStyleSheet("background-color: rgb(30, 45, 66);\n"
                                 "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 255, 255);")
        update_btn.setFixedWidth(130)
        update_btn.setFixedHeight(40)
        update_btn.clicked.connect(self.update_data)

        self.load_data()

        hlayout1 = QHBoxLayout()
        hlayout1.addStretch()
        hlayout1.addWidget(change_passwordbtn)
        hlayout1.addWidget(add_userbtn)
        hlayout1.addStretch()

        hlayout2 = QHBoxLayout()
        hlayout2.addStretch()
        hlayout2.addWidget(edit_restaurant_label)
        hlayout2.addStretch()

        hlayout3 = QHBoxLayout()
        hlayout3.addStretch()
        hlayout3.addWidget(restaurantlabel)
        hlayout3.addWidget(self.restauranttextbox)
        hlayout3.addStretch()

        hlayout4 = QHBoxLayout()
        hlayout4.addStretch()
        hlayout4.addWidget(addresslabel)
        hlayout4.addWidget(self.addresstextbox)
        hlayout4.addStretch()

        hlayout5 = QHBoxLayout()
        hlayout5.addStretch()
        hlayout5.addWidget(contact)
        hlayout5.addWidget(self.contacttextbox)
        hlayout5.addStretch()

        hlayout6 = QHBoxLayout()
        hlayout6.addStretch()
        hlayout6.addWidget(update_btn)
        hlayout6.addStretch()

        layout = QVBoxLayout()

        layout.addWidget(header)
        layout.addLayout(hlayout1)
        layout.addStretch()
        layout.addLayout(hlayout2)
        layout.addLayout(hlayout3)
        layout.addLayout(hlayout4)
        layout.addLayout(hlayout5)
        layout.addLayout(hlayout6)
        layout.addStretch()
        layout.addStretch()
        layout.addWidget(footer)

        layout.setContentsMargins(0, 0, 0, 0)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)
        self.setContentsMargins(0, 0, 0, 0)

        self.setWindowTitle("Settings")
        self.resize(1160, 605)

        self.show()
        self.center()

    def center(self):
        '''centers the window on the screen'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def getvalue(self, value):
        print(value)
        print(type(value))

        if value == 1:
            self.hide()
            view = sidebar.Dashboard(self)
        elif value == 2:
            self.hide()
            view = sidebar.Employee(self)
        elif value == 3:
            self.hide()
            view = sidebar.Table(self)
        elif value == 4:
            self.hide()
            view = sidebar.Reservations(self)
        elif value == 5:
            self.hide()
            view = sidebar.Category(self)
        elif value == 6:
            pass
        elif value == 7:
            self.hide()
            view = sidebar.Orders(self)
        elif value == 8:
            self.hide()
            view = sidebar.Menu(self)

    def change_password(self):
        view = ChangePassword(self)

    def add_user(self):
        print("Add user here")

        view = AddUser(self)
        # view.closing.connect(self.update_setting)

    '''
        Repopulates the employee table with the updated data.
    '''
    def update_setting(self, check):
        print("I am here")
        print(check)

        # data = self.add_update_emp_data()
        #
        # self.populate_table(data)

    def load_data(self):
        print("Got here.")

        query = "SELECT restaurant_name, address, contact FROM rest_info;"
        values = ()

        result = self.db.fetch(query, values)

        for (restaurant_name, address, contact) in result:
            self.restauranttextbox.setText(restaurant_name)
            self.addresstextbox.setText(address)
            self.contacttextbox.setText(contact)

    def update_data(self):
        print("Updated " + self.restauranttextbox.text())
        print("Updated " + self.addresstextbox.text())
        print("Updated " + self.contacttextbox.text())

        '''
            To do..
            Update the restaurant information in the database with the given values. 
        '''
        query = "update rest_info set restaurant_name=%s, address=%s, contact=%s"
        values = (self.restauranttextbox.text(), self.addresstextbox.text(), self.contacttextbox.text())

        result = self.db.execute(query, values)


'''
    ChangePassword class to popup when the button is clicked.
'''
class ChangePassword(QMainWindow):

    def __init__(self, parent):
        super().__init__(parent)

        self.db = DB()

        self.initUI()

    def initUI(self):

        self.setWindowModality(Qt.ApplicationModal)

        frame = QFrame()
        # frame.setStyleSheet("background-color: rgb(30, 45, 66);")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        # frame.setFixedWidth(200)
        # frame.setFixedHeight(150)

        main_label = QLabel(frame)
        main_label.setAlignment(Qt.AlignCenter)
        main_label.setGeometry(QRect(120, 40, 211, 41))
        main_label.setStyleSheet("background-color: rgb(30, 45, 66);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 75 14pt \"MS Shell Dlg 2\";")
        main_label.setText("Change Password")

        old_passwordlabel = QLabel(frame)
        old_passwordlabel.setText("Old Password")
        old_passwordlabel.setGeometry(QRect(50, 140, 101, 41))
        old_passwordlabel.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(30, 45, 66);")

        self.old_passwordtextbox = QLineEdit(frame)
        self.old_passwordtextbox.setGeometry(QRect(180, 140, 191, 41))

        new_passwordlabel = QLabel(frame)
        new_passwordlabel.setText("New Password")
        new_passwordlabel.setGeometry(QRect(50, 190, 101, 41))
        new_passwordlabel.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(30, 45, 66);")

        self.new_passwordtextbox = QLineEdit(frame)
        self.new_passwordtextbox.setGeometry(QRect(180, 190, 191, 41))

        self.error_msg = QLabel(frame)
        self.error_msg.setText("")
        self.error_msg.setGeometry(QRect(170, 250, 121, 41))
        self.error_msg.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(30, 45, 66);")

        submit_btn = QPushButton(frame)
        submit_btn.setText("Submit")
        submit_btn.setGeometry(QRect(170, 310, 111, 31))
        submit_btn.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(30, 45, 66);\n"
                                 "color: rgb(255, 255, 255);")
        submit_btn.clicked.connect(self.update_password)

        layout = QVBoxLayout()
        layout.addWidget(frame)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)
        self.setWindowTitle("Change Password")
        self.resize(430, 395)
        self.show()

        self.center()

    def center(self):
        '''centers the window on the screen'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def update_password(self):
        print("Update password")

        '''
            1. Check which user is logged in.
            2. Change the password of the logged in user.
        '''

        old_password = self.old_passwordtextbox.text()
        new_password = self.new_passwordtextbox.text()

        if old_password != '' and new_password != '':
            query = "select admin_name, password from admin where logged_in='yes'"
            values = ()

            data = self.db.fetch(query, values)

            for (admin_name, password) in data:
                match_password = password

            if match_password == old_password:
                query = "update admin set password=%s where logged_in='yes'"
                values = (new_password,)

                data = self.db.execute(query, values)

                self.error_msg.setText("Password updated")

            else:
                '''
                    Update the label here with the error message.
                '''

                self.error_msg.setText("Password Wrong")


class AddUser(QMainWindow):

    closing = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)

        self.db = DB()

        self.initUI()

    def initUI(self):

        self.setWindowModality(Qt.ApplicationModal)

        frame = QFrame()
        # frame.setStyleSheet("background-color: rgb(30, 45, 66);")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        # frame.setFixedWidth(200)
        # frame.setFixedHeight(150)

        main_label = QLabel(frame)
        main_label.setAlignment(Qt.AlignCenter)
        main_label.setGeometry(QRect(120, 40, 211, 41))
        main_label.setStyleSheet("background-color: rgb(30, 45, 66);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 75 14pt \"MS Shell Dlg 2\";")
        main_label.setText("Add User Privileges")

        user_label = QLabel(frame)
        user_label.setText("User")
        user_label.setGeometry(QRect(50, 100, 101, 41))
        user_label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(30, 45, 66);")

        getuserlist = self.get_all_user()

        self.user_list = QComboBox(frame)
        self.user_list.addItems(getuserlist)
        self.user_list.setGeometry(QRect(180, 100, 191, 46))

        user_name = QLabel(frame)
        user_name.setText("Add Username")
        user_name.setGeometry(QRect(50, 140, 101, 41))
        user_name.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(30, 45, 66);")

        self.username = QLineEdit(frame)
        self.username.setGeometry(QRect(180, 140, 191, 35))

        user_password = QLabel(frame)
        user_password.setText("Add Password")
        user_password.setGeometry(QRect(50, 180, 101, 41))
        user_password.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(30, 45, 66);")

        self.password = QLineEdit(frame)
        self.password.setGeometry(QRect(180, 180, 191, 35))


        privileges = QLabel(frame)
        privileges.setText("Privileges")
        privileges.setGeometry(QRect(50, 210, 101, 41))
        privileges.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(30, 45, 66);")

        self.option_1 = QCheckBox(frame)
        self.option_1.setText("Dashboard")
        self.option_1.setGeometry(QRect(180, 210, 101, 41))
        self.option_1.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(30, 45, 66);")

        self.option_2 = QCheckBox(frame)
        self.option_2.setText("Employees")
        self.option_2.setGeometry(QRect(280, 210, 101, 41))
        self.option_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                               "color: rgb(30, 45, 66);")

        self.option_3 = QCheckBox(frame)
        self.option_3.setText("Bill")
        self.option_3.setGeometry(QRect(180, 235, 101, 41))
        self.option_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                               "color: rgb(30, 45, 66);")

        self.option_4 = QCheckBox(frame)
        self.option_4.setText("Tables")
        self.option_4.setGeometry(QRect(280, 235, 101, 41))
        self.option_4.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                               "color: rgb(30, 45, 66);")

        self.option_5 = QCheckBox(frame)
        self.option_5.setText("Reservations")
        self.option_5.setGeometry(QRect(180, 260, 101, 41))
        self.option_5.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                               "color: rgb(30, 45, 66);")

        self.option_6 = QCheckBox(frame)
        self.option_6.setText("Category")
        self.option_6.setGeometry(QRect(280, 260, 101, 41))
        self.option_6.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                               "color: rgb(30, 45, 66);")

        self.option_7 = QCheckBox(frame)
        self.option_7.setText("Orders")
        self.option_7.setGeometry(QRect(180, 285, 101, 41))
        self.option_7.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                               "color: rgb(30, 45, 66);")

        self.option_8 = QCheckBox(frame)
        self.option_8.setText("Settings")
        self.option_8.setGeometry(QRect(280, 285, 101, 41))
        self.option_8.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                               "color: rgb(30, 45, 66);")

        self.option_9 = QCheckBox(frame)
        self.option_9.setText("Menu")
        self.option_9.setGeometry(QRect(180, 310, 101, 41))
        self.option_9.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(30, 45, 66);")

        self.option_10 = QCheckBox(frame)
        self.option_10.setText("Users")
        self.option_10.setGeometry(QRect(280, 310, 101, 41))
        self.option_10.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(30, 45, 66);")

        submit_btn = QPushButton(frame)
        submit_btn.setText("Submit")
        submit_btn.setGeometry(QRect(170, 360, 111, 31))
        submit_btn.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(30, 45, 66);\n"
                                 "color: rgb(255, 255, 255);")
        submit_btn.clicked.connect(self.add_privileges)

        layout = QVBoxLayout()
        layout.addWidget(frame)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)
        self.setWindowTitle("Add User Privileges")
        self.resize(430, 450)
        self.show()

        self.center()

    def center(self):
        ''' centers the window on the screen'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def add_privileges(self):
        print("List the selected privileges.")

        selected_privileges = []

        if self.option_1.isChecked():
            selected_privileges.append(self.option_1.text())

        if self.option_2.isChecked():
            selected_privileges.append(self.option_2.text())

        if self.option_3.isChecked():
            selected_privileges.append(self.option_3.text())

        if self.option_4.isChecked():
            selected_privileges.append(self.option_4.text())

        if self.option_5.isChecked():
            selected_privileges.append(self.option_5.text())

        if self.option_6.isChecked():
            selected_privileges.append(self.option_6.text())

        if self.option_7.isChecked():
            selected_privileges.append(self.option_7.text())

        if self.option_8.isChecked():
            selected_privileges.append(self.option_8.text())

        print(self.user_list.currentText())
        print(self.username.text())
        print(self.password.text())
        print(selected_privileges)

        '''
            All ready here.. Add the query to the database.
        '''
        query = "insert into admin (admin_name, password, roles) " \
                "values (%s, %s, %s)"
        values = (self.username.text(), self.password.text(), ', '.join(selected_privileges))

        data = self.db.execute(query, values)

        self.closeEvent = self.message()

    def message(self):
        # self.closing.emit(1)
        self.close()



    def get_all_user(self):
        query = "select employee_name, job_title from employee"
        values = ()

        data = self.db.fetch(query, values)

        list = []

        for (employee_name, job_title) in data:
            print(employee_name + " (" + job_title + ")")
            list.append(employee_name + " (" + job_title + ")")

        return list
