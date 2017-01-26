from Models.assignment import *
from Models.user import *


class Submission:
    """This is class representing student submission for Assignment graded by Mentor."""

    def __init__(self, assignment, owner, content, date, points=None):
        self.assignment_title = assignment
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
    def add_submission(cls, content, date, assignment_title, owner_name, points=None):
        """
        Adds submission to Assignment and Student submissions list.
        """
        student = Student.get_student(owner_name)

        assignment = Assignment.get_assignment(assignment_title)
        submission = Submission(assignment_title, student, content, date, points)
        assignment.submission_list.append(submission)

        student.submission_list.append(submission)
