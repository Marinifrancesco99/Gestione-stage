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
    def create_course(name):
        new_course=Course(
            name=name
        )
        db.session.add(new_course)
        db.session.commit()
        return new_course

    @staticmethod
    def update_course(course_id, name):
        course = Course.query.get(course_id)
        if not course:
            return None
        
        if name is not None:
            course.name = name
        
        db.session.commit()
        return course

    @staticmethod
    def delete_course(course_id):
        course = Course.query.get(course_id)
        if not course:
            return None
        
        db.session.delete(course)
        db.session.commit()
        return course
    
    # Get all classes for a specific course
    @staticmethod
    def get_classes_for_course(course_id):
        course = Course.query.get(course_id)
        return course.classes if course else []
    
    # Get all professors for a specific course 
    @staticmethod
    def get_professors_for_course(course_id):
        course = Course.query.get(course_id)
        return course.professors if course else []
    
    # Add professor to course (N:N)    Quando vuoi associare un professore esistente a un corso (ad esempio, dall'interfaccia admin).
    @staticmethod
    def add_professor_to_course(course_id, professor):
        course = Course.query.get(course_id)
        if not course:
            return None

        if professor not in course.professors:
            course.professors.append(professor)
            db.session.commit()
        return course
    
    # Remove professor from course (N:N) Quando vuoi rimuovere un professore da un corso.
    @staticmethod
    def remove_professor_from_course(course_id, professor):
        course = Course.query.get(course_id)
        if not course:
            return None

        if professor in course.professors:
            course.professors.remove(professor)
            db.session.commit()
        return course
