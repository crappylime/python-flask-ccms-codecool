import csv
import 

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
                    Staff.add_mentor(user["Name"], user["E-mail"], user["Password"])
                elif user["Role"] == "boss":
                    Boss.add_user(user["Name"], user["E-mail"], user["Password"])
                else:
                    raise KeyError

    @staticmethod
    def import_csv_attendance(filepath):
        with open(filepath) as source:
            attendance_csv_list = csv.DictReader(source)
            for attendance in attendance_csv_list:

    @staticmethod
    def import_csv_assigment(filepath):
        with open(filepath) as source:
            assigment_csv_list = csv.DictReader(source)
            for assigment in assigment_csv_list:
                Assigment.add_assigment(assigment["Title"], assigment["Content"], assigment["Due_date"], assigment["Max_points"])

    @staticmethod
    def import_csv_submission(filepath):
        with open(filepath) as source:
            submission_csv_list = csv.DictReader(source)
            for submission in assigment_csv_list:
                Assigment.add_assigment(assigment["Title"], assigment["Content"], assigment["Due_date"], assigment["Max_points"])




