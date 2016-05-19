#!/usr/bin/python3
from requests_oauthlib import OAuth1
import requests
api_key = ""
api_secret = ""
token = ""
token_secret = ""

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

pdic = {
        "count": 500,
        }


auth = OAuth1(api_key, api_secret, token, token_secret)
res = requests.get(url, params=pdic, auth=auth)
status_list = res.json()
for status in status_list:
    print(status["text"])

