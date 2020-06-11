from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QDockWidget)
from PyQt5.QtCore import (QRect, Qt, pyqtSignal)
from PyQt5.QtCore import Qt
import functools

from dashboard import Dashboard
from dashboard import Employee
from dashboard import Settings
from dashboard import Reservations
from dashboard import Category
from dashboard import Table
from dashboard import Orders
from dashboard import Menu
from dashboard import Bill
from dashboard import Users

from logout import Logout


from classes2.db import DB

import login

"""
    1. Dashboard
    2. Employees
    3. Stocks
    4. Tables
    5. Reservations
    6. Orders
    7. Members
    8. Settings -- Change Password, Add User (Make sure to match the added user with the employee table)
    9. Logout
"""

"""
    1. Create user priveleges
    2. Change passwords, Update restaurant Information (Settings tab) -- Almost done.. Need to put the query.
    3. Add Category                                 -- All done except Edit
    4. Reservations Add/Delete/Search features      -- All done except Edit
    5. Table Add/Delete features                    -- All done except Edit
    6. Order section. List all the menu items. Select food and add it to the bill.

"""


class Sidebar(QDockWidget):

    window = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)

        self.db = DB()

        self.initUI(parent)

    def initUI(self, parent):

        frame = QFrame()

        label1 = QLabel("Dashboard", frame)
        # label1.setStyleSheet("border: 3px solid red; text-align: center;")
        label1.setAlignment(Qt.AlignCenter)
        label1.setMinimumHeight(50)
        label1.setObjectName("Dashboard")
        label1.setMouseTracking(True)
        label1.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label1, parent])
        label1.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label1)
        label1.leaveEvent = functools.partial(self.tabsleft, source_object=label1)
        # label1.setFixedHeight(50)

        label2 = QLabel("Employees", frame)
        label2.setAlignment(Qt.AlignCenter)
        label2.setMinimumHeight(50)
        label2.setObjectName("Employees")
        label2.setMouseTracking(True)
        label2.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label2, parent])
        label2.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label2)
        label2.leaveEvent = functools.partial(self.tabsleft, source_object=label2)

        label3 = QLabel("Users", frame)
        label3.setAlignment(Qt.AlignCenter)
        label3.setMinimumHeight(50)
        label3.setObjectName("Users")
        label3.setMouseTracking(True)
        label3.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label3, parent])
        label3.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label3)
        label3.leaveEvent = functools.partial(self.tabsleft, source_object=label3)

        label4 = QLabel("Tables", frame)
        label4.setAlignment(Qt.AlignCenter)
        label4.setMinimumHeight(50)
        label4.setObjectName("Tables")
        label4.setMouseTracking(True)
        label4.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label4, parent])
        label4.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label4)
        label4.leaveEvent = functools.partial(self.tabsleft, source_object=label4)

        label5 = QLabel("Reservations", frame)
        label5.setAlignment(Qt.AlignCenter)
        label5.setMinimumHeight(50)
        label5.setObjectName("Reservations")
        label5.setMouseTracking(True)
        label5.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label5, parent])
        label5.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label5)
        label5.leaveEvent = functools.partial(self.tabsleft, source_object=label5)

        label6 = QLabel("Orders", frame)
        label6.setAlignment(Qt.AlignCenter)
        label6.setMinimumHeight(50)
        label6.setObjectName("Orders")
        label6.setMouseTracking(True)
        label6.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label6, parent])
        label6.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label6)
        label6.leaveEvent = functools.partial(self.tabsleft, source_object=label6)

        label7 = QLabel("Bill", frame)
        label7.setAlignment(Qt.AlignCenter)
        label7.setMinimumHeight(50)
        label7.setObjectName("Bill")
        label7.setMouseTracking(True)
        label7.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label7, parent])
        label7.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label7)
        label7.leaveEvent = functools.partial(self.tabsleft, source_object=label7)

        label8 = QLabel("Settings", frame)
        label8.setAlignment(Qt.AlignCenter)
        label8.setMinimumHeight(50)
        label8.setObjectName("Settings")
        label8.setMouseTracking(True)
        label8.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label8, parent])
        label8.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label8)
        label8.leaveEvent = functools.partial(self.tabsleft, source_object=label8)

        label9 = QLabel("Logout", frame)
        label9.setAlignment(Qt.AlignCenter)
        label9.setMinimumHeight(50)
        label9.setObjectName("Logout")
        label9.setMouseTracking(True)
        label9.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label9, parent])
        label9.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label9)
        label9.leaveEvent = functools.partial(self.tabsleft, source_object=label9)

        label10 = QLabel("Category", frame)
        label10.setAlignment(Qt.AlignCenter)
        label10.setMinimumHeight(50)
        label10.setObjectName("Category")
        label10.setMouseTracking(True)
        label10.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label10, parent])
        label10.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label10)
        label10.leaveEvent = functools.partial(self.tabsleft, source_object=label10)

        label11 = QLabel("Menu", frame)
        label11.setAlignment(Qt.AlignCenter)
        label11.setMinimumHeight(50)
        label11.setObjectName("Menu")
        label11.setMouseTracking(True)
        label11.mousePressEvent = functools.partial(self.tabsClicked, source_object=[label11, parent])
        label11.mouseMoveEvent = functools.partial(self.tabsHovered, source_object=label11)
        label11.leaveEvent = functools.partial(self.tabsleft, source_object=label11)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        privileges = self.get_privileges()

        list_privileges = privileges.split(", ")

        print("All the Privileges")
        print(list_privileges)
        for x in list_privileges:
            if x == 'Dashboard':
                layout.addWidget(label1, 0)
            if x == 'Employees':
                layout.addWidget(label2, 0)
            if x == 'Users':
                layout.addWidget(label3, 0)
            if x == 'Tables':
                layout.addWidget(label4, 0)
            if x == 'Reservations':
                layout.addWidget(label5, 0)
            if x == 'Category':
                layout.addWidget(label10, 0)
            if x == 'Menu':
                layout.addWidget(label11, 0)
            if x == 'Orders':
                layout.addWidget(label6, 0)
            if x == 'Bill':
                layout.addWidget(label7, 0)
            if x == 'Settings':
                layout.addWidget(label8, 0)

        layout.addWidget(label9, 0)

        # self.setLayout(layout) # when extending QFrame

        ''' Removes the title bar from the DockWidget. '''
        self.setTitleBarWidget(QWidget(None))

        ''' 
            Make the DockWidget non-resizable.
            Set the minimum & maximum width/height value equal to same amount. 
        '''
        self.setMinimumWidth(200)
        self.setMaximumWidth(200)

        ''' Removes the close button from the DockWidget '''
        # self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.setFeatures(self.NoDockWidgetFeatures)

        self.setStyleSheet("background-color: rgb(30, 45, 66); color: white; border-width: 0px; ")
        self.setContentsMargins(0, 0, 0, 0)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setWidget(centralWidget)

        # self.setWindowTitle("Test")
        self.show()

    def get_privileges(self):
        list = ""

        query = "SELECT roles FROM admin where logged_in='yes' " \
                "order by id desc limit 1;"

        result = self.db.fetch(query)

        for (roles) in result:
            list = roles[0]

        print(list)

        return list

    def tabsClicked(self, event, source_object=None):
        print("Clicked, from: ", source_object[0].objectName())

        tab = source_object[0].objectName()

        if tab == "Dashboard":
            # self.window.emit(1)
            source_object[1].hide()
            view = Dashboard(source_object[1])
        elif tab == "Employees":
            # self.window.emit(2)
            source_object[1].hide()
            view = Employee(source_object[1])

        elif tab == "Users":
            source_object[1].hide()
            view = Users(source_object[1])
        elif tab == "Tables":
            # self.window.emit(3)
            source_object[1].hide()
            view = Table(source_object[1])
        elif tab == "Reservations":
            # self.window.emit(4)
            source_object[1].hide()
            view = Reservations(source_object[1])
        elif tab == "Category":
            # self.window.emit(5)
            source_object[1].hide()
            view = Category(source_object[1])
        elif tab == "Menu":
            # self.window.emit(8)
            source_object[1].hide()
            view = Menu(source_object[1])
        elif tab == "Orders":
            # self.window.emit(7)
            source_object[1].hide()
            view = Orders(source_object[1])
        elif tab == "Bill":
            # self.window.emit(9)
            source_object[1].hide()
            view = Bill(source_object[1])
        elif tab == "Settings":
            # self.window.emit(6)
            source_object[1].hide()
            view = Settings(source_object[1])
        elif tab == "Logout":
            query = "update admin set logged_in='no' where logged_in='yes'"
            values = ()

            data = self.db.execute(query, values)

            source_object[1].hide()
            view = Logout(source_object[1])


    def tabsHovered(self, event, source_object= None):
        source_object.setStyleSheet("background-color: white; color: black")

    def tabsleft(self, event, source_object= None):
        source_object.setStyleSheet("background-color: rgb(30, 45, 66); color: white")

