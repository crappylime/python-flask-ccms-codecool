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
    def create_user_record(cls, values):
        query = 'INSERT INTO users (`name`, `mail`, `password`, `role`) VALUES (?, ?, ?, ?);'
        cls.execute_query(query, values)

    @classmethod
    def create_assignment_record(cls, values):
        query = 'INSERT INTO assignments (`title`, `content`, `due_date`, `max_points`) VALUES (?, ?, ?, ?);'
        cls.execute_query(query, values)

    @classmethod
    def create_submission_record(cls, values):
        query = 'INSERT INTO submissions (`assignment_id`, `user_id`, `content`, `date`, `points`) VALUES (?, ?, ?, ?, ?);'
        cls.execute_query(query, values)

    @classmethod
    def create_attendance_record(cls, values):
        query = 'INSERT INTO attendances (`user_id`, `date`, `status`) VALUES (?, ?, ?);'
        cls.execute_query(query, values)

