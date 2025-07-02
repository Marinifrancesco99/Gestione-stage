from .. import db

class Convention(db.Model):
    __tablename__ = 'convention'
    
    id = db.Column(db.Integer, primary_key=True)
    
    