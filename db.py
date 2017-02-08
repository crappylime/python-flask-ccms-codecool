import sqlite3


class DB:

    @classmethod
    def connect(cls):
        return sqlite3.connect('Data/ccms.db')

    @classmethod
    def execute_query(cls, query, args):
        conn = cls.connect()
        cur = conn.cursor()
        if type(args) is tuple:
            args = [args]
            print(args)
        cur.executemany(query, args)
        conn.commit()
        conn.close()

    @classmethod
    def delete_assignment_record(cls, assignment_id):
        query = "DELETE FROM assignments WHERE assignment_id = ?"
        args = assignment_id
        cls.execute_query(query, (args,))

    @classmethod
    def update_name(cls, user_id, name):
        query = "UPDATE `users` SET `name` = ? WHERE `id` = ?;"
        args = (name, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_mail(cls, user_id, mail):
        query = "UPDATE `users` SET `mail` = ? WHERE `id` = ?;"
        args = (mail, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_password(cls, user_id, password):
        query = "UPDATE `users` SET `password` = ? WHERE `id` = ?;"
        args = (password, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_attendance(cls, user_id, status):
        query = "UPDATE `attendances` SET `password` = ? WHERE `id` = ?;"
        args = (status, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_grade(clscls, user_id, assignment_id, points):
        query = "UPDATE `submissions` SET `points` = ? WHERE `assignment_id` = ? AND `id` = ?;"
        args = (points, assignment_id, user_id)
        cls.execute_query(query, args)


    # ocena





