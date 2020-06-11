"""
    This job should take no more than an hour.

    1. Add Product Details
    2. Add Table Details
    3. Add Booking Details
    4. Add Order Details

"""


from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget, QApplication, QLabel, QLineEdit, QVBoxLayout,
                             QHBoxLayout, QWidget, QFrame, QPushButton, QDateEdit, QComboBox)
from PyQt5.QtCore import (QRect, Qt)
from PyQt5.QtCore import (Qt, QDate)


class AddProductDetails(QFrame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

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
        add_employee_button.setText("Add Product Details")

        namelabel = QLabel(frame)
        namelabel.setText("Name")
        namelabel.setGeometry(QRect(70, 100, 47, 13))

        nametextbox = QLineEdit(frame)
        nametextbox.setGeometry(QRect(160, 90, 181, 31))
        nametextbox.setFixedWidth(180)

        categorylabel = QLabel(frame)
        categorylabel.setText("Category")
        categorylabel.setGeometry(QRect(70, 140, 61, 16))

        categorytextbox = QComboBox(frame)
        categorytextbox.setGeometry(QRect(160, 130, 181, 31))
        categorytextbox.setFixedWidth(180)
        categorytextbox.addItems(["Pizza", "Burger"])

        quantitylabel = QLabel(frame)
        quantitylabel.setText("Quantity")
        quantitylabel.setGeometry(QRect(70, 180, 47, 13))

        quantitytextbox = QLineEdit(frame)
        quantitytextbox.setGeometry(QRect(160, 170, 181, 31))
        quantitytextbox.setFixedWidth(180)

        pricelabel = QLabel(frame)
        pricelabel.setText("Price")
        pricelabel.setGeometry(QRect(70, 220, 47, 13))

        pricetextbox = QLineEdit(frame)
        pricetextbox.setGeometry(QRect(160, 210, 181, 31))
        pricetextbox.setFixedWidth(180)

        sellingpricelabel = QLabel(frame)
        sellingpricelabel.setText("Selling Price")
        sellingpricelabel.setGeometry(QRect(70, 260, 90, 16))

        sellingpricetextbox = QDateEdit(frame)
        sellingpricetextbox.setGeometry(QRect(160, 250, 181, 31))
        sellingpricetextbox.setFixedWidth(180)
        sellingpricetextbox.setDate(QDate.currentDate())
        sellingpricetextbox.setMinimumDate(QDate.currentDate())

        addbutton = QPushButton(frame)
        addbutton.setText("Add Product")
        addbutton.setGeometry(QRect(160, 300, 111, 31))
        addbutton.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(30, 45, 66);\n"
                                   "color: rgb(255, 255, 255);")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(frame)

        self.setLayout(layout)

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