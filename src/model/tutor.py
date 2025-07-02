from .. import db

class Tutor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(150), unique = True)
    role = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    user = db.relationship('User', back_populates='tutor')                       # back_populates crea una relazione bidirezionale.