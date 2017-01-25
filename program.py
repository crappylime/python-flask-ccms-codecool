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
    def import_all_csv():
        Program.import_csv_users("Data/user.csv")
        Program.import_csv_assigment("Data/assignment.csv")
        Program.import_csv_submission("Data/submission.csv")
