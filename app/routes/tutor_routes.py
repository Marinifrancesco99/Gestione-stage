from flask import Blueprint
from app.controller.tutor_controller import TutorController
from utils.decorators import token_required, roles_required

tutor_bp = Blueprint('tutor', __name__)

@tutor_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_tutors():
    return TutorController.get_all_tutors()

@tutor_bp.route("/<int:tutor_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_tutor_by_id(tutor_id):
    return TutorController.get_tutor_by_id(tutor_id)

@tutor_bp.route("/email/<string:email>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_tutor_by_email(email):
    return TutorController.get_tutor_by_email(email)

@tutor_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def create_tutor():
    return TutorController.create_tutor()

@tutor_bp.route("/<int:tutor_id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_tutor(tutor_id):
    return TutorController.update_tutor(tutor_id)

@tutor_bp.route("/<int:tutor_id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_tutor(tutor_id):
    return TutorController.delete_tutor(tutor_id)

@tutor_bp.route("/<int:tutor_id>/attendance-logs", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_attendance_logs_for_tutor(tutor_id):
    return TutorController.get_attendance_logs_for_tutor(tutor_id)

@tutor_bp.route("/<int:tutor_id>/internship", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_internship_for_tutor(tutor_id):
    return TutorController.get_internship_for_tutor(tutor_id)

@tutor_bp.route("/<int:tutor_id>/company", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_company_for_tutor(tutor_id):
    return TutorController.get_company_for_tutor(tutor_id)
