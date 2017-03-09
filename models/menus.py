from db_controller import DB


class Menu:
    def __init__(self, id_, name, url_for, url_for_args, upper_id, position):
        self.id = id_
        self.name = name
        self.url_for = url_for
        self.url_for_args = url_for_args
        self.position = position
        self.upper_menu_id = upper_id

    @property
    def submenus(self):
        return sorted(self.get_menu_by_upper_menu_id(self.upper_menu_id), key=lambda x: x.position)

    @property
    def permissions(self):
        role_dict = {0: 'Mentor', 1: 'Student', 2: 'Staff', 3: 'Boss'}
        role_perm = DB.read_menu_permission(self.id)
        return [role_dict[index] for index, value in enumerate(role_perm) if value == 1]


    @classmethod
    def get_main_menu(cls):
        return cls.get_menu_by_upper_menu_id(upper_menu_id=0)

    @classmethod
    def get_menu_by_upper_menu_id(cls, upper_menu_id):
        menu_list_data = DB.read_menu_record_list_by_upper_menu_id(upper_menu_id)
        menu_list = []
        for data in menu_list_data:
            menu_list.append(Menu(*data))
        return menu_list



