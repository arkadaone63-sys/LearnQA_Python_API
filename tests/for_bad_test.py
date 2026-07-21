import requests
import pytest

class ForBadTest:

    user_agent_list = {
        "list_value_one": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "list_value_two": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
        "list_value_three": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "list_value_four": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "list_value_five": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }

    expected_params = {
        "params_of_list_one": {
            "platform": "Mobile",
            "device": "Android",
            "browser": "No"
        },
        "params_of_list_two": {
            "platform": "Mobile",
            "device": "iOS",
            "browser": "Chrome"
        },
        "params_of_list_three": {
            "platform": "Googlebot",
            "device": "Unknown",
            "browser": "Unknown"
        },
        "params_of_list_four": {
            "platform": "Web",
            "device": "No",
            "browser": "Chrome"
        },
        "params_of_list_five": {
            "platform": "Mobile",
            "device": "iPhone",
            "browser": "No"
        }
    }

    response_params_from_list = [
    (
        user_agent_list["list_value_one"],
        expected_params["params_of_list_one"]["platform"],
        expected_params["params_of_list_one"]["device"],
        expected_params["params_of_list_one"]["browser"]
    ),
    (
        user_agent_list["list_value_two"],
        expected_params["params_of_list_two"]["platform"],
        expected_params["params_of_list_two"]["device"],
        expected_params["params_of_list_two"]["browser"]
    ),
    (
        user_agent_list["list_value_three"],
        expected_params["params_of_list_three"]["platform"],
        expected_params["params_of_list_three"]["device"],
        expected_params["params_of_list_three"]["browser"]
    ),
    (
        user_agent_list["list_value_four"],
        expected_params["params_of_list_four"]["platform"],
        expected_params["params_of_list_four"]["device"],
        expected_params["params_of_list_four"]["browser"]
    ),
    (
        user_agent_list["list_value_five"],
        expected_params["params_of_list_five"]["platform"],
        expected_params["params_of_list_five"]["device"],
        expected_params["params_of_list_five"]["browser"]
    )
    ]

    USER_AGENT_DATA = ()
BASE_URL = "https://playground.learnqa.ru/ajax/api/user_agent_check"

# Сюда вставь ВСЕ строки из Gist в формате:
# ("User-Agent", "device", "browser", "platform")
USER_AGENT_DATA = [
    (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "iOS",
        "Safari",
        "веб"
    ),
    (
        "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",
        "Android",
        "Chrome",
        "веб"
    )
    # добавь сюда остальные строки из Gist по такому же шаблону
]

def run_tests():
    failed_cases = []  # сюда будем складывать ошибки

    for user_agent, expected_device, expected_browser, expected_platform in USER_AGENT_DATA:
        response = requests.get(
            BASE_URL,
            headers={"User-Agent": user_agent},
            verify=False
        )

        if response.status_code != 200:
            # Если сервер вообще не ответил нормально — считаем это ошибкой
            failed_cases.append({
                "user_agent": user_agent,
                "error": f"HTTP {response.status_code}"
            })
            continue

        data = response.json()

        errors_in_this_case = []

        # Проверяем device
        if data.get("device") != expected_device:
            errors_in_this_case.append(f"device: ожидалось '{expected_device}', пришло '{data.get('device')}'")

        # Проверяем browser
        if data.get("browser") != expected_browser:
            errors_in_this_case.append(f"browser: ожидалось '{expected_browser}', пришло '{data.get('browser')}'")

        # Проверяем platform
        if data.get("platform") != expected_platform:
            errors_in_this_case.append(f"platform: ожидалось '{expected_platform}', пришло '{data.get('platform')}'")

        # Если есть хоть одна ошибка — сохраняем этот случай
        if errors_in_this_case:
            failed_cases.append({
                "user_agent": user_agent,
                "errors": errors_in_this_case
            })

    # Вывод результатов
    if not failed_cases:
        print("🎉 Все User-Agent прошли проверку: сервер нигде не ошибся.")
    else:
        print(f"⚠️ Найдено {len(failed_cases)} User-Agent с ошибками:\n")
        for i, case in enumerate(failed_cases, 1):
            print(f"{i}. User-Agent: {case['user_agent']}")
            if "error" in case:
                print(f"   Ошибка: {case['error']}")
            else:
                for err in case["errors"]:
                    print(f"   - {err}")
            print()  # пустая строка для красоты

if __name__ == "__main__":
    run_tests()
