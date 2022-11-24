from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField
from wtforms.validators import DataRequired
from datetime import date, datetime


class StudentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    start_date = DateField('start_date',default=datetime(1970, 1, 1))
    end_date = DateField('end_date',default=datetime(1970, 1, 1))
    has_door_access = BooleanField('has_door_access',default=False)
    has_git_access = BooleanField('has_git_access',default=False)
    has_git_lfs_access = BooleanField('has_git_lfs_access',default=False)