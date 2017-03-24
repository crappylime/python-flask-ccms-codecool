from flask import Flask, render_template, request, redirect, url_for, session, flash
from models.checkpoints import Checkpoint
from models.users import *
from flask import Blueprint
import time


checkpoints_ctrl = Blueprint('checkpoints_ctrl', __name__)


@checkpoints_ctrl.route("/checkpoints", methods=['GET', 'POST'])
def checkpoints():
    """Show checkpoints list with overall checkpoint
        options: show all, show by date, show by student"""

    chosen_date = request.args.get('date', None)
    chosen_student = request.args.get('student', None)
    student_list = User.get_user_list_by_role('student')

    # ------------------ retrieve data helpers section --------------------------------
    name_id_dict = {}  # create dict with pairs: student name - student id to retrieve student id from selected name
    for stu in student_list:
            name_id_dict[stu.get_name()] = stu.get_id()

    names_list = []  # create names list to view sorted names list in select form
    for name in name_id_dict.keys():
        names_list.append(name.split(' '))

    names_list.sort(key=lambda x: (x[1]).lower())  # sort by surname
    sorted_name_list = list(map(lambda x: " ".join(x), names_list))  # join [name, surname] list to one string
    # ---------------------------------------------------------------------------------

    if chosen_date:  # show by date
        checkpoints_list = Checkpoint.get_checkpoint_list_by_date(chosen_date)
        overall = Checkpoint.get_overall_checkpoint_by_date(chosen_date)
    elif chosen_student and chosen_student != 'all':  # show by chosen student
        checkpoints_list = Checkpoint.get_checkpoint_list_by_student_id(name_id_dict[chosen_student])
        overall = Checkpoint.get_overall_checkpoint(name_id_dict[chosen_student])
    else:  # show all
        checkpoints_list = Checkpoint.get_checkpoint_list()
        overall = Checkpoint.get_all_overall_checkpoint()

    checkpoints_list = sorted(checkpoints_list, key=lambda att: att.get_date(), reverse=True)  # sort by date (DESC)
    return render_template('checkpoint_list.html', checkpoints_list=checkpoints_list,
                           chosen_date=chosen_date, names=sorted_name_list, overall=overall)


@checkpoints_ctrl.route("/checkpoints/edit/<att_id>", methods=['GET', 'POST'])
def checkpoint_edit(att_id):
    """Show edit page for selected checkpoint id"""

    checkpoint_by_id = Checkpoint.get_checkpoint_by_id(att_id)
    student = checkpoint_by_id.get_student()

    if request.method == 'POST':
        updated_att = request.form[str(student.get_id())]
        Checkpoint.update_checkpoint(student.get_id(), checkpoint_by_id.get_title(), updated_att)
        return redirect(url_for('checkpoints_ctrl.checkpoints'))

    flash('edit done')

    return render_template('checkpoint_edit.html', checkpoint=checkpoint_by_id, student=student)


@checkpoints_ctrl.route("/checkpoints/check/", methods=['GET', 'POST'])
def check_checkpoint():
    """Show checkpoint check window
    options: show by date, edit"""

    students_list = User.get_user_list_by_role('student')
    chosen_title = request.args.get('title', None)
    # chosen_date = request.form('date')
    by_title_list = Checkpoint.get_checkpoint_list_by_title(chosen_title)

    student_status_dict = {}  # make dict with student_id - checkpoint pairs
    for checkpoint in by_title_list:
        student_status_dict[checkpoint.get_student().get_id()] = checkpoint.get_card()

    if request.method == 'GET':
        if chosen_title is None:  # without chosen date today is default date
            # chosen_date = time.strftime("%Y-%m-%d")
            by_title_list = Checkpoint.get_checkpoint_list_by_title(chosen_title)  # get checkpoint list for today (if any)
            student_status_dict = {}
            if len(by_title_list) != 0:
                for checkpoint in by_title_list:
                    student_status_dict[checkpoint.get_student().get_id()] = checkpoint.get_status()

        elif len(by_title_list) == 0:  # if there is no checkpoints for chosen data
            return render_template('checkpoint_check.html', students_list=students_list,
                                   chosen_title=chosen_title, student_status_dict={})

        return render_template('checkpoint_check.html', students_list=students_list,
                               chosen_title=chosen_title, student_status_dict=student_status_dict)

    if request.method == 'POST':
        checkpoints_list = []

        if chosen_title is None:  # load checkpoints for default date (if any)
            # chosen_date = time.strftime("%Y-%m-%d")
            by_date_list = Checkpoint.get_checkpoint_list_by_date(chosen_title)

        if len(by_title_list) == 0:  # add new checkpoints (because there was no checkpoints for selected day)
            for student in students_list:
                checkpoints_list.append((student.get_id(), chosen_title, request.form[str(student.get_id())]))
            for checkpoint in checkpoints_list:
                Checkpoint.add_checkpoint(checkpoint[0], checkpoint[1], checkpoint[2])

        else:
            # update checkpoints records for selected day
            for student in students_list:
                checkpoints_list.append((student.get_id(), chosen_title, request.form[str(student.get_id())]))
            for checkpoint in checkpoints_list:
                Checkpoint.update_checkpoint(checkpoint[0], checkpoint[1], checkpoint[2])

        return render_template('checkpoint_check.html', students_list=students_list,
                               student_status_dict={})
