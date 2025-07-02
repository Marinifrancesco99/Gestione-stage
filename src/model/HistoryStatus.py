from .. import db

class HistoryStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'), unique=True)  # FK con vincolo UNIQUE che punta a stage
    internship = db.relationship('Internship', back_populates='history_status')