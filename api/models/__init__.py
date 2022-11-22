from runtime import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(60))
    def __repr__(self):
        return f"{self.id} - {self.username}"
