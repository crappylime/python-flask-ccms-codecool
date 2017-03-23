from flask import render_template, request, redirect, url_for, flash
from flask import Blueprint
from models.teams import Team
from models.users import User, Student
from models.menus import Menu
from db_controller import DB
import json

teams_ctrl = Blueprint('teams_ctrl', __name__)

mainmenu = Menu.get_main_menu()


@teams_ctrl.route("/teams")
def teams():
    return render_template("teams.html", teams_list=Team.get_list_teams(), mainmenu=mainmenu)


@teams_ctrl.route("/teams/<team_id>")
def team_details(team_id):
    return render_template("team_details.html", team=Team.get_team_by_id(team_id), mainmenu=mainmenu)


@teams_ctrl.route("/teams/new", methods=["GET", "POST"])
def team_new():
    if request.method == "POST":
        team_name = request.form['name']
        if not Team.get_team_by_name(team_name):
            Team.add_team(team_name)
            return redirect(url_for('teams_ctrl.teams'))
        flash('Team name already in use')
    return render_template("add_team_form.html", title="Add new team", mainmenu=mainmenu)


@teams_ctrl.route("/add_team", methods=["POST"])
def add_team():
    team_name = request.get_json()
    print(team_name)
    if not Team.get_team_by_name(team_name):
        team = Team.add_team(team_name)
        team_in_json = json.dumps(team.__dict__, ensure_ascii=False)
        return team_in_json
    flash('Team name already in use')
    return ""


@teams_ctrl.route("/teams/edit", methods=["GET", "POST"])
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
                           student_list=User.get_user_list_by_role('student'), mainmenu=mainmenu)


@teams_ctrl.route("/teams/<team_id>/edit/<student_id>")
def team_remove_student(team_id, student_id):
    Team.get_team_by_id(team_id).remove_member(User.get_user_by_id(student_id))
    return redirect(url_for('teams_ctrl.team_edit', team_id=team_id))


@teams_ctrl.route("/teams/remove", methods=["POST"])
def team_remove():
    team_id = request.get_json()
    DB.delete_team_record(team_id)
    return ""


@teams_ctrl.route("/get_team_by_id", methods=["POST"])
def get_team_by_id():
    print("hurrra")
    team_id = request.get_json()
    print(team_id)
    students = User.get_user_list_by_role("student")
    students_for_json = []
    for student in students:
        students_for_json.append((student.get_id(), student.get_name()))
    team = Team.get_team_by_id(team_id)
    team_members = team.get_members()
    members_for_json = []
    for member in team_members:
        members_for_json.append((member.get_id(), member.get_name()))
    team_data = (students_for_json, members_for_json)
    team_data_json = json.dumps(team_data)
    print(team_data_json)
    return team_data_json
