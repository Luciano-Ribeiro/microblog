import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


class Config(object):
    FLASK_APP = "microblog.py"
    SECRET_KEY = "senha-secreta"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


