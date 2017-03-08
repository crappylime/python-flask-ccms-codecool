from flask import Flask, render_template, request, redirect, url_for, session
from models.attendances import Attendance
from models.users import User
from flask import Blueprint
import time


attendances_ctrl = Blueprint('attendances_ctrl', __name__)


@attendances_ctrl.route("/attendances", methods=['GET', 'POST'])
def attendances():

    chosen_date = request.args.get('date', None)

    if chosen_date:
        attendances_list = Attendance.get_attendance_list_by_date(chosen_date)
    else:
        attendances_list = Attendance.get_attendance_list()

    return render_template('attendance_list.html', attendances_list=attendances_list, chosen_date=chosen_date)


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
            return render_template('attendance_check.html', students_list=students_list,
                                   chosen_date=chosen_date, student_status_dict={})
        elif len(by_date_list) == 0:
            return render_template('attendance_check.html', students_list=students_list,
                                   chosen_date=chosen_date, student_status_dict={})
        else:
            return render_template('attendance_check.html', students_list=students_list,
                                   chosen_date=chosen_date, student_status_dict=student_status_dict)

    if request.method == 'POST':
        if chosen_date is None:
            chosen_date = time.strftime("%Y-%m-%d")
            by_date_list = Attendance.get_attendance_list_by_date(chosen_date)
        attendances_list = []
        if len(by_date_list) == 0:
            for student in students_list:
                attendances_list.append((student.get_id(), chosen_date, request.form[str(student.get_id())]))
            for attendance in attendances_list:
                Attendance.add_attendance(attendance[0], attendance[1], attendance[2])
            return render_template('attendance_check.html', students_list=students_list,
                                   student_status_dict={})
        else:
            for student in students_list:
                attendances_list.append((student.get_id(), chosen_date, request.form[str(student.get_id())]))
            for attendance in attendances_list:
                Attendance.update_attendance(attendance[0], attendance[1], attendance[2])
            return render_template('attendance_check.html', students_list=students_list,
                                   student_status_dict={})
