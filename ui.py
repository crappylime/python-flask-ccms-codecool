from tabulate import tabulate
import time
import re


class UserInterface:
    @staticmethod
    def user_choice(options):
        """Returns chosen option or prints error if it appears"""
        while True:
            user_choice = input('Choose action: ')
            for index, option in enumerate(options):
                if user_choice == str(index + 1):
                    return option
            else:
                print("Wrong input :-(")

    @staticmethod
    def main_menu():
        """Prints options list and returns user_choice()"""
        options = ['Log in', 'Exit']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def login():
        """Asks user for input and returns it"""
        user_name = input('Provide your username: ')
        user_password = input('Provide your password: ')
        return user_name, user_password

    @staticmethod
    def login_error():
        """Prints login error"""
        print("Username or password is incorrect!")

    @staticmethod
    def student_menu():
        """Prints options list and returns user_choice()"""
        options = ['View assignments', 'Submit an assignment', 'View my grades', 'View my overall grade', 'View my submissions', 'Log out']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def get_submit_data(user, assignment_list):
        """Returns user input about submission"""
        assignment_id = UserInterface.item_id_from_list(assignment_list, "assignment")
        unique = True
        for item in assignment_list:
            if item.get_id() == assignment_id:
                for sub in user.get_submission_list():
                    if sub.assignment.get_id() == assignment_id:
                        unique = False
                        print('\nThis assignment has already been submitted!\n')
                if unique:
                    content = input("Please provide link to your assignment: ")
                    date = time.strftime("%Y-%m-%-d %H:%M")
                    owner_id = user.get_id()
                    print('\nAssignment submitted successfully!\n')
                    return assignment_id, owner_id, content, date

        if unique is True:
            print('\nThere\'s no assignment with given ID!\n')

    @staticmethod
    def view_grade(student):
        """Chooses submission and prints information about grade"""
        submission_title = input("What submission are you interested in? ")
        grade = student.get_grade(student.name, submission_title)
        if grade:
            print("Your score is :{}".format(grade))
        else:
            print("Your submission haven't been grade yet.")

    @staticmethod
    def mentor_menu():
        """Prints options list and returns user_choice()"""
        options = ['Show students list', 'Show assignments', 'Add an assignment', 'Grade an assignment',
                   'Check attendance', 'Show attendance', 'Add student', 'Remove student', 'Edit student data',
                   'Create team', 'Add student to team', 'Show teams', 'Log out']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def get_assignment_data():
        """Returns user input about new assignment"""
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
        """Returns data about grading submission"""
        points = None

        while points is None or points > assigment_to_grade.max_points:
            provided_value = input("How much points do you want to add? ")
            if provided_value.isdigit() is True:
                points = int(provided_value)
                if int(points) > assigment_to_grade.max_points:
                    print('You exceed max points level for this assignment!')
            else:
                print('Please provide whole number!')

        sub_id = UserInterface.item_id_from_list(submission_list, 'submission')

        for item in submission_list:
            if item.get_id() == sub_id:
                return item.get_student().get_id(), item.get_assignment().get_id(), points

        print("\nThere's no submission with given id!\n")

    @staticmethod
    def get_user_data():
        """Returns user input about its data"""
        name = input("Please provide user name: ")
        mail = input("Please provide user e-mail: ")
        password = input("Please set user password: ")
        return name, mail, password

    @staticmethod
    def get_attendance_data(student):
        """Returns user input about student presence"""
        date = time.strftime("%Y-%m-%-d")
        print(student.get_name())
        while True:
            status = input("Is the student present?(0/1/L): ")
            if status not in ["0", "1", "L"]:
                print("Wrong input")
            else:
                return student.get_id(), date, status

    @staticmethod
    def staff_menu():
        """Prints options list and returns user_choice()"""
        options = ['Show students list', 'Log out']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def boss_menu():
        """Prints options list and returns user_choice()"""
        options = ['Add a mentor', 'Remove a mentor', 'Edit mentor data', 'Show mentors list', 'Show students list',
                   'Show students average grade', 'Log out']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def new_mentor():
        """Returns user input about new mentor"""
        mentor_name = input('Please provide new mentor\'s name: ')
        mentor_mail = input('Please provide new mentor\'s mail: ')
        mentor_password = input('Please provide new mentor\'s password: ')
        return mentor_name, mentor_mail, mentor_password


    @staticmethod
    def show_attendance_with_index(attendance_list, student_to_edit):
        """
        Prints attendance
        :param attendance_list:
        :param student_to_edit:
        """
        person_attendance_list = []
        for attendance in attendance_list:
            if attendance.get_student().get_name() == student_to_edit.get_name():
                person_attendance_list.append(attendance)

        for index, attendance in enumerate(person_attendance_list):
                print("({}) {} {}".format(str(index + 1), attendance.get_date(), attendance.get_status()))

    @staticmethod
    def attendance_id_from_list(attendance_list, student_to_edit):
        """
        Returns attendance object
        :param attendance_list:
        :param student_to_edit:
        :return:
            obj: attendance
        """
        UserInterface.show_attendance_with_index(attendance_list, student_to_edit)
        while True:
            user_choice = input('Please choose specific attendance by index: ')
            for index, attendance in enumerate(attendance_list):
                if user_choice == str(index + 1):
                    return attendance
            else:
                print("Wrong input :-(")

    @staticmethod
    def item_id_from_list(item_list, item_name):
        """
        Returns user id
        :param user_list:
        :return:
            int: user id
        """
        while True:
            user_choice = input('Please choose {} by index (Press x to go back): '.format(item_name))
            for item in item_list:
                if user_choice == str(item.get_id()):
                    user_choice = int(user_choice)
                    return user_choice
                elif user_choice == 'x':
                    return user_choice
            else:
                print("Wrong input :-(")

    @staticmethod
    def assignment_id_from_list(assignment_list):
        """
        Returns assignment id
        :param user_list:
        :return:
            int: user id
        """
        while True:
            user_choice = input('Please choose assignment by index: ')
            for ass in assignment_list:
                if user_choice == str(ass.get_id()):
                    user_choice = int(user_choice)
                    return user_choice
            else:
                print("Wrong input :-(")

    @staticmethod
    def edit_user_menu():
        """
        Calls user choice depending on options
        """
        options = ['Edit student attendance status', 'Edit student name', 'Edit student mail', 'Edit student password', 'Back']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def edit_mentor_menu():
        """
        Calls user choice depending on options
        """

        options = ['Edit mentor name', 'Edit mentor mail', 'Edit mentor password', 'Back']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def edit_user_status(student_attendances_to_edit_one):
        """
        Returns new attendance status
        :param student_attendances_to_edit_one:
        :return:
            str: new attendance status
        """
        while True:
            new_status = input("Is the student present?(0/1/L): ")
            if new_status not in ["0", "1", "L"]:
                print("Wrong input")
            else:
                return new_status

    @staticmethod
    def edit_user_name(user_to_edit):
        """
        Returns new user name
        :param user_to_edit:
        :return:
            str: new user name
        """
        print(user_to_edit.get_name())
        new_name = input('Please provide new name: ')
        return new_name

    @staticmethod
    def edit_user_mail(user_to_edit):
        """
        Returns new user mail
        :param user_to_edit:
        :return:
            str: new user password
        """
        print(user_to_edit.get_mail())
        new_mail = input('Please provide new mail: ')
        return new_mail

    @staticmethod
    def edit_user_password(user_to_edit):
        """
        Returns new user password
        :param user_to_edit:
        :return:
            str: new user password
        """
        print(user_to_edit.get_password())
        new_password = input('Please provide new password: ')
        return new_password

    @staticmethod
    def print_options_list(list):
        """print indices (each increased by 1) and elements from provided list as a column"""
        for index, option in enumerate(list):
            print('  (' + (str(index + 1)) + ') ' + str(option))

    @staticmethod
    def show_user(user):
        """
        Prints details of user
        :param user:
        """
        print("\n{}\n{}\n".format(user.get_name(), user.get_mail()))

    @staticmethod
    def show_table(headers, data):
        """
        Prints formatted table
        :param headers:
        :param data:
        """
        table = tabulate(data, headers, tablefmt='fancy_grid')
        print(table)

    @staticmethod
    def show_users_table(users):
        """
        Creates formatted table of users
        :param users:
        """
        headers = ['id', 'name']
        list_for_table = []
        for user in users:
            list_for_table.append([user.get_id(), user.get_name()])

        UserInterface.show_table(headers, list_for_table)

    @staticmethod
    def show_users_with_details_table(users):
        """
        Creates formatted table of users
        :param users:
        """
        headers = ['id', 'name', 'mail']
        list_for_table = []
        for user in users:
            list_for_table.append([user.get_id(), user.get_name(), user.get_mail()])

        UserInterface.show_table(headers, list_for_table)

    @staticmethod
    def show_students_with_grades_table(users):
        """
        Creates formatted table of users
        :param users:
        """
        headers = ['id', 'name', 'grade']
        list_for_table = []
        for user in users:
            list_for_table.append([user.get_id(), user.get_name(), user.get_overall_grade()])

        UserInterface.show_table(headers, list_for_table)

    @staticmethod
    def show_attendance_table(attendance_list):
        """
        Creates formatted attendance table
        :param attendance_list:
        """
        headers = ['id', 'student', 'date', 'status']
        list_for_table = []

        for attendance in attendance_list:
            list_for_table.append([attendance.get_id(), attendance.get_student().get_name(), attendance.get_date(), attendance.get_status()])

        UserInterface.show_table(headers, list_for_table)

    @staticmethod
    def show_assignments_table(assignments_list):
        """
        Creates formatted table of assignments
        :param assignments_list:
        """
        headers = ['id', 'title', 'content', 'due_date', 'max_points']
        list_for_table = []

        for assignment in assignments_list:
            list_for_table.append([assignment.get_id(), assignment.get_title(), assignment.get_content(),
                                   assignment.get_due_date(), assignment.get_max_points()])

        UserInterface.show_table(headers, list_for_table)

    @staticmethod
    def assignment_title_provide(assignments_list):
        """
        :param assignments_list:
        :return:
            str: title of assignment
        """
        title = input('Provide assignment title: ')
        for item in assignments_list:
            if item.title == title:
                return title
        print("There's no assignment with given title!")

    @staticmethod
    def show_submissions_table(submission_list, option='all'):
        """
        Creates formatted table of submissions
        :param submission_list:
        :param option:
        """
        headers = ['id', 'assignment title', 'owner', 'content', 'date', 'points']
        list_for_table = []

        if option == 'all':
            for submission in submission_list:
                list_for_table.append([submission.get_id(), submission.get_assignment().get_title(), submission.get_student().get_name(),
                                       submission.get_content(), submission.get_date(), submission.get_points()])
        else:
            for submission in submission_list:
                if submission.points is not None:
                    list_for_table.append([submission.get_id(), submission.get_assignment().get_title(), submission.get_student().get_name(),
                                           submission.get_content(), submission.get_date(), submission.get_points()])

        UserInterface.show_table(headers, list_for_table)

    @staticmethod
    def get_team_name():
        """Provide team name"""
        name = input("Provide team name: ")
        return name


    @staticmethod
    def show_teams_table(teams_list):
        """
        Creates formatted table of teams
        :param teams_list:
        """
        headers = ['team id', 'team name']
        list_for_table = []

        for team in teams_list:
            list_for_table.append([team.get_id(), team.get_name()])

        UserInterface.show_table(headers, list_for_table)

    @staticmethod
    def print_line(line):
        """
        Prints line into console
        """
        print(str(line) + "%")
