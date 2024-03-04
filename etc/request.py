import requests
import json

target = "https://google.com"
response = requests.get(url=target)
print(response.text)

# user = {
#     "id" : "khlee",
#     "password": 1234,
#     "age" : 31,
#     "hobby": ["coding", "sleep"]
# }

# json_data = json.dumps(user,indent=4)
# print(json_data)