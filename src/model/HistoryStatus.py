from .. import db

class HistoryStatus(db.Model):
    __tablename__ = 'historyStatus'
    
    id = db.Column(db.Integer, primary_key=True)
    
