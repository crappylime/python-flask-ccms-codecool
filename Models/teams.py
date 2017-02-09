from db import DB


class Team:

    def __init__(self, team_id, name):
        self.id = team_id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    @classmethod
    def get_team_by_id(cls, team_id):
        return cls.create_team_by_id(team_id)

    @classmethod
    def create_team_by_id(cls, team_id):
        args = DB.read_team_record_by_id(team_id)
        return cls(*args[0])

    def get_team_by_name(self):
        pass

    @classmethod
    def add_team(cls, name):

        new_team_id = DB.create_team(name)
        new_team = cls.get_team_by_id(new_team_id)

        return new_team

    @staticmethod
    def get_list_teams():
        team_list = DB.read_team_list()
        return [Team(*team) for team in team_list]
