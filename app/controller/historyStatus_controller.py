from flask import jsonify, request
from app.service.HistoryStatus_service import HistoryStatusService

class HistoryStatusController:
    @staticmethod
    def get_all_history_status():
        status = HistoryStatusService.get_all_history_status()
        return jsonify([sta.to_dict() for sta in status]), 200
    
    @staticmethod
    def get_history_status_by_id(status_id):
        status = HistoryStatusService.get_history_status_by_id(status_id)
        return jsonify(status.to_dict()), 200
    
    @staticmethod
    def get_by_internship(internship_id):
        status = HistoryStatusService.get_by_internship(internship_id)
        return jsonify(status.to_dict()), 200
    
    @staticmethod
    def save_history_status():
        data = request.get_json()
        status = HistoryStatusService.save_history_status(
        internship_id=data["internship_id"],
        status=data["status"],
        changed_by=data.get("changed_by"),
        note=data.get("note"),
        reason=data.get("reason")
        )
        return jsonify(status.to_dict()), 201
    
    @staticmethod
    def update_history_status(status_id):
        data = request.get_json()
        hstatus = HistoryStatusService.update_history_status(
        status_id=status_id,
        status=data.get("status"),
        changed_by=data.get("changed_by"),
        note=data.get("note"),
        reason=data.get("reason")
        )
        return jsonify(hstatus.to_dict()), 200
    
    @staticmethod
    def delete_status(status_id):
        HistoryStatusService.delete_status(status_id)
        return jsonify({"message": "History Status deleted successfully"}), 200