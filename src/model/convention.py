from .. import db

class Convention(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'))       # fk che punta a stage
    internship = db.relationship('Internship', back_populates='conventions')