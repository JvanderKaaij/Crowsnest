from runtime import app, db, bcrypt
from models import *
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    type_name = sys.argv[3]

    with app.app_context():
        db.create_all()
        db.session.commit()
        hash_pass = bcrypt.generate_password_hash(password)

        type = db.session.query(UserType).filter(UserType.name == type_name).first()

        type_id = None
        if type is None:
            admin_type = UserType(name=type_name)
            db.session.add(admin_type)
            db.session.commit()
            db.session.refresh(admin_type)
            type_id = admin_type.id
        else:
            type_id = type.id

        admin = User(username=username, password=hash_pass, user_type_id=type_id)
        db.session.add(admin)

        db.session.commit()