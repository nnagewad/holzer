import tweepy
import twitter_credentials
import random
import time, threading

auth = tweepy.OAuthHandler(twitter_credentials.API_KEY, twitter_credentials.API_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
locations = api.trends_available()

location_list = []

for location in locations:
    location_name = location['name']
    location_list.append(location_name)

WAIT_SECONDS = 1

def locationOutput():
    random_location = random.choice(location_list)
    print(random_location)
    threading.Timer(WAIT_SECONDS, locationOutput).start()

locationOutput()