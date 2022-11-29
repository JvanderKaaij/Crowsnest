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
    students = Student.query.filter(Student.active==True)
    result = []
    for s in students:
        result.append(s._asdict())
    return result


@app.route("/add_student", methods=['POST'])
@login_required
def add_student():
    form = StudentForm(request.form)
    response = {'success': False, 'message': '', 'errors': {}}
    if form.validate():
        logging.error(form.active.data)
        new_student = Student(
            name=form.name.data,
            email=form.email.data,
            start_date=form.start_date.data,
            estimated_end_date=form.estimated_end_date.data,
            has_door_access=form.has_door_access.data,
            has_git_access=form.has_git_access.data,
            has_git_lfs_access=form.has_git_lfs_access.data
        )

        db.session.add(new_student)
        db.session.commit()
        response['success'] = True
        response['message'] = 'student added'
    else:
        response['message'] = 'failed'
        response['errors'] = form.errors
    return response

@app.route("/edit_student", methods=['POST'])
@login_required
def edit_student():
    logging.error(request.form)
    form = StudentForm(request.form)
    response = {'success': False, 'message': '', 'errors': {}}
    if form.validate():
        logging.error(form)

        student = {
            'name':form.name.data,
            'email':form.email.data,
            'start_date':form.start_date.data,
            'estimated_end_date':form.estimated_end_date.data,
            'has_door_access':form.has_door_access.data,
            'has_git_access':form.has_git_access.data,
            'has_git_lfs_access':form.has_git_lfs_access.data,
            'active':form.active.data
        }

        logging.error(form.id.data)
        db.session.query(Student).filter(Student.id == form.id.data).update(student)
        db.session.commit()
        response['success'] = True
        response['message'] = 'student changed'
    else:
        response['message'] = 'failed'
        response['errors'] = form.errors

    return response

@app.route("/hardware", methods=['GET'])
@login_required
def hardware():
    hardware = Hardware.query.filter(Hardware.active==True)
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
    response = {'success':False, 'message':'', 'errors': {}}
    if form.validate():
        new_hardware = Hardware(
            name=form.name.data,
            identity=form.identity.data,
            student_id=form.student_id.data,
            purchase_date=form.purchase_date.data,
            comment=form.comment.data
        )

        db.session.add(new_hardware)
        db.session.commit()
        response['success'] = True
        response['message'] = 'hardware added'
    else:
        response['message'] = 'failed'
        response['errors'] = form.errors

    return response

@app.route("/edit_hardware", methods=['POST'])
@login_required
def edit_hardware():
    logging.error(request.form)
    form = HardwareForm(request.form)
    response = {'success': False, 'message': '', 'errors': {}}
    if form.validate():
        logging.error(form)

        hardware = {
            'name':form.name.data,
            'identity':form.identity.data,
            'student_id':form.student_id.data,
            'purchase_date':form.purchase_date.data,
            'comment':form.comment.data,
            'active': form.active.data
        }

        logging.error(form.id.data)
        db.session.query(Hardware).filter(Hardware.id == form.id.data).update(hardware)
        db.session.commit()
        response['success'] = True
        response['message'] = 'hardware changed'
    else:
        response['message'] = 'failed'
        response['errors'] = form.errors

    return response
