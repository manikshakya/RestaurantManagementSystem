from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton)
from PyQt5.QtCore import (QRect, Qt)
from PyQt5.QtCore import Qt

from appname import AppName
# from sidebar import Sidebar
from footer import Footer
import sidebar
import functools


from employee import Employee       #  Done
from reservations import Reservations
from category import Category       # Done
from tables import Table            # Done
from settings import Settings # Almost Done
from orders import Orders
from menu import Menu
from bill import Bill
from users import Users

from classes2.db import DB


class Dashboard(QMainWindow):

    def __init__(self, parent):  # Add parent as a argument
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.sidebar = sidebar.Sidebar(self)
        self.sidebar.window.connect(self.getvalue)

        print("Dashboard")
        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)

        header = AppName("dashboard")
        footer = Footer()

        statslabel = QLabel("Statistics")
        statslabel.setStyleSheet("color: rgb(30, 45, 66);" 'font: 75 16pt "MS Shell Dlg 2";')
        statslabel.setContentsMargins(20, 15, 0, 0)

        statistics = QHBoxLayout()

        dashboardsales = DashboardSales()
        dashboardorders = DashboardOrders()
        # dashboardprofits = DashboardProfits()

        statistics.addStretch()
        statistics.addWidget(dashboardsales)
        statistics.addStretch()
        statistics.addWidget(dashboardorders)
        statistics.addStretch()
        # statistics.addWidget(dashboardprofits)
        # statistics.addStretch()

        restaurantlabel = QLabel("Restaurant")
        restaurantlabel.setStyleSheet("color: rgb(30, 45, 66);" 'font: 75 16pt "MS Shell Dlg 2";')
        restaurantlabel.setContentsMargins(20, 0, 0, 0)

        restaurantdetails = RestaurantDetails()

        layout = QVBoxLayout()

        layout.addWidget(header)
        layout.addWidget(statslabel)
        layout.addWidget(HLine())
        layout.addLayout(statistics)
        layout.addWidget(HLine())
        layout.addWidget(restaurantlabel)
        layout.addWidget(HLine())
        layout.addWidget(restaurantdetails)
        layout.addStretch()
        layout.addWidget(footer)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        print("hello")

        self.setCentralWidget(centralWidget)
        self.setContentsMargins(0, 0, 0, 0)

        self.resize(1160, 605)
        self.setWindowTitle("Login")

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
            pass
        elif value == 2:
            self.hide()
            view = Employee(self)
        elif value == 3:
            self.hide()
            view = Table(self)
        elif value == 4:
            self.hide()
            view = Reservations(self)
        elif value == 5:
            self.hide()
            view = Category(self)
        elif value == 6:
            self.hide()
            view = Settings(self)
        elif value == 7:
            self.hide()
            view = Orders(self)
        elif value == 8:
            self.hide()
            view = Menu(self)
        elif value == 9:
            self.hide()
            view = Bill(self)


class DashboardSales(QFrame):

    def __init__(self):
        super().__init__()

        self.db = DB()

        self.initUI()

    def initUI(self):
        frame = QFrame()
        frame.setStyleSheet("background-color: rgb(30, 45, 66);")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setFixedWidth(200)
        frame.setFixedHeight(150)

        main_label = QLabel(frame)
        main_label.setAlignment(Qt.AlignCenter)
        main_label.setGeometry(QRect(40, 10, 120, 41))
        main_label.setStyleSheet("font: 75 28pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 36pt \"MS Shell Dlg 2\";")
        main_label.setText("Sales")

        total_sales = self.get_total_sales()

        sales = QLabel(frame)
        sales.setAlignment(Qt.AlignCenter)
        sales.setGeometry(QRect(40, 60, 120, 41))
        sales.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
                            "color: rgb(255, 255, 255);\n"
                            "font: 20pt \"MS Shell Dlg 2\";")
        sales.setText(str(total_sales))

        layout = QVBoxLayout()
        layout.addWidget(frame)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)
        # self.setGeometry(QRect(30, 5, 200, 150))

    def get_total_sales(self):
        query = "select sum(cast(total_price as decimal(5, 2))) as sales from orders;"
        values = ()

        ressult =  self.db.fetch(query, values)

        for (sales) in ressult:
            sales = sales[0]

        return sales


