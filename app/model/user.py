from .. import db
from sqlalchemy import Enum


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(150))
    role = db.Column(
        Enum("admin", "scuola", "tutor", "studente", name="user_roles"), nullable=False
    )

    # Stabiliamo la relazione 1:1 con tutor grazie a uselist=false.
    tutor = db.relationship("Tutor", back_populates="user", uselist=False)

    # Relazione con student
    student = db.relationship("Student", back_populates="user", uselist=False)

    # Relazione con notifications
    notifications = db.relationship("Notification", back_populates="user")
