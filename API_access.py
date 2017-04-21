import json

import tweepy
from tweepy import OAuthHandler

import config

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print (json.dumps(tweet) )

"""
# ця штука виводить 10 новин зі стрічки
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)


# зчитує якусь дивну і цікаву інформацію read our own timeline
# то саме що зверху тільки використовує json
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)
"""
# ця штука робить якісь посилання з фоточками list of all our followers/ тих на кого я підписаний
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)



