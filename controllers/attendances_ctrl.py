from flask import Flask, render_template, request, redirect, url_for, session
from models.attendances import Attendance
from models.users import *
from flask import Blueprint
import time


attendances_ctrl = Blueprint('attendances_ctrl', __name__)


@attendances_ctrl.route("/attendances", methods=['GET', 'POST'])
def attendances():

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
    elif chosen_student and chosen_student != 'all':  # show by chosen student
        attendances_list = Attendance.get_attendance_list_by_student_id(name_id_dict[chosen_student])
    else:  # show all
        attendances_list = Attendance.get_attendance_list()

    attendances_list = sorted(attendances_list, key=lambda att: att.get_date(), reverse=True)  # sort by date (DESC)
    return render_template('attendance_list.html', attendances_list=attendances_list,
                           chosen_date=chosen_date, names=sorted_name_list)


@attendances_ctrl.route("/attendances/edit/<att_id>", methods=['GET', 'POST'])
def attendance_edit(att_id):

    attendance = Attendance.get_attendance_by_id(att_id)
    student = attendance.get_student()

    if request.method == 'POST':
        updated_att = request.form[str(student.get_id())]
        Attendance.update_attendance(student.get_id(), attendance.get_date(), updated_att)
        return redirect(url_for('attendances_ctrl.attendances'))

    return render_template('attendance_edit.html', attendance=attendance, student=student)

    # return render_template('attendance_list.html', attendances_list=attendances_list, chosen_date=chosen_date)


@attendances_ctrl.route("/attendances/check/", methods=['GET', 'POST'])
def check_attendance():

    students_list = User.get_user_list_by_role('student')
    chosen_date = request.args.get('date', None)
    by_date_list = Attendance.get_attendance_list_by_date(chosen_date)
    student_status_dict = {}

    for attendance in by_date_list:
        student_status_dict[attendance.get_student().get_id()] = attendance.get_status()

    if request.method == 'GET':
        if chosen_date is None:
            chosen_date = time.strftime("%Y-%m-%d")
            by_date_list = Attendance.get_attendance_list_by_date(chosen_date)
            student_status_dict = {}
            print(by_date_list)
            if len(by_date_list) != 0:
                for attendance in by_date_list:
                    student_status_dict[attendance.get_student().get_id()] = attendance.get_status()

        elif len(by_date_list) == 0:
            return render_template('attendance_check.html', students_list=students_list,
                                   chosen_date=chosen_date, student_status_dict={})

        return render_template('attendance_check.html', students_list=students_list,
                               chosen_date=chosen_date, student_status_dict=student_status_dict)

    if request.method == 'POST':
        attendances_list = []

        if chosen_date is None:
            chosen_date = time.strftime("%Y-%m-%d")
            by_date_list = Attendance.get_attendance_list_by_date(chosen_date)

        if len(by_date_list) == 0:
            for student in students_list:
                attendances_list.append((student.get_id(), chosen_date, request.form[str(student.get_id())]))
            for attendance in attendances_list:
                Attendance.add_attendance(attendance[0], attendance[1], attendance[2])

        else:
            for student in students_list:
                attendances_list.append((student.get_id(), chosen_date, request.form[str(student.get_id())]))
            for attendance in attendances_list:
                Attendance.update_attendance(attendance[0], attendance[1], attendance[2])
        return render_template('attendance_check.html', students_list=students_list,
                               student_status_dict={})
