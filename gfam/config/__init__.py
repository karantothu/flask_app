class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost:3306/gfam'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True