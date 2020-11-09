from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()

def create_app():
    app: Flask = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize plugins
    db.init_app(app)

    with app.app_context():
        from german_quiz_app import routes   

        # Register blueprints
        # app.register_blueprint(auth.auth_bp)

        return app
