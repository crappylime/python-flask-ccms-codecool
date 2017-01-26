import csv

from Models.submission import *
from Models.assignment import *
from Models.attendance import *


class Program:

    @staticmethod
    def import_csv_users(filepath):
        with open(filepath) as source:
            users_csv_list = csv.DictReader(source)
            for user in users_csv_list:
                if user["role"] == "student":
                    Student.add_student(user["name"], user["mail"], user["password"])
                elif user["role"] == "mentor":
                    Mentor.add_mentor(user["name"], user["mail"], user["password"])
                elif user["role"] == "staff":
                    Staff.add_staff(user["name"], user["mail"], user["password"])
                elif user["role"] == "boss":
                    Boss.add_boss(user["name"], user["mail"], user["password"])
                else:
                    raise KeyError("There is no such role")

    @staticmethod
    def import_csv_attendance(filepath):
        with open(filepath) as source:
            attendance_csv_list = csv.DictReader(source)
            for attendance in attendance_csv_list:
                student = Student.get_student(attendance["student_name"])
                Attendance.add_attendance(student, attendance["date"], attendance["status"])

    @staticmethod
    def import_csv_assignment(filepath):
        with open(filepath) as source:
            assignment_csv_list = csv.DictReader(source)
            for assignment in assignment_csv_list:
                Assignment.add_assignment(assignment["title"], assignment["content"], assignment["due_date"], assignment["max_points"])

    @staticmethod
    def import_csv_submission(filepath):
        with open(filepath) as source:
            submission_csv_list = csv.DictReader(source)
            for submission in submission_csv_list:
                Submission.add_submission(submission["content"], submission["date"], submission["assignment_title"], submission["student_name"], submission["points"])

    @staticmethod
    def export_csv_users(filepath):
        with open(filepath, "w") as user_csv:
            fieldnames = ['name', 'mail', 'password', 'role']
            user_writer = csv.DictWriter(user_csv, fieldnames=fieldnames)
            user_writer.writeheader()
            user_list = User.get_user_list()
            for user in user_list:
                user_dict = {'name': user.get_name(), 'mail': user.get_mail(), 'password': user.get_password(), 'role': user.get_class_name().lower()}
                user_writer.writerow(user_dict)

    @staticmethod
    def export_csv_attendance(filepath):
        with open(filepath, "w") as attendance_csv:
            fieldnames = ['student_name', 'date', 'status']
            attendance_writer = csv.DictWriter(attendance_csv, fieldnames=fieldnames)
            attendance_writer.writeheader()
            attendance_list = Attendance.get_attendance_list()
            for attendance in attendance_list:
                attendance_dict = {'student_name': attendance.get_student().get_name(), 'date': attendance.get_date(), 'status': attendance.get_status()}
                attendance_writer.writerow(attendance_dict)

    @staticmethod
    def export_csv_assignment(filepath):
        with open(filepath, "w") as assignment_csv:
            fieldnames = ['title', 'content', 'due_date', 'max_points']
            assignment_writer = csv.DictWriter(assignment_csv, fieldnames=fieldnames)
            assignment_writer.writeheader()
            assignment_list = Assignment.get_list_assignmnent()
            for assignment in assignment_list:
                assignment_dict = {'title': assignment.get_title(), 'content': assignment.get_content(), 'due_date': assignment.get_due_date(), 'max_points': assignment.get_max_points()}
                assignment_writer.writerow(assignment_dict)

    @staticmethod
    def export_csv_submission(filepath):
        with open(filepath, "w") as submission_csv:
            fieldnames = ['assignment_title', 'student_name', 'content', 'date', 'points']
            submission_writer = csv.DictWriter(submission_csv, fieldnames=fieldnames)
            submission_writer.writeheader()
            assignment_list = Assignment.get_list_assignmnent()
            for assignment in assignment_list:
                for submission in assignment.get_list_submission():
                    submission_dict = {'assignment_title': submission.get_assignment().get_title(), 'student_name': submission.get_owner().get_name(), 'content': submission.get_content(), 'date': submission.get_date(), 'points': submission.get_points()}
                    submission_writer.writerow(submission_dict)

    @staticmethod
    def import_all_csv():
        Program.import_csv_users("Data/user.csv")
        Program.import_csv_attendance("Data/attendance.csv")
        Program.import_csv_assignment("Data/assignment.csv")
        Program.import_csv_submission("Data/submission.csv")

    @staticmethod
    def export_all_cvs():
        Program.export_csv_users("Data/user2.csv")
        Program.export_csv_attendance("Data/attendance2.csv")
        Program.export_csv_assignment("Data/assignment2.csv")
        Program.export_csv_submission("Data/submission2.csv")
