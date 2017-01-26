from tabulate import tabulate
import time
import re


class UserInterface:
    @staticmethod
    def user_choice(options):
        while True:
            user_choice = input('Choose action: ')
            for index, option in enumerate(options):
                if user_choice == str(index + 1):
                    return option
            else:
                print("Wrong input :-(")

    @staticmethod
    def main_menu():
        options = ['Log in', 'Exit']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def login():
        user_name = input('Provide your username: ')
        user_password = input('Provide your password: ')
        return user_name, user_password

    @staticmethod
    def login_error():
        print("Username or password is incorrect!")

    @staticmethod
    def student_menu():
        options = ['View assignments', 'Submit an assignment', 'View my grades', 'View my submissions', 'Log out']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def get_submit_data(user):
        assignment_title = input("Please provide title of assignment: ")
        unique = True
        for item in user.submission_list:
            if item.assignment.title == assignment_title:
                unique = False
                print('This assignment has already been submitted!')
        if unique is True:
            content = input("Please provide link to your assignment: ")
            date = time.strftime("%Y-%m-%-d %H:%M")
            owner_name = user.name
            return content, date, assignment_title, owner_name

    @staticmethod
    def view_grade(student):
        submission_title = input("What submission are you interested in? ")
        grade = student.get_grade(student.name, submission_title)
        if grade:
            print("Your score is :{}".format(grade))
        else:
            print("Your submission haven't been grade yet.")

    @staticmethod
    def mentor_menu():
        options = ['Show students list', 'Show assignments', 'Add an assignment', 'Grade an assignment',
                   'Check attendance', 'Show attendance', 'Add student', 'Remove student', 'Edit student data', 'Log out']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def get_assignment_data():
        title = input("Please provide assignment title: ")
        content = input("Please provide assignment content: ")

        date_pattern = re.compile(r'^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$')
        date_input = input("Please provide due date (yyyy-mm-dd): ")
        while not re.match(date_pattern, date_input):
            date_input = input("Please provide due date (yyyy-mm-dd): ")
        while True:
            max_points = input("Please set max points for this assignment: ")
            if max_points.isdigit():
                return title, content, date_input, max_points
            else:
                print("Points must be a number! ")

    @staticmethod
    def get_grade_assignment_data(submission_list, assigment_to_grade):
        points = None

        while points is None or points > assigment_to_grade.max_points:
            provided_value = input("How much points do you want to add? ")
            if provided_value.isdigit() is True:
                points = int(provided_value)
                if int(points) > assigment_to_grade.max_points:
                    print('You exceed max points level for this assignment!')
            else:
                print('Please provide whole number!')

        owner_name = input("Whose assignment is it? ")
        for item in submission_list:
            if item.owner.name == owner_name:
                return points, owner_name
        print("\nThere's no submission with given student name!\n")

    @staticmethod
    def get_user_data():
        name = input("Please provide user name: ")
        mail = input("Please provide user e-mail: ")
        password = input("Please set user password: ")
        return name, mail, password

    @staticmethod
    def get_remove_data():
        name = input("Please provide name of the person you would like to remove: ")
        return name

    @staticmethod
    def get_attendance_data(student):
        date = time.strftime("%Y-%m-%-d")
        print(student.get_name())
        while True:
            status = input("Is the student present?(0/1/L): ")
            if status not in ["0", "1", "L"]:
                print("Wrong input")
            else:
                return student, date, status

    @staticmethod
    def staff_menu():
        options = ['Show students list', 'Log out']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def boss_menu():
        options = ['Add a mentor', 'Remove a mentor', 'Edit mentor data', 'Show mentors list', 'Show students list',
                   'Log out']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def new_mentor():
        mentor_name = input('Please provide new mentor\'s name: ')
        mentor_mail = input('Please provide new mentor\'s mail: ')
        mentor_password = input('Please provide new mentor\'s password: ')
        return mentor_name, mentor_mail, mentor_password


    @staticmethod
    def show_attendance_with_index(attendance_list, student_to_edit):
        person_attendance_list = []
        for attendance in attendance_list:
            if attendance.get_student().get_name() == student_to_edit.get_name():
                person_attendance_list.append(attendance)

        for index, attendance in enumerate(person_attendance_list):
                print("({}) {} {}".format(str(index + 1), attendance.get_date(), attendance.get_status()))

    @staticmethod
    def attendance_id_from_list(attendance_list, student_to_edit):
        UserInterface.show_attendance_with_index(attendance_list, student_to_edit)
        while True:
            user_choice = input('Please choose specific attendance by index: ')
            for index, attendance in enumerate(attendance_list):
                if user_choice == str(index + 1):
                    return attendance
            else:
                print("Wrong input :-(")

    @staticmethod
    def user_name_from_list(user_list):
        UserInterface.show_list_with_index(user_list)
        while True:
            user_choice = input('Please choose person by index: ')
            for index, user in enumerate(user_list):
                if user_choice == str(index + 1):
                    return user.get_name()
            else:
                print("Wrong input :-(")

    @staticmethod
    def edit_user_menu():
        options = ['Edit student attendance status', 'Edit student name', 'Edit student mail', 'Edit student password', 'Back']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def edit_user_status(student_attendances_to_edit_one):
        while True:
            new_status = input("Is the student present?(0/1/L): ")
            if new_status not in ["0", "1", "L"]:
                print("Wrong input")
            else:
                return new_status

    @staticmethod
    def edit_user_name(user_to_edit):
        print(user_to_edit.get_name())
        new_name = input('Please provide new name: ')
        return new_name

    @staticmethod
    def edit_user_mail(user_to_edit):
        print(user_to_edit.get_mail())
        new_mail = input('Please provide new mail: ')
        return new_mail

    @staticmethod
    def edit_user_password(user_to_edit):
        print(user_to_edit.get_password())
        new_password = input('Please provide new password: ')
        return new_password

    @staticmethod
    def print_options_list(list):
        """print indices (each increased by 1) and elements from provided list as a column"""
        for index, option in enumerate(list):
            print('  (' + (str(index + 1)) + ') ' + str(option))

    @staticmethod
    def show_list(user_list):
        for user in user_list:
            print(user.get_name())

    @staticmethod
    def show_list_with_index(user_list):
        for index, user in enumerate(user_list):
            print('  (' + (str(index + 1)) + ') ' + user.get_name())

    @staticmethod
    def show_table(headers, data):
        table = tabulate(data, headers, tablefmt='fancy_grid')
        print(table)

    @staticmethod
    def show_students_table(users):
        headers = ['idx', 'name']
        list_for_table = []
        for index, user in enumerate(users):
            list_for_table.append([index + 1, user.get_name()])

        UserInterface.show_table(headers, list_for_table)

    @staticmethod
    def show_attendance_table(attendance_list):

        headers = ['idx', 'student', 'date', 'status']
        list_for_table = []

        for index, row in enumerate(attendance_list):
            list_for_table.append([index + 1, row.get_student().get_name(), row.get_date(), row.get_status()])

        UserInterface.show_table(headers, list_for_table)

    @staticmethod
    def show_assignments_table(assignments_list):

        headers = ['idx', 'title', 'content', 'due_date', 'max_points']
        list_for_table = []

        for index, ass in enumerate(assignments_list):
            list_for_table.append([index + 1, ass.get_title(), ass.get_content(),
                                   ass.get_due_date(), ass.get_max_points()])

        UserInterface.show_table(headers, list_for_table)

    @staticmethod
    def assignment_title_provide(assignments_list):
        title = input('Provide assignment title: ')
        for item in assignments_list:
            if item.title == title:
                return title
        print("There's no assignment with given title!")

    @staticmethod
    def show_submissions_table(submission_list, option='all'):

        headers = ['idx', 'assignment title', 'owner', 'content', 'date', 'points']
        list_for_table = []

        if option == 'all':
            for index, ass in enumerate(submission_list):
                list_for_table.append([index + 1, ass.get_assignment().get_title(), ass.get_owner().get_name(),
                                       ass.get_content(), ass.get_date(), ass.get_points()])
        else:
            for index, ass in enumerate(submission_list):
                if ass.points is not None:
                    list_for_table.append([index + 1, ass.get_assignment().get_title(), ass.get_owner().get_name(),
                                           ass.get_content(), ass.get_date(), ass.get_points()])

        UserInterface.show_table(headers, list_for_table)
