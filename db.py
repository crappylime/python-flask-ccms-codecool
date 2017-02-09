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
        return cls.execute_insert_query(query, values)

    @classmethod
    def create_assignment_record(cls, values):
        query = 'INSERT INTO assignments (`title`, `content`, `due_date`, `max_points`) VALUES (?, ?, ?, ?);'
        return cls.execute_insert_query(query, values)

    @classmethod
    def create_submission_record(cls, values):
        query = 'INSERT INTO submissions (`assignment_id`, `user_id`, `content`, `date`) VALUES (?, ?, ?, ?);'
        return cls.execute_insert_query(query, values)

    @classmethod
    def create_attendance_record(cls, values):
        query = 'INSERT INTO attendances (`user_id`, `date`, `status`) VALUES (?, ?, ?);'
        return cls.execute_insert_query(query, values)

    @classmethod
    def create_team(cls, name):
        query = "INSERT INTO `teams` (`name`) VALUES (?)"
        args = name
        return cls.execute_insert_query(query, (args,))

    @classmethod
    def create_member_record(cls, team_id, student_id):
        query = 'INSERT INTO `members` VALUES (?, ?);'
        print(team_id, student_id)
        args = (team_id, student_id)
        return cls.execute_insert_query(query, args)

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
    def read_user_record_list(cls):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `users`;"
        cursor.execute(query)
        user_list = cursor.fetchall()
        conn.close()
        return user_list

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
    def read_user_record_list_by_id(cls, id_list):
        conn = cls.connect()
        cursor = conn.cursor()
        placeholder = '?'
        placeholders = ', '.join(placeholder for unused in id_list)
        query = 'SELECT * FROM `users` WHERE `user_id` IN (%s);' % placeholders
        cursor.execute(query, id_list)
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
    def read_submission_record_list_by_user_id(cls, user_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `submissions` WHERE `user_id` = ?;"
        cursor.execute(query, (user_id,))
        user_submission_list = cursor.fetchall()
        conn.close()
        return user_submission_list

    @classmethod
    def read_team_record_by_id(cls, team_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `teams` WHERE `id` = ?;"
        cursor.execute(query, (team_id,))
        team_list = cursor.fetchall()
        conn.close()
        return team_list

    @classmethod
    def read_submission_record_list_by_assignment_id(cls, assignment_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `submissions` WHERE `assignment_id` = ?;"
        cursor.execute(query, (assignment_id,))
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

    @classmethod
    def read_attendance_record_by_id(cls, attendance_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `attendances` WHERE `attendance_id` = ?;"
        cursor.execute(query, (attendance_id,))
        attendance = cursor.fetchall()
        conn.close()
        return attendance

    @classmethod
    def read_attendance_record_list_by_student_id(cls, student_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `attendances` WHERE `user_id` = ?;"
        cursor.execute(query, (student_id,))
        attendance = cursor.fetchall()
        conn.close()
        return attendance

    @classmethod
    def read_attendance_record_list(cls):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `attendances`;"
        cursor.execute(query)
        attendance_list = cursor.fetchall()
        conn.close()
        return attendance_list

    @classmethod

    def read_overall_grade(cls, student_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT round(avg(100.0*submissions.points/assignments.max_points),2) FROM submissions " \
                "INNER JOIN assignments ON submissions.assignment_id=assignments.assignment_id " \
                "WHERE `user_id`=?;"
        cursor.execute(query, (student_id,))
        overall_grade = cursor.fetchall()[0][0]
        print(overall_grade, student_id)
        conn.close()
        return overall_grade

    @classmethod
    def read_overall_attendance(cls, student_id):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT round(avg(100.0*status), 2) from attendances WHERE `user_id`=?;"
        cursor.execute(query, (student_id,))
        overall_attendance = cursor.fetchall()[0][0]
        print(overall_attendance, student_id)
        conn.close()
        return overall_attendance

    @classmethod
    def read_team_list(cls):
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `teams`;"
        cursor.execute(query)
        team_list = cursor.fetchall()
        conn.close()
        return team_list

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
