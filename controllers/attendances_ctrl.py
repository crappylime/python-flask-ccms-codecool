from flask import Flask, render_template, request, redirect, url_for, session
from models.attendances import Attendance
from models.users import User
from flask import Blueprint



attendances_ctrl = Blueprint('attendances_ctrl', __name__)


@attendances_ctrl.route("/attendances")
def attendances():

    attendances_list = Attendance.get_attendance_list()

    return render_template('attendance_list.html', attendances_list=attendances_list)


# @attendances_ctrl.route("/attendances/check/", methods=['GET'])
@attendances_ctrl.route("/attendances/check/", methods=['GET', 'POST'])
def check_attendance():
    students_list = User.get_user_list_by_role('student')

    chosen_date = request.args.get('date', None)
    print(chosen_date)

    if request.method == 'GET':
        if chosen_date is None:
            print('dfdf')
            return render_template('attendance_check.html', students_list=students_list)

    if request.method == 'POST':
        print('poost')
        # date = request.form["date"]

        attendances_list = []
        by_date_list = Attendance.get_attendance_list_by_date(chosen_date)
        if len(by_date_list) == 0:
            for student in students_list:
                attendances_list.append((student.get_id(), chosen_date, request.form[str(student.get_id())]))
            for atten in attendances_list:
                Attendance.add_attendance(atten[0], atten[1], atten[2])

        return render_template('attendance_check.html', students_list=students_list)

    return render_template('attendance_check.html', students_list=students_list, chosen_date=chosen_date)
        #     print(attendances_list)
        #     print('nie podano daty')
        # print(date)


    # if len(by_date_list) == 0:



