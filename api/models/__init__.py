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


class Student(db.Model, ExportMixin):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(60))
    start_date = db.Column(db.DateTime(timezone=True))
    estimated_end_date = db.Column(db.DateTime(timezone=True))
    borrowed_hardware = db.relationship("Hardware")
    has_door_access = db.Column(db.Boolean, default=False)
    has_git_access = db.Column(db.Boolean, default=False)
    has_git_lfs_access = db.Column(db.Boolean, default=False)

class Hardware(db.Model, ExportMixin):
    __tablename__ = "hardware"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    name = db.Column(db.String(90))
    identity = db.Column(db.String(90))
    purchase_date = db.Column(db.DateTime(timezone=True))
    comment = db.Column(db.Text)
    active = db.Column(db.Boolean, default=False)



