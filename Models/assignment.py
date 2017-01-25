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

    def get_submission(self, submission_title):
        """
        Returns submission object.

        Raises:
            NameError: If submission's title was NOT found.
        """
        for submission in self.submission_list:
            if submission.title == submission_title:
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

    def set_grade_submission(self, points, student_name):
        """
        Sets grade to submission.

        Raises:
            TypeError: If points limit has been exceeded.
        """
        if points < self.max_points:
            return self.points = points
        raise TypeError("Points limit has been exceeded")

    @classmethod
    def get_list_assignmnent():
        """
        Returns assignments list.
        """
        return cls.assignment_list

    def get_list_submission(self):
        """
        Returns submissions list.
        """
        return self.submission_list
