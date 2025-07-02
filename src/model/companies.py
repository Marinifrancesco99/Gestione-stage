from .. import db


class Companies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer(50))
    companyName = db.Column(db.String(100))
    address = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    province = db.Column(db.String(50))
    note = db.Column(db.String(50))
    city = db.Column(db.String(50))
    cap = db.Column(db.Integer(50))
    partitaIVA = db.Column(db.integer(50))
    type_id = db.Column(db.Integer, db.ForeignKey('company_types.id'), unique=True)     #Fk con tipo azienda
    type = db.relationship('CompanyTypes', back_populates='company')
    
    internships = db.relationship('Internship', back_populates='company')
    
    history_status = db.relationship('HistoryStatus', back_populates='internship', uselist=False)  # uselist=False rende 1:1
    