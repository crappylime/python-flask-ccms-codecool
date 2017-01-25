from assignment import Assignment
from Student import *


class Submission:
    """This is class representing student submission for Assignment graded by Mentor."""

    def __init__(self, title, content, date, points=None):
        self.title = title
        self.content = content
        self.date = date
        self.points = points

    def __str__(self):
        info = self.__class__.__name__

        for key, value in self.__dict__.items():
            info += ", {}: {}".format(key, value)

        return info

    @classmethod
    def add_submission(cls, title, content, date, assignment_title, owner_name):
        """
        Adds submission to submissions list.
        """
        submission = Submission(title, content, date)
        assignment = Assignment.get_assignment(assignment_title)
        assignment.submission_list.append(submission)

        student = Student.get_student(owner_name)
        student.submission_list.append(submission)