class DashboardOrders(QFrame):

    def __init__(self):
        super().__init__()

        self.db = DB()

        self.initUI()

    def initUI(self):
        frame = QFrame()
        frame.setStyleSheet("background-color: rgb(30, 45, 66);")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setFixedWidth(200)
        frame.setFixedHeight(150)

        main_label = QLabel(frame)
        main_label.setAlignment(Qt.AlignCenter)
        main_label.setGeometry(QRect(40, 10, 120, 41))
        main_label.setStyleSheet("font: 75 28pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 36pt \"MS Shell Dlg 2\";")
        main_label.setText("Orders")

        data = self.get_orders()

        sales = QLabel(frame)
        sales.setAlignment(Qt.AlignCenter)
        sales.setGeometry(QRect(40, 60, 120, 41))
        sales.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
                            "color: rgb(255, 255, 255);\n"
                            "font: 20pt \"MS Shell Dlg 2\";")
        sales.setText(str(data))

        layout = QVBoxLayout()
        layout.addWidget(frame)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)
        self.setGeometry(QRect(30, 5, 200, 150))

    def get_orders(self):
        query = "select id from orders;"
        values = ()

        result = self.db.fetch(query, values)

        for (sales) in result:
            sales = sales[0]

        print("Rows")
        print(len(result))

        return len(result)


class DashboardProfits(QFrame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        frame = QFrame()
        frame.setStyleSheet("background-color: rgb(30, 45, 66);")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setFixedWidth(200)
        frame.setFixedHeight(150)

        main_label = QLabel(frame)
        main_label.setAlignment(Qt.AlignCenter)
        main_label.setGeometry(QRect(40, 10, 120, 41))
        main_label.setStyleSheet("font: 75 28pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 36pt \"MS Shell Dlg 2\";")
        main_label.setText("Profits")

        layout = QVBoxLayout()
        layout.addWidget(frame)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)
        self.setGeometry(QRect(30, 5, 200, 150))


class RestaurantDetails(QFrame):

    def __init__(self):
        super().__init__()

        self.db = DB()

        self.initUI()

    def initUI(self):
        frame = QFrame()
        # frame.setStyleSheet("background-color: rgb(30, 45, 66);")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setMinimumWidth(200)
        frame.setFixedHeight(150)
        frame.setStyleSheet("border: none")

        details = self.get_restaurant_details()

        restname = QLabel(frame)
        # restname.setAlignment(Qt.AlignCenter)
        restname.setGeometry(QRect(100, 0, 300, 41))
        restname.setStyleSheet("color: rgb(30, 45, 66);" 'font: 75 16pt "MS Shell Dlg 2";')
        restname.setText(details[0])

        address = QLabel(frame)
        # address.setAlignment(Qt.AlignCenter)
        address.setGeometry(QRect(100, 40, 300, 41))
        address.setStyleSheet("color: rgb(30, 45, 66);" 'font: 75 16pt "MS Shell Dlg 2";')
        address.setText(details[1])

        number = QLabel(frame)
        # number.setAlignment(Qt.AlignCenter)
        number.setGeometry(QRect(100, 80, 300, 41))
        number.setStyleSheet("color: rgb(30, 45, 66);" 'font: 75 16pt "MS Shell Dlg 2";')
        number.setText(details[2])

        layout = QVBoxLayout()
        layout.addWidget(frame)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)
        # self.setGeometry(QRect(30, 5, 200, 150))

        # self.setStyleSheet("border: none")

    def get_restaurant_details(self):
        query = "select restaurant_name, address, contact from rest_info"
        values = ()

        data = self.db.fetch(query, values)

        for (restaurant_name, address, contact) in data:
            restaurant_name = restaurant_name
            address = address
            contact = contact

        return [restaurant_name, address, contact]


class HLine(QFrame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)

        self.setMinimumHeight(20)
