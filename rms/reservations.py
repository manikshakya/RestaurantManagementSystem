from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import (QRect, Qt, QDate, QTime)
from PyQt5.QtCore import Qt

from appname import AppName
# from sidebar import Sidebar
from footer import Footer
from addsearchframe import AddSearchFrame
import sidebar

from addbookingdetails import AddBookingDetails

from classes2.db import DB


import dashboard




class Reservations(QMainWindow):

    def __init__(self, parent):
        super().__init__(parent)

        self.db = DB()

        self.initUI()

    def initUI(self):
        in_class = "reservations"

        self.sidebar = sidebar.Sidebar(self)
        self.sidebar.window.connect(self.getvalue)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)

        header = AppName(in_class)
        footer = Footer()

        add_and_search = AddSearchFrame(in_class)
        add_and_search.add_button.clicked.connect(lambda: self.add_reservation(in_class))
        add_and_search.search_button.clicked.connect(lambda: self.search_reservation(add_and_search.search_box))


        self.table = QTableWidget()
        self.table.setColumnCount(6)
        # self.table.setStyleSheet("border: none")
        # self.table.setStyleSheet(
        #     "background-color: rgb(255, 255, 255);\n"
        #     'font: 10pt "MS Shell Dlg 2";\n'
        #     "color: rgb(30, 45, 66);"
        # )

        # self.table.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Customer Name"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Phone No."))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Date"))
        # self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Bonus"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Time"))
        # self.table.setHorizontalHeaderItem(6, QTableWidgetItem("Total Salary"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("Edit"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("Delete"))

        data = self.load_reservation_data()
        print(data)

        for x in data:
            print(x)

        self.populate_table(data)

        layout = QVBoxLayout()

        layout.addWidget(header)
        layout.addWidget(add_and_search)
        layout.addWidget(self.table)
        # layout.addStretch()
        layout.addWidget(footer)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)
        self.setContentsMargins(0, 0, 0, 0)

        # self.resize(800, 600)
        self.setWindowTitle("Login")
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
            pass
        elif value == 5:
            self.hide()
            view = sidebar.Category(self)
        elif value == 6:
            self.hide()
            view = sidebar.Settings(self)
        elif value == 7:
            self.hide()
            view = sidebar.Orders(self)
        elif value == 8:
            self.hide()
            view = sidebar.Menu(self)
        elif value == 9:
            self.hide()
            view = sidebar.Bill(self)

    def load_reservation_data(self):
        query = "select id, customer_name, phone_number, date(booking_date) as date, " \
                "time_format(time(booking_date), '%H:%i') as time from customerBooking;"

        result = self.db.fetch(query)

        return result

    '''
        This function is called after an employee has been added and returns only the last row.
    '''

    def add_update_reservation_data(self):
        query = "select id, customer_name, phone_number, date(booking_date) as date, " \
                "time_format(time(booking_date), '%H:%i') as time from customerBooking " \
                "order by id desc limit 1;"

        result = self.db.fetch(query)

        return result

    def edit_reservation(self):
        emp_row = self.table.indexAt(self.sender().pos())
        id = int(self.table.cellWidget(emp_row.row(), emp_row.column()).objectName())
        print(emp_row.row())
        print(id)
        print(type(id))

        '''
            Get the data from the database for that user.
        '''
        data = self.get_data(id)

        print("Data")
        print(data)
        # print(type(data[4]))

        view = AddBookingDetails(self, "update", data[0])

        view.customernametextbox.setText(data[1])
        view.customercontacttextbox.setText(str(data[2]))
        view.datetextbox.setDate(QDate.fromString(data[3], "dd-MM-yyyy"))
        # view.starttimetextbox.setTime(QTime.fromString(data[4]), "hh:mm")

        view.closing.connect(self.editupdate_emp)

    def editupdate_emp(self):
        self.table.clearContents()
        self.table.setRowCount(0)

        data = self.load_reservation_data()

        self.populate_table(data)

    def get_data(self, id):
        query = "select id, customer_name, phone_number, date(booking_date) as date, " \
                "time_format(time(booking_date), '%H:%i') as time FROM customerBooking " \
                "where id=%s"
        values = (id,)

        result = self.db.fetch(query, values)

        for (id, customer_name, phone_number, date, time) in result:
            id = id
            customer_name = customer_name
            phone_number = phone_number
            date = date
            time = time

        return [id, customer_name, phone_number, str(date.strftime("%d-%m-%Y"))]

    def delete_reservation(self):
        emp_row = self.table.indexAt(self.sender().pos())

        id = int(self.table.cellWidget(emp_row.row(), emp_row.column()).objectName())

        query = "DELETE FROM customerBooking WHERE id=%s"
        values = (id,)

        result = self.db.execute(query, values)

        self.table.clearContents()
        self.table.setRowCount(0)
        data = self.load_reservation_data()

        self.populate_table(data)

    def add_reservation(self, where):
        if where == "reservations":
            print("Employee Button Clicked from employee")

            view = AddBookingDetails(self, "add")
            view.closing.connect(self.update_reservation)

        elif where == "stocks":
            print("Stock Button Clicked")

    def search_reservation(self, search_obj):
        search = search_obj.text()
        search_obj.setText("")

        print("Search")
        if search != "":
            query = "select id, customer_name, phone_number, date(booking_date) as date, " \
                    "time_format(time(booking_date), '%H:%i') as time FROM customerBooking " \
                    "WHERE customer_name like %s"
            values = ("%" + search + "%",)
        else:
            query = "select id, customer_name, phone_number, date(booking_date) as date, " \
                    "time_format(time(booking_date), '%H:%i') as time FROM customerBooking"
            values = ()

        self.table.clearContents()
        self.table.setRowCount(0)

        data = self.db.fetch(query, values)

        self.populate_table(data)

    '''
        Repopulates the employee table with the updated data.
    '''

    def update_reservation(self, check):
        print("I am here")
        print(check)

        data = self.add_update_reservation_data()

        self.populate_table(data)

    '''
        This function populates the employee table with data.
    '''

    def populate_table(self, data):
        for (id, employee_name, job_title, salary, joining_date) in data:
            self.table.insertRow(self.table.rowCount())

            self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(str(employee_name)))
            self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(str(job_title)))
            self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(str(salary.strftime("%d-%m-%Y"))))
            # self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(str(bonus)))
            self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(str(joining_date)))

            edit = QPushButton(self.table)
            edit.setObjectName(str(id))
            edit.setStyleSheet("background-color: rgb(50,205,50);")
            edit.setText("Edit")
            edit.adjustSize()
            edit.clicked.connect(self.edit_reservation)

            self.table.setCellWidget(self.table.rowCount() - 1, 4, edit)

            delete = QPushButton(self.table)
            delete.setObjectName(str(id))
            delete.setStyleSheet("background-color: #d63447;")
            delete.setText("Delete")
            delete.adjustSize()
            delete.clicked.connect(self.delete_reservation)
            # delete.mousePressEvent = functools.partial(self.delete_emp, source_object=delete)
            self.table.setCellWidget(self.table.rowCount() - 1, 5, delete)