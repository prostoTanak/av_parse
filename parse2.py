from datetime import datetime
import logging.config
import time
import json
import requests
import os
import yaml

req_token = requests.get('https://api.avito.ru/token/?grant_type=client_credentials&client_id=liyTTRM4Y1qoInlxrBZz&client_secret=__BVxVk-XcXVcsZ4lRvWOCJyfEoDKNhiO-9E7ebe')
data = json.loads(req_token.text)

to_yaml = {"token": data["access_token"]} #вставка в yaml файл ключ-значение

with open("token.yml", "w") as f:
    yaml.dump(to_yaml, f) # запись в файл

#print(data)

#определяем токен и заголовки
with open('token.yml') as f:
    token = yaml.safe_load(f)['token']

headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=token)
    }

url_users_info = "https://api.avito.ru/core/v1/accounts/"


def get_user_inf():
    url = url_users_info + "self"
    try:
        inf = requests.get(url, headers=headers)

        # попробовать тут получить с сылки на сайт информацию
        return json.loads(inf.text)
    except Exception as e:
        print(e)

print(get_user_inf())