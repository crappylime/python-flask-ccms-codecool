from db import DB

class Assignment:
    """This is class representing Assignment given by Mentor."""

    def __init__(self, id, title, content, due_date, max_points):
        self.id = id
        self.title = title
        self.content = content
        self.due_date = due_date
        self.max_points = max_points

    def __str__(self):
        info = self.__class__.__name__

        for key, value in self.__dict__.items():
            info += ", {}: {}".format(key, value)

        return info

    @classmethod
    def get_assignment(cls, id):
        """
        Returns assignment object.

       :return:
            assignment: object
        """
        return cls.create_assignment(id)

    @classmethod
    def get_assignment_list(cls):
        """
        Returns list of assignments instances
        :return:
            list: list of assignments instances
        """
        return cls.create_assignment_list()

    @classmethod
    def create_assignment(cls, id):
        """
        Creates instance of user
        :return:
            user: object
        """
        args = DB.read_assignment_record_by_id(id)
        return Assignment(*args[0])

    @classmethod
    def create_assignment_list(cls):
        """
        Creates list of user instances
        :return:
            user_list: list
        """
        assignment_data = DB.read_assignment_record_list()
        return [Assignment(*assignment) for assignment in assignment_data]

    @classmethod
    def add_assignment(cls, title, content, due_date, max_points):
        """
        Adds assignment to assignments list.
        """
        try:
            max_points = int(max_points)
        except TypeError:
            raise TypeError("Points must be a number")
        cls.assignment_list.append(Assignment(title, content, due_date, max_points))

    def get_title(self):
        """
        :return:
            str: title of assignment
        """
        return self.title

    def get_content(self):
        """
        :return:
            str: content of assignment
        """
        return self.content

    def get_due_date(self):
        """
        :return:
            str: due date of assignment
        """
        return self.due_date

    def get_max_points(self):
        """
        :return:
            int: max points for given assignment
        """
        return self.max_points

    def edit_assignment(self, title, due_date, max_points):
        """
        Edits assignments parameters
        """
        self.title = title
        self.due_date = due_date
        self.max_points = max_points
