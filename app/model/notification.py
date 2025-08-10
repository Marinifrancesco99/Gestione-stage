from datetime import datetime
from app.extension import db

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
    user = db.relationship("User", back_populates="notifications")

    # Relazione con stage
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'), nullable=True)
    internship = db.relationship("Internship", back_populates="notifications")
    
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'type': self.type,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'read': self.read,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'user_id': self.user_id,
            'internship_id': self.internship_id
        }


