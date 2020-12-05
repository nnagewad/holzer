import tweepy
import twitter_credentials
import random
import time, threading
import os

auth = tweepy.OAuthHandler(twitter_credentials.API_KEY, twitter_credentials.API_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

locations = api.trends_available()

location_list = []

city_list = []
country_list = []

for location in locations:
    city_name = location['name']
    country_name = location['country']
    city_list.append(city_name)
    country_list.append(country_name)
