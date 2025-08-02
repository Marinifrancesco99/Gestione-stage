from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from app.config import Config
from app.routes.user_routes import user_bp
from app.routes.auth_routes import auth_bp
from app.routes.attendanceLogs_routes import attendanceLogs_bp
from app.routes.classes_routes import classes_bp
from app.extension import db, migrate
from app.exceptions.not_found import NotFoundException


# Importa tutti i modelli per renderli visibili alle migrazioni
from app.model import (
    user, tutor, students, interviews, professors, courses, internships, convention, companies, companyTipes, classes, association, attendanceLogs, HistoryStatus, notification
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  # collega migrate all'app e al db
    
    CORS(app)
    
    @app.errorhandler(NotFoundException)
    def handle_not_found(e):
        return jsonify({"error": e.message}), 404

    # Registra le rotte
    
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(attendanceLogs_bp, url_prefix="/api/attendance_logs")
    app.register_blueprint(classes_bp, url_prefix="/api/classes")

    return app