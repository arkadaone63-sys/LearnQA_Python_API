import pytest
from lib.base_case import BaseCase
from lib.my_requests import MyRequests

from lib.assertions import Assertions

class TestUserEditNegative(BaseCase):

    def test_edit_unauthorized(self):
        user_data = self.prepare_registration_data()
        create_resp = MyRequests.post("/user/", data=user_data)

        Assertions.assert_code_status(create_resp, 200)
        user_id = self.get_json_value(create_resp, "id")

        edit_payload = {"firstName": "NewName"}
        response = MyRequests.put(f"/user/{user_id}", data=edit_payload)

        assert response.status_code in [401, 403], (
            f"Awaiting status 401 or 403, but get {response.status_code}"
        )

    def test_edit_by_other_user(self):
        data1 = self.prepare_registration_data()
        r1 = MyRequests.post("/user/", data=data1)

        Assertions.assert_code_status(r1, 200)
        id1 = self.get_json_value(r1, "id")
        username1 = data1["username"]

        data2 = self.prepare_registration_data()
        r2 = MyRequests.post("/user/", data=data2)

        Assertions.assert_code_status(r2, 200)
        id2 = self.get_json_value(r2, "id")
        original_firstName2 = data2.get("firstName", "")

        login_resp = MyRequests.post("/user/login", data={
            "email": data1["email"],
            "password": data1["password"]
        })
        Assertions.assert_code_status(login_resp, 200)
        auth_cookie = self.get_cookie(login_resp, "auth_cookie")
        token = self.get_header(login_resp, "x-csrf-token")

        payload = {"firstName": "HackedName"}
        edit_resp = MyRequests.put(
            f"/user/{id2}",
            data=payload,
            headers={"x-csrf-token": token},
            cookies={"auth_cookie": auth_cookie}
        )

        assert edit_resp.status_code == 403, (
            f"Awaiting status 403 but get {edit_resp.status_code}"
        )



    @pytest.mark.parametrize("field,value,reason", [
        ("email", "bad-email.com", "email без символа @"),
        ("firstName", "A", "firstName длиной 1 символ (слишком короткий)"),
    ])
    def test_edit_invalid_field_values(self, field, value, reason):
        data = self.prepare_registration_data()
        create_resp = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(create_resp, 200)
        user_id = self.get_json_value(create_resp, "id")


        login_resp = MyRequests.post("/user/login", data={
            "email": data["email"],
            "password": data["password"]
        })
        Assertions.assert_code_status(login_resp, 200)
        auth_cookie = self.get_cookie(login_resp, "auth_cookie")
        token = self.get_header(login_resp, "x-csrf-token")

        payload = {field: value}
        edit_resp = MyRequests.put(
            f"/user/{user_id}",
            data=payload,
            headers={"x-csrf-token": token},
            cookies={"auth_cookie": auth_cookie}
        )

        assert edit_resp.status_code == 400, (
            f"[{reason}] Awaiting status 400 '{field}', "
            f"but get {edit_resp.status_code} (body: {edit_resp.text})"
        )

        get_resp = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_cookie": auth_cookie}
        )
        Assertions.assert_code_status(get_resp, 200)
        current_data = get_resp.json()

        if field == "email":
            # Если email не обновился, значит он остался прежним
            assert current_data.get("email") != value, (
                f"[{reason}] Field '{field}' has changed"
            )
        elif field == "firstName":
            # Аналогично для firstName
            assert current_data.get("firstName") != value, (
                f"[{reason}] Field '{field}' has changed"
            )
