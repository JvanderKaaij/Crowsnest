from runtime import app, db
from models import Users

with app.app_context():
    db.create_all()
    admin = Users(username='admin', password='test')
    db.session.add(admin)
    db.session.commit()
