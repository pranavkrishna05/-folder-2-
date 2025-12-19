# settings.py
class Config:
 SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
 SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
 SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
 DEBUG = True

class ProductionConfig(Config):
 DEBUG = False
