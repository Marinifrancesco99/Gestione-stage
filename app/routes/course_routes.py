from flask import Blueprint
from app.controller.course_controller import CourseController
from app.utils.decorators import token_required, roles_required

course_bp = Blueprint('courses', __name__)

@course_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_courses():
    return CourseController.get_all_courses()

@course_bp.route("/<int:course_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_course_by_id(course_id):
    return CourseController.get_course_by_id(course_id)

@course_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def save_course():
    return CourseController.save_course()

@course_bp.route("/<int:course_id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_course(course_id):
    return CourseController.update_course(course_id)

@course_bp.route("/<int:course_id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_course(course_id):
    return CourseController.delete_course(course_id)

@course_bp.route("/classes/<int:course_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_classes_for_course(course_id):
    return CourseController.get_classes_for_course(course_id)

@course_bp.route("/professors/<int:course_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_professor_for_course(course_id):
    return CourseController.get_professors_for_course(course_id)


@course_bp.route("/professors/<int:course_id>/add", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def add_professor_to_course(course_id):
    return CourseController.add_professor_to_course(course_id)

@course_bp.route("/professors/<int:course_id>/remove", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def remove_professor_from_course(course_id):
    return CourseController.remove_professor_from_course(course_id)