from .. import db

professor_course = db.Table(
    'professor_course',
    db.Column('professor_id', db.Integer, db.ForeignKey('professors.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
)