#!/usr/bin/python3
from requests_oauthlib import OAuth1
import requests
api_key = "yOFiaBnu6qJYDfFWiXiwa80dN"
api_secret = "kn8jzWCF9AQkTXl3aQp79cd5PKqZct3gfW4aX3tiizd9w90UKv"
token = "3142731804-QKkbAyhi4RWj2UUW85CQ5OylhhOZEHQVLyX24cO"
token_secret = "pHIZ2WydnOtqnRf0eo6hBt47yWOrMz0f4VZHLB8nvgWXO"

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

pdic = {
        "count": 500,
        }


auth = OAuth1(api_key, api_secret, token, token_secret)
res = requests.get(url, params=pdic, auth=auth)
status_list = res.json()
for status in status_list:
    print(status["text"])

