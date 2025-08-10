from app.extension import db

class Interview(db.Model):
    __tablename__ = 'interviews'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    result = db.Column(db.String(200))
    note = db.Column(db.String(50))
    
    # Fk di companies
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    company = db.relationship("Companies", back_populates = "interview")
    
    # Fk di student
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship("Student", back_populates = "interview")
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat() if self.date else None,
            'result': self.result,
            'note': self.note,
            'company_id': self.company_id,
            'student_id': self.student_id
        }
