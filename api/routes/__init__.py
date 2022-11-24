from runtime import app, db, bcrypt
from models import User, Student, Hardware
from flask import request
from flask_login import login_user, login_required
from datetime import date


@app.route('/')
def root():
    return "welcome"


@app.route('/login', methods=['POST'])
def login():
    username = request.json["username"]
    password = request.json["password"]
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return 'true'

    return 'false'


@app.route("/students", methods=['GET'])
@login_required
def students():
    students = Student.query.all()
    result = []
    for s in students:
        result.append(s._asdict())
    return result


@app.route("/add_student", methods=['POST'])
@login_required
def add_student():
    name = request.form["name"]
    email = request.form["email"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()
    return "added student"

@app.route("/hardware", methods=['GET'])
@login_required
def hardware():
    hardware = Hardware.query.all()
    result = []
    for h in hardware:
        result.append(h._asdict())
    return result


@app.route("/add_hardware", methods=['POST'])
@login_required
def add_hardware():
    name = request.form["name"]
    identity = request.form["identity"]
    # purchase_date = request.form["purchase_date"]
    comment = request.form["comment"]
    # active = request.form["active"]
    new_hardware = Hardware(name=name, identity=identity, comment=comment, active=False)
    db.session.add(new_hardware)
    db.session.commit()
    return "added hardware"