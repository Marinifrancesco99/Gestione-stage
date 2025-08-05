from flask import Blueprint
from app.controller.convention_controller import ConventionController
from app.utils.decorators import token_required, roles_required

convention_bp = Blueprint('convention', __name__)

@convention_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_conventions():
    return ConventionController.get_all_conventions()

@convention_bp.route("/<int:id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_convention_by_id(id):
    return ConventionController.get_convention_by_id(id)

@convention_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def save_convention():
    return ConventionController.save_convention()

@convention_bp.route("/<int:id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_convention(id):
    return ConventionController.update_convention(id)

@convention_bp.route("/<int:id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_convention(id):
    return ConventionController.delete_convention(id)

@convention_bp.route("/signed", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_signed_conventions():
    return ConventionController.get_signed_conventions()

@convention_bp.route("/downloaded", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_downloaded_conventions():
    return ConventionController.get_downloaded_conventions()

@convention_bp.route("/internship/<int:internship_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_conventions_by_internship_id(internship_id):
    return ConventionController.get_conventions_by_internship_id(internship_id)

@convention_bp.route("/user/<int:user_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_conventions_by_user_id(user_id):
    return ConventionController.get_conventions_by_user_id(user_id)

@convention_bp.route("/unsigned", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_downloaded_but_not_signed():
    return ConventionController.get_downloaded_but_not_signed()

@convention_bp.route("/document/<string:document_filename>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_conventions_by_document_filename(document_filename):
    return ConventionController.get_conventions_by_document_filename(document_filename)