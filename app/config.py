# Config file for Flask app

class Config:
    DEBUG = True
    TESTING = False
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "password"  # Cryptographic signing for Cross-Site Request Forgery(CSRF) protection and to sign session
    APP_PORT = 8000
    HOST_IP = "localhost"