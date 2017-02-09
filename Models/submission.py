from db import DB


class Submission:
    """This is class representing student submission for Assignment graded by Mentor."""

    def __init__(self, submission_id, assignment_id, user_id, content, date, points=None):
        self.id = submission_id
        self.assignment = Assignment.get_assigment_by_id(assignment_id)
        self.user = User.get_user_by_id(user_id)
        self.content = content
        self.date = date
        self.points = points

    def __str__(self):
        info = self.__class__.__name__

        for key, value in self.__dict__.items():
            info += ", {}: {}".format(key, value)

        return info

    @classmethod
    def add_submission(cls, content, date, assignment_id, student_id):
        values = (assignment_id, student_id, content, date)
        new_submission_id = DB.create_submission_record(values)
        new_submission = cls.get_submission_by_id(new_submission_id)
        return new_submission

    @classmethod
    def get_submission_by_id(cls, submission_id):
        pass

    @classmethod
    def get_submission_by_user_id(cls, user_id):
        """
        Returns submission object.

       :return:
            submission: object
        """
        return cls.create_submission_by_user_id(user_id)

    def get_submission_by_assignment_id(cls, assignment_id):
        """
        Returns submission object.

       :return:
            submission: object
        """
        return cls.create_submission_by_assignment_id(assignment_id)

    @classmethod
    def get_submission_list(cls):
        """
        Returns list of submissions instances
        :return:
            list: list of submissions instances
        """
        return cls.create_submission_list()

    @classmethod
    def create_submission_by_user_id(cls, user_id):
        """
        Creates instance of user
        :return:
            user: object
        """
        args = DB.read_assignment_record_by_id(user_id)
        return Assignment(*args[0])

    def create_submission_by_assignment_id(cls, assignment_id):
        """
        Creates instance of user
        :return:
            user: object
        """
        args = DB.read_assignment_record_by_id(assignment_id)
        return Assignment(*args[0])

    @classmethod
    def create_submission_list(cls):
        """
        Creates list of user instances
        :return:
            user_list: list
        """
        assignment_data = DB.read_assignment_record_list()
        return [Assignment(*assignment) for assignment in assignment_data]

    def get_id(self):
        """Returns submission instance id"""
        return self.id

    def get_user_id(self):
        """
        :return:
            obj: submission owner's object
        """
        return self.user_id

    def get_assignment_id(self):
        """
        :return:
            obj: assignment object
        """
        return self.assignment_id

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

    def get_points(self):
        """
        :return:
            int: point assigned to submission
        """
        return self.points
