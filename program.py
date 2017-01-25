import csv

from Models.submission import *
from Models.assignment import *


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
                    continue
                    Staff.add_staff(user["name"], user["mail"], user["password"])
                elif user["role"] == "boss":
                    continue
                    Boss.add_boss(user["name"], user["mail"], user["password"])
                else:
                    raise KeyError("There is no such role")

    @staticmethod
    def import_csv_attendance(filepath):
        with open(filepath) as source:
            attendance_csv_list = csv.DictReader(source)
            for attendance in attendance_csv_list:
                Attendance.add_attendance(attendance["student name"], attendance["date"], attendance["status"])

    @staticmethod
    def import_csv_assigment(filepath):
        with open(filepath) as source:
            assignment_csv_list = csv.DictReader(source)
            for assignment in assignment_csv_list:
                Assignment.add_assignment(assignment["title"], assignment["content"], assignment["due_date"], assignment["max_points"])

    @staticmethod
    def import_csv_submission(filepath):
        with open(filepath) as source:
            submission_csv_list = csv.DictReader(source)
            for submission in submission_csv_list:
                Submission.add_submission(submission["title"], submission["content"], submission["date"], submission["assignment_title"], submission["student_name"], submission["points"])

    @staticmethod
    def export_csv_users(filepath):
        with open(filepath, "w") as user_csv:
            fieldnames = ['name', 'mail' , 'password', 'role']
            user_writer = csv.DictWriter(user_csv, fieldnames=fieldnames)
            user_writer.writeheader()
            user_list = User.get_user_list()
            print(user_list)
            for user in user_list:
                user_dict = {'name': user.get_name(), 'mail': user.get_mail(), 'password': user.get_password(), 'role': user.get_class_name().lower()}
                user_writer.writerow(user_dict)

    @staticmethod
    def import_all_csv():
        Program.import_csv_users("Data/user.csv")
        Program.import_csv_assigment("Data/assignment.csv")
        Program.import_csv_submission("Data/submission.csv")

    @staticmethod
    def export_all_cvs():
        Program.export_csv_users("Data/user.csv")
