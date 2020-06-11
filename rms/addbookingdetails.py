from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QDateEdit, QComboBox, QTimeEdit)
from PyQt5.QtCore import (QRect, Qt, pyqtSignal)
from PyQt5.QtCore import (Qt, QDate)

import datetime

from classes2.db import DB


class AddBookingDetails(QMainWindow):

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
        # frame.setStyleSheet("border: none")

        add_booking_button = QLabel(frame)
        add_booking_button.setAlignment(Qt.AlignCenter)
        add_booking_button.setGeometry(QRect(110, 30, 210, 41))
        add_booking_button.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                 "background-color: rgb(30, 45, 66);\n"
                                 "color: rgb(255, 255, 255);")
        add_booking_button.setText("Add Reservation Details")

        # tablelabel = QLabel(frame)
        # tablelabel.setText("Table")
        # tablelabel.setGeometry(QRect(50, 120, 81, 20))
        #
        # tabletextbox = QComboBox(frame)
        # tabletextbox.setGeometry(QRect(170, 110, 181, 31))
        # tabletextbox.setFixedWidth(180)
        # tabletextbox.addItems(["Table 1", "Table 2"])

        customernamelabel = QLabel(frame)
        customernamelabel.setText("Customer Name")
        customernamelabel.setGeometry(QRect(50, 120, 100, 20))

        self.customernametextbox = QLineEdit(frame)
        self.customernametextbox.setGeometry(QRect(170, 110, 181, 31))
        self.customernametextbox.setFixedWidth(180)

        customercontactlabel = QLabel(frame)
        customercontactlabel.setText("Customer Contact")
        customercontactlabel.setGeometry(QRect(50, 160, 145, 19))

        self.customercontacttextbox = QLineEdit(frame)
        self.customercontacttextbox.setGeometry(QRect(170, 150, 181, 31))
        self.customercontacttextbox.setFixedWidth(180)

        datelabel = QLabel(frame)
        datelabel.setText("Date")
        datelabel.setGeometry(QRect(50, 200, 145, 19))

        self.datetextbox = QDateEdit(frame)
        self.datetextbox.setGeometry(QRect(170, 190, 181, 31))
        self.datetextbox.setFixedWidth(180)
        self.datetextbox.setDate(QDate.currentDate())
        self.datetextbox.setMinimumDate(QDate.currentDate())
        self.datetextbox.setDisplayFormat("dd-MM-yyyy")

        starttimelabel = QLabel(frame)
        starttimelabel.setText("Start Time")
        starttimelabel.setGeometry(QRect(50, 240, 121, 16))

        self.starttimetextbox = QTimeEdit(frame)
        self.starttimetextbox.setGeometry(QRect(170, 230, 181, 31))
        self.starttimetextbox.setFixedWidth(180)
        # self.starttimetextbox.setTime(QDate.currentDate())
        # self.starttimetextbox.setMinimumDate(QDate.currentDate())

        self.addbutton = QPushButton(frame)
        self.addbutton.setText("Add Booking")
        self.addbutton.setGeometry(QRect(160, 300, 151, 31))
        self.addbutton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(30, 45, 66);\n"
                                   "color: rgb(255, 255, 255);")
        # self.addbutton.clicked.connect(lambda: self.add_button_click("reservations"))

        if update == 'add':
            print("Add")
            print(id)
            self.addbutton.setText("Add Reservation")
            self.addbutton.clicked.connect(lambda: self.add_button_click("reservations"))
        else:
            print("Update")
            print(id)
            self.addbutton.setText("Update Reservation")
            self.addbutton.clicked.connect(lambda: self.update_button_click("reservations", id))

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(frame)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

        # self.setLayout(layout)

        self.setWindowTitle("Add Reservation Details")
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
        if where == "reservations":
            print("Tables Finally here")

            customer_name = self.customernametextbox.text()
            customer_contact = self.customercontacttextbox.text()
            start_time = self.starttimetextbox.text()

            try:
                date = datetime.datetime.strptime(self.datetextbox.text(), "%d-%m-%Y")
                booking_date = datetime.datetime.strftime(date, "%Y-%m-%d")
            except Exception as e:
                ''' Make sure to add an error message. '''
                print(e)
                return

            if customer_name != "" and customer_contact != "":

                query = "update customerBooking set `customer_name`=%s, " \
                        "`phone_number`=%s, `booking_date`=concat(%s, ' ', %s)" \
                        "where id=%s;"
                values = (customer_name, customer_contact, booking_date, start_time, id)

                result = self.db.execute(query, values)

                self.closeEvent = self.message()

    def add_button_click(self, where):
        if where == "reservations":
            print("Finally here")

            customer_name = self.customernametextbox.text()
            customer_contact = self.customercontacttextbox.text()
            start_time = self.starttimetextbox.text()

            try:
                date = datetime.datetime.strptime(self.datetextbox.text(), "%d-%m-%Y")
                booking_date = datetime.datetime.strftime(date, "%Y-%m-%d")
            except Exception as e:
                ''' Make sure to add an error message. '''
                print(e)
                return

            if customer_name != "" and customer_contact != "":

                print("Got Here")

                query = "insert into customerBooking (`customer_name`, `phone_number`, `booking_date`)" \
                        "values (%s, %s, concat(%s, ' ', %s));"
                values = (customer_name, customer_contact, booking_date, start_time)

                result = self.db.execute(query, values)

                self.closeEvent = self.message()

    def message(self):
        self.closing.emit(1)
        self.close()