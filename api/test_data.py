from runtime import app, db, bcrypt
from models import *

with app.app_context():
    st_one = Student(name="test_student_one", email="student_one@email.com", active=1)
    db.session.add(st_one)

    st_two = Student(name="test_student_two", email="student_two@email.com", active=1)
    db.session.add(st_two)

    hw_one = Hardware(name="Hammer", identity="0x0x0x0x", comment="comment", active=1)
    db.session.add(hw_one)

    hw_two = Hardware(name="Bucket", student_id=1, identity="yxyxyxyxyx", comment="Bucket Comment", active=1)
    db.session.add(hw_two)

    attr_type = AttributeType(name="Port")
    db.session.add(attr_type)

    attr_one = Attribute(type=1, content="8042")
    db.session.add(attr_one)

    std_attr_one = StudentAttribute(student_id=1, attribute_id=1)
    db.session.add(std_attr_one)

    db.session.commit()
