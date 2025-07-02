from .. import db

class CompanyTypes(db.Model):
    __tablename__ = 'companyTypes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    