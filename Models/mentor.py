class Mentor:

    mentor_list = []

    def __init__(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password

    @classmethod
    def add_mentor(cls, mentor):
        cls.mentor_list.append(mentor)

    def edit_mentor(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password

    @classmethod
    def remove_mentor(cls, mentor):
        cls.mentor_list.remove(mentor)

