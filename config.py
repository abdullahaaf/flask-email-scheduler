from decouple import config

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER=config('MAIL_SERVER')
    MAIL_PORT=config('MAIL_PORT')
    MAIL_USERNAME=config('MAIL_USERNAME')
    MAIL_PASSWORD=config('MAIL_PASSWORD')
    MAIL_USE_TLS=config('MAIL_USE_TLS')
    MAIL_DEFAULT_SENDER=config('MAIL_DEFAULT_SENDER')
    JSON_AS_ASCII=False

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT=True
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=config('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER=config('MAIL_SERVER')
    MAIL_PORT=config('MAIL_PORT')
    MAIL_USERNAME=config('MAIL_USERNAME')
    MAIL_PASSWORD=config('MAIL_PASSWORD')
    MAIL_USE_TLS=config('MAIL_USE_TLS')
    MAIL_DEFAULT_SENDER=config('MAIL_DEFAULT_SENDER')
    JSON_AS_ASCII=False
