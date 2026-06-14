import pytest
import requests

class TestForCookie:

    def test_for_cookie_request(self):

        response_for_cookie = requests.get("https://playground.learnqa.ru/api/homework_cookie", verify=False)
        print(dict(response_for_cookie.cookies))

        assert "HomeWork" in response_for_cookie.cookies, "There is no HomeWorkCookie in the response"
        print(dict(response_for_cookie.cookies))
