import sqlite3


class DB:

    @classmethod
    def connect(cls):
        return sqlite3.connect('ccms.db')

