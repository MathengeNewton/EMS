class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mathenge,./1998@127.0.0.1:5432/ems'
    SECRET_KEY = 'some-random-key'

class ProductionConfig(Config):
    DEBUG=False
    SECRET_KEY = 'SOME-RANDOM-KEY'