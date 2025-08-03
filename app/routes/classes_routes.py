from flask import Blueprint
from app.controller.classes_controller import ClassesController
from app.utils.decorators import token_required, roles_required

classes_bp = Blueprint('classes', __name__)

@classes_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_classes():
    return ClassesController.get_all_classes()

@classes_bp.route("/<int:id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_class_by_id(id):
    return ClassesController.get_class_by_id(id)

@classes_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def save_class():
    return ClassesController.save_class()

@classes_bp.route("/<int:id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_class(id):
    return ClassesController.update_class(id)

@classes_bp.route("/<int:id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_class(id):
    return ClassesController.delete_class(id)
