from Models.assignment import *
from Models.user import *


class Submission:
    """This is class representing student submission for Assignment graded by Mentor."""

    def __init__(self, assignment, owner, content, date, points=None):
        self.assignment = assignment
        self.owner = owner
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


    def get_owner(self):
        """
        :return:
            obj: submission owner's object
        """
        return self.owner

    def get_assignment(self):
        """
        :return:
            obj: assignment object
        """
        return self.assignment

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
