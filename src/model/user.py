from .. import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(150))
    role = db.Column(db.String(50))
    
    # Stabiliamo la relazione 1:1 con tutor grazie a uselist=false.
    tutor = db.relationship('Tutor', uselist=False, back_populates='user')
    
