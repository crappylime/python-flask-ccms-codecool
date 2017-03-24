from models.submissions import Submission
from models.assignments import Assignment
from models.menus import Menu
from models.users import User
from flask import Blueprint, render_template, url_for, request, redirect, session, flash
import json


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


@submissions_ctrl.route('/add_submission', methods=['POST'])
def add_submission():
    student_id = session['user_id']
    user = User.get_user_by_id(student_id)
    submission_content_list = request.get_json()
    submission_link = submission_content_list[0]
    assignment_id = submission_content_list[1]
    for submission in user.get_submission_list():
        if submission.get_assignment().get_id() == assignment_id:
            return 'Already added'
    else:
        submission = Submission.add_submission(assignment_id, student_id, submission_link)
        submission.student = ''
        submission.assignment_title = submission.get_assignment().get_title()
        submission.assignment_max_points = submission.get_assignment().get_max_points()
        submission.assignment = submission.get_assignment().get_id()
        new_submission_in_json = json.dumps(submission.__dict__, ensure_ascii=False)
    return new_submission_in_json


@submissions_ctrl.route('/grade_submission', methods=['POST'])
def grade_submission():
    grade_submission_content_list = request.get_json()
    points = int(grade_submission_content_list[0])
    submission_id = grade_submission_content_list[1]
    submission = Submission.get_submission_by_id(submission_id)
    user_id = submission.get_student().get_id()
    assignment = submission.get_assignment()
    max_points = assignment.get_max_points()
    if points > max_points:
        return ''
    Submission.set_grade_submission(user_id, assignment.get_id(), points)
    submission.student = ''
    submission.assignment = ''
    graded_submission_in_json = json.dumps(submission.__dict__, ensure_ascii=False)
    return graded_submission_in_json
