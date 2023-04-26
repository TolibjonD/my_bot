import requests
import json

BASE_URL = "http://saidqodirovchat.pythonanywhere.com/api/v1"


def create_user(username, name, user_id):
    url = f"{BASE_URL}/bot-users/"
    response = requests.get(url=url)
    data = json.loads(response.text)
    user_exist = False
    for i in data:
        if i["user_id"] == user_id:
            user_exist = True
            break
    if user_exist == False:
        requests.post(
            url=url, data={"username": username, "name": name, "user_id": user_id}
        )
        return "Foydalanuvchi yaratildi."
    else:
        return "Foydalanuvchi oldin yaratilgan."


def create_feedback(user_id, body):
    url = f"{BASE_URL}/feedbacks/"
    if body and str(user_id):
        requests.post(url=url, data={"user_id": user_id, "body": body})
        return "Adminga yuborildi fikringiz uchun taashakkur !..."
    else:
        return "Amal oxiriga yetmadi"
