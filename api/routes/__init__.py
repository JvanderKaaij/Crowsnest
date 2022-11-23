from runtime import app, db, bcrypt
from models import User, Student, Onboarding, Hardware
from flask import request
from flask_login import login_user, login_required
from datetime import date

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


@app.route("/add_onboarding", methods=['POST'])
@login_required
def add_onboarding():
    student_id = request.form["student_id"]
    new_onboarding = Onboarding(student_id=student_id, door=False, git=False, git_lfs=False)
    db.session.add(new_onboarding)
    db.session.commit()
    return "added onboarding"


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