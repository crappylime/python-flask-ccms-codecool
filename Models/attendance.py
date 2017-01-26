from Models.user import *


class Attendance:
    attendance_list = []

    def __init__(self, student, date, status):
        self.student = student
        self.date = date
        self.status = status
        Attendance.attendance_list.append(self)

    @classmethod
    def add_attendance(cls, student_name, date, status):
        """
         Adds attendance to Student submissions list.
         """
        student = Student.get_student(student_name)
        attendance = Attendance(student, date, status)
        student.attendance_list.append(attendance)

    @classmethod
    def get_attendance_list(cls):
        return cls.attendance_list

    def set_status(self, new_status):
        self.status = new_status
