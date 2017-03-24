from db_controller import DB
import models.users


class Checkpoint:
    """Class that represents checkpoint"""

    def __init__(self, checkpoint_id, student_id, date, title, card):
        """Checkpoint attributes - student instance and its card, date of checkpoint checking"""
        self.id = checkpoint_id
        self.student = models.users.User.get_user_by_id(student_id)
        self.date = date
        self.title = title
        self.card = card

    @classmethod
    def get_checkpoint_by_id(cls, checkpoint_id):
        """
        Returns Checkpoint instance
        :return:
            checkpoint: object
        """
        return cls.create_checkpoint_by_id(checkpoint_id)

    @classmethod
    def get_checkpoint_list_by_student_id(cls, student_id):
        """
        Returns list of Checkpoint instances
        :return:
            checkpoint_list: list
        """
        return cls.create_checkpoint_list_by_student_id(student_id)

    @classmethod
    def get_checkpoint_list_by_date(cls, date):
        """
        Returns list of Checkpoint instances
        :return:
            checkpoint_list: list
        """
        return cls.create_checkpoint_list_by_date(date)

    @classmethod
    def get_checkpoint_list_by_title(cls, title):
        """
        Returns list of Checkpoint instances
        :return:
            checkpoint_list: list
        """
        return cls.create_checkpoint_list_by_title(title)

    @classmethod
    def get_checkpoint_list(cls):
        """
        Returns list of Checkpoint instances
        :return:
            checkpoint_list: list
        """
        return cls.create_checkpoint_list()

    @classmethod
    def get_overall_checkpoint(cls, student_id):
        """
        Returns overall checkpoint
        :return:
            overall checkpoint: str
        """
        return cls.create_overall_checkpoint(student_id)

    @classmethod
    def get_all_overall_checkpoint(cls):
        """
        Returns all students overall checkpoints
        :return:
            all students overall checkpoint: str
        """
        return cls.create_all_overall_checkpoint()

    @classmethod
    def get_overall_checkpoint_by_date(cls, date):
        """
        Return all students overall checkpoints by date
        :return:
            all students overall checkpoints by date
        """
        return cls.create_overall_checkpoint_by_date(date)

    @classmethod
    def create_checkpoint_by_id(cls, checkpoint_id):
        """
        Creates Checkpoint instance
        :return:
            checkpoint: object
        """
        args = DB.read_checkpoint_record_by_id(checkpoint_id)
        return Checkpoint(*args[0])

    @classmethod
    def create_checkpoint_list_by_date(cls, date):
        """
        Creates list of Checkpoint instances
        :return:
            checkpoint_list: list
        """
        checkpoint_data = DB.read_checkpoint_record_list_by_date(date)
        return [Checkpoint(*checkpoint) for checkpoint in checkpoint_data]

    @classmethod
    def create_checkpoint_list_by_title(cls, title):
        """
        Creates list of Checkpoint instances
        :return:
            checkpoint_list: list
        """
        checkpoint_data = DB.read_checkpoint_record_list_by_title(title)
        return [Checkpoint(*checkpoint) for checkpoint in checkpoint_data]

    @classmethod
    def create_checkpoint_list_by_student_id(cls, student_id):
        """
        Creates list of Checkpoint instances
        :return:
            checkpoint_list: list
        """
        checkpoint_data = DB.read_checkpoint_record_list_by_student_id(student_id)
        return [Checkpoint(*checkpoint) for checkpoint in checkpoint_data]

    @classmethod
    def create_checkpoint_list(cls):
        """
        Creates list of Checkpoint instances
        :return:
            checkpoint_list: list
        """
        checkpoint_data = DB.read_checkpoint_record_list()
        return [Checkpoint(*checkpoint) for checkpoint in checkpoint_data]

    @classmethod
    def create_overall_checkpoint(cls, student_id):
        """
        Creates overall_checkpoint
        :return:
            overall checkpoint: float
        """
        return DB.read_overall_checkpoint(student_id)

    @classmethod
    def create_all_overall_checkpoint(cls):
        """
        Creates all students overall checkpoint
        :return: overall checkpoint: float
        """
        return DB.read_all_overall_checkpoint()

    @classmethod
    def create_overall_checkpoint_by_date(cls, date):
        """
        Creates overall checkpoint for all students by date
        :param date: date
        :return: overall checkpoint by date: float
        """
        return DB.read_overall_checkpoint_by_date(date)

    @classmethod
    def update_checkpoint(cls, student_id, title, card):
        """
        Updates checkpoint
        """
        return DB.update_checkpoint(student_id, title, card)

    @classmethod
    def add_checkpoint(cls, student_id, date, title, card):
        card_dict = {'0': 0, '1': 1, '0.8': 0.8}
        values = (student_id, date, title, card_dict[card])
        new_checkpoint_id = DB.create_checkpoint_record(values)
        new_checkpoint = cls.get_checkpoint_by_id(new_checkpoint_id)
        return new_checkpoint

    def get_id(self):
        """Returns checkpoint instance id"""
        return self.id

    def get_student(self):
        """Returns student instance is subject to the checkpoint object"""
        return self.student

    def get_date(self):
        """Returns date is subject to the checkpoint object (string)"""
        return self.date

    def get_card(self):
        """Returns student card from checkpoint instance"""
        return self.card

    def get_title(self):
        """Returns checkpoint title from checkpoint instance"""
        return self.title

    def set_card(self, new_card):
        """Sets new card of students checkpoint"""
        self.card = new_card
        DB.update_checkpoint(self.student.get_id(), self.get_date(), self.get_title(), new_card)
