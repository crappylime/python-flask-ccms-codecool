


class UserInterface:

    @staticmethod
    def login():
        user_name = input('Provide your username: ')
        user_password = input('Provide your password: ')
        return (user_name, user_password)

    @staticmethod
    def student_menu():
        options = ['Submit an assignment', 'View my grades', 'Log out']
        UserInterface.print_options_list(options)
        user_choice = input('Chose action: ')
        return option[user_choice - 1]

    @staticmethod
    def s_submit_an_assignment():


    @staticmethod
    def mentor_menu():
        options = ['Show students list', 'Add an assignment', 'Grade an assignment', 'Check attendance', 'Add student',
                   'Remove student', 'Edit student data', 'Log out']
        UserInterface.print_options_list(options)
        user_choice = input('Chose action: ')
        return option[user_choice - 1]

    @staticmethod
    def staff_menu():
        options = ['Show students list', 'Log out']
        UserInterface.print_options_list(options)
        user_choice = input('Chose action: ')
        return option[user_choice - 1]

    @staticmethod
    def boss_menu():
        options = ['Add a mentor', 'Remove a mentor', 'Edit mentor data', 'Show mentors list', 'Show students list',
                   'Log out']
        UserInterface.print_options_list(options)
        user_choice = input('Chose action: ')
        return option[user_choice - 1]

    @staticmethod
    def new_mentor():
        mentor_name = input('Please provide new mentor\'s name: ')
        mentor_mail = input('Please provide new mentor\'s mail')
        mentor_password = input('Please provide new mentor\'s password')
        return mentor_name, mentor_mail, mentor_password

    @staticmethod
    def mentor_to_remove_data():
        mentor_name = input('Please provide mentor\'s to remove name: ')
        return mentor_name

    @staticmethod
    def mentor_to_edit_name():
        mentor_name = input('Please provide mentor\'s to edit name: ')
        return mentor_name

    @staticmethod
    def edit_mentor_data(mentor_to_edit):
        print(mentor_to_edit.get_name)
        new_name = input('Please provide new name: ')
        print(mentor_to_edit.get_mail)
        new_mail = input('Please provide new mail: ')
        print(mentor_to_edit.get_password)
        new_password = input('Please provide new password: ')
        return new_name, new_mail, new_password




    @staticmethod
    def print_options_list(list):
        """print indices (each increased by 1) and elements from provided list as a column"""
        for index, option in enumerate(list):
            print('  (' + (str(index + 1)) + ') ' + str(option))









>>>>>>> df3de584d75ce1a4ab20acabe1cd3eaa6716d925
