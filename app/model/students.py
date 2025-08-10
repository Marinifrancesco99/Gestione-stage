from app.extension import db

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    status = db.Column(db.String(50))
    
    # Relazione con interviews
    interview = db.relationship("Interview", back_populates = "student")
    
    # Fk di user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    user = db.relationship("User", back_populates="student")
    
    # Relazione con internship
    internship = db.relationship("Internship", back_populates = "student")
    
    # Fk di class
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    classe = db.relationship("Classes", back_populates="students")
    
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone': self.phone,
            'status': self.status,
            'interview_ids': [interview.id for interview in self.interview],
            'user_id': self.user_id,
            'internship_ids': [internship.id for internship in self.internship],
            'class_id': self.class_id
        }
