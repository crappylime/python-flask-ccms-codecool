import sqlite3


class DB:

    @classmethod
    def connect(cls):
        """Connect with database"""
        return sqlite3.connect('data/ccms.db')

    @classmethod
    def execute_query(cls, query, args):
        """Execute query based on provided parameters"""
        conn = cls.connect()
        cur = conn.cursor()
        if type(args) is tuple:
            args = [args]
        cur.executemany(query, args)
        conn.commit()
        conn.close()

    @classmethod
    def execute_insert_query(cls, query, args):
        """Execute query and return new record id"""
        conn = cls.connect()
        cur = conn.cursor()
        cur.execute(query, args)
        last_id = cur.lastrowid
        conn.commit()
        conn.close()
        return last_id

    @classmethod
    def create_user_record(cls, values):
        """Add new user record to database"""
        query = 'INSERT INTO users (`name`, `mail`, `password`, `role`) VALUES (?, ?, ?, ?);'
        return cls.execute_insert_query(query, values)

    @classmethod
    def create_assignment_record(cls, values):
        """Add new assignment record to database"""
        query = 'INSERT INTO assignments (`title`, `is_team`, `content`, `due_date`, `max_points`) VALUES (?, ?, ?, ?, ?);'
        return cls.execute_insert_query(query, values)

    @classmethod
    def create_submission_record(cls, values):
        """Add new submission record to database"""
        query = 'INSERT INTO submissions (`assignment_id`, `user_id`, `content`, `date`) VALUES (?, ?, ?, ?);'
        return cls.execute_insert_query(query, values)

    @classmethod
    def create_attendance_record(cls, values):
        """Add attendance record to database"""
        query = 'INSERT INTO attendances (`user_id`, `date`, `status`) VALUES (?, ?, ?);'
        return cls.execute_insert_query(query, values)

    @classmethod
    def create_team(cls, name):
        """Add new team to database"""
        query = "INSERT INTO `teams` (`name`) VALUES (?)"
        args = name
        return cls.execute_insert_query(query, (args,))

    @classmethod
    def create_member_record(cls, team_id, student_id):
        """Add new member record to database"""
        query = 'INSERT INTO `members` VALUES (?, ?);'
        args = (team_id, student_id)
        return cls.execute_insert_query(query, args)

    @classmethod
    def read_user_record_by_user_id(cls, user_id):
        """Read user record by provided id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `users` WHERE `user_id` = ?;"
        cursor.execute(query, (user_id,))
        user = cursor.fetchall()
        conn.close()
        return user

    @classmethod
    def read_user_record_list_by_user_id(cls, user_id):
        """Read user record list by provided id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `users` WHERE `user_id` = ?;"
        cursor.execute(query, (user_id,))
        user = cursor.fetchall()
        conn.close()
        return user

    @classmethod
    def read_user_record_list(cls):
        """Read all user records list"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `users`;"
        cursor.execute(query)
        user_list = cursor.fetchall()
        conn.close()
        return user_list

    @classmethod
    def read_user_record_list_by_role(cls, role):
        """Read user record list by provided role"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `users` WHERE `role` = ?;"
        cursor.execute(query, (role,))
        user_list = cursor.fetchall()
        conn.close()
        return user_list

    @classmethod
    def read_user_record_list_by_id(cls, id_list):
        """Read user record list by provided id"""
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
    def read_user_id_list_by_team_id(cls, team_id):
        """Read user id list by provided team id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT `student_id` FROM `members` WHERE `team_id` = ?;"
        cursor.execute(query, (team_id,))
        temp_list = cursor.fetchall()
        user_list = [int(elem[0]) for elem in temp_list]
        conn.close()
        return user_list

    @classmethod
    def read_assignment_record_by_id(cls, assignment_id):
        """Read assignment record by provided assignment id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `assignments` WHERE `assignment_id` = ?;"
        cursor.execute(query, (assignment_id,))
        assignment = cursor.fetchall()
        conn.close()
        return assignment

    @classmethod
    def read_assignment_record_list(cls):
        """Read assignment record list"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `assignments`;"
        cursor.execute(query)
        assignment_list = cursor.fetchall()
        conn.close()
        return assignment_list

    @classmethod
    def read_team_assignment_record_list(cls):
        """Read assignment record list"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `assignments` WHERE `is_team` = 1;"
        cursor.execute(query)
        assignment_list = cursor.fetchall()
        conn.close()
        return assignment_list

    @classmethod
    def read_submission_record_by_id(cls, submission_id):
        """Read submission reacord by provided submission id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `submissions` WHERE `submission_id` = ?;"
        cursor.execute(query, (submission_id,))
        submission = cursor.fetchall()
        conn.close()
        return submission

    @classmethod
    def read_submission_record_list_by_user_id(cls, user_id):
        """Read submission record list by provided user id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `submissions` WHERE `user_id` = ?;"
        cursor.execute(query, (user_id,))
        user_submission_list = cursor.fetchall()
        conn.close()
        return user_submission_list

    @classmethod
    def read_team_record_by_id(cls, team_id):
        """Read team record by provided team id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `teams` WHERE `id` = ?;"
        cursor.execute(query, (team_id,))
        team_list = cursor.fetchall()
        conn.close()
        return team_list

    @classmethod
    def read_submission_record_list_by_assignment_id(cls, assignment_id):
        """Read submission record list by provided assignment id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `submissions` WHERE `assignment_id` = ?;"
        cursor.execute(query, (assignment_id,))
        user_submission_list = cursor.fetchall()
        conn.close()
        return user_submission_list

    @classmethod
    def read_submission_record_list(cls):
        """Read submission record list"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `submissions`;"
        cursor.execute(query)
        submission_list = cursor.fetchall()
        conn.close()
        return submission_list

    @classmethod
    def read_attendance_record_by_id(cls, attendance_id):
        """Read attendance record by provided attendance id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `attendances` WHERE `attendance_id` = ?;"
        cursor.execute(query, (attendance_id,))
        attendance = cursor.fetchall()
        conn.close()
        return attendance

    @classmethod
    def read_attendance_record_list_by_student_id(cls, student_id):
        """Read attendance record list by provided studen id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `attendances` WHERE `user_id` = ?;"
        cursor.execute(query, (student_id,))
        attendance = cursor.fetchall()
        conn.close()
        return attendance

    @classmethod
    def read_attendance_record_list(cls):
        """Read attendance record list"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `attendances`;"
        cursor.execute(query)
        attendance_list = cursor.fetchall()
        conn.close()
        return attendance_list

    @classmethod
    def read_overall_grade(cls, student_id):
        """Read overall grade by provided student id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT round(avg(100.0*submissions.points/assignments.max_points),2) FROM submissions " \
                "INNER JOIN assignments ON submissions.assignment_id=assignments.assignment_id " \
                "WHERE `user_id`=?;"
        cursor.execute(query, (student_id,))
        overall_grade = cursor.fetchall()[0][0]
        conn.close()
        return overall_grade

    @classmethod
    def read_overall_attendance(cls, student_id):
        """Read overall attendance by provided student id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT round(avg(100.0*status), 2) from attendances WHERE `user_id`=?;"
        cursor.execute(query, (student_id,))
        overall_attendance = cursor.fetchall()[0][0]
        conn.close()
        return overall_attendance

    @classmethod
    def read_team_list(cls):
        """Read team record list"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `teams`;"
        cursor.execute(query)
        team_list = cursor.fetchall()
        conn.close()
        return team_list

    @classmethod
    def read_team_membership(cls, student_id):
        """Read student team id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT `team_id` FROM `members` WHERE `student_id` = ?;"
        cursor.execute(query, (student_id,))
        try:
            team_id = cursor.fetchall()[0][0]
        except IndexError:
            team_id = None
        conn.close()
        print(team_id)
        return team_id


    @classmethod
    def update_name(cls, user_id, name):
        """Update name in user record by provided user id"""
        query = "UPDATE `users` SET `name` = ? WHERE `user_id` = ?;"
        args = (name, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_mail(cls, user_id, new_mail):
        """Update mail in user record by provided user id"""
        query = "UPDATE `users` SET `mail` = ? WHERE `user_id` = ?;"
        args = (new_mail, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_password(cls, user_id, new_password):
        """Update password in user record by provided user id"""
        query = "UPDATE `users` SET `password` = ? WHERE `user_id` = ?;"
        args = (new_password, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_attendance(cls, user_id, date, status):
        """Update status in attendance record by provided user id and date"""
        query = "UPDATE `attendances` SET `status` = ? WHERE `user_id` = ? AND `date` = ?;"
        args = (status, user_id, date)
        cls.execute_query(query, args)

    @classmethod
    def update_grade(cls, user_id, assignment_id, points):
        """Update points in submission record by provided user id and assignment id"""
        query = "UPDATE `submissions` SET `points` = ? WHERE `assignment_id` = ? AND `user_id` = ?;"
        args = (points, assignment_id, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_title(cls, assignment_id, title):
        """Update title of assignment by provided assignment id"""
        query = "UPDATE `assignments` SET `title` = ? WHERE `assignment_id` = ?;"
        args = (title, assignment_id)
        cls.execute_query(query, args)

    @classmethod
    def update_content(cls, assignment_id, content):
        """Update content of assignment by provided assignment id"""
        query = "UPDATE `assignments` SET `content` = ? WHERE `assignment_id` = ?;"
        args = (content, assignment_id)
        cls.execute_query(query, args)

    @classmethod
    def update_due_date(cls, assignment_id, due_date):
        """Update due date of assignment by provided assignment id"""
        query = "UPDATE `assignments` SET `due_date` = ? WHERE `assignment_id` = ?;"
        args = (due_date, assignment_id)
        cls.execute_query(query, args)

    @classmethod
    def update_max_points(cls, assignment_id, max_points):
        """Update max points of assignment by provided assignment id"""
        query = "UPDATE `assignments` SET `max_points` = ? WHERE `assignment_id` = ?;"
        args = (max_points, assignment_id)
        cls.execute_query(query, args)

    @classmethod
    def update_assignment(cls, assignment_id, is_team, title, content, due_date, max_points):
        query = "UPDATE `assignments` SET `title` = ?, `is_team` = ?, `content` = ?, `due_date` = ?, `max_points` = ? WHERE `assignment_id` = ?;"
        args = (title, is_team, content, due_date, max_points, assignment_id)
        cls.execute_query(query, args)

    @classmethod
    def update_team_name(cls, team_id, new_name):
        query = "UPDATE `teams` SET `name` = ? WHERE `id` = ?;"
        args = (new_name, team_id)
        cls.execute_query(query, args)

    @classmethod
    def update_student_team_id(cls, team_id, student_id):
        query = "UPDATE `members` SET `team_id` = ? WHERE `student_id` = ?;"
        args = (team_id, student_id)
        cls.execute_query(query, args)

    @classmethod
    def delete_assignment_record(cls, assignment_id):
        """Delete assignment record by provided assignment id"""
        query = "DELETE FROM assignments WHERE assignment_id = ?"
        args = assignment_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_attendance_record(cls, attendance_id):
        """Delete attendance record by provided attendance id"""
        query = "DELETE FROM attendances WHERE attendance_id = ?"
        args = attendance_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_submission_record(cls, submission_id):
        """Delete submission record by provided submission id"""
        query = "DELETE FROM submissions WHERE submission_id = ?"
        args = submission_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_user_record(cls, user_id):
        """Delete user record by provided user id"""
        query = "DELETE FROM users WHERE user_id = ?"
        args = user_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_member_record(cls, student_id):
        """Delete member record from database"""
        query = 'DELETE FROM `members` WHERE student_id = ?;'
        args = student_id
        return cls.execute_query(query, (args,))

    @classmethod
    def delete_user_attendance_record(cls, user_id):
        """Delete attendance record by provided user id"""
        query = "DELETE FROM attendances WHERE user_id = ?"
        args = user_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_user_submission_record(cls, user_id):
        """Delete submission record by provided user id"""
        query = "DELETE FROM submissions WHERE user_id = ?"
        args = user_id
        cls.execute_query(query, (args,))

    @classmethod
    def delete_assignment_submission_record(cls, assignment_id):
        """Delete submission record by provided assignment id"""
        query = "DELETE FROM submissions WHERE assignment_id = ?"
        args = assignment_id
        cls.execute_query(query, (args,))
