from .. import db

class Classes(db.Model):
    __tablename__ = 'classes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    # Relazione con student
    student = db.relationship("Student", back_populates = "classes")
    
    # Fk di course
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    course = db.relationship("Course", back_populates="classes")