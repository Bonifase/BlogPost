from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import app_config

db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=True)

from app imphort views

app.config['JWT_SECRET_KEY'] = 'supersecretishere'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config.from_object(app_config["development"])

db.init_app(app)
CORS(app)
