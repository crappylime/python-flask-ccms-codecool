from flask import render_template
from flask import Blueprint
from models.assignments import Assignment

assignments_ctrl = Blueprint('assignments_ctrl', __name__)


@assignments_ctrl.route("/assignments")
def assignments():
    return render_template("assignments.html", assignment_list=Assignment.get_assignment_list())


@assignments_ctrl.route("/assignments/<assignment_id>")
def assignment_details(assignment_id):
    return render_template("assignment_details.html", assignment=Assignment.get_assignment_by_id(assignment_id))
