from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from app.config import Config
from app.routes.user_routes import user_bp

db = SQLAlchemy()
migrate = Migrate()  # inizializza Migrate

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

    # Registra le rotte
    
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app