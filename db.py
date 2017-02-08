import sqlite3


class DB:

    @classmethod
    def connect(cls):
        conn = sqlite3.connect('Data/ccms.db')
        return conn.cursor()

    @classmethod
    def update_name(cls, user_id, name):
        db = cls.connect()
        db.execute("UPDATE `users` SET `name` = ? WHERE `id` = ?;", (user_id, name))
        conn.commit()
        conn.close()

    @classmethod
    def update_mail(cls, user_id, mail):
        db = cls.connect()
        db.execute("UPDATE `users` SET `mail` = ? WHERE `id` = ?;", (user_id, mail))
        conn.commit()
        conn.close()

    @classmethod
    def update_password



