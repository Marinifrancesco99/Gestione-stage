from app.dao.courses_dao import CoursesDAO

class CoursesService:
    @staticmethod
    def get_all_courses():
        return CoursesDAO.get_all_courses()
    
    @staticmethod
    def get_course_by_id(course_id):
        course = CoursesDAO.get_course_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")
        return course
    
    @staticmethod
    def save_course(name):
        return CoursesDAO.create_course(name)
    
    @staticmethod
    def update_course(course_id, name):
        existing_course = CoursesDAO.get_course_by_id(course_id)
        if not existing_course:
            raise ValueError(f"Course with ID {course_id} not found")
        return CoursesDAO.update_course(course_id, name)
    
    @staticmethod
    def delete_course(course_id):
        course = CoursesDAO.get_course_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")   
        CoursesDAO.delete_course(course_id)
        return True
    
    @staticmethod
    def get_classes_for_course(course_id):
        classes = CoursesDAO.get_classes_for_course(course_id)
        if not classes:
            raise ValueError(f"No classes found for course ID {course_id}")
        return classes
    
    @staticmethod
    def get_professors_for_course(course_id):
        professors = CoursesDAO.get_professors_for_course(course_id)
        if not professors:
            raise ValueError(f"No professors found for course ID {course_id}")
        return professors
    
    @staticmethod
    def add_professor_to_course(course_id, professor):
        course = CoursesDAO.get_course_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")
        return CoursesDAO.add_professor_to_course(course_id, professor)
    
    @staticmethod
    def remove_professor_from_course(course_id, professor):
        course = CoursesDAO.get_course_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")
        return CoursesDAO.remove_professor_from_course(course_id, professor)