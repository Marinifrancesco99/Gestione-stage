from .. import db

class CompanyTypes(db.Model):
    __tablename__ = 'companyTypes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    
    # Stabiliamo la relazione 1:1 con Companies
    companies = db.relationship("Companies", back_populates="company_type")
    
    