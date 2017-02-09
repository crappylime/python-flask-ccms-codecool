from Models.submission import *
from Models.assignment import *
from Models.attendance import *
from ui import *
import os


class Menu:
    """log in menu with import/export csv"""

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
        Program.import_all_csv()

        while True:
            user_choice = UserInterface.main_menu()
            os.system("clear")
            if user_choice == "Log in":
                self.log_in()
            else:
                break
        Program.export_all_cvs()

    @staticmethod
    def show_students():
        UserInterface.show_users_table(Student.get_student_list())
        student_to_show_name = UserInterface.user_name_from_list(Student.get_student_list())
        student_to_show = Student.get_student(student_to_show_name)
        UserInterface.show_user(student_to_show)


class StudentMenu:
    """Student menu options"""
    def __init__(self, user):
        while True:
            user_choice = UserInterface.student_menu()
            os.system("clear")
            if user_choice == "Submit an assignment":
                UserInterface.show_assignments_table(Assignment.get_list_assignmnent())
                data_for_submission = UserInterface.get_submit_data(user, Assignment.get_list_assignmnent())
                if data_for_submission is not None:
                    Submission.add_submission(*data_for_submission)
            elif user_choice == "View my grades":
                UserInterface.show_submissions_table(user.submission_list, 'graded')
            elif user_choice == "View my submissions":
                UserInterface.show_submissions_table(user.submission_list)
            elif user_choice == "View assignments":
                UserInterface.show_assignments_table(Assignment.get_list_assignmnent())
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
            UserInterface.show_users_table(Student.get_student_list())
            student_to_edit_name = UserInterface.user_name_from_list(Student.get_student_list())
            student_to_edit = Student.get_student(student_to_edit_name)
            if option_choice == "Edit student attendance status":
                student_attendances_to_edit_one = UserInterface.attendance_id_from_list(student_to_edit.attendance_list, student_to_edit)
                student_attendance_to_edit = UserInterface.edit_user_status(student_attendances_to_edit_one)
                student_attendances_to_edit_one.set_status(student_attendance_to_edit)
            elif option_choice == "Edit student name":
                student_to_edit.set_name(UserInterface.edit_user_name(student_to_edit))
            elif option_choice == "Edit student mail":
                student_to_edit.set_mail(UserInterface.edit_user_mail(student_to_edit))
            elif option_choice == "Edit student password":
                student_to_edit.set_password(UserInterface.edit_user_password(student_to_edit))

    def __init__(self, user):
        while True:
            user_choice = UserInterface.mentor_menu()
            os.system("clear")
            if user_choice == "Show students list":
                Menu.show_students()
            elif user_choice == "Show assignments":
                UserInterface.show_assignments_table(Assignment.get_list_assignmnent())
            elif user_choice == "Add an assignment":
                UserInterface.show_assignments_table(Assignment.get_list_assignmnent())
                Assignment.add_assignment(*UserInterface.get_assignment_data())
            elif user_choice == "Grade an assignment":
                UserInterface.show_assignments_table(Assignment.get_list_assignmnent())
                assignment_title = UserInterface.assignment_title_provide(Assignment.get_list_assignmnent())
                if assignment_title is not None:
                    assignment = Assignment.get_assignment(assignment_title)
                    UserInterface.show_submissions_table(assignment.get_list_submission())
                    grade_data = UserInterface.get_grade_assignment_data(assignment.get_list_submission(), assignment)
                    if grade_data is not None:
                        assignment.set_grade_submission(*grade_data)
            elif user_choice == "Check attendance":
                for student in Student.get_student_list():
                    Attendance.add_attendance(*UserInterface.get_attendance_data(student))
            elif user_choice == "Show attendance":
                UserInterface.show_attendance_table(Attendance.get_attendance_list())
            elif user_choice == "Add student":
                Student.add_student(*UserInterface.get_user_data())
            elif user_choice == "Remove student":
                UserInterface.show_users_table(Student.get_student_list())
                Student.remove_student(UserInterface.get_remove_data())
            elif user_choice == "Edit student data":
                MentorMenu.edit_user_data()
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
            UserInterface.show_users_table(Mentor.get_list_mentor())
            mentor_to_edit_name = UserInterface.user_name_from_list(Mentor.get_list_mentor())
            mentor_to_edit = Mentor.get_mentor(mentor_to_edit_name)
            if option_choice == "Edit mentor name":
                mentor_to_edit.set_name(UserInterface.edit_user_name(mentor_to_edit))
            elif option_choice == "Edit mentor mail":
                mentor_to_edit.set_mail(UserInterface.edit_user_mail(mentor_to_edit))
            elif option_choice == "Edit mentor password":
                mentor_to_edit.set_password(UserInterface.edit_user_password(mentor_to_edit))

    def __init__(self, user):
        while True:
            user_choice = UserInterface.boss_menu()
            os.system("clear")
            if user_choice == "Add a mentor":
                Mentor.add_mentor(*UserInterface.new_mentor())
            elif user_choice == "Remove a mentor":
                mentor_to_remove_name = UserInterface.user_name_from_list(Mentor.get_list_mentor())
                Mentor.remove_mentor(mentor_to_remove_name)
            elif user_choice == "Edit mentor data":
                BossMenu.edit_user_data()
            elif user_choice == "Show mentors list":
                UserInterface.show_users_table(Mentor.get_list_mentor())
                mentor_to_show_name = UserInterface.user_name_from_list(Mentor.get_list_mentor())
                mentor_to_show = Mentor.get_mentor(mentor_to_show_name)
                UserInterface.show_user(mentor_to_show)
            elif user_choice == "Show students list":
                Menu.show_students()
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
                Menu.show_students()
            elif user_choice == "Log out":
                break


def main():
    Menu()

if __name__ == "__main__":
    main()
