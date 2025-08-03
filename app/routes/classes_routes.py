from flask import Blueprint
from app.controller.classes_controller import ClassesController

classes_bp = Blueprint('classes', __name__)
classes_bp.route("/", methods=["GET"])(ClassesController.get_all_classes)
classes_bp.route("/<int:id>", methods=["GET"])(ClassesController.get_class_by_id)
classes_bp.route("/", methods=["POST"])(ClassesController.save_class)
classes_bp.route("/<int:id>", methods=["PUT"])(ClassesController.update_class)
classes_bp.route("/<int:id>", methods=["DELETE"])(ClassesController.delete_class)