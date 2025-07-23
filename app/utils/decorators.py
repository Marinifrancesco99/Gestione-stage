from functools import wraps
from flask import request, jsonify, g
from app.utils.auth import decode_jwt

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Token mancante"}), 401

        token = auth_header.split(" ")[1]
        payload = decode_jwt(token)
        if not payload:
            return jsonify({"error": "Token non valido o scaduto"}), 401

        g.current_user = payload
        return f(*args, **kwargs)

    return decorated_function
