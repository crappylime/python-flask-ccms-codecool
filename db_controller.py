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
    def execute_select_query(cls, query, args):
        """Execute select query and return fetchall"""
        conn = cls.connect()
        cur = conn.cursor()
        cur.execute(query, args)
        return cur.fetchall()

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
    def create_checkpoint_record(cls, values):
        """Add checkpoint record to database"""
        query = 'INSERT INTO checkpoints (`student_id`, `date`, `title`, `card`) VALUES (?, ?, ?, ?);'
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
    def read_team_record_by_name(cls, team_name):
        """Read team record by provided team name"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `teams` WHERE `name` = ?;"
        cursor.execute(query, (team_name,))
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
    def read_menu_record_list_by_upper_menu_id(cls, upper_menu_id):
        """"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT id, `name`, url_for, url_for_args, `position`, upper_menu_id FROM menus WHERE upper_menu_id = ?"
        cursor.execute(query, (upper_menu_id,))
        submenu_list = cursor.fetchall()
        conn.close()
        return submenu_list

    @classmethod
    def read_menu_by_name(cls, menu_name):
        """"""
        print(menu_name)
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT id, `name`, url_for, url_for_args, `position`, upper_menu_id FROM menus WHERE url_for = ?"
        cursor.execute(query, (menu_name,))
        menu_data = cursor.fetchall()[0]
        print(menu_data)
        conn.close()
        return menu_data

    @classmethod
    def read_menu_permission(cls, menu_id):
        """"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT mentor_perm, student_perm, staff_perm, boss_perm FROM menus WHERE id = ?"
        cursor.execute(query, (menu_id,))
        perm_list = list(cursor.fetchall()[0])
        conn.close()
        print(perm_list)
        return perm_list



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
    def read_checkpoint_record_by_id(cls, checkpoint_id):
        """Read checkpoint record by provided checkpoint id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `checkpoints` WHERE `checkpoint_id` = ?;"
        cursor.execute(query, (checkpoint_id,))
        checkpoint = cursor.fetchall()
        conn.close()
        return checkpoint

    @classmethod
    def read_checkpoint_record_list_by_student_id(cls, student_id):
        """Read checkpoint record list by provided studen id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `checkpoints` WHERE `student_id` = ?;"
        cursor.execute(query, (student_id,))
        checkpoint = cursor.fetchall()
        conn.close()
        return checkpoint

    @classmethod
    def read_checkpoint_record_list_by_title(cls, title):
        """Read checkpoint record list by provided title"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `checkpoints` WHERE `title` = ?;"
        cursor.execute(query, (title,))
        checkpoint = cursor.fetchall()
        conn.close()
        return checkpoint

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
    def read_attendance_record_list_by_date(cls, date):
        """Read attendance record list by provided date"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `attendances` WHERE `date` = ?;"
        cursor.execute(query, (date,))
        attendance = cursor.fetchall()
        conn.close()
        return attendance

    @classmethod
    def read_checkpoint_record_list_by_date(cls, date):
        """Read checkpoint record list by provided date"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM `checkpoints` WHERE `date` = ?;"
        cursor.execute(query, (date,))
        checkpoint = cursor.fetchall()
        conn.close()
        return checkpoint

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
    def read_checkpoint_record_list(cls):
        """Read checkpoint record list"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM checkpoints;"
        cursor.execute(query)
        checkpoint_list = cursor.fetchall()
        conn.close()
        return checkpoint_list

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
    def read_overall_checkpoint(cls, student_id):
        """Read overall checkpoint by provided student id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT round(avg(100.0*card), 2) from checkpoints WHERE `student_id`=?;"
        cursor.execute(query, (student_id,))
        overall_checkpoint = cursor.fetchall()[0][0]
        conn.close()
        return overall_checkpoint

    @classmethod
    def read_all_overall_attendance(cls):
        """Read overall attendance by provided student id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT round(avg(100.0*status), 2) from attendances;"
        cursor.execute(query)
        overall_attendance = cursor.fetchall()[0][0]
        conn.close()
        return overall_attendance

    @classmethod
    def read_all_overall_checkpoint(cls):
        """Read overall checkpoint by provided student id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT round(avg(100.0*card), 2) from checkpoints;"
        cursor.execute(query)
        overall_checkpoint = cursor.fetchall()[0][0]
        conn.close()
        return overall_checkpoint

    @classmethod
    def read_overall_attendance_by_date(cls, date):
        """Read overall attendance by provided student id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT round(avg(100.0*status), 2) from attendances WHERE `date` = ?;"
        args = (date,)
        cursor.execute(query, args)
        overall_attendance = cursor.fetchall()[0][0]
        conn.close()
        return overall_attendance

    @classmethod
    def read_overall_checkpoint_by_date(cls, date):
        """Read overall checkpoint by provided student id"""
        conn = cls.connect()
        cursor = conn.cursor()
        query = "SELECT round(avg(100.0*card), 2) from checkpoints WHERE `date` = ?;"
        args = (date,)
        cursor.execute(query, args)
        overall_checkpoint = cursor.fetchall()[0][0]
        conn.close()
        return overall_checkpoint


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
    def update_checkpoint(cls, user_id, title, status):
        """Update status in checkpoint record by provided user id and date"""
        query = "UPDATE `checkpoints` SET `card` = ? WHERE `student_id` = ? AND `title` = ?;"
        args = (status, user_id, title)
        cls.execute_query(query, args)

    @classmethod
    def update_grade(cls, user_id, assignment_id, points):
        """Update points in submission record by provided user id and assignment id"""
        query = "UPDATE `submissions` SET `points` = ? WHERE `assignment_id` = ? AND `user_id` = ?;"
        args = (points, assignment_id, user_id)
        cls.execute_query(query, args)

    @classmethod
    def update_user(cls, user_id, name, mail, password):
        query = "UPDATE `users` SET `name` = ?, `mail` = ?, `password` = ? WHERE `user_id` = ?;"
        args = (name, mail, password, user_id)
        cls.execute_query(query, args)


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
    def update_assignment(cls, assignment_id, title, is_team, content, due_date, max_points):
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
        cls.execute_query(query, (args,))

    @classmethod
    def delete_team_record(cls, team_id):
        """Delete team record from database"""
        query = 'DELETE FROM `members` WHERE team_id = ?;'
        args = team_id
        cls.execute_query(query, (args,))
        query = 'DELETE FROM `teams` WHERE id = ?;'
        cls.execute_query(query, (args,))

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
