from app.extension import db
from app.model.notification import Notification

class NotificationDAO:
    # Get all notifications
    @staticmethod
    def get_all_notifications():
        return Notification.query.all()
    
    @staticmethod
    def get_notification_by_id(notification_id):
        return Notification.query.get(notification_id)
    
    # Retrieves all unread notifications of a user
    @staticmethod
    def get_notifications_for_user(user_id, only_unread=False):
        query = Notification.query.filter_by(user_id=user_id)
        if only_unread:
            query = query.filter_by(read=False)
        return query.order_by(Notification.created_at.desc()).all()
    
    # Create a new notification
    @staticmethod
    def create_notification(user_id, message, type, internship_id=None, due_date=None):
        new_notification = Notification(
            user_id=user_id,
            message=message,
            type=type,
            internship_id=internship_id,
            due_date=due_date
        )
        db.session.add(new_notification)
        db.session.commit()
        return new_notification
    
    # Marks a notification as read
    @staticmethod
    def mark_notification_as_read(notification_id):
        notification = Notification.query.get(notification_id)
        if notification and not notification.read:
            notification.read = True
            db.session.commit()
        return notification
    
    # delete notification by id
    @staticmethod
    def delete_notification(notification_id):
        notification = Notification.query.get(notification_id)
        if notification:
            db.session.delete(notification)
            db.session.commit()
        return notification
    
    # delete all notifications for a user
    @staticmethod
    def delete_all_notifications_for_user(user_id):
        notifications = Notification.query.filter_by(user_id=user_id).all()
        for notification in notifications:
            db.session.delete(notification)
        db.session.commit()
        return notifications
    
    # Get notification for internship
    @staticmethod
    def get_notifications_for_internship(internship_id):
        return Notification.query.filter_by(internship_id=internship_id).order_by(Notification.created_at.desc()).all()
    
    # Get notifications that are due
    @staticmethod
    def get_due_notifications(now=None):
        from datetime import datetime
        if not now:
            now = datetime.utcnow()
        return Notification.query.filter(
            Notification.due_date != None,
            Notification.due_date <= now,
            Notification.read == False
        ).all()