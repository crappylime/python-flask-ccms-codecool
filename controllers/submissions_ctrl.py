from models.submissions import Submission
from flask import Blueprint, render_template

submissions_ctrl = Blueprint('submissions_ctrl', __name__)


@submissions_ctrl.route("/<assignment_id>/submissions")
def list_assignment_submissions(assignment_id, assignment):
    """ Shows list of submissions stored in the database.
    """
    return render_template('submissions.html', assignment,  list_assignment_submissions=Submission.get_submission_list_by_assignment_id(assignment_id))
