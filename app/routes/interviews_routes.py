from flask import Blueprint
from app.controller.interviews_controller import InterviewsController
from app.utils.decorators import token_required, roles_required

interview_bp = Blueprint("interviews", __name__)

@interview_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_interviews():
    return InterviewsController.get_all_interviews()

@interview_bp.route("/<int:interview_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_interview_by_id(interview_id):
    return InterviewsController.get_interview_by_id(interview_id)

@interview_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def save_interview():
    return InterviewsController.save_interview()

@interview_bp.route("/<int:interview_id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_interview(interview_id):
    return InterviewsController.update_interview(interview_id)

@interview_bp.route("/<int:interview_id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_interview(interview_id):
    return InterviewsController.delete_interview(interview_id)

# Filtri extra
@interview_bp.route("/student/<int:student_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_interviews_by_student(student_id):
    return InterviewsController.get_interviews_by_student(student_id)

@interview_bp.route("/company/<int:company_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_interviews_by_company(company_id):
    return InterviewsController.get_interviews_by_company(company_id)

@interview_bp.route("/date/<string:date>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_interviews_by_date(date):
    return InterviewsController.get_interviews_by_date(date)

@interview_bp.route("/result/<string:result_text>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_by_result(result_text):
    return InterviewsController.get_by_result(result_text)
