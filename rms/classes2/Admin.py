from classes2.db import DB

# Admin Class for managing Admin  related operation


class Admin:

    # Admin class constructor for initalizaing the object
    def __init__(self, id=None, name=None, password=None):
        # Database Class object for communication with database; will be used down in the function
        self._db = DB()
        # Id of admin used for database primary key
        self.id = id
        # name of admin
        self.name = name
        # password of admin
        self.password = password

    # login function for the admin class;  It true if name and password matches otherwise returns false
    def login(self):
        query = "SELECT * FROM admin where admin_name=%s and password=%s"
        db = DB()
        values = (self.name, self.password)
        result = db.fetch(query, values)
        if result:
            self.id = result[0][0]
            self.name = result[0][1]
            self.password = result[0][2]
            return True
        return False

    def login(self, name, password):
        query = "update admin set logged_in='no' where logged_in='yes'"
        db = DB()
        values = (self.name, self.password)

        self.name = name
        self.password = password

        query = "SELECT * FROM admin where admin_name=%s and password=%s"
        db = DB()
        values = (self.name, self.password)
        result = db.fetch(query, values)
        if result:
            self.id = result[0][0]
            self.name = result[0][1]
            self.password = result[0][2]
            return True
        return False

    # Change password function for admin; It returns nothing
    def changePwd(self, newPwd):
        query = """UPDATE `admin` SET `password`= %s WHERE id = %s;"""
        values = (newPwd, self.id)
        self._db.execute(query, values)

    # Function that updates the restaurent information in the database; It returns nothing
    def updateRestaurentDetail(self, name, address, contact):
        query = """UPDATE `rest_info` SET `name`= %s, `address`= %s, `contact`= %s WHERE id = %s;"""
        values = (name, address, contact, 1)
        self._db.execute(query, values)

    # It is a static function of admin class that is use get the Restaurent
    # information from the database; It returns the restaurent information
    @staticmethod
    def getRestDetails():
        query = "SELECT * FROM rest_info where id=%s"
        db = DB()
        values = (1,)
        result = db.fetch(query, values)
        return result

    # It is a static function that Counts the Number of order from the database; It returns the value of orders count
    @staticmethod
    def getOrdersCounts():
        query = "SELECT Count(id) FROM `order`"
        db = DB()
        result = db.fetch(query)
        return result[0][0]

    # It is a static function that calculate the sum of total sales; It returns the value of total sale
    @staticmethod
    def getTotalSale():
        query = "SELECT SUM(product.selling_price*product_order.quantity) FROM product_order JOIN product ON product_order.product_id=product.id;"
        db = DB()
        result = db.fetch(query)
        if result:
            return result[0][0]
        return None

    # It is a static function that calculate the sum of profit i.e.
    # For each order calculate the profit for individual product and then sum it; It returns the value of total profit
    @staticmethod
    def getTotalProfit():
        query = "SELECT SUM((product.selling_price-product.price)*product_order.quantity) FROM product_order JOIN product ON product_order.product_id=product.id;"
        db = DB()
        result = db.fetch(query)
        if result:
            return result[0][0]
        return None
