from flask import request
from flask_api import FlaskAPI, status
from flask_sqlalchemy import SQLAlchemy
import os


app = FlaskAPI(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

from views import *


if __name__ == '__main__':
    app.run()

