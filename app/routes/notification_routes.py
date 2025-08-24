from flask import Blueprint
from app.controller.notification_controller import NotificationController
from app.utils.decorators import token_required, roles_required

notification_bp = Blueprint('notification', __name__)

@notification_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_notifications():
    return NotificationController.get_all_notifications()

@notification_bp.route("/<int:notification_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_notification_by_id(notification_id):
    return NotificationController.get_notification_by_id(notification_id)

@notification_bp.route("/user/<int:user_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_notifications_for_user(user_id):
    return NotificationController.get_notifications_for_user(user_id)

@notification_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def create_notification():
    return NotificationController.create_notification()

@notification_bp.route("/<int:notification_id>/read", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def mark_notification_as_read(notification_id):
    return NotificationController.mark_notification_as_read(notification_id)

@notification_bp.route("/<int:notification_id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_notification(notification_id):
    return NotificationController.delete_notification(notification_id)

@notification_bp.route("/user/<int:user_id>/all", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_all_notifications_for_user(user_id):
    return NotificationController.delete_all_notifications_for_user(user_id)

@notification_bp.route("/internship/<int:internship_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_notifications_by_internship(internship_id):
    return NotificationController.get_notifications_by_internship(internship_id)

@notification_bp.route("/due/<string:now>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_due_notifications(now):
    return NotificationController.get_due_notifications(now)
