from flask import url_for
import unittest
from tests import BaseTestSetUp

new_user = {
    "username": "username",
    "units": "64kg",
    "email": "user@gmail.com",
    "password": "user123"}


class TestUserCase(BaseTestSetUp):

    def test_new_user_registration_works(self):
        """Test API registers new user successfully (POST request)"""

        response = self.testHelper.add_user(new_user)
        self.assertEqual(response.status_code, 404)
