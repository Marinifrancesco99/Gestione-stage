from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .. import db

class Internship(db.Model):
    __tablename__ = 'internship'
    
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(50))
    
    # FK che punta a companies
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company = db.relationship("Company", back_populates= 'internship')
    
    # Relazione inversa con convention
    convention = db.relationship('Convention', back_populates = 'internship')
    
    # Relazione 1:1 con Hystory Status
    history_status = db.relationship("HistoryStatus", back_populates = 'internship', uselist=False)
    
    # Fk di tutor
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))
    tutor = db.relationship("Tutor", back_populates = "internship")
    
    # Relazione con attendance logs
    attendance_logs = db.relationship("Attendance_logs", back_populates = "internship")
    
    # Fk di student
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship("Student", back_populates = "internship")