from models.submissions import Submission
from models.assignments import Assignment
from flask import Blueprint, render_template, url_for, request, redirect

submissions_ctrl = Blueprint('submissions_ctrl', __name__)


@submissions_ctrl.route("/assignments/<assignment_id>/submissions")
def list_assignment_submissions(assignment_id):
    """ Shows list of submissions stored in the database.
    """
    assignment = Assignment.get_assignment_by_id(assignment_id)
    assignment_id = assignment.get_id()
    return render_template('submissions.html', assignment=assignment,  list_assignment_submissions=Submission.get_submission_list_by_assignment_id(assignment_id))


@submissions_ctrl.route("/submissions/<submission_id>")
def submission_details(submission_id):
    """ Shows details of submission stored in the database.
    """
    submission = Submission.get_submission_by_id(submission_id)
    return render_template('submission_details.html', submission=submission, assignment=submission.get_assignment())


@submissions_ctrl.route('/assignments/<assignment_id>/submissions/new', methods=['GET', 'POST'])
def submission_add(assignment_id):
    """ Creates new submission
    If the method was GET it should show new submission form.
    If the method was POST it should create, save new submission.
    """
    student_id = 2
    assignment = Assignment.get_assignment_by_id(assignment_id)
    if request.method == 'POST':
        Submission.add_submission(assignment_id, student_id, request.form['content'])
        return redirect(url_for('assignments_ctrl.assignments'))
    return render_template('add_submission.html', assignment=assignment)
