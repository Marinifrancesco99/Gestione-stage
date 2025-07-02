from .. import db


class Companies(db.Model):
    __tablename__ = 'companies' 

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50))  
    companyName = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    province = db.Column(db.String(50))
    note = db.Column(db.String(50))
    city = db.Column(db.String(50))
    cap = db.Column(db.String(10))  
    partitaIVA = db.Column(db.String(20))  
    