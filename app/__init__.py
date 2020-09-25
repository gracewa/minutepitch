from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from .config import DevConfig
from os import environ
from flask_fontawesome import FontAwesome



bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()
fa = FontAwesome()

photos = UploadSet('photos',IMAGES)

app = Flask(__name__, instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)

# Initializing flask extensions
bootstrap.init_app(app)
db.init_app(app)
login_manager.init_app(app)
mail.init_app(app)
fa.init_app(app)

# configure UploadSet
configure_uploads(app,photos)

from app import views
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

if __name__ == "__main__":
    app.run(debug=True)
