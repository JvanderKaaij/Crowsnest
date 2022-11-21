from runtime import db

class Users(db.Model):
    __tablename__ = "users"
    ID = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"{self.ID}"