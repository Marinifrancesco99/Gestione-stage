from app.extension import db

class Classes(db.Model):
    __tablename__ = 'classes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    # Relazione con student
    students = db.relationship("Student", back_populates="classe")
    
    # Fk di course
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    course = db.relationship("Course", back_populates="classes")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'students': [student.id for student in self.students],
            'course_id': self.course_id
        }