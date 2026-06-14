import pytest
import requests

class TestForHeader:

    def test_for_headers_request(self):

        response_for_headers = requests.get("https://playground.learnqa.ru/api/homework_header", verify=False)
        print(response_for_headers.headers)

        assert "x-secret-homework-header" in response_for_headers.headers, "There is no secret headers in the response"
        print(response_for_headers.headers.get("x-secret-homework-header"))