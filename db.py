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
        cur.executemany(query, args)
        conn.commit()
        conn.close()

    @classmethod
    def delete_assignment_record(cls, assignment_id):
        query = "DELETE FROM assignments WHERE assignment_id = ?"
        args = assignment_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_attendance_record(cls, attendance_id):
        query = "DELETE FROM attendances WHERE attendance_id = ?"
        args = attendance_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_submission_record(cls, submission_id):
        query = "DELETE FROM submissions WHERE submission_id = ?"
        args = submission_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_user_record(cls, user_id):
        query = "DELETE FROM users WHERE user_id = ?"
        args = user_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_user_attendance_record(cls, user_id):
        query = "DELETE FROM attendances WHERE user_id = ?"
        args = user_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_user_submission_record(cls, user_id):
        query = "DELETE FROM submissions WHERE user_id = ?"
        args = user_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_assignment_submission_record(cls, assignment_id):
        query = "DELETE FROM submissions WHERE assignment_id = ?"
        args = assignment_id
        cls.execute_query(query, (args,))
