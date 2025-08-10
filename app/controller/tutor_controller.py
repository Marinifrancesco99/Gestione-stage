from flask import jsonify, request
from app.service.tutor_service import TutorService

class TutorController:
    @staticmethod
    def get_all_tutors():
        tutors = TutorService.get_all_tutors()
        return jsonify([tutor.to_dict() for tutor in tutors]), 200
    
    @staticmethod
    def get_tutor_by_id(tutor_id):
        tutor = TutorService.get_tutor_by_id(tutor_id)
        return jsonify(tutor.to_dict()), 200
    
    @staticmethod
    def get_tutor_by_email(email):
        tutor = TutorService.get_tutor_by_email(email)
        return jsonify(tutor.to_dict()), 200
    
    @staticmethod
    def create_tutor():
        data = request.get_json()
        tutor = TutorService.create_tutor(
            name=data["name"],
            surname=data["surname"],
            email=data["email"],
            role=data["role"],
            user_id=data.get("user_id"),
            company_id=data.get("company_id")
        )
        return jsonify(tutor.to_dict()), 201
    
    @staticmethod
    def update_tutor(tutor_id):
        data = request.get_json()
        tutor = TutorService.update_tutor(tutor_id, **data)
        return jsonify(tutor.to_dict()), 200
    
    @staticmethod
    def delete_tutor(tutor_id):
        TutorService.delete_tutor(tutor_id)
        return jsonify({"message": "Tutor deleted successfully"}), 200
    
    @staticmethod
    def get_attendance_logs_for_tutor(tutor_id):
        logs = TutorService.get_attendance_logs_for_tutor(tutor_id)
        return jsonify([log.to_dict() for log in logs]), 200
    
    @staticmethod
    def get_internship_for_tutor(tutor_id):
        internship = TutorService.get_internship_for_tutor(tutor_id)
        return jsonify(internship.to_dict()), 200
    
    @staticmethod
    def get_company_for_tutor(tutor_id):
        company = TutorService.get_company_for_tutor(tutor_id)
        return jsonify(company.to_dict()), 200
