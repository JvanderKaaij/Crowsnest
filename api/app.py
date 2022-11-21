import os
from flask import Flask
from sqlalchemy import create_engine

engine = create_engine(os.environ['DATABASE_URL'])
app = Flask(__name__)

@app.route('/')
def hello():
    with engine.connect() as connection:
        result = connection.execute("SELECT ID FROM users")
        for row in result:
            print("username:", row['ID'])

    return 'test hello 123'
