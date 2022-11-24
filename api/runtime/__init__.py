import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_wtf.csrf import generate_csrf

app = Flask(__name__)
app.config["SECRET_KEY"] = "/|Q`4~n>f}t+N7VcXUQSx+~VkI>>ki"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)

@app.after_request
def set_xsrf_cookie(response):
    response.set_cookie('CSRF-TOKEN', generate_csrf())
    return response


import routes