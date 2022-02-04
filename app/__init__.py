import os
from flask import Flask, Blueprint, request, redirect, flash, render_template
from werkzeug.utils import secure_filename


# ALLOWED_EXTENSIONS = {'wav'}
app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

# app.config['UPLOAD_FOLDER'] 

# def inicia_app():
from app.audio.routes import audio

app.register_blueprint(audio)

    # return app


# if __name__ == "__main__":
#     inicia_app()
