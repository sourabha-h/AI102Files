import requests
# pprint is used to format the JSON response
from pprint import pprint

import os

subscription_key = "2f0dfd2f37b44aef85e2dcc1c6368fd3"
endpoint = "https://azcogsvc.cognitiveservices.azure.com/"

language_api_url = endpoint + "/text/analytics/v3.0/languages"

documents = {"documents": [
    {"id": "1", "text": "This is a document written in English."},
    {"id": "2", "text": "Este es un document escrito en Español."},
    {"id": "3", "text": "这是一个用中文写的文件"}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)