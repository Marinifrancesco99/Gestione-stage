from flask import jsonify, request
from app.service.students_service import StudentsService

class StudentController:
    @staticmethod
    def get_all_students():
        students = StudentsService.get_all_students()
        return jsonify([s.to_dict() for s in students]), 200
    
    @staticmethod
    def get_student_by_id(student_id):
        student = StudentsService.get_student_by_id(student_id)
        return jsonify(student.to_dict()), 200
    
    @staticmethod
    def get_student_by_email(email):
        student = StudentsService.get_student_by_email(email)
        return jsonify(student.to_dict()), 200
    
    @staticmethod
    def create_student():
        data = request.get_json()
        student = StudentsService.create_student(
            name=data["name"],
            surname=data["surname"],
            email=data["email"],
            phone=data["phone"],
            status=data["status"],
            user_id=data.get("user_id"),
            class_id=data.get("class_id")
        )
        return jsonify(student.to_dict()), 201
    
    @staticmethod
    def update_student(student_id):
        data = request.get_json()
        student = StudentsService.update_student(student_id, **data)
        return jsonify(student.to_dict()), 200
    
    @staticmethod
    def delete_student(student_id):
        StudentsService.delete_student(student_id)
        return jsonify({"message": "Student deleted successfully"}), 200
    
    @staticmethod
    def get_interviews_for_student(student_id):
        interviews = StudentsService.get_interviews_for_student(student_id)
        return jsonify([i.to_dict() for i in interviews]), 200
    
    @staticmethod
    def get_internship_for_student(student_id):
        internship = StudentsService.get_internship_for_student(student_id)
        return jsonify(internship.to_dict() if internship else {}), 200
    
    @staticmethod
    def get_class_for_student(student_id):
        class_info = StudentsService.get_class_for_student(student_id)
        return jsonify(class_info.to_dict() if class_info else {}), 200
