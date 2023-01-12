from runtime import db, login_manager
from flask_login import UserMixin
import json

class ExportMixin(object):
    def _asdict(self):
        return {c.key: getattr(self, c.key)
                for c in db.inspect(self).mapper.column_attrs}


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(60))
    user_type_id = db.Column(db.Integer, db.ForeignKey("user_type.id"), nullable=True)


class UserType(db.Model, UserMixin):
    __tablename__ = "user_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))


class Student(db.Model, ExportMixin):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(60))
    start_date = db.Column(db.DateTime(timezone=True))
    estimated_end_date = db.Column(db.DateTime(timezone=True))
    has_door_access = db.Column(db.Integer, default=False)
    has_git_access = db.Column(db.Integer, default=False)
    has_git_lfs_access = db.Column(db.Integer, default=False)
    active = db.Column(db.Integer, default=True)


class StudentAttribute(db.Model, ExportMixin):
    __tablename__ = "student_attribute"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.ForeignKey("student.id"))
    attribute_id = db.Column(db.ForeignKey("attribute.id"))
    student = db.relationship('Student', uselist=False)
    attribute = db.relationship('Attribute', uselist=False)


class Attribute(db.Model, ExportMixin):
    __tablename__ = "attribute"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(60))
    attribute_type_id = db.Column(db.Integer, db.ForeignKey("attribute_type.id"))
    type = db.relationship('AttributeType')


class AttributeType(db.Model, ExportMixin):
    __tablename__ = "attribute_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    multiple = db.Column(db.Integer, default=False)
    element_type = db.Column(db.String(60))
    user_type_id = db.Column(db.Integer, db.ForeignKey("user_type.id"), nullable=True)


class Hardware(db.Model, ExportMixin):
    __tablename__ = "hardware"
    id = db.Column(db.Integer, primary_key=True)
    student = db.relationship("Student", uselist=False)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=True)
    name = db.Column(db.String(90))
    identity = db.Column(db.String(90))
    purchase_date = db.Column(db.DateTime(timezone=True))
    comment = db.Column(db.Text)
    active = db.Column(db.Integer, default=True)



