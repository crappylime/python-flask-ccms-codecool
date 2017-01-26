class User:

    user_list = []

    def __init__ (self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password
        User.user_list.append(self)

    @classmethod
    def get_user_list(cls):
        return cls.user_list

    def get_name(self):
        return self.name

    def get_mail(self):
        return self.mail

    def get_password(self):
        return self.password

    def get_class_name(self):
        return self.__class__.__name__

    def set_name(self, new_name):
        self.name = new_name

    def set_mail(self, new_mail):
        self.mail = new_mail

    def set_password(self, new_password):
        self.password = new_password


class Student(User):

    student_list = []

    def __init__(self, name, mail, password):
        User.__init__(self, name, mail, password)
        self.grade_list = []
        self.attendance_list = []
        self.submission_list = []

    @classmethod
    def add_student(cls, name, mail, password):
        cls.student_list.append(Student(name, mail, password))

    def edit_student(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password

    @classmethod
    def remove_student(cls, name):
        for student in cls.student_list:
            if student.name == name:
                cls.student_list.remove(student)

    @classmethod
    def get_student_list(cls):
        return cls.student_list

    @classmethod
    def get_student(cls, name):
        for student in cls.student_list:
            if student.name == name:
                return student

    @classmethod
    def get_grade(cls, name, assignment_title):
        for student in cls.student_list:
            if student.name == name:
                for submission in student.submission_list:
                    if submission.title == assignment_title:
                        return submission.grade
                    else:
                        print('there is no such submission added by {}'.format(student.name))
            else:
                print('there is no such student in students list')


class Employee(User):
    pass


class Mentor(Employee):

    mentor_list = []

    def __init__(self, name, mail, password):
        super().__init__(name, mail, password)

    @classmethod
    def add_mentor(cls, name, mail, password):
        cls.mentor_list.append(Mentor(name, mail, password))

    def edit_mentor(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password

    @classmethod
    def remove_mentor(cls, name):
        for mentor in cls.mentor_list:
            if mentor.name == name:
                cls.mentor_list.remove(mentor)

    @classmethod
    def get_list_mentor(cls):
        return cls.mentor_list

    @classmethod
    def get_mentor(cls, name):
        for mentor in cls.mentor_list:
            if mentor.name == name:
                return mentor


class Boss(Employee):

    boss_list = []

    def __init__(self, name, mail, password):
        super().__init__(name, mail, password)

    @classmethod
    def add_boss(cls, name, mail, password):
        cls.boss_list.append(Boss(name, mail, password))


class Staff(Employee):

    staff_list = []

    def __init__(self, name, mail, password):
        super().__init__(name, mail, password)

    @classmethod
    def add_staff(cls, name, mail, password):
        cls.staff_list.append(Staff(name, mail, password))