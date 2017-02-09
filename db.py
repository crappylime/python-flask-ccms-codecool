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

    @classmethod
    def read_user_record_list_by_role(cls, role):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `users` WHERE `role` = ?;"
        cursor.execute(query, (role,))
        user_list = cursor.fetchall()
        conn.close()
        return user_list

    @classmethod
    def read_assignment_record_by_id(cls, assignment_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `assignments` WHERE `assignment_id` = ?;"
        cursor.execute(query, (assignment_id,))
        assignment = cursor.fetchall()
        conn.close()
        return assignment

    @classmethod
    def read_assignment_record_list(cls):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `assignments`;"
        cursor.execute(query)
        assignment_list = cursor.fetchall()
        conn.close()
        return assignment_list

    @classmethod
    def read_submission_record_by_id(cls, submission_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `submissions` WHERE `submission_id` = ?;"
        cursor.execute(query, (submission_id,))
        submission = cursor.fetchall()
        conn.close()
        return submission

    @classmethod
    def read_submission_record_by_user_id(cls, user_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `submissions` WHERE `user_id` = ?;"
        cursor.execute(query, (user_id,))
        user_submission_list = cursor.fetchall()
        conn.close()
        return user_submission_list

    @classmethod
    def read_submission_record_list(cls):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `submissions`;"
        cursor.execute(query)
        submission_list = cursor.fetchall()
        conn.close()
        return submission_list
