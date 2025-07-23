from flask import Blueprint, request, jsonify
from app.dao.user_dao import UsersDAO
from app.model.user import User
from app.utils.auth import hash_password, verify_password, generate_jwt, decode_jwt
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint('auth', __name__)

# Registration route
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "studente")  # Default a studente

    # Permetti solo la registrazione come studente
    if role != "studente":
        return jsonify({"error": "Non puoi registrarti come admin, scuola o tutor."}), 403

    if not all([name, email, password]):
        return jsonify({"error": "Tutti i campi sono obbligatori."}), 400

    hashed = hash_password(password)
    try:
        user = UsersDAO.create_user(name, email, hashed, role)
    except IntegrityError:
        return jsonify({"error": "Email già registrata."}), 409

    return jsonify({"message": "Registrazione avvenuta con successo."}), 201



# Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = UsersDAO.get_user_by_email(email)
    if not user or not verify_password(password, user.password):
        return jsonify({"error": "Email o password errati."}), 401

    token = generate_jwt(user.id, user.role)
    return jsonify({"token": token, "role": user.role, "user_id": user.id})