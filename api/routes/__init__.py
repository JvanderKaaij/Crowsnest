from runtime import app, db, bcrypt
from models import User, Student, Hardware
from forms import StudentForm
import logging

from flask import request
from flask_login import login_user, login_required
from datetime import datetime


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
    form = StudentForm(request.form)
    if form.validate():
        new_student = Student(
            name=form.name.data,
            email=form.email.data,
            start_date=form.start_date.data,
            estimated_end_date=form.end_date.data,
            has_door_access=form.has_door_access.data,
            has_git_access=form.has_git_access.data,
            has_git_lfs_access=form.has_git_lfs_access.data,
        )

        db.session.add(new_student)
        db.session.commit()
        return "added student"
    return f'{form.errors}'

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