from flask import Blueprint
from app.controller.attendanceLogs_controller import AttendanceLogsController

attendanceLogs_bp = Blueprint('attendance_logs', __name__)
attendanceLogs_bp.route("/", methods=["GET"])(AttendanceLogsController.get_all_attendance_logs)
attendanceLogs_bp.route("/<int:id>", methods=["GET"])(AttendanceLogsController.get_attendance_log_by_id)
attendanceLogs_bp.route("/", methods=["POST"])(AttendanceLogsController.save_attendance_log)
attendanceLogs_bp.route("/<int:id>", methods=["PUT"])(AttendanceLogsController.update_attendance_log)
attendanceLogs_bp.route("/<int:id>", methods=["DELETE"])(AttendanceLogsController.delete_attendance_log)
attendanceLogs_bp.route("/internship/<int:internship_id>", methods=["GET"])(AttendanceLogsController.get_attendanceLog_by_internship_id)
attendanceLogs_bp.route("/tutor/<int:tutor_id>", methods=["GET"])(AttendanceLogsController.get_attendanceLog_by_tutor_id)
