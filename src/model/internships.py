from .. import db

class Internship(db.Model):
    __tablename__ = 'internship'
    
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(50))
    