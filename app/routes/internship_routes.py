from flask import Blueprint
from app.controller.internship_controller import InternshipController
from app.utils.decorators import token_required, roles_required

internship_bp = Blueprint("internships", __name__)

@internship_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_internships():
    return InternshipController.get_all_internships()

@internship_bp.route("/<int:internship_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_internship_by_id(internship_id):
    return InternshipController.get_internship_by_id(internship_id)

@internship_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def save_internship():
    return InternshipController.save_internship()

@internship_bp.route("/<int:internship_id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_internship(internship_id):
    return InternshipController.update_internship(internship_id)

@internship_bp.route("/<int:internship_id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_internship(internship_id):
    return InternshipController.delete_internship(internship_id)

# Filtri extra
@internship_bp.route("/student/<int:student_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_by_student(student_id):
    return InternshipController.get_by_student(student_id)

@internship_bp.route("/company/<int:company_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_by_company(company_id):
    return InternshipController.get_by_company(company_id)

@internship_bp.route("/tutor/<int:tutor_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_by_tutor(tutor_id):
    return InternshipController.get_by_tutor(tutor_id)

@internship_bp.route("/status/<string:status>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_by_status(status):
    return InternshipController.get_by_status(status)

@internship_bp.route("/dates/<string:start_date>/<string:end_date>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_by_date_range(start_date, end_date):
    return InternshipController.get_by_date_range(start_date, end_date)
