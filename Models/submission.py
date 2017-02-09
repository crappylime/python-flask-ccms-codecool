from db import DB
from Models.assignment import Assignment


class Submission:
    """This is class representing student submission for Assignment graded by Mentor."""

    def __init__(self, submission_id, assignment_id, user_id, content, date, points=None):
        self.id = submission_id
        self.assignment = Assignment.get_assignment_by_id(assignment_id)
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
        submission_data = DB.read_submission_record_list()
        return [Submission(*submission) for submission in submission_data]


    @classmethod
    def add_submission(cls, student_id, assignment_id, content, date):
        values = (assignment_id, student_id, content, date)
        new_submission_id = DB.create_submission_record(values)
        #new_attendance = cls.get_attendance_by_id(new_attendance_id)
        #return new_attendance
    # @classmethod
    # def add_submission(cls, content, date, assignment_title, owner_name, points=None):
    #     """
    #     Adds submission to Assignment and Student submissions list.
    #     """
    #     student = Student.get_student(owner_name)
    #
    #     assignment = Assignment.get_assignment(assignment_title)
    #
    #     unique = True
    #
    #     for item in student.submission_list:
    #         if item.assignment == assignment:
    #             unique = False
    #
    #     if unique is True:
    #         submission = Submission(assignment, student, content, date,
    #                                 int(points) if type(points) == str and len(points) > 0 else None)
    #         assignment.submission_list.append(submission)
    #         student.submission_list.append(submission)
    #     else:
    #         raise NameError('This assignment has already been submitted!')

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
