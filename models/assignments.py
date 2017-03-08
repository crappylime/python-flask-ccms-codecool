from db_controller import DB


class Assignment:
    """This is class representing Assignment given by Mentor."""

    def __init__(self, assignment_id, title, is_team, content, due_date, max_points, ):
        self.id = assignment_id
        self.title = title
        self.is_team = is_team
        self.content = content
        self.due_date = due_date
        self.max_points = max_points

    def __str__(self):
        info = self.__class__.__name__

        for key, value in self.__dict__.items():
            info += ", {}: {}".format(key, value)

        return info

    @classmethod
    def get_assignment_by_id(cls, assignment_id):
        """
        Returns assignment object.

       :return:
            assignment: object
        """
        return cls.create_assignment_by_id(assignment_id)

    @classmethod
    def get_assignment_list(cls):
        """
        Returns list of assignments instances
        :return:
            list: list of assignments instances
        """
        return cls.create_assignment_list()

    @classmethod
    def get_team_assignment_list(cls):
        """
        Returns list of team assignments instances
        :return:
            list: list of assignments instances
        """
        return cls.create_team_assignment_list()

    @classmethod
    def create_assignment_by_id(cls, assignment_id):
        """
        Creates instance of assignment
        :return:
            assignment: object
        """
        args = DB.read_assignment_record_by_id(assignment_id)
        return Assignment(*args[0])

    @classmethod
    def create_assignment_list(cls):
        """
        Creates list of assignments instances
        :return:
            assignment_list: list
        """
        assignment_data = DB.read_assignment_record_list()
        return [Assignment(*assignment) for assignment in assignment_data]

    @classmethod
    def create_team_assignment_list(cls):
        """
        Creates list of team assignments instances
        :return:
            assignment_list: list
        """
        assignment_data = DB.read_team_assignment_record_list()
        return [Assignment(*assignment) for assignment in assignment_data]

    @classmethod
    def add_assignment(cls, title, is_team, content, due_date, max_points):
        values = (title, is_team, content, due_date, max_points)
        new_assignment_id = DB.create_assignment_record(values)
        new_assignment = cls.get_assignment_by_id(new_assignment_id)
        return new_assignment

    def get_id(self):
        """Returns assignment instance id"""
        return self.id

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

    def edit_assignment(self, title, is_team, content, due_date, max_points):
        """
        Edits assignments parameters
        """
        self.title = title
        self.is_team = is_team
        self.content = content
        self.due_date = due_date
        self.max_points = max_points
        DB.update_assignment(self.id, self.title, self.is_team, self.content, self.due_date, self.max_points)

    def get_assignment_type(self):
        print(self.is_team)
        return self.is_team
