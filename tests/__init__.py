import unittest
import json
from urllib.parse import urljoin
from blogpost import app

from blogpost.models.models import *


class BaseTestSetUp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app
        self.app.config['SERVER_NAME'] = 'http://127.0.0.1:5000'
        self.app.config['SECRET_KEY'] = 'some-random-string-that-should-be'
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
        self.app = app.test_client()
        self.testHelper = TestHelper()
        self.base_url = self.testHelper.base_url
        self.app = self.testHelper.app
        self.headers = self.testHelper.headers

        with app.app_context():
            # create all tables
            db.session.close()
            db.drop_all()
            db.create_all()


user_data = {
    "first_name": "username",
    "last_name": "lastname",
    "last_name": "lastname",
    "units": "64kg",
    "email": "user@gmail.com",
    "password": "user123"}


class TestHelper():

    def __init__(self):
        self.base_url = 'http://127.0.0.1:5000'
        self.headers = {'content-type': 'application/json'}
        self.app = app.test_client()
    # Create a new user

    def add_user(self, user_data):
        url = self.base_url + '/register'
        result = self.app.post("/register", data=user_data)
        print("++++++++++++++", result)
        return result

    def login_user(self, user_data):
        url = self.base_url + '/api/login'
        result = self.app.post(url, data=json.dumps(
            user_data), headers=self.headers)
        return result
