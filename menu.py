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


class StudentMenu:
    """Student menu options"""
    def __init__(self, user):
        while True:
            user_choice = UserInterface.student_menu()
            os.system("clear")
            if user_choice == "Submit an assignment":
                UserInterface.show_assignments_table(Assignment.get_assignment_list())
                data_for_submission = UserInterface.get_submit_data(user, Assignment.get_assignment_list())
                if data_for_submission is not None:
                    Submission.add_submission(*data_for_submission)
            elif user_choice == "View my grades":
                UserInterface.show_submissions_table(user.submission_list, 'graded')
            elif user_choice == "View my overall grade":
                UserInterface.print_line(Student.get_overall_grade(user))
            elif user_choice == "View my submissions":
                UserInterface.show_submissions_table(user.submission_list)
            elif user_choice == "View assignments":
                UserInterface.show_assignments_table(Assignment.get_assignment_list())
            elif user_choice == "Log out":
                break


class MentorMenu:
    """Mentor menu options"""
    @staticmethod
    def edit_user_data():
        while True:
            option_choice = UserInterface.edit_user_menu()
            os.system("clear")
            if option_choice == "Back":
                break
            user_list = User.get_user_list_by_role('student')
            UserInterface.show_users_with_details_table(user_list)
            user_id = UserInterface.item_id_from_list(user_list, 'person')
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

    def __init__(self, user):
        while True:
            user_choice = UserInterface.mentor_menu()
            os.system("clear")
            if user_choice == "Show students list":
                Menu.show_users_with_details('student')
            elif user_choice == "Show assignments":
                UserInterface.show_assignments_table(Assignment.get_assignment_list())
            elif user_choice == "Add an assignment":
                UserInterface.show_assignments_table(Assignment.get_assignment_list())
                Assignment.add_assignment(*UserInterface.get_assignment_data())
            elif user_choice == "Grade an assignment":
                UserInterface.show_assignments_table(Assignment.get_assignment_list())
                assignment_id = UserInterface.assignment_id_from_list(Assignment.get_assignment_list())
                if assignment_id is not None:
                    assignment = Assignment.get_assignment_by_id(assignment_id)
                    submission_list = Submission.create_submission_list_by_assignment_id(assignment_id)
                    UserInterface.show_submissions_table(submission_list)
                    grade_data = UserInterface.get_grade_assignment_data(submission_list, assignment)
                    if grade_data is not None:
                        Submission.set_grade_submission(*grade_data)
            elif user_choice == "Check attendance":
                for student in Student.get_user_list():
                    Attendance.add_attendance(*UserInterface.get_attendance_data(student))
            elif user_choice == "Show attendance":
                UserInterface.show_attendance_table(Attendance.get_attendance_list())
            elif user_choice == "Add student":
                Student.add_user(*UserInterface.get_user_data())
            elif user_choice == "Remove student":
                user_list = User.get_user_list_by_role('student')
                UserInterface.show_users_table(user_list)
                Student.remove_user(UserInterface.item_id_from_list(user_list, 'person'))
            elif user_choice == "Edit student data":
                MentorMenu.edit_user_data()
            elif user_choice == "Create team":  # TODO
                name = UserInterface.get_team_name()
                Team.add_team(name)
            elif user_choice == "Add student to team":  # TODO
                team_list = Team.get_list_teams()
                UserInterface.show_teams_table(team_list)
                team_id_from_user = UserInterface.item_id_from_list(Team.get_list_teams(), 'team')
                UserInterface.show_users_table(User.get_user_list_by_role('student'))
                student_id_from_user = UserInterface.item_id_from_list(User.get_user_list_by_role('student'), 'student')
                DB.create_member_record(team_id_from_user, student_id_from_user)
            elif user_choice == "Show teams":  # TODO
                UserInterface.show_teams_table(Team.get_list_teams())
                team_id_from_user = UserInterface.item_id_from_list(Team.get_list_teams(), 'team')
                members_id = DB.read_user_id_list_by_team_id(team_id_from_user)
                print('s:', members_id)
                user_list = User.get_user_list_by_id_list(members_id)
                UserInterface.show_users_table(user_list)
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
    @staticmethod
    def edit_user_data():
        while True:
            option_choice = UserInterface.edit_mentor_menu()
            os.system("clear")
            if option_choice == "Back":
                break
            user_list = User.get_user_list_by_role('mentor')
            UserInterface.show_users_with_details_table(user_list)
            user_id = UserInterface.item_id_from_list(user_list, 'person')
            user_to_edit = User.get_user_by_id(user_id)
            if option_choice == "Edit mentor name":
                user_to_edit.set_name(UserInterface.edit_user_name(user_to_edit))
            elif option_choice == "Edit mentor mail":
                user_to_edit.set_mail(UserInterface.edit_user_mail(user_to_edit))
            elif option_choice == "Edit mentor password":
                user_to_edit.set_password(UserInterface.edit_user_password(user_to_edit))

    def __init__(self, user):
        while True:
            user_choice = UserInterface.boss_menu()
            os.system("clear")
            if user_choice == "Add a mentor":
                Mentor.add_user(*UserInterface.new_mentor())
            elif user_choice == "Remove a mentor":
                user_list = User.get_user_list_by_role('mentor')
                UserInterface.show_users_table(user_list)
                Mentor.remove_user(UserInterface.item_id_from_list(user_list, 'person'))
            elif user_choice == "Edit mentor data":
                BossMenu.edit_user_data()
            elif user_choice == "Show mentors list":
                Menu.show_users_with_details('mentor')
            elif user_choice == "Show students list":
                Menu.show_users_with_details('student')
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
                Menu.show_users_with_details('student')
            elif user_choice == "Log out":
                break


def main():
    Menu()

if __name__ == "__main__":
    main()
