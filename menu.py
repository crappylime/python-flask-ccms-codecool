from ui import *
from Models.user import *
from Models.assignment import Assignment
from Models.teams import Team
import os


class Menu:
    """log in menu"""

    @staticmethod
    def log_in():
        (user_name, user_password) = UserInterface.login()
        for user in User.get_user_list():
            if user_name == user.get_name():
                if user_password == user.get_password():
                    if user.get_class_name() == "Boss":
                        BossMenu(user)
                    elif user.get_class_name() == "Mentor":
                        MentorMenu(user)
                    elif user.get_class_name() == "Staff":
                        StaffMenu(user)
                    elif user.get_class_name() == "Student":
                        StudentMenu(user)
        else:
            UserInterface.login_error()

    def __init__(self):
        os.system("clear")

        while True:
            user_choice = UserInterface.main_menu()
            os.system("clear")
            if user_choice == "Log in":
                self.log_in()
            else:
                break


    @staticmethod
    def show_users_with_details(role):
        user_list = User.get_user_list_by_role(role)
        UserInterface.show_users_with_details_table(user_list)


    @staticmethod
    def show_students_with_grades():
        user_list = User.get_user_list_by_role('student')
        UserInterface.show_students_with_grades_table(user_list)

class StudentMenu:
    """Student menu options"""
    def __init__(self, user):
        while True:
            user_choice = UserInterface.student_menu()
            os.system("clear")
            if user_choice == "Submit an assignment":
                MenuMethods.submit_an_assignment(user)
            elif user_choice == "View my grades":
                MenuMethods.view_my_grades(user)
            elif user_choice == "View my overall grade":
                MenuMethods.view_my_grades(user)
            elif user_choice == "View my submissions":
                MenuMethods.view_my_submissions(user)
            elif user_choice == "View assignments":
                MenuMethods.view_assignments()
            elif user_choice == "Log out":
                break


class MentorMenu:
    """Mentor menu options"""

    def __init__(self, user):
        while True:
            user_choice = UserInterface.mentor_menu()
            os.system("clear")
            if user_choice == "Show students list":
                MenuMethods.show_student_list()
            elif user_choice == "Show assignments":
                MenuMethods.show_assignments()
            elif user_choice == "Add an assignment":
                MenuMethods.add_an_assignment()
            elif user_choice == "Grade an assignment":
                MenuMethods.grade_an_assignment()
            elif user_choice == "Check attendance":
                MenuMethods.check_attendance()
            elif user_choice == "Show attendance":
                MenuMethods.show_attendance()
            elif user_choice == "Add student":
                MenuMethods.add_student()
            elif user_choice == "Remove student":
                MenuMethods.remove_student()
            elif user_choice == "Edit student data":
                MenuMethods.edit_user_student_data()
            elif user_choice == "Create team":
                MenuMethods.create_team()
            elif user_choice == "Add student to team":
                MenuMethods.add_student_to_team()
            elif user_choice == "Show teams":
                MenuMethods.show_teams()
            elif user_choice == "Log out":
                break


class BossMenu:
    """Class that represents boss menu.
       Functions:
       Add a mentor
       Remove a mentor
       Show mentors list
       Show students list
        """

    def __init__(self, user):
        while True:
            user_choice = UserInterface.boss_menu()
            os.system("clear")
            if user_choice == "Add a mentor":
                MenuMethods.add_a_mentor()
            elif user_choice == "Remove a mentor":
                MenuMethods.remove_a_mentor()
            elif user_choice == "Edit mentor data":
                MenuMethods.edit_mentor_data()
            elif user_choice == "Show mentors list":
                MenuMethods.show_mentor_list()
            elif user_choice == "Show students list":
                MenuMethods.show_student_list()
            elif user_choice == "Show students average grade":
                MenuMethods.show_student_average_grade()
            elif user_choice == "Log out":
                break


class StaffMenu:
    """Class that represents staff menu.
       Functions "Show students list", "Log out" """
    def __init__(self, user):
        while True:
            user_choice = UserInterface.staff_menu()
            os.system("clear")
            if user_choice == "Show students list":
                MenuMethods.show_student_list()
            elif user_choice == "Log out":
                break


