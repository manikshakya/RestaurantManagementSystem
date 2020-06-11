import mysql.connector as mysql

# Database Class


class DB:
    # Constructor of Database Class
    def __init__(self):
        # instance of database object that connects us to the database
        self._db = mysql.connect(
            host="localhost", user="root", passwd="", database="rmsFinalProject")  # rms_final_project
        # Closing the database Connection
        self._db.close()

    # It is function that gets takes query and values and perform the query on database;
    # This function is only used for query that are related to getting the information from database;
    # It returns the result after getting from the database
    def fetch(self, query, values=None):
        self._db.reconnect()
        cursor = self._db.cursor()
        if values == None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        self._db.close()
        return result

    # It is a function that also takes the query and values to perform the query on database
    # This function is only used for query where there is only execution is need; no data to get from database
    # It returns the status of query executed on the database
    def execute(self, query, values):
        self._db.reconnect()
        cursor = self._db.cursor()
        cursor.execute(query, values)
        # row_count = cursor.rowcount
        self._db.commit()
        row_last_id = cursor.getlastrowid()
        cursor.close()
        self._db.close()
        return row_last_id
