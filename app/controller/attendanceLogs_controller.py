from flask import request, jsonify
from app.service.attendanceLogs_service import AttendanceLogsService
from app.model.attendanceLogs import AttendanceLogs
from sqlalchemy.exc import IntegrityError

class AttendanceLogsController:
    @staticmethod
    def get_all_attendance_logs():
        logs = AttendanceLogsService.get_all_attendance_logs()
        return jsonify([log.to_dict() for log in logs], 200)