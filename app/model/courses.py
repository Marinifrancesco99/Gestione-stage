from .. import db
from .association import professor_course

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    
    # Relazione con classes
    classes = db.relationship("Classes", back_populates="course")
    
    # Relazione N:N con Professor
    professors = db.relationship(
        'Professor',
        secondary=professor_course,
        back_populates='courses'
    )