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
    def add_submission(cls, content, date, assignment_title, owner_name, points=None):
        """
        Adds submission to Assignment and Student submissions list.
        """
        student = Student.get_student(owner_name)

        assignment = Assignment.get_assignment(assignment_title)

        unique = True

        for item in student.submission_list:
            if item.assignment == assignment:
                unique = False

        if unique is True:
            submission = Submission(assignment, student, content, date,
                                    int(points) if type(points) == str and len(points) > 0 else None)
            assignment.submission_list.append(submission)
            student.submission_list.append(submission)
        else:
            raise NameError('This assignment has already been submitted!')

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
