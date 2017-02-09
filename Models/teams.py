from db import *


class Team:

    def __init__(self, team_id, name):
        self.id = team_id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_team_by_id(self):
        pass

    def get_team_by_name(self):

    @staticmethod
    def get_list_teams():
        pass



