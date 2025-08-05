from flask import jsonify, request
from app.service.courses_service import CoursesService

class CourseController:
    @staticmethod
    def get_all_courses():
        courses = CoursesService.get_all_courses()
        return jsonify([cou.to_dict() for cou in courses]), 200
    
    @staticmethod
    def get_course_by_id(course_id):
        course = CoursesService.get_course_by_id(course_id)
        return jsonify(course.to_dict()), 200
    
    @staticmethod
    def save_course():
        data = request.get_json()
        course = CoursesService.save_course(
            name=data["name"]
        )
        return jsonify(course.to_dict()), 201
    
    @staticmethod
    def update_course(course_id):
        data = request.get_json()
        course = CoursesService.update_course(
            course_id=course_id,
            name=data["name"]
        )
        return jsonify(course.to_dict()), 200
    
    @staticmethod
    def delete_course(course_id):
        CoursesService.delete_course(course_id)
        return jsonify({"message": "Course deleted successfully"}), 200
    
    @staticmethod
    def get_classes_for_course(course_id):
        classes = CoursesService.get_classes_for_course(course_id)
        return jsonify([cl.to_dict() for cl in classes]), 200
    
    @staticmethod
    def get_professors_for_course(course_id):
        professors = CoursesService.get_professors_for_course(course_id)
        return jsonify([pr.to_dict() for pr in professors]), 200
    
    @staticmethod
    def add_professor_to_course(course_id):
        data = request.get_json()
        professor = data.get("professor")
        course = CoursesService.add_professor_to_course(course_id, professor)
        return jsonify(course.to_dict()), 200

    
    @staticmethod
    def remove_professor_from_course(course_id):
        data = request.get_json()
        professor = data.get("professor")
        course = CoursesService.remove_professor_from_course(course_id, professor)
        return jsonify(course.to_dict()), 200