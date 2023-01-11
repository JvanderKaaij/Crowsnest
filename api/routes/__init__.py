from runtime import app, db, bcrypt
from models import User, Student, Hardware, StudentAttribute, AttributeType, Attribute
from forms import StudentForm, HardwareForm, AttributeForm
import logging

from flask import request
from flask_login import login_user, login_required, current_user

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
        stud = s._asdict()
        stud['attributes'] = student_attributes(stud['id'])
        result.append(stud)
    return result


def student_attributes(id):
    attribute_for_student = StudentAttribute.query.filter(StudentAttribute.student_id==id).all()
    result = []
    for s in attribute_for_student:
        attr = s.attribute._asdict()
        if s.attribute.type is not None: attr['type'] = s.attribute.type._asdict()
        result.append(attr)
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
        db.session.refresh(new_student)
        add_empty_attributes(new_student.id)
        response['success'] = True
        response['message'] = 'student added'
    else:
        response['message'] = 'failed'
        response['errors'] = form.errors
    return response


def add_empty_attributes(student_id):
    types = AttributeType.query.all()
    for t in types:
        attribute = Attribute(content="", attribute_type_id=t.id)
        db.session.add(attribute)
        db.session.commit()
        db.session.refresh(attribute)
        attr_student = StudentAttribute(student_id=student_id, attribute_id=attribute.id)
        db.session.add(attr_student)
        db.session.commit()


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


@app.route("/attribute_types", methods=['GET'])
@login_required
def attribute_types():
    all_attribute_types = AttributeType.query.all()
    result = []
    for s in all_attribute_types:
        result.append(s._asdict())
    return result


@app.route("/edit_attribute", methods=['POST'])
@login_required
def edit_attribute():
    logging.error(request.form)
    form = AttributeForm(request.form)
    response = {'success': False, 'message': '', 'errors': {}}
    if form.validate():
        logging.error('validated')
        logging.error(form.content.data)

        attribute = {
            'content':form.content.data
        }

        logging.error(form.id.data)
        db.session.query(Attribute).filter(Attribute.id == form.id.data).update(attribute)
        db.session.commit()
        response['success'] = True
        response['message'] = 'hardware changed'
    else:
        response['message'] = 'failed'
        response['errors'] = form.errors

    return response