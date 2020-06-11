from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import (QRect, Qt)
from PyQt5.QtCore import Qt

from appname import AppName
# from sidebar import Sidebar
from footer import Footer
import sidebar

from addsearchframe import AddSearchFrame

from addmenudetails import AddMenuDetails

from classes2.db import DB


class Menu(QMainWindow):

    def __init__(self, parent):
        super().__init__(parent)

        self.db = DB()

        self.initUI()

    def initUI(self):

        in_class = "menu"

        self.sidebar = sidebar.Sidebar(self)
        self.sidebar.window.connect(self.getvalue)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)

        header = AppName(in_class)
        footer = Footer()

        add_and_search = AddSearchFrame(in_class)
        add_and_search.add_button.clicked.connect(lambda: self.add_menu(in_class))
        add_and_search.search_button.clicked.connect(
                                        lambda: self.search_menu(add_and_search.search_box))


        self.table = QTableWidget()
        self.table.setColumnCount(5)
        # self.table.setStyleSheet("border: none")
        # self.table.setStyleSheet(
        #     "background-color: rgb(255, 255, 255);\n"
        #     'font: 10pt "MS Shell Dlg 2";\n'
        #     "color: rgb(30, 45, 66);"
        # )

        # self.table.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Food"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Category"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Price"))
        # self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Bonus"))
        # self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Joining Date"))
        # self.table.setHorizontalHeaderItem(6, QTableWidgetItem("Total Salary"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Edit"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("Delete"))


        data = self.load_menu_data()
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
            pass
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

    def load_menu_data(self):
        query = "SELECT food_name, price, category_name FROM menu " \
                "join category on menu.category_id = category.id order by category_name"

        result = self.db.fetch(query)

        return result

    '''
        This function is called after an employee has been added and returns only the last row.
    '''
    def add_update_menu_data(self):
        query = "SELECT food_name, price, category_name FROM menu " \
                "join category on menu.category_id = category.id " \
                "order by id desc limit 1;"

        result = self.db.fetch(query)

        return result

    def edit_menu(self):
        emp_row = self.table.indexAt(self.sender().pos())
        id = self.table.cellWidget(emp_row.row(), emp_row.column()).objectName()
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



        view = AddMenuDetails(self, "update", data[0])

        view.nametextbox.setText(data[0])
        view.pricetextbox.setText(str(data[1]))

        category = self.get_category(data[2])
        view.category_list.setCurrentText(category)

        view.closing.connect(self.editupdate_emp)

    def get_category(self, category):
        query = "SELECT category_name FROM category " \
                "where id=%s"
        values = (category,)

        result = self.db.fetch(query, values)

        for (category) in result:
            category = category[0]

        return category

    def editupdate_emp(self, check):
        print("I am here")
        print(check)

        self.table.clearContents()
        self.table.setRowCount(0)

        data = self.load_menu_data()

        self.populate_table(data)
        self.table.resizeColumnsToContents()
        # self.table.resizeColumnsToContents()

    def get_data(self, id):
        query = "SELECT food_name, price, category_id FROM menu " \
                "where food_name=%s"
        values = (id,)

        result = self.db.fetch(query, values)

        for (food_name, price, category) in result:
            food_name = food_name
            price = price
            category = category

        return [food_name, price, category]

    def delete_menu(self):
        emp_row = self.table.indexAt(self.sender().pos())

        # print(emp_row.row())
        # print(emp_row.column())

        # print(self.table.cellWidget(emp_row.row(), emp_row.column()).objectName())

        id = self.table.cellWidget(emp_row.row(), emp_row.column()).objectName()
        # print(id)
        # print(emp_row.child(emp_row.row(), emp_row.column()))

        query = "DELETE FROM menu WHERE food_name=%s"
        values = (id,)

        result = self.db.execute(query, values)

        self.table.clearContents()
        self.table.setRowCount(0)
        data = self.load_menu_data()

        self.populate_table(data)

    def add_menu(self, where):
        if where == "menu":
            print("Employee Button Clicked from Menu")

            view = AddMenuDetails(self, "add")
            view.closing.connect(self.update_menu)

        elif where == "stocks":
            print("Stock Button Clicked")

    def search_menu(self, search_obj):
        search = search_obj.text()
        search_obj.setText("")

        print("Search")
        if search != "":
            query = "SELECT * FROM menu WHERE food_name like %s"
            values = ("%" + search + "%",)
        else:
            query = "SELECT * FROM menu"
            values = ()

        self.table.clearContents()
        self.table.setRowCount(0)

        data = self.db.fetch(query, values)

        self.populate_table(data)




    '''
        Repopulates the employee table with the updated data.
    '''
    def update_menu(self, check):
        print("I am here")
        print(check)

        self.table.clearContents()
        self.table.setRowCount(0)
        data = self.load_menu_data()

        self.populate_table(data)

    '''
        This function populates the employee table with data.
    '''
    def populate_table(self, data):
        for (food_name, price, category_name) in data:
            self.table.insertRow(self.table.rowCount())

            self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(str(food_name)))
            self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(str(category_name)))
            self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(str(price)))
            # self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(str(bonus)))
            # self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(str(joining_date.strftime("%d-%m-%Y"))))
            edit = QPushButton(self.table)
            edit.setObjectName(str(food_name))
            edit.setStyleSheet("background-color: rgb(50,205,50);")
            edit.setText("Edit")
            edit.adjustSize()
            edit.clicked.connect(self.edit_menu)

            self.table.setCellWidget(self.table.rowCount() - 1, 3, edit)

            delete = QPushButton(self.table)
            delete.setObjectName(str(food_name))
            delete.setStyleSheet("background-color: #d63447;")
            delete.setText("Delete")
            delete.adjustSize()
            delete.clicked.connect(self.delete_menu)
            # delete.mousePressEvent = functools.partial(self.delete_menu, source_object=delete)
            self.table.setCellWidget(self.table.rowCount() - 1, 4, delete)