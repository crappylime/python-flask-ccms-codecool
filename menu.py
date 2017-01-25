from Models.user import *
from ui import *

class Menu:
    def log_in(self):
        (user_name, user_password) = UserInterface.login()
        for student in Student.get_student_list():
            if user_name == student.name:
                user = student
                StudentMenu(user)

        for mentor in Mentor.get_mentor_list():
            if user_name == mentor.name:
                user = mentor
                MentorMenu(user)

        if user_name == Boss.get_boss().name:
            user = Boss.get_boss()
            BossMenu(user)



    def __init__(self):

        while True:
            user_choice = UserInterface.main_menu()
            if user_choice == "Log in":
                self.log_in()
            else:
                break


class StudentMenu:
    def __init__(self, user):

        while True:
            user_choice = UserInterface.student_menu()
            if user_choice == "Submit an assignment":
                submission_data = UserInterface.submit_assignment()
                Submission.add_submission(submission_data)
            elif user_choice == "View my grades":
            elif user_choice == "Log out":
                break

class MentorMenu:
    def __init__(self, user):

        while True:
            user_choice = UserInterface.mentor_menu()
            if user_choice == "Show students list":
            elif user_choice == "Add an assignment":
            elif user_choice == "Grade an assignment":
            elif user_choice == "Check attendance":
            elif user_choice == "Add student":
            elif user_choice == "Remove student":
            elif user_choice == "Edit student data":
            elif user_choice == "Log out":
                break

class BossMenu:
    def __init__(self, user):

        while True:
            user_choice = UserInterface.boss_menu()
            if user_choice == "Add a mentor":
            elif user_choice == "Remove a mentor":
            elif user_choice == "Edit mentor data":
            elif user_choice == "Show mentors list":
            elif user_choice == "Show students list":
            elif user_choice == "Log out":
            break

class StaffMenu:
    def __init__(self, user):

        while True:
            user_choice = UserInterface.staff_menu()
            if user_choice == "Show students list":
            elif user_choice == "Log out":
                break


def main():
    Menu()