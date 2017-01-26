from Models.user import *


class Assignment:
    """This is class representing Assignment given by Mentor."""

    assignment_list = []

    def __init__(self, title, content, due_date, max_points):
        self.title = title
        self.content = content
        self.due_date = due_date
        self.max_points = max_points
        self.submission_list = []

    def __str__(self):
        info = self.__class__.__name__

        for key, value in self.__dict__.items():
            info += ", {}: {}".format(key, value)

        return info

    @classmethod
    def add_assignment(cls, title, content, due_date, max_points):
        """
        Adds assignment to assignments list.
        """
        cls.assignment_list.append(Assignment(title, content, due_date, max_points))

    @classmethod
    def get_assignment(cls, title):
        """
        Returns assignment object.

        Raises:
            NameError: If assignment's title was NOT found.
        """
        for item in cls.assignment_list:
            if item.title == title:
                return item
        raise NameError("There's no assignment with given title")

    def get_submission(self, owner_name):
        """
        Returns submission object.

        Raises:
            NameError: If submission's title was NOT found.
        """
        student = Student.get_student(owner_name)
        for submission in self.submission_list:
            if submission.owner == student:
                return submission
        raise NameError("There's no submission with given title")

    def edit_assignment(self, title, due_date, max_points):
        """
        Returns edited assignment.
        """
        self.title = title
        self.due_date = due_date
        self.max_points = max_points

    @classmethod
    def remove_assignment(cls, assignment):
        """
        Removes assignment.
        """
        cls.assignment_list.remove(assignment)

    def set_grade_submission(self, points, owner_name):
        """
        Sets grade to submission.

        Raises:
            TypeError: If points limit has been exceeded.
            NameError: There's no submission with given student name.
        """
        try:
            points = int(points)
        except TypeError:
            raise TypeError('An argument must be integer type')

        if points not in range(0, self.max_points):
            raise ValueError("Points limit has been exceeded")

        student = Student.get_student(owner_name)
        for submission in self.submission_list:
            if submission.owner == student:
                submission.points = points
                return submission.points
            raise NameError("There's no submission with given student name")

    @classmethod
    def get_list_assignmnent(cls):
        """
        Returns assignments list.
        """
        return cls.assignment_list

    def get_list_submission(self):
        """
        Returns submissions list.
        """
        return self.submission_list
