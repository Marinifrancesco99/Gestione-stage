from flask import jsonify, request
from app.service.professor_service import ProfessorService

class ProfessorController:
    @staticmethod
    def get_professor_by_id(professor_id):
        professor = ProfessorService.get_professor_by_id(professor_id)
        return jsonify(professor.to_dict()), 200
    
    @staticmethod
    def get_all_professors():
        professors = ProfessorService.get_all_professors()
        return jsonify([p.to_dict() for p in professors]), 200
    
    @staticmethod
    def create_professor():
        data = request.get_json()
        professor = ProfessorService.create_professor(
            name=data["name"],
            surname=data["surname"],
            email=data["email"],
            phone=data.get("phone"),
            vote=data.get("vote"),
            evaluation=data.get("evaluation"),
            note=data.get("note")
        )
        return jsonify(professor.to_dict()), 201
    
    @staticmethod
    def update_professor(professor_id):
        data = request.get_json()
        professor = ProfessorService.update_professor(
            professor_id=professor_id,
            name=data.get("name"),
            surname=data.get("surname"),
            email=data.get("email"),
            phone=data.get("phone"),
            vote=data.get("vote"),
            evaluation=data.get("evaluation"),
            note=data.get("note")
        )
        return jsonify(professor.to_dict()), 200
    
    @staticmethod
    def delete_professor(professor_id):
        ProfessorService.delete_professor(professor_id)
        return jsonify({"message": "Professor deleted successfully"}), 200
    
    @staticmethod
    def get_professor_by_email(email):
        professor = ProfessorService.get_professor_by_email(email)
        return jsonify(professor.to_dict()), 200
    
    @staticmethod
    def get_by_course(course_id):
        professor = ProfessorService.get_by_course(course_id)
        return jsonify(professor.to_dict()), 200
    
    @staticmethod
    def add_course(professor_id):
        data = request.get_json()
        course = data.get("course")
        professor = ProfessorService.add_course(professor_id, course)
        return jsonify(professor.to_dict()), 200
    
    @staticmethod
    def remove_course(professor_id):
        data = request.get_json()
        course = data.get("course")
        professor = ProfessorService.remove_course(professor_id, course)
        return jsonify(professor.to_dict()), 200
