from flask import Flask, render_template, request, redirect, url_for, session
from models.attendances import Attendance
from models.users import *
from flask import Blueprint
import time


attendances_ctrl = Blueprint('attendances_ctrl', __name__)


@attendances_ctrl.route("/attendances", methods=['GET', 'POST'])
def attendances():
    """Show attendances list with overall attendance
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
        attendances_list = Attendance.get_attendance_list_by_date(chosen_date)
        overall = Attendance.get_overall_attendance_by_date(chosen_date)
        print(overall)
    elif chosen_student and chosen_student != 'all':  # show by chosen student
        attendances_list = Attendance.get_attendance_list_by_student_id(name_id_dict[chosen_student])
        overall = Attendance.get_overall_attendance(name_id_dict[chosen_student])
    else:  # show all
        attendances_list = Attendance.get_attendance_list()
        overall = Attendance.get_all_overall_attendance()

    attendances_list = sorted(attendances_list, key=lambda att: att.get_date(), reverse=True)  # sort by date (DESC)
    return render_template('attendance_list.html', attendances_list=attendances_list,
                           chosen_date=chosen_date, names=sorted_name_list, overall=overall)


@attendances_ctrl.route("/attendances/edit/<att_id>", methods=['GET', 'POST'])
def attendance_edit(att_id):
    """Show edit page for selected attendance id"""

    attendance_by_id = Attendance.get_attendance_by_id(att_id)
    student = attendance_by_id.get_student()

    if request.method == 'POST':
        updated_att = request.form[str(student.get_id())]
        Attendance.update_attendance(student.get_id(), attendance_by_id.get_date(), updated_att)
        return redirect(url_for('attendances_ctrl.attendances'))

    return render_template('attendance_edit.html', attendance=attendance_by_id, student=student)

    # return render_template('attendance_list.html', attendances_list=attendances_list, chosen_date=chosen_date)


@attendances_ctrl.route("/attendances/check/", methods=['GET', 'POST'])
def check_attendance():
    """Show attendance check window
    options: show by date, edit"""

    students_list = User.get_user_list_by_role('student')
    chosen_date = request.args.get('date', None)

    by_date_list = Attendance.get_attendance_list_by_date(chosen_date)
    student_status_dict = {}  # make dict with student_id - attendance pairs
    for attendance in by_date_list:
        student_status_dict[attendance.get_student().get_id()] = attendance.get_status()

    if request.method == 'GET':
        if chosen_date is None:  # without chosen date today is default date
            chosen_date = time.strftime("%Y-%m-%d")
            by_date_list = Attendance.get_attendance_list_by_date(chosen_date)  # get attendance list for today (if any)
            student_status_dict = {}
            if len(by_date_list) != 0:
                for attendance in by_date_list:
                    student_status_dict[attendance.get_student().get_id()] = attendance.get_status()

        elif len(by_date_list) == 0:  # if there is no attendances for chosen data
            return render_template('attendance_check.html', students_list=students_list,
                                   chosen_date=chosen_date, student_status_dict={})

        return render_template('attendance_check.html', students_list=students_list,
                               chosen_date=chosen_date, student_status_dict=student_status_dict)

    if request.method == 'POST':
        attendances_list = []

        if chosen_date is None:  # load attendances for default date (if any)
            chosen_date = time.strftime("%Y-%m-%d")
            by_date_list = Attendance.get_attendance_list_by_date(chosen_date)

        if len(by_date_list) == 0:  # add new attendances (because there was no attendances for selected day)
            for student in students_list:
                attendances_list.append((student.get_id(), chosen_date, request.form[str(student.get_id())]))
            for attendance in attendances_list:
                Attendance.add_attendance(attendance[0], attendance[1], attendance[2])

        else:  # update attendances records for selected day
            for student in students_list:
                attendances_list.append((student.get_id(), chosen_date, request.form[str(student.get_id())]))
            for attendance in attendances_list:
                Attendance.update_attendance(attendance[0], attendance[1], attendance[2])
        return render_template('attendance_check.html', students_list=students_list,
                               student_status_dict={})
