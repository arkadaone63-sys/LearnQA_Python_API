import requests
import time



response_1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", verify=False)
parsed_response_token = response_1.json()['token']
parsed_response_time = response_1.json()['seconds']

seconds = parsed_response_time
token = {'token': parsed_response_token}

time.sleep(seconds - 10)

response_2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token, verify=False)
parsed_status_2 = response_2.json()

if parsed_status_2.get('status') == 'Job is NOT ready':
    print(parsed_status_2['status'])
else:
    print(f"задача в процессе")

response_3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", verify=False)
parsed_response_token = response_3.json()['token']
parsed_response_time = response_3.json()['seconds']

seconds = parsed_response_time
token = {'token': parsed_response_token}
time.sleep(seconds + 1)

response_4 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token, verify=False)
parsed_status_4 = response_4.json()


if parsed_status_4.get('status') == 'Job is ready':
    print(parsed_status_4['status'])
else:
    print(f"задача в процессе")

if 'result' in response_4.text:
    print(response_4.text)
