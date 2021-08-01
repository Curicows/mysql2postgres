import psycopg2
from DB import DB


class Postgres(DB):
    def __init__(self):
        super().__init__()
        #self.conn = None
        #self.cursor = None

    def connect(self, *args, **kwargs):
        try:
            conn = psycopg2.connect(host=kwargs.get("host"), database=kwargs.get("database"),
                                    user=kwargs.get("user"), password=kwargs.get("password"))
        except:
            return False
        self.conn = conn
        return True

    def insert(self):
        pass
