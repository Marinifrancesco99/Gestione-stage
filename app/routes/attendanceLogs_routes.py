from flask import Blueprint
from app.controller.attendanceLogs_controller import AttendanceLogsController

attendanceLogs_bp = Blueprint('attendance_logs', __name__)
attendanceLogs_bp.route("/", methods=["GET"])(AttendanceLogsController.get_all_attendance_logs)