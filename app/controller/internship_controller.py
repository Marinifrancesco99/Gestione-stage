from flask import jsonify, request
from app.service.internship_service import InternshipService

class InternshipController:
    @staticmethod
    def get_internship_by_id(internship_id):
        internship = InternshipService.get_internship_by_id(internship_id)
        return jsonify(internship.to_dict()), 200
    
    @staticmethod
    def get_all_internships():
        internships = InternshipService.get_all_internships()
        return jsonify([inte.to_dict() for inte in internships]), 200
    
    @staticmethod
    def save_internship():
        data = request.get_json()
        internship = InternshipService.save_internship(
            start_date= data["start_date"],
            end_date= data["end_date"],
            status= data["status"],
            company_id= data["company_id"],
            tutor_id= data["tutor_id"],
            student_id= data["student_id"]
        )
        return jsonify(internship.to_dict()), 201
    
    @staticmethod
    def update_internship(internship_id):
        data = request.get_json()
        internship = InternshipService.update_internship(
            internship_id= internship_id,
            start_date= data["start_date"],
            end_date= data["end_date"],
            status= data["status"],
            company_id= data["company_id"],
            tutor_id= data["tutor_id"],
            student_id= data["student_id"]
        )
        return jsonify(internship.to_dict()), 200
    
    @staticmethod
    def delete_internship(internship_id):
        InternshipService.delete_internship(internship_id)
        return jsonify({"message": "Internship deleted successfully"}), 200
    
    @staticmethod
    def get_by_student(student_id):
        internship = InternshipService.get_by_student(student_id)
        return jsonify([inte.to_dict() for inte in internship]), 200
    
    @staticmethod
    def get_by_company(company_id):
        internship = InternshipService.get_by_company(company_id)
        return jsonify([inte.to_dict() for inte in internship]), 200
    
    @staticmethod
    def get_by_tutor(tutor_id):
        internship = InternshipService.get_by_tutor(tutor_id)
        return jsonify([inte.to_dict() for inte in internship]), 200
    
    @staticmethod
    def get_by_status(status):
        internship = InternshipService.get_by_status(status)
        return jsonify([inte.to_dict() for inte in internship]), 200
    
    @staticmethod
    def get_by_date_range(start_date, end_date):
        internship = InternshipService.get_by_date_range(start_date, end_date)
        return jsonify([inte.to_dict() for inte in internship]), 200