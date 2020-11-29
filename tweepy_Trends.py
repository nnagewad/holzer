import tweepy
import twitter_credentials
import random
import time, threading

auth = tweepy.OAuthHandler(twitter_credentials.API_KEY, twitter_credentials.API_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
locations = api.trends_available()

woeid_list = []
location_list = []

for location in locations:
    woeid_number = location['woeid']
    city_name = location['name']
    country_name = location['country']
    woeid_list.append(woeid_number)
    location_list.append(city_name + ", " + country_name)

WAIT_SECONDS = 1

def locationOutput():
    selected_location = random.choice(location_list)
    print(selected_location)
    threading.Timer(WAIT_SECONDS, locationOutput).start()

locationOutput()