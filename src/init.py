from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config
from .routes.user_routes import user_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    # Registra le rotte
    
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app


