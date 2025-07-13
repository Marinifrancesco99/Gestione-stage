from datetime import datetime
from .. import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Convention(db.Model):
    __tablename__ = 'convention'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Flags per stato
    downloaded = db.Column(db.Boolean, default=False)      # verifica che è stato scaricato
    signed = db.Column(db.Boolean, default=False)          # altra verifica per vedere se è stato firmato

    # Eventi temporali come: quando è stato scaricato o quando è stato firmato.
    download_date = db.Column(db.DateTime)                 
    signed_date = db.Column(db.DateTime)                   

    # nome della persona che firma
    signed_by = db.Column(db.String(100))                  

    # Note generiche
    note = db.Column(db.String(255))

    # Timestamp automatico creazione/modifica
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # es: "convenzione_123.pdf"
    document_filename = db.Column(db.String(255))  
    
    # Fk che punta a internship, con il lato non proprietario reference inversa
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'))
    internship = db.relationship("Internship", back_populates = 'convention')
    
    