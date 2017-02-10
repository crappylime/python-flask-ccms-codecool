from db import DB


class Team:
    """Class that represent teams"""

    def __init__(self, team_id, name):
        self.id = team_id
        self.name = name

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

    def get_team_by_name(self):
        """not increment"""
        pass

    @classmethod
    def add_team(cls, name):
        """Add new team to data base and return team object"""
        new_team_id = DB.create_team(name)
        new_team = cls.get_team_by_id(new_team_id)

        return new_team

    @staticmethod
    def get_list_teams():
        """Return list of team objects from data base"""
        team_list = DB.read_team_list()
        return [Team(*team) for team in team_list]
