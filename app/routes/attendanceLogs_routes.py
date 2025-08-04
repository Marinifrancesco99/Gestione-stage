from flask import Blueprint
from app.controller.attendanceLogs_controller import AttendanceLogsController
from app.utils.decorators import token_required, roles_required

attendanceLogs_bp = Blueprint('attendance_logs', __name__)

@attendanceLogs_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola", "tutor")
def get_all_attendance_logs():
    return AttendanceLogsController.get_all_attendance_logs

@attendanceLogs_bp.route("/<int:id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola", "tutor")
def get_attendance_log_by_id(id):
    return AttendanceLogsController.get_attendance_log_by_id(id)

@attendanceLogs_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "tutor")
def save_attendance_log():
    return AttendanceLogsController.save_attendance_log()

@attendanceLogs_bp.route("/<int:id>", methods=["PUT"])
@token_required
@roles_required("admin", "tutor")
def update_attendance_log(id):
    return AttendanceLogsController.update_attendance_log(id)

@attendanceLogs_bp.route("/<int:id>", methods=["DELETE"])
@token_required
@roles_required("admin")
def delete_attendance_log(id):
    return AttendanceLogsController.delete_attendance_log(id)

@attendanceLogs_bp.route("/internship/<int:internship_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola", "tutor")
def get_attendanceLog_by_internship_id(internship_id):
    return AttendanceLogsController.get_attendanceLog_by_internship_id(internship_id)

@attendanceLogs_bp.route("/tutor/<int:tutor_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola", "tutor")
def get_attendanceLog_by_tutor_id(tutor_id):
    return AttendanceLogsController.get_attendanceLog_by_tutor_id(tutor_id)