from flask import Blueprint
from app.controller.historyStatus_controller import HistoryStatusController
from app.utils.decorators import token_required, roles_required

historyStatus_bp = Blueprint('historyStatus', __name__)

@historyStatus_bp.route("/", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_all_historyStatus():
    return HistoryStatusController.get_all_history_status()

@historyStatus_bp.route("/<int:status_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_history_status_by_id(status_id):
    return HistoryStatusController.get_history_status_by_id(status_id)

@historyStatus_bp.route("/internship/<int:internship_id>", methods=["GET"])
@token_required
@roles_required("admin", "scuola")
def get_by_internship(internship_id):
    return HistoryStatusController.get_by_internship(internship_id)

@historyStatus_bp.route("/", methods=["POST"])
@token_required
@roles_required("admin", "scuola")
def save_history_status():
    return HistoryStatusController.save_history_status()

@historyStatus_bp.route("/<int:status_id>", methods=["PUT"])
@token_required
@roles_required("admin", "scuola")
def update_history_status(status_id):
    return HistoryStatusController.update_history_status(status_id)

@historyStatus_bp.route("/<int:status_id>", methods=["DELETE"])
@token_required
@roles_required("admin", "scuola")
def delete_history_status(status_id):
    return HistoryStatusController.delete_status(status_id)