from app import db
from app.model.courses import Course

class CoursesDAO:
    @staticmethod
    def get_all_courses():
        return Course.query.all()

    @staticmethod
    def get_course_by_id(course_id):
        return Course.query.get(course_id)

    @staticmethod
    def add_course(course):
        db.session.add(course)
        db.session.commit()
        return course

    @staticmethod
    def update_course(course):
        db.session.commit()
        return course

    @staticmethod
    def delete_course(course):
        db.session.delete(course)
        db.session.commit()