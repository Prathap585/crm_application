from flask import Flask
from flask_cors import CORS, cross_origin

UPLOAD_FOLDER = 'D:/uploads'
SENDER_EMAIL = "prathapr585@gmail.com"
SENDER_EMAIL_PASSWORD = "Prathap@mazda1"

app = Flask(__name__)
CORS(app)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SENDER_EMAIL'] = SENDER_EMAIL
app.config['SENDER_EMAIL_PASSWORD'] = SENDER_EMAIL_PASSWORD
