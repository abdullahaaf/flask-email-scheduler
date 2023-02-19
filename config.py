from decouple import config

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT=True
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=config('SQLALCHEMY_DATABASE_URI')
