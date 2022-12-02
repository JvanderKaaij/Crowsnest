from runtime import app, db, bcrypt
from models import User

with app.app_context():
    db.create_all()
    hash_pass = bcrypt.generate_password_hash('test')
    admin = User(username='admin', password=hash_pass, type="admin")
    db.session.add(admin)
    vislab = User(username='vislab', password=hash_pass, type="vislab")
    db.session.add(vislab)
    db.session.commit()
