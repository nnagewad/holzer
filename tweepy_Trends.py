import tweepy
import twitter_credentials
import random
import time, threading
import os

auth = tweepy.OAuthHandler(twitter_credentials.API_KEY, twitter_credentials.API_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

locations = api.trends_available()

country_list = []
city_list = []

for location in locations:
    city_name = location['name']
    country_name = location['country']
    city_list.append(city_name)
    country_list.append(country_name)

country_list = list(dict.fromkeys(country_list))
city_list = set(city_list) - set(country_list)
city_list = list(city_list)

country_list.remove('')
city_list.remove('Worldwide')

def random_city():
    random_city = random.choice(city_list)
    print(random_city)

def random_country():
    random_country = random.choice(country_list)
    print(random_country)

def random_city_generator():
    os.system('clear')
    random_city = random.choice(city_list)
    print(random_city)
    random_count = random.randint(1,10)*.375
    threading.Timer(random_count, random_city_generator).start()

def random_country_generator():
    os.system('clear')
    random_country()
    random_count = random.randint(1,10)*.375
    threading.Timer(random_count, random_country_generator).start()

random_city_generator()
# random_country_generator()