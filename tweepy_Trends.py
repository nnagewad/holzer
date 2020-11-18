import tweepy
import random
import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.API_KEY, twitter_credentials.API_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

locations = api.trends_available()

woeid_list = []

for location in locations:
    # location_name = location['name']
    woeid = location['woeid']
    woeid_list.append(woeid)
    # print(location_name)
    # print(woeid)

random_woeid = random.choice(woeid_list)

trends = api.trends_place(id=random_woeid)

for value in trends: 
    for trend in value['trends']: 
        print(trend['name'])