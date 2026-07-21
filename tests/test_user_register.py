from lib.my_requests import MyRequests
import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user", data=data)

        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_code_status(response, 200)

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('UTF-8') == f"Users with email '{email}' already exists", f"unexpected content {response.content}"

    def test_create_user_with_invalid_email(self):
        email = 'vin_example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode('UTF-8') == f"Cannot create user with incorrect email '{email}'", f"unexpected content {response.content}"

    empty_fields = {
        'password',
        'username',
        'firstName',
        'lastName',
        'email'
    }
    @pytest.mark.parametrize("empty_field", empty_fields)
    def test_create_user_with_empty_fields(self, empty_field):
        data = self.prepare_registration_data()
        data.pop(empty_field,None)

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode('UTF-8') == f"Cannot create user with empty field '{empty_field}'", f"unexpected content {response.content}"


    names = {
        "A",
        "xK9mP2vL7qZ4nR8sT1wY6jH3cD5fG0aS9kM4pB7lQ2zX8vN1tY5rH6cJ9dF3sA7mP0kL2qZ8nR4tW1yV6bH9cD2fG5aS8kM1pB4lQ7zX3vN6tY9"
        "rH2cJ5dF8sA1mP4kL7qZ2nR5tW8yV3bH6cD9fG2aS5kM8pB1lQ4zX7vN0tY3rH8cJ1dF6sA4mP7kL0qZ5nR2tW9yV1bH4cD7fG0aS3kM6pB9lQ2zX5vN8tY1r"
        "H4cJ7dF0sA2mP5kL8qZ1nR4tW7yV0bH3cD6fG9aS2kM5pB8lQ1zX4vN7tY0rH3111"
    }

    @pytest.mark.parametrize("name", names)
    def test_create_user_with_different_username_str_length(self, name):
        data = self.prepare_registration_data(username=name)

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)

        assert_text = "long" if len(name) > 250 else "short"

        assert response.content.decode("utf-8") == f"The value of 'username' field is too {assert_text}", \
            f"Unexpected response content: {response.content}"