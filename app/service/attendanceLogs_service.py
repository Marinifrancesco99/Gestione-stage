from app.dao.attendanceLogs_dao import AttendanceLogDAO
from app.exceptions.not_found import NotFoundException

class AttendanceLogsService:
    @staticmethod
    def get_all_attendance_logs():
        return AttendanceLogDAO.get_all_attendanceLogs()
    
    @staticmethod
    def get_attendanceLog_by_id(id):
        attendance_log = AttendanceLogDAO.get_attendanceLog_by_id(id)
        if not attendance_log:
            raise NotFoundException(f"Attendance log with id: {id} not found.")
        return attendance_log
    
    @staticmethod
    def save_attendanceLog(date, start_time, end_time, notes, register_signature, tutor_id, internship_id, validation=False):
        return AttendanceLogDAO.create_attendanceLog(date, start_time, end_time, notes, register_signature, tutor_id, internship_id, validation)
    
    @staticmethod
    def get_attendanceLog_by_internship_id(internship_id):
        attendance_logs = AttendanceLogDAO.get_attendanceLog_by_internship_id(internship_id)
        return attendance_logs
    
    @staticmethod
    def get_attendanceLog_by_tutor_id(tutor_id):
        attendance_logs = AttendanceLogDAO.get_attendanceLog_by_tutor_id(tutor_id)
        return attendance_logs
    
    @staticmethod
    def update_attendanceLog(id, date=None, start_time=None, end_time=None, notes=None, register_signature=None, validation=None):
        existing_log = AttendanceLogDAO.get_attendanceLog_by_id(id)
        return AttendanceLogDAO.update_attendanceLog(id, date, start_time, end_time, notes, register_signature, validation)
    
    @staticmethod
    def delete_attendanceLog(id):
        attendance_log = AttendanceLogDAO.get_attendanceLog_by_id(id)
        AttendanceLogDAO.delete_attendanceLog(id)
        return True