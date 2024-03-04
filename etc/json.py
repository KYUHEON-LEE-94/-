import json

user = {
    "id" : "khlee",
    "password": 1234,
    "age" : 31,
    "hobby": ["coding", "sleep"]
}

with open("user.json", "w", encoding="utf-8") as file:
    json_data = json.dump(user, file, indent=4)