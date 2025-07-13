from .. import db
from .association import professor_course

class Professor(db.Model):
    __tablename__ = 'professors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    vote = db.Column(db.Integer)
    evaluation = db.Column(db.Integer)
    note = db.Column(db.String(100))
    
    # Relazione N:N con Course
    courses = db.relationship(
        'Course',
        secondary=professor_course,
        back_populates='professors'
    )