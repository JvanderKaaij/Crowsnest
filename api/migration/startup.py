from runtime import app, db, bcrypt
from models import *

with app.app_context():
    db.create_all()

    hash_pass = bcrypt.generate_password_hash('E2LFdU8R^z%e4z')

    admin_type = UserType(name="admin")
    db.session.add(admin_type)

    db.session.commit()

    admin = User(username='jkaaij', password=hash_pass, user_type_id=1)
    db.session.add(admin)

    vislab_type = UserType(name="vislab")
    db.session.add(vislab_type)

    db.session.commit()

    vislab = User(username='vislab', password=hash_pass, user_type_id=2)
    db.session.add(vislab)

    db.session.commit()

