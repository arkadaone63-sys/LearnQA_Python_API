import requests

response = requests.get("https://playground.learnqa.ru/api/get_text", verify=False)
print(response.text)


