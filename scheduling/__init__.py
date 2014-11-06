from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)
app.config['SECRET_KEY'] = '24fec6632cf39ecaa8a7f3028f3485da77bd11e644fa114572f16f8a5b6e4910'
app.config['DATABASE_FILE'] = 'scheduling.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

admin = Admin(app, name='Scheduling Admin')

from scheduling import base
