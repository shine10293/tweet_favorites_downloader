import tweepy
import urllib.request
import json
import os

config_name = "config.json"
with open(config_name, "r", encoding="utf-8") as f:
    config = json.load(f)

consumer_key = config["consumer_key"]
consumer_secret = config["consumer_secret"]
access_token = config["access_token"]
access_token_secret = config["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user_name = config["user_name"]
count = api.me().favourites_count

i = 1

for like in api.favorites(screen_name=user_name, count=count):
    print(like)
    if 'media' in like.entities:
        for image in like.entities['media']:
            # picName = status.user.screen_name
            picName = "pic%s.jpg" % i
            i += 1
            link = image['media_url']
            filename = os.path.join("./favorite_images/", picName)
            urllib.request.urlretrieve(link, filename)

