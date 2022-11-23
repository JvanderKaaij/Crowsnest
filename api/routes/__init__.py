from runtime import app, bcrypt
from models import User
from flask import request
from flask_login import login_user, login_required


@app.route('/')
def root():
    return "welcome"


@app.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return "user logged in"

    return f'{username} not found'


@app.route("/settings", methods=['GET'])
@login_required
def settings():
    return "settings"
