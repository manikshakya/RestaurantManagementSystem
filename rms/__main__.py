from PyQt5.QtWidgets import QApplication
import sys

from test import Test

from login import Login  # This the only one we need.

# from sidebar import Sidebar
# from dashboard import Dashboard
# from employee import Employee       #  Done
# from addemployeedetails import AddEmployeeDetails
# from addproductdetails import AddProductDetails
# from addtabledetails import AddTableDetails
# from addbookingdetails import AddBookingDetails
# from reservations import Reservations   # Done
# from category import Category       # Done
# from tables import Table            # Done
# from settings import Settings # Almost Done
# from addmenudetails import AddMenuDetails
# from orders import Orders

app = QApplication([])
login = Login()  # starting point Login()
sys.exit(app.exec_())
