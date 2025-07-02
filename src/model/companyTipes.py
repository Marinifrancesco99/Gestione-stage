from .. import db

class CompanyTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    company = db.relationship('Companies', back_populates='type', uselist=False)  # garantisce la relazione 1:1