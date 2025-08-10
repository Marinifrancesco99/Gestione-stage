from app.dao.notification_dao import NotificationDAO
from app.exceptions.not_found import NotFoundException

class NotificationService:
    @staticmethod
    def get_all_notifications():
        return NotificationDAO.get_all_notifications()
    
    @staticmethod
    def get_notification_by_id(notification_id):
        notification = NotificationDAO.get_notification_by_id(notification_id)
        if not notification:
            raise NotFoundException(f"Notification not found with id: {notification_id}")
        return notification
    
    @staticmethod
    def get_notifications_for_user(user_id, only_unread=False):
        return NotificationDAO.get_notifications_for_user(user_id, only_unread)
    
    @staticmethod
    def create_notification(user_id, message, type, internship_id=None, due_date=None):
        return NotificationDAO.create_notification(user_id, message, type, internship_id, due_date)
    
    @staticmethod
    def mark_notification_as_read(notification_id):
        return NotificationDAO.mark_notification_as_read(notification_id)
    
    @staticmethod
    def delete_notification(notification_id):
        notification = NotificationDAO.get_notification_by_id(notification_id)
        if not notification:
            raise NotFoundException(f"Notification not found with id: {notification_id}")
        NotificationDAO.delete_notification(notification_id)
        return True
    
    @staticmethod
    def delete_all_notifications_for_user(user_id):
        notifications = NotificationDAO.delete_all_notifications_for_user(user_id)
        if not notifications:
            raise NotFoundException(f"No notifications found for user with id: {user_id}")
        return notifications
    
    @staticmethod
    def get_notifications_by_internship(internship_id):
        notifications = NotificationDAO.get_notifications_for_internship(internship_id)
        if not notifications:
            raise NotFoundException(f"No notifications found for internship with id: {internship_id}")
        return notifications
    
    @staticmethod
    def get_due_notifications(now):
        notifications = NotificationDAO.get_due_notifications(now)
        if not notifications:
            raise NotFoundException("No due notifications found")
        return notifications
    
    
    