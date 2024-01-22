from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, IntegerField, FieldList, FormField
from wtforms import validators
from datetime import datetime


class TempAttributeForm(FlaskForm):
    class Meta:
        csrf = False
    id = IntegerField('id')
    content = StringField('content')


class AttributeForm(FlaskForm):
    class Meta:
        csrf = False
    id = IntegerField('id')
    content = StringField('content')
    student_id = IntegerField('student_id', validators=[validators.Optional()])
    attribute_type_id = IntegerField('attribute_type_id', validators=[validators.Optional()])


class StudentForm(FlaskForm):
    class Meta:
        csrf = False
    id = IntegerField('id')
    name = StringField('name', validators=[validators.DataRequired(), validators.Length(min=3, max=90)])
    email = StringField('email')
    start_date = DateField('start_date', default=datetime(1970, 1, 1))
    estimated_end_date = DateField('estimated_end_date', default=datetime(1970, 1, 1))
    has_door_access = IntegerField('has_door_access', default=False)
    has_git_access = IntegerField('has_git_access', default=False)
    has_git_lfs_access = IntegerField('has_git_lfs_access', default=False)
    active = IntegerField('active', default=True)
    new_attributes = FieldList(FormField(TempAttributeForm))


class HardwareForm(FlaskForm):
    class Meta:
        csrf = False
    id = IntegerField('id')
    name = StringField('name', validators=[validators.DataRequired(), validators.Length(min=3, max=90)])
    identity = StringField('identity')
    purchase_date = DateField('purchase_date',default=datetime(1970, 1, 1))
    student_id = IntegerField('student_id', validators=[validators.Optional()])
    comment = TextAreaField('comment')
    active = IntegerField('active', default=True)
