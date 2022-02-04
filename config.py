# from distutils.debug import DEBUG
# # from pickle import TRUE
import os

class Config(object):
    TESTING = False
    DEBUG = True


class DevelopmentConfig(Config):
    UPLOAD_FOLDER = "/home/matheus/Documentos/converteAudioTexto/app/uploads"
    UPLOAD_PATH = "app/uploads" #os.open("app/uploads", os.O_RDONLY)
    UPLOAD_EXTENSIONS = ['.wav']
    SECRET_KEY = 'audioPython'

    
