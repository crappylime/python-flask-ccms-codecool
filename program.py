import csv
from Models.user import *
from Models.submission import *
from Models.assignment import *


class Program:

    @staticmethod
    def import_csv_users(filepath):
        with open(filepath) as source:
            users_csv_list = csv.DictReader(source)
            print(users_csv_list.fieldnames)
            for user in users_csv_list:
                if user["Role"] == "student":
                    Student.add_student(user["Name"], user["E-mail"], user["Password"])
                elif user["Role"] == "mentor":
                    Mentor.add_mentor(user["Name"], user["E-mail"], user["Password"])
                elif user["Role"] == "staff":
                    Staff.add_staff(user["Name"], user["E-mail"], user["Password"])
                elif user["Role"] == "boss":
                    Boss.add_boss(user["Name"], user["E-mail"], user["Password"])
                else:
                    raise KeyError("There is no such role")

    @staticmethod
    def import_csv_attendance(filepath):
        with open(filepath) as source:
            attendance_csv_list = csv.DictReader(source)
            for attendance in attendance_csv_list:
                Attendance.add_attendance(attendance["Student name"], attendance["Date"], attendance["Status"])

    @staticmethod
    def import_csv_assigment(filepath):
        with open(filepath) as source:
            assignment_csv_list = csv.DictReader(source)
            for assignment in assignment_csv_list:
                Assignment.add_assignment(assignment["Title"], assignment["Content"], assignment["Due_date"], assignment["Max_points"])

    @staticmethod
    def import_csv_submission(filepath):
        with open(filepath) as source:
            submission_csv_list = csv.DictReader(source)
            for submission in submission_csv_list:
                Submission.add_submission(submission["Title"], submission["Content"], submission["Date"], submission["Assignment_title"], submission["Student_name"], submission["Points"])




