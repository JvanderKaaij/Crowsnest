from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField,TextAreaField
from wtforms import validators
from datetime import date, datetime


class StudentForm(FlaskForm):
    name = StringField('name', validators=[validators.DataRequired(), validators.Length(min=3, max=90)])
    email = StringField('email', validators=[validators.DataRequired(), validators.Length(min=3, max=90)])
    start_date = DateField('start_date',default=datetime(1970, 1, 1))
    end_date = DateField('end_date',default=datetime(1970, 1, 1))
    has_door_access = BooleanField('has_door_access',default=False)
    has_git_access = BooleanField('has_git_access',default=False)
    has_git_lfs_access = BooleanField('has_git_lfs_access',default=False)

class HardwareForm(FlaskForm):
    name = StringField('name', validators=[validators.DataRequired(), validators.Length(min=3, max=90)])
    identity = StringField('identity', validators=[validators.Length(min=1, max=90)])
    purchase_date = DateField('purchase_date',default=datetime(1970, 1, 1))
    comment = TextAreaField('comment')
    active = BooleanField('active',default=True)