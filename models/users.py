from db_controller import DB
from models.teams import Team


class User:
    """Parent class for all user instances - represents all users"""

    def __init__(self, user_id, name, mail, password):
        """Attributes for all users - id, name, e-mail, password"""
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
    def get_user_list(cls):
        """
        Returns list with user objects
        :return:
            user_list: list
        """
        return cls.create_user_list()

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
        pairs = {"student": Student, "mentor": Mentor, "staff": Staff, "boss": Boss}
        args = DB.read_user_record_by_user_id(user_id)
        return pairs[args[0][-1]](*args[0][:-1])

    @classmethod
    def create_user_list(cls):
        """
        Creates list of user instances
        :return:
            user_list: list
        """
        user_list = []
        users_data = DB.read_user_record_list()
        pairs = {"student": Student, "mentor": Mentor, "staff": Staff, "boss": Boss}
        for user in users_data:
            user_list.append(pairs[user[-1]](*user[:-1]))

        return user_list

    @classmethod
    def get_mails_list(cls):
        mails_list = []
        for user in cls.get_user_list():
            mails_list.append(user.mail)
        return mails_list

    @classmethod
    def create_user_list_by_role(cls, role):
        """
        Creates list of user instances
        :return:
            user_list: list
        """
        user_list = []
        users_data = DB.read_user_record_list_by_role(role)
        pairs = {"student": Student, "mentor": Mentor, "staff": Staff, "boss": Boss}
        for user in users_data:
            user_list.append(pairs[user[-1]](*user[:-1]))

        return user_list

    @classmethod
    def create_user_list_by_id_list(cls, id_list):
        """
        Creates list of user instances
        :return:
            user_list: list
        """
        user_list = []
        users_data = DB.read_user_record_list_by_id(id_list)
        pairs = {"student": Student, "mentor": Mentor, "staff": Staff, "boss": Boss}
        for user in users_data:
            user_list.append(pairs[user[-1]](*user[:-1]))

        return user_list

    @classmethod
    def add_user(cls, name, mail, password, role=None):
        values = (name, mail, password, role if role else cls.get_class_name().lower())
        new_user_id = DB.create_user_record(values)
        new_user = cls.get_user_by_id(new_user_id)
        return new_user

    @classmethod
    def temporary_user(cls, name, mail, role=None):
        roles = {"student": Student, "mentor": Mentor, "staff": Staff, "boss": Boss}
        return roles[role](name=name, mail=mail, password=None, user_id=None)

    @classmethod
    def get_class_name(cls):
        """Returns user instance subclass name"""
        return cls.__name__

    def get_name(self):
        """Returns user instance name"""
        return self.name

    def get_id(self):
        """Returns user instance id"""
        return self.id

    def get_mail(self):
        """Returns user instance mail"""
        return self.mail

    def get_password(self):
        """Returns user instance password"""
        return self.password

    def get_user_class_name(self):
        """Returns user instance subclass name"""
        return self.__class__.__name__

    def set_name(self, new_name):
        """Sets users name"""
        self.name = new_name
        #DB.update_name(self.get_id(), new_name)

    def set_mail(self, new_mail):
        """Sets users mail"""
        self.mail = new_mail
        #DB.update_mail(self.get_id(), new_mail)

    def set_password(self, new_password):
        """Sets users password"""
        self.password = new_password
        #DB.update_password(self.get_id(), new_password)

    def save_changes(self):
        DB.update_user(self.id, self.name, self.mail, self.password)

    @classmethod
    def remove_user(cls, user_id):
        """Removes user instance from user list"""
        DB.delete_user_record(user_id)
        DB.delete_user_attendance_record(user_id)
        DB.delete_user_submission_record(user_id)

    def remove(self):
        """Removes user instance from user list"""
        DB.delete_user_record(self.id)
        DB.delete_user_attendance_record(self.id)
        DB.delete_user_submission_record(self.id)


class Student(User):
    """Class that represent students"""

    @property
    def submission_list(self):
        return Submission.get_submission_list_by_user_id(self.id)

    @property
    def overall_grade(self):
        return Submission.get_overall_grade(self.id)

    @property
    def attendance_list(self):
        return Attendance.get_attendance_list_by_student_id(self.id)

    @property
    def overall_attendance(self):
        return Attendance.get_overall_attendance(self.id)

    def get_submission_list(self):
        return self.submission_list

    def get_overall_grade(self):
        return self.overall_grade

    def get_attendance_list(self):
        return self.attendance_list

    def get_overall_attendance(self):
        return self.overall_attendance


class Employee(User):
    """Class that represent employees"""


class Mentor(Employee):
    """Class that represent mentors"""


class Boss(Employee):
    """Class that represent boss"""


class Staff(Employee):
    """Class that represent staff employees"""
