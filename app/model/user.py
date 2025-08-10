from app.extension import db
from sqlalchemy import Enum


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(500))
    role = db.Column(
        Enum("admin", "scuola", "tutor", "studente", name="user_roles"), nullable=False
    )

    # Stabiliamo la relazione 1:1 con tutor grazie a uselist=false.
    tutor = db.relationship("Tutor", back_populates="user", uselist=False)

    # Relazione con student
    student = db.relationship("Student", back_populates="user", uselist=False)

    # Relazione con notifications
    notifications = db.relationship("Notification", back_populates="user")




    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'tutor_id': self.tutor.id if self.tutor else None,
            'student_id': self.student.id if self.student else None,
            'notification_ids': [notif.id for notif in self.notifications]
        }
