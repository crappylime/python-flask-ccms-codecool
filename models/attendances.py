from db_controller import DB
import models.users


class Attendance:
    """Class that represents attendance"""

    def __init__(self, attendance_id, student_id, date, status):
        """Attendance attributes - student instance and its status, date of attendance checking"""
        self.id = attendance_id
        self.student = models.users.User.get_user_by_id(student_id)
        self.date = date
        self.status = status

    @classmethod
    def get_attendance_by_id(cls, attendance_id):
        """
        Returns Attendance instance
        :return:
            attendance: object
        """
        return cls.create_attendance_by_id(attendance_id)

    @classmethod
    def get_attendance_list_by_student_id(cls, student_id):
        """
        Returns list of Attendance instances
        :return:
            attendance_list: list
        """
        return cls.create_attendance_list_by_student_id(student_id)

    @classmethod
    def get_attendance_list_by_date(cls, date):
        """
        Returns list of Attendance instances
        :return:
            attendance_list: list
        """
        return cls.create_attendance_list_by_date(date)

    @classmethod
    def get_attendance_list(cls):
        """
        Returns list of Attendance instances
        :return:
            attendance_list: list
        """
        return cls.create_attendance_list()

    @classmethod
    def get_overall_attendance(cls, student_id):
        """
        Returns overall attendance
        :return:
            overall attendance: str
        """
        return cls.create_overall_attendance(student_id)

    @classmethod
    def create_attendance_by_id(cls, attendance_id):
        """
        Creates Attendance instance
        :return:
            attendance: object
        """
        args = DB.read_attendance_record_by_id(attendance_id)
        return Attendance(*args[0])

    @classmethod
    def create_attendance_list_by_date(cls, date):
        """
        Creates list of Attendance instances
        :return:
            attendance_list: list
        """
        attendance_data = DB.read_attendance_record_list_by_date(date)
        return [Attendance(*attendance) for attendance in attendance_data]

    @classmethod
    def create_attendance_list_by_student_id(cls, student_id):
        """
        Creates list of Attendance instances
        :return:
            attendance_list: list
        """
        attendance_data = DB.read_attendance_record_list_by_student_id(student_id)
        return [Attendance(*attendance) for attendance in attendance_data]

    @classmethod
    def create_attendance_list(cls):
        """
        Creates list of Attendance instances
        :return:
            attendance_list: list
        """
        attendance_data = DB.read_attendance_record_list()
        return [Attendance(*attendance) for attendance in attendance_data]

    @classmethod
    def create_overall_attendance(cls, student_id):
        """
        Creates overall_attendance
        :return:
            overall attendance: str
        """
        return DB.read_overall_attendance(student_id)

    @classmethod
    def add_attendance(cls, student_id, date, status):
        status_dict = {'0': 0, '1': 1, 'L': 0.8}
        values = (student_id, date, status_dict[status])
        new_attendance_id = DB.create_attendance_record(values)
        new_attendance = cls.get_attendance_by_id(new_attendance_id)
        return new_attendance

    def get_id(self):
        """Returns attendance instance id"""
        return self.id

    def get_student(self):
        """Returns student instance is subject to the attendance object"""
        return self.student

    def get_date(self):
        """Returns date is subject to the attendance object (string)"""
        return self.date

    def get_status(self):
        """Returns student status from attendance instance"""
        return self.status

    def set_status(self, new_status):
        """Sets new status of students attendance"""
        self.status = new_status
        DB.update_attendance(self.student.get_id(), self.get_date(), new_status)
