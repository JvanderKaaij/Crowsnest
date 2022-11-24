from runtime import app, db, bcrypt
from models import User, Student, Hardware
from forms import StudentForm, HardwareForm
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
        logging.error(form.active.data)
        new_student = Student(
            name=form.name.data,
            email=form.email.data,
            start_date=form.start_date.data,
            estimated_end_date=form.end_date.data,
            has_door_access=form.has_door_access.data,
            has_git_access=form.has_git_access.data,
            has_git_lfs_access=form.has_git_lfs_access.data
        )

        db.session.add(new_student)
        db.session.commit()
        return "added student"
    return f'{form.errors}'

@app.route("/edit_student", methods=['POST'])
@login_required
def edit_student():
    student = db.session.query(Student).get(request.form['id'])
    if "name" in request.form: student.name = request.form['name']
    if "email" in request.form: student.email = request.form['email']
    if "start_date" in request.form: student.start_date = request.form['start_date']
    if "end_date" in request.form: student.estimated_end_date = request.form['end_date']
    if "has_door_access" in request.form: student.has_door_access = request.form['has_door_access']
    if "has_git_access" in request.form: student.has_git_access = request.form['has_git_access']
    if "has_git_lfs_access" in request.form: student.has_git_lfs_access = request.form['has_git_lfs_access']
    if "active" in request.form: student.active = request.form['active']
    db.session.commit()
    return "changed student"

@app.route("/hardware", methods=['GET'])
@login_required
def hardware():
    hardware = Hardware.query.all()
    result = []
    for h in hardware:
        as_dict = h._asdict()
        if h.student is not None: as_dict['lend_to_student'] = h.student._asdict()
        result.append(as_dict)
    return result

@app.route("/add_hardware", methods=['POST'])
@login_required
def add_hardware():
    form = HardwareForm(request.form)
    if form.validate():
        new_hardware = Hardware(
            name=form.name.data,
            identity=form.identity.data,
            purchase_date=form.purchase_date.data,
            comment=form.comment.data
        )

        db.session.add(new_hardware)
        db.session.commit()
        return "hardware added"
    return f'{form.errors}'

@app.route("/edit_hardware", methods=['POST'])
@login_required
def edit_hardware():
    hardware = db.session.query(Hardware).get(request.form['id'])
    if "name" in request.form: hardware.name = request.form['name']
    if "student_id" in request.form: hardware.student_id = request.form['student_id']
    if "identity" in request.form: hardware.identity = request.form['identity']
    if "purchase_date" in request.form: hardware.purchase_date = request.form['purchase_date']
    if "comment" in request.form: hardware.comment = request.form['comment']
    if "active" in request.form: hardware.active = request.form['active']
    db.session.commit()
    return "hardware changed"