from flask import Blueprint
from app.controller.students_controller import StudentController
from app.utils.decorators import token_required, roles_required

student_bp = Blueprint("student", __name__)

@student_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_students():
    return StudentController.get_all_students()

@student_bp.route("/<int:student_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_student_by_id(student_id):
    return StudentController.get_student_by_id(student_id)

@student_bp.route("/email/<string:email>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_student_by_email(email):
    return StudentController.get_student_by_email(email)

@student_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def create_student():
    return StudentController.create_student()

@student_bp.route("/<int:student_id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_student(student_id):
    return StudentController.update_student(student_id)

@student_bp.route("/<int:student_id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_student(student_id):
    return StudentController.delete_student(student_id)

@student_bp.route("/<int:student_id>/interviews", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_interviews_for_student(student_id):
    return StudentController.get_interviews_for_student(student_id)

@student_bp.route("/<int:student_id>/internship", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_internship_for_student(student_id):
    return StudentController.get_internship_for_student(student_id)

@student_bp.route("/<int:student_id>/class", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_class_for_student(student_id):
    return StudentController.get_class_for_student(student_id)
