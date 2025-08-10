from flask import Blueprint
from app.controller.user_controller import UserController
from utils.decorators import token_required, roles_required

user_bp = Blueprint('user', __name__)

@user_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_users():
    return UserController.get_all_users()

@user_bp.route("/<int:user_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_user_by_id(user_id):
    return UserController.get_user_by_id(user_id)

@user_bp.route("/email/<string:email>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_user_by_email(email):
    return UserController.get_user_by_email(email)

@user_bp.route("/<int:user_id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_user(user_id):
    return UserController.update_user(user_id)

@user_bp.route("/<int:user_id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_user(user_id):
    return UserController.delete_user(user_id)

@user_bp.route("/tutor/<int:user_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_tutor_for_user(user_id):
    return UserController.get_tutor_for_user(user_id)

@user_bp.route("/student/<int:user_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_student_for_user(user_id):
    return UserController.get_student_for_user(user_id)

@user_bp.route("/role/<string:role>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_users_by_role(role):
    return UserController.get_users_by_role(role)

@user_bp.route("/tutors", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_tutors():
    return UserController.get_all_tutors()

@user_bp.route("/students", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_students():
    return UserController.get_all_students()