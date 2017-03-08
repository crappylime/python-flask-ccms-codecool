from flask import render_template, request, redirect, url_for
from flask import Blueprint
from models.teams import Team
from db_controller import DB

teams_ctrl = Blueprint('teams_ctrl', __name__)


@teams_ctrl.route("/teams")
def teams():
    return render_template("teams.html", teams_list=Team.get_list_teams())


@teams_ctrl.route("/teams/<team_id>")
def team_details(team_id):
    return render_template("team_details.html", team=Team.get_team_by_id(team_id))
