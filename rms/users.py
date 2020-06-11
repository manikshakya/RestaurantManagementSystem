from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import (QRect, Qt)
from PyQt5.QtCore import Qt

from appname import AppName
# from sidebar import Sidebar
from footer import Footer
from addsearchframe import AddSearchFrame
import sidebar

from addemployeedetails import AddEmployeeDetails

from classes2.db import DB


'''
    Put a try catch on db execution later..
'''

class Users(QMainWindow):

    def __init__(self, parent):
        super().__init__(parent)

        self.db = DB()

        self.initUI()

    def initUI(self):

        in_class = "users"

        self.sidebar = sidebar.Sidebar(self)
        # self.sidebar.window.connect(self.getvalue)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)

        header = AppName(in_class)
        footer = Footer()

        add_and_search = AddSearchFrame(in_class)
        add_and_search.add_button.clicked.connect(lambda: self.add_users(in_class))
        add_and_search.search_button.clicked.connect(
                                        lambda: self.search_users(add_and_search.search_box))

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        # self.table.setStyleSheet("border: none")
        # self.table.setStyleSheet(
        #     "background-color: rgb(255, 255, 255);\n"
        #     'font: 10pt "MS Shell Dlg 2";\n'
        #     "color: rgb(30, 45, 66);"
        # )

        # self.table.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Usernmae"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Password"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Roles"))
        # self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Bonus"))
        # self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Joining Date"))
        # self.table.setHorizontalHeaderItem(6, QTableWidgetItem("Total Salary"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Edit"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("Delete"))

        data = self.load_users_data()
        print(data)

        for x in data:
            print(x)

        self.populate_table(data)
        self.table.resizeColumnsToContents()

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
        self.setWindowTitle("Employee")
        self.resize(1160, 605)

        self.show()
        self.center()

    def center(self):
        '''centers the window on the screen'''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def load_users_data(self):
        query = "SELECT id, admin_name, password, roles FROM admin where admin_name != 'admin'"

        result = self.db.fetch(query)

        return result

        # for (name, job_title, salary, bonus, joining_date) in result:
        #     print("=========Start==========")
        #     print("     " + str(name))
        #     print("     " + str(job_title))
        #     print("     " + str(salary))
        #     print("     " + str(bonus))
        #     print("     " + str(joining_date))
        #     print("=========End==========")
        #     print("\n")

    '''
        This function is called after an employee has been added and returns only the last row.
    '''
    def add_update_users_data(self):
        query = "SELECT id, admin_name, password, roles FROM admin where admin_name != 'admin' " \
                "order by id desc limit 1;"

        result = self.db.fetch(query)

        return result

    def edit_users(self):
        emp_row = self.table.indexAt(self.sender().pos())
        print(emp_row.row())

    def delete_users(self):
        emp_row = self.table.indexAt(self.sender().pos())

        # print(emp_row.row())
        # print(emp_row.column())

        # print(self.table.cellWidget(emp_row.row(), emp_row.column()).objectName())

        id = int(self.table.cellWidget(emp_row.row(), emp_row.column()).objectName())
        # print(id)
        # print(emp_row.child(emp_row.row(), emp_row.column()))

        query = "DELETE FROM admin WHERE id=%s"
        values = (id,)

        result = self.db.execute(query, values)

        self.table.clearContents()
        self.table.setRowCount(0)
        data = self.load_users_data()

        self.populate_table(data)

    def add_users(self, where):
        if where == "employees":
            print("Employee Button Clicked from employee")

            view = AddEmployeeDetails(self)
            view.closing.connect(self.update_users)

        elif where == "stocks":
            print("Stock Button Clicked")

    def search_users(self, search_obj):
        search = search_obj.text()
        search_obj.setText("")

        print("Search")
        if search != "":
            query = "SELECT id, admin_name, password, roles FROM admin " \
                    "where admin_name != 'admin' and admin_name like %s"
            values = ("%" + search + "%",)
        else:
            query = "SELECT id, admin_name, password, roles FROM admin " \
                    "where admin_name != 'admin'"
            values = ()

        self.table.clearContents()
        self.table.setRowCount(0)

        data = self.db.fetch(query, values)

        self.populate_table(data)

    '''
        Repopulates the employee table with the updated data.
    '''
    def update_users(self, check):
        print("I am here")
        print(check)

        data = self.add_update_users_data()

        self.populate_table(data)

    '''
        This function populates the employee table with data.
    '''
    def populate_table(self, data):
        for (id, admin_name, password, roles) in data:
            self.table.insertRow(self.table.rowCount())

            self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(str(admin_name)))
            self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(str(password)))
            self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(str(roles)))
            # self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(str(bonus)))
            # self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(str(joining_date.strftime("%d-%m-%Y"))))
            edit = QPushButton(self.table)
            edit.setStyleSheet("background-color: rgb(50,205,50);")
            edit.setText("Edit")
            edit.adjustSize()
            edit.clicked.connect(self.edit_users)

            self.table.setCellWidget(self.table.rowCount() - 1, 3, edit)

            delete = QPushButton(self.table)
            delete.setObjectName(str(id))
            delete.setStyleSheet("background-color: #d63447;")
            delete.setText("Delete")
            delete.adjustSize()
            delete.clicked.connect(self.delete_users)
            # delete.mousePressEvent = functools.partial(self.delete_users, source_object=delete)
            self.table.setCellWidget(self.table.rowCount() - 1, 4, delete)