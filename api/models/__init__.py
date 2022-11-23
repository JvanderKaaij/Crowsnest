from runtime import db, login_manager
from flask_login import UserMixin
import json
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(60))

    def __repr__(self):
        return f"{self.id} - {self.username}"


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(60))
    start_date = db.Column(db.DateTime(timezone=True))
    estimated_end_date = db.Column(db.DateTime(timezone=True))
    onboarding = db.relationship("Onboarding")
    borrowed_hardware = db.relationship("Hardware")

    def _asdict(self):
        return {c.key: getattr(self, c.key)
                for c in db.inspect(self).mapper.column_attrs}



class Onboarding(db.Model):
    __tablename__ = "onboarding"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    door = db.Column(db.Boolean, default=False)
    git = db.Column(db.Boolean, default=False)
    git_lfs = db.Column(db.Boolean, default=False)


class Hardware(db.Model):
    __tablename__ = "hardware"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    name = db.Column(db.String(90))
    identity = db.Column(db.String(90))
    purchase_date = db.Column(db.DateTime(timezone=True))
    comment = db.Column(db.Text)
    active = db.Column(db.Boolean, default=False)

    def _asdict(self):
        return {c.key: getattr(self, c.key)
                for c in db.inspect(self).mapper.column_attrs}