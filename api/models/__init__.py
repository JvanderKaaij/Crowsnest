from runtime import db

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(60))
    def __repr__(self):
        return f"{self.id} - {self.username}"