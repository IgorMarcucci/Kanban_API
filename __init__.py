from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:lipao2002@localhost:5432/flask"

    db.init_app(app)
    migrate.init_app(app, db)

    return app