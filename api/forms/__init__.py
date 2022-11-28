from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField,TextAreaField, IntegerField
from wtforms import validators
from datetime import date, datetime


class StudentForm(FlaskForm):
    class Meta:
        csrf = False
    name = StringField('name', validators=[validators.DataRequired(), validators.Length(min=3, max=90)])
    email = StringField('email', validators=[validators.DataRequired(), validators.Length(min=3, max=90)])
    start_date = DateField('start_date',default=datetime(1970, 1, 1))
    estimated_end_date = DateField('estimated_end_date',default=datetime(1970, 1, 1))
    has_door_access = IntegerField('has_door_access',default=False)
    has_git_access = IntegerField('has_git_access',default=False)
    has_git_lfs_access = IntegerField('has_git_lfs_access',default=False)
    active = IntegerField('active', default=True)

class HardwareForm(FlaskForm):
    class Meta:
        csrf = False
    name = StringField('name', validators=[validators.DataRequired(), validators.Length(min=3, max=90)])
    identity = StringField('identity', validators=[validators.Length(min=1, max=90)])
    purchase_date = DateField('purchase_date',default=datetime(1970, 1, 1))
    student_id = IntegerField('student_id',default=0)
    comment = TextAreaField('comment')
    active = IntegerField('active',default=True)