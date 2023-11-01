import requests
import os
from dotenv import load_dotenv
import json

# reading .env variables
load_dotenv()
API_KEY = os.getenv('TELEGRAM_API_TOKEN')
base_url = "https://api.telegram.org/bot"+API_KEY


def Read_message(offset):
    data = []
    parameters = {
        "offset": offset,
        "limit": 1
    }
    req = requests.get(base_url + "/getUpdates", data=parameters)
    data = req.json()
    return data


def sendPhoto(url, id):
    parameters = {
        "chat_id": id,
        "photo": url
    }
    resp = requests.get(base_url + "/sendPhoto", params=parameters)


def sendMessage(text, id, keyboard=[]):
    headers = {'Content-type': 'application/json'}
    reply_markup = {
         'keyboard': keyboard,
          'resize_keyboard': True,
          'one_time_keyboard': True
    }
    parameters = {
        'chat_id': id,
        'text': text,
        'reply_markup': reply_markup
    }
    resp = requests.get(base_url + "/sendMessage", data=json.dumps(parameters), headers=headers)
    print(resp.status_code)








# def sendMessage(text, id, keyboard=keyboardDefault):
#     headers = {'Content-type': 'application/json'}
#     parameters = {
#         'chat_id': id,
#         'text': text,
#         'reply_markup': {
#             'keyboard': keyboard,
#             'resize_keyboard': True,
#             'one_time_keyboard': True
#         }
#     }
#     response = requests.get(tUrl + "/sendMessage",
#                             data=json.dumps(parameters), headers=headers)


# def sendPhoto(image_path, chat_id):
#     image = Image.open(f'{image_path}')
#     print("image opened")
#     image.save(f'{outputPath}\\{filename}.jpg', 'JPEG', quality=80)
#     print("image saved")
#     imagePath = f'{outputPath}\\{filename}.jpg'

#     with open(imagePath, 'rb') as photo:
#         response = requests.post(
#             tUrl + "/sendPhoto", data={"chat_id": chat_id}, files={"photo": photo})
#         print(response)


# def getMessages():
#     response = requests.get(tUrl + "/getUpdates")
#     data = response.json()
#     return data


# def Read_input_message(chat_id, offset):
#     while True:
#         messages = getMessages()
#         if "result" in messages:
#             if messages["result"]:
#                 for message in messages["result"]:
#                     if chat_id == message["message"]["chat"]["id"]:
#                         input = message["message"]["text"]
#                         Read_message(offset)
#                         return input
#         else:
#             continue
