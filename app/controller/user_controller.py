from flask import jsonify, request
from app.service.user_service import UserService

class UserController:
    @staticmethod
    def get_all_users():
        users = UserService.get_all_users()
        return jsonify([us.to_dict() for us in users]), 200
    
    @staticmethod
    def get_user_by_id(user_id):
        user = UserService.get_user_by_id(user_id)
        return jsonify(user.to_dict()), 200
    
    @staticmethod
    def get_user_by_email(email):
        user = UserService.get_user_by_email(email)
        return jsonify(user.to_dict()), 200
    
    @staticmethod
    def update_user(user_id):
        data = request.get_json()
        updated_user = UserService.update_user(user_id, **data)
        return jsonify(updated_user.to_dict()), 200

    @staticmethod
    def delete_user(user_id):
        UserService.delete_user(user_id)
        return jsonify({"message": "Tutor deleted successfully"}), 200
    
    @staticmethod
    def get_tutor_for_user(user_id):
        user = UserService.get_student_for_user(user_id)
        return jsonify(user.to_dict()), 200
    
    @staticmethod
    def get_student_for_user(user_id):
        student = UserService.get_student_for_user(user_id)
        return jsonify(student.to_dict()), 200
    
    @staticmethod
    def get_users_by_role(role):
        users = UserService.get_users_by_role(role)
        return jsonify([us.to_dict() for us in users]), 200
    
    @staticmethod
    def get_all_tutors():
        users_tutors = UserService.get_all_tutors()
        return jsonify([us.to_dict() for us in users_tutors]), 200
    
    @staticmethod
    def get_all_students():
        users_students = UserService.get_all_students()
        return jsonify([us.to_dict() for us in users_students]), 200
    
    
    
