from datetime import datetime
from .. import db

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.DateTime, nullable=True)

    # Relazione con user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    user = db.relationship("User", backref="notifications")

    # Relazione con stage
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'), nullable=True)
    internship = db.relationship("Internship", backref="notifications")

