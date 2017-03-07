from flask import Flask, render_template, request, redirect, url_for, session
from models.attendances import Attendance
from models.users import User
from flask import Blueprint



attendances_ctrl = Blueprint('attendances_ctrl', __name__)


@attendances_ctrl.route("/attendances")
def attendances():

    attendances_list = Attendance.get_attendance_list()

    return render_template('attendance_list.html', attendances_list=attendances_list)


@attendances_ctrl.route("/attendances/check/", methods=['GET', 'POST'])
def check_attendance():
    students_list = User.get_user_list_by_role('student')

    if request.method == 'POST':
        # return 'oj'
        attendances_list = []
        for student in students_list:
            attendances_list.append((student.get_id(), "2030-02-09", request.form[str(student.get_id())]))
        print(attendances_list)
        for atten in attendances_list:
            Attendance.add_attendance(atten[0], atten[1], atten[2])



    return render_template('attendance_check.html', students_list=students_list)


