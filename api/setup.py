from runtime import app, db, bcrypt
from models import User

with app.app_context():
    db.create_all()
    hash_pass = bcrypt.generate_password_hash('test')
    admin = User(username='admin', password=hash_pass)
    db.session.add(admin)
    db.session.commit()
