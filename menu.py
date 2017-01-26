from Models.submission import *
from Models.assignment import *
from Models.attendance import *
from program import *
from ui import *


class Menu:
    def log_in(self):
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
                    break

    def __init__(self):
        Program.import_all_csv()

        while True:
            user_choice = UserInterface.main_menu()
            if user_choice == "Log in":
                self.log_in()
            else:
                break
        Program.export_all_cvs()


class StudentMenu:
    def __init__(self, user):
        while True:
            user_choice = UserInterface.student_menu()
            if user_choice == "Submit an assignment":
                UserInterface.show_assignments_table(Assignment.get_list_assignmnent())
                Submission.add_submission(*UserInterface.get_submit_data(user))
            elif user_choice == "View my grades":
                UserInterface.show_submissions_table(user.submission_list, 'graded')
            elif user_choice == "View my submissions":
                UserInterface.show_submissions_table(user.submission_list)
            elif user_choice == "View assignments":
                UserInterface.show_assignments_table(Assignment.get_list_assignmnent())
            elif user_choice == "Log out":
                break


class MentorMenu:
    def __init__(self, user):
        while True:
            user_choice = UserInterface.mentor_menu()
            if user_choice == "Show students list":
                UserInterface.show_students_table(Student.get_student_list())
            elif user_choice == "Add an assignment":
                Assignment.add_assignment(*UserInterface.get_assignment_data())
            elif user_choice == "Grade an assignment":
                UserInterface.show_assignments_table(Assignment.get_list_assignmnent())
                assignment = Assignment.get_assignment(UserInterface.assignment_title_provide())
                UserInterface.show_submissions_table(assignment.get_list_submission())
                assignment.set_grade_submission(*UserInterface.get_grade_assignment_data())
            elif user_choice == "Check attendance":
                for student in Student.get_student_list():
                    Attendance.add_attendance(*UserInterface.get_attendance_data(student))
            elif user_choice == "Add student":
                Student.add_student(*UserInterface.get_user_data())
            elif user_choice == "Remove student":
                Student.remove_student(UserInterface.get_remove_data())
            elif user_choice == "Edit student data":
                student_to_edit_name = UserInterface.user_name_from_list(Student.get_student_list())
                student_to_edit = Student.get_student(student_to_edit_name)
                student_to_edit.edit_student(*UserInterface.edit_user_data(student_to_edit))
            elif user_choice == "Log out":
                break


class BossMenu:

    def __init__(self, user):
        while True:
            user_choice = UserInterface.boss_menu()
            if user_choice == "Add a mentor":
                Mentor.add_mentor(*UserInterface.new_mentor())
            elif user_choice == "Remove a mentor":
                mentor_to_remove_name = UserInterface.user_name_from_list(Mentor.get_list_mentor())
                Mentor.remove_mentor(mentor_to_remove_name)
            elif user_choice == "Edit mentor data":
                mentor_to_edit_name = UserInterface.user_name_from_list(Mentor.get_list_mentor())
                mentor_to_edit = Mentor.get_mentor(mentor_to_edit_name)
                mentor_to_edit.edit_mentor(*UserInterface.edit_user_data(mentor_to_edit))
            elif user_choice == "Show mentors list":
                UserInterface.show_list(Mentor.get_list_mentor())
            elif user_choice == "Show students list":
                UserInterface.show_list(Student.get_student_list())
            elif user_choice == "Log out":
                break


class StaffMenu:
    def __init__(self, user):
        while True:
            user_choice = UserInterface.staff_menu()
            if user_choice == "Show students list":
                UserInterface.show_list(Student.get_student_list())
            elif user_choice == "Log out":
                break


def main():
    Menu()

if __name__ == "__main__":
    main()
