import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'\x84\x88E\x08a\xb9\xe0\xd0\xa4\xf0\x84\x0b\x03\xe6A\x92'"
    MONGODB_SETTINGS = {'db' : 'TEST'}
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gl.007@localhost/test'
    # SQLALCHEMY_TRACK_MODIFICATIONS = True