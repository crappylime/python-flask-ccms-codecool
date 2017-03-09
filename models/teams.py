from db_controller import DB
from models.users import User
from models.assignments import Assignment


class Team:
    """Class that represent teams"""

    def __init__(self, team_id, name):
        self.id = team_id
        self.name = name

    @property
    def member_list(self):
        return User.get_user_list_by_id_list(DB.read_user_id_list_by_team_id(self.id))

    @property
    def team_assignments_list(self):
        return Assignment.get_team_assignment_list()

    def get_id(self):
        """Return team instance id"""
        return self.id

    def get_name(self):
        """Return team instance name"""
        return self.name

    @classmethod
    def get_team_by_id(cls, team_id):
        """Return team by provided id """

        return cls.create_team_by_id(team_id)

    @classmethod
    def create_team_by_id(cls, team_id):
        """Return team object by provided id"""
        args = DB.read_team_record_by_id(team_id)
        return cls(*args[0])

    @classmethod
    def get_team_by_name(cls, team_name):
        """Returns team object by name"""
        args = DB.read_team_record_by_name(team_name)
        if args:
            return cls(*args[0])
        return None

    @classmethod
    def add_team(cls, name):
        """Add new team to data base and return team object"""
        new_team_id = DB.create_team(name)
        new_team = cls.get_team_by_id(new_team_id)
        return new_team

    def add_member(self, member):
        """Adds member obj to a team"""
        self.member_list.append(member)
        DB.create_member_record(self.id, member.get_id())

    @staticmethod
    def remove_member(member):
        DB.delete_member_record(member.get_id())

    def relocate_member(self, student_id):
        DB.update_student_team_id(self.id, student_id)

    def get_members(self):
        return self.member_list

    @staticmethod
    def get_list_teams():
        """Return list of team objects from data base"""
        team_list = DB.read_team_list()
        return [Team(*team) for team in team_list]

    def get_team_assignments(self):
        return self.team_assignments_list

    def set_name(self, new_name):
        """
        Sets team name
        """
        self.name = new_name
        DB.update_team_name(self.id, self.name)


