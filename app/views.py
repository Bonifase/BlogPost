from app import app
from flask import jsonify


@app.route('/')
def index():
    return jsonify("Welcome To BlogPost")
# Endpoint to Register user and saving the details in a list called users
