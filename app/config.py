import os

class Config:
    '''
    General configuration parent class
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:g11111111@localhost/minutepitch'
    SECRET_KEY = os.urandom(32)
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    # Email Settings
    EMAIL_USE_SSL = True
    EMAIL_HOST = 'smtp.zoho.com'
    EMAIL_PORT = 465
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
            SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
