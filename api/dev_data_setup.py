from runtime import app, db, bcrypt
from models import *

with app.app_context():
    db.create_all()
    hash_pass = bcrypt.generate_password_hash('test')

    admin_type = UserType(name="admin")
    db.session.add(admin_type)

    db.session.commit()

    admin = User(username='admin', password=hash_pass, user_type_id=1)
    db.session.add(admin)

    vislab_type = UserType(name="vislab")
    db.session.add(vislab_type)

    db.session.commit()

    vislab = User(username='vislab', password=hash_pass, user_type_id=2)
    db.session.add(vislab)

    db.session.commit()

    st_one = Student(name="test_student_one", email="student_one@email.com", active=1)
    db.session.add(st_one)

    st_two = Student(name="test_student_two", email="student_two@email.com", active=1)
    db.session.add(st_two)

    db.session.commit()

    hw_one = Hardware(name="Hammer", identity="0x0x0x0x", comment="comment", active=1)
    db.session.add(hw_one)

    hw_two = Hardware(name="Bucket", student_id=1, identity="yxyxyxyxyx", comment="Bucket Comment", active=1)
    db.session.add(hw_two)

    db.session.commit()

    attr_type = AttributeType(name="Ports", multiple=True, element_type="int", user_type_id=1)
    db.session.add(attr_type)

    attr_type = AttributeType(name="Git", multiple=False, element_type="bool", user_type_id=1)
    db.session.add(attr_type)

    attr_type = AttributeType(name="Servers", multiple=True, element_type="string", user_type_id=1)
    db.session.add(attr_type)

    db.session.commit()

    attr_one = Attribute(content="8042", attribute_type_id=1)
    db.session.add(attr_one)

    std_attr_one = StudentAttribute(student_id=1, attribute_id=1)
    db.session.add(std_attr_one)

    db.session.commit()
