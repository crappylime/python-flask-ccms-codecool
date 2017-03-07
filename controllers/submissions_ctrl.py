from models.submissions import Submission
from models.assignments import Assignment
from flask import Blueprint, render_template

submissions_ctrl = Blueprint('submissions_ctrl', __name__)


@submissions_ctrl.route("/assignments/<assignment_id>/submissions")
def list_assignment_submissions(assignment_id):
    """ Shows list of submissions stored in the database.
    """
    assignment = Assignment.get_assignment_by_id(assignment_id)
    assignment_id = assignment.get_id()
    return render_template('submissions.html', assignment=assignment,  list_assignment_submissions=Submission.get_submission_list_by_assignment_id(assignment_id))
