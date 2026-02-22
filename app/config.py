import os

class Config:
    # App Screte Key
    SECRET_KEY = os.environ.get("SECRET_KEY")

    #Database Configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLCHEMY_TRACK_MODIFICATIONS = False

    # File Configurations
    PRODUCT_PIC_FOLDER = os.environ.get("PRODUCT_PIC_FOLDER")
    CHAT_FILE_UPLOAD_FOLDER = os.environ.get("CHAT_FILE_UPLOAD_FOLDER")
    PROFILE_PIC_UPLOAD_FOLDER = os.environ.get("PROFILE_PIC_UPLOAD_FOLDER")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # Email Service Configurations
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS = True
    MAIL_PORT = 587
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME")