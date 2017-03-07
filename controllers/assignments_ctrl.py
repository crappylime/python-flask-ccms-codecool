from flask import render_template
from flask import Blueprint
from models.assignments import Assignment

assignments_list = Blueprint('assignments_list', __name__)


@assignments_list.route("/assignments")
def assignments():
    return render_template("assignments.html", assignment_list=Assignment.get_assignment_list())
