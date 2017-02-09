import sqlite3


class DB:

    @classmethod
    def connect(cls):
        return sqlite3.connect('ccms.db')

    @classmethod
    def read_user_record_by_user_id(cls, user_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `users` WHERE `user_id` = ?;"
        cursor.execute(query, (user_id,))
        user = cursor.fetchall()
        conn.close()
        return user
