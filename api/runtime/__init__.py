import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_wtf.csrf import generate_csrf

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ['COOKIE_SECRET']
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://root:{os.environ['MYSQL_ROOT_PASSWORD']}@db:3306/{os.environ['MYSQL_DATABASE']}"

print(app.config["SQLALCHEMY_DATABASE_URI"] )

db = SQLAlchemy(app)

login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)

@app.after_request
def set_xsrf_cookie(response):
    response.set_cookie('CSRF-TOKEN', generate_csrf())
    return response


import routes