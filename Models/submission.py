from db import DB


class Submission:
    """This is class representing student submission for Assignment graded by Mentor."""

    def __init__(self, submission_id, assignment_id, user_id, content, date, points=None):
        self.id = submission_id
        self.assignment_id = assignment_id
        self.user_id = user_id
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
        assignment_data = DB.read_assignment_record_list()
        return [Assignment(*assignment) for assignment in assignment_data]

    def get_id(self):
        """Returns submission instance id"""
        return self.id

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

    def set_grade_submission(self, points, user_id):
        """
        Sets grade to submission.
        """
        DB.update_grade(user_id, self.assignment.get_id(), points)
