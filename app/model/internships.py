from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.extension import db

class Internship(db.Model):
    __tablename__ = 'internship'
    
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(50))
    
    # FK che punta a companies
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company = db.relationship("Companies", back_populates= 'internship')
    
    # Relazione inversa con convention
    convention = db.relationship('Convention', back_populates = 'internship')
    
    # Relazione 1:1 con Hystory Status
    history_status = db.relationship("HistoryStatus", back_populates = 'internship', uselist=False)
    
    # Fk di tutor
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))
    tutor = db.relationship("Tutor", back_populates = "internship")
    
    # Relazione con attendance logs
    attendance_logs = db.relationship("AttendanceLogs", back_populates="internship")
    
    # Fk di student
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship("Student", back_populates = "internship")
    
    # Relazione con notifications
    notifications = db.relationship("Notification", back_populates="internship")
    
    
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'status': self.status,
            'company_id': self.company_id,
            'convention_id': self.convention.id if self.convention else None,
            'history_status_id': self.history_status.id if self.history_status else None,
            'tutor_id': self.tutor_id,
            'attendance_log_ids': [log.id for log in self.attendance_logs],
            'student_id': self.student_id,
            'notification_ids': [notif.id for notif in self.notifications]
        }
