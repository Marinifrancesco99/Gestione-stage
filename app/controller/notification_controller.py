from flask import jsonify, request
from app.service.notification_service import NotificationService


class NotificationController:
    @staticmethod
    def get_all_notifications():
        notifications = NotificationService.get_all_notifications()
        return jsonify([n.to_dict() for n in notifications]), 200
    
    @staticmethod
    def get_notification_by_id(notification_id):
        notification = NotificationService.get_notification_by_id(notification_id)
        return jsonify(notification.to_dict()), 200
    
    @staticmethod
    def get_notifications_for_user(user_id):
        notifications = NotificationService.get_notifications_for_user(user_id)
        return jsonify([n.to_dict() for n in notifications]), 200
    
    @staticmethod
    def create_notification():
        data = request.get_json()
        notification = NotificationService.create_notification(
            user_id=data["user_id"],
            message=data["message"],
            type=data["type"],
            internship_id=data.get("internship_id"),
            due_date=data.get("due_date")
        )
        return jsonify(notification.to_dict()), 201
    
    @staticmethod
    def mark_notification_as_read(notification_id):
        notification = NotificationService.mark_notification_as_read(notification_id)
        return jsonify(notification.to_dict()), 200
    
    @staticmethod
    def delete_notification(notification_id):
        NotificationService.delete_notification(notification_id)
        return jsonify({"message": "Notification deleted successfully"}), 200
    
    @staticmethod
    def delete_all_notifications_for_user(user_id):
        NotificationService.delete_all_notifications_for_user(user_id)
        return jsonify({"message": "All notifications deleted successfully"}), 200
    
    @staticmethod
    def get_notifications_by_internship(internship_id):
        notifications = NotificationService.get_notifications_by_internship(internship_id)
        return jsonify([n.to_dict() for n in notifications]), 200
    
    @staticmethod
    def get_due_notifications(now):
        notifications = NotificationService.get_due_notifications(now)
        return jsonify([n.to_dict() for n in notifications]), 200
