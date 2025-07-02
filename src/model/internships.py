from .. import db

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(50))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))          # FK con aziende
    company = db.relationship('Companies', back_populates='internships')
    
    conventions = db.relationship('Convention', back_populates='internship')  
    
    