class MenuMethods:
    """Gather methods from menus"""

    # StudentMenu:

    @staticmethod
    def submit_an_assignment(user):
        UserInterface.show_assignments_table(Assignment.get_assignment_list())
        data_for_submission = UserInterface.get_submit_data(user, Assignment.get_assignment_list())
        if data_for_submission is not None:
            Submission.add_submission(*data_for_submission)

    @staticmethod
    def view_my_grades(user):
        UserInterface.show_submissions_table(user.submission_list, 'graded')

    @staticmethod
    def view_my_overall_grade(user):
        UserInterface.print_line(Student.get_overall_grade(user))

    @staticmethod
    def view_my_submissions(user):
        UserInterface.show_submissions_table(user.submission_list)

    @staticmethod
    def view_assignments():
        UserInterface.show_assignments_table(Assignment.get_assignment_list())

    # MentorMenu:

    @staticmethod
    def edit_user_student_data():
        while True:
            option_choice = UserInterface.edit_user_menu()
            os.system("clear")
            if option_choice == "Back":
                break
            user_list = User.get_user_list_by_role('student')
            UserInterface.show_users_with_details_table(user_list)
            user_id = UserInterface.item_id_from_list(user_list, 'person')
            if user_id is None:
                break
            user_to_edit = User.get_user_by_id(user_id)
            if option_choice == "Edit student attendance status":
                student_attendances_to_edit_one = UserInterface.attendance_id_from_list(user_to_edit.attendance_list, user_to_edit)
                student_attendance_to_edit = UserInterface.edit_user_status(student_attendances_to_edit_one)
                student_attendances_to_edit_one.set_status(student_attendance_to_edit)
            elif option_choice == "Edit student name":
                user_to_edit.set_name(UserInterface.edit_user_name(user_to_edit))
            elif option_choice == "Edit student mail":
                user_to_edit.set_mail(UserInterface.edit_user_mail(user_to_edit))
            elif option_choice == "Edit student password":
                user_to_edit.set_password(UserInterface.edit_user_password(user_to_edit))

    @staticmethod
    def show_student_list():
        Menu.show_users_with_details('student')

    @staticmethod
    def show_assignments():
        UserInterface.show_assignments_table(Assignment.get_assignment_list())

    @staticmethod
    def add_an_assignment():
        UserInterface.show_assignments_table(Assignment.get_assignment_list())
        Assignment.add_assignment(*UserInterface.get_assignment_data())

    @staticmethod
    def grade_an_assignment():
        UserInterface.show_assignments_table(Assignment.get_assignment_list())
        assignment_id = UserInterface.item_id_from_list(Assignment.get_assignment_list(), 'assignment')
        if assignment_id:
            assignment = Assignment.get_assignment_by_id(assignment_id)
            submission_list = Submission.create_submission_list_by_assignment_id(assignment_id)
            UserInterface.show_submissions_table(submission_list)
            grade_data = UserInterface.get_grade_assignment_data(submission_list, assignment)
            if grade_data:
                Submission.set_grade_submission(*grade_data)

    @staticmethod
    def check_attendance():
        for student in Student.get_user_list():
            Attendance.add_attendance(*UserInterface.get_attendance_data(student))

    @staticmethod
    def show_attendance():
        UserInterface.show_attendance_table(Attendance.get_attendance_list())

    @staticmethod
    def add_student():
        Student.add_user(*UserInterface.get_user_data())

    @staticmethod
    def remove_student():
        user_list = User.get_user_list_by_role('student')
        UserInterface.show_users_table(user_list)
        Student.remove_user(UserInterface.item_id_from_list(user_list, 'person'))

    @staticmethod
    def create_team():
        name = UserInterface.get_team_name()
        Team.add_team(name)

    @staticmethod
    def add_student_to_team():
        team_list = Team.get_list_teams()
        UserInterface.show_teams_table(team_list)
        team_id_from_user = UserInterface.item_id_from_list(Team.get_list_teams(), 'team')
        UserInterface.show_users_table(User.get_user_list_by_role('student'))
        student_id_from_user = UserInterface.item_id_from_list(User.get_user_list_by_role('student'), 'student')
        DB.create_member_record(team_id_from_user, student_id_from_user)

    @staticmethod
    def show_teams():
        UserInterface.show_teams_table(Team.get_list_teams())
        team_id_from_user = UserInterface.item_id_from_list(Team.get_list_teams(), 'team')
        members_id = DB.read_user_id_list_by_team_id(team_id_from_user)
        user_list = User.get_user_list_by_id_list(members_id)
        UserInterface.show_users_table(user_list)

    # BossMenu:

    @staticmethod
    def edit_user_mentor_data():
        while True:
            option_choice = UserInterface.edit_mentor_menu()
            os.system("clear")
            if option_choice == "Back":
                break
            user_list = User.get_user_list_by_role('mentor')
            UserInterface.show_users_with_details_table(user_list)
            user_id = UserInterface.item_id_from_list(user_list, 'person')
            if user_id is None:
                break
            user_to_edit = User.get_user_by_id(user_id)
            if option_choice == "Edit mentor name":
                user_to_edit.set_name(UserInterface.edit_user_name(user_to_edit))
            elif option_choice == "Edit mentor mail":
                user_to_edit.set_mail(UserInterface.edit_user_mail(user_to_edit))
            elif option_choice == "Edit mentor password":
                user_to_edit.set_password(UserInterface.edit_user_password(user_to_edit))

    @staticmethod
    def add_a_mentor():
        Mentor.add_user(*UserInterface.new_mentor())

    @staticmethod
    def remove_a_mentor():
        user_list = User.get_user_list_by_role('mentor')
        UserInterface.show_users_table(user_list)
        Mentor.remove_user(UserInterface.item_id_from_list(user_list, 'person'))

    @staticmethod
    def edit_mentor_data():
        MenuMethods.edit_user_mentor_data()

    @staticmethod
    def show_mentor_list():
        Menu.show_users_with_details('mentor')

    @staticmethod
    def show_student_average_grade():
        Menu.show_students_with_grades()


def main():
    Menu()

if __name__ == "__main__":
    main()
