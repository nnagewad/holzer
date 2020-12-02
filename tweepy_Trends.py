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
    city_name = location['name']
    country_name = location['country']
    woeid_number = location['woeid']
    if city_name == country_name:
        location_list.append(country_name + "woeid: " + str(woeid_number))
    else:
        location_list.append(city_name + ", " + country_name + "woeid: " + str(woeid_number))

WAIT_SECONDS = 1

def locationFunction():
    selected_location = random.choice(location_list)
    locationArray = selected_location.rsplit("woeid: ")
    print(locationArray[0])
    print(locationArray[1])
    threading.Timer(WAIT_SECONDS, locationFunction).start()

locationFunction()