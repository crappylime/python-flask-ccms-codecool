from flask import Flask, render_template, request, redirect, url_for, session
from models.attendances import Attendance
from models.users import User
from flask import Blueprint



attendances_ctrl = Blueprint('attendances_ctrl', __name__)


@attendances_ctrl.route("/attendances")
def attendances():

    attendances_list = Attendance.get_attendance_list()

    name_dict = {1: 'Present', 0: 'Absent', 0.8: 'Late' }

    return render_template('attendance_list.html', attendances_list=attendances_list)


@attendances_ctrl.route("/attendances/check/", methods=['GET', 'POST'])
def check_attendance():

    students_list = User.get_user_list_by_role('student')
    chosen_date = request.args.get('date', None)
    by_date_list = Attendance.get_attendance_list_by_date(chosen_date)
    student_status_dict = {}

    for attendance in by_date_list:
        student_status_dict[attendance.get_student().get_id()] = attendance.get_status()

    if request.method == 'GET':
        if chosen_date is None or len(by_date_list) == 0:
            return render_template('attendance_check.html', students_list=students_list,
                                   chosen_date=chosen_date, student_status_dict={})
        else:
            return render_template('attendance_check.html', students_list=students_list,
                                   chosen_date=chosen_date, student_status_dict=student_status_dict)

    if request.method == 'POST':
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

    # return render_template('attendance_check.html', students_list=students_list,
    #                        chosen_date=chosen_date, student_status_dict={})
