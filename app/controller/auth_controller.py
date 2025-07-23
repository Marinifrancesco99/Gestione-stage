from flask import request, jsonify
from app.service.auth_service import AuthService
from sqlalchemy.exc import IntegrityError

class AuthController:
    @staticmethod
    def register():
        data = request.json
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        role = data.get("role", "studente")

        try:
            AuthService.register_user(name, email, password, role)
            return jsonify({"message": "Registrazione avvenuta con successo."}), 201
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 403
        except IntegrityError:
            return jsonify({"error": "Email già registrata."}), 409
        
        
    @staticmethod
    def login():
        data = request.json
        email = data.get("email")
        password = data.get("password")

        token_data = AuthService.login_user(email, password)
        if not token_data:
            return jsonify({"error": "Email o password errati."}), 401

        token, user = token_data
        return jsonify({"token": token, "role": user.role, "user_id": user.id})