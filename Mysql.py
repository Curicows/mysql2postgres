import mysql.connector
from DB import DB


class Mysql(DB):
    def __init__(self):
        super().__init__()

    def connect(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword"
        )

    def query(self):
        pass

    def commit(self):
        pass

    def insert(self):
        pass

    def kill(self):
        pass
