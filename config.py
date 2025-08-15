import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacity.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'hello'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityuser'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Udacity@1234'
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'hellowo123'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'bwC9rXbhvcbHUbHOD4RrWXChBDxEQ0qBkGguUjjz44R+SF73o69Kamhk+qtqOQKTfxCVW/xrSpBn+AStvZLVdg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
