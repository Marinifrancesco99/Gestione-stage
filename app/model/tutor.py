from .. import db

class Tutor(db.Model):
    __tablename__ = 'tutors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(150), unique = True)
    role = db.Column(db.String(50))
    
    # Fk che punta a user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    user = db.relationship("User", back_populates="tutor")
    
    # Relazione con Relationship
    internship = db.relationship("Internship", back_populates = "tutor")
    
    # Relazione con Attendance logs
    attendance_logs = db.relationship("AttendanceLogs", back_populates="tutor")
    
    # Fk che punta a companies 
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company = db.relationship("Company", back_populates = "tutor")