from Models.user import *
from db import *


class Attendance:
    """Class that represents attendance"""
    attendance_list = []

    def __init__(self, id, student, date, status):
        """Attendance attributes - student instance and its status, date of attendance checking"""
        self.id = id
        self.student = student
        self.date = date
        self.status = status
        Attendance.attendance_list.append(self)

    @classmethod
    def add_attendance(cls, student_id, date, status):
        values = (student_id, date, status)
        new_attendance_id = DB.create_attendance_record(values)
        new_attendance = cls.get_attendance_by_id(new_attendance_id)
        return new_attendance

    @classmethod
    def get_attendance_list(cls):
        """"Returns list with attendance instances"""
        return cls.attendance_list

    def get_id(self):
        """Returns attendance id"""
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
        DB.update_attendance(student.get_id(), self.get_date(), new_status)

