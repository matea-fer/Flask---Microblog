import os 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    #MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'matea.zadar95@gmail.com'
    MAIL_PASSWORD = 'lopticaskocica1'
    ADMINS = ['matea.zadar95@gmail.com']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY='af0b113076c848d4b0ce583c8acd503c'