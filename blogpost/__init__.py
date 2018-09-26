from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'somerandomnumbers'
app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:///site.db"

db = SQLAlchemy(app)

from blogpost import routes
