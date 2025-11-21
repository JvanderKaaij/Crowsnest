import os
import logging
import datetime
import sys

from runtime import app, db, bcrypt
from models import User, Student, Hardware, StudentAttribute, AttributeType, Attribute
from forms import StudentForm, HardwareForm, AttributeForm

from flask import request, redirect, jsonify
from flask_login import login_user, login_required, current_user, logout_user
from mailjet_rest import Client

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

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


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect('/')


@app.route("/students", methods=['GET'])
@login_required
def students():
    students = Student.query.filter(Student.user_type_id == current_user.user_type_id and Student.active==True)
    result = []
    for s in students:
        stud = s._asdict()
        stud['attributes'] = student_attributes(stud['id'])
        result.append(stud)
    return result


def student_attributes(id):
    attribute_for_student = Attribute.query.filter(Attribute.student_id==id).all()
    result = []
    for s in attribute_for_student:
        attr = s._asdict()
        if s.type is not None: attr['type'] = s.type._asdict()
        result.append(attr)
    return result


@app.route("/add_student", methods=['POST'])
@login_required
def add_student():
    json = request.get_json()
    data = json.get('data')
    form = StudentForm(data=data)

    response = {'success': False, 'message': '', 'errors': {}}
    if form.validate():
        new_student = Student(
            name=form.name.data,
            email=form.email.data,
            start_date=form.start_date.data,
            estimated_end_date=form.estimated_end_date.data,
            user_type_id=current_user.user_type_id
        )

        db.session.add(new_student)
        db.session.commit()
        db.session.refresh(new_student)

        new_attributes = data.get("new_attributes")

        for attribute in new_attributes:
            new_attr = Attribute(
                student_id=new_student.id,
                content=attribute.get("content"),
                attribute_type_id=attribute.get("id")
            )
            db.session.add(new_attr)
            db.session.commit()
            db.session.refresh(new_attr)

        response['success'] = True
        response['message'] = 'student added'
        response['new_student_id'] = new_student.id
        response['attributes'] = student_attributes(new_student.id)
    else:
        response['message'] = 'failed'
        response['errors'] = form.errors
    return response


def add_empty_attributes(student_id):
    types = AttributeType.query.all()
    for t in types:
        attribute = Attribute(content="", attribute_type_id=t.id, student_id=student_id)
        db.session.add(attribute)
        db.session.commit()
        db.session.refresh(attribute)

@app.route("/edit_student", methods=['POST'])
@login_required
def edit_student():
    form = StudentForm(request.form)
    response = {'success': False, 'message': '', 'errors': {}}
    if form.validate():
        student = {
            'name':form.name.data,
            'email':form.email.data,
            'start_date':form.start_date.data,
            'estimated_end_date':form.estimated_end_date.data,
            'active':form.active.data
        }

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
    hardware = Hardware.query.filter(Hardware.user_type_id == current_user.user_type_id and Hardware.active==True)
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
            comment=form.comment.data,
            user_type_id=current_user.user_type_id
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
        hardware = {
            'name':form.name.data,
            'identity':form.identity.data,
            'student_id':form.student_id.data,
            'purchase_date':form.purchase_date.data,
            'comment':form.comment.data,
            'active': form.active.data
        }

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
    all_attribute_types = AttributeType.query.filter(AttributeType.user_type_id == current_user.id)
    result = []
    for s in all_attribute_types:
        result.append(s._asdict())
    return result


@app.route("/attributes", methods=['POST'])
@login_required
def attributes():
    sid = request.args.get("student_id")
    attributes = Attribute.query.filter(Attribute.student_id == sid)

    result = []
    for attr in attributes:
        as_dict = attr._asdict()
        if attr.attribute is not None: as_dict['attribute'] = attr.attribute._asdict()
        result.append(as_dict)

    return result


@app.route("/edit_attribute", methods=['POST'])
@login_required
def edit_attribute():
    form = AttributeForm(request.form)
    response = {'success': False, 'message': '', 'errors': {}}
    if form.validate():
        attribute = {
            'content':form.content.data
        }

        db.session.query(Attribute).filter(Attribute.id == form.id.data).update(attribute)
        db.session.commit()
        response['success'] = True
        response['message'] = 'hardware changed'
    else:
        response['message'] = 'failed'
        response['errors'] = form.errors

    return response


@app.route("/add_attribute", methods=['POST'])
@login_required
def add_attribute():
    form = AttributeForm(request.form)
    response = {'success': False, 'message': '', 'errors': {}}
    if form.validate():
        logging.debug(form.student_id.data)
        new_attr = Attribute(
            student_id=form.student_id.data,
            content=form.content.data,
            attribute_type_id=form.attribute_type_id.data
        )
        db.session.add(new_attr)
        db.session.commit()
        db.session.refresh(new_attr)

        response['success'] = True
        response['message'] = 'attribute created'

    return response

@app.cli.command("check_expired_users")
def check_expired_users():
    current = datetime.datetime.today()
    expired = Student.query.filter(Student.active == True and Student.estimated_end_date <= current).all()
    if len(expired) > 0:
        send_mail(expired)


def format_message(expired_students):
    result = "Expired Students: <br> \n \n "
    for st in expired_students:
        result += "{name} expired on {end_date} <br>\n".format(name=st.name, mail=st.email, end_date=st.estimated_end_date)
    return result


def send_mail(expired_students):
    api_key = os.environ['MJ_APIKEY_PUBLIC']
    api_secret = os.environ['MJ_APIKEY_PRIVATE']
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
      'Messages': [
            {
                "From": {
                        "Email": "j.g.vanderkaaij@uva.nl",
                        "Name": "Crowsnest"
                },
                "To": [
                        {
                                "Email": "j.g.vanderkaaij@uva.nl",
                                "Name": "Joey"
                        }
                ],
                "Subject": "Crowsnest Expired Students",
                "TextPart": format_message(expired_students),
                "HTMLPart": format_message(expired_students)
            }
        ]
    }
    result = mailjet.send.create(data=data)

@app.route("/public/hardware/<int:user_type_id>", methods=['GET'])
def public_hardware(user_type_id):
    hardware = Hardware.query.filter(Hardware.user_type_id == user_type_id, Hardware.active==True)
    result = []
    for h in hardware:
        as_dict = h._asdict()
        if h.student is not None: as_dict['lend_to_student'] = h.student._asdict()
        result.append(as_dict)
    return jsonify(result)