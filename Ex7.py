import requests


response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", verify=False)
print(response.text)

response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", verify=False)
print(response.text)

payload = {"method": "POST"}
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload, verify=False)
print(response.text)


method_types = ["POST", "PUT", "PATCH", "DELETE", "GET", "HEAD", "OPTIONS"]
methods = [{"method": "GET"}, {"method": "POST"},
               {"method": "PUT"}, {"method": "PATCH"}, {"method": "DELETE"}, {"method": "HEAD"}, {"method": "OPTIONS"}]

for method_type in method_types:
    for method in methods:
            response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method, verify=False)
            print(response.status_code)
            print(response.request)
            print(response.text)

method_types = ["POST", "PUT", "PATCH", "DELETE", "GET", "HEAD", "OPTIONS"]
methods = [{"method": "GET"}, {"method": "POST"},
               {"method": "PUT"}, {"method": "PATCH"}, {"method": "DELETE"}, {"method": "HEAD"}, {"method": "OPTIONS"}]

for method_type in method_types:
       for method in methods:
            response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method, verify=False)
            print(response.status_code)
            print(response.request)
            print(response.text)

method_types = ["POST", "PUT", "PATCH", "DELETE", "GET", "HEAD", "OPTIONS"]
methods = [{"method": "GET"}, {"method": "POST"},
               {"method": "PUT"}, {"method": "PATCH"}, {"method": "DELETE"}, {"method": "HEAD"}, {"method": "OPTIONS"}]

for method_type in method_types:
       for method in methods:
            response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method, verify=False)
            print(response.status_code)
            print(response.request)
            print(response.text)

method_types = ["POST", "PUT", "PATCH", "DELETE", "GET", "HEAD", "OPTIONS"]
methods = [{"method": "GET"}, {"method": "POST"},
               {"method": "PUT"}, {"method": "PATCH"}, {"method": "DELETE"}, {"method": "HEAD"}, {"method": "OPTIONS"}]

for method_type in method_types:
       for method in methods:
            response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method, verify=False)
            print(response.status_code)
            print(response.request)
            print(response.text)

method_types = ["POST", "PUT", "PATCH", "DELETE", "GET", "HEAD", "OPTIONS"]
methods = [{"method": "GET"}, {"method": "POST"},
               {"method": "PUT"}, {"method": "PATCH"}, {"method": "DELETE"}, {"method": "HEAD"}, {"method": "OPTIONS"}]

for method_type in method_types:
       for method in methods:
            response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method, verify=False)
            print(response.status_code)
            print(response.request)
            print(response.text)

method_types = ["POST", "PUT", "PATCH", "DELETE", "GET", "HEAD", "OPTIONS"]
methods = [{"method": "GET"}, {"method": "POST"},
               {"method": "PUT"}, {"method": "PATCH"}, {"method": "DELETE"}, {"method": "HEAD"}, {"method": "OPTIONS"}]

for method_type in method_types:
       for method in methods:
            response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method, verify=False)
            print(response.status_code)
            print(response.request)
            print(response.text)

method_types = ["POST", "PUT", "PATCH", "DELETE", "GET", "HEAD", "OPTIONS"]
methods = [{"method": "GET"}, {"method": "POST"},
                  {"method": "PUT"}, {"method": "PATCH"}, {"method": "DELETE"}, {"method": "HEAD"},
                  {"method": "OPTIONS"}]

for method_type in method_types:
    for method in methods:
               response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method,
                                       verify=False)
               print(response.status_code)
               print(response.request)
               print(response.text)








#################################################################
# 1 запрос GET
# payload = {"method":["POST", "PUT", "PATCH", "DELETE", "GET"]}
# key = "method"
# value = "GET"
# response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload, verify=False)
#
# if value in payload[key]:
#     print(payload[key])
# else:
#     print(f"Неверный метод")
#
# print(response.status_code)
# print(response.request)
# print(response.text)

# if value in method[key]:
#     print(method[key])
# else:
#     print(f"Неверный метод")

###############################################################
# payload = {"method": "POST, GET, PATCH, PUT, DELETE, HEAD"}
# response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload, verify=False)
# print(response.text)
#
# payload = {"method": "POST, GET, PATCH, PUT, DELETE, HEAD"}
# response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload, verify=False)
# print(response.text)
#
# payload = {"method": "POST, GET, PATCH, PUT, DELETE, HEAD"}
# response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload, verify=False)
# print(response.text)
#
# payload = {"method": "POST, GET, PATCH, PUT, DELETE, HEAD"}
# response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload, verify=False)
# print(response.text)
#
# payload = {"method": "POST, GET, PATCH, PUT, DELETE, HEAD"}
# response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload, verify=False)
# print(response.text)
#
# payload = {"method": "POST, GET, PATCH, PUT, DELETE, HEAD"}
# response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload, verify=False)
# print(response.text)
#
# payload = {"method": "POST, GET, PATCH, PUT, DELETE, HEAD"}
# response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload, verify=False)
# print(response.text)
#
#
# method_types = ["POST", "PUT", "PATCH", "DELETE", "GET", "HEAD", "OPTIONS"]
# methods = [{"method": "GET"}, {"method": "POST"},
#            {"method": "PUT"}, {"method": "PATCH"}, {"method": "DELETE"}, {"method": "HEAD"}, {"method": "OPTIONS"} ]
