from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
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
    
    # Fk che punta a companyType
    type_id = db.Column(db.Integer, db.ForeignKey('companyTypes.id'))
    company_type = db.relationship("CompanyTypes", back_populates="companies")
    
    # lato non proprietario
    internship = db.relationship("Internship", back_populates = "company")
    
    # Relazione con tutor
    tutor = db.relationship("Tutor", back_populates = "company")
    
    # Relazione con interviews
    interview = db.relationship("Interview", back_populates = "company")
    