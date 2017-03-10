from models.submissions import Submission
from models.assignments import Assignment
from models.menus import Menu
from flask import Blueprint, render_template, url_for, request, redirect, session, flash


submissions_ctrl = Blueprint('submissions_ctrl', __name__)

mainmenu = Menu.get_main_menu()

@submissions_ctrl.route("/assignments/<assignment_id>/submissions")
def list_assignment_submissions(assignment_id, methods=['GET', 'POST']):
    """ Shows list of submissions stored in the database.
    """
    assignment = Assignment.get_assignment_by_id(assignment_id)
    return render_template('submissions.html', assignment=assignment,  list_assignment_submissions=Submission.get_submission_list_by_assignment_id(assignment_id), mainmenu=mainmenu)


@submissions_ctrl.route("/submissions/<submission_id>")
def submission_details(submission_id):
    """ Shows details of submission stored in the database.
    """
    submission = Submission.get_submission_by_id(submission_id)
    return render_template('submission_details.html', submission=submission, assignment=submission.get_assignment(), mainmenu=mainmenu)


@submissions_ctrl.route('/assignments/<assignment_id>/submissions/new', methods=['GET', 'POST'])
def submission_add(assignment_id):
    """ Creates new submission
    If the method was GET it should show new submission form.
    If the method was POST it should create, save new submission.
    """
    student_id = session['user_id']
    assignment = Assignment.get_assignment_by_id(assignment_id)
    if request.method == 'POST':
        submission = Submission.add_submission(assignment_id, student_id, request.form['content'])
        flash('Submission {} has been added.'.format(submission.get_content()))
        return redirect(url_for('assignments_ctrl.assignments'))
    return render_template('add_submission.html', assignment=assignment, mainmenu=mainmenu)


@submissions_ctrl.route('/submissions/<submission_id>/grade', methods=['GET', 'POST'])
def submission_grade(submission_id):
    """ Creates new submission
    If the method was GET it should show new submission form.
    If the method was POST it should create, save new submission.
    """
    submission = Submission.get_submission_by_id(submission_id)
    user_id = submission.get_student().get_id()
    assignment = submission.get_assignment()
    if request.method == 'POST':
        points = int(request.form['points'])
        Submission.set_grade_submission(user_id, assignment.get_id(), points)
        flash("{}'s submission has been graded.".format(submission.get_student().get_name()))
        return redirect(url_for('submissions_ctrl.list_assignment_submissions', assignment_id=assignment.get_id()))
    return render_template('submission_grade.html', assignment=assignment, submission=submission, mainmenu=mainmenu)
