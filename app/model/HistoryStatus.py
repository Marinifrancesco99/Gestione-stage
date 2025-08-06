from datetime import datetime
from app.extension import db

class HistoryStatus(db.Model):
    __tablename__ = 'historyStatus'
    
    id = db.Column(db.Integer, primary_key=True)
    
    status = db.Column(db.String(50), nullable=False)
    changed_at = db.Column(db.DateTime, default=datetime.utcnow)
    changed_by = db.Column(db.String(100))
    note = db.Column(db.String(255))
    reason = db.Column(db.String(255))

    # Fk di internship
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'))
    internship = db.relationship('Internship', back_populates='history_status')
    

    def to_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'changed_at': self.changed_at.isoformat() if self.changed_at else None,
            'changed_by': self.changed_by,
            'note': self.note,
            'reason': self.reason,
            'internship_id': self.internship_id
        }
