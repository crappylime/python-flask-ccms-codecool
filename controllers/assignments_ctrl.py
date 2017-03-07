from flask import render_template, request, redirect
from flask import Blueprint
from models.assignments import Assignment

assignments_ctrl = Blueprint('assignments_ctrl', __name__)


@assignments_ctrl.route("/assignments")
def assignments():
    return render_template("assignments.html", assignment_list=Assignment.get_assignment_list())


@assignments_ctrl.route("/assignments/<assignment_id>")
def assignment_details(assignment_id):
    return render_template("assignment_details.html", assignment=Assignment.get_assignment_by_id(assignment_id))


@assignments_ctrl.route("/assignments/new", methods=["GET", "POST"])
def assignment_new():
    if request.method == "POST":
        assignment_title = request.form['assignment_title']
        content = request.form['content']
        due_date = request.form['due_date']
        max_points = request.form['max_points']
        Assignment.add_assignment(assignment_title, content, due_date, max_points)
        return redirect('/assignments')
    return render_template("add_edit_assignment.html", title="Add an assignment")


# @assignments_ctrl.route("/assignments/new")
# def assignment_new():
#     return render_template("add_edit_assignment.html", title="Add an assignment")
