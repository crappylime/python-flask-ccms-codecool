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
    def execute_insert_query(cls, query, args):
        conn = cls.connect()
        cur = conn.cursor()
        cur.execute(query, args)
        last_id = cur.lastrowid
        conn.commit()
        conn.close()
        return last_id

    @classmethod
    def create_user_record(cls, values):
        query = 'INSERT INTO users (`name`, `mail`, `password`, `role`) VALUES (?, ?, ?, ?);'
        cls.execute_insert_query(query, values)

    @classmethod
    def create_assignment_record(cls, values):
        query = 'INSERT INTO assignments (`title`, `content`, `due_date`, `max_points`) VALUES (?, ?, ?, ?);'
        cls.execute_insert_query(query, values)

    @classmethod
    def create_submission_record(cls, values):
        query = 'INSERT INTO submissions (`assignment_id`, `user_id`, `content`, `date`) VALUES (?, ?, ?, ?);'
        cls.execute_insert_query(query, values)

    @classmethod
    def create_attendance_record(cls, values):
        query = 'INSERT INTO attendances (`user_id`, `date`, `status`) VALUES (?, ?, ?);'
        cls.execute_insert_query(query, values)

    def delete_assignment_record(cls, assignment_id):
        query = "DELETE FROM assignments WHERE assignment_id = ?"
        args = assignment_id
        cls.execute_query(query, (args,))

    @classmethod
    def create_team(cls, name):
        query = "INSERT INTO `teams` (`name`) VALUES (?)"
        args = name
        cls.execute_query(query, (args,))

    @classmethod
    def update_name(cls, user_id, name):
        query = "UPDATE `users` SET `name` = ? WHERE `user_id` = ?;"
        args = (name, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_mail(cls, user_id, new_mail):
        query = "UPDATE `users` SET `mail` = ? WHERE `user_id` = ?;"
        args = (new_mail, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_password(cls, user_id, new_password):
        query = "UPDATE `users` SET `password` = ? WHERE `user_id` = ?;"
        args = (new_password, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_attendance(cls, user_id, date, status):
        query = "UPDATE `attendances` SET `status` = ? WHERE `user_id` = ? AND `date` = ?;"
        args = (status, user_id, date)
        cls.execute_query(query, args)

    @classmethod
    def update_grade(cls, user_id, assignment_id, points):
        query = "UPDATE `submissions` SET `points` = ? WHERE `assignment_id` = ? AND `user_id` = ?;"
        args = (points, assignment_id, user_id)
        cls.execute_query(query, args)

    @classmethod
    def add_member(cls, team_id, student_id):
        pass

