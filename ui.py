from tabulate import tabulate


class UserInterface:
    @staticmethod
    def user_choice(options):
        while True:
            user_choice = input('Choose action: ')
            for index, option in enumerate(options):
                if user_choice == str(index + 1):
                    return option
            else:
                print("Wrong input")

    @staticmethod
    def main_menu():
        options = ['Log in', 'Exit']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def login():
        user_name = input('Provide your username: ')
        user_password = input('Provide your password: ')
        return (user_name, user_password)

    @staticmethod
    def login_error():
        print("Username or password is incorrect! ")

    @staticmethod
    def student_menu():
        options = ['View assignments', 'Submit an assignment', 'View my grades', 'View my submissions', 'Log out']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def get_submit_data(user):
        assignment_title = input("Please provide title of assignment: ")
        content = input("Please provide link to your assignment: ")
        date = input("What date is it today? ;p ") # Remember to import date
        owner_name = user.name
        return content, date, assignment_title, owner_name

    @staticmethod
    def view_grade(student):
        submission_title = input("What submission are you interested in? ")
        grade = student.get_grade(student.name, submission_title)
        if grade:
            print("Your score is :{}".format(grade))
        else:
            print("Your submission haven't been grade yet")

    @staticmethod
    def mentor_menu():
        options = ['Show students list', 'Add an assignment', 'Grade an assignment', 'Check attendance', 'Add student',
                   'Remove student', 'Edit student data', 'Log out']
        UserInterface.print_options_list(options)
        return UserInterface.user_choice(options)

    @staticmethod
    def get_assignment_data():
        title = input("Please provide assignment title: ")
        content = input("Please provide assignment content: ")
        due_date = input("Please provide due date: ")
        max_points = input("Plese set max points for this assignment: ")
        return title, content, due_date, max_points

    @staticmethod
    def get_grade_assignment_data():
        points = int(input("How much points do you want to add? "))
        owner_name = input("Whose assignment is it? ")
        return points, owner_name

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
        date = input("What date is it today? :) ")
        print(student.get_name())
        status = input("Is the student present?(0/1/L) ")
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
        mentor_mail = input('Please provide new mentor\'s mail')
        mentor_password = input('Please provide new mentor\'s password')
        return mentor_name, mentor_mail, mentor_password

    @staticmethod
    def user_name_from_list(list):
        UserInterface.show_list_with_index(list)
        try:
            user_choice = int(input('Please choose person by index: '))
            return list[user_choice - 1].get_name()
        except ValueError:
            print("Wrong input")


    @staticmethod
    def edit_user_data(user_to_edit):
        print(user_to_edit.get_name)
        new_name = input('Please provide new name: ')
        print(user_to_edit.get_mail)
        new_mail = input('Please provide new mail: ')
        print(user_to_edit.get_password)
        new_password = input('Please provide new password: ')
        return new_name, new_mail, new_password

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
            list_for_table.append([index +1, user.get_name()])

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
    def assignment_title_provide():
        title = input('Provide assignment title: ')
        return title

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
                if ass.points != None:
                    list_for_table.append([index + 1, ass.get_assignment().get_title(), ass.get_owner().get_name(),
                                           ass.get_content(), ass.get_date(), ass.get_points()])


        UserInterface.show_table(headers, list_for_table)
