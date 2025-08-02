from flask import request, jsonify
from app.service.attendanceLogs_service import AttendanceLogsService
from app.model.attendanceLogs import AttendanceLogs
from sqlalchemy.exc import IntegrityError

class AttendanceLogsController:
    @staticmethod
    def get_all_attendance_logs():
        logs = AttendanceLogsService.get_all_attendance_logs()
        return jsonify([log.to_dict() for log in logs]), 200
    
    @staticmethod
    def get_attendance_log_by_id(id):
        logs = AttendanceLogsService.get_attendanceLog_by_id(id)
        return jsonify(logs.to_dict()), 200