from runtime import app
from models import Users

@app.route('/')
def root():
    return Users().query.first().__repr__()