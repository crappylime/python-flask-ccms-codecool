from db_controller import DB
import models.users
import models.assignments
import time


class Submission:
    """This is class representing student submission for Assignment graded by Mentor."""

    def __init__(self, submission_id, assignment_id, user_id, content, date, points=None):
        self.id = submission_id
        self.assignment = models.assignments.Assignment.get_assignment_by_id(assignment_id)
        self.student = models.users.User.get_user_by_id(user_id)
        self.content = content
        self.date = date
        self.points = points

    def __str__(self):
        info = self.__class__.__name__

        for key, value in self.__dict__.items():
            info += ", {}: {}".format(key, value)

        return info

    @classmethod
    def get_submission_by_id(cls, submission_id):
        """
        Returns submission object.

       :return:
            submission: object
        """
        return cls.create_submission_by_id(submission_id)

    @classmethod
    def get_submission_list_by_user_id(cls, user_id):
        """
        Returns submission list of instances.

       :return:
            submission_list: list
        """
        return cls.create_submission_list_by_user_id(user_id)

    @classmethod
    def get_submission_list_by_assignment_id(cls, assignment_id):
        """
        Returns submission list of instances.

       :return:
            submission_list: list
        """
        return cls.create_submission_list_by_assignment_id(assignment_id)

    @classmethod
    def get_submission_list(cls):
        """
        Returns list of submissions instances
        :return:
            list: list of submissions instances
        """
        return cls.create_submission_list()

    @classmethod
    def get_overall_grade(cls, student_id):
        """
        Returns overall grade
        :return:
           str: overall grade
        """
        return cls.create_overall_grade(student_id)

    @classmethod
    def create_submission_by_id(cls, submission_id):
        """
        Creates instance of user
        :return:
            user: object
        """
        args = DB.read_submission_record_by_id(submission_id)
        return Submission(*args[0])

    @classmethod
    def create_submission_list_by_user_id(cls, user_id):
        """
        Creates instance of user
        :return:
            user: object
        """
        submission_data = DB.read_submission_record_list_by_user_id(user_id)
        return [Submission(*submission) for submission in submission_data]

    @classmethod
    def create_submission_list_by_assignment_id(cls, assignment_id):
        """
        Creates instance of user
        :return:
            user: object
        """
        submission_data = DB.read_submission_record_list_by_assignment_id(assignment_id)
        return [Submission(*submission) for submission in submission_data]

    @classmethod
    def create_submission_list(cls):
        """
        Creates list of user instances
        :return:
            user_list: list
        """
        submission_data = DB.read_submission_record_list()
        return [Submission(*submission) for submission in submission_data]

    @classmethod
    def create_overall_grade(cls, student_id):
        """
        Create overall_grade
        :return:
            overall grade: str
        """
        return DB.read_overall_grade(student_id)

    @classmethod
    def add_submission(cls, assignment_id, student_id, content):
        date = time.strftime("%Y-%m-%-d %H:%M")
        values = (assignment_id, student_id, content, date)
        new_submission_id = DB.create_submission_record(values)
        new_submission = cls.get_submission_by_id(new_submission_id)
        return new_submission

    def get_date(self):
        """
        :return:
            str: date of submission
        """
        return self.date

    def get_content(self):
        """
        :return:
            str: content of submission
        """
        return self.content

    def get_id(self):
        """return submission id"""
        return self.id

    def get_points(self):
        """
        :return:
            int: point assigned to submission
        """
        return self.points

    @classmethod
    def set_grade_submission(cls, user_id, assignment_id, points):
        """
        Sets grade to submission.
        """
        DB.update_grade(user_id, assignment_id, points)

    def get_assignment(self):
        """ Return assignment object"""
        return self.assignment

    def get_student(self):
        return self.student
