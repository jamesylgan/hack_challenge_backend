import os
# Different environments for the app to run in

# Database info
DB_USERNAME             = 'postgres' #windows wouldnt update env so had to hardcode
#DB_USERNAME            = os.environ['DB_USERNAME']
DB_PASSWORD             = os.environ['DB_PASSWORD']
DB_HOST                 = os.environ['DB_HOST']
DB_NAME                 = 'flaskplate_db' #windows wouldnt update env so had to hardcode
#DB_NAME                = os.environ['DB_NAME']
DB_URL                  = 'postgresql://{}:{}@{}/{}'.format(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME)

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  CSRF_ENABLED = True
  CSRF_SESSION_KEY = "secret"
  SECRET_KEY = "not_this"
  SQLALCHEMY_DATABASE_URI = DB_URL

class ProductionConfig(Config):
  DEBUG = False

class StagingConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True

class TestingConfig(Config):
  TESTING = True
