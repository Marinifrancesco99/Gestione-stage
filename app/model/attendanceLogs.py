from app.extension import db

class AttendanceLogs(db.Model):
    __tablename__ = 'attendanceLogs'
    
    id = db.Column(db.Integer, primary_key=True)
    
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    notes = db.Column(db.String(50))
    validation = db.Column(db.Boolean, default=False)
    register_signature = db.Column(db.String(100))
    
    # Fk che punta a tutor
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'))
    tutor = db.relationship("Tutor", back_populates="attendance_logs")
    
    # Fk che punta ad internship
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'))
    internship = db.relationship("Internship", back_populates="attendance_logs")
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat() if self.date else None,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'notes': self.notes,
            'validation': self.validation,
            'register_signature': self.register_signature,
            'tutor_id': self.tutor_id,
            'internship_id': self.internship_id
        }