import sqlite3


class DB:

    @classmethod
    def connect(cls):
        conn = sqlite3.connect('Data/ccms.db')
        return conn.cursor()

    @classmethod
    def delete_assignment_record(cls):
        cur = cls.connect()
        cur.execute("DELETE FROM assignments WHERE assignment_id = ?", assignment_id)

    @classmethod
    def delete_attendance_record(cls):
        cur = cls.connect()
        cur.execute("DELETE FROM attendances WHERE attendance_id = ?", attendance_id)

    @classmethod
    def delete_submission_record(cls):
        cur = cls.connect()
        cur.execute("DELETE FROM submissions WHERE submission_id = ?", submission_id)

    @classmethod
    def delete_user_record(cls):
        cur = cls.connect()
        cur.execute("DELETE FROM users WHERE user_id = ?", user_id)
