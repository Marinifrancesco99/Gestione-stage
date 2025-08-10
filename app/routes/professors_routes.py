from flask import Blueprint
from app.controller.professor_controller import ProfessorController
from utils.decorators import token_required, roles_required

professor_bp = Blueprint('professor', __name__)

@professor_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_professors():
    return ProfessorController.get_all_professors()

@professor_bp.route("/<int:professor_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_professor_by_id(professor_id):
    return ProfessorController.get_professor_by_id(professor_id)

@professor_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def create_professor():
    return ProfessorController.create_professor()

@professor_bp.route("/<int:professor_id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_professor(professor_id):
    return ProfessorController.update_professor(professor_id)

@professor_bp.route("/<int:professor_id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_professor(professor_id):
    return ProfessorController.delete_professor(professor_id)

@professor_bp.route("/email/<string:email>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_professor_by_email(email):
    return ProfessorController.get_professor_by_email(email)

@professor_bp.route("/course/<int:course_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_by_course(course_id):
    return ProfessorController.get_by_course(course_id)

@professor_bp.route("/<int:professor_id>/add_course", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def add_course(professor_id):
    return ProfessorController.add_course(professor_id)

@professor_bp.route("/<int:professor_id>/remove_course", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def remove_course(professor_id):
    return ProfessorController.remove_course(professor_id)
