import os.path
diretorio = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(diretorio, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '098765'
