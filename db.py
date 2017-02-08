import sqlite3


class DB:

    @classmethod
    def connect(cls):
        conn = sqlite3.connect('Data/ccms.db')
        return conn.cursor()

    @classmethod
    def create_record(cls, table, values):
        db = cls.connect()
        queries = ['INSERT INTO ? VALUES (']
