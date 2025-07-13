from .. import db

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
    classes = db.relationship("Classes", back_populates="student")