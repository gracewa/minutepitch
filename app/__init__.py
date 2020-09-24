from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:g11111111@localhost/minutepitch'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Initializing flask extensions
bootstrap.init_app(app)
db.init_app(app)
login_manager.init_app(app)

from app import views
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

if __name__ == "__main__":
    app.run()
