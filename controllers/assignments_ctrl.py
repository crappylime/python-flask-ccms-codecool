from flask import render_template, request, redirect, url_for
from flask import Blueprint
from models.assignments import Assignment
from models.menus import Menu
from db_controller import DB

assignments_ctrl = Blueprint('assignments_ctrl', __name__)
mainmenu = Menu.get_main_menu()


@assignments_ctrl.route("/assignments")
def assignments():
    return render_template("assignments.html", assignment_list=Assignment.get_assignment_list(), mainmenu=mainmenu)


@assignments_ctrl.route("/assignments/<assignment_id>")
def assignment_details(assignment_id):
    return render_template("assignment_details.html", assignment=Assignment.get_assignment_by_id(assignment_id),
                           mainmenu=mainmenu)


@assignments_ctrl.route("/assignments/new", methods=["GET", "POST"])
def assignment_new():
    if request.method == "POST":
        assignment_title = request.form['assignment_title']
        if 'is_team' in request.form:
            is_team = 1
        else:
            is_team = 0
        content = request.form['content']
        due_date = request.form['due_date']
        max_points = request.form['max_points']
        Assignment.add_assignment(assignment_title, is_team, content, due_date, max_points)
        return redirect(url_for('assignments_ctrl.assignments'))
    return render_template("add_edit_assignment.html", title="Add an assignment", mainmenu=mainmenu)


@assignments_ctrl.route("/assignments/<assignment_id>/edit", methods=["GET", "POST"])
def assignment_edit(assignment_id):
    if request.method == "POST":
        assignment_title = request.form['assignment_title']
        if 'is_team' in request.form:
            is_team = 1
        else:
            is_team = 0
        content = request.form['content']
        due_date = request.form['due_date']
        max_points = request.form['max_points']
        Assignment.get_assignment_by_id(assignment_id).edit_assignment(assignment_title, is_team, content, due_date,
                                                                       max_points)
        return redirect(url_for('assignments_ctrl.assignments'))
    return render_template("add_edit_assignment.html", title="Edit an assignment",
                           assignment=Assignment.get_assignment_by_id(assignment_id), mainmenu=mainmenu)


@assignments_ctrl.route("/assignments/<assignment_id>/remove")
def assignment_remove(assignment_id):
    DB.delete_assignment_record(assignment_id)
    return redirect(url_for('assignments_ctrl.assignments'))
