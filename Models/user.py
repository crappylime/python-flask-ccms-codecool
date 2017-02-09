import sqlite3
from db import *


class User:
    """Parent class for all user instances - represents all users"""

    user_list = []  # collects all user instances - needed for login and csv export

    def __init__(self, user_id, name, mail, password):
        """Attributes for all users - name, e-mail, password"""
        self.id = user_id
        self.name = name
        self.mail = mail
        self.password = password
        User.user_list.append(self)

    @classmethod
    def get_user_list(cls):
        """Returns list with all users instances"""
        return cls.user_list

    @classmethod
    def get_user_by_id(cls, user_id):
        retur

    def get_id(self):
        """Returns user id"""
        return self.id

    def get_name(self):
        """Returns user instance name"""
        return self.name

    def get_mail(self):
        """Returns user instance mail"""
        return self.mail

    def get_password(self):
        """Returns user instance password"""
        return self.password

    def get_class_name(self):
        """Returns user instance subclass name"""
        return self.__class__.__name__

    def set_name(self, new_name):
        """Sets users name"""
        self.name = new_name
        DB.update_name(self.get_id(), new_name)

    def set_mail(self, new_mail):
        """Sets users mail"""
        self.mail = new_mail
        DB.update_mail(self.get_id(), new_mail)

    def set_password(self, new_password):
        """Sets users password"""
        self.password = new_password
        DB.update_password(self.get_id(), new_password)


class Student(User):
    """Class that represent students"""
    student_list = []  # collects all student instances

    def __init__(self, user_id, name, mail, password):
        """Student has additional attributes - grade list, attendance list, submission list"""
        super().__init__(user_id, name, mail, password)
        self.grade_list = []
        self.attendance_list = []  # collect all attendance instances
        self.submission_list = []  # collect all submissions sending by student

    @classmethod
    def add_student(cls, name, mail, password):
        """Adds news student instance and appends its to student list"""
        cls.student_list.append(Student(name, mail, password))

    @classmethod
    def remove_student(cls, name):
        """Removes student instance from student list"""
        for student in cls.student_list:
            if student.name == name:
                cls.student_list.remove(student)

    @classmethod
    def get_student_list(cls):
        """Returns list with students"""
        student_list = []
        con = sqlite3.connect('Data/ccms.db')
        table = con.execute("SELECT * FROM `users`;")
        for row in table:
            student_list.append(cls(*row[1:]))
        return student_list

    @classmethod
    def get_student(cls, name):
        """Searching in student list and returns student instance with given name"""
        for student in cls.student_list:
            if student.name == name:
                return student

    @classmethod
    def get_grade(cls, name, assignment_title):
        """Returns grade from assignment with title 'assignment_title' submit by student with name 'name'"""
        for student in cls.student_list:
            if student.name == name:
                for submission in student.submission_list:
                    if assignment_title:
                        return submission.points
                    else:
                        print('there is no such submission added by {}'.format(student.name))
            else:
                print('there is no such student in students list')


class Employee(User):
    """Class that represent employees"""
    pass


class Mentor(Employee):
    """Class that represent mentors"""
    mentor_list = []  # collects all mentors instances

    def __init__(self, user_id, name, mail, password):
        """init from user class"""
        super().__init__(user_id, name, mail, password)

    @classmethod
    def add_mentor(cls, name, mail, password):
        """Adds news mentor instance and appends its to mentors list"""
        cls.mentor_list.append(Mentor(name, mail, password))

    @classmethod
    def remove_mentor(cls, name):
        """Removes mentor instance from mentor list"""
        for mentor in cls.mentor_list:
            if mentor.name == name:
                cls.mentor_list.remove(mentor)

    @classmethod
    def get_list_mentor(cls):
        """Returns list with mentors"""
        return cls.mentor_list

    @classmethod
    def get_mentor(cls, name):
        """Searching in mentor list and returns mentor instance with given name"""
        for mentor in cls.mentor_list:
            if mentor.name == name:
                return mentor


class Boss(Employee):
    """Class that represent boss"""
    boss_list = []  # collects all boss instances

    def __init__(self, user_id, name, mail, password):
        """init from user class"""
        super().__init__(user_id, name, mail, password)

    @classmethod
    def add_boss(cls, name, mail, password):
        """Adds news boss instance and appends its to boss list"""
        cls.boss_list.append(Boss(name, mail, password))

    @classmethod
    def remove_boss(cls, name):
        """Removes boss instance from boss list"""
        for boss in cls.boss_list:
            if boss.name == name:
                cls.boss_list.remove(boss)

    @classmethod
    def get_boss_list(cls):
        """Returns list with boss instances"""
        return cls.boss_list

    @classmethod
    def get_boss(cls, name):
        """Searching in boss list and returns boss instance with given name"""
        for boss in cls.boss_list:
            if boss.name == name:
                return boss


class Staff(Employee):
    """Class that represent staff employees"""
    staff_list = []  # collects all staff instances

    def __init__(self, user_id, name, mail, password):
        """init from user class"""
        super().__init__(user_id, name, mail, password)

    @classmethod
    def add_staff(cls, name, mail, password):
        """Adds news staff instance and appends its to staff list"""
        cls.staff_list.append(Staff(name, mail, password))

    @classmethod
    def remove_staff(cls, name):
        """Removes staff instance from staff list"""
        for staff in cls.staff_list:
            if staff.name == name:
                cls.staff_list.remove(staff)

    @classmethod
    def get_staff_list(cls):
        """Returns list with staff instances"""
        return cls.staff_list

    @classmethod
    def get_staff(cls, name):
        """Searching in staff list and returns staff instance with given name"""
        for staff in cls.staff_list:
            if staff.name == name:
                return staff
