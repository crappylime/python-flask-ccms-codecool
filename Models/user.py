from db import DB


class User:
    """Parent class for all user instances - represents all users"""

    def __init__(self, user_id, name, mail, password):
        """Attributes for all users - name, e-mail, password"""
        self.id = user_id
        self.name = name
        self.mail = mail
        self.password = password

    @classmethod
    def get_user_by_id(cls, user_id):
        """
        Returns user object.
        :return:
            user: object
        """
        return cls.create_user(user_id)

    @classmethod
    def get_user_list_by_role(cls, role):
        """
        Returns list with user objects
        :return:
            user_list: list
        """
        return cls.create_user_list_by_role(role)

    @classmethod
    def get_user_list_by_id_list(cls, id_list):
        """
        Returns list with user objects
        :return:
            user_list: list
        """
        return cls.create_user_list_by_id_list(id_list)

    @classmethod
    def create_user(cls, user_id):
        """
        Creates instance of user
        :return:
            user: object
        """
        args = DB.read_user_record_by_user_id(user_id)
        return User(*args[0])

    @classmethod
    def create_user_list_by_role(cls, role):
        """
        Creates list of user instances
        :return:
            user_list: list
        """
        users_data = DB.read_user_record_list_by_role(role)
        return [User(*user) for user in users_data]

    @classmethod
    def create_user_list_by_id_list(cls, id_list):
        """
        Creates list of user instances
        :return:
            user_list: list
        """
        users_data = DB.read_user_record_list_by_id(id_list)
        return [User(*user) for user in users_data]

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

    def set_mail(self, new_mail):
        """Sets users mail"""
        self.mail = new_mail

    def set_password(self, new_password):
        """Sets users password"""
        self.password = new_password


class Student(User):
    """Class that represent students"""

    def __init__(self, user_id, name, mail, password):
        """Student has additional attributes - grade list, attendance list, submission list"""
        super().__init__(self, user_id, name, mail, password)

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
    def __init__(self, user_id, name, mail, password):
        """init from user class"""
        super().__init__(user_id, name, mail, password)


class Mentor(Employee):
    """Class that represent mentors"""

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

class Boss(Employee):
    """Class that represent boss"""

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

class Staff(Employee):
    """Class that represent staff employees"""

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
