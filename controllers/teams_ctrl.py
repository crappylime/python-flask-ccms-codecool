from flask import render_template, request, redirect, url_for, flash
from flask import Blueprint
from models.teams import Team
from models.users import User, Student
from db_controller import DB

teams_ctrl = Blueprint('teams_ctrl', __name__)


@teams_ctrl.route("/teams")
def teams():
    return render_template("teams.html", teams_list=Team.get_list_teams())


@teams_ctrl.route("/teams/<team_id>")
def team_details(team_id):
    return render_template("team_details.html", team=Team.get_team_by_id(team_id))


@teams_ctrl.route("/teams/new", methods=["GET", "POST"])
def team_new():
    if request.method == "POST":
        team_name = request.form['name']
        if not Team.get_team_by_name(team_name):
            Team.add_team(team_name)
            return redirect(url_for('teams_ctrl.teams'))
        flash('Team name already in use')
    return render_template("add_team_form.html", title="Add new team")


@teams_ctrl.route("/teams/<team_id>/edit", methods=["GET", "POST"])
def team_edit(team_id):
    if request.method == "POST":
        if request.form['name']:
            team_name = request.form['name']
            Team.get_team_by_id(team_id).set_name(team_name)
        if request.form['student']:
            student_id = int(''.join(filter(lambda x: x.isdigit(), request.form['student'])))
            if Student.get_student_team_id(student_id):
                Team.get_team_by_id(team_id).relocate_member(student_id)
            else:
                Team.get_team_by_id(team_id).add_member(User.get_user_by_id(student_id))
    return render_template("edit_team_form.html", team=Team.get_team_by_id(team_id),
                           student_list=User.get_user_list_by_role('student'))


@teams_ctrl.route("/teams/<team_id>/edit/<student_id>")
def team_remove_student(team_id, student_id):
    Team.get_team_by_id(team_id).remove_member(User.get_user_by_id(student_id))
    return redirect(url_for('teams_ctrl.team_edit', team_id=team_id))


@teams_ctrl.route("/teams/<team_id>/remove")
def team_remove(team_id):
    DB.delete_team_record(team_id)
    return redirect(url_for('teams_ctrl.teams'))
