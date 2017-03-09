class MainMenu:
    def __init__(self, name, permissions):
        self.name = name
        self.submenus = []
        self.permissions = permissions

class SubMenu:
    def __init__(self, name, url_for, url_for_args, permisions, mainmenu, position):
       pass